---
name: tdd
description: Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.
---

# Test-Driven Development

Read the current project's applicable `AGENTS.md` for tool routing and constraints.
Resolve project paths from that project, not from this installed skill.

TDD is the red → green loop. This skill is the reference that makes that loop produce tests worth keeping: what a good test is, where tests go, the anti-patterns, and the rules of the loop. Every section applies on every cycle — consult them before and during the loop, not after.

When exploring the codebase, read `CONTEXT.md` (if it exists) so test names and interface vocabulary match the project's domain language, and respect ADRs in the area you're touching.

## What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification — "user can checkout with valid cart" tells you exactly what capability exists — and survives refactors because it doesn't care about internal structure.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidelines.

## Seams — where tests go

A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside. Tests live at seams, never against internals.

## Boundary gate

Before writing any test, record the test boundary, acceptance condition, and
irreversible side effects. If all three are clear from the approved OpenSpec
revision, proceed. If any one is unclear, stop: do not create or modify a test
and start `$grill-with-docs` with the user. Resume only after its decision is
recorded in the OpenSpec/TDD contract.

Tests bind observable business outcomes, not private functions, internal data
structures, or incidental call order. For irreversible or security-sensitive
work, the observable contract includes effects such as no duplicate external
record, diagnosis without mutation, and no credential in output.

## Refusal-path tracer

When an approved refusal behavior is missing, incorrect, or newly required,
write a separate approved tracer before changing production code. Test the
public seam's exit code, human-readable reason, and absence of the specified
irreversible side effects. Do not modify an existing high-risk refusal-path
test to add this case; record its boundary and validation evidence.

Follow the current project's model-choice rules.
The user selects the model. Do not open a fallback subagent or infer a model
switch automatically.

## TDD contract

For a code change, record this contract in the change `design.md` before the
first test:

```md
## TDD contract

- Model / effort: <active model and effort, if exposed>
- Test boundary:
- Acceptance links:
- Irreversible side effects:
- Boundary gate: clear | grill-with-docs decision link
- Test files:
- Test evidence:
```

Each test name states a behavior, keeps
Arrange/Act/Assert readable, uses an independent expected value, and covers one
rule at a time.

Put behavior tests beside existing owner tests using the project's conventions.
Reuse project Toolbox commands where applicable. A documentation or governance change
uses a `Validation contract` in `design.md` instead of inventing a TDD test.

Use normal version control and CI for ordinary TDD tracers. Record a fixed
hash and make a test read-only only for a high-risk control or refusal case
where accidental mutation would invalidate safety evidence.

TDD authors may update a test only to cover an already approved acceptance
condition. A changed acceptance condition returns to OpenSpec.

## Anti-patterns

- **Implementation-coupled** — mocks internal collaborators, tests private methods, or verifies through a side channel (querying the database instead of using the interface). The tell: the test breaks when you refactor but behavior hasn't changed.
- **Tautological** — the assertion recomputes the expected value the way the code does (`expect(add(a, b)).toBe(a + b)`, a snapshot derived by hand the same way, a constant asserted equal to itself), so it passes by construction and can never disagree with the code. Expected values must come from an independent source of truth — a known-good literal, a worked example, the spec.
- **Horizontal slicing** — writing all tests first, then all implementation. Bulk tests verify _imagined_ behavior: you test the _shape_ of things rather than user-facing behavior, the tests go insensitive to real changes, and you commit to test structure before understanding the implementation. Work in **vertical slices** instead — one test → one implementation → repeat, each test a **tracer bullet** that responds to what the last cycle taught you.

## Rules of the loop

Before production edits, identify the existing owner and callers, reusable
path, interface, locality, and simplest sufficient change. Record material
decisions in the design contract. Escalate architecture review only for unclear
ownership, major seam changes, or an interface that cannot test the behavior.
This replaces the separate `implement` entrypoint.

Keep one acceptance condition per slice. Difficult state or concurrency work
needs counterexamples and focused review, not weaker acceptance. Use the user's
selected model and effort. Run affected build/type checks and regressions after
GREEN. Apply hash/read-only checks only to designated protected tests. Finish
with `code-review`; implementation does not authorize commit or push.

- **Red before green.** Write the failing test first, then only enough code to pass it. Don't anticipate future tests or add speculative features.
- **One slice at a time.** One seam, one test, one minimal implementation per cycle.
- **Refactoring is not part of the loop.** It belongs to the review stage (see the `code-review` skill), not the red → green implementation cycle.
