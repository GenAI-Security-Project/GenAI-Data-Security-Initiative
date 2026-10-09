# Reference data sources

Lookup tables the validators check identifiers against.

| Table | File | Version | Source |
|---|---|---|---|
| DSGAI | `dsgai_entries.json` | 1.0 | OWASP GenAI Data Security Risks and Mitigations 2026 (kept identical to `datasets/_shared/dsgai_taxonomy.json`; a test enforces it) |
| MITRE ATLAS | `mitre_atlas_techniques.csv` | 2026.09 | latest release listed in `https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/manifest.yaml` |
| OWASP Top 10s | `owasp_top10.csv` | LLM 2025, LLM 2026, Agentic 2026 | LLM: `https://github.com/GenAI-Security-Project/GenAI-LLM-Top10` (2026 published 2026-08-04). Agentic: `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/` (published 2025-12-09) |
| CWE | `cwe_ids.csv` | 4.20 | `https://cwe.mitre.org/data/xml/cwec_latest.xml.zip` (weaknesses, categories and views) |

`owasp_top10.csv` is maintained by hand. The 2026 LLM list renumbered the entries (LLM03 was Supply Chain in 2025 and is Excessive Agency in 2026), so IDs always carry the edition year; `equivalent_2025` gives the 2025 ID each 2026 entry continues (LLM08:2026 Hidden Context Exposure broadens LLM07:2025 System Prompt Leakage). OWASP writes the Agentic IDs without a year (ASI01); this repository adds `:2026` so a future edition cannot collide.

Regenerate the ATLAS and CWE tables with `python update_reference_data.py`; it fills in the Version column. Do not edit those two CSVs by hand.

`datasets/_shared/dsgai_taxonomy.json` is the DSGAI list the validators use. `dsgai_entries.json` is kept because the Turkish prompt-injection validator reads it.

Framework control lists (ISO/IEC 27001, ISO/IEC 42001, CIS Controls, NIST) are not included. Complete lists are needed for a check to be useful, and the ISO and CIS texts are not freely redistributable, so framework control IDs are left to reviewers.
