---
name: skill-evolution
description: Assess Wiki-backed skill quality improvements, validate isolated project-local candidates against the original, and prepare user-approved local or shared promotion after stable evidence.
---

# Skill Evolution

Input: mode (assess, evaluate, promote), project spec/toolbox, Wiki root, bounded
pattern/event evidence, target skill and prior history. Output: decision, reasons,
candidate/version, evidence, pending action and feedback to the originating Wiki.
Use the user's language for reports and the target skill's authored language.

Read project AGENTS.md and selected spec/toolbox. Read
[eligibility.md](references/eligibility.md) for assess,
[evaluation.md](references/evaluation.md) for evaluate, and
[promotion.md](references/promotion.md) for promote.
Resolve the target's actual project-local path; never silently edit an installed
global/plugin cache or another project's skill.

## Lifecycle

1. Assess every completed llm-wiki update using its update ID. Reuse the prior
   assessment if the same update resumes; do not create duplicate candidates.
2. Separate verified mechanical maintenance from quality evolution. Repair
   maintenance directly within authorization and verify it. No repeated-event
   threshold or activation vote is needed for unchanged semantics.
3. For quality work, require distinct repeated-root-cause events, successful and
   failing evidence, and a runnable comparison. Missing evidence returns a reason
   and the smallest next evidence task; do not create an empty candidate.
4. Produce one candidate for one skill, preserving the baseline and all relevant
   resources outside active skill discovery. Use codebase-design to assess the
   interface, locality and leverage. Reuse an existing owner; apply the deletion
   test; do not add an adapter without actual variation. Use available
   skill-creator guidance for authoring, not for deciding promotion.
5. Validate through the same invocation interface used by the agent, explicitly
   selecting baseline/candidate in separate permitted runs. Version changes reset
   stability evidence. Never describe structural validation as agent improvement.
6. Only a stable candidate can be recommended for promotion. Present evidence
   and concrete diff; the user decides activation. Local validation precedes
   any shared-skill recommendation. Honor exact target/version authorization.
7. Return outcomes to the originating Wiki log with links to evaluation records.
   Rejection or rollback preserves knowledge and the original skill. This
   feedback is not a new Wiki assessment trigger.

If the updater itself is the proposed target, preserve the original qualification
and promotion rules for this evaluation; a candidate cannot approve its own
weaker gate. Rule changes require a separate explicit user decision.
