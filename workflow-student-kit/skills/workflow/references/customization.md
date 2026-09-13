# Customization and acceptance

## Editing map

| Change | Owner | Keep aligned |
|---|---|---|
| Invocation, resume summary, change checkpoint | SKILL.md | delivery.md handoffs and examples |
| Stage order, completion evidence, downstream skill | references/delivery.md | Actual available skills; do not copy their procedures |
| Human change acceptance and project README closeout | references/delivery.md | SKILL.md checkpoints; root README as user manual and file guide |
| First-workflow teaching and later brief prompts | references/delivery.md; scripts/state.py | SKILL.md; references/state.md teaching level and topic markers |
| Knowledge closeout | references/knowledge.md | Target project's Wiki governance, not teaching snapshots |
| Tool selection and project mapping | references/project-context.md; installed docs/tools.md | Active OpenSpec project spec/toolbox; source templates under management/ |
| Five-workflow threshold | scripts/state.py SWITCH_AFTER | SKILL.md, state.md, acceptance examples |
| State path, fields, migration | scripts/state.py, references/state.md | All installed copies share one protocol; migrate explicitly, never reset old data |
| Name, UI text, invocation example | SKILL.md frontmatter, agents/openai.yaml | Folder name and `$workflow` references |

Change delivery.md to change when review runs; change code-review to change how
review works. Use the target project's validation commands and document locations,
not hard-coded project paths. Link new references with a clear loading condition.
Roll back procedures by restoring the skill version, preserving user state.
Switching back to change mode does not require resetting completion history.

## Example requests

```text
$workflow Build a shop with login, cart, and checkout.
$workflow
$workflow Show the goal and progress only; do not implement.
$workflow Switch to automatic continuation between changes.
$workflow Pause after each complete change again.
```

Delivery requires OpenSpec CLI and the relevant bundled skills. The installer
includes llm-wiki, skill-evolution, and docs/management in .agents/workflow-kit;
it does not install CLI/MCP dependencies or configure project AGENTS.md.
Instructions are English; user-facing replies
follow the user's language.

## Acceptance scenarios

Run helper tests from the bundle root with
`python -B -m unittest discover -s tests`. They use temporary state, not personal
history. The following agent behaviors require practice-project execution;
string matching or JSON validity cannot prove them:

1. **New project:** begin with `$grill-with-docs` to confirm intent and scope for
   login, cart depending on login, and checkout. Ask one unresolved decision at a
   time and wait; do not set up the project, register the workflow, or begin specs
   or implementation before requirements are confirmed. Continue
   from login specs through implementation, review, sync, and archive. Pause
   after login; do not implement cart in change mode.
2. **Resume:** with cart tasks 2/4 complete, start a new conversation. First show
   goal, 1/3 changes, 2/4 tasks, validation status, and actual paths, then resume.
   Do not repeat the interview or ask for reconfirmation. Multiple active workflows
   require selection; status-only never interviews or implements.
3. **Counting:** three complete workflows in A plus two in B trigger the offer
   at the fifth closeout. An individual change, interruption, or failed project
   acceptance does not count. Repeating complete for the same ID adds nothing.
4. **Preference:** declining suppresses the sixth-closeout prompt. No answer
   preserves pending/current mode. Explicit auto continues across changes;
   explicit change restores checkpoints. Both preserve decision/permission gates.
5. **Knowledge:** offer only after all scoped changes complete. On consent,
   use actual OpenSpec original/archive/evidence paths and the real Wiki entry.
   With no Wiki, explain and offer a bounded summary; never execute snapshots.
6. **Recovery:** corrupt state, stale revisions, denied writes, and broken paths
   never reset counts or become success claims. Preserve recovery context and
   consult actual OpenSpec rather than treating the index as completion evidence.
7. **New requirements on resume:** the user adds coupons to the approved cart.
   Re-enter `$grill-with-docs` for coupon requirements and their impact, preserving
   settled cart decisions. Wait for unresolved answers before updating scope or
   implementing coupons, then continue delivery without another routine approval.
8. **Mode only:** switching checkpoint mode changes the preference without an
   interview or implementation.
9. **Project README:** in either mode, present completed implementation and
   validation for human acceptance. Pending/rejected review does not become
   acceptance through agent review or passing tests. Reuse explicit acceptance
   for the delivered scope. After sync/archive, create a missing root README or
   update the existing manual with current usage and an actual annotated file
   tree, preserving unrelated useful content. Verify links and applicable
   commands before reporting closeout or continuing. Resume an interrupted
   README update without repeating accepted review or archive.

10. **Teaching:** with no registered workflows, introduce the complete route before
    interviewing, then explain each stage's purpose/work/output before acting and
    its actual result/evidence/next step afterward. Persist delivered topic markers
    only after scope-confirmed registration. Resume that workflow across sessions
    without replaying lessons. A second workflow starts brief even if the first
    is unfinished. Expand a requested topic without resetting progress or adding
    approvals; an explicit ongoing preference changes only that workflow's level.
    Mode-only and status-only calls do not consume first use. Legacy history stays
    intact; absent teaching records are not proof of prior lessons.

Automated tests validate teaching defaults/persistence, the helper and installation.
They do not prove explanation quality or a real first-project teaching experience.
They do not establish full
agent orchestration, five real completed projects, or improved Wiki/skill quality.
