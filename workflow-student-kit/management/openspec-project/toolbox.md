# Project toolbox

Template: fill for one project under its actual OpenSpec root. Do not execute
placeholder commands. Keep this file with the adjacent routing spec after
individual changes are archived; it describes the whole project's tool choices.

## Project mapping

| Field | Value to resolve |
|---|---|
| Project key / goal | Confirmed project scope |
| Project root / OpenSpec root | Absolute paths resolved on this machine |
| Scoped changes / dependencies | Actual CLI-resolved IDs and locations |
| Source / glossary / ADR locations | Existing project-owned locations |
| Wiki root | Project-local persistent knowledge location |
| Evidence root | Existing logs/reports location |
| Generic tool guide | Installed .agents/workflow-kit/docs/tools.md or kit source |
| Routing contract | Adjacent spec.md |

## Effective route

Populate selected rows after decomposing the problem; omit irrelevant tools.
This table is the sole owner of concrete routing for this project.

| Task signal | Selected interface/tool | Why it fits | Probe and result/date | Allowed fallback | Stop when |
|---|---|---|---|---|---|
| Source relationships, if needed | Select SymDex MCP/CLI or verified project interface | Needed relationship evidence | Check repo/index/version | Declare explicitly | Required relationship remains unverified |
| Git inspection, if needed | Select RTK or project Git interface | Scoped state/diff evidence | Check supported invocation | Declare explicitly | Diff scope or required output is unavailable |
| Files/documents | Select permitted direct read or filesystem MCP | Known source content | Check target access | Declare explicitly | Required source cannot be read |
| Specification lifecycle | Installed OpenSpec CLI | Canonical change artifacts | Inspect version/help/status | Existing supported project procedure | Paths or schema cannot be resolved |
| Build/test or document checks | Project-native command | Observable acceptance | Verify command/cwd | Declare explicitly | Evidence does not establish acceptance |
| Simplification, if needed | Ponytail or existing design skill | Concrete overbuilding concern | Inspect actual installation | Existing design review | Simplification changes required behavior |
| Knowledge/evolution | Bundled llm-wiki and skill-evolution | Source-backed quality improvement | Resolve installed skills | Report missing capability | Required evidence or validation is unavailable |

## Task packets

For each selected operation, record:

- Task signal and owning module.
- Executable or tool name, exact arguments, working directory and required inputs.
- Side effects: source writes, cache writes, network, logs, external mutation.
- Required authorization already supplied, and any additional permission needed.
- Output paths, observable acceptance, failure/stop condition and next action.
- Minimal validation command; raw evidence required beyond compressed output.
- Availability observation date and interface/version, not a copied health claim.

Register repeated side-effecting commands only when the project has a registry.
Use existing build/test entrypoints; do not create wrappers for one-off commands.

## Quality evaluation packet

Before a skill candidate run, define two distinct project-local tasks, at least
one not used to author the candidate, acceptance and refusal cases, baseline and
candidate versions, controlled environment/model, repeat policy and raw results.
Primary metrics: correctness and completeness of requirements, tool evidence,
implementation and validation. Time/tokens are secondary and require measurement.
Missing measurements are unknown, not zero. Link results to Wiki evolution records.

## Maintenance

Repair verified paths, broken links and command typos directly within existing
authorization; verify the repair and record its source. A command change affecting
scope, effects, required evidence or a route's default is a policy/behavior change,
not a typo repair. Preserve unresolved decisions for the user.
