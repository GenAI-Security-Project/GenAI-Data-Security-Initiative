# GenAI Data Security Incident Database

A structured, anonymized catalog of real-world data security incidents in GenAI deployments.

**Status:** Accepting contributions — this dataset is being built from scratch with the community.

## Scope

Documented incidents where GenAI systems experienced data security failures in production or staging environments. This includes data leakage events, cross-tenant bleed, RAG exfiltration, agent credential exposure, training data extraction, vector store compromise, telemetry over-collection, and any other incident aligned with the DSGAI risk taxonomy (DSGAI01–DSGAI21).

This dataset is modeled on existing incident databases (e.g., AIAAIC, AI Incident Database) but focused specifically on **data security failure modes** in GenAI systems.

## Data Format

Each entry is one JSON file in `entries/`, named after its `incident_id` (e.g. `entries/INC-0001.json`), that validates against [`data_validation/schemas/incident.schema.json`](../../data_validation/schemas/incident.schema.json). Start the file with `"$schema": "../../../data_validation/schemas/incident.schema.json"`. Check your entry with:

```bash
cd datasets/incident_dataset
python validate.py
```

Required fields are `incident_id`, `date`, `summary`, `dsgai_mapping`, `attack_vector`, `data_types_affected` and `impact`. Contributions should include where possible:

- **Incident ID** — Unique identifier (assigned on merge)
- **Date** — When the incident occurred or was disclosed
- **Summary** — Brief description of what happened
- **DSGAI mapping** — Primary DSGAI entry (DSGAI01–DSGAI21)
- **Attack vector** — How the data security failure occurred
- **Data types affected** — PII, PHI, credentials, IP, model weights, embeddings, etc.
- **Root cause** — Misconfiguration, missing control, architectural flaw, insider, etc.
- **Impact** — Scope of data exposed, regulatory consequences, operational disruption
- **Detection method** — How the incident was discovered
- **Mitigations applied** — What was done to remediate
- **Source** — Public advisory, news report, research paper, or anonymized self-report
- **Industry / sector** — If known and non-identifying

## Anonymization Requirements

All submissions **must** be anonymized:

- No organization names, employee names, or customer names
- No IP addresses, internal hostnames, or system identifiers
- No proprietary model names unless publicly known
- Generalize details that could identify a specific organization (e.g., "a financial services company" not "Bank X")

Self-reported incidents from your own organization are welcome and encouraged — anonymization makes this safe.

## Contributing

Add each incident as its own JSON file in `entries/` and submit a pull request. See the [main datasets README](../README.md) for general contribution guidelines.
