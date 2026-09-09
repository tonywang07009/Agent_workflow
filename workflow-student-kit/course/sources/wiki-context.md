# RedCap Research Wiki Context

## Context packet

A bounded task-start contract that identifies the question, wiki operation and
goal, required navigation pages, authoritative evidence sources, claim
boundary, autonomy level, completion evidence, stop conditions, and capture
route. It directs work without replacing an active project plan or an
authoritative raw source.

## Critical check

A conditional context-packet field for `query`, `decide`, and `case-draft`
work that records a counter explanation, discriminating evidence, and a
falsifier. It is not required for L0/L1 navigation, lint, or mechanical
maintenance work.

## Context-packet memo

| Field | Definition | Use |
|---|---|---|
| `question` | The exact bounded question. | Prevents unfocused reading. |
| `operation` | One of `query`, `decide`, `capture-triage`, or `sync-docs`. | Selects the workflow. |
| `goal` | The applicable G0-G7 execution contract. | Sets expected input, output, and completion evidence. |
| `system_scope` | The bounded system or project area. | Limits source navigation. |
| `required_pages` | Wiki pages to read before work begins. | Supplies curated terminology and known gaps. |
| `authoritative_sources` | Raw spec, paper, source, configuration, or retained evidence paths. | Supports technical claims. |
| `evidence_required` | Evidence types required for the question. | Prevents promotion across evidence tiers. |
| `claim_boundary` | Strongest conclusion the evidence can support. | Prevents overclaiming. |
| `autonomy_level` | Applicable L0-L4 boundary. | Limits agent actions. |
| `completion_evidence` | Observable output that completes the operation. | Defines done. |
| `stop_conditions` | Missing or conflicting evidence that stops work. | Prevents unsupported continuation. |
| `capture_route` | `none`, `log`, `update-page`, `case-draft`, or `decision-contract`. | Decides whether to retain the result. |
| `next_action` | The next owner, skill, or human review. | Makes handoff explicit. |
| `critical_check` | Counter explanation, discriminating evidence, and falsifier. | Required only for conclusion-bearing `query`, `decide`, or case-draft work. |

## RedCap DRL xApp glossary

| Term | Definition |
|---|---|
| Control Run | One bounded, auditable control attempt from preflight through `open`, `act`, `close`, and evidence capture. It creates one evidence package at start, including failed preflight, qualification, or model-input attempts that sent no UDS control. On either terminal outcome, it writes `finalized_at` and rejects later appends for that run ID. It excludes the Bridge-owned native lease, journal, and apply-proof mechanics. |
