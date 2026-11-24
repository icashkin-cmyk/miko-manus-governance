"""Shared runtime helpers for reproducible acceptance tests.

Default output is ignored out/acceptance. Set MIKO_ACCEPTANCE_OUT only when an
operator intentionally wants a committed evidence snapshot.
"""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]

def output_dir(relative: str) -> Path:
    base = Path(os.environ.get("MIKO_ACCEPTANCE_OUT", str(ROOT / "out" / "acceptance")))
    path = base / relative
    path.mkdir(parents=True, exist_ok=True)
    return path

def repo_label() -> str:
    return "<REPO_ROOT>"

def current_commit() -> str:
    """Return a commit when Git metadata is available; never raise in bundles."""
    import subprocess
    try:
        p = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                           text=True, capture_output=True, check=False)
        return p.stdout.strip() if p.returncode == 0 else "NOT_RUN"
    except OSError:
        return "NOT_RUN"

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
