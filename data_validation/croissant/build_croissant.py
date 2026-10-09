"""
Generates datasets/<name>/croissant.json, the MLCommons Croissant 1.1
metadata (with the Responsible AI vocabulary) for each published dataset.

Croissant makes a dataset machine-readable for ML tooling and dataset
search: what the files are, their checksums, how to load the records, and
RAI documentation (limitations, biases, intended uses, personal data,
collection). NeurIPS 2026 requires it, RAI fields included, for dataset
submissions.

    python build_croissant.py            # write every croissant.json
    python build_croissant.py --check    # fail if any is out of date (CI)

The descriptive and RAI text lives in DATASETS below; file lists, SHA-256
checksums, record fields and dates are derived from the repository, so the
output is deterministic and only changes when the data does. CI validates
every file with `mlcroissant validate` and loads records through it.
Requires: mlcroissant (requirements-croissant.txt).

incident_dataset (no entries yet) and crossframework_mapping_dataset
(superseded by the GenAI Crosswalk) are not described.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATASETS_ROOT = REPO_ROOT / "datasets"
REPO_URL = "https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative"
LICENSE_BY_SA = "https://creativecommons.org/licenses/by-sa/4.0/"
LICENSE_BY = "https://creativecommons.org/licenses/by/4.0/"
CROISSANT_1_1 = "http://mlcommons.org/croissant/1.1"
MAINTENANCE = ("Maintained by the OWASP GenAI Data Security Initiative (Workstream 5). Contributions arrive as "
               "pull requests and must pass data_validation/run_all_checks.py in CI and peer review; weekly online "
               "checks re-verify cited CVEs, advisories and links. Versioned releases carry SHA-256 checksums.")

# Per-dataset description and Responsible AI documentation. Keep these true
# to the data: when a dataset changes shape, update its entry here.
DATASETS: dict[str, dict] = {
    "vulnerability_dataset": {
        "title": "DSGAI Vulnerability Dataset",
        "description": (
            "Publicly disclosed vulnerabilities in LLM and GenAI applications (CVE-tracked issues and significant "
            "published research disclosures), each mapped to the OWASP GenAI Data Security (DSGAI) risk taxonomy, "
            "the OWASP Top 10 for LLM Applications (2025 and 2026 editions), CWE and CVSS."),
        "index": "index.csv",
        "license": [LICENSE_BY_SA],
        "collection": ("Curated by initiative contributors from public sources: NVD and CVE records, vendor and "
                       "GitHub security advisories, and peer-reviewed or widely cited research. Every entry cites "
                       "its sources; CVSS vectors and scores are taken from NVD or the assigning CNA."),
        "collection_type": ["Secondary Data analysis", "Manual Human Curator"],
        "limitations": [
            "Covers only publicly disclosed issues; undisclosed and vendor-internal vulnerabilities are absent by design.",
            "Not exhaustive: a curated sample, not a census of GenAI CVEs. Absence of a product does not imply it is secure.",
            "DSGAI and OWASP mappings are expert judgments reviewed by peers, not mechanically derived.",
        ],
        "biases": [
            "Skews toward open-source Python LLM frameworks and inference servers (agent frameworks are about half of "
            "the entries), because CVE assignment concentrates there; closed SaaS assistants appear only through "
            "public research disclosures.",
            "Skews toward High and Critical severity: low-severity issues are rarely publicised or assigned CVEs.",
            "Disclosure dates cluster in 2023-2025, the period the corpus was assembled for.",
        ],
        "use_cases": [
            "Mapping real GenAI vulnerabilities to DSGAI risks for threat modelling and control prioritisation.",
            "Evaluation and regression data for GenAI security scanners and LLM-application security reviews.",
            "Not intended for exploit development; entries describe issues at advisory level of detail.",
        ],
        "pii": ("No personal data. Entries describe software vulnerabilities and cite public advisories; researcher "
                "names appear only where a cited public source credits them."),
        "social_impact": ("Helps defenders prioritise GenAI data-security controls. All issues are already public, "
                          "so the dataset adds aggregation and mapping rather than new attack capability."),
    },
    "exploit_dataset": {
        "title": "DSGAI Exploit Technique Dataset",
        "description": (
            "Publicly documented attack techniques against GenAI systems, one technique class per entry (how an attacker "
            "does something, not a product-specific flaw), mapped to MITRE ATLAS, the DSGAI taxonomy and the OWASP "
            "Top 10 for LLM Applications. Most entries follow MITRE ATLAS techniques; the rest are research-derived "
            "technique families ATLAS does not track separately."),
        "index": "index.csv",
        "license": [LICENSE_BY_SA],
        "collection": ("Curated from the MITRE ATLAS catalog and published research (papers, vendor advisories, "
                       "conference talks). Each entry cites its sources and links related vulnerability entries."),
        "collection_type": ["Secondary Data analysis", "Manual Human Curator"],
        "limitations": [
            "Describes techniques at the level of public literature; it is not a playbook and omits weaponised detail.",
            "ATLAS-derived entries track the ATLAS release they were written against; a monthly job flags retired IDs.",
            "Severity is a qualitative judgment of the technique class, not a CVSS score.",
        ],
        "biases": [
            "About 70% of entries come from the MITRE ATLAS catalog, so coverage follows ATLAS's own emphasis.",
            "Weighted toward prompt-injection, jailbreak and poisoning techniques, which dominate the published literature.",
        ],
        "use_cases": [
            "Red-team planning and coverage analysis of GenAI defences against known technique classes.",
            "Linking techniques to concrete vulnerabilities and to DSGAI risks in threat models.",
        ],
        "pii": "No personal data.",
        "social_impact": ("Techniques are already public; the dataset organises them for defenders. Dual-use "
                          "risk is limited by keeping entries at catalog-level detail."),
    },
    "riskassessment_dataset": {
        "title": "DSGAI Risk Assessment Dataset",
        "description": (
            "Structured risk assessments of GenAI deployment archetypes: for each representative architecture, the "
            "DSGAI risks with inherent and residual ratings and rationale, existing controls, control gaps, and "
            "alignments to security and AI-governance frameworks."),
        "index": "index.csv",
        "license": [LICENSE_BY_SA],
        "collection": ("Written by initiative contributors as synthetic-but-realistic templates of common deployment "
                       "patterns, informed by public guidance and practitioner experience; peer reviewed."),
        "collection_type": ["Manual Human Curator"],
        "limitations": [
            "Every entry is a synthetic template of a deployment archetype, not an assessment of a real organisation.",
            "Ratings and control gaps are expert judgments for the described archetype; a real deployment needs its own assessment.",
        ],
        "biases": [
            "Sector coverage is uneven: cross-sector templates are the largest group, followed by financial "
            "services and SaaS; several sectors have a single template.",
            "Framework alignments reflect the frameworks contributors know best.",
        ],
        "use_cases": [
            "Starting points and worked examples for GenAI risk assessments and DSGAI training.",
            "Benchmark scenarios for comparing control coverage across deployment patterns.",
        ],
        "pii": "No personal data: the scenarios are synthetic and describe archetypes, not organisations or people.",
        "social_impact": "Lowers the cost of structured GenAI risk assessment for smaller organisations.",
    },
    "agentdataflow_toolexchange_traces": {
        "title": "Agent Data Flow and Tool Exchange Traces",
        "description": (
            "Sanitized traces of agentic AI tool calls, plugin data exchanges and delegation chains: typed spans, "
            "data classes and sensitivity, findings mapped to DSGAI risks, and a provenance tier with cited evidence."),
        "index": "index.csv",
        "license": [LICENSE_BY_SA],
        "collection": ("Constructed by contributors as minimal traces of documented agent and MCP behaviour, or as "
                       "explicitly hypothetical scenarios; each declares its provenance tier and cites evidence."),
        "collection_type": ["Manual Human Curator", "Document analysis"],
        "limitations": [
            "Very small: a handful of traces so far, all of unintentional failures; adversarial traces are not yet included.",
            "Traces are reconstructions from public documentation or hypothetical, not captured production telemetry.",
        ],
        "biases": ["Centred on MCP-based tool ecosystems, where most public agent data-flow documentation exists."],
        "use_cases": [
            "Studying how sensitive data moves through agent tool calls, and testing agent data-flow analysers.",
            "Worked examples for DSGAI06 and related agent data-exchange risks.",
        ],
        "pii": ("No personal data. Payload values are synthetic placeholders; validate.py fails any trace containing "
                "credential, internal-hostname or real-address patterns."),
        "social_impact": "Supports safer agent designs by making data-exchange failure modes concrete.",
    },
    "promptinj_dataextraction_testcases": {
        "title": "Prompt Injection and Data Extraction Test Cases",
        "description": (
            "Adversarial prompts with expected secure and vulnerable behaviour, for red-teaming and regression "
            "testing of GenAI data-security controls. Current suites are Turkish-language: adapted cases from a public "
            "corpus, contrastive attack/benign-control pairs, and a small hand-written set with English glosses."),
        "index": None,
        "published": "2026-03-23",
        "manifests": ["tr_altaysec_turkish_llm_injection/manifest.csv",
                      "tr_turkish_conversation_prompt_injection_pairs/manifest.csv"],
        "license": [LICENSE_BY_SA, LICENSE_BY],
        "collection": ("Contributed suites. Most cases adapt public CC BY 4.0 corpora (attribution and source "
                       "hashes are kept in each case's provenance); the adaptation adds DSGAI mappings, expected "
                       "behaviours and sandbox prerequisites. A small set was written for this dataset."),
        "collection_type": ["Secondary Data analysis", "Manual Human Curator"],
        "limitations": [
            "Almost entirely Turkish; results do not transfer to other languages without new cases.",
            "Expected behaviours are defensive test expectations, not observed results for any model.",
            "Lexical deduplication only; paraphrased near-duplicates may remain.",
        ],
        "biases": [
            "Weighted toward system-prompt extraction and direct data extraction; other categories have fewer cases.",
            "Reflects the attack styles of its source corpora (authority and urgency framing, morphological and "
            "cross-lingual bypasses).",
        ],
        "use_cases": [
            "Sandboxed red-team exercises and regression tests for prompt-injection and data-extraction defences.",
            "Evaluating multilingual (Turkish) robustness of guardrails. Do not run against production systems.",
        ],
        "pii": ("Synthetic data only: secrets and identifiers in prompts are placeholders, and cases were screened "
                "for real personal data and live-secret patterns."),
        "social_impact": ("Adversarial prompts are dual-use; they are published at the level already public in "
                          "their source corpora so defenders can test non-English guardrail gaps."),
    },
    "rag_dataset": {
        "title": "RAG Poisoning and Retrieval Integrity Dataset",
        "description": (
            "Synthetic documents and test fixtures for retrieval-augmented generation: poisoned documents, integrity "
            "and redaction tests, cross-tenant probes, each with expected secure and vulnerable retrieval behaviour."),
        "index": None,
        "published": "2026-03-23",
        "license": [LICENSE_BY_SA],
        "collection": "Written by contributors as synthetic, safe-to-ingest regression fixtures.",
        "collection_type": ["Manual Human Curator"],
        "limitations": ["A single fixture so far; it demonstrates the format more than it covers the space."],
        "biases": ["Covers one poisoning pattern (a false policy value plus a harmless canary instruction)."],
        "use_cases": ["Regression tests for RAG ingestion quarantine, retrieval filtering and context resilience."],
        "pii": "No personal data; all content is synthetic and labelled as such in each record's metadata.",
        "social_impact": "Fixtures use harmless canaries so they cannot cause harm if ingested by mistake.",
    },
}


def sha256(path: Path) -> str:
    """SHA-256 of the file as the repository stores and serves it.

    .gitattributes keeps dataset CSV and JSON files LF in the repository, but
    a Windows checkout (core.autocrlf) or a csv-module writer may leave CRLF
    in a working copy; hashing LF-normalized bytes gives the same checksum
    on every platform, matching the downloaded file."""
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def entry_dates(dataset: Path) -> list[str]:
    dates = []
    for path in dataset.rglob("*.json"):
        if "fixtures" in path.parts or path.name.endswith("schema.json") or path.name == "croissant.json":
            continue
        for value in re.findall(r'"date_added":\s*"(\d{4}-\d{2}-\d{2})"', path.read_text(encoding="utf-8")):
            dates.append(value)
    return sorted(dates)


def csv_record_set(mlc, rs_id: str, file_id: str, path: Path):
    columns = next(csv.reader(path.open(encoding="utf-8")))
    fields = [mlc.Field(id=f"{rs_id}/{c}", name=c, data_types=[mlc.DataType.TEXT],
                        source=mlc.Source(file_object=file_id, extract=mlc.Extract(column=c)))
              for c in columns]
    return mlc.RecordSet(id=rs_id, name=rs_id, fields=fields,
                         description=f"One record per row of {path.name}; list-valued columns are joined with '|'.")


def build(name: str, spec: dict, version: str) -> dict:
    import mlcroissant as mlc
    dataset = DATASETS_ROOT / name
    distribution, record_sets = [], []
    for csv_rel in ([spec["index"]] if spec.get("index") else []) + spec.get("manifests", []):
        path = dataset / csv_rel
        file_id = csv_rel
        distribution.append(mlc.FileObject(id=file_id, name=file_id, content_url=csv_rel,
                                           encoding_formats=["text/csv"], sha256=sha256(path)))
        rs_id = "index" if csv_rel == spec.get("index") else csv_rel.split("/")[0]
        record_sets.append(csv_record_set(mlc, rs_id, file_id, path))
    for schema in sorted(dataset.rglob("*schema.json")):
        rel = schema.relative_to(dataset).as_posix()
        if "fixtures" in rel:
            continue
        distribution.append(mlc.FileObject(id=rel, name=rel, content_url=rel, encoding_formats=["application/json"],
                                           sha256=sha256(schema), description="JSON Schema for the records"))
    globs = sorted({p.relative_to(dataset).parent.as_posix() for p in dataset.rglob("*.json")
                    if p.parent.name in ("entries", "cases")})
    for g in globs:
        distribution.append(mlc.FileSet(id=f"{g}/", name=f"{g}/", includes=[f"{g}/*.json"],
                                        encoding_formats=["application/json"], description="One JSON record per file"))
    # Dates come from the records (date_added); a dataset whose records carry
    # none states its publication date in DATASETS. Nothing is read from git,
    # so the output is the same in a shallow CI clone.
    dates = entry_dates(dataset)
    published = dates[0] if dates else spec["published"]
    modified = dates[-1] if dates else None
    url = f"{REPO_URL}/tree/main/datasets/{name}"
    metadata = mlc.Metadata(
        name=name,
        description=f"{spec['title']}. {spec['description']}",
        url=url,
        license=spec["license"],
        conforms_to=[CROISSANT_1_1],
        version=version,
        cite_as=(f"OWASP GenAI Data Security Initiative. {spec['title']} (version {version}). "
                 f"OWASP GenAI Security Project. {url}"),
        date_published=datetime.fromisoformat(published) if published else None,
        date_modified=datetime.fromisoformat(modified) if modified else None,
        distribution=distribution,
        record_sets=record_sets,
        data_collection=spec["collection"],
        data_collection_type=spec["collection_type"],
        data_limitations=spec["limitations"],
        data_biases=spec["biases"],
        data_use_cases=spec["use_cases"],
        personal_sensitive_information=[spec["pii"]],
        data_social_impact=spec["social_impact"],
        data_release_maintenance_plan=MAINTENANCE,
    )
    issues = metadata.issues
    if issues.errors:
        raise SystemExit(f"{name}: {issues.report()}")
    return metadata.to_json()


def release_version() -> str:
    """The datasets release version, from CITATION.cff."""
    match = re.search(r"^version:\s*['\"]?([^'\"\s]+)", (REPO_ROOT / "CITATION.cff").read_text(encoding="utf-8"), re.M)
    if not match:
        raise SystemExit("CITATION.cff has no version")
    return match.group(1)


def render(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, default=str) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate Croissant 1.1 metadata for the datasets")
    parser.add_argument("--check", action="store_true", help="Fail if any croissant.json is out of date")
    args = parser.parse_args(argv)
    version = release_version()
    stale = []
    for name, spec in DATASETS.items():
        target = DATASETS_ROOT / name / "croissant.json"
        text = render(build(name, spec, version))
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != text:
                stale.append(target.relative_to(REPO_ROOT).as_posix())
        else:
            target.write_text(text, encoding="utf-8", newline="")  # LF on every platform
            print(f"wrote {target.relative_to(REPO_ROOT).as_posix()}")
    if stale:
        print("Out of date (run python data_validation/croissant/build_croissant.py): " + ", ".join(stale))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
