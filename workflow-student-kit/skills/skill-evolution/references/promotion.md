# Promotion and rollback

Local evaluation comes first. A stable candidate may be recommended for a local
active skill update and, if useful beyond the project, a separate shared update.
Two local tasks justify a recommendation, not a claim of universal improvement.

Before any activation:
1. Recheck eligibility, current-version stability and project-required review.
2. Resolve the exact active target, current contents and original baseline.
   If it changed since evaluation, stop for reconciliation and revalidation;
   do not overwrite intervening user edits.
3. Show the complete proposed diff, successful/failed task evidence, applicability,
   limitations, target path and rollback source.
4. Obtain or reuse explicit user authorization for this exact version and target.
   Wiki consent, assessment consent and a mode switch do not authorize activation.
   The host may separately require filesystem permission.
5. Apply only the reviewed change, verify the resulting files match the candidate
   and run required target checks. Preserve the original backup.
6. Append version, target, user decision, validation and result to evaluation.md
   and the originating Wiki log. An unchanged rejected candidate is not reoffered.

For a shared target, inspect the actual installed location and compatibility with
its callers. Do not assume it equals the local copy or write into a plugin cache.
Use the host's supported update path; missing support remains pending.

Rollback restores only this promoted version to its recorded prior version.
If the active target has later edits, reconcile first. Preserve Wiki evidence,
including failures and reasons; never erase the knowledge because skills revert.
