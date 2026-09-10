# Knowledge records and ownership

Use existing project locations. Default only after resolving project scope:

```text
wiki/
  index.md
  sources/<source-id>.md
  patterns/<pattern-id>.md
  log.md
  evolution/<candidate-id>/
    proposal.md
    baseline/
    candidate/
    evaluation.md
    evaluation.json
```

Create records lazily. Baseline/candidate hold the relevant complete skill
resources; they are not installed under an active skills directory.

## Source record

Record source ID, project/workflow, original location, current archive location
if moved, revision/date, exact locator (page/section/line/test case), evidence
path, and limitations. Link existing raw logs rather than duplicating them.
For remote sources retain the URL, accessed date and needed locator. Sensitive
inputs are not required as examples; use bounded reproducible fixtures.
Do not collect hidden reasoning; use observable actions, outputs and user decisions.

## Pattern record

Record pattern ID/title, status (draft/review-required/confirmed), observation,
root-cause hypothesis, applicability, successful and failing event references,
counterexample, falsifier, source IDs, affected skill if known, and review decision.
Two events must be distinct observations, not the same log cited twice.
A confirmed label requires the project's actual human decision; software lint
does not supply it. Evidence can later refute a confirmed pattern: annotate and
supersede the conclusion instead of rewriting historical results.

## Index and update log

Index: topic -> page -> relevant source IDs.
Log: update/assessment ID, scope, changed paths, source references, maintenance
repairs, assessment outcome/reason, candidate link, pending action and timestamp.
Preserve rejection reasons so an unchanged failed candidate is not proposed again.

## Evolution link

The skill-evolution skill owns proposal/evaluation record contents. Wiki links
to them and retains outcome summaries. Promotion/evaluation feedback appends to
the originating update; it does not recursively trigger another evaluation.
Later independent evidence may trigger a new assessment referencing the old one.
