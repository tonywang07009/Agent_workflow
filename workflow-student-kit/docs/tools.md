# Tool selection guide

This catalog describes the classroom tool set, not a requirement to run every
tool. Select capabilities after decomposing the problem. The active project's
OpenSpec toolbox owns the chosen route, commands, probes, and evidence limits.

## Selection procedure

1. Identify the question, required evidence, affected module, and allowed effects.
2. Consult the relevant row below; inspect the installed interface/version.
3. Run the smallest non-mutating availability probe. An installation link or old
   health snapshot is not proof of current availability.
4. Record the selected route, fallback, command, working directory, effects,
   output/evidence, and stop condition in the project's toolbox.
5. Use the chosen tool; inspect its result before making a claim. Missing evidence
   means a bounded result or a stop, not an inferred success.

## Capabilities

| Tool / form | Select when | Do not infer | Probe / setup source |
|---|---|---|---|
| SymDex: CLI and MCP server | Find symbols, ownership, callers/callees or scoped code context | Empty results do not prove no caller; verify repository, index freshness and language support | Discover available MCP tools, check the indexed repository; CLI help is read-only. [Official repository](https://github.com/husnainpk/SymDex) |
| RTK: CLI proxy | Inspect Git state/diffs or reduce supported command output | Compressed output alone may omit evidence needed for a claim; retrieve raw output when necessary | Check executable/version and supported command shape. [Official repository](https://github.com/rtk-ai/rtk) |
| OpenSpec: CLI and agent workflows | Maintain requirements, design, tasks, sync and archive | A checked task is not runtime verification; tool-route project files are not CLI-generated feature specs | Inspect installed help/status; initialization changes project files. [Official repository](https://github.com/Fission-AI/OpenSpec) |
| Ponytail: skills/plugin with an MCP option | Investigate whether an existing/native feature can replace unnecessary implementation | Fewer lines do not prove correctness or better depth; do not remove required behavior | Inspect the installed skill or advertised MCP interface. [Official repository](https://github.com/DietrichGebert/ponytail) |
| Direct filesystem access / filesystem MCP | Read known documents, configuration and logs | Text matches alone are not a complete call graph | Use the host's permitted read interface; writes and indexing may have effects |
| Project test/build tools | Verify behavior through the same interface used by callers | Compilation or one passing test does not establish all acceptance | Resolve the actual project command and evidence threshold from its toolbox |
| Document parser / browser | Read source material inaccessible as ordinary text; verify rendered UI | Parsing output may omit figures/tables; tool availability does not establish source accuracy | Prefer existing readable sources; probe supported formats and inspect outputs. Follow the host's browser skill |
| LLM Wiki desktop application | A user chooses an external document-to-wiki application | It is not the bundled llm-wiki skill and its local interface must be verified | [Application repository and setup](https://github.com/nashsu/llm_wiki) |

The choices and cautions above are this kit's routing guidance. Follow linked
upstream setup documentation for platform-specific installation; do not copy
another machine's paths, credentials, model settings, or health status.
An external application is optional unless the project explicitly selects it.

## Practical selections

- Code defect: OpenSpec + source navigation + Git inspection + nearest meaningful
  tests. Ponytail only if unnecessary implementation is a concrete concern.
- Document research: source reading/parsing + llm-wiki; source navigation is
  unnecessary unless a claim depends on implementation.
- Interface refactor: codebase-design/improve-codebase-architecture + source
  relationships + behavior tests. Prefer reuse/deletion before a new adapter.
- Project closeout: OpenSpec evidence + llm-wiki + skill-evolution assessment.

## Failure and cost policy

Keep a single effective route per task type in the project toolbox. Where the
project permits it, use Git CLI if RTK cannot answer, or targeted source inspection
if SymDex MCP and CLI cannot answer. Explain the fallback reason for Git/source
lookups and its evidence limits. Never claim text search proves a complete call
graph. If a required conclusion needs an unavailable capability, stop that claim.
Do not auto-install or change tool configuration merely to obey this guide.

Correctness and completeness come first. Measure time/tokens only with comparable
tasks, revisions, environments, and actual usage. Do not promise token savings
from a tool name or English instructions.

## Knowledge and skill evolution

The kit supplies llm-wiki and skill-evolution as cooperating local skills.
They adapt the raw-evidence / persistent-knowledge / candidate-skill separation
in [WikiSkill, sections 3.1-3.2](https://arxiv.org/html/2608.27454#S3).
This kit adds user-selected activation and two distinct local validation tasks;
these are classroom rules, not reproduced benchmark results.
