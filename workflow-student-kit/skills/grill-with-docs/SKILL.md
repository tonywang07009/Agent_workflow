---
name: grill-with-docs
description: Sharpen a repository-grounded plan or design through a one-question-at-a-time interview and retain conclusion-bearing results.
disable-model-invocation: true
---

# Grill With Docs

For a cross-project workflow overview, read [workflow.md](workflow.md). Skip
that reference for a single already-scoped decision.

Read the current project's applicable `AGENTS.md`. Follow its tool routing and
documentation governance; resolve project paths from that project, not this
installed skill. Read only relevant contracts, source, and evidence. Inspect
facts before asking the user; mark unsupported claims `[Needs Verification]`.

1. Establish goal, non-goals, observable behavior, owner, acceptance, and
   rollback/stop conditions. Resume settled decisions rather than restarting.
2. Ask one unresolved decision at a time, explain a recommendation, and wait
   for the answer. Use a concrete example or counterexample to test intent.
   Do not implement undecided behavior; existing explicit authorization stands.
3. Use `improve-codebase-architecture` for scoped candidates when ownership or
   testability is unclear. Skip a full review when the existing design suffices.
4. Retain agreed decisions in existing OpenSpec or decision records when
   requested. Follow project context gates for wiki updates. Use
   `domain-modeling` only for terminology or durable architectural decisions.
5. Use `openspec-explore` and `openspec-propose` for formal changes as needed.
   End with scope, acceptance, unresolved issues, and the next stage. Do not
   repeat approval already supplied by the user.

The user chooses model and effort. Size the evidence pack and decision to the
task; do not prescribe model names or automatic model-switch gates.
