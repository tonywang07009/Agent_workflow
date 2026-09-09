"""Install the classroom skills without replacing existing skills."""
from pathlib import Path
import shutil
import sys


def install(repo):
    repo = Path(repo).expanduser().resolve()
    if not repo.is_dir():
        raise ValueError('Target repository must already exist')
    source = Path(__file__).resolve().parent / 'skills'
    folders = sorted(p for p in source.iterdir() if p.is_dir())
    target = repo / '.agents' / 'skills'
    conflicts = [p.name for p in folders if (target / p.name).exists() or (target / p.name).is_symlink()]
    if conflicts:
        raise ValueError('No files changed; existing skills: ' + ', '.join(conflicts))
    target.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for folder in folders:
            dest = target / folder.name
            dest.mkdir()  # Exclusive create also rejects a concurrent installer.
            created.append(dest)
            shutil.copytree(folder, dest, dirs_exist_ok=True)
    except Exception:
        for dest in reversed(created):
            shutil.rmtree(dest)
        raise
    return len(created)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: python3 install.py /path/to/existing/practice-repo')
    try:
        count = install(sys.argv[1])
    except (ValueError, OSError) as exc:
        sys.exit(str(exc))
    print(f'Installed {count} skills; no existing skills replaced.')
