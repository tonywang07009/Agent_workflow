"""Sync lessons; optionally regenerate the diagram with a local Archify checkout."""
import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent


def embedded(data):
    return json.dumps(data, ensure_ascii=False, indent=2).replace('<', '\\u003c')


def build(archify_root=None):
    course = ROOT / 'course'
    lessons = json.loads((course / 'lesson.json').read_text(encoding='utf-8'))
    if archify_root is not None:
        cli = Path(archify_root).resolve() / 'archify/bin/archify.mjs'
        if not cli.is_file():
            raise ValueError(f'Archify CLI not found: {cli}')
        result = subprocess.run(
            ['node', str(cli), 'deliver', 'workflow', str(course / 'workflow.archify.json'),
             str(course / 'workflow.html'), '--quality', 'showcase', '--json'],
            cwd=ROOT, capture_output=True, encoding='utf-8', check=True)
        receipt = json.loads(result.stdout)
        if not receipt.get('ok'):
            raise ValueError('Archify did not accept the artifact')
        (course / 'workflow.delivery.json').write_text(
            json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    index = ROOT / 'index.html'
    text = index.read_text(encoding='utf-8')
    pattern = r'(<script id="lesson-data" type="application/json">).*?(</script>)'
    text, count = re.subn(pattern, lambda m: m[1] + embedded(lessons) + '\n' + m[2], text, flags=re.S)
    if count != 1:
        raise ValueError('Expected exactly one lesson-data block')
    index.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archify-root', type=Path, help='Local archify repository; omit to sync lessons only')
    build(parser.parse_args().archify_root)
