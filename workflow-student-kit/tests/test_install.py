"""Installation must deliver references without activating project templates."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import install


class InstallTests(unittest.TestCase):
    def test_skills_and_resource_pack_install_without_live_project_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / 'AGENTS.md').write_text('Existing project rules', encoding='utf-8')
            self.assertEqual(install.install(repo), 14)
            self.assertTrue((repo / '.agents/workflow-kit/management/openspec-project/toolbox.md').is_file())
            self.assertTrue((repo / '.agents/workflow-kit/docs/tools.md').is_file())
            self.assertTrue((repo / '.agents/skills/llm-wiki/SKILL.md').is_file())
            self.assertEqual((repo / 'AGENTS.md').read_text(), 'Existing project rules')
            for name in ('openspec', 'wiki', '.workflow'):
                self.assertFalse((repo / name).exists())

    def test_resource_collision_refuses_before_installing_any_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            resources = repo / '.agents/workflow-kit'
            resources.mkdir(parents=True)
            (resources / 'mine.md').write_text('Keep', encoding='utf-8')
            with self.assertRaises(ValueError):
                install.install(repo)
            self.assertFalse((repo / '.agents/skills').exists())
            self.assertEqual((resources / 'mine.md').read_text(), 'Keep')

    def test_resource_copy_failure_rolls_back_only_new_installation(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / 'mine.md').write_text('Keep', encoding='utf-8')
            real_copy = install.shutil.copytree
            def fail_docs(src, dst, *args, **kwargs):
                if Path(src).name == 'docs':
                    raise OSError('Fixture copy failure')
                return real_copy(src, dst, *args, **kwargs)
            with patch.object(install.shutil, 'copytree', side_effect=fail_docs):
                with self.assertRaises(OSError):
                    install.install(repo)
            self.assertFalse((repo / '.agents/workflow-kit').exists())
            self.assertEqual(list((repo / '.agents/skills').iterdir()), [])
            self.assertEqual((repo / 'mine.md').read_text(), 'Keep')
