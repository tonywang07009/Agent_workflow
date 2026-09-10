"""Local workflow index. No OpenSpec edits or claims about evidence contents."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
import uuid


SWITCH_AFTER = 5
STAGES = {"planned", "spec", "apply", "review", "archived"}


def fresh():
    return {"version": 1, "revision": 0, "mode": "change",
            "switch_offer": "not_offered", "workflows": {}}


def default_path():
    # Independent of project and CODEX_HOME, so all installed copies share it.
    return Path.home() / ".workflow" / "state.json"


def load(path):
    if not path.exists():
        return fresh()
    state = json.loads(path.read_text(encoding="utf-8"))
    if (not isinstance(state, dict) or state.get("version") != 1 or type(state.get("revision")) is not int
            or state["revision"] < 0
            or state.get("mode") not in {"change", "auto"}
            or state.get("switch_offer") not in
            {"not_offered", "pending", "accepted", "declined"}
            or not isinstance(state.get("workflows"), dict)):
        raise ValueError("Unsupported or invalid state; preserve it for recovery")
    for wid, workflow in state["workflows"].items():
        if not isinstance(wid, str) or not isinstance(workflow, dict):
            raise ValueError("Invalid workflow index; preserve it for recovery")
        if workflow.get("status") not in {"active", "completed"}:
            raise ValueError("Invalid workflow status; preserve it for recovery")
        if not isinstance(workflow.get("changes"), list):
            raise ValueError("Invalid changes; preserve state for recovery")
        if (not workflow["changes"] or workflow.get("knowledge_offer") not in
                {"not_offered", "pending", "accepted", "declined", "done"}
                or any(not isinstance(workflow.get(key), str) or not workflow[key].strip()
                       for key in ("goal", "repo_root", "openspec_root"))):
            raise ValueError("Incomplete workflow record; preserve state for recovery")
        for change in workflow["changes"]:
            if (not isinstance(change, dict) or change.get("stage") not in STAGES
                    or not isinstance(change.get("id"), str)
                    or not isinstance(change.get("original_path"), str)):
                raise ValueError("Invalid change record; preserve state for recovery")
        if workflow["status"] == "completed" and (
                not workflow.get("completed_at") or not workflow.get("completion_evidence")
                or any(c["stage"] != "archived" or not c.get("archive_path") or not c.get("evidence")
                       for c in workflow["changes"])):
            raise ValueError("Incomplete completion record; preserve state for recovery")
    return state


def count(state):
    return sum(w["status"] == "completed" for w in state["workflows"].values())


def view(state):
    return {**state, "completed_count": count(state),
            "switch_due": count(state) >= SWITCH_AFTER
            and state["switch_offer"] == "not_offered"}


def absolute(value, exists=None):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Expected a nonempty absolute path")
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise ValueError("Paths must be absolute: " + value)
    path = path.resolve()
    if exists == "dir" and not path.is_dir():
        raise ValueError("Missing directory: " + str(path))
    if exists == "file" and not path.is_file():
        raise ValueError("Missing evidence file: " + str(path))
    return str(path)


def evidence(items):
    if not isinstance(items, list) or not items:
        raise ValueError("At least one evidence file is required")
    return [absolute(p, "file") for p in items]


def normalize_record(data):
    if not isinstance(data, dict):
        raise ValueError("record must be an object")
    goal = data.get("goal")
    if not isinstance(goal, str) or not goal.strip():
        raise ValueError("A goal is required")
    result = {"goal": goal, "repo_root": absolute(data["repo_root"], "dir"),
              "openspec_root": absolute(data["openspec_root"], "dir"),
              "current_change": data.get("current_change"),
              "next_step": data.get("next_step", ""), "changes": []}
    context = data.get("project_context")
    if context is not None:
        if not isinstance(context, dict):
            raise ValueError("project_context must be an object")
        result["project_context"] = {
            "spec_path": absolute(context["spec_path"], "file"),
            "toolbox_path": absolute(context["toolbox_path"], "file"),
            "wiki_root": absolute(context["wiki_root"]),
        }
    if not isinstance(result["next_step"], str):
        raise ValueError("next_step must be text")
    changes = data.get("changes")
    if not isinstance(changes, list) or not changes:
        raise ValueError("Confirmed, nonempty change scope is required")
    ids, roots = set(), set()
    for change in changes:
        if not isinstance(change, dict):
            raise ValueError("Each change must be an object")
        cid, stage = change.get("id"), change.get("stage", "planned")
        if not isinstance(cid, str) or not cid.strip() or cid in ids or stage not in STAGES:
            raise ValueError("Invalid/duplicate change ID or stage")
        ids.add(cid)
        original = absolute(change["original_path"])
        if original in roots:
            raise ValueError("Duplicate change path")
        roots.add(original)
        archive = change.get("archive_path")
        refs = change.get("evidence", [])
        if not isinstance(refs, list) or any(not isinstance(p, str) for p in refs):
            raise ValueError("evidence must list file paths")
        if stage == "archived":
            archive, refs = absolute(archive, "dir"), evidence(refs)
            if archive == original:
                raise ValueError("Archive must differ from original path")
        elif archive is not None:
            archive = absolute(archive)
        deps = change.get("depends_on", [])
        if not isinstance(deps, list) or any(not isinstance(d, str) for d in deps):
            raise ValueError("depends_on must list change IDs")
        result["changes"].append({"id": cid, "original_path": original,
                                  "archive_path": archive, "stage": stage,
                                  "depends_on": deps, "evidence": refs})
    graph = {c["id"]: c["depends_on"] for c in result["changes"]}
    done = set()
    while len(done) < len(ids):
        ready = {cid for cid, deps in graph.items() if cid not in done and set(deps) <= done}
        if not ready:
            raise ValueError("Missing dependency or dependency cycle")
        done.update(ready)
    if result["current_change"] is not None and result["current_change"] not in ids:
        raise ValueError("current_change must belong to this workflow")
    return result


def apply(state, request):
    action = request["action"]
    if action in {"register", "checkpoint"}:
        wid = request.get("id") if action == "checkpoint" else str(uuid.uuid4())
        supplied = request["record"]
        if action == "checkpoint" and isinstance(supplied, dict) and "project_context" not in supplied:
            previous = state["workflows"][wid].get("project_context")
            if previous is not None:
                supplied = {**supplied, "project_context": previous}
        record = normalize_record(supplied)
        if action == "checkpoint" and state["workflows"][wid]["status"] != "active":
            raise ValueError("Completed workflows are immutable; do not recount")
        claimed = {c["original_path"] for c in record["changes"]}
        for other_id, other in state["workflows"].items():
            if other_id != wid and claimed.intersection(c["original_path"] for c in other["changes"]):
                raise ValueError("Change already belongs to another workflow; resume it")
        old = state["workflows"].get(wid, {})
        state["workflows"][wid] = {**record, "status": "active",
                                  "knowledge_offer": old.get("knowledge_offer", "not_offered")}
        return wid
    if action == "complete":
        workflow = state["workflows"][request["id"]]
        if workflow["status"] == "completed":
            return request["id"]  # Idempotent, including after paths later move.
        checked = normalize_record(workflow)
        if any(c["stage"] != "archived" for c in checked["changes"]):
            raise ValueError("All scoped changes must be verified, synced and archived")
        workflow.update(checked)
        workflow.update(status="completed", current_change=None, next_step="",
                        completion_evidence=evidence(request["evidence"]),
                        completed_at=datetime.now(timezone.utc).isoformat())
        return request["id"]
    if action == "offer-mode":
        if count(state) < SWITCH_AFTER or state["switch_offer"] != "not_offered":
            raise ValueError("Mode offer is not due")
        state["switch_offer"] = "pending"
    elif action == "answer-mode":
        if state["switch_offer"] != "pending" or type(request.get("accept")) is not bool:
            raise ValueError("A pending offer and explicit boolean answer are required")
        state["switch_offer"] = "accepted" if request["accept"] else "declined"
        if request["accept"]:
            state["mode"] = "auto"
    elif action == "set-mode":
        if request.get("mode") not in {"auto", "change"}:
            raise ValueError("Expected auto or change")
        state["mode"] = request["mode"]
        state["switch_offer"] = "accepted" if request["mode"] == "auto" else "declined"
    elif action == "knowledge":
        workflow = state["workflows"][request["id"]]
        choice = request.get("status")
        allowed = {"not_offered": {"pending"}, "pending": {"accepted", "declined"},
                   "accepted": {"done"}, "declined": {"accepted"}, "done": {"accepted"}}
        if workflow["status"] != "completed" or choice not in allowed[workflow["knowledge_offer"]]:
            raise ValueError("Invalid knowledge transition or unfinished workflow")
        workflow["knowledge_offer"] = choice
    else:
        raise ValueError("Unknown action: " + str(action))
    return None


def transact(path, request):
    """Exclusive lock plus revision check; never reset malformed or stale state."""
    if not isinstance(request, dict):
        raise ValueError("Request must be an object")
    path = Path(path).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name(path.name + ".lock")
    # Refuse contention; do not guess whether someone else's lock is stale.
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    temp = None
    try:
        os.close(fd)
        state = load(path)
        if type(request.get("expected_revision")) is not int or request["expected_revision"] != state["revision"]:
            raise ValueError("Stale revision; reread state and reconcile before retrying")
        wid = apply(state, request)
        state["revision"] += 1
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=path.name + ".", suffix=".tmp", delete=False) as output:
            temp = Path(output.name)
            json.dump(state, output, ensure_ascii=False, indent=2)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        os.replace(temp, path)
        return {"id": wid, **view(state)}
    finally:
        if temp is not None and temp.exists():
            temp.unlink()
        lock.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=default_path(), help="Override only for testing or explicit migration")
    parser.add_argument("--request", type=Path, help="UTF-8 JSON transaction; omitted means read-only")
    args = parser.parse_args()
    try:
        result = (transact(args.state, json.loads(args.request.read_text(encoding="utf-8-sig")))
                  if args.request else view(load(args.state)))
        # ASCII escapes keep JSON portable across Windows console code pages.
        print(json.dumps(result, ensure_ascii=True, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, "State unchanged; " + str(exc) + "\n")


if __name__ == "__main__":
    main()
