"""
Generates a Markdown coverage report: how records spread across DSGAI
entries, severity, and each dataset's main categorical fields. It shows gaps
(DSGAI entries no record maps to) and overrepresentation; it does not judge
whether either is a problem.

Usage:
    python bias_report.py                          # print to stdout
    python bias_report.py --output bias_report.md
    python bias_report.py --datasets ../../datasets/
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validators._common import DATASETS_ROOT, ensure_utf8_stdout, load_dataset_records  # noqa: E402
from validators.dsgai_mapping_check import record_dsgai_ids  # noqa: E402

# Top-level fields reported per dataset when present.
CATEGORY_FIELDS = (
    "category", "affected_component", "target_component", "industry_sector",
    "deployment_pattern", "entry_type", "disclosure_status", "disposition",
)


def taxonomy(datasets_root: Path) -> list[tuple[str, str]]:
    data = json.loads((datasets_root / "_shared" / "dsgai_taxonomy.json").read_text(encoding="utf-8"))
    return [(e["id"], e["name"]) for e in data["entries"]]


def severity_of(record: dict) -> str | None:
    sev = record.get("severity")
    if isinstance(sev, dict):
        sev = sev.get("qualitative")
    return sev if isinstance(sev, str) else None


def _pct(n: int, total: int) -> str:
    return f"{n} ({n / total:.0%})" if total else "0"


def build_report(datasets_root: Path = DATASETS_ROOT) -> str:
    records = load_dataset_records(datasets_root)
    tax = taxonomy(datasets_root)
    names = [n for n, recs in records.items() if recs]
    lines = ["# Dataset coverage report", ""]
    lines += ["| Dataset | Records |", "|---|---|"]
    lines += [f"| `{n}` | {len(recs)} |" for n, recs in records.items()]

    coverage = {n: Counter(i for _p, r in records[n] for i in record_dsgai_ids(r)) for n in names}
    lines += ["", "## DSGAI coverage", "",
              "Records that map to each DSGAI entry. A record can map to several.", ""]
    lines.append("| DSGAI | Name | " + " | ".join(f"`{n}`" for n in names) + " | Total |")
    lines.append("|---|---|" + "---|" * (len(names) + 1))
    for did, dname in tax:
        counts = [coverage[n][did] for n in names]
        lines.append(f"| {did} | {dname} | " + " | ".join(str(c) for c in counts) + f" | {sum(counts)} |")
    uncovered = [did for did, _ in tax if not any(coverage[n][did] for n in names)]
    lines += ["", f"DSGAI entries no record maps to: {', '.join(uncovered) if uncovered else 'none'}."]

    for n in names:
        recs = [r for _p, r in records[n]]
        total = len(recs)
        sections = []
        sev = Counter(s for r in recs if (s := severity_of(r)))
        if sev:
            sections.append(("severity", sev))
        for field in CATEGORY_FIELDS:
            c = Counter(r[field] for r in recs if isinstance(r.get(field), str))
            if c:
                sections.append((field, c))
        if not sections:
            continue
        lines += ["", f"## `{n}`"]
        for field, c in sections:
            lines += ["", f"**{field}**: " + ", ".join(f"{k} {_pct(v, total)}" for k, v in c.most_common())]
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="Generate a dataset coverage and bias report")
    parser.add_argument("--datasets", default=str(DATASETS_ROOT), help="Root datasets directory")
    parser.add_argument("--output", help="Write the report here instead of stdout")
    args = parser.parse_args(argv)
    root = Path(args.datasets)
    if not root.is_dir():
        print(f"Directory not found: {args.datasets}")
        return 2
    report = build_report(root.resolve())
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
