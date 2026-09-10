# Resolve project context

Read this on first setup, a project switch, or a missing/conflicting mapping.
Use applicable AGENTS.md, then the workflow index's project_context. Explicit
user-selected context wins over a guessed default. Multiple matches require
selection; never use the newest file as an implicit project choice.

## Resource locations

In this source kit, docs/ and management/ are at the kit root. install.py copies
them to <target>/.agents/workflow-kit/docs/ and management/.
Resolve those paths from the target repository, not the original author's machine.
With a nonstandard skill installation, ask for the kit-resource location if it
cannot be found. A missing guide does not prove tool availability.

## First setup

1. Decompose the goal into evidence needs and scoped changes. Read the tool guide;
   choose only relevant capabilities and inspect their availability.
2. Locate existing OpenSpec with the installed CLI. If absent, explain the required
   initialization and use the current upstream setup only within authorization.
   Do not initialize OpenSpec in a teaching kit or a read-only reference.
3. Reuse existing project routing records where adequate. Otherwise adapt
   management/openspec-project/spec.md and toolbox.md into
   <actual-openspec-root>/projects/<project-key>/, using a stable scoped project key.
   This grouping is a kit convention, not a CLI schema or change ID.
4. Populate actual routes, commands, effects, fallback and acceptance. Replace
   placeholder values before execution. Correctness/completeness take priority.
   Preserve the CLI's feature spec/design/tasks paths and existing AGENTS rules.
5. Record absolute spec_path, toolbox_path and wiki_root under project_context in
   the workflow state request. The Wiki directory need not exist before consent.
   Merge management/AGENTS.md guidance only if target setup is in scope; never
   replace the whole existing file.
6. Show the goal, selected capabilities, contract paths and any unresolved choice.
   Continue already-decided work without adding a setup approval gate.

## Resume and direct skill invocation

Read the mapped spec/toolbox before choosing tools; obtain task counts and evidence
from actual change artifacts. Summary includes project contract and active change
paths. Indexes are navigation, not evidence. Correct verified moved references
directly and checkpoint them. Keep legacy state version 1 readable; enrich it when
context is resolved rather than resetting counts.

A directly invoked lower-level skill uses the same context via AGENTS or the
available workflow index, without starting unrelated workflow stages or registering
a second workflow. Outside workflow, use an explicitly selected existing project
contract or the project's own approved evidence rules. Missing context returns
to a narrow selection/clarification, not silent RedCap defaults.

## Ownership

AGENTS.md: root constraints and context selection.
Project toolbox.md: effective tools, fallbacks, commands and task packets.
Project spec.md: routing acceptance; feature specs stay with OpenSpec.
Skills: procedures and handoffs. Wiki: durable knowledge/evolution evidence.
Project records persist after change archives so completed-workflow curation can
resolve the original scope. Do not archive projects/ as though it were a change.
