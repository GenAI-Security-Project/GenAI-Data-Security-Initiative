# Data Validation and Quality Control

Part of the [OWASP GenAI Data Security Initiative](../README.md) · Workstream 5

---

## Overview

This directory holds the validation and quality control (QC) tooling for the data in [`/datasets`](../datasets). Every pull request that changes `datasets/` or `data_validation/` runs it in CI (`.github/workflows/datasets-validate-all.yml`), and contributors can run the same thing locally with one command:

```bash
python data_validation/run_all_checks.py
```

The tooling has two jobs: keep the research data behind OWASP deliverables (the DSGAI risk taxonomy, framework mappings) accurate, and give the community validation code it can adapt for its own GenAI data security work.

---

## Validation Pipeline

### Stage 1 — Automated checks

`run_all_checks.py` runs two layers.

**1. Dataset validators.** Each dataset that has a `validate.py` (at its root, or in a sub-collection folder) is run in its own directory. Most are thin wrappers around a shared core, [`datasets/_shared/validate_lib.py`](../datasets/_shared/validate_lib.py) (schema with formats, DSGAI IDs, ID matches file name, duplicate IDs), plus the dataset's own extra rules. These are the authoritative checks for their data: schema conformance against the dataset's own `schema.json`, plus rules a schema cannot express. Datasets without one are listed as `NO VALIDATOR` so the gap is visible.

| Dataset | Own validator |
|---|---|
| [`agentdataflow_toolexchange_traces`](../datasets/agentdataflow_toolexchange_traces) | `validate.py`: schema, span graph, provenance evidence, secret and IP scan |
| [`exploit_dataset`](../datasets/exploit_dataset) | `validate.py`: schema, DSGAI IDs, ATLAS ID consistency |
| [`riskassessment_dataset`](../datasets/riskassessment_dataset) | `validate.py`: schema, DSGAI IDs |
| [`vulnerability_dataset`](../datasets/vulnerability_dataset) | `validate.py`: schema, DSGAI IDs |
| [`promptinj_dataextraction_testcases`](../datasets/promptinj_dataextraction_testcases) | `tr_turkish_conversation_prompt_injection_pairs/validate.py` for that collection only |
| [`rag_dataset`](../datasets/rag_dataset), [`incident_dataset`](../datasets/incident_dataset) | `validate.py`: schema (from `data_validation/schemas/`), DSGAI IDs, ID matches file name |
| [`crossframework_mapping_dataset`](../datasets/crossframework_mapping_dataset) | none; superseded by the [GenAI Crosswalk](https://github.com/GenAI-Security-Project/crosswalk) |

**2. Shared checks** (`validators/`), on every data file in every dataset:

| Check | ERROR (fails the run) | WARN (for the reviewer) |
|---|---|---|
| `schema_validator.py` | Schema violations, for files no dataset validator covers | File with no schema to check against |
| `dsgai_mapping_check.py` | DSGAI ID not in the taxonomy; a mapping value that is not a DSGAI ID | Same ID twice in one mapping; more than 6 mappings |
| `crossref_validator.py` | Malformed CVE/GHSA/CWE/ATLAS ID; CVE year in the future; unknown CWE, ATLAS, OWASP Top 10 (`LLM01:2026`, `ASI01:2026`) or NIST AI 100-2 (`NISTAML.018`) ID | Deprecated CWE; retired ATLAS ID; OWASP ID without its edition year; malformed ID in free text (often a placeholder) |
| `severity_check.py` | CVSS v3.x/v4.0 vector that doesn't parse; score that doesn't match its vector; qualitative rating outside the score's FIRST band | Score with no vector |
| `date_check.py` | Date that isn't ISO 8601; date in the future; documented, reported or observed after `date_added` | — |
| `metadata_check.py` | Licence field that doesn't resolve to one SPDX licence (ID, expression or full name; the ID is preferred); language field that isn't a BCP 47 tag of registered IANA subtags | Deprecated SPDX ID or language subtag |
| `anonymization_scanner.py` | — | Email addresses, keys and tokens, private or (in a network context) public IPs, internal hostnames, home paths, SSNs |
| `dedup_checker.py` | Two records in one dataset with the same ID | Records with identical or ≥ 80% similar text |

CI also runs **gitleaks** (pinned release, checksum-verified) over `datasets/` and `data_validation/`; a finding fails the PR.

Anonymization and similarity hits are warnings because a pattern cannot tell a real secret from a synthetic one; the prompt-injection datasets contain fake credentials on purpose. Use obviously fake values to keep a file quiet: `example.com` and other RFC 2606 domains, the RFC 5737 documentation addresses (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`), or placeholders such as `<API_KEY>` or `[API_KEY]`.

CVE and GHSA IDs are format-checked only; there is no offline list to confirm they exist. Framework control IDs (ISO, NIST, CIS) are not checked: see [`reference_data/SOURCES.md`](reference_data/SOURCES.md).

### Stage 2 — Peer review

After the automated checks pass, contributions are reviewed by cybersecurity and AI security practitioners from the initiative's contributor community. Peer review covers what tooling cannot reliably judge:

- **Accuracy and plausibility.** Does the entry describe a real, correctly characterized GenAI data security issue?
- **DSGAI alignment.** Is the mapping the best fit? Are secondary mappings needed? The tooling only confirms the IDs exist.
- **Severity calibration.** Is the severity consistent with similar entries?
- **Bias.** Does the contribution skew the dataset toward one vendor, framework or attack class? The QC reports below help here.
- **Responsible disclosure.** For exploits and vulnerabilities, is the technique already public?
- **Anonymization.** Are the scanner's warnings real? Is anything identifying that no pattern would catch?

---

## Quality control tools

`qc_tools/` produces reports for reviewers. CI writes the coverage report and the anomaly list to the job summary of every run.

| Script | What it reports |
|---|---|
| `bias_report.py` | Markdown coverage report: records per dataset, a DSGAI × dataset matrix, DSGAI entries nothing maps to, and the spread of severity and each dataset's categorical fields |
| `anomaly_detector.py` | A DSGAI entry most of a dataset maps to, records with far more mappings than usual, and one severity or category value dominating a dataset (datasets of 10+ records) |
| `online_check.py` | Runs weekly (`datasets-online-checks` workflow), not on PRs, because it needs the network. **Fails** on a CVE the CVE Program has rejected or doesn't know, a withdrawn GHSA, a dead cited link (with the Wayback Machine snapshot to use instead), or a CVE in CISA KEV whose entry isn't marked `exploited_in_the_wild`. Reports every CVE's EPSS v4 score and KEV status. These change daily, so they're reported, not stored |
| `ner_pii_scan.py` | Person names (and, in `incident_dataset`, organisation names) found by named-entity recognition (Microsoft Presidio + spaCy) in the datasets that require anonymization. Warnings only, in the CI job summary; reviewed false positives go in `reference_data/ner_allowlist.txt`. Optional dependencies: `requirements-ner.txt` |
| `croissant/build_croissant.py`, `croissant/check_croissant.py` | Generate each dataset's MLCommons Croissant 1.1 metadata (with RAI fields) and check it in CI: up to date with the data, valid per `mlcroissant`, and loadable record by record |
| `consistency_check.py` | **Fails** on internal references (`DSGAI-VULN-…`, `DSGAI-EXP-…`, `DSGAI-RA-…`) that point at no existing entry; notes CVEs cited by exploits that have no vulnerability entry |

---

## Running the checks

Python 3.11 or higher (CI tests 3.11, 3.12 and 3.13).

```bash
pip install -r data_validation/requirements.txt

python data_validation/run_all_checks.py                       # everything
python data_validation/run_all_checks.py --dataset datasets/exploit_dataset
python data_validation/run_all_checks.py --verbose             # every validator's output and every warning
python data_validation/run_all_checks.py --strict              # warnings fail too
python data_validation/run_all_checks.py --github              # also emit annotations (CI uses this)

# One check, on chosen files or datasets (each script's docstring has details)
python data_validation/validators/schema_validator.py --file datasets/rag_dataset/entries/RAG-0001.json
python data_validation/validators/dedup_checker.py --file my_new_entry.json --dataset datasets/exploit_dataset

# Reports
python data_validation/qc_tools/bias_report.py --output coverage.md
python data_validation/qc_tools/anomaly_detector.py
python data_validation/qc_tools/consistency_check.py
GITHUB_TOKEN=... python data_validation/qc_tools/online_check.py --summary online.md   # needs network

# Tests, lint, types and coverage for the tooling itself (what CI runs)
cd data_validation
pip install -r requirements-dev.txt
ruff check . ../datasets/_shared/validate_lib.py && mypy && python -m pytest --cov
```

**Dependencies.** Every `requirements*.txt` is a hash-pinned lock (each package, including transitive ones, pinned to one version with its SHA-256 hashes), so `pip install -r` installs exactly the reviewed artefacts on Linux, macOS or Windows. Edit the matching `requirements*.in` and run `python update_locks.py` (needs `uv`) to change them; Dependabot proposes updates weekly. Lint (ruff), type-checking (mypy) and coverage (at least 78%) are configured in `pyproject.toml` and run in CI.

`run_all_checks.py` exits 0 when everything passed, 1 on any failure, and 2 when there was nothing to check. In CI it runs with `--github`, so every finding also appears as an annotation on the exact line of the file in the pull request diff.

---

## Layout

```
data_validation/
├── run_all_checks.py        One command for everything (CI runs this)
├── requirements*.in / .txt  Dependency ranges / hash-pinned locks (update_locks.py)
├── pyproject.toml           ruff, mypy, pytest and coverage settings
├── validators/              Shared checks; each also runs on its own
├── qc_tools/                Reports for reviewers
├── croissant/               Croissant 1.1 metadata generator and checker
├── schemas/                 Schemas for datasets without their own schema.json
│                            (the rest are pointers to the dataset-local schemas)
├── reference_data/          DSGAI, MITRE ATLAS, CWE, OWASP Top 10, NIST AI 100-2, SPDX and
│                            IANA language lookup tables; see SOURCES.md
└── tests/                   Tests and deliberately valid/invalid fixtures
```

Dataset-local schemas (`datasets/<name>/schema.json`) are authoritative. `schemas/exploit`, `vulnerability`, `riskassessment` and `agentdataflow_trace` are kept only as `$ref` pointers to them; `schemas/incident`, `rag`, `crossframework_mapping` and `promptinj_testcase` are the only schemas for their data.

The ATLAS, CWE, SPDX and language tables are generated from their publishers' releases by `reference_data/update_reference_data.py`; don't edit them by hand. The `reference-data-refresh` workflow runs it on the 2nd of each month and, when MITRE has published something new, pushes a branch and opens an issue for a maintainer to turn into a PR. `owasp_top10.csv` and `nist_ai_100_2.csv` are maintained by hand when a new edition is published.

---

## Adapting the scripts

The scripts are plain Python with one runtime dependency (`jsonschema`) and are meant to be reused:

- **Tune the heuristics.** `DEFAULT_THRESHOLD` in `dedup_checker.py`, `PII_PATTERNS` in `anonymization_scanner.py`, `CONCENTRATION` and `SKEW` in `anomaly_detector.py`.
- **Add a schema.** Give a new dataset a `schema.json` and have its entries point at it with `"$schema"`; `schema_validator.py` finds it.
- **Add a reference table.** Put the list in `reference_data/`, record its source in `SOURCES.md`, and check against it in `crossref_validator.py`.
- **Wire it into your pipeline.** `run_all_checks.py` exit codes are CI-friendly, and each validator's check functions (`validate_file`, `check_data`, `check_records`) can be imported and return a list of findings.

---

## Contributing

Improvements are welcome: new checks, better patterns, fewer false positives, a `validate.py` for a sub-collection that has none. Include tests in `tests/`, and update this README with what the check does and which findings are errors versus warnings. Discuss ideas in `#team-genai-data-security-initiative` on the [OWASP Slack workspace](https://owasp.slack.com).
