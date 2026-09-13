# Skill responsibility and handoff audit

This records the user-approved kit change; it is not an active OpenSpec project.
Runtime context resolution belongs to workflow's project-context reference.
Design vocabulary belongs to codebase-design.

| Skill | Input interface | Output / next owner |
|---|---|---|
| workflow | Goal/resume and project context | New-workflow grill-with-docs interview before delivery; resume without reconfirmation unless the user adds requirements; verified summary, change checkpoint, closeout and curation offer |
| grill-with-docs | Unresolved decision and evidence | Goal/acceptance/owner/stop decision, returning to caller |
| codebase-design | Scoped interface question | Depth, seam, adapter, leverage and locality vocabulary |
| domain-modeling | Domain term or durable decision | Authorized existing glossary/ADR update |
| improve-codebase-architecture | Concrete friction and scope | Before/after candidates, then selected design discussion |
| openspec-explore | Question and existing records | Findings without unsolicited implementation |
| openspec-propose | Selected goal and acceptance | CLI/schema-resolved artifacts for apply |
| openspec-apply-change | Change and context files | Implemented tasks with validation/review or bounded blocker |
| openspec-sync-specs | Delta and canonical specs | Reconciled behavior; no duplicate tool route |
| openspec-archive-change | Complete change and evidence | Actual archive with verified code-trace.md; failed required sync blocks completion |
| tdd | Approved acceptance and public interface | RED/GREEN and affected regression evidence |
| code-review | Fixed point, current work and requirements | Separate Standards/Spec findings |
| llm-wiki | Project, operation and bounded sources | Knowledge update plus one evolution assessment |
| skill-evolution | Patterns, events, target and history | Maintenance/refusal/candidate/validation/promotion result |

## Architecture changes

- All skills resolve the selected project spec/toolbox without copying its route.
  The installed resource pack supplies the shared guide and management templates.
- Root AGENTS governs this kit; management holds inactive student templates.
  Actual tools and commands vary at the project toolbox seam.
- The architecture deletion test matches codebase-design: vanishing complexity
  favors deletion; complexity redistributed to callers indicates useful depth.
- OpenSpec exploration respects subsequent explicit implementation instructions;
  archive stops when required sync fails. Routine handoffs are not new approvals.
- TDD allows useful post-GREEN refactoring and existing acceptance records when
  the user explicitly excludes OpenSpec. Protected tests remain specifically scoped.
- Wiki/evolution share one bounded update/assessment identity. Feedback does not
  recurse. Candidates remain outside active discovery until user activation.
- The existing workflow state helper owns the optional project_context extension;
  legacy completion counts remain intact.
- The same helper assigns full teaching to the first registered workflow and
  brief prompts to later workflows, preserving per-workflow level and delivered
  topic markers on resume. Delivery owns explanation quality; teaching does not
  change checkpoint mode, human acceptance, or completion counts. Legacy records
  remain readable without inventing prior lessons.
- No router skill, speculative adapter or parallel implementation was added.
- Archive owns the per-change code trace format and path verification; workflow
  reports its archived location. The tree follows actual project paths and nesting,
  marks omitted branches, and links canonical acceptance without duplicating it.
- Workflow owns human change acceptance and the subsequent root README update
  after change completion. The README is the current project user manual and file
  guide; its actual tree and verified usage complement the archived code trace.
  Both checkpoint modes require this closeout and reuse existing human acceptance.

## Validation map

| Behavior | Check |
|---|---|
| Install resources without activating templates or overwriting settings | tests/test_install.py |
| Resume project context; preserve legacy counts | tests/test_workflow_state.py |
| Distinct current tasks, holdout, resource changes and regression refusal | tests/test_evolution.py through the actual evaluation CLI |
| Course data, local links and installed resources agree | verify.py / course/build.py |
| Offline Archify diagram, lesson dialogs, node focus/search/theme, page width | tests/test_course_browser.mjs with a fresh browser profile |

Manual contract walkthroughs:
- Missing SymDex uses only the declared fallback; no unsupported complete-call-graph claim.
- Verified archive moves are maintenance, not quality candidates.
- One quality event yields insufficient-evidence, while retaining the Wiki finding.
- Two same-root-cause events plus relevant positive/negative evidence may produce
  one isolated candidate; no active skill changes during assess.
- One task repeated twice is insufficient. Changed candidate resources require
  new version evidence. A current regression prevents readiness.
- Readiness is not activation: the target, version, user decision and rollback
  source are checked by promotion.
- Evaluation feedback updates the originating Wiki record without another trigger.

These walkthroughs check procedural consistency, not measured agent improvement.
Real candidates still require real task execution and evidence review.
