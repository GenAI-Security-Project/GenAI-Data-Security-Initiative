"""
Regenerates the hash-pinned requirement locks from their .in files.

    python update_locks.py          # needs uv: pip install uv

Each requirements*.in lists what the tooling needs, with version ranges;
each requirements*.txt next to it is the lock CI and contributors install:
every package, including transitive ones, pinned to one version with its
SHA-256 hashes, so `pip install -r requirements.txt` installs exactly the
reviewed artefacts (pip checks the hashes automatically). The locks are
universal: they resolve for Python 3.11+ on Linux, macOS and Windows, with
platform markers where a dependency differs.

The croissant lock is constrained to the NER lock's versions so the two can
be installed together. Dependabot proposes updates to the locks weekly;
after editing an .in file, run this script and commit both files.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PYTHON = "3.11"
LOCKS = ["requirements", "requirements-dev", "requirements-ner", "requirements-croissant"]
HEADER = (
    "# Hash-pinned lock generated from {src} by data_validation/update_locks.py\n"
    "# (uv pip compile --universal --generate-hashes --python-version {py}{extra}).\n"
    "# Do not edit by hand: change {src} and rerun the script.\n"
)


def compile_lock(name: str, constraints: Path | None = None) -> None:
    src, out = HERE / f"{name}.in", HERE / f"{name}.txt"
    cmd = ["uv", "pip", "compile", str(src), "--universal", "--generate-hashes",
           "--python-version", PYTHON, "--no-header", "--quiet", "-o", str(out)]
    if constraints:
        cmd += ["-c", str(constraints)]
    subprocess.run(cmd, check=True, cwd=HERE)
    extra = ", constrained to requirements-ner.txt" if constraints else ""
    body = out.read_text(encoding="utf-8")
    out.write_text(HEADER.format(src=src.name, py=PYTHON, extra=extra) + body, encoding="utf-8", newline="")
    print(f"wrote {out.name}")


def pins(lock: Path) -> str:
    """name==version lines of a lock, usable as a constraints file."""
    lines = [line.split()[0].rstrip(";") for line in lock.read_text(encoding="utf-8").splitlines()
             if line[:1].isalnum() and "==" in line]
    return "\n".join(lines) + "\n"


def main() -> int:
    for name in LOCKS[:3]:
        compile_lock(name)
    with tempfile.TemporaryDirectory() as tmp:
        constraints = Path(tmp) / "ner-constraints.txt"
        constraints.write_text(pins(HERE / "requirements-ner.txt"), encoding="utf-8")
        compile_lock("requirements-croissant", constraints)
    return 0


if __name__ == "__main__":
    sys.exit(main())
