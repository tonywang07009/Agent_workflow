# Candidate evaluation

## Stability contract

Before execution, fix the baseline and candidate versions, two distinct
project-local task identities, acceptance/refusal cases, and pass criteria.
At least one task must not have been used to author the candidate.
A rerun of the same task is not a second task. Do not retrofit criteria to results.

Use comparable starting revisions, inputs, tools, model/effort and environment
for baseline and candidate. Invoke each explicitly through the same skill entry
the production agent uses, in separate isolated task runs without loading both
sets of instructions into one run. Do not pass the intended answer to an evaluator.
Side-effecting tests must remain within their authorized fixture scope.

For each task preserve commands, actual outputs, evaluator checks and limits.
Required correctness/completeness must pass with no required regression; the
targeted issue must improve against baseline. Record time/tokens only when
measured comparably; absent data is unknown, never zero.

A stable version passes two distinct tasks, including the held-out task.
Any candidate content/resource change invalidates prior stability evidence for
promotion. Keep old run history and rerun the current version. Do not invent new
project tasks merely to reach the threshold; wait for a suitable authorized task.

## Record and structural gate

Keep the human-readable comparison in evaluation.md and an evaluation.json
packet for the read-only helper:

```text
python "<skill-evolution>/scripts/evaluate.py" "<candidate-record>/evaluation.json"
```

The helper checks hashes, distinct tasks, held-out evidence and declared results.
It does not run an LLM, verify the truth of evaluation claims, or activate skills.
The agent/user must inspect the raw evidence and review the concrete diff.

Packet version 1 fields:
- project_root: actual project directory.
- baseline_dir, candidate_dir: complete isolated skill copies.
- baseline_hash, candidate_hash: helper's tree hashes; use --hash <directory>.
- runs: list of task_id, candidate_hash, baseline_hash, project_root,
  held_out (boolean), comparable (boolean), required_pass (boolean),
  no_regression (boolean), improved (boolean), evidence (nonempty local file paths).
- decision is not an input: a packet cannot approve itself.

All paths in a packet are absolute. Current-version runs determine readiness;
stale-version runs remain history. If any current-version run fails a required
condition, promotion is blocked until a new candidate version is evaluated.
Use more tasks when the risk or project acceptance requires them; two is a
minimum local stability gate, not proof of cross-project generalization.

Return validation-pending, rejected or promotion-ready with exact evidence links.
No user approval is inferred from a helper's successful exit.
