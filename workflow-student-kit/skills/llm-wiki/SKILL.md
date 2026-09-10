---
name: llm-wiki
description: Curate and query project-local, source-backed knowledge from bounded documents or completed workflow evidence, and assess every completed Wiki update for skill improvement.
---

# LLM Wiki

Input: operation (ingest, query, capture, lint), project context, question or
bounded source paths. Output: status, changed pages, verified source/evidence
paths, claim limits, evolution assessment and next action.
Respond in the user's language; authored Wiki records use the project's language.

Read applicable AGENTS.md and the selected OpenSpec project's spec/toolbox.
Resolve wiki_root from workflow project_context or an explicit project mapping.
Never infer it from this skill's installation directory. For workflow closeout,
require the user's accepted knowledge offer; direct Wiki requests authorize only
their specified scope. This is a local skill, not an integration with the
nashsu/llm_wiki desktop application.

## Procedure

1. Read [operations.md](references/operations.md) for the selected operation and
   [knowledge-model.md](references/knowledge-model.md) when creating/updating records.
2. Read the Wiki index if present, then only relevant pages and original sources.
   On first authorized write, create only the index, log and needed source/page
   records; do not prepopulate empty projects or copy entire private conversations.
3. Verify original/archive OpenSpec mappings, source locators, and evidence.
   Preserve raw results. Distinguish fact, inference, unverified claim and human
   confirmation; missing evidence narrows the claim instead of becoming PASS.
4. Apply justified updates to existing pages first, repair verified maintenance
   within scope, and update the index/log. Avoid a write when nothing changed.
5. After every completed content or maintenance update, invoke the sibling
   skill-evolution with the bounded handoff below in assess mode. This is part
   of the Wiki operation; do not ask again just to assess. No eligible candidate
   is a valid outcome. Queries and read-only lint without changes do not trigger.
6. Return the Wiki result plus assessment status. If evolution is unavailable,
   retain an assessment-pending log entry and report the gap; do not claim the
   combined operation is done. On resume finish that assessment before new writes.

## Handoff

Pass project root, project spec/toolbox paths, workflow ID when available,
Wiki root, changed pattern IDs/paths, source/evidence locators, assessment ID,
and any existing candidate/history links. The update ID also serves as the
assessment ID to avoid duplicate candidates across interrupted turns.

Skill-evolution returns maintenance / insufficient-evidence / no-change /
candidate / validation-pending / promotion-ready plus reasons and evidence.
Append its result to the same Wiki log entry; link evaluation records instead
of copying them. This bookkeeping does not trigger another assessment.
Raw evidence, Wiki knowledge and active skill instructions have different owners.

Do not activate a skill, mark a conclusion confirmed without the required human
review, or launch unbounded evaluations from a Wiki update.
