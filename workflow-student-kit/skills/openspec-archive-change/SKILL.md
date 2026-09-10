---
name: openspec-archive-change
description: Archive a completed change in the experimental workflow. Use when the user wants to finalize and archive a change after implementation is complete.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.4.1"
---

## Project context

Use applicable AGENTS.md to resolve the selected project's OpenSpec spec/toolbox.
For missing or ambiguous mappings, read the available workflow skill's
[project-context guide](../workflow/references/project-context.md).
This resolves tools and evidence only; it does not start the workflow or repeat
settled decisions. Follow this skill's own scope after context is resolved.


## Host compatibility

Use the host's available question and progress tools; `AskUserQuestion`,
`TodoWrite`, and `Task` below are procedural roles, not required tool names.
If unavailable, ask directly, track progress in text, and perform the work
locally. Delegate only when authorized. Resolve artifact paths from the
installed OpenSpec CLI; fields such as `planningHome`, `artifactPaths`, and
`actionContext` may be project extensions. If absent, inspect the CLI
instructions and actual change paths rather than inventing values.


Archive a completed change in the experimental workflow.

**Input**: Optionally specify a change name. If omitted, check if it can be inferred from conversation context. If vague or ambiguous you MUST prompt for available changes.

**Steps**

1. **If no change name provided, prompt for selection**

   Run `openspec list --json` to get available changes. Use the **AskUserQuestion tool** to let the user select.

   Show only active changes (not already archived).
   Include the schema used for each change if available.

   **IMPORTANT**: Do NOT guess or auto-select a change. Always let the user choose.

2. **Check artifact completion status**

   Run `openspec status --change "<name>" --json` to check artifact completion.

   Parse the JSON to understand:
   - `schemaName`: The workflow being used
   - `planningHome`, `changeRoot`, `artifactPaths`, and `actionContext`: path and scope context
   - `artifacts`: List of artifacts with their status (`done` or other)

   If status reports `actionContext.mode: "workspace-planning"`, explain that workspace archive is not supported in this slice and STOP. Do not move workspace changes into repo-local archives or edit linked repos.

   **If any artifacts are not `done`:**
   - Display the incomplete-artifact list and STOP.
   - Do not archive a change whose canonical OpenSpec artifacts are incomplete.

3. **Check task completion status**

   Read the tasks file (typically `tasks.md`) to check for incomplete tasks.

   Count tasks marked with `- [ ]` (incomplete) vs `- [x]` (complete).

   **If incomplete tasks found:**
   - Display the incomplete-task count and STOP.
   - Do not archive a change whose implementation, validation, or review task
     remains incomplete.

   **If no tasks file exists:** STOP and request a task contract.

4. **Check canonical completion evidence**

   Verify approval in the form required by the current project's AGENTS.md and
   OpenSpec contract. Require an annotated tag only when that project mandates
   one. Verify applicable TDD and review evidence; frozen hashes apply only to
   designated protected high-risk tests.
   For a documentation or governance change, verify its validation contract and
   documentation/governance review result. Stop when any required evidence is
   absent. A GitHub Issue mirror is external projection evidence only: it does
   not block archive when it is absent or failed.

5. **Assess delta spec sync state**

   Use `artifactPaths.specs.existingOutputPaths` from status JSON to check for delta specs. If none exist, proceed without sync prompt.

   **If delta specs exist:**
   - Compare each delta spec with its corresponding main spec at `openspec/specs/<capability>/spec.md`
   - Determine what changes would be applied (adds, modifications, removals, renames)
   - Show a combined summary before prompting

   **Prompt options:**
   - If changes needed: "Sync now (recommended)", "Archive without syncing"
   - If already synced: "Archive now", "Sync anyway", "Cancel"

   If sync is selected or already authorized by workflow, invoke openspec-sync-specs for the selected change. Verify sync succeeds before archive; a failed sync stops the dependent archive. Perform locally unless delegation is available and authorized. Standalone explicit archive-without-sync is not workflow completion.

6. **Prepare the code trace**

   Create or refresh `code-trace.md` in the resolved `changeRoot` using
   [the code trace contract](references/code-trace.md). This is a kit closeout
   document, not an additional CLI/schema artifact. Use verified implementation,
   requirements, and validation evidence; preserve existing useful trace content.
   Prepare archive-local links for the actual destination selected below.

7. **Perform the archive**

   Create an `archive` directory under `planningHome.changesDir` if it doesn't exist:
   ```bash
   mkdir -p "<planningHome.changesDir>/archive"
   ```

   Generate target name using current date: `YYYY-MM-DD-<change-name>`

   **Check if target already exists:**
   - If yes: Fail with error, suggest renaming existing archive or using different date
   - If no: Move `changeRoot` to the archive directory

   ```bash
   mv "<changeRoot>" "<planningHome.changesDir>/archive/YYYY-MM-DD-<name>"
   ```

   After moving, verify `code-trace.md` and its local links at the actual archive
   location. Repair stale paths before reporting completion. If the move succeeded
   but verification failed, report the archive location and remaining issue;
   resume verification there rather than moving the change again.

8. **Display summary**

   Show archive completion summary including:
   - Change name
   - Schema that was used
   - Archive location
   - Final `code-trace.md` location and any explicit trace evidence limitations
   - Whether specs were synced (if applicable)
   - Note about any warnings (incomplete artifacts/tasks)

**Output On Success**

```
## Archive Complete

**Change:** <change-name>
**Schema:** <schema-name>
**Archived to:** the archive path derived from `planningHome.changesDir`/YYYY-MM-DD-<name>/
**Specs:** ✓ Synced to main specs (or "No delta specs" or "Sync skipped")

All artifacts complete. All tasks complete.
```

**Guardrails**
- Always prompt for change selection if not provided
- Use artifact graph (openspec status --json) for completion checking
- Stop on incomplete canonical tasks or missing approval, validation, or review evidence
- Do not require a live GitHub Issue mirror for archive
- Preserve .openspec.yaml when moving to archive (it moves with the directory)
- Show clear summary of what happened
- If sync is requested, use openspec-sync-specs approach (agent-driven)
- If delta specs exist, always run the sync assessment and show the combined summary before prompting
