"""
Run every dataset's own validator and report one result per dataset.

Each dataset that ships a validate.py (schema.json + entries/) is checked by
running that script in its own directory. Datasets without a validate.py are
listed as "no validator" so the gap is visible instead of silently passing.

Usage:
    python run_all_checks.py                      # every dataset under ../datasets
    python run_all_checks.py --dataset ../datasets/exploit_dataset
    python run_all_checks.py --verbose            # print each validator's output

Exit code: 0 when every validator that ran passed, 1 when any failed,
2 when the arguments name no dataset that can be checked.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

DATASETS_ROOT = Path(__file__).resolve().parent.parent / "datasets"


def find_datasets(root: Path) -> list[Path]:
    """Dataset directories under root, skipping shared and hidden folders."""
    return sorted(
        p for p in root.iterdir()
        if p.is_dir() and not p.name.startswith(("_", "."))
    )


def run_validator(dataset: Path) -> tuple[str, str]:
    """Run dataset/validate.py. Returns (status, combined output)."""
    script = dataset / "validate.py"
    if not script.is_file():
        return "NO VALIDATOR", ""
    proc = subprocess.run(
        [sys.executable, script.name],
        cwd=dataset,
        capture_output=True,
        text=True,
        check=False,
    )
    output = (proc.stdout + proc.stderr).strip()
    if proc.returncode == 0:
        return "PASS", output
    if proc.returncode == 2:
        return "ERROR", output
    return "FAIL", output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run all dataset validators")
    parser.add_argument(
        "--dataset",
        help="Path to one dataset directory (default: every dataset)",
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Check every dataset (the default; kept for the documented usage)",
    )
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Print each validator's output")
    args = parser.parse_args(argv)

    if args.dataset:
        target = Path(args.dataset).resolve()
        if not target.is_dir():
            print(f"Directory not found: {args.dataset}")
            return 2
        # The datasets root itself means "all of them"; anything else is one dataset.
        datasets = find_datasets(target) if target == DATASETS_ROOT.resolve() else [target]
    else:
        datasets = find_datasets(DATASETS_ROOT)

    if not datasets:
        print("No dataset directories found")
        return 2

    results = []
    for dataset in datasets:
        status, output = run_validator(dataset)
        results.append(status)
        print(f"{status:<13} {dataset.name}")
        if output and (args.verbose or status in ("FAIL", "ERROR")):
            for line in output.splitlines():
                print(f"    {line}")

    ran = [s for s in results if s != "NO VALIDATOR"]
    failed = [s for s in ran if s != "PASS"]
    print(f"\n{len(ran)} validator(s) ran, {len(failed)} failed, "
          f"{len(results) - len(ran)} dataset(s) have no validator yet")
    if not ran:
        return 2
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
