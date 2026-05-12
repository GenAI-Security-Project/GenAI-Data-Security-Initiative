# OWASP GenAI Crosswalk — Master Cross-Reference

This is the single navigation index across all three OWASP GenAI source lists.
Read left to right: an LLM vulnerability ? its agentic amplification ? its data security dimension.

> **How to use:** Find the risk you care about in any column, then follow the row to see how it surfaces in the other lists and which framework files cover it.

---

## Cross-reference table

| LLM Top 10 2025 | Agentic Top 10 2026 | DSGAI 2026 | Primary frameworks |
|---|---|---|---|
| LLM01 Prompt Injection | ASI01 Agent Goal Hijack | DSGAI01 Sensitive Data Leakage | MITRE ATLAS · AIUC-1 B001/B005 · NIST AI RMF · ASVS |
| LLM01 Prompt Injection | ASI02 Tool Misuse | DSGAI12 Unsafe NL Data Gateways | MITRE ATLAS · AIUC-1 B006 · ISA 62443 · STRIDE |
| LLM02 Sensitive Info Disclosure | ASI03 Identity & Privilege Abuse | DSGAI01 Sensitive Data Leakage | ISO 27001 · ISO 27701 · AIUC-1 A · SOC 2 · PCIDSS |
| LLM02 Sensitive Info Disclosure | ASI03 Identity & Privilege Abuse | DSGAI02 Agent Identity & Credential Exposure | OWASP NHI · AIUC-1 B007 · NIST CSF 2.0 · ISO 27001 |
| LLM03 Supply Chain | ASI04 Agentic Supply Chain | DSGAI04 Data Model & Artifact Poisoning | CycloneDX ML SBOM · NIST SP 800-218A · BSIMM · SAMM |
| LLM04 Data & Model Poisoning | ASI06 Memory & Context Poisoning | DSGAI04 Data Model & Artifact Poisoning | MITRE ATLAS · AIUC-1 A · CIS Controls · AITG |
| LLM04 Data & Model Poisoning | ASI06 Memory & Context Poisoning | DSGAI21 Disinformation via Data Poisoning | MITRE ATT&CK · STRIDE · ENISA · EU AI Act |
| LLM05 Insecure Output Handling | ASI02 Tool Misuse | DSGAI05 Data Integrity & Validation Failures | ASVS · CIS Controls · NIST CSF 2.0 · AIUC-1 B009 |
| LLM06 Excessive Agency | ASI01 Agent Goal Hijack | DSGAI06 Tool Plugin & Agent Data Exchange | AIUC-1 B006 · ISA 62443 · NIST AI RMF · COBIT |
| LLM06 Excessive Agency | ASI10 Rogue Agents | DSGAI16 Endpoint & Browser Overreach | AIUC-1 C · MITRE ATLAS · STRIDE · EU AI Act |
| LLM07 System Prompt Leakage | ASI01 Agent Goal Hijack | DSGAI15 Over-Broad Context Windows | AIUC-1 B003/B009 · ISO 27001 · CIS Controls · ASVS |
| LLM08 Vector & Embedding Weaknesses | ASI06 Memory & Context Poisoning | DSGAI13 Vector Store Platform Security | MITRE ATLAS · AIUC-1 A · NIST AI RMF · CWE/CVE |
| LLM09 Misinformation | ASI09 Human-Agent Trust Exploitation | DSGAI21 Disinformation via Data Poisoning | AIUC-1 C/F · EU AI Act · ENISA · NIST AI RMF |
| LLM10 Unbounded Consumption | ASI08 Cascading Failures | DSGAI17 Data Availability & Resilience Failures | AIUC-1 D · ISA 62443 · NIST SP 800-82 · CIS Controls |
| — | ASI05 Unexpected Code Execution | DSGAI12 Unsafe NL Data Gateways | MITRE ATT&CK · AIUC-1 B006 · ASVS · CWE/CVE |
| — | ASI07 Insecure Inter-Agent Comms | DSGAI02 Agent Identity & Credential Exposure | OWASP NHI · AIUC-1 E · ISA 62443 · ISO 27001 |
| — | — | DSGAI03 Shadow AI & Unsanctioned Data Flows | COBIT · ISO 27001 · ENISA · CIS Controls |
| — | — | DSGAI07 Data Governance & Lifecycle | ISO 42001 · ISO 27701 · EU AI Act · NIST AI RMF |
| — | — | DSGAI08 Non-Compliance & Regulatory Violations | EU AI Act · ISO 42001 · ISO 27701 · PCIDSS · SOC 2 |
| — | — | DSGAI09 Multimodal Cross-Channel Leakage | ISO 27001 · AIUC-1 A · CIS Controls · ENISA |
| — | — | DSGAI10 Synthetic Data & Anonymization Pitfalls | ISO 27701 · NIST AI RMF · EU AI Act · ENISA |
| — | — | DSGAI11 Cross-Context Conversation Bleed | ASVS · ISO 27001 · NIST CSF 2.0 · AIUC-1 A |
| — | — | DSGAI14 Excessive Telemetry & Monitoring Leakage | ISO 27001 · CIS Controls · SOC 2 · NIST CSF 2.0 |
| — | — | DSGAI18 Inference & Data Reconstruction | MITRE ATLAS · ISO 27701 · ENISA · AIUC-1 A |
| — | — | DSGAI19 Human-in-Loop & Labeler Overexposure | ISO 27701 · EU AI Act · NIST AI RMF · BSIMM |
| — | — | DSGAI20 Model Exfiltration & IP Replication | MITRE ATLAS · CWE/CVE · ISO 27001 · AIUC-1 B |

---

## OT / ICS lens

For OT environments, these entries carry the highest blast radius:

| Risk | Why it matters in OT | Primary OT frameworks |
|---|---|---|
| LLM01 / ASI01 | NL-to-SCADA interfaces make prompt injection a process disruption risk | ISA/IEC 62443 · NIST SP 800-82 |
| LLM10 / ASI08 | Cascading failures in OT can affect physical safety systems | ISA/IEC 62443 SR 7.1 · NIST SP 800-82 |
| ASI02 Tool Misuse | AI agents with OT tool access can trigger physical actions | ISA/IEC 62443 · NIST SP 800-82 |
| DSGAI12 | LLM-to-SQL/historian gateways in OT expose process data | ISA/IEC 62443 · NIST SP 800-82 |
| DSGAI17 | RAG failures in OT AI affect real-time operational decisions | ISA/IEC 62443 SR 7.6 · NIST SP 800-82 |

---

## Framework index

Jump directly to any framework mapping folder:

### LLM Top 10 mappings ? [`/llm-top10/`](llm-top10/)
### Agentic Top 10 mappings ? [`/agentic-top10/`](agentic-top10/)
### DSGAI 2026 mappings ? [`/dsgai-2026/`](dsgai-2026/)
### Shared resources ? [`/shared/`](shared/)
### Machine-readable data ? [`/data/`](data/)

---

*Last updated: 2026-Q1 | Maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
