"""Read-only candidate stability checks; never executes or activates a skill."""
import argparse
import hashlib
import json
from pathlib import Path


def tree_hash(folder):
    folder = Path(folder)
    if not folder.is_dir() or not (folder / 'SKILL.md').is_file():
        raise ValueError('A complete skill directory with SKILL.md is required')
    digest = hashlib.sha256()
    for path in sorted(folder.rglob('*')):
        if path.is_symlink():
            raise ValueError('Skill snapshots must not contain symlinks')
        if path.is_file():
            name = path.relative_to(folder).as_posix().encode('utf-8')
            content = path.read_bytes()
            digest.update(len(name).to_bytes(8, 'big') + name)
            digest.update(len(content).to_bytes(8, 'big') + content)
    return digest.hexdigest()


def local_path(value, kind):
    if not isinstance(value, str) or not Path(value).is_absolute():
        raise ValueError('Expected absolute local path')
    path = Path(value).resolve()
    if not (path.is_dir() if kind == 'dir' else path.is_file()):
        raise ValueError('Missing evidence or snapshot: ' + value)
    return path


def evaluate(packet):
    if not isinstance(packet, dict) or packet.get('version') != 1:
        raise ValueError('Unsupported evaluation packet')
    root = local_path(packet['project_root'], 'dir')
    baseline = local_path(packet['baseline_dir'], 'dir')
    candidate = local_path(packet['candidate_dir'], 'dir')
    if baseline == candidate:
        raise ValueError('Baseline and candidate must be separate snapshots')
    for snapshot in (baseline, candidate):
        if not snapshot.is_relative_to(root):
            raise ValueError('Evaluate project-local snapshots before shared promotion')
    hashes = (tree_hash(baseline), tree_hash(candidate))
    reasons = []
    if hashes != (packet.get('baseline_hash'), packet.get('candidate_hash')):
        reasons.append('Snapshot changed: revalidate the current version')
    if hashes[0] == hashes[1]:
        reasons.append('Candidate has no content change')
    runs = packet.get('runs')
    if not isinstance(runs, list):
        raise ValueError('runs must be a list')
    current = []
    for run in runs:
        if not isinstance(run, dict):
            raise ValueError('Each run must be an object')
        if (run.get('baseline_hash'), run.get('candidate_hash')) != hashes:
            continue  # Retain historical versions, but do not count them.
        task = run.get('task_id')
        if not isinstance(task, str) or not task.strip():
            raise ValueError('A stable task identity is required')
        if local_path(run['project_root'], 'dir') != root:
            reasons.append('Run belongs to a different project')
        refs = run.get('evidence')
        if not isinstance(refs, list) or not refs:
            raise ValueError('Run evidence is required')
        for ref in refs:
            local_path(ref, 'file')
        for field in ('held_out', 'comparable', 'required_pass', 'no_regression', 'improved'):
            if type(run.get(field)) is not bool:
                raise ValueError('Explicit boolean required: ' + field)
        current.append(run)
    if len({r['task_id'] for r in current}) < 2:
        reasons.append('Two distinct current-version tasks are required')
    if not any(r['held_out'] for r in current):
        reasons.append('At least one task must be held out from candidate authoring')
    if any(not r['comparable'] for r in current):
        reasons.append('Baseline/candidate conditions are not comparable')
    failed = any(not r['required_pass'] or not r['no_regression'] for r in current)
    if failed:
        reasons.append('A current-version run has a required failure or regression')
    if not any(r['improved'] for r in current):
        reasons.append('No demonstrated improvement on the targeted issue')
    return {'status': 'rejected' if failed else 'validation-pending' if reasons else 'promotion-ready',
            'reasons': reasons, 'current_tasks': sorted({r['task_id'] for r in current}),
            'activation_authorized': False,
            'limit': 'Checks declared records and hashes only; inspect raw evidence and obtain user approval.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('packet', nargs='?', type=Path)
    parser.add_argument('--hash', dest='folder', type=Path)
    args = parser.parse_args()
    if (args.packet is None) == (args.folder is None):
        parser.error('Supply one evaluation packet or --hash directory')
    try:
        result = ({'hash': tree_hash(args.folder)} if args.folder else
                  evaluate(json.loads(args.packet.read_text(encoding='utf-8-sig'))))
        print(json.dumps(result, indent=2))
        return 0 if result.get('status', 'promotion-ready') == 'promotion-ready' else 1
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(json.dumps({'status': 'invalid', 'reason': str(exc), 'activation_authorized': False}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
