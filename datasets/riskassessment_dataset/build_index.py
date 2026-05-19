"""Generate index.csv from every entry in ./entries/.

Usage: python build_index.py
Writes ./index.csv with key flat columns; arrays are joined with '|'.
Stdlib only.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENTRIES_DIR = ROOT / "entries"
INDEX_PATH = ROOT / "index.csv"

COLUMNS = [
    "assessment_id",
    "scenario_name",
    "entry_type",
    "industry_sector",
    "deployment_pattern",
    "maturity_overall",
    "dsgai_risks",
    "highest_inherent_rating",
    "highest_residual_rating",
    "control_count",
    "gap_count",
    "immediate_gap_count",
    "frameworks_mapped",
    "compliance_obligations",
    "date_added",
    "tags",
]

RATING_ORDER = ["Informational", "Low", "Medium", "High", "Critical"]


def highest(ratings: list[str]) -> str:
    best_idx = -1
    for r in ratings:
        if r in RATING_ORDER:
            best_idx = max(best_idx, RATING_ORDER.index(r))
    return RATING_ORDER[best_idx] if best_idx >= 0 else ""


def row_for(entry: dict) -> dict[str, str]:
    risks = entry.get("risks_identified", []) or []
    return {
        "assessment_id": entry.get("assessment_id", ""),
        "scenario_name": entry.get("scenario_name", ""),
        "entry_type": entry.get("entry_type", ""),
        "industry_sector": entry.get("industry_sector", ""),
        "deployment_pattern": entry.get("deployment_pattern", ""),
        "maturity_overall": entry.get("maturity_overall", ""),
        "dsgai_risks": "|".join(sorted({r.get("dsgai_id", "") for r in risks if r.get("dsgai_id")})),
        "highest_inherent_rating": highest([r.get("inherent_rating", "") for r in risks]),
        "highest_residual_rating": highest([r.get("residual_rating", "") for r in risks]),
        "control_count": str(len(entry.get("existing_controls", []) or [])),
        "gap_count": str(len(entry.get("control_gaps", []) or [])),
        "immediate_gap_count": str(sum(1 for g in (entry.get("control_gaps") or []) if g.get("urgency") == "Immediate")),
        "frameworks_mapped": "|".join(sorted({f.get("framework", "") for f in (entry.get("framework_alignments") or [])})),
        "compliance_obligations": "|".join(entry.get("compliance_obligations", []) or []),
        "date_added": entry.get("date_added", ""),
        "tags": "|".join(entry.get("tags", []) or []),
    }


def main() -> None:
    rows = []
    for path in sorted(ENTRIES_DIR.glob("*.json")):
        entry = json.loads(path.read_text(encoding="utf-8"))
        rows.append(row_for(entry))

    with INDEX_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {INDEX_PATH.name} with {len(rows)} entries.")


if __name__ == "__main__":
    main()
