# Validation record

Validated on 2026-09-10 on Windows with Python 3.12, Node 24 and Microsoft Edge.

| Check | Result |
|---|---|
| `python -B -m unittest discover -s tests` | 22 tests passed: workflow state, isolated installer and evolution evaluation CLI |
| `python -B verify.py` | Course data, local references, installation/refusal paths, package hashes and provenance checked |
| Official skill-creator `quick_validate.py` | workflow, llm-wiki and skill-evolution passed |
| PyYAML 6.0.3 | All 14 skill frontmatters and agent YAML files parsed |
| `node tests/test_course_browser.mjs <edge-path> course/current-preview` | 8 lesson dialogs, navigation, references, 10 nodes, mode demo, desktop/mobile width and absence of runtime exceptions passed |

Browser checks used a fresh headless Edge profile and offline file URLs. The
built-in browser could not initialize in this host; the approved external Edge
test provided rendered validation. Screenshots are in course/current-preview/;
the desktop course and desktop/mobile flow were visually inspected.

Tests use temporary projects. No live OpenSpec, Wiki, personal completion state
or active shared-skill candidate was created by these checks.

The evolution CLI checks hashes and declared evidence records. It does not judge
the content of evidence or measure agent quality. Real candidates need actual
project tasks, evidence review and the specified activation decision. Procedural
walkthroughs are documented in [skill-contracts.md](skill-contracts.md).
