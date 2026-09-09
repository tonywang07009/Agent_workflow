"""Run offline checks for the teaching bundle and safe installation."""
from pathlib import Path
import hashlib
import json
import re
import tempfile
import install

root = Path(__file__).resolve().parent
lessons = json.loads((root / 'course/lesson.json').read_text(encoding='utf-8'))
assert len(lessons) == 8 and sum(c['minutes'] for c in lessons) == 90
assert len({c['id'] for c in lessons}) == 8

for c in lessons:
    for key in ['goal', 'points', 'demo', 'prompt', 'output', 'stop', 'question', 'answer', 'notes']:
        assert c[key], (c['id'], key)
    for source in c['sources']:
        assert (root / 'course/sources' / source).is_file()
assert len(list((root / 'skills').glob('*/SKILL.md'))) == 12

# Check this bundle's new English entrypoint and local reference topology offline.
workflow_source = root / 'skills/workflow'
entry = (workflow_source / 'SKILL.md').read_text(encoding='utf-8')
frontmatter = entry.split('---', 2)[1]
metadata = dict(line.split(': ', 1) for line in frontmatter.strip().splitlines())
assert metadata['name'] == 'workflow' and metadata['description']
for document in workflow_source.rglob('*.md'):
    content = document.read_text(encoding='utf-8')
    assert not re.search(r'[\u3400-\u9fff]', content), document
    for target in re.findall(r'\]\(([^)]+)\)', content):
        assert (document.parent / target).is_file(), (document, target)

with tempfile.TemporaryDirectory() as tmp:
    repo = Path(tmp)
    assert install.install(repo) == 12
    workflow = repo / '.agents/skills/workflow'
    for relative in ['SKILL.md', 'agents/openai.yaml', 'scripts/state.py',
                     'references/delivery.md', 'references/knowledge.md',
                     'references/state.md', 'references/customization.md']:
        assert (workflow / relative).read_bytes() == (root / 'skills/workflow' / relative).read_bytes()
    assert not (repo / 'openspec').exists()
    assert not (repo / '.workflow').exists()
    before = {str(p.relative_to(repo)): p.read_bytes() for p in repo.rglob('*') if p.is_file()}
    try:
        install.install(repo)
        raise AssertionError('Collision should refuse')
    except ValueError:
        pass
    assert before == {str(p.relative_to(repo)): p.read_bytes() for p in repo.rglob('*') if p.is_file()}
    try:
        install.install(repo / 'missing')
        raise AssertionError('Missing target should refuse')
    except ValueError:
        pass
manifest = root / 'SHA256SUMS'

if manifest.exists():
    for line in manifest.read_text(encoding='utf-8').splitlines():
        digest, relative = line.split('  ', 1)
        assert hashlib.sha256((root / relative).read_bytes()).hexdigest() == digest, relative
        
print('PASS: 8 chapters / 90 minutes / sources / 12 skills / install / no-overwrite / missing-target / hashes')
