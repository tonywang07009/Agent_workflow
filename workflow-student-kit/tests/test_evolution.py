"""Exercise the same read-only evaluation CLI used by the skill."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'skills/skill-evolution/scripts/evaluate.py'


class EvolutionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.baseline = self.root / 'baseline'
        self.candidate = self.root / 'candidate'
        for folder, text in [(self.baseline, 'original'), (self.candidate, 'candidate')]:
            folder.mkdir()
            (folder / 'SKILL.md').write_text(text, encoding='utf-8')
        self.log = self.root / 'results.txt'
        self.log.write_text('Fixture only: evaluation assertions are not real agent results.', encoding='utf-8')

    def call(self, *args):
        return subprocess.run([sys.executable, '-B', str(SCRIPT), *map(str, args)],
                              capture_output=True, text=True)

    def packet(self):
        baseline_hash = json.loads(self.call('--hash', self.baseline).stdout)['hash']
        candidate_hash = json.loads(self.call('--hash', self.candidate).stdout)['hash']
        return {'version': 1, 'project_root': str(self.root),
                'baseline_dir': str(self.baseline), 'candidate_dir': str(self.candidate),
                'baseline_hash': baseline_hash, 'candidate_hash': candidate_hash,
                'runs': [dict(task_id=f'task-{i}', project_root=str(self.root),
                              baseline_hash=baseline_hash, candidate_hash=candidate_hash,
                              held_out=bool(i), comparable=True, required_pass=True,
                              no_regression=True, improved=True, evidence=[str(self.log)])
                         for i in range(2)]}

    def evaluate(self, packet):
        path = self.root / 'evaluation.json'
        path.write_text(json.dumps(packet), encoding='utf-8')
        before = {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result = self.call(path)
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
        return result

    def test_two_distinct_current_tasks_with_holdout_are_ready_but_not_approved(self):
        result = self.evaluate(self.packet())
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        self.assertEqual(output['status'], 'promotion-ready')
        self.assertFalse(output['activation_authorized'])

    def test_repeating_one_task_or_missing_holdout_does_not_count(self):
        for field, value in [('task_id', 'same-task'), ('held_out', False)]:
            packet = self.packet()
            for run in packet['runs']:
                run[field] = value
            self.assertEqual(self.evaluate(packet).returncode, 1)

    def test_resource_change_invalidates_previous_stability(self):
        packet = self.packet()
        (self.candidate / 'rules.md').write_text('changed resource', encoding='utf-8')
        result = json.loads(self.evaluate(packet).stdout)
        self.assertEqual(result['status'], 'validation-pending')
        self.assertEqual(result['current_tasks'], [])

    def test_current_failure_blocks_promotion_even_with_other_passes(self):
        packet = self.packet()
        packet['runs'].append({**packet['runs'][0], 'task_id': 'regression', 'no_regression': False})
        self.assertEqual(json.loads(self.evaluate(packet).stdout)['status'], 'rejected')

    def test_missing_evidence_or_nonboolean_claims_are_invalid(self):
        for field, value in [('evidence', [str(self.root / 'missing')]), ('required_pass', 'true')]:
            packet = self.packet()
            packet['runs'][0][field] = value
            self.assertEqual(self.evaluate(packet).returncode, 2)

    def test_no_improvement_is_not_ready(self):
        packet = self.packet()
        for run in packet['runs']:
            run['improved'] = False
        self.assertEqual(json.loads(self.evaluate(packet).stdout)['status'], 'validation-pending')


if __name__ == '__main__':
    unittest.main()
