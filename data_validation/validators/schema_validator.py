"""
Validates data files against their JSON Schema. Also covers completeness:
required fields and allowed values are what the schemas define.

The schema for a file is found in this order:
  1. the file's own "$schema" key, when it is a relative path
     (entries/*.json use "../schema.json"; the Turkish test cases point at
     data_validation/schemas/promptinj_testcase.schema.json)
  2. the nearest schema.json in the file's folder or a parent folder,
     up to the dataset directory
  3. data_validation/schemas/ for datasets that have no schema.json of
     their own (incident, rag, crossframework_mapping)
A file with no schema found is reported as a warning.

Usage:
    python schema_validator.py --file ../../datasets/rag_dataset/RAG-0001.json
    python schema_validator.py --dataset ../../datasets/rag_dataset/
    python schema_validator.py --file entry.json --schema ../schemas/rag.schema.json
"""
from __future__ import annotations

import argparse
import json
import sys
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import url2pathname

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import (  # noqa: E402
    DATASETS_ROOT, ERROR, SCHEMAS_DIR, WARN, Finding, add_target_args,
    dataset_root_of, ensure_utf8_stdout, load_json, print_findings, resolve_targets,
)

CHECK = "schema"

# Datasets whose only schema lives in data_validation/schemas/.
FALLBACK_SCHEMAS = {
    "incident_dataset": "incident.schema.json",
    "rag_dataset": "rag.schema.json",
    "crossframework_mapping_dataset": "crossframework_mapping.schema.json",
}


def find_schema(path: Path, data, dataset_root: Path | None = None) -> Path | None:
    """The schema file for a data file, or None (see the module docstring)."""
    ref = data.get("$schema") if isinstance(data, dict) else None
    if isinstance(ref, str) and not ref.startswith(("http://", "https://")):
        return (path.parent / ref).resolve()
    root = (dataset_root or dataset_root_of(path)).resolve()
    folder = path.resolve().parent
    while True:
        if (folder / "schema.json").is_file():
            return folder / "schema.json"
        if folder == root or folder.parent == folder:
            break
        folder = folder.parent
    fallback = FALLBACK_SCHEMAS.get(root.name)
    return SCHEMAS_DIR / fallback if fallback else None


def _retrieve(uri: str):
    from referencing import Resource
    from referencing.jsonschema import DRAFT202012
    parsed = urlparse(uri)
    if parsed.scheme != "file":
        raise LookupError(f"only local schema references are resolved: {uri}")
    contents = json.loads(Path(url2pathname(unquote(parsed.path))).read_text(encoding="utf-8"))
    return Resource.from_contents(contents, default_specification=DRAFT202012)


@lru_cache(maxsize=None)
def _validator(schema_path: Path):
    from jsonschema.validators import validator_for
    from referencing import Registry
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    # An $id lets relative "$ref"s in the schema resolve against its own location.
    schema = {**schema, "$id": schema_path.as_uri()}
    cls = validator_for(schema)
    return cls(schema, registry=Registry(retrieve=_retrieve), format_checker=cls.FORMAT_CHECKER)


def validate_file(path: Path, schema_path: Path | None = None, dataset_root: Path | None = None) -> list[Finding]:
    """Validate one file. Returns findings (empty when it passes)."""
    data, err = load_json(path, CHECK)
    if err:
        return [err]
    schema_path = schema_path or find_schema(path, data, dataset_root)
    if schema_path is None:
        return [Finding(WARN, CHECK, path, "", "no schema found for this file, so it was not schema-checked")]
    if not schema_path.is_file():
        return [Finding(ERROR, CHECK, path, "/$schema", f"schema not found: {schema_path}")]
    findings = []
    for e in _validator(schema_path.resolve()).iter_errors(data):
        loc = "/" + "/".join(str(p) for p in e.absolute_path) if e.absolute_path else "<root>"
        findings.append(Finding(ERROR, CHECK, path, loc, e.message))
    return findings


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Validate data files against their JSON Schema")
    add_target_args(parser)
    parser.add_argument("--schema", help="Use this schema instead of finding one per file")
    args = parser.parse_args(argv)
    files = resolve_targets(args)
    if files is None:
        return 2
    schema = Path(args.schema).resolve() if args.schema else None
    findings = [f for p in files for f in validate_file(p, schema)]
    print(f"Checked {len(files)} file(s)")
    return print_findings(findings, DATASETS_ROOT.parent)


if __name__ == "__main__":
    sys.exit(main())
