# Assessment eligibility

## Maintenance versus quality

Maintenance restores verified intent without changing behavior: a known archive
path, broken link, or demonstrable command typo. Check the source and repair,
then verify the target/result and log the reason. Do not wait for two events.
If the repair changes command effects, routing, acceptance or decision policy,
classify it as quality/policy work and resolve any undecided behavior first.

Quality evolution improves correctness/completeness in requirements, tool
evidence, implementation or validation. Time and token use are secondary.
Less text, more files, and a prettier report do not establish better quality.

## Candidate gate

Require all of:
- The same diagnosed root cause in at least two distinct observed events.
- Successful and failing evidence, each with a source and locator. A success
  must test the relevant condition, not an unrelated passing project.
- A specific target skill and a bounded behavior improvement with applicability
  and counterexample. Missing intended acceptance returns to clarification.
- A runnable baseline/candidate comparison using project toolbox commands and
  explicit evaluation authorization. Unavailable tools are a pending evaluation,
  never a simulated PASS.
- No other active candidate in this project's evaluation loop (WIP = 1).
  Finish, reject, or explicitly supersede it before creating another.

Outcome: maintenance / insufficient-evidence / no-change / candidate.
For a declined or failed proposal, inspect the prior reason first. New evidence
or a materially changed candidate is required before proposing it again.

## Proposal record

Create wiki/evolution/<candidate-id>/proposal.md only after eligibility:
assessment ID, project/workflow context paths, source pattern/event locators,
root cause, target skill's actual local path, baseline version/hash, candidate
version/hash, goal/non-goal, applicability/counterexample, minimal diff rationale,
planned held-out task, validation interface/commands, and stop/rollback conditions.
Snapshot the complete baseline skill resources and stage a candidate copy.
Do not change the active skill to create this record.

These thresholds are classroom decisions. WikiSkill supplies the separation of
evidence, knowledge, candidate and validation, not this exact event-count policy.
Source: [WikiSkill methodology](https://arxiv.org/html/2608.27454#S3).
