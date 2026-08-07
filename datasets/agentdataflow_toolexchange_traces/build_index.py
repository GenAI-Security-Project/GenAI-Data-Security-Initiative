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

SENSITIVITY_ORDER = ["none", "low", "moderate", "high"]

COLUMNS = [
    "trace_id",
    "title",
    "category",
    "disposition",
    "provenance_tier",
    "primary_dsgai",
    "dsgai_mapping",
    "owasp_llm_top10_mapping",
    "agent_framework",
    "tool_protocol",
    "span_count",
    "finding_count",
    "max_sensitivity",
    "data_classes",
    "evidence_count",
    "primary_evidence",
    "date_added",
    "tags",
]


def max_sensitivity(spans: list[dict]) -> str:
    best = -1
    for span in spans:
        value = span.get("sensitivity")
        if value in SENSITIVITY_ORDER:
            best = max(best, SENSITIVITY_ORDER.index(value))
    return SENSITIVITY_ORDER[best] if best >= 0 else ""


def row_for(entry: dict) -> dict[str, str]:
    spans = entry.get("spans", []) or []
    prov = entry.get("provenance", {}) or {}
    agent = entry.get("agent", {}) or {}
    evidence = prov.get("evidence", []) or []
    dsgai = entry.get("dsgai_mapping", []) or []

    data_classes: list[str] = []
    for span in spans:
        for cls in span.get("data_classes", []) or []:
            if cls not in data_classes:
                data_classes.append(cls)

    return {
        "trace_id": entry.get("trace_id", ""),
        "title": entry.get("title", ""),
        "category": entry.get("category", ""),
        "disposition": entry.get("disposition", ""),
        "provenance_tier": prov.get("tier", ""),
        "primary_dsgai": dsgai[0] if dsgai else "",
        "dsgai_mapping": "|".join(dsgai),
        "owasp_llm_top10_mapping": "|".join(entry.get("owasp_llm_top10_mapping", []) or []),
        "agent_framework": agent.get("framework", ""),
        "tool_protocol": agent.get("tool_protocol", ""),
        "span_count": str(len(spans)),
        "finding_count": str(sum(1 for s in spans if s.get("finding"))),
        "max_sensitivity": max_sensitivity(spans),
        "data_classes": "|".join(sorted(data_classes)),
        "evidence_count": str(len(evidence)),
        "primary_evidence": evidence[0].get("citation", "") if evidence else "",
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
