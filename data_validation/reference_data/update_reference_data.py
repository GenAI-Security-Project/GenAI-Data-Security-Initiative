"""
Regenerates the lookup tables that track an external release: MITRE ATLAS,
CWE, the SPDX License List and the IANA Language Subtag Registry.

    python update_reference_data.py              # all of them
    python update_reference_data.py --atlas      # mitre_atlas_techniques.csv
    python update_reference_data.py --cwe        # cwe_ids.csv
    python update_reference_data.py --spdx       # spdx_licenses.csv
    python update_reference_data.py --languages  # language_subtags.csv

Run it when one of them publishes a new release (the reference-data-refresh
workflow does so monthly), and commit the regenerated CSVs together with the
version line this script updates in SOURCES.md.
Requires pyyaml for the ATLAS data. Needs network access; nothing else in
data_validation does.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
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
SPDX_URL = "https://raw.githubusercontent.com/spdx/license-list-data/main/json/licenses.json"
IANA_SUBTAGS_URL = "https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry"
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
        root = ET.fromstring(zf.read(zf.namelist()[0]))  # noqa: S314 - MITRE's own release file, see import
    ns = {"c": root.tag.split("}")[0].strip("{")}
    rows = []
    for kind, xpath in (("weakness", "c:Weaknesses/c:Weakness"),
                        ("category", "c:Categories/c:Category"),
                        ("view", "c:Views/c:View")):
        for el in root.findall(xpath, ns):
            rows.append({
                "cwe_id": f"CWE-{el.get('ID')}",
                "name": el.get("Name", ""),
                "type": kind,
                "status": el.get("Status", ""),
            })
    rows.sort(key=lambda r: int(r["cwe_id"].split("-")[1]))
    with open(HERE / "cwe_ids.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["cwe_id", "name", "type", "status"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    version = root.get("Version", "unknown")
    set_version("CWE", version)
    print(f"cwe_ids.csv: {len(rows)} entries (CWE {version})")


def update_spdx() -> None:
    data = json.loads(fetch(SPDX_URL))
    exceptions = json.loads(fetch(SPDX_URL.replace("licenses.json", "exceptions.json")))
    rows = [{"spdx_id": lic["licenseId"], "name": lic["name"], "type": "license",
             "deprecated": str(lic.get("isDeprecatedLicenseId", False)).lower()} for lic in data["licenses"]]
    rows += [{"spdx_id": exc["licenseExceptionId"], "name": exc["name"], "type": "exception",
              "deprecated": str(exc.get("isDeprecatedLicenseId", False)).lower()} for exc in exceptions["exceptions"]]
    rows.sort(key=lambda r: r["spdx_id"].lower())
    with open(HERE / "spdx_licenses.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["spdx_id", "name", "type", "deprecated"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    set_version("SPDX licenses", data["licenseListVersion"])
    print(f"spdx_licenses.csv: {len(rows)} licenses and exceptions (SPDX License List {data['licenseListVersion']})")


def update_languages() -> None:
    text = fetch(IANA_SUBTAGS_URL).decode("utf-8")
    records = text.split("\n%%\n")
    file_date = records[0].split(":", 1)[1].strip()
    rows = []
    for record in records[1:]:
        fields: dict[str, str] = {}
        for line in record.splitlines():
            if line.startswith("  "):  # continuation of the previous field
                continue
            key, _, value = line.partition(":")
            fields.setdefault(key.strip(), value.strip())  # first Description only
        kind = fields.get("Type")
        if kind in ("language", "script", "region") and "Subtag" in fields and ".." not in fields["Subtag"]:
            rows.append({"type": kind, "subtag": fields["Subtag"], "description": fields.get("Description", ""),
                         "deprecated": "true" if "Deprecated" in fields else "false"})
    rows.sort(key=lambda r: (r["type"], r["subtag"].lower()))
    with open(HERE / "language_subtags.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["type", "subtag", "description", "deprecated"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    set_version("Language subtags", file_date)
    print(f"language_subtags.csv: {len(rows)} subtags (IANA registry {file_date})")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Regenerate the externally maintained reference tables")
    for name in ("atlas", "cwe", "spdx", "languages"):
        parser.add_argument(f"--{name}", action="store_true")
    args = parser.parse_args(argv)
    every = not (args.atlas or args.cwe or args.spdx or args.languages)
    for name, update in (("atlas", update_atlas), ("cwe", update_cwe), ("spdx", update_spdx), ("languages", update_languages)):
        if every or getattr(args, name):
            update()
    return 0


if __name__ == "__main__":
    sys.exit(main())
