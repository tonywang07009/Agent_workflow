"""Behavioral checks for local history, using isolated temporary repositories."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "skills/workflow/scripts/state.py"
spec = importlib.util.spec_from_file_location("workflow_state", SCRIPT)
state = importlib.util.module_from_spec(spec)
spec.loader.exec_module(state)


class WorkflowStateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.path = self.root / "user/state.json"

    def send(self, action, **fields):
        return state.transact(self.path, {"action": action,
                              "expected_revision": state.load(self.path)["revision"], **fields})

    def record(self, name="shop", changes=2):
        repo = self.root / name
        openspec = repo / "openspec"
        openspec.mkdir(parents=True, exist_ok=True)
        return {"goal": "Deliver " + name, "repo_root": str(repo),
                "openspec_root": str(openspec), "current_change": "change-0",
                "next_step": "Implement pending tasks", "changes": [
                    {"id": f"change-{i}", "original_path": str(openspec / "changes" / f"change-{i}"),
                     "stage": "apply", "depends_on": [f"change-{i-1}"] if i else []}
                    for i in range(changes)]}

    def archived(self, record):
        record = copy.deepcopy(record)
        for change in record["changes"]:
            archive = Path(record["openspec_root"]) / "changes/archive" / change["id"]
            archive.mkdir(parents=True, exist_ok=True)
            evidence = archive / "verification.md"
            evidence.write_text("Fixture evidence; no real project was executed.\n", encoding="utf-8")
            change.update(stage="archived", archive_path=str(archive), evidence=[str(evidence)])
        return record

    def finish(self, name):
        record = self.archived(self.record(name))
        wid = self.send("register", record=record)["id"]
        return self.send("complete", id=wid, evidence=record["changes"][0]["evidence"])

    def test_read_only_does_not_create_personal_state(self):
        result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--state", str(self.path)],
                                capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        self.assertEqual(data["completed_count"], 0)
        self.assertEqual(data["mode"], "change")
        self.assertFalse(self.path.parent.exists())

    def test_project_tool_context_is_preserved_on_resume_and_legacy_checkpoint(self):
        record = self.record()
        project = Path(record['openspec_root']) / 'projects' / 'shop'
        project.mkdir(parents=True)
        for name in ('spec.md', 'toolbox.md'):
            (project / name).write_text('Fixture contract', encoding='utf-8')
        context = {'spec_path': str(project / 'spec.md'),
                   'toolbox_path': str(project / 'toolbox.md'),
                   'wiki_root': str(self.root / 'shop/wiki')}
        record['project_context'] = context
        wid = self.send('register', record=record)['id']
        del record['project_context']
        saved = self.send('checkpoint', id=wid, record=record)
        self.assertEqual(saved['workflows'][wid]['project_context'], context)
        self.assertFalse(Path(context['wiki_root']).exists())
        self.assertEqual(saved['completed_count'], 0)

    def test_resume_persists_id_goal_paths_and_next_action(self):
        record = self.record()
        wid = self.send("register", record=record)["id"]
        record["next_step"] = "Resume cart task 3"
        record["current_change"] = "change-1"
        self.send("checkpoint", id=wid, record=record)
        result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--state", str(self.path)],
                                capture_output=True, text=True, check=True)
        saved = json.loads(result.stdout)
        self.assertEqual(list(saved["workflows"]), [wid])
        self.assertEqual(saved["workflows"][wid]["next_step"], "Resume cart task 3")
        self.assertEqual(saved["workflows"][wid]["goal"], record["goal"])
        self.assertEqual(saved["completed_count"], 0)

    def test_partial_change_and_missing_evidence_refuse_completion(self):
        record = self.record()
        wid = self.send("register", record=record)["id"]
        archived = self.archived(record)
        record["changes"][0] = archived["changes"][0]
        self.send("checkpoint", id=wid, record=record)
        before = self.path.read_bytes()
        with self.assertRaises(ValueError):
            self.send("complete", id=wid, evidence=record["changes"][0]["evidence"])
        self.assertEqual(self.path.read_bytes(), before)
        self.send("checkpoint", id=wid, record=archived)
        with self.assertRaises(ValueError):
            self.send("complete", id=wid, evidence=[str(self.root / "missing.md")])
        self.assertEqual(state.count(state.load(self.path)), 0)

    def test_cross_project_fifth_offer_decline_and_manual_modes(self):
        for i in range(5):
            result = self.finish(f"project-{i % 2}/workflow-{i}")
            self.assertEqual(result["completed_count"], i + 1)
            self.assertEqual(result["switch_due"], i == 4)
        pending = self.send("offer-mode")
        self.assertEqual(pending["mode"], "change")
        self.assertEqual(state.load(self.path)["switch_offer"], "pending")
        self.send("answer-mode", accept=False)
        sixth = self.finish("sixth")
        self.assertFalse(sixth["switch_due"])
        self.assertEqual(sixth["mode"], "change")
        self.assertEqual(self.send("set-mode", mode="auto")["mode"], "auto")
        restored = self.send("set-mode", mode="change")
        self.assertEqual(restored["completed_count"], 6)
        self.assertFalse(restored["switch_due"])

    def test_offer_requires_threshold_and_explicit_answer(self):
        with self.assertRaises(ValueError):
            self.send("offer-mode")
        with self.assertRaises(ValueError):
            self.send("answer-mode", accept=True)
        for i in range(5):
            self.finish(str(i))
        self.send("offer-mode")
        with self.assertRaises(ValueError):
            self.send("answer-mode", accept="yes")
        self.assertEqual(state.load(self.path)["mode"], "change")
        self.assertEqual(self.send("answer-mode", accept=True)["mode"], "auto")

    def test_retry_completion_and_duplicate_registration_do_not_recount(self):
        result = self.finish("shop")
        wid = result["id"]
        again = self.send("complete", id=wid)
        self.assertEqual(again["completed_count"], 1)
        self.assertEqual(again["workflows"][wid]["completed_at"], result["workflows"][wid]["completed_at"])
        with self.assertRaises(ValueError):
            self.send("register", record=self.record("shop"))
        with self.assertRaises(ValueError):
            self.send("checkpoint", id=wid, record=self.record("shop"))

    def test_knowledge_waits_for_full_workflow_and_never_counts(self):
        wid = self.send("register", record=self.record())["id"]
        with self.assertRaises(ValueError):
            self.send("knowledge", id=wid, status="pending")
        record = self.archived(self.record())
        self.send("checkpoint", id=wid, record=record)
        self.send("complete", id=wid, evidence=record["changes"][0]["evidence"])
        self.send("knowledge", id=wid, status="pending")
        with self.assertRaises(ValueError):
            self.send("knowledge", id=wid, status="done")
        self.send("knowledge", id=wid, status="declined")
        with self.assertRaises(ValueError):
            self.send("knowledge", id=wid, status="pending")
        self.send("knowledge", id=wid, status="accepted")
        result = self.send("knowledge", id=wid, status="done")
        self.assertEqual(result["completed_count"], 1)

    def test_stale_revision_and_busy_lock_preserve_other_writer(self):
        self.send("register", record=self.record())
        before = self.path.read_bytes()
        with self.assertRaises(ValueError):
            state.transact(self.path, {"action": "set-mode", "mode": "auto", "expected_revision": 0})
        self.assertEqual(self.path.read_bytes(), before)
        lock = self.path.with_name("state.json.lock")
        lock.write_text("another writer", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            self.send("set-mode", mode="auto")
        self.assertEqual(lock.read_text(), "another writer")
        self.assertEqual(self.path.read_bytes(), before)

    def test_corrupt_or_unknown_state_is_preserved(self):
        self.path.parent.mkdir(parents=True)
        for content in ["broken JSON", '[]', 'null', '{"version": 99}', '{"version": 1}']:
            self.path.write_text(content, encoding="utf-8")
            with self.assertRaises(ValueError):
                state.transact(self.path, {"action": "set-mode", "mode": "auto", "expected_revision": 0})
            self.assertEqual(self.path.read_text(), content)

    def test_replace_failure_leaves_valid_previous_state(self):
        self.send("register", record=self.record())
        before = self.path.read_bytes()
        with patch.object(state.os, "replace", side_effect=PermissionError("denied")):
            with self.assertRaises(PermissionError):
                self.send("set-mode", mode="auto")
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_missing_archive_and_cyclic_scope_are_rejected(self):
        record = self.record()
        record["changes"][0]["depends_on"] = ["change-1"]
        with self.assertRaises(ValueError):
            self.send("register", record=record)
        record = self.archived(self.record())
        record["changes"][0]["archive_path"] = str(self.root / "missing")
        with self.assertRaises(ValueError):
            self.send("register", record=record)

    def test_cli_writes_request_file_and_rejects_invalid_request(self):
        request = self.root / "request.json"
        record = self.record()
        record['goal'] = 'Shop \u5546\u5e97 \U0001f6d2'
        request.write_text(json.dumps({"action": "register", "expected_revision": 0,
                                      "record": record}), encoding="utf-8-sig")
        command = [sys.executable, "-B", str(SCRIPT), "--state", str(self.path), "--request", str(request)]
        first = subprocess.run(command, capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(first.stdout)["revision"], 1)
        self.assertEqual(next(iter(json.loads(first.stdout)['workflows'].values()))['goal'], record['goal'])
        before = self.path.read_bytes()
        retry = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(retry.returncode, 1)
        self.assertIn("Stale revision", retry.stderr)
        self.assertEqual(self.path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
