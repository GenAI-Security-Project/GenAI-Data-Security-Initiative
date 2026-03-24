# OWASP GenAI Data Security Initiative

Part of the [OWASP GenAI Security Project](https://genai.owasp.org/) · [Data Security Initiative Page](https://genai.owasp.org/initiative/data-security/)

---

## Overview

The OWASP GenAI Data Security Initiative focuses on the data security risks and best practices specific to Large Language Models (LLMs), Generative AI, and Agentic AI systems. As AI systems create new data surfaces — prompts, context windows, embeddings, vector stores, agent traces, tool payloads — and new failure modes — prompt-driven extraction, cross-session bleed, inference attacks, plugin and tool data drains — traditional data security frameworks no longer map cleanly to what needs protection.

This initiative produces community-developed, peer-reviewed guidance to help organizations understand and address these emerging data security challenges. All materials are released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

---

## Key Deliverables

### GenAI Data Security Risks and Mitigations 2026 (v1.0)

📄 [Download PDF](<!-- TODO: Add link to published PDF -->) · Released March 2026

A focused enumeration of 21 data security risks specific to GenAI systems, each with tiered mitigations (Foundational → Hardening → Advanced) designed to support organizations at different stages of security maturity. This is not a Top 10 — it is a comprehensive, structured risk taxonomy following data as it moves through a GenAI system.

Aligned with and cross-referenced to the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) and the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/initiatives/agentic-security-initiative/).

<details>
<summary><strong>DSGAI Risk Taxonomy (21 entries)</strong></summary>

| ID | Risk |
|---|---|
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

Each entry follows a consistent structure: how the attack unfolds in GenAI-specific terms, an illustrative scenario, attacker capabilities, impact, and tiered mitigations with scope annotations (Buy / Build / Both).

</details>

### LLM and GenAI Data Security Best Practices 2025 (v1.0)

📄 [Download PDF](https://genai.owasp.org/resource/llm-and-gen-ai-data-security-best-practices/) · Released February 2025

The companion implementation guide covering practical data security principles, secure deployment architectures, monitoring and auditing guidelines, governance models, and future trends. Topics include data minimization, encryption strategies, access control for LLM pipelines, securing data flows in LLM agents, and regulatory compliance alignment.

---

## Workstreams

### 1. Data Collection

Public open call for real-world data on vulnerabilities and risks associated with LLMs and GenAI applications. This workstream supports future iterations of the OWASP Top 10 for LLM Applications and related guidance by gathering incident data, vulnerability reports, and field observations from the global community.

Community members are encouraged to submit data through the Slack channel or by opening an issue in this repository.

### 2. Mapping

Mapping of the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) and the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/initiatives/agentic-security-initiative/) to recognized cybersecurity frameworks and standards, including NIST CSF 2.0, NIST AI RMF, MITRE ATT&CK, MITRE ATLAS, ISO/IEC 42001, CIS Controls, and others.

Full mapping files are maintained in the [`/mappings`](./mappings) directory. See the [Framework Mappings](#framework-mappings) section for the complete list of mapped frameworks.

### 3. Data Security Risks and Best Practices

Research, authoring, and maintenance of the initiative's two published white papers:

- **GenAI Data Security Risks and Mitigations 2026** — The 21-entry DSGAI risk taxonomy with tiered mitigations
- **LLM and GenAI Data Security Best Practices 2025** — The companion implementation and governance guide

This workstream also maintains alignment with the broader OWASP GenAI Security Project deliverables and ensures cross-references to the LLM Top 10 and Agentic Top 10.

### 4. Community Datasets

Development of open, community-contributed datasets to support research, benchmarking, and practical security testing for GenAI data security. This workstream covers both the curation of existing datasets and the creation of new ones addressing gaps in the current landscape. See the [`/datasets`](./datasets) section for current and proposed datasets.

### 5. Data Validation

Automated and peer-reviewed validation of all data collected and contributed to the initiative. Scripts in the [`/data_validation`](./data_validation) directory ensure integrity and accuracy. All submissions are also subject to manual verification by cybersecurity and AI security experts.

---

## Datasets

### Current

- **Vulnerability Dataset** — Real-world vulnerabilities affecting LLM applications
- **Exploit Dataset** — Documented exploits and attack techniques targeting LLMs
- **Risk Assessment Dataset** — Mapped risk assessments for various LLM deployments

### Proposed Community Datasets

We are looking for contributors to help build datasets that the broader AI security community can use. Priority areas include:

- **GenAI Data Security Incident Database** — A structured, anonymized catalog of real-world data security incidents in GenAI deployments (leakage events, cross-tenant bleed, RAG exfiltration, agent credential exposure). Modeled on existing incident databases but focused specifically on the data security failure modes enumerated in DSGAI01–DSGAI21.
- **Prompt Injection & Data Extraction Test Cases** — A curated set of adversarial prompts and extraction techniques mapped to the DSGAI risk taxonomy, usable for red-teaming and regression testing of data security controls.
- **RAG Poisoning & Retrieval Integrity Dataset** — Benign and adversarial document sets for testing vector store integrity controls, retrieval-time redaction, and poisoning detection pipelines.
- **Cross-Framework Control Mapping Dataset** — A machine-readable mapping of DSGAI risks to controls across NIST CSF 2.0, NIST AI RMF, MITRE ATLAS, ISO/IEC 42001, and the OWASP Top 10 for LLM Applications — enabling automated compliance gap analysis.
- **Agent Data Flow & Tool Exchange Traces** — Sanitized traces of agentic AI tool calls, plugin data exchanges, and delegation chains to support research into DSGAI06 (tool/plugin data exchange risks) and related agent security patterns.

If you are interested in contributing to any of these datasets, please join the Slack channel or reach out directly.

---

## Framework Mappings

The initiative maps GenAI data security risks to widely recognized frameworks. Full mapping files are maintained in the [`/mappings`](./mappings) directory. The frameworks below are selected for direct relevance to securing GenAI systems.

### Foundational Cybersecurity & AI Standards

| Framework | Relevance to GenAI |
|---|---|
| **NIST Cybersecurity Framework (CSF) 2.0** | Foundational risk management applicable to AI system governance |
| **NIST AI RMF 1.0 (AI 100-1)** | AI-specific risk management covering reliability, robustness, and trustworthiness |
| **ISO/IEC 27001** | Information security management and compliance baseline |
| **ISO/IEC 42001** | AI management system standard — traceability, transparency, and ethical considerations |
| **ISO/IEC 23894** | AI risk management guidance |
| **ISO/IEC 5338** | AI and ML system lifecycle processes |

### Threat Modeling & Adversarial Frameworks

| Framework | Relevance to GenAI |
|---|---|
| **MITRE ATT&CK** | Adversarial tactics and techniques for threat modeling |
| **MITRE ATLAS** | Adversarial threat landscape for AI systems — attack techniques specific to ML/AI |
| **STRIDE** | Threat modeling methodology for early-stage security design |
| **FAIR** | Quantifying cybersecurity risk in financial terms |

### Application Security & Compliance

| Framework | Relevance to GenAI |
|---|---|
| **CIS Controls** | Practical, actionable security controls |
| **ASVS** | Application security verification for web-facing LLM interfaces |
| **SOC 2** | Service provider security — relevant for LLM-as-a-Service deployments |
| **PCI DSS** | Data security for payment-adjacent LLM applications |
| **ENISA** | EU cybersecurity guidance — critical for European regulatory compliance |
| **CycloneDX ML SBOM** | Software supply chain transparency for ML models and components |

### Governance & Architecture

| Framework | Relevance to GenAI |
|---|---|
| **COBIT** | IT governance alignment with enterprise objectives |
| **OPENCRE** | Cross-framework control alignment and interoperability |
| **SAMM** | Software assurance maturity for AI development practices |
| **BSIMM** | Measuring and benchmarking software security initiatives |

### OT / Industrial AI Security

| Framework | Relevance to GenAI |
|---|---|
| **ISA/IEC 62443** | ICS security — critical for GenAI deployments in industrial and OT environments |

> **Note:** The Agentic Top 10 2026 mappings are in progress and will be added to the `/mappings` directory as they are completed.

---

## AI Risk Database Collaboration

The initiative collaborates with leading AI risk authorities to consolidate efforts and avoid fragmented approaches to risk identification:

- [MIT AI Risk Repository](https://airisk.mit.edu/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/risk-management-framework)

We encourage community members to report new GenAI data security vulnerabilities and risks to these partnered organizations as well as to this initiative.

---

## How to Contribute

- **Slack:** Join `#team-genai-data-security-initiative` on the [OWASP Slack workspace](https://owasp.slack.com)
- **Contact:** Reach out to Emmanuel Guilherme Junior (Initiative Lead) via [Slack](https://owasp.slack.com) or [LinkedIn](https://www.linkedin.com/in/emmanuelgjr/)
- **GitHub:** Submit issues or pull requests to this repository
- **Data Submissions:** Contribute vulnerability data, incident reports, or framework mappings through the channels above
- **New to OWASP Slack?** [Join the workspace here](https://owasp.org/slack/invite)

All contributions are welcome — from security practitioners, AI engineers, researchers, compliance professionals, and anyone working to secure GenAI systems.

---

## OWASP GenAI Security Project — Initiatives

This initiative is one of several under the [OWASP GenAI Security Project](https://genai.owasp.org/). The full list of project initiatives:

| Initiative | Description | Link |
|---|---|---|
| **Agentic App Security** | Securing autonomous and agentic AI systems, including the Top 10 for Agentic Applications 2026 | [Initiative Page](https://genai.owasp.org/initiatives/agentic-security-initiative/) |
| **AI Red Teaming & Evaluation** | Standardized methodology, benchmarks, and tools for adversarial testing of GenAI systems | [Initiative Page](https://genai.owasp.org/initiatives/#ai-redteaming) |
| **AI Security Solutions Landscape** | Vendor-agnostic mapping of the GenAI security tooling ecosystem across the full lifecycle | [Solutions Directory](https://genai.owasp.org/ai-security-solutions-landscape/) |
| **AIBOM Generator** | Open-source tool for generating AI Bills of Materials for supply chain transparency | [Initiative Page](https://genai.owasp.org/ai-sbom-initiative/) |
| **Data Security** | GenAI data security risks, mitigations, best practices, and framework mappings *(this initiative)* | [Initiative Page](https://genai.owasp.org/initiative/data-security/) |
| **Governance Checklist (COMPASS)** | Cybersecurity and governance checklist for LLM and GenAI deployments | [Resource Page](https://genai.owasp.org/resource/llm-applications-cybersecurity-and-governance-checklist-english/) |
| **Secure AI Adoption** | Center of Excellence guidance for safe, ethical, and secure organizational AI adoption | [Initiative Page](https://genai.owasp.org/initiatives/#secure-ai-adoption) |
| **Threat Intelligence** | Research into LLM-enabled exploit generation and deepfake threat preparation | [Initiative Page](https://genai.owasp.org/initiatives/#ai-threat-intel) |

---

## Acknowledgments

**Initiative Lead:** [Emmanuel Guilherme Junior](https://www.linkedin.com/in/emmanuelgjr/)

**2026 Risks and Mitigations — Authors:** Scott Clinton (Board Co-chair, OWASP GenAI Co-founder), Kyriakos "Rock" Lambros (Director of AI Standards and Governance, Zenity), Emmanuel Guilherme Junior (Data Security Initiative Lead)

This initiative is made possible by the contributions of dozens of authors, contributors, and reviewers from across the global AI security community. Full contributor lists are included in each published document.

For information on OWASP GenAI Security Project sponsorship, visit the [Sponsorship page](https://genai.owasp.org/sponsorship/).

---

## License

All materials produced by this initiative are licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

You are free to share and adapt the material for any purpose, including commercial, under the following terms: provide appropriate attribution including the project name and asset name, and distribute any derivative works under the same license.
