# Risk Assessment Dataset

Anonymized, structured risk assessments of GenAI deployment archetypes — each entry walks DSGAI risks (inherent + residual), existing controls, control gaps, and framework alignments for a representative architecture.

## Scope

The dataset documents **deployment archetypes**, not specific organizations. Each entry is a synthetic-but-realistic scenario covering:

- The data the deployment handles and who interacts with it
- The major architectural components
- Which DSGAI risks (DSGAI01–DSGAI21) apply, rated before and after controls
- What mitigations are typical at the maturity level depicted
- What's commonly missing (control gaps), with suggested remediation and urgency
- How the posture maps to recognized frameworks — NIST CSF 2.0, NIST AI RMF, ISO/IEC 42001, ISO/IEC 27001, plus sector-triggered controls (EU AI Act, GDPR, HIPAA, FERPA, PCI DSS, SOC 2)

The initial corpus is **23 deployment archetypes** spanning financial services (consumer RAG, claims triage, research analyst), healthcare (clinical-decision support), legal (contract review), public sector (citizen chatbot), education (K-12 tutoring), HR (resume screening, employee chatbot), retail/e-commerce (shopping agent), automotive (in-vehicle voice), cybersecurity (SOC analyst copilot), technology/SaaS (code assistant, multi-tenant feature, DevOps copilot, self-hosted open-weights), telecom (multi-agent support), and cross-sector productivity patterns (enterprise search, browser assistant, email triage, translation, marketing content, synthetic-data pipeline).

## Layout

```
riskassessment_dataset/
├── README.md            # this file
├── schema.json          # JSON Schema 2020-12 — canonical definition
├── example.json         # fully populated example (customer-facing banking RAG)
├── entries/             # one JSON file per archetype
├── index.csv            # generated flat index (risk-rating summary + gap counts)
├── build_index.py       # regenerate index.csv from entries/
└── validate.py          # validate every entry against schema.json
```

DSGAI taxonomy referenced by `dsgai_id` fields lives at [`../_shared/dsgai_taxonomy.json`](../_shared/dsgai_taxonomy.json).

## Schema (summary)

Canonical schema: [`schema.json`](./schema.json). Reference entry: [`example.json`](./example.json).

| Field | Required | Notes |
|---|---|---|
| `assessment_id` | yes | `DSGAI-RA-<slug>` |
| `scenario_name` | yes | Short name |
| `entry_type` | yes | `synthetic_template` \| `anonymized_real` \| `public_reference_architecture` |
| `industry_sector` | yes | Enum: financial_services, healthcare, public_sector, education, retail_ecommerce, manufacturing, technology_saas, energy_utilities, legal_professional_services, hospitality_travel, media_marketing, automotive, telecom, cybersecurity, hr_staffing, cross_sector, other |
| `deployment_pattern` | yes | Enum: customer_facing_chatbot, internal_knowledge_assistant, code_assistant, multi_agent_workflow, content_generation, browser_endpoint_assistant, email_triage, search_aggregator, training_or_data_pipeline, mlops_platform, voice_assistant, decision_support, soc_analyst_copilot, self_hosted_inference, embedded_saas_feature, other |
| `description` | yes | 3–8 sentence scenario description |
| `assumptions` | no | Stated assumptions that scope the assessment |
| `components` | yes (≥3) | Architectural components with role + description + optional sensitivity_tier |
| `risks_identified` | yes (≥5) | Per-DSGAI risk entries: `dsgai_id`, `inherent_rating`, `rationale`, optional `residual_rating` + `residual_rationale` |
| `existing_controls` | no | Mitigations in place; each with optional tier and `addresses_dsgai[]` |
| `control_gaps` | no | Missing/weak mitigations; each with `urgency` (Immediate/Near-term/Strategic) and optional `suggested_remediation` |
| `framework_alignments` | yes (≥4) | Mappings to NIST CSF 2.0, NIST AI RMF, ISO/IEC 42001/27001, OWASP LLM/Agentic Top 10, MITRE ATLAS/ATT&CK, EU AI Act, GDPR, HIPAA, FERPA, PCI DSS 4.0, SOC 2, FedRAMP, Other |
| `compliance_obligations` | no | Regimes the deployment likely operates under |
| `maturity_overall` | no | CMMI-like: Initial/Developing/Defined/Managed/Optimizing |
| `source_urls` | no | Optional inspirational references |
| `date_added` | yes | ISO date |
| `tags` | no | Free-form tags |
| `notes` | no | Author caveats |

Top-level `$schema` pointer permitted for editor tooling.

## Anonymization (hard rule)

Per the upstream README's requirement, **all submissions must be anonymized**:

- No organization names, employee names, customer names, or proprietary system names.
- No IP addresses, internal hostnames, or system identifiers.
- Generalize details that could identify a specific deployment ("a retail bank" not "Bank X").

The v1 corpus is entirely synthetic-template entries — none describe a real, identifiable deployment. The schema supports `entry_type: anonymized_real` for contributors who have a real assessment they have carefully anonymized.

## Tooling

```bash
# install once
pip install jsonschema

# validate every entry against schema.json
python validate.py

# regenerate index.csv after adding or editing entries
python build_index.py
```

The generated `index.csv` includes summary columns useful for compliance buyers and roadmap planning: highest inherent and residual risk ratings, control and gap counts, count of `Immediate`-urgency gaps, frameworks mapped, and compliance obligations.

## Contributing

1. Fork the repository.
2. Add a new file under `entries/` named `DSGAI-RA-<slug>.json`.
3. Confirm your entry is anonymized — no organization, employee, customer, or system names; no IPs or hostnames.
4. Run `python validate.py` and fix any failures.
5. Run `python build_index.py` to refresh `index.csv`.
6. Submit a PR with a one-paragraph description of the archetype.

See [`../README.md`](../README.md) for cross-dataset contribution norms.
