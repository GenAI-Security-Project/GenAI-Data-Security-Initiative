"""
Regenerates the MITRE ATLAS and CWE lookup tables from MITRE's published data.

    python update_reference_data.py            # both
    python update_reference_data.py --atlas    # mitre_atlas_techniques.csv only
    python update_reference_data.py --cwe      # cwe_ids.csv only

Run it when ATLAS or CWE publish a new release, and commit the regenerated
CSVs together with the version line this script updates in SOURCES.md.
Requires pyyaml for the ATLAS data. Needs network access; nothing else in
data_validation does.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import urllib.request
# stdlib ElementTree does not fetch external entities; the input is MITRE's
# own release file over HTTPS, read only by maintainers running this script.
import xml.etree.ElementTree as ET  # noqa: S405
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ATLAS_DIST = "https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/"
# manifest.yaml lists every release, newest first; dist/ATLAS.yaml is the
# deprecated pre-2026 format and is no longer updated.
ATLAS_MANIFEST = ATLAS_DIST + "manifest.yaml"
# Last release in the old format. IDs in it that the current release no longer
# has are kept as "retired" rows, so data citing them gets a warning that says
# so instead of an "unknown ID" error.
ATLAS_LEGACY = ATLAS_DIST + "ATLAS.yaml"
CWE_URL = "https://cwe.mitre.org/data/xml/cwec_latest.xml.zip"
SOURCES = HERE / "SOURCES.md"


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=60) as resp:  # noqa: S310 - fixed https URLs
        return resp.read()


def set_version(label: str, version: str) -> None:
    text = SOURCES.read_text(encoding="utf-8")
    text = re.sub(rf"(\| {re.escape(label)} \|[^|]*\| )[^|]*(\|)", rf"\g<1>{version} \2", text)
    SOURCES.write_text(text, encoding="utf-8")


def update_atlas() -> None:
    import yaml
    latest = yaml.safe_load(fetch(ATLAS_MANIFEST))[0]
    path = next(v["path"] for v in latest["versions"] if v["format-version"].startswith("6."))
    data = yaml.safe_load(fetch(ATLAS_DIST + path))
    tactics = {tid: t["name"] for tid, t in data["tactics"].items()}
    rels = data["relationships"]
    rows = []
    for tid in sorted(data["techniques"]):
        links = rels.get(tid, {})
        rows.append({
            "technique_id": tid,
            "name": data["techniques"][tid]["name"],
            "parent_id": "; ".join(r["target"] for r in links.get("specializes", [])),
            "tactics": "; ".join(tactics.get(r["target"], r["target"]) for r in links.get("achieves", [])),
            "status": "current",
        })
    legacy = yaml.safe_load(fetch(ATLAS_LEGACY))
    for matrix in legacy["matrices"]:
        for t in matrix["techniques"]:
            if t["id"] not in data["techniques"]:
                rows.append({"technique_id": t["id"], "name": t["name"], "parent_id": t.get("specializes", ""),
                             "tactics": "", "status": "retired"})
    rows.sort(key=lambda r: r["technique_id"])
    with open(HERE / "mitre_atlas_techniques.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["technique_id", "name", "parent_id", "tactics", "status"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    version = data["collection"]["version"]
    set_version("MITRE ATLAS", str(version))
    retired = sum(r["status"] == "retired" for r in rows)
    print(f"mitre_atlas_techniques.csv: {len(rows) - retired} techniques, {retired} retired (ATLAS {version})")


def update_cwe() -> None:
    with zipfile.ZipFile(io.BytesIO(fetch(CWE_URL))) as zf:
        root = ET.fromstring(zf.read(zf.namelist()[0]))
    ns = {"c": root.tag.split("}")[0].strip("{")}
    rows = []
    for kind, xpath in (("weakness", "c:Weaknesses/c:Weakness"),
                        ("category", "c:Categories/c:Category"),
                        ("view", "c:Views/c:View")):
        for el in root.findall(xpath, ns):
            rows.append({
                "cwe_id": f"CWE-{el.get('ID')}",
                "name": el.get("Name"),
                "type": kind,
                "status": el.get("Status"),
            })
    rows.sort(key=lambda r: int(r["cwe_id"].split("-")[1]))
    with open(HERE / "cwe_ids.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["cwe_id", "name", "type", "status"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    set_version("CWE", root.get("Version"))
    print(f"cwe_ids.csv: {len(rows)} entries (CWE {root.get('Version')})")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Regenerate ATLAS and CWE reference tables")
    parser.add_argument("--atlas", action="store_true")
    parser.add_argument("--cwe", action="store_true")
    args = parser.parse_args(argv)
    both = not (args.atlas or args.cwe)
    if both or args.atlas:
        update_atlas()
    if both or args.cwe:
        update_cwe()
    return 0


if __name__ == "__main__":
    sys.exit(main())
