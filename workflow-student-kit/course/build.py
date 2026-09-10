"""Build offline HTML from the maintained workflow and lesson data."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def embedded(data):
    return json.dumps(data, ensure_ascii=False, indent=2).replace('<', '\\u003c')


def build():
    course = ROOT / 'course'
    flow = json.loads((course / 'workflow.json').read_text(encoding='utf-8'))
    lessons = json.loads((course / 'lesson.json').read_text(encoding='utf-8'))
    template = (course / 'workflow.template.html').read_text(encoding='utf-8')
    (course / 'workflow.html').write_text(template.replace('__WORKFLOW_DATA__', embedded(flow)), encoding='utf-8')
    index = ROOT / 'index.html'
    text = index.read_text(encoding='utf-8')
    pattern = r'(<script id="lesson-data" type="application/json">).*?(</script>)'
    text, count = re.subn(pattern, lambda m: m[1] + embedded(lessons) + '\n' + m[2], text, flags=re.S)
    if count != 1:
        raise ValueError('Expected exactly one lesson-data block')
    index.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    build()
