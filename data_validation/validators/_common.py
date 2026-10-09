"""Shared helpers for the validators and QC tools.

Every check reports Finding objects. An ERROR is something that is wrong
(an unknown DSGAI ID, a schema violation, a malformed CVE ID) and fails a
run. A WARN is a heuristic hit (something that looks like PII, a likely
duplicate) that a reviewer should look at, and does not fail a run.
"""
from __future__ import annotations

import csv
import json
import sys
from collections.abc import Iterator
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DV_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = DV_ROOT.parent
DATASETS_ROOT = REPO_ROOT / "datasets"
REFERENCE_DIR = DV_ROOT / "reference_data"
SCHEMAS_DIR = DV_ROOT / "schemas"
TAXONOMY_PATH = DATASETS_ROOT / "_shared" / "dsgai_taxonomy.json"

ERROR = "ERROR"
WARN = "WARN"

# Folders under a dataset that hold tooling or deliberately invalid fixtures,
# not data.
SKIP_DIRS = {"tests", "fixtures", "__pycache__", "node_modules"}

# Container keys: a file whose top-level object holds a list of records under
# one of these keys is treated as one record per list item.
CONTAINER_KEYS = ("test_cases", "entries", "cases")

# The field that identifies a record, in the order they are tried.
ID_FIELDS = (
    "vulnerability_id", "exploit_id", "assessment_id", "trace_id",
    "testcase_id", "document_id", "incident_id", "id",
)


@dataclass(frozen=True)
class Finding:
    level: str
    check: str
    path: Path
    location: str
    message: str

    def format(self, base: Path | None = None) -> str:
        shown = self.path
        if base is not None:
            with suppress(ValueError):
                shown = self.path.resolve().relative_to(base.resolve())
        where = f"{shown.as_posix()}: {self.location}" if self.location else shown.as_posix()
        return f"{self.level:<5} [{self.check}] {where}: {self.message}"


def is_data_file(path: Path, root: Path) -> bool:
    """A JSON file under root that holds data, not a schema, Croissant metadata or a test fixture."""
    if path.suffix != ".json" or path.name in ("schema.json", "croissant.json") or path.name.endswith(".schema.json"):
        return False
    rel = path.relative_to(root).parts[:-1]
    return not any(p in SKIP_DIRS or p.startswith((".", "_")) for p in rel)


def iter_data_files(root: Path) -> list[Path]:
    """Data files under root (a dataset directory, or a single file)."""
    if root.is_file():
        return [root]
    return sorted(p for p in root.rglob("*.json") if is_data_file(p, root))


def load_json(path: Path, check: str) -> tuple[Any, Finding | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return None, Finding(ERROR, check, path, "", f"cannot be read as JSON: {exc}")


def iter_records(data: Any) -> Iterator[tuple[str, dict]]:
    """(JSON pointer, record) for each record in a file."""
    if isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, dict):
                yield f"/{i}", item
        return
    if not isinstance(data, dict):
        return
    for key in CONTAINER_KEYS:
        items = data.get(key)
        if isinstance(items, list) and items and all(isinstance(i, dict) for i in items):
            for i, item in enumerate(items):
                yield f"/{key}/{i}", item
            return
    yield "", data


def record_id(record: dict) -> str | None:
    for field in ID_FIELDS:
        value = record.get(field)
        if isinstance(value, str) and value:
            return value
    return None


def walk_strings(obj: Any, pointer: str = "", key: str | None = None) -> Iterator[tuple[str, str | None, str]]:
    """(JSON pointer, key the string sits under, string) for every string in obj."""
    if isinstance(obj, str):
        yield pointer or "<root>", key, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, f"{pointer}/{k}", str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, f"{pointer}/{i}", key)


def load_taxonomy_ids(datasets_root: Path | None = None) -> set[str]:
    """DSGAI IDs from datasets/_shared/dsgai_taxonomy.json."""
    path = TAXONOMY_PATH
    if datasets_root is not None:
        candidate = datasets_root / "_shared" / "dsgai_taxonomy.json"
        if candidate.is_file():
            path = candidate
    data = json.loads(path.read_text(encoding="utf-8"))
    return {e["id"] for e in data["entries"]}


def load_reference_ids(filename: str, column: str) -> set[str]:
    with open(REFERENCE_DIR / filename, newline="", encoding="utf-8") as fh:
        return {row[column] for row in csv.DictReader(fh) if row.get(column)}


def dataset_dirs(datasets_root: Path = DATASETS_ROOT) -> list[Path]:
    """Dataset directories, skipping shared (_shared) and hidden folders."""
    return sorted(p for p in datasets_root.iterdir() if p.is_dir() and not p.name.startswith(("_", ".")))


def load_dataset_records(datasets_root: Path = DATASETS_ROOT) -> dict[str, list[tuple[Path, dict]]]:
    """{dataset name: [(file, record), ...]} for every dataset; example.json files skipped."""
    out: dict[str, list[tuple[Path, dict]]] = {}
    for d in dataset_dirs(datasets_root):
        records: list[tuple[Path, dict]] = []
        for path in iter_data_files(d):
            if path.name == "example.json":
                continue
            data, err = load_json(path, "load")
            if err is None:
                records.extend((path, rec) for _ptr, rec in iter_records(data))
        out[d.name] = records
    return out


def dataset_root_of(path: Path, datasets_root: Path = DATASETS_ROOT) -> Path:
    """The top-level dataset directory a file belongs to (its parent if outside datasets/)."""
    path = path.resolve()
    try:
        rel = path.relative_to(datasets_root.resolve())
    except ValueError:
        return path.parent if path.is_file() else path
    return datasets_root.resolve() / rel.parts[0] if len(rel.parts) > 1 else path


def add_target_args(parser) -> None:
    parser.add_argument("--file", action="append", default=[],
                        help="A data file to check (repeatable)")
    parser.add_argument("--dataset", action="append", default=[],
                        help="A dataset directory to check (repeatable; default: every dataset)")


def resolve_targets(args, datasets_root: Path = DATASETS_ROOT) -> list[Path] | None:
    """Files named by --file/--dataset, or every data file. None if a path is missing."""
    files: list[Path] = []
    for f in args.file:
        p = Path(f)
        if not p.is_file():
            print(f"File not found: {f}")
            return None
        files.append(p.resolve())
    for d in args.dataset:
        p = Path(d)
        if not p.is_dir():
            print(f"Directory not found: {d}")
            return None
        files.extend(iter_data_files(p.resolve()))
    if not args.file and not args.dataset:
        files = iter_data_files(datasets_root)
    return files


def print_findings(findings: list[Finding], base: Path | None = None) -> int:
    """Print findings and a summary line. Returns the exit code (1 if any ERROR)."""
    for f in findings:
        print(f.format(base))
    errors = sum(f.level == ERROR for f in findings)
    warnings = len(findings) - errors
    print(f"{errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


def ensure_utf8_stdout() -> None:
    """Dataset text is multilingual; don't crash on a cp1252 console."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="replace")
