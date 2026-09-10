# Validation record

Validated on 2026-09-10 on Windows with Python 3.12, Node 24 and Microsoft Edge.

| Check | Result |
|---|---|
| `python -B -m unittest discover -s tests` | 22 tests passed: workflow state, isolated installer and evolution evaluation CLI |
| `python -B verify.py` | Course data, local references, installation/refusal paths, package hashes and provenance checked |
| Official skill-creator `quick_validate.py` | workflow, llm-wiki and skill-evolution passed |
| PyYAML 6.0.3 | All 14 skill frontmatters and agent YAML files parsed |
| `node tests/test_course_browser.mjs <edge-path> course/current-preview` | 8 lesson dialogs, navigation, references, 10 Archify nodes, focus/close, search, theme toggle, export menu, desktop/mobile page width and absence of runtime exceptions passed |

Browser checks used a fresh headless Edge profile and offline file URLs. The
built-in browser could not initialize in this host; the approved external Edge
test provided rendered validation. Screenshots are in course/current-preview/;
the desktop course and desktop/mobile flow were visually inspected.

## Archify regeneration

The user selected the adjacent local archify project, version 2.17.0-dev.1.
`course/workflow.archify.json` is now the maintained diagram source. The former
custom HTML template and its data file were replaced. Plain `course/build.py`
updates lessons only; `--archify-root ../archify` invokes the actual CLI delivery
and saves its receipt without modifying the generated artifact afterward.

```text
diagram_type: workflow
output: course/workflow.html
specification_sha256: c24b6c7fcf2ff9076a4d0c891928593d9b1837a1bb50001bcc51bb4356a9ad35
artifact_sha256: e10652825b49c9313241c3490550cfb28d77d48f00622e7f491b00333e99a6ad
validation: 9/9 showcase, 0 errors, 0 warnings
browser_evidence: passed
visual_review: passed (desktop scope)
correction_rounds: 0
```

Delivery evidence: course/workflow.delivery.json. Official automated evidence:
course/workflow.visual-check.json, generated with ARCHIFY_CHROME pointing to
the installed Edge executable. All four desktop measurements passed:
1440x900, 1600x1000, 1920x1080 and 2048x1320. Both endpoint sizes were captured
in light and dark themes. An image-capable reviewer inspected the light large
desktop, dark small desktop and embedded course screenshots; nodes, labels,
return branch and policy cards were legible without intersecting routes.
The initial layout validation rejected a backward mainPath; the corrected source
limits mainPath to the forward intake segment and preserves every delivery edge.
Unlabeled edges connect sequential steps whose action is stated by their nodes;
branch conditions retain explicit labels.

Mobile width checks measure document containment only. At 390px the Archify
viewer requires pan/zoom and part of its fixed toolbar falls outside the visible
area. Mobile visual completeness is not claimed. The generated runtime was left
intact; the course provides a direct standalone diagram link. Export-menu opening
was tested; exported-file quality was not tested.

Tests use temporary projects. No live OpenSpec, Wiki, personal completion state
or active shared-skill candidate was created by these checks.

The evolution CLI checks hashes and declared evidence records. It does not judge
the content of evidence or measure agent quality. Real candidates need actual
project tasks, evidence review and the specified activation decision. Procedural
walkthroughs are documented in [skill-contracts.md](skill-contracts.md).
