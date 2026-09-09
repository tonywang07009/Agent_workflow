---
name: redcap-research-wiki
description: Maintain the English-first, source-backed RedCap research wiki when ingesting a bounded source pack, answering a research question, preparing a simulator decision contract, synchronizing an approved conclusion into documentation, triaging reusable knowledge capture, or checking wiki health.
metadata:
  input: Operation, research question or bounded source paths, target project, requested claim, and human approval state.
  output: Status, proposed paths, evidence paths, claim boundary, unresolved items, and next action.
  tool_dependencies:
    - validate_redcap_research_wiki
    - test_research_wiki_skill_evolution
  openspec_change: evolve-redcap-research-wiki-english-cases
---

# RedCap Research Wiki

## Load Contracts

1. Read `redcap_research_wiki/governance.md`.
2. Read `redcap_research_wiki/index.md`.
3. Read the target project's `project_plan.md` and `agent_rules.md`.
4. Read only the source records and pages required by the active question.
5. Read `redcap_library/redcap_doc_writer_skill/SKILL.md` only for an approved documentation-sync operation.
6. Resolve `validate_redcap_research_wiki` from `redcap_library/bash_tool/registry.json`.

Do not bulk-read historical PDFs or logs. Do not execute direct shell commands from this skill.
Write all authored prose, result envelopes, and templates in English. Preserve
raw titles, repository paths, commands, symbols, markers, and direct evidence
fragments verbatim.

## Select One Operation

| Operation | Required input | Required output |
|---|---|---|
| `ingest` | One bounded source pack | Source record and proposed affected pages |
| `query` | One research question | Cited answer, claim boundary, and optional page proposal |
| `decide` | Question, sources, configuration, markers | Completed simulator decision contract |
| `sync-docs` | Human-approved wiki conclusion and target docs | Existing bilingual documentation proposal |
| `lint` | Wiki root | Registered validator result and review findings |
| `capture-triage` | One completed bounded operation | `none`, `log`, `update-page`, `case-draft`, or `decision-contract` |

Reject mixed operations. Complete one bounded operation, report it, then accept the next task.

## Evolution Roles

| Role | Input | Authority | Output |
|---|---|---|---|
| Runner | One task and the active skill | Execute the active skill only | Bounded result envelope |
| Evolution Worker | One root cause, two representative traces, one reviewed wiki pattern or case, and one existing validation command | Propose one candidate only | Minimal skill diff or refusal |

### Water Spider Pull Rule

Qualify a proposal only when the same root cause observed at least twice has
positive and negative evidence. WIP = 1. The Water Spider is pull-only: it
does not edit wiki content, skill content, or active-skill state.

Refuse when the root cause is absent, the packet exceeds the stated envelope,
or either evidence polarity is missing. Do not create or activate a candidate.
Keep the active skill unchanged.

## Candidate Contract

Return exactly one candidate envelope:

```text
applicability:
counterexample:
stop_condition:
validation_command: registered_read_only_tool
rejection_reason: non-empty reason required
```

The candidate proposes a minimal diff only. Invoke only the registered read-only validation tool before review.
Only a human may promote a validated candidate by editing the active skill;
failure or incomplete evidence requires the rejection reason and keeps the
active skill unchanged.

## Ingest

1. Verify every source path and locator.
2. Search the index before creating a page.
3. Register the source without copying raw content.
4. Update an existing page when the material corrects or extends an existing concept.
5. Label every technical claim using the governance labels.
6. Keep new or changed synthesis `review-required`.
7. Update `index.md` and append an ingest entry to `log.md`.
8. Invoke `validate_redcap_research_wiki`.

## Query

1. Read the index and the smallest relevant page set.
2. Follow `source_refs` to authoritative sources when the answer depends on exact wording, current status, or runtime evidence.
3. Separate source statements, runtime observations, source traces, and inference.
4. Return `[Needs Verification]` when evidence is missing or ambiguous.
5. Propose a new page only when the answer will be reused.

## Decide

1. Start from `decisions/simulator-decision-contract.md`.
2. Fill every field before implementation or runtime execution.
3. Classify source endpoints as implemented/called, partial, dormant, definition-only, or missing.
4. Stop when the requested metric or markers cannot support the intended claim.
5. Return the contract as L3 `NEEDS_REVIEW`; do not start L4 work without explicit approval.

## Capture Triage

1. Classify the completed bounded operation as `none`, `log`, `update-page`,
   `case-draft`, or `decision-contract`.
2. Select `case-draft` only for a reusable finding with verifiable sources or
   evidence and a future consumer.
3. Use `cases/case-template.md` for a case draft; preserve `draft` or
   `review-required` until human review.
4. Use `decision-contract` before source modification or runtime execution.
5. Append a `capture` entry to `log.md` for the result.

## Synchronize Documentation

1. Require an approved wiki page with `status: confirmed`.
2. Use `redcap_library/redcap_doc_writer_skill/SKILL.md` for existing README and stable-document rules.
3. Update English and Traditional Chinese public pages together.
4. Preserve historical reports and their original evidence paths.
5. Invoke the registered documentation checker that owns the changed route.

## Lint

1. Invoke `validate_redcap_research_wiki`.
2. Report broken paths, missing metadata, unsupported labels, orphans, contradictions, and stale claims separately.
3. Propose mechanical fixes only. Never promote semantic content automatically.

## Return

```text
status: PASS | PARTIAL | BLOCKED | NEEDS_REVIEW
changed_or_proposed_paths:
evidence_paths:
claim_boundary:
unresolved_items:
next_action:
```
