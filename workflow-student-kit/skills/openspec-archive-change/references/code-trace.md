# Change code trace

Write one `code-trace.md` per completed change, inside its resolved change root,
then preserve it with that change's archive. It is a navigation snapshot of the
delivered work, not a replacement for canonical requirements or raw test evidence.
Write explanations in the user's language and preserve actual file/symbol names.

## Evidence and paths

- Record change name, capture date, absolute project root, original change path,
  and final archive path. Record the actual Git revision and dirty/uncommitted
  scope when available; do not imply HEAD alone identifies uncommitted work.
- Inspect the change's actual affected files and relevant entry points using the
  project's tool routing. Include supporting unchanged files only when needed to
  follow the feature. Do not scan unrelated projects or infer a caller graph from
  text hits. Label inferred relationships and unavailable evidence explicitly.
- For every listed file, give its project-relative path, absolute capture path,
  purpose, and status (added, modified, unchanged supporting file, renamed, or
  deleted). For renames retain old-to-new mapping; deleted paths are historical
  records, not live links. For external files identify their owning root.
- Make file entries clickable using actual resolved paths. Absolute source paths
  describe this machine at capture time; relative paths support later relocation.
  For documents that move with the change, prefer archive-local relative links
  and retain original-to-archive path mappings. Resolve final paths after moving.
- Verify live files and named symbols exist. Missing required evidence must be
  resolved before completion; label legitimate absences and tool limitations.
  Do not manufacture files, tests, or PASS results to fill the outline.

## Required content

1. **Context:** the change identity and path/revision information above.
2. **File tree:** generate a tree from the actual selected project's directory
   structure, rooted at its absolute project path. Preserve real directory names,
   nesting, filename spelling, and case; do not invent category folders such as
   `main_code`, `Test_code`, or `Project_Management`. Annotate relevant files with
   their purposes and identify files affected by this change. Include source,
   tests, requirements, the effective AGENTS.md, and OpenSpec locations where
   they actually exist. For large projects, expand relevant branches and clearly
   mark omitted branches; state that the tree is scoped rather than complete.
   Record absent resources and deleted paths separately, not as existing nodes.
3. **File details:** the paths, purposes, and statuses above, with important
   entry symbols where useful for navigation.
4. **Behavior trace:** for each delivered behavior, link its canonical acceptance
   criterion to implementation entry points and corresponding test cases/evidence.
   Describe the verified call/data flow briefly; distinguish inference from
   inspected relationships. Identify gaps instead of treating a file list as proof.
5. **Validation:** actual test case names, covered behavior, command and cwd,
   execution date, outcome/counts, and evidence location. Distinguish tests found
   from tests executed. Include manual/documentation validation when applicable.

## Tree presentation

Use tree connectors and inline purpose comments as below. This is presentation
syntax only: derive every node and parent-child relationship from inspected
project paths, never copy the placeholders as a prescribed layout. Put absolute
file paths in the associated file details. Test names and counts likewise come
from the project's actual acceptance requirements and execution evidence.

```text
<absolute project root>/
├── <actual directory>/
│   ├── <actual file>    # Purpose; change status
│   └── <actual subdirectory>/
│       └── <actual file> # Purpose; change status
└── <actual root file>   # Purpose; change status
```

If acceptance already lives in OpenSpec, link those actual specs instead of
creating a duplicate `requirements.md`. Use tables for file details and behavior
mapping, for example:

```markdown
| File / symbol | Project-relative path | Absolute capture path | Purpose / status |
|---|---|---|---|
| <actual file link and symbol> | <path> | <absolute path> | <purpose; status> |

| Requirement / acceptance link | Implementation / flow | Test case / evidence | Result / limitation |
|---|---|---|---|
| <canonical criterion> | <verified symbols and links> | <actual case and evidence link> | <observed result> |
```

On resume before completion, refresh the existing trace rather than creating a
second copy. Later changes get their own snapshots; do not rewrite completed
historical traces to describe new behavior.
