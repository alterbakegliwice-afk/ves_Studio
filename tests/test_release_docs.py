"""Release-docs coherence tests (P0-09/P0-10)."""
import shutil
import subprocess
import sys

import validate_release_docs
import vlib


def test_release_docs_pass():
    assert validate_release_docs.main() == 0


def test_stale_version_in_status_fails(tmp_path):
    """P0-10: a STATUS.md that declares an older release version fails the gate."""
    dst = tmp_path / "repo"

    def ignore(d, names):
        return [n for n in names if n in (".git", "__pycache__", ".pytest_cache")
                or n.endswith(".zip")]
    shutil.copytree(vlib.REPO_ROOT, dst, ignore=ignore)

    r0 = subprocess.run([sys.executable, "scripts/validate_release_docs.py"],
                        cwd=dst, capture_output=True, text=True)
    assert r0.returncode == 0, r0.stdout + r0.stderr

    status = dst / "STATUS.md"
    status.write_text(status.read_text(encoding="utf-8")
                      .replace("1.1.1", "1.1.0"), encoding="utf-8")
    r1 = subprocess.run([sys.executable, "scripts/validate_release_docs.py"],
                        cwd=dst, capture_output=True, text=True)
    assert r1.returncode == 1, "stale STATUS version must fail"


def test_missing_referenced_report_fails(tmp_path):
    dst = tmp_path / "repo"

    def ignore(d, names):
        return [n for n in names if n in (".git", "__pycache__", ".pytest_cache")
                or n.endswith(".zip")]
    shutil.copytree(vlib.REPO_ROOT, dst, ignore=ignore)
    # reintroduce a dead reference
    vr = dst / "VALIDATION_REPORT.md"
    vr.write_text(vr.read_text(encoding="utf-8")
                  + "\n\npatrz `CLAUDE_CODE_IMPLEMENTATION_REPORT.md`\n", encoding="utf-8")
    r = subprocess.run([sys.executable, "scripts/validate_release_docs.py"],
                       cwd=dst, capture_output=True, text=True)
    assert r.returncode == 1
