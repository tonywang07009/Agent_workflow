# RedCap MCP And Command Toolbox

## Purpose

- [Goal]: keep RedCap/OAI tool use predictable, low-token, and evidence-first.
- [Scope]: repository navigation, MCP health checks, build/test commands, RFsim runtime commands, PDF/spec handling, and report export.
- [Rule]: do not treat every available MCP as part of the default path. Use the smallest tool that answers the current question.
- [Date]: 2026-06-27 snapshot. Re-check tool health when Codex, MCP config, or the local environment changes.

## Delegated Tool Routing

Root [`AGENTS.md`](../../AGENTS.md#file-query-workflow) is the authoritative
tool-routing rule. This document supplies task packets and command references;
it does not change a default route, fallback, or evidence threshold.

`ask-matt` reads this document after it selects a primary skill. Return one
tool-routing packet that follows root `AGENTS.md`:

| Field | Source |
|---|---|
| Task signal | Current request |
| Primary skill | Direct user selection or `ask-matt` workflow route |
| Tool steps | Root `AGENTS.md` plus the applicable task packet below |
| Stop condition | Applicable task packet below |
| Fallback | Root `AGENTS.md` |

- A directly selected primary skill keeps its explicit tool instructions.
  Use this table only for an omitted necessary step.
- The router selects tools; the primary skill executes its own workflow.
- Research-wiki work first follows [Context Gate](../../redcap_research_wiki/CONTEXT.md)
  and [Ask Matt Routing Memo](../../redcap_research_wiki/ASK_MATT_ROUTING_MEMO.md).

## Cost Control Policy

- [MCP count itself]: not the main problem. The real cost is uncontrolled priority, context loading, and repeated ad-hoc review logic.
- [Decision cost]: too many tools marked "always use first" slows tool selection. Keep one default route per task type.
- [Context cost]: do not bulk-load old PDFs, historical reports, all runtime logs, or unrelated milestones at task start.
- [Reasoning cost]: use fixed review and validation packets so each task does not reinvent spec mapping, runtime evidence, and pass/fail rules.

## Task Packet Layers

Root `AGENTS.md` selects the required-first tool and fallback. These packets
only state what evidence is sufficient for the current task.

| Layer | Purpose | Completion condition |
|---|---|---|
| [Layer 1: Navigation] | Find the owner, symbol relationship, or marker needed by the task. | Target files/functions and markers are known. |
| [Layer 2: Evidence] | Prove build, unit, or runtime behavior. | Evidence path and key pass/fail marker are captured. |
| [Layer 3: Documentation] | Preserve decisions and handoff value. | Report or checklist is updated without unrelated context. |

## Task Packets And Command References

Use [root `AGENTS.md`](../../AGENTS.md#file-query-workflow) for the required
first tool and fallback. The sections below add only task-specific stop
conditions, health notes, and command references; they do not define a second
tool route.

## Tool-Route Governance

- Correct task packet and command-reference details directly in this document.
- Require OpenSpec and human confirmation before changing a default route,
  fallback, stop condition, or evidence threshold. Change root `AGENTS.md`
  only when the required-first tool route or fallback itself changes.

## MCP Health Snapshot

| Tool | Status | Health Probe | Observed Limitation | Default Use |
|---|---|---|---|---|
| [filesystem MCP] | [Available] | `list_allowed_directories` returns `/home/tonywang/OAI` | Startup now uses local binary `/usr/local/bin/mcp-server-filesystem` | Read/list metadata; do not use write/move without explicit approval. |
| [symdex] | [CLI fallback available] | `symdex --state-dir .symdex repos`; `search`; `text`; `outline` | MCP and CLI command names differ; `callers/callees` may return empty | Main code navigation tool. |
| [markitdown MCP] | [Partially available] | ASCII Markdown conversion succeeds | Unicode README probe hit `UnicodeDecodeError` | Use for stable non-Unicode document conversion only after small probe. |
| [mineru MCP] | [Server code compile OK] | `py_compile` on `mineru_mcp_server.py` and scanner | `parse_pdf` mutates Markdown cache, so run only when cache refresh is intended | RedCap PDF/spec cache generation. |
| [Google Drive connector] | [Available] | profile probe succeeds | Cloud scope is wider than daily code review needs | Report export, shared docs, Sheets, Slides. |
| [GitHub plugin] | [Enabled, task-gated] | config shows enabled | Tool discovery may not expose GitHub actions in every turn | Use only for PR/CI/issue workflows. |

## Non-Default Connectors

| Connector / Tool Area | Project Fit | Use Only When |
|---|---|---|
| [Google Drive Docs/Sheets/Slides] | Report export, shared learning reports, presentation materials | The user asks for Drive/Docs/Sheets/Slides output or collaboration. |
| [Sites] | Frontend Gantt chart deployment or hosted project dashboard | A deployable web app exists and the user asks to save/deploy it. |
| [Workspace Agents] | Agent configuration work | The user explicitly asks to create or update a workspace agent. |
| [Google Calendar] | Scheduling only | The user asks for calendar planning; it is not part of RedCap protocol validation. |
| [GitHub] | PR review, CI triage, issue/MR workflow | The task is explicitly GitHub or CI related. |

## Known Repair Candidates

- [filesystem MCP startup]
  - [Status]: applied on 2026-06-27 after user approval.
  - [Before]: `/home/tonywang/.codex/config.toml` used `npx -y @modelcontextprotocol/server-filesystem`.
  - [After]: command is `/usr/local/bin/mcp-server-filesystem` with args `["/home/tonywang/OAI"]`.
  - [Backup]: `/home/tonywang/.codex/config.toml.bak-20260627-filesystem-mcp`.
  - [Validation]: local server binary starts on stdio and config diff shows only the filesystem MCP startup lines changed.

- [rtk command shape]
  - [Current]: `rtk` works well for normal commands but not every shell builtin or complex predicate.
  - [Evidence]: `rtk test -f ...` and `rtk find ... -type f \( ... \)` are not reliable.
  - [Recommended use]: follow root `AGENTS.md` for current routing: RTK first for Git, Symdex MCP first for symbol relationships, and direct reads for documents and logs. Commands below are historical references, not a replacement for that route.

- [symdex command naming]
  - [Current]: MCP tool names and CLI subcommands are not identical.
  - [Recommended use]: CLI commands are `repos`, `search`, `find`, `outline`, `text`, `semantic`, `callers`, `callees`, `index`, `invalidate`, `serve`.

## Code Navigation Commands

```bash
rtk /home/tonywang/miniforge3/bin/symdex --state-dir .symdex repos
rtk /home/tonywang/miniforge3/bin/symdex --state-dir .symdex search <symbol> --repo redcap_oai
rtk /home/tonywang/miniforge3/bin/symdex --state-dir .symdex find <symbol> --repo redcap_oai
rtk /home/tonywang/miniforge3/bin/symdex --state-dir .symdex text "<marker>" --repo redcap_oai
rtk /home/tonywang/miniforge3/bin/symdex --state-dir .symdex outline <path> --repo redcap_oai
rtk /home/tonywang/miniforge3/bin/symdex --state-dir .symdex callers <function> --repo redcap_oai
rtk /home/tonywang/miniforge3/bin/symdex --state-dir .symdex callees <function> --repo redcap_oai
```

```bash
rtk rg -n "<runtime-or-log-marker>" test_log redcap_library agent_doc
```

Use Symdex, not `rg`, for source symbols, definitions, callers, callees, or
module ownership. This command is only for marker text after the owner is
already known.

## Build And Unit Test Commands

```bash
rtk cmake --preset default
rtk cmake --build --preset default --target nr-softmodem
rtk cmake --build --preset default --target nr-uesoftmodem
rtk cmake --preset tests
rtk cmake --build --preset tests
rtk ctest --test-dir cmake_targets/ran_build/build_test --output-on-failure
```

- [UE-side C change]: build `nr-uesoftmodem`.
- [gNB-side C change]: build `nr-softmodem`.
- [Shared or cross-layer change]: build both sides and the closest CTest target.
- [Docs-only change]: run reference scans and `git diff --check`; do not run CMake unless needed.

## RedCap Runtime Commands

```bash
rtk bash redcap_interface/validate_redcap_interface.sh
rtk bash mmtc.menu.bash
rtk bash mmtc.menu.bash status
rtk bash mmtc.menu.bash smoke
rtk bash mmtc.menu.bash gate3
rtk bash mmtc.menu.bash gate4
rtk bash mmtc.menu.bash redcap-vs-normal
rtk bash mmtc.menu.bash rebuild
rtk bash mmtc.menu.bash inspect
```

- [Daily RFsim]: prefer root `mmtc.menu.bash`.
- [Paper/demo]: prefer `redcap_interface/mmtc.display.bash`.
- [Legacy shims]: keep existing compatibility scripts when old reports reference them.

## Runtime Evidence Commands

```bash
rtk docker ps -a
rtk docker logs <container>
rtk rg -n "\\[RedCap RA\\]|\\[RedCap BWP\\]|cg-SDT|RRC_INACTIVE|RRCResume|UE with RNTI is RedCap" test_log redcap_library openair2
```

- [Runtime PASS rule]: attach, PDU session, tunnel, or ping success is not enough for RedCap protocol claims.
- [Required evidence]: include gNB/UE markers for the claimed behavior, or mark the result as [PARTIAL] with a limitation.
- [Common marker examples]: `[RedCap RA]`, `[RedCap RA][UE Msg1]`, `[RedCap BWP]`, `cg-SDT`, `RRC_INACTIVE`, `RRCResume`.

## PDF And Spec Commands

```bash
rtk sed -n '1,120p' redcap_doc/mineru_markdown/scan_manifest.md
rtk rg -n "<TS-or-topic>" redcap_doc/specs redcap_doc/mineru_markdown -g '*.md'
rtk /home/tonywang/miniforge3/envs/mcp/bin/python mcp/magic-pdf/redcap_doc_mineru_scan.py --language ch --max-spec-pages 150
```

- [Spec lookup]: cached Markdown first, PDF parsing second.
- [Clause policy]: exact 3GPP clause numbers must be locally verified; otherwise mark `[Needs Verification]`.
- [MinerU use]: parse only when the cache is missing, stale, or explicitly being refreshed.

## Documentation Checks

```bash
rtk rg -n "<new-path-or-marker>" AGENTS.md agent_doc redcap_doc redcap_library redcap_interface -g '*.md' -g '*.sh' -g '*.bash' -g '*.yml' -g '*.yaml'
rtk git diff --check -- AGENTS.md agent_doc redcap_doc redcap_library redcap_interface
```

- [Root AGENTS.md]: keep it as a router.
- [Detailed workflow]: keep under `agent_doc/Project_management/`.
- [Process logs]: write only when a completed improvement creates reusable handoff value.
