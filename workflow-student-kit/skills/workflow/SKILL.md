---
name: workflow
description: Start or resume a development project spanning OpenSpec changes, with change-level checkpoints, progress summaries, local cross-project completion tracking, and an optional Skill/Wiki closeout.
---

# Workflow

One workflow is one user-scoped project containing one or more dependent OpenSpec
changes. Count it only when the entire development scope is complete. Tasks,
individual changes, conversations, and tool calls do not count as workflows.
Respond in the user's language. The user chooses model and effort.

## Teaching level

The first registered workflow for this local OS user receives full teaching;
later workflows receive brief prompts, regardless of completion count or repo.
Read the local index without writing before the entry interview to select the
level; no registered workflows means first use, even if mode preferences exist.
Follow [delivery.md](references/delivery.md#teaching-during-delivery) from the
opening overview through project closeout. Explain more whenever requested.
Persist level and delivered topic markers through [state.md](references/state.md#teaching-progress)
after scope-confirmed registration. Resume the same workflow's teaching progress
across conversations; do not repeat its opening lesson or completed explanations.
Status-only and mode-only requests do not launch teaching or consume first use.
Teaching never adds approvals or changes checkpoint mode or human acceptance.

## Start or resume

1. Begin a new workflow with `$grill-with-docs`. Read applicable `AGENTS.md`
   and only the existing records needed to ground the interview or distinguish
   a new workflow from a resume. Confirm intent, goal, non-goals, observable
   acceptance, owner, and stop conditions before project setup, registration,
   specification, or implementation. Ask one unresolved decision at a time and
   wait for its answer; reuse answers already supplied. On resume, do not repeat
   the interview or request reconfirmation. Re-enter `$grill-with-docs` only when
   the user introduces new requirements, and clarify their scope and impact before
   updating scope or implementing them. Status-only and mode-only requests skip
   the interview and perform only the requested operation.
2. Read applicable project `AGENTS.md` and follow its tool routing. Resolve skills
   from the active catalog or sibling folders in this bundle; load them as needed.
   Resolve the selected OpenSpec project's spec/toolbox through
   [project-context.md](references/project-context.md). Decompose the problem and
   consult the installed tool guide before selecting this project's capabilities.
3. Read [state.md](references/state.md) and query the local user index. Resolve the
   current project root. Resume its sole active workflow; ask which one if several
   exist; clarify a new project if none exists. Honor an explicit new-workflow
   request. With existing OpenSpec but no index, identify its scope before
   registering it; do not create duplicate changes.
4. Reconcile the index against CLI-resolved OpenSpec paths, tasks, validation,
   and archive evidence. Explain discrepancies before updating the index. Missing
   paths require investigation, not a completion claim or counter reset.
5. Before continuing, summarize in four to six lines: implementation goal,
   completed/total changes, current change's completed/total tasks and validation,
   next action, checkpoint mode, project spec/toolbox and actual change paths. Label unverified
   progress as such. Do not inspect other projects merely to build this summary.
6. Follow [delivery.md](references/delivery.md). Reuse settled decisions. Resume
   unfinished work directly. At a saved change boundary, a new bare `$workflow`
   invocation or request to continue authorizes the next change. A status-only
   request does not authorize implementation.

Example summary; replace paths and counts with verified values:

> Goal: deliver a shop with login, cart, and checkout.  
> Progress: 1/3 changes complete; cart tasks 2/4 complete; integration tests pending.  
> Next: implement quantity updates; pause after the whole cart change completes.  
> OpenSpec: `<project>/openspec/changes/shopping-cart/`.

## Checkpoints and closeout

- Default `change` mode: proceed through specification, implementation, review,
  validation, sync, and archive within one change. After implementation and
  validation, obtain human review acceptance for the delivered change; reuse
  explicit acceptance already given for that scope. After the change is complete
  and accepted, create or update the project's root `README.md` as its user manual
  and file guide, following [delivery.md](references/delivery.md#project-readme).
  Then report results, evidence, and the next change, and wait. Do not add other
  routine task or stage approvals.
- `auto` mode: continue into the next eligible change within the agreed scope.
  Both modes pause for unresolved decisions, additional authorization, missing
  required evidence, or blockers that cannot be resolved within scope. Diagnose
  and fix authorized failures before treating them as blockers.
  Human change acceptance and README closeout apply in both modes; automatic
  checks or agent reviews alone do not establish human acceptance.
- Complete the workflow once all scoped changes/tasks, required project-level
  acceptance, spec reconciliation, and archives are complete. Combine the last
  change report with project closeout. Count the same workflow ID only once.
- After **5 complete workflows across projects for this local user**, offer `auto`
  once at closeout. Persist a pending offer before asking. No answer preserves
  the current mode and pending question; remind on resume without treating it as
  a new offer. Declining suppresses future unsolicited offers; accepting switches
  modes. Explicit user requests can select either mode at any time and also
  settle this preference. See state.md for transitions and the threshold.
- After every complete workflow, follow [knowledge.md](references/knowledge.md)
  to offer Skill/Wiki work. This is independent of mode and completion count.
  If both questions are due, ask about mode first, then knowledge after the answer.

## Commands and boundaries

Understand `$workflow`, `$workflow build a booking system`, `$workflow status only`,
`$workflow switch to auto`, and `$workflow pause after each change`. For status or
mode-only requests, finish that operation without starting development.

Invocation does not expand scope or authorize commits, pushes, deployment, or
unrelated project edits. If OpenSpec CLI, a required skill, or index write access
is missing, identify the gap and next step. Do not silently install dependencies,
execute teaching snapshots, or claim unsaved progress is persistent.

For stage routing, skill replacement, storage, thresholds, and acceptance examples,
read [customization.md](references/customization.md). Leave teaching snapshots intact.
