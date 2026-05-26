# OWASP GenAI Data Security Initiative

Part of the [OWASP GenAI Security Project](https://genai.owasp.org/) · [Data Security Initiative Page](https://genai.owasp.org/initiative/data-security/)

---

## Overview

The OWASP GenAI Data Security Initiative addresses the data security risks unique to Large Language Models, Generative AI, and Agentic AI systems. As AI introduces new data surfaces — prompts, context windows, embeddings, vector stores, agent traces, tool payloads — and new failure modes — prompt-driven extraction, cross-session bleed, inference attacks, plugin data drains — traditional data security frameworks no longer map cleanly to what needs protection.

This initiative produces community-developed, peer-reviewed guidance to help organizations understand and address these emerging challenges. All materials are released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

---

## Key Deliverables

### GenAI Data Security Risks and Mitigations 2026 (v1.0)

📄 [Download PDF](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/) · Released March 2026

A comprehensive enumeration of 21 data security risks specific to GenAI systems, each with tiered mitigations (Foundational → Hardening → Advanced) designed for organizations at different maturity levels. This is not a Top 10 — it is a structured risk taxonomy following data as it moves through a GenAI system.

Cross-referenced to the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) and the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/initiatives/agentic-security-initiative/).

<details>
<summary><strong>DSGAI Risk Taxonomy (21 entries)</strong></summary>

| ID | Risk |
| --- | --- |
| DSGAI01 | Sensitive Data Leakage |
| DSGAI02 | Agent Identity & Credential Exposure |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows |
| DSGAI04 | Data, Model & Artifact Poisoning |
| DSGAI05 | Data Integrity & Validation Failures |
| DSGAI06 | Tool, Plugin & Agent Data Exchange Risks |
| DSGAI07 | Data Governance, Lifecycle & Classification for AI Systems |
| DSGAI08 | Non-Compliance & Regulatory Violations |
| DSGAI09 | Multimodal Capture & Cross-Channel Data Leakage |
| DSGAI10 | Synthetic Data, Anonymization & Transformation Pitfalls |
| DSGAI11 | Cross-Context & Multi-User Conversation Bleed |
| DSGAI12 | Unsafe Natural-Language Data Gateways (LLM-to-SQL/Graph) |
| DSGAI13 | Vector Store Platform Data Security |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage |
| DSGAI15 | Over-Broad Context Windows & Prompt Over-Sharing |
| DSGAI16 | Endpoint & Browser Assistant Overreach |
| DSGAI17 | Data Availability & Resilience Failures in AI Pipelines |
| DSGAI18 | Inference & Data Reconstruction |
| DSGAI19 | Human-in-the-Loop & Labeler Overexposure |
| DSGAI20 | Model Exfiltration & IP Replication |
| DSGAI21 | Disinformation & Integrity Attacks via Data Poisoning |

Each entry follows a consistent structure: attack scenario in GenAI-specific terms, attacker capabilities, impact, and tiered mitigations with scope annotations (Buy / Build / Both).

</details>

### LLM and GenAI Data Security Best Practices 2025 (v1.0)

📄 [Download PDF](https://genai.owasp.org/resource/llm-and-gen-ai-data-security-best-practices/) · Released February 2025

The companion implementation guide covering data security principles, secure deployment architectures, monitoring and auditing guidelines, governance models, and future trends. Topics include data minimization, encryption strategies, access control for LLM pipelines, securing data flows in LLM agents, and regulatory compliance alignment.

---

## Framework Crosswalk

The initiative maintains a comprehensive crosswalk of GenAI data security risks against 20 widely recognized cybersecurity and AI frameworks. The crosswalk covers all 41 entries across the OWASP LLM Top 10 2025, Agentic Top 10 2026, and DSGAI Risk Taxonomy.

### 🌐 [Crosswalk →](https://genai-security-project.github.io/GenAI-Data-Security-Initiative/#/)
The web application provides an interactive interface for exploring crosswalk mappings, framework coverage, incident data, security tooling, implementation recipes, and a glossary of key terms.

Crosswalk source files are maintained in the [`/crosswalk`](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) directory.

### Frameworks Covered

**Cybersecurity & AI Standards** — NIST CSF 2.0, NIST AI RMF 1.0, ISO/IEC 27001, ISO/IEC 42001, ISO/IEC 23894, ISO/IEC 5338

**Threat Modeling & Adversarial** — MITRE ATT&CK, MITRE ATLAS, STRIDE, FAIR

**Application Security & Compliance** — CIS Controls, ASVS, SOC 2, PCI DSS, ENISA, CycloneDX ML SBOM

**Governance & Architecture** — COBIT, OPENCRE, SAMM, BSIMM

**OT / Industrial AI Security** — ISA/IEC 62443

---

## Workstreams

1. **Data Collection** — Public open call for real-world vulnerability data and incident reports related to LLMs and GenAI applications. Submit data through the Slack channel or by opening an issue in this repository.

2. **Framework Crosswalk** — Crosswalking the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) and [Agentic Top 10 2026](https://genai.owasp.org/initiatives/agentic-security-initiative/) to recognized cybersecurity and AI frameworks. See the [Crosswalk](https://genai-security-project.github.io/GenAI-Data-Security-Initiative/#/) and the [`/crosswalk`](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) directory for current crosswalk data.

3. **Data Security Risks & Best Practices** — Research, authoring, and maintenance of the initiative's two published white papers: the DSGAI risk taxonomy and the companion implementation guide. This workstream also maintains alignment with the broader OWASP GenAI Security Project deliverables.

4. **Community Datasets** — Development of open, community-contributed datasets for research, benchmarking, and security testing. See the [`/datasets`](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/datasets) directory for current and proposed datasets.

5. **Data Validation** — Automated and peer-reviewed validation of all contributed data. Scripts in [`/data_validation`](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/data_validation) ensure integrity and accuracy.

---

## Datasets

### Current

- **Vulnerability Dataset** — Real-world vulnerabilities affecting LLM applications
- **Exploit Dataset** — Documented exploits and attack techniques targeting LLMs
- **Risk Assessment Dataset** — Mapped risk assessments for various LLM deployments

### Proposed Community Datasets

We are looking for contributors to help build datasets for the broader AI security community. Priority areas include:

- **GenAI Data Security Incident Database** — Structured, anonymized catalog of real-world data security incidents in GenAI deployments (leakage events, cross-tenant bleed, RAG exfiltration, agent credential exposure), focused on failure modes enumerated in DSGAI01–DSGAI21.
- **Prompt Injection & Data Extraction Test Cases** — Adversarial prompts and extraction techniques mapped to the DSGAI risk taxonomy for red-teaming and regression testing.
- **RAG Poisoning & Retrieval Integrity Dataset** — Benign and adversarial document sets for testing vector store integrity, retrieval-time redaction, and poisoning detection.
- **Cross-Framework Control Crosswalk Dataset** — Machine-readable crosswalk of DSGAI risks to controls across NIST CSF 2.0, NIST AI RMF, MITRE ATLAS, ISO/IEC 42001, and OWASP LLM Top 10 for automated compliance gap analysis.
- **Agent Data Flow & Tool Exchange Traces** — Sanitized traces of agentic AI tool calls, plugin data exchanges, and delegation chains supporting research into DSGAI06 and related agent security patterns.

If you are interested in contributing, join the Slack channel or reach out directly.

---

## AI Risk Database Collaboration

The initiative collaborates with leading AI risk authorities to consolidate efforts and avoid fragmented approaches to risk identification:

- [MIT AI Risk Repository](https://airisk.mit.edu/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/risk-management-framework)

Community members are encouraged to report new GenAI data security risks to these organizations as well as to this initiative.

---

## How to Contribute

- **Slack:** Join `#team-genai-data-security-initiative` on the [OWASP Slack workspace](https://owasp.slack.com) · [New to OWASP Slack? Join here](https://owasp.org/slack/invite)
- **GitHub:** Submit issues or pull requests to this repository
- **Contact:** Reach out to Emmanuel Guilherme Junior (Initiative Lead) via [Slack](https://owasp.slack.com) or [LinkedIn](https://www.linkedin.com/in/emmanuelgjr/)

All contributions are welcome — from security practitioners, AI engineers, researchers, compliance professionals, and anyone working to secure GenAI systems.

---

## OWASP GenAI Security Project — Initiatives

This initiative is one of several under the [OWASP GenAI Security Project](https://genai.owasp.org/):

| Initiative | Description | Link |
| --- | --- | --- |
| **Agentic App Security** | Securing autonomous and agentic AI systems, including the Top 10 for Agentic Applications 2026 | [Initiative Page](https://genai.owasp.org/initiatives/agentic-security-initiative/) |
| **AI Red Teaming & Evaluation** | Methodology, benchmarks, and tools for adversarial testing of GenAI systems | [Initiative Page](https://genai.owasp.org/initiatives/#ai-redteaming) |
| **AI Security Solutions Landscape** | Vendor-agnostic mapping of the GenAI security tooling ecosystem | [Solutions Directory](https://genai.owasp.org/ai-security-solutions-landscape/) |
| **AIBOM Generator** | Open-source tool for generating AI Bills of Materials for supply chain transparency | [Initiative Page](https://genai.owasp.org/ai-sbom-initiative/) |
| **Data Security** | GenAI data security risks, mitigations, best practices, and framework crosswalks *(this initiative)* | [Initiative Page](https://genai.owasp.org/initiative/data-security/) |
| **Governance Checklist (COMPASS)** | Cybersecurity and governance checklist for LLM and GenAI deployments | [Resource Page](https://genai.owasp.org/resource/llm-applications-cybersecurity-and-governance-checklist-english/) |
| **Secure AI Adoption** | Center of Excellence guidance for safe, ethical, and secure organizational AI adoption | [Initiative Page](https://genai.owasp.org/initiatives/#secure-ai-adoption) |
| **Threat Intelligence** | Research into LLM-enabled exploit generation and deepfake threat preparation | [Initiative Page](https://genai.owasp.org/initiatives/#ai-threat-intel) |

---

## Acknowledgments

**Initiative Lead:** [Emmanuel Guilherme Junior](https://www.linkedin.com/in/emmanuelgjr/)

This initiative is made possible by the contributions of its authors, contributors, and reviewers from across the global AI security community. Thank you to everyone who has helped build and shape this community resource. Full contributor lists are included in each published document.

---

## License

All materials produced by this initiative are licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

You are free to share and adapt the material for any purpose, including commercial, under the following terms: provide appropriate attribution including the project name and asset name, and distribute any derivative works under the same license.
