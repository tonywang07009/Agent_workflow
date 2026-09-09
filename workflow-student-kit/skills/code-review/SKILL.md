---
name: code-review
description: Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".
---

Two-axis review of the diff between `HEAD` and a fixed point the user supplies:

- **Standards** — does the code conform to this repo's documented coding standards?
- **Spec** — does the code faithfully implement the originating issue / PRD / spec?

Keep the axes separate. Use parallel subagents when available and permitted;
otherwise perform two focused passes with the same evidence and selected model.

Read the current project's applicable `AGENTS.md` and relevant Toolbox commands.
Resolve paths from that project, not this installed skill.

Every report labels relevant findings through three lenses without merging the
two axes:

- **Boundary** — inputs, outputs, state owner, failure mode, and non-goal are
  explicit and match the approved change.
- **Business logic** — each branch changing observable behavior, protocol
  state, or a data decision traces to an approved requirement or TDD acceptance
  criterion.
- **Readability** — names, control flow, and module ownership expose intent
  without hidden preconditions or unnecessary cross-file navigation.

OpenSpec is the canonical spec source. An issue tracker, if present, is mirror
evidence only and cannot add a requirement, schedule, or acceptance condition.

## Process

### 1. Pin the fixed point

Use the user's fixed point or infer it from approved change context when clear.
Ask only when ambiguous. Include staged and unstaged changes for a work-in-progress
review; a HEAD-only diff does not cover them.

Capture the diff command once: `git diff <fixed-point>...HEAD` (three-dot, so the comparison is against the merge-base). Also note the list of commits via `git log <fixed-point>..HEAD --oneline`.

Before going further, confirm the fixed point resolves (`git rev-parse <fixed-point>`) and the diff is non-empty. A bad ref or empty diff should fail here — not inside two parallel sub-agents.

### 2. Identify the spec source

For an OpenSpec change, read the source in this order:

1. The approved change `proposal.md`, `design.md`, and capability specification.
2. Its TDD acceptance links for code changes.
3. A path the user passed that supplements, but does not override, the OpenSpec record.
4. Mirror Issue data only to identify publication drift; never as a requirement source.

If no approved OpenSpec record exists, ask the user for the governing
specification. If none exists, the **Spec** sub-agent reports "no spec
available".

For a documentation or governance change, use its OpenSpec proposal/spec as the
source and inspect links, rule consistency, claim boundaries, parent task, and
approved revision traceability. Do not require a program test that the change
does not have.

For code, read the TDD contract and execute the relevant tests. Compare hashes
and frozen baselines only for designated protected high-risk tests. Ordinary
tests use version control and CI. Do not write or
modify a TDD test. Missing coverage for an existing acceptance condition returns
to TDD; a changed acceptance condition returns to OpenSpec.

Read the **Architecture-aware OpenSpec** section of `workflow.md` bundled
with the available `grill-with-docs` skill and apply its review checks. Resolve that
skill through the current skill catalog; do not assume a repository-local
installation or invoke its interview for already-settled decisions.

### 3. Identify the standards sources

Anything in the repo that documents how code should be written, such as `CODING_STANDARDS.md` or `CONTRIBUTING.md`.

On top of whatever the repo documents, the Standards axis always carries the **smell baseline** below — a fixed set of Fowler code smells (_Refactoring_, ch.3) that applies even when a repo documents nothing. Two rules bind it:

- **The repo overrides.** A documented repo standard always wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic ("possible Feature Envy"), never a hard violation — and, like any standard here, skip anything tooling already enforces.

Each smell reads *what it is* → *how to fix*; match it against the diff:

- **Mysterious Name** — a function, variable, or type whose name doesn't reveal what it does or holds. → rename it; if no honest name comes, the design's murky.
- **Duplicated Code** — the same logic shape appears in more than one hunk or file in the change. → extract the shared shape, call it from both.
- **Feature Envy** — a method that reaches into another object's data more than its own. → move the method onto the data it envies.
- **Data Clumps** — the same few fields or params keep travelling together (a type wanting to be born). → bundle them into one type, pass that.
- **Primitive Obsession** — a primitive or string standing in for a domain concept that deserves its own type. → give the concept its own small type.
- **Repeated Switches** — the same `switch`/`if`-cascade on the same type recurs across the change. → replace with polymorphism, or one map both sites share.
- **Shotgun Surgery** — one logical change forces scattered edits across many files in the diff. → gather what changes together into one module.
- **Divergent Change** — one file or module is edited for several unrelated reasons. → split so each module changes for one reason.
- **Speculative Generality** — abstraction, parameters, or hooks added for needs the spec doesn't have. → delete it; inline back until a real need shows.
- **Message Chains** — long `a.b().c().d()` navigation the caller shouldn't depend on. → hide the walk behind one method on the first object.
- **Middle Man** — a class or function that mostly just delegates onward. → cut it, call the real target direct.
- **Refused Bequest** — a subclass or implementer that ignores or overrides most of what it inherits. → drop the inheritance, use composition.

### 4. Spawn both sub-agents in parallel

Use two review agents when available and permitted; otherwise apply the briefs
below in separate passes without changing models.

**Standards sub-agent prompt** — include:

- The full diff command and commit list.
- The list of standards-source files you found in step 3, **plus the smell baseline from step 3** pasted in full — the sub-agent has no other access to it.
- The brief: "Report — per file/hunk where relevant — (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk. Label relevant findings Boundary, Business logic, or Readability. Distinguish hard violations from judgement calls — documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline. Skip anything tooling enforces. Under 400 words."

**Spec sub-agent prompt** — include:

- The diff command and commit list.
- The path or fetched contents of the spec.
- The brief: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Label each applicable finding Boundary, Business logic, or Readability. A behavior/protocol-state/data-decision branch without an approved requirement or acceptance link is a finding. Quote the spec line for each finding. Under 400 words."

If the spec is missing, skip the Spec sub-agent and note this in the final report.

### 5. Aggregate

Present the two reports under `## Standards` and `## Spec` headings, verbatim or lightly cleaned. Do **not** merge or rerank findings — the two axes are deliberately separate (see _Why two axes_).

End with a one-line summary: total findings per axis, and the worst issue _within each axis_ (if any). Don't pick a single winner across axes — that's the reranking the separation exists to prevent.

## Why two axes

For performance claims, require baseline/candidate revisions, controlled
workload and environment, warm-up, repeat count, raw samples and spread, and
the agreed regression threshold. One run or code coverage cannot prove
performance. Distinguish unit, integration, simulator, and hardware evidence.
Missing measurements support an unverified finding, not a PASS.

A change can pass one axis and fail the other:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**

Reporting them separately stops one axis from masking the other.
