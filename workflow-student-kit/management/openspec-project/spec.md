# Project tool-routing contract

Template: adapt for one scoped project at
<openspec-root>/projects/<project-key>/spec.md.
This contract covers tool use. Feature requirements remain in CLI-managed
change specs and canonical capability specs.

## Context

Fill project key, implementation goal, scoped change IDs/dependencies, actual
OpenSpec root, toolbox location, Wiki root and evidence location. Retain both
original and archive locations as changes complete. Values are project-local,
not global defaults. Confirm unresolved scope before dependent work.

## Requirements

### Requirement: Select tools from the problem

The agent SHALL decompose the task into required evidence and effects, consult
the tool guide, and select the applicable route in this project's toolbox.
A catalog entry SHALL NOT imply a tool is installed, healthy, or mandatory.

#### Scenario: Source relationship
- WHEN a task requires symbol ownership or callers
- THEN use this toolbox's source-navigation route and verify the relevant index
- AND report any permitted fallback and remaining relationship uncertainty

#### Scenario: Git inspection
- WHEN a task requires repository state or a diff
- THEN use this toolbox's Git route
- AND retain raw output if the selected proxy omits required evidence

#### Scenario: Ordinary document
- WHEN a known document or log answers the question
- THEN use the toolbox's permitted file-read interface without unrelated tools

#### Scenario: Missing capability
- WHEN a selected tool cannot provide required evidence
- THEN use only the declared fallback and report its limits
- AND stop dependent claims if the acceptance condition still cannot be verified

### Requirement: One effective project route

The toolbox SHALL own concrete tool choices, fallbacks, commands and task stop
conditions. AGENTS.md and skills SHALL reference it, not repeat competing tables.

#### Scenario: Two projects in one repository
- WHEN projects choose different tools
- THEN resolve the selected project by explicit mapping or workflow context
- AND do not apply the other project's toolbox

### Requirement: Evidence matches the claim

Validation SHALL observe the intended behavior through the caller's interface.
A build, checkbox, format check, or tool-health probe SHALL NOT replace behavior
acceptance. New routing/acceptance policy requires a user decision; verified
maintenance that preserves semantics may be corrected directly and logged.

#### Scenario: Known archive move
- WHEN evidence moved to a verified archive location
- THEN repair the link and check its target without waiting for repeated failures
- AND preserve the original/archive mapping and provenance

#### Scenario: Quality candidate
- WHEN experience suggests changing how a skill reasons or acts
- THEN route through skill-evolution and its local validation/promotion contract
- AND never treat routine maintenance or Wiki publication as candidate activation
