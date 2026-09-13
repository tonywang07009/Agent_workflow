# Development delivery

## Scope and authority

For a new workflow, complete the entry interview with `$grill-with-docs` before
delivery: confirm intent, goal, non-goals, observable acceptance, ownership, and
stop conditions, asking one unresolved decision at a time and waiting for answers.
On resume, reuse confirmed requirements without another interview or confirmation.
Re-enter `$grill-with-docs` only for user-introduced new requirements; clarify their
scope and impact before updating scope or implementing them.
Identify the scoped changes, their goals, dependencies, and OpenSpec locations.
Include only user-confirmed scope, not every change found in the repository.
Confirm scope changes before updating the index and affected OpenSpec artifacts.

Project `AGENTS.md` owns constraints and context selection; the selected OpenSpec
project toolbox owns concrete tool routing. Read [project-context.md](project-context.md)
for setup or ambiguous mappings. OpenSpec owns requirements,
design, tasks, and acceptance. The user index owns navigation, resume hints, and
preferences. Do not copy entire skills into specifications.

This delivery contract requires OpenSpec in the target project. If the user
requests work without it, honor that request but do not claim that this workflow's
completion contract was met or add it to the five-workflow count.

## Teaching during delivery

Use the workflow's saved teaching level independently of `change`/`auto` mode.
In the first workflow, before the entry interview, introduce the complete route:
requirements interview, project context/setup, specification and design,
implementation and tests, review and human acceptance, spec sync and archive,
project README, and whole-project closeout with the optional knowledge offer.
Explain each stage's purpose, expected output, and where the user participates.
Introduce unfamiliar terms in plain language; skill names alone are not teaching.
Do not create setup, OpenSpec artifacts, or state before the confirmed-scope gate.

For each stage of a full-teaching workflow:
- Before acting, explain the problem being solved, planned work, expected files
  or evidence, and how those outputs feed the next stage. Tie it to this project.
- After acting, explain what actually changed, where to inspect the outputs,
  what establishes completion or remains unresolved, and why the next step follows.
  A failed or skipped stage gets an honest explanation, never a success recap.
- Cover every change's stages with project-specific explanations. Reuse terminology
  already taught; do not replay the whole overview at each change or tool call.

From the second registered workflow onward, use brief prompts stating the current
stage, immediate task, and next step; include relevant results/evidence in normal
completion reports. If the user asks to learn more, explain the current topic's
purpose, rationale, files, and a concrete example, then continue authorized work.
A one-topic question does not change the saved level. An explicit request for
more or less teaching throughout this workflow changes its saved full/brief level;
later new workflows still default to brief.

Save only explanations actually delivered, using the topic keys in state.md.
On resume, summarize current progress and continue missing explanations rather
than restarting the overview or rerunning finished work. Markers track teaching,
not implementation completion or human approval. Never omit a newly relevant
decision or current result solely because a related topic was taught earlier.
Explain at meaningful stage/decision boundaries, not every read/search command.
After explaining, proceed within existing authorization; wait only at existing
decision, permission, human acceptance, or change-mode boundaries. Do not ask
whether the user understood each explanation or wants to proceed after each one.

## Within each change

Process changes in dependency order, one at a time. Record a fixed Git comparison
point before implementation and identify existing user edits. If review scope
cannot be established reliably, clarify it without overwriting existing work.

| Stage | Skills when needed | Exit condition and handoff |
|---|---|---|
| Intent/design | Reuse the entry interview; `grill-with-docs` for user-introduced new requirements; `domain-modeling` for terminology; `codebase-design` for interfaces | Clear goal, acceptance, owner, interface, dependencies. Do not repeat confirmation on resume or at each change. Reuse adequate design; use `improve-codebase-architecture` only for concrete architecture friction. |
| Specification | `openspec-explore`, `openspec-propose` | CLI/schema-required implementation artifacts ready. Fill gaps in an existing change instead of creating a duplicate. |
| Implementation | `openspec-apply-change`, `tdd` | Acceptance-driven RED, GREEN, affected regressions for behavior changes. Document why TDD is inapplicable for other work and run relevant checks. |
| Review/validation | `code-review`, project validation commands | Address Standards and Spec findings; retain commands, results, limitations, and evidence paths. Reuse an applicable review already completed by apply. Present the completed implementation and validation evidence for human acceptance; reuse explicit acceptance for this delivered scope, but do not infer it from silence, passing checks, or agent reviews. If pending or rejected, retain the checkpoint and resolve feedback before proceeding. |
| Sync/archive | `openspec-sync-specs`, `openspec-archive-change` | Required tasks, artifacts, tests, and review complete; delta specs reconciled (or no delta); archive and verified `code-trace.md` exist and evidence remains reachable. |

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

Complete the project README step below before reporting the change boundary or
continuing to the next change. This applies in both `change` and `auto` modes.

Save original/archive paths, stage, evidence, current change, and next action before
reporting completion. Include the archived `code-trace.md` path in the evidence and
report; its format and verification belong to openspec-archive-change's
[code trace contract](../../openspec-archive-change/references/code-trace.md).
For example:

> Login is verified, reviewed, synced, and archived.  
> Evidence: `<actual file>`; archive: `<actual directory>`.  
> Project: 1/3 changes complete. Cart is next; waiting for you to continue.

In `change` mode, end the turn here. In `auto`, report and continue to the next
dependency-ready change. Before an interruption, checkpoint useful progress.
On resume, summarize and inspect actual tasks; do not rerun completed work or
restart settled interviews.

## Project README

After the change is complete, including sync/archive, and human review has passed,
create or update `README.md` at the selected project's root. This is the project's
current user manual and file guide, covering all delivered functionality rather
than only the latest change. Preserve useful existing content and the project's
documentation language and conventions. Update affected sections; create the
root README if absent, without generating a README for every directory.

Include the following where applicable to the project:

- Purpose, intended users, and main capabilities.
- Prerequisites, installation, configuration, and startup commands.
- Usage steps and examples, including expected inputs and outputs.
- An annotated directory tree and descriptions of the main bundled files,
  source modules, configuration, resources, tests, and documentation.
- Maintenance and validation commands and relevant usage limitations.

Derive the tree from the actual current project structure and verified code trace;
check archived paths against the current filesystem before reuse. Preserve real
names and nesting, annotate purposes, and mark omitted branches in a scoped tree.
Use project-relative links for portability. Explain behavior from inspected
implementation and acceptance evidence; a directory tree alone cannot establish
usage or call relationships. Keep per-change review history and detailed test
evidence in `code-trace.md`, linking it only where useful to the reader.

Check paths, links, and documented commands against actual project entry points,
and run applicable documentation validation. Report commands that could not be
executed as unverified. Do not claim README closeout until these checks finish;
report its path and validation with the change result. Resume a pending README
update directly without repeating accepted review or archiving the change again.

## Project completion

Checkboxes alone are insufficient. Verify each scoped change's artifacts, tests,
review, human acceptance, sync, archive, project README closeout, and required
cross-change acceptance. Return to affected
work when checks fail. Never remove unfinished scope merely to permit closeout;
cancellation or scope removal requires an explicit user decision.

Call `complete` as described in state.md, attaching project-level acceptance
evidence files. The helper checks structural conditions and file existence; the
agent must verify that their contents actually establish acceptance.

Repeat completion of the same ID is idempotent. New requirements after closeout
use a new workflow, without reusing already counted changes. Report project root,
all original/archive OpenSpec paths, validation summary, and cumulative count.
Then handle the mode and knowledge questions.
