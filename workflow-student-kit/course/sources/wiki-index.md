# RedCap Research Wiki Index

## Governance

- [README](README.md) — entry point and operations.
- [Governance](governance.md) — metadata, evidence, review, capture, and stop rules.
- [Context Packet Memo](CONTEXT.md) — gate workflow and field definitions.
- [Ask Matt Routing Memo](ASK_MATT_ROUTING_MEMO.md) — OpenSpec gate, evidence escalation, and retained skill routes.
- [Agent Goals](agent_goals.md) — bounded operations and autonomy levels.
- [Activity Log](log.md) — append-only maintenance history.

## Sources

- [Karpathy LLM Wiki Pattern](sources/karpathy-llm-wiki-pattern.md) — source for cumulative derived knowledge structure.
- [Research Survival Guide PDF](sources/research-survival-guide.md) — research-method source record.
- [Active RedCap Projects](sources/active-redcap-projects.md) — active project-plan source records.

## Concepts

- [Evidence-First Research Method](concepts/evidence-first-research-method.md) — literature, criticism, synthesis, and innovation loop.

## Systems

### RedCap

- [RedCap System Map](systems/redcap/overview.md) — configuration-to-runtime overview, repair order, and course route.
- [Configuration and Capability](systems/redcap/configuration-capability.md) — gNB config, SIB1, and UE capability owners.
- [RRC and Access](systems/redcap/rrc-access.md) — access gate, capability exchange, and RedCap RA inputs.
- [BWP, RA, and Scheduling](systems/redcap/bwp-ra-scheduling.md) — initial BWP, CORESET, RACH, Msg2, and scheduler ownership.
- [Inactive, Power, and SDT](systems/redcap/inactive-power-sdt.md) — feature-separated RRC_INACTIVE, SDT, DRX, eDRX, and PSM route.
- [Runtime Evidence](systems/redcap/runtime-evidence.md) — retained RFsim evidence and capacity claim boundary.

### A-IoT

- [A-IoT System Map](systems/aiot/overview.md) — experimental Topology-2 flow, AIOTF, and blocked standard path.
- [Tag and UE Reader](systems/aiot/tag-reader.md) — CW, R2D/D2R, codec, wake gate, and diagnostic report.
- [AIOTF](systems/aiot/aiotf.md) — binding, scheduling, arbitration, NRF, and bounded Naiotf Inventory.
- [Standard-Path Boundary](systems/aiot/standard-path.md) — missing AMF/RAN/NEF owners and stop condition.

### xApp/dApp

- [xApp and dApp System Map](systems/xapp-dapp/overview.md) — decision-to-outcome evidence flow.
- [xApp Observation and Control](systems/xapp-dapp/xapp-observation-control.md) — metrics, selection, and RC request builders.
- [E2 Transport](systems/xapp-dapp/e2-transport.md) — transport, decode, and ACK boundary.
- [dApp Guard](systems/xapp-dapp/dapp-guard.md) — local policy and parameter-specific accept/reject owners.
- [gNB Apply and Rollback](systems/xapp-dapp/gnb-apply-rollback.md) — state mutation, snapshot, and rollback boundary.
- [Outcome Evidence](systems/xapp-dapp/outcome-evidence.md) — static-to-outcome evidence classification.

### Cross-domain

- [RFsim Performance Evaluation](systems/rfsim-performance-evaluation.md) — simulator evaluation knowledge route.

## Decisions

- [Simulator Decision Contract](decisions/simulator-decision-contract.md) — required contract before implementation or runtime execution.
- [GitHub Issue Mirror Format Context](decisions/github-issue-mirror-format-context-2026-08-15.md) — approved mirror fields, state boundary, and retention rule.
- [Pipeline Unified Approval Context](decisions/pipeline-unified-approval-context-2026-08-13.md) — independent approval and acceptance boundary.
- [TDD Observable-Behavior Boundary Context](decisions/tdd-observable-behavior-context-2026-08-13.md) — public behavior and implementation-boundary rule.

## Cases

- [Reusable Case Template](cases/case-template.md) — create one reusable case after capture triage selects `case-draft`.
- [CASE-2026-001: O-RAN G4 Report-Index Drift](cases/CASE-2026-001-oran-g4-report-index-drift.md) — project-local report index lagged the canonical G4 status and Gate report.
