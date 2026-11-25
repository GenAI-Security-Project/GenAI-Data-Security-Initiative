"""
Checks that a framework mapping row which cites published test records is
backed by records that exist and pass their reference verifier.

A row in framework_alignments (or any object with a "control_id") may carry

    "test_records": {
        "package": "agent-evidence-vectors",
        "corpus": "vectors-mcp-owasp",
        "requirement": "MCPVS-1"
    }

naming a conformance corpus of signed accept and reject records shipped in
the agent-evidence-vectors package (pinned in requirements.in), and
optionally one requirement in that corpus's REGISTRY.json. The row's
alignment_status then rests on something a third party can re-run instead
of on the author's word.

ERROR: the package is not installed; the corpus is not shipped in the
       installed version; the requirement is not in the corpus registry or
       is withdrawn; the requirement does not list the row's control_id
       when the control is one the registry indexes (MCP01-MCP10); or the
       corpus does not replay clean under the package's reference verifier
       (including a corpus the reference verifier has no reader for).
WARN:  test_records on a row whose alignment_status is "missing" or
       "not_applicable", where the records cannot support the row.

Each corpus is replayed once per run, however many rows cite it.

Usage:
    python evidence_mapping_check.py --file ../../datasets/riskassessment_dataset/entries/X.json
    python evidence_mapping_check.py                # every dataset
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from functools import cache
from importlib import metadata
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT,
    ERROR,
    WARN,
    Finding,
    add_target_args,
    ensure_utf8_stdout,
    load_json,
    print_findings,
    resolve_targets,
)

CHECK = "evidence"
PACKAGE = "agent-evidence-vectors"
MODULE = "agent_evidence_vectors"
KEY = "test_records"
REPLAY_TIMEOUT = 300
# Control IDs a corpus registry indexes in its "top10" lists.
INDEXED_CONTROL_RE = re.compile(r"^MCP(0[1-9]|10)$")
NO_SUPPORT = {"missing", "not_applicable"}


@cache
def package_version() -> str | None:
    try:
        return metadata.version(PACKAGE)
    except metadata.PackageNotFoundError:
        return None


@cache
def corpora_dir() -> Path | None:
    if package_version() is None:
        return None
    from agent_evidence_vectors.run_vectors import corpora_root

    return Path(corpora_root())


@cache
def registry(corpus: str) -> dict[str, dict] | None:
    """Requirement and threat entries of a corpus registry, by id, or None if it has none."""
    root = corpora_dir()
    path = root / corpus / "REGISTRY.json" if root else None
    if path is None or not path.is_file():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    return {e["id"]: e for section in ("requirements", "threats") for e in data.get(section, []) if "id" in e}


@cache
def replay(corpus: str) -> tuple[bool, str]:
    """(passed, last output line) for one replay of a shipped corpus by the reference verifier."""
    with tempfile.TemporaryDirectory() as tmp:
        try:
            proc = subprocess.run(
                [sys.executable, "-m", f"{MODULE}.run_vectors", "--corpus", corpus, "--report", str(Path(tmp) / "report.json")],
                cwd=tmp, capture_output=True, text=True, encoding="utf-8", errors="replace",
                timeout=REPLAY_TIMEOUT, check=False,
            )
        except subprocess.TimeoutExpired:
            return False, f"replay timed out after {REPLAY_TIMEOUT}s"
    lines = (proc.stdout + proc.stderr).strip().splitlines()
    return proc.returncode == 0, (lines[-1] if lines else f"exit {proc.returncode}")


def iter_cited_rows(obj: Any, pointer: str = ""):
    """(pointer, row) for every object that carries test_records."""
    if isinstance(obj, dict):
        if KEY in obj:
            yield pointer, obj
        for k, v in obj.items():
            yield from iter_cited_rows(v, f"{pointer}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from iter_cited_rows(v, f"{pointer}/{i}")


def check_row(path: Path, pointer: str, row: dict) -> list[Finding]:
    where = f"{pointer}/{KEY}"
    cited = row[KEY]
    if not isinstance(cited, dict) or cited.get("package") != PACKAGE or not isinstance(cited.get("corpus"), str):
        return [Finding(ERROR, CHECK, path, where, f'expected {{"package": "{PACKAGE}", "corpus": "<name>"}}')]
    if package_version() is None:
        return [Finding(ERROR, CHECK, path, where, f"{PACKAGE} is not installed (pip install -r requirements.txt)")]
    findings: list[Finding] = []
    status = row.get("alignment_status")
    if status in NO_SUPPORT:
        findings.append(Finding(WARN, CHECK, path, where, f'alignment_status is "{status}"; test records cannot support it'))
    corpus = cited["corpus"]
    root = corpora_dir()
    if root is None or not (root / corpus / "MANIFEST.json").is_file():
        return findings + [Finding(ERROR, CHECK, path, where, f"{PACKAGE} {package_version()} ships no corpus {corpus!r}")]
    requirement = cited.get("requirement")
    if requirement is not None:
        entries = registry(corpus)
        entry = entries.get(requirement) if entries else None
        if entry is None:
            findings.append(Finding(ERROR, CHECK, path, where, f"{requirement!r} is not in the {corpus} registry"))
        elif entry.get("status") == "withdrawn":
            findings.append(Finding(ERROR, CHECK, path, where, f"{requirement} is withdrawn in the {corpus} registry"))
        else:
            control = str(row.get("control_id", "")).strip()
            if INDEXED_CONTROL_RE.match(control) and control not in entry.get("top10", []):
                findings.append(Finding(ERROR, CHECK, path, where,
                                        f"{requirement} tests {', '.join(entry.get('top10', [])) or 'no control'}, not {control}"))
    passed, last = replay(corpus)
    if not passed:
        findings.append(Finding(ERROR, CHECK, path, where, f"{corpus} does not replay clean under the reference verifier: {last}"))
    return findings


def check_data(path: Path, data: Any) -> list[Finding]:
    return [f for pointer, row in iter_cited_rows(data) for f in check_row(path, pointer, row)]


def check_file(path: Path) -> list[Finding]:
    data, err = load_json(path, CHECK)
    if err:
        return [err]
    return check_data(path, data)


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Check mapping rows that cite published test records")
    add_target_args(parser)
    args = parser.parse_args(argv)
    files = resolve_targets(args)
    if files is None:
        return 2
    findings = [f for p in files for f in check_file(p)]
    print(f"Checked {len(files)} file(s)")
    return print_findings(findings, DATASETS_ROOT.parent)


if __name__ == "__main__":
    sys.exit(main())
