# Development delivery

## Scope and authority

Establish goal, non-goals, observable acceptance, ownership, and stop conditions.
Use `grill-with-docs` for one unresolved decision at a time; reuse settled answers.
Identify the scoped changes, their goals, dependencies, and OpenSpec locations.
Include only user-confirmed scope, not every change found in the repository.
Confirm scope changes before updating the index and affected OpenSpec artifacts.

Project `AGENTS.md` owns constraints and tool routing. OpenSpec owns requirements,
design, tasks, and acceptance. The user index owns navigation, resume hints, and
preferences. Do not copy entire skills into specifications.

This delivery contract requires OpenSpec in the target project. If the user
requests work without it, honor that request but do not claim that this workflow's
completion contract was met or add it to the five-workflow count.

## Within each change

Process changes in dependency order, one at a time. Record a fixed Git comparison
point before implementation and identify existing user edits. If review scope
cannot be established reliably, clarify it without overwriting existing work.

| Stage | Skills when needed | Exit condition and handoff |
|---|---|---|
| Intent/design | `grill-with-docs`; `domain-modeling` for terminology; `codebase-design` for interfaces | Clear goal, acceptance, owner, interface, dependencies. Reuse adequate design; use `improve-codebase-architecture` only for concrete architecture friction. |
| Specification | `openspec-explore`, `openspec-propose` | CLI/schema-required implementation artifacts ready. Fill gaps in an existing change instead of creating a duplicate. |
| Implementation | `openspec-apply-change`, `tdd` | Acceptance-driven RED, GREEN, affected regressions for behavior changes. Document why TDD is inapplicable for other work and run relevant checks. |
| Review/validation | `code-review`, project validation commands | Address Standards and Spec findings; retain commands, results, limitations, and evidence paths. Reuse an applicable review already completed by apply. |
| Sync/archive | `openspec-sync-specs`, `openspec-archive-change` | Required tasks, artifacts, tests, and review complete; delta specs reconciled (or no delta); archive exists and evidence remains reachable. |

Load only needed stage references. The available `grill-with-docs/workflow.md`
supplies shared architecture/evidence principles, not a requirement to run every
skill on every task.

## Integrating downstream checkpoints

`workflow` carries the authorized change through its lifecycle. Downstream
messages such as "ready for apply" or "suggest archive" are handoffs: continue
to that stage without asking the user to repeat apply/archive. Pass the selected
change ID explicitly to avoid another selection prompt. Show sync differences;
authorization to complete the change includes necessary sync and archive.

This integrates routine handoffs only. Preserve explicit project requirements,
unresolved scope/behavior, and genuine permission boundaries. `auto` never bypasses
unsupported workspace-planning operations or missing acceptance evidence. Follow
current authorization and available tools for agent reviews; never claim an
unperformed review.

## Change boundary

Save original/archive paths, stage, evidence, current change, and next action before
reporting completion. For example:

> Login is verified, reviewed, synced, and archived.  
> Evidence: `<actual file>`; archive: `<actual directory>`.  
> Project: 1/3 changes complete. Cart is next; waiting for you to continue.

In `change` mode, end the turn here. In `auto`, report and continue to the next
dependency-ready change. Before an interruption, checkpoint useful progress.
On resume, summarize and inspect actual tasks; do not rerun completed work or
restart settled interviews.

## Project completion

Checkboxes alone are insufficient. Verify each scoped change's artifacts, tests,
review, sync, archive, and required cross-change acceptance. Return to affected
work when checks fail. Never remove unfinished scope merely to permit closeout;
cancellation or scope removal requires an explicit user decision.

Call `complete` as described in state.md, attaching project-level acceptance
evidence files. The helper checks structural conditions and file existence; the
agent must verify that their contents actually establish acceptance.

Repeat completion of the same ID is idempotent. New requirements after closeout
use a new workflow, without reusing already counted changes. Report project root,
all original/archive OpenSpec paths, validation summary, and cumulative count.
Then handle the mode and knowledge questions.
