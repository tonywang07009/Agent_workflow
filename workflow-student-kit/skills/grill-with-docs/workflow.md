# Shared Development Workflow

Use this reference when orienting a new project or resuming across stages.
It is a map, not an instruction to invoke every skill for every task.

| Need | Entry | Required result |
|---|---|---|
| Clarify intent | `grill-with-docs` | Goal, non-goals, observable acceptance, owner, and stop conditions. |
| Resolve architecture friction | `improve-codebase-architecture` | Scoped alternatives; existing owner reused or a justified interface change. `codebase-design` supplies design principles; `domain-modeling` resolves domain terms and relationships. |
| Control scope and progress | OpenSpec explore → propose → apply → sync → archive | Approved requirements, dependency-ordered tasks, evidence-linked completion, reconciled specs. |
| Implement behavior | `tdd` via OpenSpec apply | Intended RED failure → minimal GREEN → affected regressions; callers and tests cross the same interface. |
| Verify results | `code-review` and project validation commands | Separate Standards/Spec findings and measured outcomes with limitations. |

## Architecture-aware OpenSpec

Use these checks from specification writing through implementation and review.
Read `codebase-design` for module, interface, depth, seam, adapter, leverage,
and locality. Read the applicable domain glossary and ADRs; use
`domain-modeling` when terms or relationships need resolution. Scale the work
to the change: an existing adequate design needs only a reuse decision.

| Stage / artifact | Required result when relevant |
|---|---|
| Explore / proposal | Scope the affected behavior before scanning. Identify concrete friction and the existing owner. Apply the deletion test: complexity that disappears indicates a pass-through; complexity redistributed to callers indicates useful depth. Reuse the owner when it suffices. |
| Specs | Use canonical domain terms. State observable behavior, invariants, normal/refusal cases, and applicable edge cases. Keep implementation choices in design. |
| Design | Identify the owning module and its interface, including caller obligations, ordering, errors, and side effects. Explain seam placement, hidden complexity, and expected locality/leverage. For a proposed deepening, show a concise before/after and why deletion or reuse alone is insufficient. Do not invent an adapter merely to justify a seam; one adapter is hypothetical, two actual adapters establish real variation. |
| Tasks | Link acceptance scenarios to runnable checks through the same interface used by production callers. Order implementation by dependencies and preserve explicitly authorized RED-only stopping points. |
| Apply | After reading the CLI-resolved context files, check terminology, ownership, interface obligations, and the production/test entry against design. Use TDD for behavior changes. If evidence invalidates the design or acceptance, return to the affected artifacts before implementing the changed behavior. |
| Review | Under Spec, compare implementation and tests with the approved scenarios and interface decisions. Under Standards, assess ownership, locality, and unnecessary indirection against applicable guidance; label design heuristics as judgments. Keep the two axes separate. |

Use `improve-codebase-architecture` principles for scoped friction analysis.
Its full scan, temporary HTML report, candidate selection, and grilling loop
remain an explicit architecture-exploration route; ordinary OpenSpec work does
not automatically invoke that route or parallel interface-design agents.
Honor existing ADRs; identify evidence before proposing to revisit a decision.

Keep document authority distinct:

- `CONTEXT.md` (or the project's mapped glossary) holds resolved domain terms
  and relationships, without implementation details.
- OpenSpec specs hold behavioral requirements; `design.md` holds this change's
  design decisions; tasks link acceptance to implementation and evidence.
- Offer an ADR only for a hard-to-reverse, surprising decision with a real
  trade-off. Reuse existing records and follow project file-creation policy.

When integrating this workflow into a project's OpenSpec configuration, use
its existing `context` and per-artifact `rules` to reference these skills and
project records. Preserve schema templates and CLI-resolved artifact paths;
do not copy entire skills into configuration or every artifact. The propose,
apply, and review entrypoints read this section so the checks also apply when
invoked directly. Configuration changes require that project to be in scope.

Example: for a resource-admission change, specs define insufficient resources
and no send on refusal; design assigns admission to the existing owning module;
tasks exercise insufficient, exact, and excess capacity through the production
interface; apply and review verify refusal has no send side effect. This is an
acceptance example, not evidence that a particular implementation passes.

## Project authority and evidence

Read the current project's `AGENTS.md` first. It owns constraints and project-context selection. The selected OpenSpec
project's toolbox owns effective tools, fallbacks, commands and stop conditions. OpenSpec owns
requirements, design, and acceptance; issue trackers are mirrors when the project
uses that policy. Skills own procedure, not duplicate project rules.

Missing acceptance returns to clarification; changed acceptance returns to
OpenSpec; missing coverage returns to TDD; a failed check returns to diagnosis.
Resume approved work without repeating decisions. Preserve user-selected model
and effort. Size tasks to explicit interfaces and acceptance rather than model
brand. Do not lower evidence requirements for a weaker agent.

Follow project tool routing. Where none is defined, prefer an available indexed
symbol tool such as Symdex for relationships, RTK for scoped Git output, and
targeted filesystem reads for documents/logs. Verify availability; use native
Git or targeted source search when these optional tools cannot answer. Do not
install tools just to follow this map. Stop once the current question is answered.

For performance, predeclare metric, baseline, workload/environment, warm-up,
repeat count, aggregation/spread, and acceptance threshold. Keep raw evidence.
For token comparisons, hold task, revision, tokenizer/model and cache conditions
comparable. Record actual usage when available; returned bytes are only a proxy.
Never infer runtime correctness, physical performance, or token savings from
tool availability, successful compilation, or a checked task box.

Keep stable decisions in design and append run/review evidence to the project's
existing evidence records. Close only after required tests, review, and spec
reconciliation. Publishing, commits, or pushes need authorization for that scope.

## Knowledge handoff

Whole-workflow closeout offers llm-wiki. Each completed Wiki update passes bounded
sources and patterns to skill-evolution assess. Verified maintenance is repaired
directly; quality candidates use its evidence and stable local validation rules.
The evolution result is feedback to the originating Wiki record, not another
trigger. Keep project mappings in the available workflow skill's
[project-context guide](../workflow/references/project-context.md).
