"""
Run every dataset's own validator, then the shared checks, and report one
result per dataset.

1. Dataset validators. Each validate.py inside a dataset (at its root, or in
   a sub-collection such as one contributor's folder of cases) is run in its
   own directory. These are authoritative for their data. Datasets without
   one are listed as "no validator" so the gap is visible instead of
   silently passing.
2. Shared checks (data_validation/validators/) on every data file:
   schema (for files no dataset validator covers), DSGAI IDs, CVE/CWE/ATLAS
   and OWASP Top 10 IDs, CVSS scores and ratings, dates, anonymization
   patterns and duplicates. Errors fail the run;
   heuristic warnings (anonymization, near-duplicates, retired IDs) are
   counted, and printed with --verbose.

Usage:
    python run_all_checks.py                      # every dataset under ../datasets
    python run_all_checks.py --dataset ../datasets/exploit_dataset
    python run_all_checks.py --verbose            # print each validator's output and every warning
    python run_all_checks.py --strict             # warnings fail the run too

Exit code: 0 when everything that ran passed, 1 when any validator failed
or any shared check reported an error, 2 when the arguments name nothing
that can be checked.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validators import (  # noqa: E402
    anonymization_scanner, crossref_validator, date_check, dedup_checker, dsgai_mapping_check,
    schema_validator, severity_check,
)
from validators._common import (  # noqa: E402
    ERROR, SKIP_DIRS, Finding, ensure_utf8_stdout, iter_data_files, load_json, load_taxonomy_ids,
)

DATASETS_ROOT = Path(__file__).resolve().parent.parent / "datasets"
DEFAULT_TIMEOUT = 300


def find_datasets(root: Path) -> list[Path]:
    """Dataset directories under root, skipping shared and hidden folders."""
    return sorted(
        p for p in root.iterdir()
        if p.is_dir() and not p.name.startswith(("_", "."))
    )


def find_validators(dataset: Path) -> list[Path]:
    """Every validate.py in the dataset, outside test and hidden folders."""
    return sorted(
        p for p in dataset.rglob("validate.py")
        if not any(part in SKIP_DIRS or part.startswith(".") for part in p.relative_to(dataset).parts[:-1])
    )


def run_validator(dataset: Path, timeout: float = DEFAULT_TIMEOUT) -> tuple[str, str]:
    """Run dataset/validate.py. Returns (status, combined output)."""
    script = dataset / "validate.py"
    if not script.is_file():
        return "NO VALIDATOR", ""
    try:
        proc = subprocess.run(
            [sys.executable, script.name],
            cwd=dataset,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "ERROR", f"timed out after {timeout:g}s"
    output = (proc.stdout + proc.stderr).strip()
    if proc.returncode == 0:
        return "PASS", output
    if proc.returncode == 2:
        return "ERROR", output
    return "FAIL", output


def shared_checks(dataset: Path, datasets_root: Path) -> tuple[int, list[Finding]]:
    """(files checked, findings) for the shared checks on one dataset."""
    files = iter_data_files(dataset)
    covered_dirs = [v.parent for v in find_validators(dataset)]
    taxonomy = load_taxonomy_ids(datasets_root)
    findings: list[Finding] = []
    for path in files:
        data, err = load_json(path, "load")
        if err:
            findings.append(err)
            continue
        if not any(path.is_relative_to(d) for d in covered_dirs):
            findings += schema_validator.validate_file(path, dataset_root=dataset)
        findings += dsgai_mapping_check.check_data(path, data, taxonomy)
        findings += crossref_validator.check_data(path, data)
        findings += severity_check.check_data(path, data)
        findings += date_check.check_data(path, data)
        findings += anonymization_scanner.check_data(path, data)
    records, load_errors = dedup_checker.load_records(files)
    findings += load_errors + dedup_checker.check_records(records)
    return len(files), findings


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Run all dataset validators and shared checks")
    parser.add_argument(
        "--dataset",
        help="Path to one dataset directory (default: every dataset)",
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Check every dataset (the default; kept for the documented usage)",
    )
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Print each validator's output and every warning")
    parser.add_argument("--strict", action="store_true",
                        help="Treat shared-check warnings as failures")
    parser.add_argument("--no-shared", action="store_true",
                        help="Run only the dataset validators")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT,
                        help=f"Seconds each dataset validator may run (default {DEFAULT_TIMEOUT})")
    args = parser.parse_args(argv)

    datasets_root = DATASETS_ROOT.resolve()
    if args.dataset:
        target = Path(args.dataset).resolve()
        if not target.is_dir():
            print(f"Directory not found: {args.dataset}")
            return 2
        # The datasets root itself means "all of them"; anything else is one dataset.
        datasets = find_datasets(target) if target == datasets_root else [target]
    else:
        datasets = find_datasets(datasets_root)

    if not datasets:
        print("No dataset directories found")
        return 2

    results = []
    for dataset in datasets:
        validators = find_validators(dataset)
        if not validators:
            results.append("NO VALIDATOR")
            print(f"{'NO VALIDATOR':<13} {dataset.name}")
            continue
        for script in validators:
            label = dataset.name
            if script.parent != dataset:
                label += "/" + script.parent.relative_to(dataset).as_posix()
            status, output = run_validator(script.parent, args.timeout)
            results.append(status)
            print(f"{status:<13} {label}")
            if output and (args.verbose or status in ("FAIL", "ERROR")):
                for line in output.splitlines():
                    print(f"    {line}")

    checked_files = errors = warnings = 0
    if not args.no_shared:
        print("\nShared checks (schema, DSGAI, CVE/CWE/ATLAS/OWASP IDs, CVSS, dates, anonymization, duplicates):")
        for dataset in datasets:
            n, findings = shared_checks(dataset, datasets_root)
            if not n:
                continue
            e = sum(f.level == ERROR for f in findings)
            w = len(findings) - e
            checked_files, errors, warnings = checked_files + n, errors + e, warnings + w
            status = "FAIL" if e or (args.strict and w) else "WARN" if w else "PASS"
            print(f"{status:<13} {dataset.name} ({n} file(s), {e} error(s), {w} warning(s))")
            for f in findings:
                if f.level == ERROR or args.verbose or args.strict:
                    print(f"    {f.format(datasets_root.parent)}")

    ran = [s for s in results if s != "NO VALIDATOR"]
    failed = [s for s in ran if s != "PASS"]
    print(f"\n{len(ran)} validator(s) ran, {len(failed)} failed, "
          f"{len(results) - len(ran)} dataset(s) have no validator yet")
    if not args.no_shared:
        print(f"Shared checks: {checked_files} file(s), {errors} error(s), {warnings} warning(s)"
              + ("" if args.verbose or not warnings else " (--verbose lists the warnings)"))
    if not ran and not checked_files:
        return 2
    return 1 if failed or errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
