#!/usr/bin/env python3
"""Validate the Turkish contrastive prompt-injection contribution."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - exercised only in incomplete environments
    raise SystemExit(
        "jsonschema is required; install data_validation/requirements.txt"
    ) from exc

from build_cases import (  # noqa: E402
    ADAPTATION_CHANGES,
    ADAPTATION_LICENSE,
    ADAPTATION_LICENSE_URL,
    CONTRIBUTED_SOURCE_PAIRS,
    EXCLUDED_PAIRS,
    FAMILIES,
    MANIFEST_FIELDNAMES,
    SOURCE_ATTRIBUTION,
    SOURCE_DATASET,
    SOURCE_DISTRIBUTION_URL,
    SOURCE_DOI,
    SOURCE_FILE_SHA256,
    SOURCE_LICENSE,
    SOURCE_LICENSE_URL,
    SOURCE_REPOSITORY,
    SOURCE_REVISION,
    SOURCE_VERSION,
    classify_case,
    languages_for,
    load_source,
    primary_language_for,
    sha256_bytes,
    sha256_text,
)


CASE_COUNT = len(CONTRIBUTED_SOURCE_PAIRS)
NEAR_DUPLICATE_THRESHOLD = 0.92

EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
IPV4_RE = re.compile(r"(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)")
IBAN_RE = re.compile(r"\bTR\d{24}\b", re.IGNORECASE)
PHONE_RE = re.compile(r"(?<!\d)(?:\+?90[\s.-]?)?0?5\d{2}(?:[\s.-]?\d{3})(?:[\s.-]?\d{2}){2}(?!\d)")
TCKN_RE = re.compile(r"(?<!\d)\d{11}(?!\d)")
LIVE_SECRET_RE = re.compile(
    r"\b(?:sk-[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{20,})\b"
)
NAMED_VENDOR_RE = re.compile(
    r"\b(?:OpenAI|Anthropic|Google|Microsoft|Amazon|Meta|Apple|GitHub|Slack|Salesforce)\b",
    re.IGNORECASE,
)


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    normalized = re.sub(r"[^\w\s]", " ", normalized, flags=re.UNICODE)
    return " ".join(normalized.split())


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def extract_prompts(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        if isinstance(value.get("prompt"), str):
            yield value["prompt"]
        for key, child in value.items():
            if key == "contrastive_control":
                continue
            yield from extract_prompts(child)
    elif isinstance(value, list):
        for child in value:
            yield from extract_prompts(child)


def extract_testcase_ids(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        if isinstance(value.get("testcase_id"), str):
            yield value["testcase_id"]
        for child in value.values():
            yield from extract_testcase_ids(child)
    elif isinstance(value, list):
        for child in value:
            yield from extract_testcase_ids(child)


def find_external_prompts(contribution_root: Path) -> list[tuple[str, str]]:
    dataset_root = contribution_root.parent
    prompts: list[tuple[str, str]] = []
    for path in sorted(dataset_root.rglob("*.json")):
        if contribution_root in path.parents:
            continue
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for prompt in extract_prompts(value):
            prompts.append((str(path.relative_to(dataset_root)), prompt))
    return prompts


def find_external_testcase_ids(contribution_root: Path) -> dict[str, list[str]]:
    dataset_root = contribution_root.parent
    locations: dict[str, list[str]] = {}
    for path in sorted(dataset_root.rglob("*.json")):
        if contribution_root in path.parents:
            continue
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        relative_path = str(path.relative_to(dataset_root))
        for testcase_id in extract_testcase_ids(value):
            locations.setdefault(testcase_id, []).append(relative_path)
    return locations


def validate_attribution_readme(root: Path) -> None:
    readme = (root / "README.md").read_text(encoding="utf-8")
    expected = "| Attribution | Enes Deniz, Copyright © 2026 |"
    if expected not in readme:
        raise ValueError("README source attribution row is missing or changed")
    if readme.count("Enes Deniz") != 1:
        raise ValueError("README must keep source attribution in one canonical location")
    if "| Affiliation | AltaySec |" not in readme:
        raise ValueError("README source affiliation row is missing or changed")
    if "## Source and attribution" not in readme:
        raise ValueError("README source attribution anchor is missing")


def check_pairwise_near_duplicates(
    items: list[tuple[str, str]],
    label: str,
) -> tuple[float, str, str]:
    maximum = (0.0, "", "")
    for index, (left, left_id) in enumerate(items):
        for right, right_id in items[index + 1 :]:
            ratio = SequenceMatcher(None, left, right, autojunk=False).ratio()
            if ratio > maximum[0]:
                maximum = (ratio, left_id, right_id)
            if ratio >= NEAR_DUPLICATE_THRESHOLD:
                raise ValueError(f"near-duplicate {label}: {left_id}/{right_id} ratio={ratio:.3f}")
    return maximum


def check_cross_near_duplicates(
    left_items: list[tuple[str, str]],
    right_items: list[tuple[str, str]],
    label: str,
    skip_matching_ids: bool = False,
) -> tuple[float, str, str]:
    maximum = (0.0, "", "")
    for left, left_id in left_items:
        for right, right_id in right_items:
            if skip_matching_ids and left_id == right_id:
                continue
            ratio = SequenceMatcher(None, left, right, autojunk=False).ratio()
            if ratio > maximum[0]:
                maximum = (ratio, left_id, right_id)
            if ratio >= NEAR_DUPLICATE_THRESHOLD:
                raise ValueError(f"near-duplicate {label}: {left_id}/{right_id} ratio={ratio:.3f}")
    return maximum


def validate_source(
    source_root: Path,
    cases_by_pair: dict[str, dict[str, Any]],
) -> None:
    all_rows, row_source_file = load_source(source_root)
    rows_by_id = {row["id"]: row for row in all_rows}
    for pair_id, case in cases_by_pair.items():
        provenance = case["provenance"]
        attack_id = provenance["source_attack_record_id"]
        control_id = provenance["source_control_record_id"]
        attack = rows_by_id.get(attack_id)
        control = rows_by_id.get(control_id)
        if attack is None or control is None:
            raise ValueError(f"{pair_id}: source record missing")
        if attack["pair_id"] != pair_id or control["pair_id"] != pair_id:
            raise ValueError(f"{pair_id}: source pair identity mismatch")
        if attack["label"] != 1 or control["label"] != 0:
            raise ValueError(f"{pair_id}: source labels do not form an attack/control pair")
        if control["category"] != "benign_boundary":
            raise ValueError(f"{pair_id}: source control is not benign_boundary")
        if attack["split"] != control["split"] or attack["split"] != provenance["source_split"]:
            raise ValueError(f"{pair_id}: source split lineage mismatch")
        if attack["text"] != case["prompt"]:
            raise ValueError(f"{pair_id}: attack text differs from pinned source")
        if control["text"] != case["contrastive_control"]["prompt"]:
            raise ValueError(f"{pair_id}: control text differs from pinned source")
        if (
            row_source_file[attack_id] != provenance["source_file"]
            or row_source_file[control_id] != provenance["source_file"]
        ):
            raise ValueError(f"{pair_id}: source-file mapping mismatch")
        if case["source_context"] != attack["source_context"]:
            raise ValueError(f"{pair_id}: source context differs from pinned source")
        if case["language"] != primary_language_for(attack):
            raise ValueError(f"{pair_id}: primary language differs from content review")
        if case["languages"] != languages_for(attack):
            raise ValueError(f"{pair_id}: language inventory differs from content review")
        if provenance["source_attack_sha256"] != sha256_text(attack["text"]):
            raise ValueError(f"{pair_id}: source attack hash mismatch")
        if provenance["source_control_sha256"] != sha256_text(control["text"]):
            raise ValueError(f"{pair_id}: source control hash mismatch")
        category, mappings, severity, scope = classify_case(attack)
        if (
            case["category"],
            case["dsgai_mapping"],
            case["severity"],
            case["scope"],
        ) != (category, mappings, severity, scope):
            raise ValueError(f"{pair_id}: deterministic mapping mismatch")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        help="Optional source dataset checkout for full pinned-source verification",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    repo_root = root.parents[2]
    schema_path = repo_root / "data_validation/schemas/promptinj_testcase.schema.json"
    extension_schema_path = root / "contrastive_testcase.schema.json"
    taxonomy_path = repo_root / "data_validation/reference_data/dsgai_entries.json"
    schema = load_json(schema_path)
    extension_schema = load_json(extension_schema_path)
    jsonschema.Draft7Validator.check_schema(schema)
    jsonschema.Draft7Validator.check_schema(extension_schema)
    taxonomy = {entry["id"] for entry in json.loads(taxonomy_path.read_text(encoding="utf-8"))}
    validate_attribution_readme(root)

    case_paths = sorted((root / "cases").glob("TC-*.json"))
    if len(case_paths) != CASE_COUNT:
        raise ValueError(f"expected {CASE_COUNT} case files, found {len(case_paths)}")

    expected_ids = [
        f"TC-{300 + int(pair_id.rsplit('_', 1)[1]):04d}"
        for pair_id in sorted(CONTRIBUTED_SOURCE_PAIRS)
    ]
    external_id_locations = find_external_testcase_ids(root)
    id_collisions = sorted(set(expected_ids) & set(external_id_locations))
    if id_collisions:
        details = [
            f"{testcase_id}={','.join(external_id_locations[testcase_id])}"
            for testcase_id in id_collisions
        ]
        raise ValueError("testcase ID collision with existing repository data: " + "; ".join(details))

    manifest_path = root / "manifest.csv"
    with manifest_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(MANIFEST_FIELDNAMES):
            raise ValueError("manifest header differs from the canonical field order")
        manifest_rows = list(reader)
    if len(manifest_rows) != CASE_COUNT:
        raise ValueError(f"expected {CASE_COUNT} manifest rows, found {len(manifest_rows)}")
    manifest_by_id = {row["testcase_id"]: row for row in manifest_rows}
    if set(manifest_by_id) != set(expected_ids):
        raise ValueError("manifest testcase IDs are incomplete or duplicated")

    cases: list[dict[str, Any]] = []
    cases_by_pair: dict[str, dict[str, Any]] = {}
    attack_norms: dict[str, str] = {}
    control_norms: dict[str, str] = {}
    pii_findings: list[str] = []

    for expected_id, path in zip(expected_ids, case_paths):
        case = load_json(path)
        jsonschema.validate(case, schema)
        jsonschema.validate(case, extension_schema)
        testcase_id = case["testcase_id"]
        if testcase_id != expected_id or path.stem != testcase_id:
            raise ValueError(f"{path}: ID/path mismatch (expected {expected_id})")
        if case.get("$schema") != "../../../../data_validation/schemas/promptinj_testcase.schema.json":
            raise ValueError(f"{testcase_id}: incorrect schema reference")
        if case.get("synthetic_data_only") is not True:
            raise ValueError(f"{testcase_id}: synthetic_data_only must be true")
        if case.get("technique") not in FAMILIES:
            raise ValueError(f"{testcase_id}: unknown technique")
        if not set(case["dsgai_mapping"]).issubset(taxonomy):
            raise ValueError(f"{testcase_id}: non-canonical DSGAI mapping")
        provenance = case["provenance"]
        expected_static_provenance = {
            "source_dataset": SOURCE_DATASET,
            "source_version": SOURCE_VERSION,
            "source_repository": SOURCE_REPOSITORY,
            "source_distribution_url": SOURCE_DISTRIBUTION_URL,
            "source_revision": SOURCE_REVISION,
            "source_release_doi": SOURCE_DOI,
            "source_license": SOURCE_LICENSE,
            "source_license_url": SOURCE_LICENSE_URL,
            "source_attribution": SOURCE_ATTRIBUTION,
            "adaptation_license": ADAPTATION_LICENSE,
            "adaptation_license_url": ADAPTATION_LICENSE_URL,
            "changes": list(ADAPTATION_CHANGES),
        }
        for field, expected in expected_static_provenance.items():
            if provenance[field] != expected:
                raise ValueError(
                    f"{testcase_id}: provenance {field} mismatch: "
                    f"{provenance[field]!r} != {expected!r}"
                )
        pair_number = int(testcase_id[3:]) - 300
        pair_id = provenance["source_pair_id"]
        expected_pair_id = f"pair_{pair_number:04d}"
        if pair_id in EXCLUDED_PAIRS:
            raise ValueError(f"{testcase_id}: excluded source-quality pair was emitted")
        expected_attack_id = f"tcpi_p{pair_number:04d}_a"
        expected_control_id = f"tcpi_p{pair_number:04d}_b"
        if pair_id != expected_pair_id:
            raise ValueError(f"{testcase_id}: source pair is not sequential")
        if provenance["source_attack_record_id"] != expected_attack_id:
            raise ValueError(f"{testcase_id}: source attack ID mismatch")
        if provenance["source_control_record_id"] != expected_control_id:
            raise ValueError(f"{testcase_id}: source control ID mismatch")
        if case["contrastive_control"]["source_record_id"] != expected_control_id:
            raise ValueError(f"{testcase_id}: contrastive control ID mismatch")
        expected_source = (
            f"{SOURCE_DATASET} v{SOURCE_VERSION}, pair {pair_id}; "
            f"CC BY 4.0; {SOURCE_DISTRIBUTION_URL}"
        )
        if case["source"] != expected_source:
            raise ValueError(f"{testcase_id}: human-readable source citation mismatch")
        split_to_file = {
            "train": "data/train.jsonl",
            "validation": "data/validation.jsonl",
            "test": "data/test.jsonl",
        }
        source_split = provenance["source_split"]
        source_file = provenance["source_file"]
        if split_to_file.get(source_split) != source_file:
            raise ValueError(f"{testcase_id}: source split/file mismatch")
        if case["provenance"]["source_file_sha256"] != SOURCE_FILE_SHA256[source_file]:
            raise ValueError(f"{testcase_id}: source file hash mismatch")
        expected_category, expected_mappings, expected_severity, expected_scope = classify_case(
            {"attack_family": case["technique"], "pair_id": pair_id}
        )
        if (
            case["category"],
            case["dsgai_mapping"],
            case["severity"],
            case["scope"],
        ) != (expected_category, expected_mappings, expected_severity, expected_scope):
            raise ValueError(f"{testcase_id}: content-reviewed classification mismatch")

        attack = case["prompt"]
        control = case["contrastive_control"]["prompt"]
        attack_sha256 = sha256_text(attack)
        control_sha256 = sha256_text(control)
        if case["integrity"]["attack_prompt_sha256"] != attack_sha256:
            raise ValueError(f"{testcase_id}: attack prompt hash mismatch")
        if case["integrity"]["control_prompt_sha256"] != control_sha256:
            raise ValueError(f"{testcase_id}: control prompt hash mismatch")
        if provenance["source_attack_sha256"] != attack_sha256:
            raise ValueError(f"{testcase_id}: provenance attack hash mismatch")
        if provenance["source_control_sha256"] != control_sha256:
            raise ValueError(f"{testcase_id}: provenance control hash mismatch")
        language_input = {"text": attack, "pair_id": pair_id}
        if case["language"] != primary_language_for(language_input):
            raise ValueError(f"{testcase_id}: primary language mismatch")
        if case["languages"] != languages_for(language_input):
            raise ValueError(f"{testcase_id}: language inventory mismatch")
        attack_norm = normalize_text(attack)
        control_norm = normalize_text(control)
        if not attack_norm or not control_norm or attack_norm == control_norm:
            raise ValueError(f"{testcase_id}: invalid contrastive pair")
        if attack_norm in attack_norms:
            raise ValueError(f"{testcase_id}: duplicate attack prompt with {attack_norms[attack_norm]}")
        if control_norm in control_norms:
            raise ValueError(f"{testcase_id}: duplicate control prompt with {control_norms[control_norm]}")
        attack_norms[attack_norm] = testcase_id
        control_norms[control_norm] = testcase_id

        for label, text in (("attack", attack), ("control", control)):
            for pattern_name, pattern in (
                ("email", EMAIL_RE),
                ("IPv4", IPV4_RE),
                ("IBAN", IBAN_RE),
                ("phone", PHONE_RE),
                ("TCKN-like", TCKN_RE),
                ("live-secret", LIVE_SECRET_RE),
                ("named-vendor", NAMED_VENDOR_RE),
            ):
                if pattern.search(text):
                    pii_findings.append(f"{testcase_id}:{label}:{pattern_name}")

        if pair_id in cases_by_pair:
            raise ValueError(f"duplicate source pair ID: {pair_id}")
        cases_by_pair[pair_id] = case

        row = manifest_by_id[testcase_id]
        serialized = path.read_bytes()
        expected_manifest = {
            "output_file": f"cases/{testcase_id}.json",
            "source_pair_id": pair_id,
            "source_attack_record_id": case["provenance"]["source_attack_record_id"],
            "source_control_record_id": case["provenance"]["source_control_record_id"],
            "attack_family": case["technique"],
            "source_context": case["source_context"],
            "source_split": case["provenance"]["source_split"],
            "category": case["category"],
            "dsgai_mapping": "|".join(case["dsgai_mapping"]),
            "severity": case["severity"],
            "scope": case["scope"],
            "source_file": source_file,
            "source_file_sha256": case["provenance"]["source_file_sha256"],
            "attack_prompt_sha256": case["integrity"]["attack_prompt_sha256"],
            "control_prompt_sha256": case["integrity"]["control_prompt_sha256"],
            "case_file_sha256": sha256_bytes(serialized),
            "source_revision": SOURCE_REVISION,
        }
        for field, expected in expected_manifest.items():
            if row[field] != expected:
                raise ValueError(
                    f"{testcase_id}: manifest {field} mismatch: {row[field]!r} != {expected!r}"
                )
        cases.append(case)

    if pii_findings:
        raise ValueError("sensitive or named-entity patterns found: " + ", ".join(pii_findings))

    cross_exact = sorted(set(attack_norms) & set(control_norms))
    if cross_exact:
        details = [
            f"{attack_norms[value]}:attack={control_norms[value]}:control"
            for value in cross_exact
        ]
        raise ValueError("exact attack/control collision: " + ", ".join(details))

    external_prompts = find_external_prompts(root)
    normalized_attacks = list(attack_norms.items())
    normalized_controls = list(control_norms.items())
    external_normalized = [
        (normalized, path)
        for path, prompt in external_prompts
        for normalized in [normalize_text(prompt)]
        if normalized
    ]
    external_norms = {normalized: path for normalized, path in external_normalized}
    for label, contribution_norms in (
        ("attack", attack_norms),
        ("control", control_norms),
    ):
        overlaps = sorted(set(contribution_norms) & set(external_norms))
        if overlaps:
            details = [
                f"{contribution_norms[value]}={external_norms[value]}"
                for value in overlaps
            ]
            raise ValueError(
                f"exact {label} overlap with existing repository prompts: "
                + ", ".join(details)
            )

    max_internal_attacks = check_pairwise_near_duplicates(
        normalized_attacks, "contributed attacks"
    )
    max_internal_controls = check_pairwise_near_duplicates(
        normalized_controls, "contributed controls"
    )
    max_unpaired_cross = check_cross_near_duplicates(
        normalized_attacks,
        normalized_controls,
        "unpaired attack/control prompts",
        skip_matching_ids=True,
    )
    max_external_attacks = check_cross_near_duplicates(
        normalized_attacks,
        external_normalized,
        "attack versus existing repository prompt",
    )
    max_external_controls = check_cross_near_duplicates(
        normalized_controls,
        external_normalized,
        "control versus existing repository prompt",
    )

    paired_similarity = (0.0, "", "")
    for attack_norm, testcase_id in normalized_attacks:
        control_norm = next(
            normalized
            for normalized, control_id in normalized_controls
            if control_id == testcase_id
        )
        ratio = SequenceMatcher(None, attack_norm, control_norm, autojunk=False).ratio()
        if ratio > paired_similarity[0]:
            paired_similarity = (ratio, testcase_id, testcase_id)

    if args.source:
        validate_source(args.source.resolve(), cases_by_pair)

    family_counts = Counter(case["technique"] for case in cases)
    category_counts = Counter(case["category"] for case in cases)
    mapping_counts = Counter(mapping for case in cases for mapping in case["dsgai_mapping"])
    severity_counts = Counter(case["severity"] for case in cases)
    scope_counts = Counter(case["scope"] for case in cases)
    split_counts = Counter(case["provenance"]["source_split"] for case in cases)

    print(f"Validated {len(cases)} schema-conformant contrastive test cases.")
    print(f"Families: {dict(sorted(family_counts.items()))}")
    print(f"Categories: {dict(sorted(category_counts.items()))}")
    print(f"DSGAI mappings: {dict(sorted(mapping_counts.items()))}")
    print(f"Severity: {dict(sorted(severity_counts.items()))}")
    print(f"Scope: {dict(sorted(scope_counts.items()))}")
    print(f"Source splits: {dict(sorted(split_counts.items()))}")
    print("Exact attack/control collisions: 0")
    print("Exact attack or control overlaps with existing cases: 0")
    print(
        "Maximum internal attack similarity: "
        f"{max_internal_attacks[0]:.3f} "
        f"({max_internal_attacks[1]}, {max_internal_attacks[2]})"
    )
    print(
        "Maximum internal control similarity: "
        f"{max_internal_controls[0]:.3f} "
        f"({max_internal_controls[1]}, {max_internal_controls[2]})"
    )
    print(
        "Maximum unpaired attack/control similarity: "
        f"{max_unpaired_cross[0]:.3f} "
        f"({max_unpaired_cross[1]}, {max_unpaired_cross[2]})"
    )
    print(
        "Maximum paired attack/control similarity (reported, not failed): "
        f"{paired_similarity[0]:.3f} ({paired_similarity[1]})"
    )
    print(
        "Maximum attack similarity to an existing case: "
        f"{max_external_attacks[0]:.3f} "
        f"({max_external_attacks[1]}, {max_external_attacks[2]})"
    )
    print(
        "Maximum control similarity to an existing case: "
        f"{max_external_controls[0]:.3f} "
        f"({max_external_controls[1]}, {max_external_controls[2]})"
    )
    print("Sensitive-data and named-vendor pattern findings: 0")
    if args.source:
        print(
            "Pinned source text, pair identity, split, repository revision, "
            "release tag, metadata, and file hashes: verified"
        )


if __name__ == "__main__":
    try:
        main()
    except (KeyError, OSError, TypeError, ValueError, jsonschema.ValidationError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
