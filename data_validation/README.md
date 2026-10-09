# Data Validation and Quality Control

Part of the [OWASP GenAI Data Security Initiative](../README.md) · Workstream 5

---

## Overview

This directory contains the data validation and quality control (QC) framework for all data contributed to the OWASP GenAI Data Security Initiative. Every dataset in the [`/datasets`](../datasets) directory — whether community-contributed vulnerability reports, incident records, framework mappings, or adversarial test cases — passes through this validation pipeline before being accepted.

The framework serves two purposes: ensuring the integrity and accuracy of research data that informs OWASP deliverables (Top 10 for LLM Applications, DSGAI risk taxonomy, framework mappings), and providing reusable validation tooling that the community can adapt for their own GenAI data security workflows.

---

## What Gets Validated

| Dataset | Key Validation Checks |
|---|---|
| [`vulnerability_dataset`](../datasets/vulnerability_dataset) | DSGAI mapping accuracy, CVE/CWE reference verification, severity consistency, deduplication |
| [`exploit_dataset`](../datasets/exploit_dataset) | Source verification, MITRE ATLAS alignment, prerequisite completeness, responsible disclosure check |
| [`riskassessment_dataset`](../datasets/riskassessment_dataset) | Anonymization verification, DSGAI coverage, framework control alignment, internal consistency |
| [`incident_dataset`](../datasets/incident_dataset) | Anonymization completeness, DSGAI mapping, source attribution, deduplication against existing entries |
| [`promptinj_dataextraction_testcases`](../datasets/promptinj_dataextraction_testcases) | DSGAI mapping, expected behavior definitions, severity classification, no undisclosed zero-days |
| [`rag_dataset`](../datasets/rag_dataset) | Synthetic data verification (no real PII/PHI), payload labeling, adversarial content safety check |
| [`crossframework_mapping_dataset`](../datasets/crossframework_mapping_dataset) | Control ID verification against source framework, relationship type accuracy, schema compliance |
| [`agentdataflow_toolexchange_traces`](../datasets/agentdataflow_toolexchange_traces) | Sanitization completeness (no real credentials/PII), structural integrity, DSGAI annotation accuracy |

---

## Validation Pipeline

All contributed data goes through a two-stage validation process.

### Stage 1 — Automated Validation

Automated scripts in this directory perform structural and consistency checks on contributed data. These run on every pull request that modifies the `/datasets` directory.

**Schema validation** — Verifies that contributed files conform to the expected schema for their dataset (field names, types, required fields, allowed values). Each dataset defines its schema in its own README.

**DSGAI mapping verification** — Checks that referenced DSGAI IDs (DSGAI01–DSGAI21) exist and that the mapping is plausible given the content. Flags entries that reference non-existent IDs or where the described risk clearly misaligns with the mapped DSGAI entry.

**Cross-reference verification** — For entries that cite CVEs, CWEs, MITRE ATLAS technique IDs, or framework control IDs, validates that the referenced identifiers exist and are formatted correctly.

**Deduplication** — Compares new entries against existing dataset records to identify potential duplicates based on content similarity, source URLs, and key field matching.

**Anonymization checks** — For datasets requiring anonymization (incidents, risk assessments, agent traces), scans for patterns that may indicate residual PII, credentials, internal hostnames, or organization-identifying information.

**Completeness checks** — Verifies that all required fields are populated and that optional fields, when present, contain valid data.

### Stage 2 — Peer Review

After automated checks pass, contributions are reviewed by cybersecurity and AI security experts from the initiative's contributor community. Peer review focuses on areas that automated tooling cannot reliably assess.

**Accuracy and plausibility** — Does the described vulnerability, incident, or technique reflect a real and correctly characterized GenAI data security issue?

**DSGAI alignment quality** — Is the DSGAI mapping the best fit, or would a different entry be more appropriate? Are secondary mappings needed?

**Severity calibration** — Is the assigned severity consistent with similar entries in the dataset and with the DSGAI mitigation tier structure?

**Bias assessment** — Does the contribution introduce systematic bias into the dataset (e.g., overrepresentation of a specific vendor, framework, or attack class)?

**Responsible disclosure** — For exploit and vulnerability entries, confirms that the technique is publicly documented and that submission does not constitute premature disclosure.

---

## Scripts

### Validation Scripts

| Script | Purpose |
|---|---|
| `schema_validator.py` | Validates contributed files against dataset-specific JSON schemas |
| `dsgai_mapping_check.py` | Verifies DSGAI ID references and flags mapping misalignments |
| `crossref_validator.py` | Checks CVE, CWE, MITRE ATLAS, and framework control ID references |
| `dedup_checker.py` | Identifies potential duplicate entries across datasets |
| `anonymization_scanner.py` | Scans for residual PII, credentials, and identifying information |
| `completeness_check.py` | Reports missing required fields and invalid optional field values |

### Quality Control Tools

| Script | Purpose |
|---|---|
| `anomaly_detector.py` | Identifies statistical outliers in severity distributions, DSGAI mapping concentrations, and submission patterns |
| `bias_report.py` | Generates coverage reports showing dataset distribution across DSGAI entries, industries, attack vectors, and frameworks to surface gaps and overrepresentation |
| `consistency_check.py` | Cross-validates related entries across datasets (e.g., an exploit entry should have a corresponding vulnerability entry if both describe the same issue) |

---

## Adapting the Scripts

These scripts are designed to be reusable. Organizations can adapt them for validating their own internal GenAI security data. Common adaptations include:

**Parameter tuning** — Adjusting similarity thresholds for deduplication, modifying anonymization detection patterns for your data types, or tuning anomaly detection sensitivity.

**Custom schema definitions** — Adding dataset-specific schemas for internal data formats beyond what the initiative uses.

**Additional cross-references** — Extending the cross-reference validator to check against internal control frameworks, proprietary vulnerability databases, or organization-specific risk taxonomies.

**CI/CD integration** — Wiring the validation scripts into your own pull request or data ingestion pipelines.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

### Setup

```bash
cd data_validation
pip install -r requirements.txt
```

### Running Validation

```bash
# Validate a single contributed file
python schema_validator.py --file ../datasets/vulnerability_dataset/new_entry.json

# Run every dataset's own validate.py (or one dataset with --dataset)
python run_all_checks.py
python run_all_checks.py --dataset ../datasets/exploit_dataset/

# Generate a bias and coverage report for all datasets
python bias_report.py --datasets ../datasets/
```

Refer to the docstring at the top of each script for detailed usage, configuration options, and output format.

---

## Contributing

Improvements to the validation framework are welcome — new checks, better detection patterns, performance improvements, and additional schema definitions. Submit a pull request or discuss ideas in `#team-genai-data-security-initiative` on the [OWASP Slack workspace](https://owasp.slack.com).

When contributing new validation scripts, include unit tests and update this README with the script's purpose and usage.
