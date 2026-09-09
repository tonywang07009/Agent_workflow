# RedCap Research Wiki Governance

## Responsibilities

- Humans own research priorities, standards interpretation, evidence acceptance,
  and final engineering decisions.
- Agents own source registration, traceable synthesis drafts, cross-reference
  maintenance, capture triage, and mechanical checks.
- Each project plan remains the active-status source for its project.
- Raw sources remain authoritative for quotations and technical claims.

## Page Metadata

Every page under `sources/`, `concepts/`, `systems/`, and `decisions/` starts
with this metadata:

```yaml
---
status: draft | review-required | confirmed | superseded
source_refs:
  - repository/relative/path
evidence_tier: source-record | 3gpp | paper | runtime | source-trace | mixed | inference
last_reviewed: YYYY-MM-DD
related_pages:
  - repository/relative/wiki/path.md
---
```

Each case page also declares `case_id`, `case_type`, `system_scope`, and
`evidence_refs`. Valid case types are `resolved-problem`, `blocked-path`,
`experiment-learning`, and `doc-drift`.

`status` is editorial status; `evidence_tier` is evidence support. They are
independent. Only a human reviewer may promote a conclusion to `confirmed`.

## System-Page Contract

Each domain `overview.md` contains Scope, System Flow, Component Index, Current
State, Evidence Ladder, Repair Order, Course Route, Claim Boundary, and Open
Questions. Mermaid may explain a flow, but the Component Index is the canonical
portable navigation.

Each component page contains Role, Inputs and Outputs, Owner and Source Trace,
Implementation Status, Evidence and Markers, Failure Propagation, Repair
Inventory, Research Reading Card, Course Route, Claim Boundary, and Open
Questions. Create a component page only when a current source, project, manual,
or retained-evidence owner exists. Otherwise keep the component in its overview
as `[Needs Verification]`; do not create an empty page.

A component remains one file until it owns more than one maintained artifact.
Use repository-relative Markdown links so Git renderers and Obsidian work
without community plugins.

## Claim Labels

| Label | Meaning |
|---|---|
| `[3GPP Evidence]` | Supported by a verified local clause |
| `[Paper Evidence]` | Supported by cited paper pages, figures, or tables |
| `[Runtime Evidence]` | Observed in retained runtime evidence |
| `[Source Trace]` | Supported by current source ownership and caller/apply-path inspection |
| `[Inference]` | Synthesis, not a direct source statement |
| `[Needs Verification]` | Evidence is missing, ambiguous, release-dependent, or stale |

Do not promote one evidence tier into another. In particular:

- source readiness does not establish runtime behavior;
- attach, PDU session, tunnel, or ping does not establish a protocol-specific PASS;
- request acknowledgement does not establish local acceptance or application;
- an RFsim trend does not establish physical power or real-network equivalence.

## Capture Triage and Review Workflow

1. Register one bounded source pack.
2. Search `index.md` before creating a page.
3. Classify the reusable result as `none`, `log`, `update-page`, `case-draft`,
   or `decision-contract`.
4. Select `case-draft` only for a reusable finding with verifiable sources or
   evidence and a future consumer.
5. Update an existing page for a property or correction; create a case only for
   a reusable retrospective record.
6. Keep content changes at `draft` or `review-required`, list contradictions,
   missing evidence, and unclaimed conclusions, then obtain human review before
   promotion to `confirmed`.
7. Append the operation to `log.md`. Use `capture` for a capture-triage result.
8. Mark a replaced case `superseded` and link its successor; never rewrite its
   historical conclusion.

## Autonomy Boundaries

| Level | Boundary |
|---|---|
| L0 | Read-only queries and navigation |
| L1 | Mechanical proposals and checks; human approval before merge |
| L2 | Source-backed synthesis drafts; human approval for conclusions |
| L3 | Research or design proposals; human selects scope and acceptance criteria |
| L4 | Source/protocol changes or runtime campaigns; explicit human approval required |

## Context Gate

Create a context packet before a `query`, `decide`, `capture-triage` operation
that can produce a conclusion-bearing artifact, or `sync-docs` operation. Use
the field definitions in [CONTEXT.md](CONTEXT.md).

1. Classify the operation and the applicable G0-G7 goal.
2. Select the system scope, required wiki pages, and authoritative raw sources.
3. Set the evidence requirement, claim boundary, autonomy level, completion
   evidence, stop conditions, capture route, and next action.
4. Add a `critical_check` for conclusion-bearing `query`, `decide`, or
   case-draft work.
5. Execute the selected operation and return its required result envelope.

Do not create a context packet for L0/L1 navigation, lint, or mechanical
maintenance. A context packet directs evidence-bearing work; it does not
replace an active project plan or an authoritative raw source.

## Stop Conditions

Stop and return a review packet when standards text is missing or ambiguous,
sources conflict without a resolution criterion, a source path or version cannot
be verified, simulator markers do not support the requested claim, L4 work is
not approved, or a proposal would rewrite historical evidence.

## No-New-Infrastructure Rule

Use Markdown, Git, `rg`, and existing repository tools first. Add search
infrastructure only after measurements show index-based retrieval is inadequate.
