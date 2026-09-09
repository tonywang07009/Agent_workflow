# Local user state

## Location and permissions

Default: Python `Path.home() / '.workflow' / 'state.json'`, typically
`C:\Users\<user>\.workflow\state.json` on Windows or `~/.workflow/state.json`
on macOS/Linux. This is this skill's index, not built-in Codex memory. All copies
share it for the same OS user, independent of repository, conversation, and
CODEX_HOME. There is no cross-device sync. Store references and preferences,
not credentials, full conversations, or raw test output.

Installation copies skills only; it never creates personal state. Read first:
missing state returns an empty index without writing. Register only after scope
is established. If home writes need sandbox permission, use the host approval
mechanism and identify the exact path. While unavailable, proceed with otherwise
authorized project work, but disclose that cross-session progress/counts were
not saved. Do not silently relocate state into the repo or bypass permissions.

## Helper interface

Use an available Python 3 executable. Resolve `<skill>` to this installed skill
and `<tmp>` to an allowed temporary directory:

```text
python "<skill>/scripts/state.py"
python "<skill>/scripts/state.py" --request "<tmp>/workflow-request.json"
```

Write requests as UTF-8 JSON files, avoiding shell interpolation of user text.
Before each mutation, read current state and use its `expected_revision`.
The helper uses an exclusive lock and atomic replacement. On revision conflict,
reread and reconcile instead of overwriting from a stale snapshot. Never remove
another writer's lock without establishing that it is abandoned. Preserve corrupt
or unsupported state for recovery; do not reset counts. `--state` is for isolated
tests or explicit migration, not routine per-project storage.

Read output includes revision, mode, switch_offer, workflows, derived
completed_count, and switch_due. Each completed workflow ID contributes one.
Use the helper for mutations; never manually increment the count or edit state.

## Register and checkpoint

Confirm scope and resolve the real OpenSpec root. Replace example paths with
absolute local paths. Planned change paths may not exist yet; verify them against
the CLI after creation. Project and OpenSpec roots must already exist.

```json
{
  "action": "register",
  "expected_revision": 0,
  "record": {
    "goal": "Deliver the shop",
    "repo_root": "/absolute/shop",
    "openspec_root": "/absolute/shop/openspec",
    "current_change": "login",
    "next_step": "Complete login specifications",
    "changes": [
      {
        "id": "login",
        "original_path": "/absolute/shop/openspec/changes/login",
        "archive_path": null,
        "stage": "spec",
        "depends_on": [],
        "evidence": []
      },
      {
        "id": "cart",
        "original_path": "/absolute/shop/openspec/changes/cart",
        "archive_path": null,
        "stage": "planned",
        "depends_on": ["login"],
        "evidence": []
      }
    ]
  }
}
```

Keep the returned UUID id for every resume. Do not register again on a new turn.
The helper rejects a change path already assigned to another workflow.

`checkpoint` takes the same full record, existing id, and latest revision.
Stages: planned, spec, apply, review, archived. Update only verified fields;
preserve all scoped changes unless the user explicitly changes scope.
current_change names the current or next change; next_step is a concrete action.
Checkpoint before pausing and at useful progress/interruption points.

Resolve paths from CLI/project evidence, not an assumed repo/openspec layout.
Preserve original_path after archive and record the actual archive_path. Evidence
references must point to files still reachable after archive, including tasks,
review, and validation records. Task counts are read live for summaries, not
cached in this index.

For a moved repo, identify the same workflow ID and checkpoint corrected active
paths rather than creating a duplicate. Completed records retain historical
locations. For later knowledge work, verify a user-provided path mapping and
document it in the output; do not fabricate historical paths.

## Completion and preferences

Every request also requires the latest expected_revision:

| Action and fields | Use |
|---|---|
| `complete`, `id`, `evidence: [absolute file paths]` | After verified change and project acceptance, sync, and archive. Checks existence/structure only, not evidence semantics. Completed records cannot be checkpointed. |
| `offer-mode` | When switch_due is true at closeout; saves pending before asking. Threshold: scripts/state.py SWITCH_AFTER = 5. |
| `answer-mode`, `accept: true/false` | Explicit answer to a pending offer. False preserves mode and suppresses future unsolicited offers. No answer means no request. |
| `set-mode`, `mode: "auto"/"change"` | Explicit user mode request, even before five completions. Settles preference without a later threshold prompt. |
| `knowledge`, `id`, `status: "pending"` | Before the first curation offer for a completed workflow. |
| `knowledge`, `id`, `status: "accepted"/"declined"` | Explicit answer. A declined/done record can become accepted again on a new explicit request. |
| `knowledge`, `id`, `status: "done"` | After accepted curation actually finishes. Does not affect delivery count. |

Example completion request, after checkpointing all archived changes:

```json
{
  "action": "complete",
  "expected_revision": 7,
  "id": "the-returned-workflow-uuid",
  "evidence": ["/absolute/shop/verification/project-acceptance.md"]
}
```

Persist pending before presenting a question so interrupted closeout is resumable.
On resume, also inspect closeout questions on this project's completed records.
If not_offered, finish that missed offer without recounting. Pending is neither
consent nor decline. Ask global mode first, then that workflow's knowledge question,
one at a time. An explicit request to do other work leaves the question pending;
do not block authorized work on an optional preference answer.
