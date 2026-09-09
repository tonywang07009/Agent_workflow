"""Run offline checks for the teaching bundle and safe installation."""
from pathlib import Path
import hashlib
import json
import tempfile
import install

root = Path(__file__).resolve().parent
lessons = json.loads((root / 'course/lesson.json').read_text())
assert len(lessons) == 8 and sum(c['minutes'] for c in lessons) == 90
assert len({c['id'] for c in lessons}) == 8

for c in lessons:
    for key in ['goal', 'points', 'demo', 'prompt', 'output', 'stop', 'question', 'answer', 'notes']:
        assert c[key], (c['id'], key)
    for source in c['sources']:
        assert (root / 'course/sources' / source).is_file()
assert len(list((root / 'skills').glob('*/SKILL.md'))) == 11

with tempfile.TemporaryDirectory() as tmp:
    repo = Path(tmp)
    assert install.install(repo) == 11
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
    for line in manifest.read_text().splitlines():
        digest, relative = line.split('  ', 1)
        assert hashlib.sha256((root / relative).read_bytes()).hexdigest() == digest, relative
        
print('PASS: 8 chapters / 90 minutes / sources / 11 skills / install / no-overwrite / missing-target / hashes')
