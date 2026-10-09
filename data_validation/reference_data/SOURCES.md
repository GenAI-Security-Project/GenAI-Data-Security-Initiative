# Reference data sources

Lookup tables the validators check identifiers against.

| Table | File | Version | Source |
|---|---|---|---|
| DSGAI | `dsgai_entries.json` | 1.0 | OWASP GenAI Data Security Risks and Mitigations 2026 (kept identical to `datasets/_shared/dsgai_taxonomy.json`; a test enforces it) |
| MITRE ATLAS | `mitre_atlas_techniques.csv` | 2026.09 | latest release listed in `https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/manifest.yaml` |
| CWE | `cwe_ids.csv` | 4.20 | `https://cwe.mitre.org/data/xml/cwec_latest.xml.zip` (weaknesses, categories and views) |

Regenerate the ATLAS and CWE tables with `python update_reference_data.py`; it fills in the Version column. Do not edit those two CSVs by hand.

`datasets/_shared/dsgai_taxonomy.json` is the DSGAI list the validators use. `dsgai_entries.json` is kept because the Turkish prompt-injection validator reads it.

Framework control lists (ISO/IEC 27001, ISO/IEC 42001, CIS Controls, NIST) are not included. Complete lists are needed for a check to be useful, and the ISO and CIS texts are not freely redistributable, so framework control IDs are left to reviewers.
