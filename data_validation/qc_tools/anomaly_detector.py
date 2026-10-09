"""
Flags statistical outliers for a reviewer to look at:

  * a DSGAI entry that more than CONCENTRATION of a dataset's records map to
  * a record that maps to far more DSGAI entries than its dataset's typical
    record (more than mean + 2 standard deviations, more than twice the mean,
    and more than 3)
  * a severity level, or a value of a categorical field, that covers more
    than SKEW of a dataset's records

Datasets with fewer than MIN_RECORDS records are skipped: percentages of a
handful of records say nothing. Findings are WARN only; the exit code is 0
unless the arguments are wrong.

Usage:
    python anomaly_detector.py
    python anomaly_detector.py --datasets ../../datasets/
"""
from __future__ import annotations

import argparse
import statistics
import sys
from collections import Counter
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from qc_tools.bias_report import CATEGORY_FIELDS, severity_of  # noqa: E402
from validators._common import (  # noqa: E402
    DATASETS_ROOT,
    WARN,
    Finding,
    ensure_utf8_stdout,
    load_dataset_records,
    print_findings,
    record_id,
)
from validators.dsgai_mapping_check import record_dsgai_ids  # noqa: E402

CHECK = "anomaly"
MIN_RECORDS = 10
CONCENTRATION = 0.6
SKEW = 0.85


def detect(datasets_root: Path = DATASETS_ROOT) -> list[Finding]:
    findings: list[Finding] = []
    for name, items in load_dataset_records(datasets_root).items():
        if len(items) < MIN_RECORDS:
            continue
        ds_path = datasets_root / name
        total = len(items)
        mappings = [record_dsgai_ids(r) for _p, r in items]

        for did, n in Counter(i for m in mappings for i in m).most_common():
            if n / total > CONCENTRATION:
                findings.append(Finding(WARN, CHECK, ds_path, "",
                                        f"{n / total:.0%} of {total} records map to {did}; check it is not a default mapping"))

        sizes = [len(m) for m in mappings]
        if len(set(sizes)) > 1:
            mean = statistics.mean(sizes)
            limit = max(mean + 2 * statistics.stdev(sizes), 2 * mean, 3)
            for (path, rec), size in zip(items, sizes, strict=True):
                if size > limit:
                    findings.append(Finding(WARN, CHECK, path, "",
                                            f"{record_id(rec) or path.name} maps to {size} DSGAI entries "
                                            f"(dataset mean {mean:.1f})"))

        fields = {"severity": Counter(s for _p, r in items if (s := severity_of(r)))}
        for field in CATEGORY_FIELDS:
            fields[field] = Counter(r[field] for _p, r in items if isinstance(r.get(field), str))
        for field, counts in fields.items():
            if not counts or len(counts) == 1 and field != "severity":
                continue  # a field with one value everywhere is a constant, not a skew
            value, n = counts.most_common(1)[0]
            if n / total > SKEW:
                findings.append(Finding(WARN, CHECK, ds_path, "",
                                        f"{field} is {value!r} in {n / total:.0%} of {total} records"))
    return findings


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Detect anomalies in dataset distributions")
    parser.add_argument("--datasets", default=str(DATASETS_ROOT), help="Root datasets directory")
    args = parser.parse_args(argv)
    root = Path(args.datasets)
    if not root.is_dir():
        print(f"Directory not found: {args.datasets}")
        return 2
    print_findings(detect(root.resolve()), root.resolve().parent)
    return 0


if __name__ == "__main__":
    sys.exit(main())
