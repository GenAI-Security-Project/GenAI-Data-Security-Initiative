"""End-to-end tests for ../validate.py against the fixtures in fixtures/.

These run `validate.py` as a subprocess, the same way a contributor or CI
does, rather than importing its functions - so a refactor of validate.py's
internals cannot silently stop testing anything as long as the CLI's
contract (exit code, stderr/stdout message) holds. Each fixture in
fixtures/ is a full trace built from valid_minimal.json with exactly one
change, so a fixture that starts passing again means the check for that
change stopped firing.

Every fixture below is a case emmanuelgjr asked to keep from rotting during
review of #62: "With CI now running the validator, a small tests/ of known
-bad fixtures would keep them from rotting."
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

# name -> a substring that must appear in validate.py's output when this
# fixture is the only entry, so a failure for the WRONG reason still fails
# the test.
BROKEN_FIXTURES: dict[str, str] = {
    "span-self-parent": "which is not a preceding span",
    "span-backwards-offset": "moves t_offset_ms backwards",
    "span-dangling-parent": "which is not a preceding span",
    "secret-bearer-token": "bearer credential",
    "secret-internal-hostname": "internal hostname",
    "secret-credential-assignment": "secret-looking assignment",
    "secret-public-ip-cluster": "real routable IPv4 addresses",
    "date-added-not-iso": "is not an ISO 8601 date",
    "span-timestamp-not-iso": "is not an ISO 8601 date-time",
    "provenance-missing-evidence": "requires at least one",
    "evidence-citation-bad-cve-form": "is not a CVE id",
    "evidence-citation-bad-url-form": "is not an absolute http",
    "evidence-missing-supports": "'supports' is a required property",
    "sanitization-attestation-false": "was expected",
    "dsgai-mapping-off-enum": "is not one of",
    "filename-trace-id-mismatch": "does not match the filename stem",
}


def _run_validate(tmp_path: Path) -> subprocess.CompletedProcess:
    # Run the COPY staged into tmp_path, not the real ROOT/validate.py.
    # validate.py resolves its own ROOT from __file__, not from cwd, so
    # running the original file here would silently validate the real
    # (empty) entries/ in the source tree instead of the fixture.
    return subprocess.run(
        [sys.executable, str(tmp_path / "validate.py")],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )


def _stage(tmp_path: Path) -> Path:
    """Set up a dataset directory: real schema/example, a copy of the real
    shared taxonomy one level up (validate.py looks for it at
    ROOT.parent / "_shared", so the fixture tree needs the same shape
    relative to itself), and an empty entries/ for the caller to populate."""
    shutil.copy(ROOT / "schema.json", tmp_path / "schema.json")
    shutil.copy(ROOT / "example.json", tmp_path / "example.json")
    shutil.copy(ROOT / "validate.py", tmp_path / "validate.py")

    shared_dir = tmp_path.parent / "_shared"
    shared_dir.mkdir(exist_ok=True)
    taxonomy_dest = shared_dir / "dsgai_taxonomy.json"
    if not taxonomy_dest.exists():
        shutil.copy(ROOT.parent / "_shared" / "dsgai_taxonomy.json", taxonomy_dest)

    entries = tmp_path / "entries"
    entries.mkdir(exist_ok=True)
    return entries


@pytest.fixture
def entries_dir(tmp_path):
    return _stage(tmp_path)


def test_valid_minimal_passes(tmp_path, entries_dir):
    entry = json.loads((FIXTURES_DIR / "valid_minimal.json").read_text())
    (entries_dir / f"{entry['trace_id']}.json").write_text(json.dumps(entry))

    result = _run_validate(tmp_path)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK" in result.stdout


@pytest.mark.parametrize("fixture_name,expected_substring", sorted(BROKEN_FIXTURES.items()))
def test_broken_fixture_fails(tmp_path, entries_dir, fixture_name, expected_substring):
    entry = json.loads((FIXTURES_DIR / f"{fixture_name}.json").read_text())

    if fixture_name == "filename-trace-id-mismatch":
        # The one fixture whose whole point is that its filename does NOT
        # match trace_id - name the file after the fixture, not the trace_id.
        dest = entries_dir / f"{fixture_name}.json"
    else:
        dest = entries_dir / f"{entry['trace_id']}.json"
    dest.write_text(json.dumps(entry))

    result = _run_validate(tmp_path)

    assert result.returncode == 1, (
        f"{fixture_name} was expected to fail validate.py but exit code was "
        f"{result.returncode}\n{result.stdout}{result.stderr}"
    )
    assert expected_substring in result.stdout, (
        f"{fixture_name} failed, but not with the expected message "
        f"({expected_substring!r} not found)\n{result.stdout}"
    )


def test_every_fixture_file_is_covered():
    """Every .json in fixtures/ other than the valid base is exercised by
    BROKEN_FIXTURES above - a fixture nobody references is not testing
    anything."""
    on_disk = {p.stem for p in FIXTURES_DIR.glob("*.json")} - {"valid_minimal"}
    assert on_disk == set(BROKEN_FIXTURES), (
        "fixtures/ and BROKEN_FIXTURES have drifted apart: "
        f"on disk but not tested: {on_disk - set(BROKEN_FIXTURES)}; "
        f"tested but missing from disk: {set(BROKEN_FIXTURES) - on_disk}"
    )
