# Cross-Framework Control Mapping Dataset

Machine-readable mappings of DSGAI risks to controls across major cybersecurity and AI governance frameworks.

**Status:** Accepting contributions — this dataset is being built from scratch with the community.

## Scope

Structured, machine-readable mappings that connect each DSGAI entry (DSGAI01–DSGAI21) to the specific controls, requirements, and guidelines in recognized security and AI frameworks. Unlike the narrative mappings in the `/mappings` directory, this dataset is designed for **automated consumption** — enabling compliance gap analysis tools, GRC platforms, and audit automation.

Target frameworks for mapping:

- **NIST Cybersecurity Framework (CSF) 2.0** — Functions, categories, and subcategories
- **NIST AI RMF 1.0 (AI 100-1)** — Map, Measure, Manage, Govern functions
- **MITRE ATLAS** — Techniques and mitigations
- **MITRE ATT&CK** — Relevant enterprise techniques
- **ISO/IEC 42001** — AI management system controls
- **ISO/IEC 27001** — Annex A controls
- **CIS Controls v8** — Safeguards
- **OWASP Top 10 for LLM Applications 2025** — Entries and mitigations
- **OWASP Top 10 for Agentic Applications 2026** — Entries and mitigations
- **EU AI Act** — Relevant articles and requirements
- **GDPR** — Relevant articles
- **SOC 2** — Trust Services Criteria

## Data Format

Mappings should be provided in JSON or CSV with the following structure:

```json
{
  "dsgai_id": "DSGAI01",
  "dsgai_name": "Sensitive Data Leakage",
  "framework": "NIST CSF 2.0",
  "control_id": "PR.DS-01",
  "control_name": "Data-at-rest is protected",
  "relationship": "mitigates",
  "notes": "Applies to training data, embeddings, and vector store contents at rest",
  "mitigation_tier": "Tier 1"
}
```

Fields:

- **dsgai_id** — DSGAI entry identifier (DSGAI01–DSGAI21)
- **dsgai_name** — DSGAI entry name
- **framework** — Target framework name and version
- **control_id** — The specific control, requirement, or article identifier in the target framework
- **control_name** — Human-readable name of the control
- **relationship** — `mitigates`, `detects`, `governs`, `partially_addresses`, or `related`
- **notes** — GenAI-specific context for how this control applies
- **mitigation_tier** — Which DSGAI mitigation tier (Tier 1 / Tier 2 / Tier 3) the control aligns with, if applicable

## Contributing

Add mappings as JSON or CSV files organized by framework (e.g., `nist_csf2_mapping.json`, `mitre_atlas_mapping.csv`). Submit a pull request. See the [main datasets README](../README.md) for general contribution guidelines.
