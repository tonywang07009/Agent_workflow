## Purpose

Define the authoritative, evidence-bounded tool route for OAI repository work
and the governance boundary for changing that route.

## Requirements

### Requirement: Authoritative OAI tool routing

Root `AGENTS.md` SHALL define the authoritative required-first tool route and
fallback for an OAI task signal. The applicable `redcap_toolbox.md` task packet
SHALL define task-specific stop conditions and command references. Skills and
`redcap_toolbox.md` SHALL link to the root rule rather than duplicate it.
Source code, symbols, callers, callees, and repository structure SHALL use
Symdex first; Git status, diff, log, blame, branch, and commit lookup SHALL use
rtk first; Markdown, PDF, configuration, logs, generated artifacts, and file
content SHALL use filesystem MCP first. A fallback SHALL be reported with its
reason and MUST NOT replace a required Symdex lookup with `rg`.

#### Scenario: Router handles a source-navigation question
- **WHEN** an OAI request needs a symbol, caller, callee, or module owner
- **THEN** the route selects Symdex first and records a fallback only when
  Symdex cannot perform the lookup

#### Scenario: Router handles Git state
- **WHEN** an OAI request needs Git status, diff, history, blame, branch, or
  commit information
- **THEN** the route selects rtk first and records a fallback only when rtk
  cannot perform the operation

#### Scenario: Router handles repository evidence
- **WHEN** an OAI request needs Markdown, PDF, configuration, logs, generated
  artifacts, or ordinary file content
- **THEN** the route selects filesystem MCP first and records a fallback only
  when filesystem MCP cannot access the required path

#### Scenario: Router handles research-wiki work
- **WHEN** an OAI request queries or updates the research wiki
- **THEN** the route links to `CONTEXT.md` and `ASK_MATT_ROUTING_MEMO.md`
  without restating their rules

### Requirement: Tool-route governance boundary

`redcap_toolbox.md` SHALL treat tool availability, command examples, and
fallback corrections as direct maintenance. A change to a default route, stop
condition, or evidence threshold SHALL be an OpenSpec candidate requiring
human confirmation before application.

#### Scenario: A command example becomes stale
- **WHEN** an existing example or tool-health entry needs correction without
  changing a default route, stop condition, or evidence threshold
- **THEN** the toolbox can be updated directly

#### Scenario: A default route changes
- **WHEN** a proposed toolbox update changes a default tool route, stop
  condition, or evidence threshold
- **THEN** the router presents an OpenSpec candidate and waits for human
  confirmation before applying the change
