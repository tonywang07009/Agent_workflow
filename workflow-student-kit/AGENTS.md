# Teaching kit rules

This repository distributes workflow skills, management templates, and an offline
course. It is not the original RedCap/OAI source repository.

## Ownership and source layout

- skills/: reusable procedures and their actual helper implementations.
- management/: project setup templates; never treat them as an active OpenSpec.
- docs/tools.md: shared tool capabilities, setup links and selection criteria.
- course/ and index.html: teaching content and offline interaction.
- install.py: installation; verify.py and tests/: package and behavior checks.
- course/sources/: historical read-only teaching snapshots, not active policy.

Modify the existing owner. Create files only for a concrete new responsibility.
Apply codebase-design depth, locality, deletion and interface-test principles;
do not introduce adapters or full scans without actual variation or friction.
See docs/skill-contracts.md for this package's responsibility and handoff audit.

## Tool routing for this kit

For Git inspection, use RTK when available, otherwise native Git and state why.
For source relationships, use SymDex MCP, then its available CLI; if unavailable,
inspect scoped source directly and state evidence limits. Text search alone is
not a complete caller graph. Read ordinary documents/configuration/logs directly.
Do not auto-install tools. docs/tools.md is a capability catalog, not health proof.

Student projects choose their own effective routes under their OpenSpec project
context using management/AGENTS.md and management/openspec-project/.
Do not activate copied project rules, create openspec/ or wiki/ here, or write
personal .workflow state while authoring/testing the kit. Use temporary fixtures.

## Work and verification

The user's approved task and recorded decisions govern this kit change; no
OpenSpec proposal is required for authorized teaching-package maintenance.
Keep English skill instructions and management templates; course explanations
and user reports may use Traditional Chinese. Preserve user-selected model/effort.

Run:
```text
python -B -m unittest discover -s tests
python -B verify.py
```

Use temporary roots for installers, project context and evolution tests. Do not
mark behavior proven from string checks. UI changes require rendered inspection
when browser capability exists; report unavailable checks accurately.
Update README, provenance and SHA256SUMS for delivered changes. Preserve upstream
source hashes; record adapted package hashes separately. Leave unrelated user files.

No commit, push, deployment, external messages or shared-skill activation unless
the user requests that scope. Existing authorization need not be requested again.
