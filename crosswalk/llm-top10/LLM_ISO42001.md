<!--
  GenAI Security Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : ISO/IEC 42001:2023 — Artificial Intelligence Management System
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × ISO/IEC 42001:2023

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) —
the international standard for Artificial Intelligence Management Systems (AIMS),
published December 2023.

---

## Why ISO 42001 for LLM security

ISO/IEC 42001 is the AI-specific management system standard — the
AI equivalent of ISO 27001 for information security. Where ISO 27001
asks "how do you manage information security risk?", ISO 42001 asks
"how do you manage AI risk?" — covering the full AI system lifecycle
from design through deployment through decommission.

Three properties make ISO 42001 the right governance framework for
LLM security programmes:

**AI-specific risk framework:** ISO 42001 Clause 6 (Planning) and
Annex A explicitly address AI risk categories that ISO 27001 does
not — data quality, model performance, AI system objectives, and
impacts on persons affected by AI outputs. LLM security risks map
directly to these AI-specific risk categories.

**Lifecycle coverage:** ISO 42001 Clause 8 (Operation) covers the
full AI system lifecycle — acquisition, development, testing, deployment,
monitoring, and decommissioning. Every phase of the LLM lifecycle has
associated security controls in the standard.

**Third-party and supply chain:** ISO 42001 Annex A control A.6
(AI system operation and monitoring) and A.10 (third-party and
customer relationships) explicitly address AI vendor management —
model providers, dataset suppliers, and plugin ecosystems are in scope.

**Relationship to ISO 27001:** ISO 42001 is designed to be used
alongside ISO 27001 — they share the same high-level structure (HLS)
and are intended to be integrated in a combined management system.
Organisations with ISO 27001 certification should extend their ISMS
with an AIMS under ISO 42001 for AI deployments.

---

## ISO 42001:2023 structure

| Clause | Title | LLM security relevance |
|---|---|---|
| 4 | Context of the organisation | AI system scope, interested parties, regulatory context |
| 5 | Leadership | AI governance, policy, roles and responsibilities |
| 6 | Planning | AI risk assessment, AI objectives, change planning |
| 7 | Support | Resources, competence, awareness, communication, documented information |
| 8 | Operation | AI system lifecycle — acquisition, development, testing, deployment |
| 9 | Performance evaluation | Monitoring, measurement, internal audit, management review |
| 10 | Improvement | Nonconformity, corrective action, continual improvement |

**Annex A — AI controls reference:**

| Section | Title | LLM relevance |
|---|---|---|
| A.2 | Policies related to AI | Acceptable use, data governance, AI ethics policy |
| A.3 | Internal organisation | Roles, accountability, training |
| A.4 | Resources for AI systems | Data, compute, human expertise |
| A.5 | Assessing impacts of AI systems | Impact assessment, stakeholder consultation |
| A.6 | AI system lifecycle | Design, development, testing, deployment, monitoring |
| A.7 | Data for AI systems | Data governance, quality, provenance |
| A.8 | Information for interested parties | Transparency, disclosure |
| A.9 | Use of AI systems | Acceptable use, user guidance |
| A.10 | Third-party and customer relationships | Vendor management, customer obligations |

---

## Quick-reference summary

| ID | Name | Severity | Primary ISO 42001 Controls | Tier |
|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | A.6.2.3, A.6.2.6, A.6.2.8, Cl.6.1 | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | A.7.2, A.7.3, A.6.2.3, A.5.2 | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | A.10.1, A.10.2, A.6.1.2, A.7.2 | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | Critical | A.7.2, A.7.3, A.6.2.3, A.6.2.6 | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | A.6.2.3, A.6.2.6, A.9.1, Cl.8 | Foundational–Hardening |
| LLM06 | Excessive Agency | High | A.6.1.2, A.6.2.3, A.5.2, Cl.5 | Foundational–Hardening |
| LLM07 | System Prompt Leakage | High | A.7.3, A.6.2.3, A.8.1, Cl.7 | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | A.7.2, A.7.3, A.6.2.6, A.10.1 | Hardening–Advanced |
| LLM09 | Misinformation | Medium | A.5.2, A.6.2.8, A.8.1, A.9.1 | Foundational–Hardening |
| LLM10 | Unbounded Consumption | Medium | A.6.2.3, A.6.2.8, Cl.6.1, Cl.9 | Foundational–Hardening |

---

## Audience tags

- **CISO / governance** — full file, ISO 42001 AIMS integration for LLM programme
- **AI governance lead** — Annex A control mapping, management review evidence
- **Auditor / certifier** — clause and control mapping for ISO 42001 certification audits
- **Security engineer** — A.6, A.7 lifecycle and data controls
- **Compliance officer** — A.5, A.8, A.10 policy and third-party entries
- **OT engineer** — LLM01, LLM04, LLM10 with ISA 62443 crosswalk

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions in user input or processed content manipulate
LLM behaviour. ISO 42001 addresses this through AI system design
controls (A.6.2.3), security testing (A.6.2.6), and the broader
AI risk management process (Clause 6.1).

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| AI system security | A.6.2.3 | AI systems designed with security controls — input validation, context separation, injection detection as AIMS design requirements |
| Testing of AI systems | A.6.2.6 | AI systems tested before deployment — adversarial testing for prompt injection as AIMS testing requirement |
| Monitoring of AI systems | A.6.2.8 | AI systems monitored in operation — runtime injection detection as AIMS monitoring control |
| Risk assessment | Cl.6.1 | Prompt injection included in AI risk assessment — risk owner, treatment, review cadence documented |

#### Mitigations for ISO 42001 alignment

**Foundational**
- Cl.6.1: Include prompt injection in AI risk assessment —
  document specific injection paths per deployment, risk
  owner, treatment controls, and review cadence in AIMS
  risk register
- A.6.2.3: Establish AI system security requirements in
  the design phase — input validation and context
  separation as AIMS design controls documented before
  development begins
- Treat all external content as untrusted at the AIMS
  policy level — document in A.2 AI policy

**Hardening**
- A.6.2.6: Include prompt injection scenarios in AIMS
  testing programme — direct, indirect via RAG, and
  jailbreak vectors tested before each production release,
  results documented as AIMS evidence
- A.6.2.8: Implement runtime injection monitoring as
  AIMS operational control — alerts integrated into
  AIMS incident management workflow
- Document injection controls in AIMS documented
  information per Clause 7.5

**Advanced**
- A.6.2.6: Extend adversarial testing to cover your
  specific indirect injection surfaces — RAG sources,
  tool descriptors, processed documents tested before
  each deployment, results in AIMS audit trail
- Cl.9: Include injection control effectiveness in AIMS
  management review — trend data, incident rates, control
  improvements reviewed at defined intervals

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISO 27001 A.8.28 · NIST CSF 2.0 PR.PS-04 · NIST AI RMF MS-2.5

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs expose PII, financial data, or confidential information through
outputs. ISO 42001 Annex A.7 (Data for AI systems) is the primary
control section — data governance is a first-class AIMS concern.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Data quality | A.7.2 | Training data and RAG content quality requirements — sensitivity, completeness, appropriateness assessed before use |
| Data provenance and characteristics | A.7.3 | Data provenance documented — source, classification, handling requirements tracked from ingestion through all derived forms |
| AI system security | A.6.2.3 | Output scanning and redaction as AIMS security controls — DLP enforced at the system boundary |
| Impact assessment | A.5.2 | Impact assessment covers data disclosure risk — what data is in LLM scope, what is the disclosure impact per stakeholder |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.7.2: Establish data quality criteria for all data
  entering LLM scope — sensitivity classification,
  appropriateness for AI use, handling requirements
  documented in AIMS
- A.7.3: Document provenance for all training data and
  RAG sources — source, classification, consent basis,
  handling obligations tracked per dataset
- A.5.2: Include sensitive data disclosure in AI impact
  assessment — identify affected stakeholders, assess
  disclosure impact severity

**Hardening**
- A.6.2.3: Implement output redaction as AIMS security
  control — PII and sensitive patterns masked before
  responses leave the LLM service boundary, documented
  as AIMS operational control
- A.7.3: Extend provenance tracking to derived assets —
  embeddings and caches inherit source classification,
  propagation documented in AIMS
- Cl.9: Monitor data leakage incidents in AIMS —
  incident rates, affected data categories reported in
  management review

**Advanced**
- Apply differential privacy for LLM trained on sensitive
  data — document privacy budget as A.7.2 data quality
  control in AIMS
- Conduct model inversion red team as A.6.2.6 testing
  activity — validate sensitive training data cannot be
  reconstructed, results in AIMS test records

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.8.11/A.8.12 · NIST AI RMF GV-1.6 · EU AI Act Art. 10

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, datasets,
libraries, and plugins. ISO 42001 Annex A.10 (Third-party and
customer relationships) is the primary control section.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Third-party AI system acquisition | A.10.1 | Security requirements applied to all LLM component vendors — model providers, dataset suppliers, inference runtime vendors |
| Customer relationships | A.10.2 | LLM deployment obligations to downstream customers — what security properties are guaranteed |
| Responsible AI system management | A.6.1.2 | LLM components managed responsibly through lifecycle — acquisition, testing, deployment, decommission |
| Data quality | A.7.2 | Third-party training datasets assessed for quality — provenance, completeness, representativeness, security |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.10.1: Establish AIMS third-party requirements for
  all LLM component vendors — security obligations,
  provenance documentation, vulnerability disclosure
  requirements documented before any component enters
  production
- A.7.2: Apply data quality criteria to all third-party
  training datasets — provenance, appropriateness, and
  security assessed as AIMS requirements
- Maintain ML SBOM as AIMS documented information
  per Clause 7.5 — every component inventoried with
  version, source, hash

**Hardening**
- A.10.1: Include security requirements in contracts
  with all LLM component vendors — provenance,
  integrity guarantees, incident notification SLA
  as AIMS contractual controls
- A.6.2.6: Test all components before deployment in
  AIMS testing programme — signature verification,
  backdoor scanning, behavioural baseline
- Cl.9: Include third-party component incidents in
  AIMS performance monitoring — supply chain risk
  trends in management review

**Advanced**
- A.10.1: Conduct periodic security assessments of
  strategic LLM component suppliers — include in
  AIMS third-party review programme with defined cadence
- Operate isolated component evaluation environment
  as A.6.2.6 testing control — document as AIMS evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST CSF 2.0 GV.SC-01 · ISO 27001 A.5.19/A.5.21 · NIST SP 800-218A

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Adversaries corrupt training data or model weights. ISO 42001 A.7
(Data for AI systems) and A.6.2.6 (Testing) are the primary controls —
data integrity is an AIMS first-class concern.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Data quality | A.7.2 | Training data quality requirements include integrity — anomaly detection, source allowlisting, provenance tracking as data quality controls |
| Data provenance and characteristics | A.7.3 | Training data provenance documented — full chain from source to training dataset, modification history tracked |
| AI system security | A.6.2.3 | Training pipeline integrity controls — input validation, source allowlisting as AIMS security design requirements |
| Testing of AI systems | A.6.2.6 | Poisoning detection in AIMS testing — backdoor trigger testing, biased output detection before each production promotion |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.7.2: Establish data quality requirements covering
  integrity for all training data — source allowlisting,
  anomaly detection, statistical validation documented
  as AIMS data quality controls
- A.7.3: Document complete provenance for all training
  data — source, preprocessing steps, quality checks,
  approval chain in AIMS documented information
- Model rollback capability documented as A.6.1.2
  responsible management control — clean checkpoint
  always available

**Hardening**
- A.6.2.6: Include poisoning detection in AIMS testing
  programme — backdoor trigger testing and output
  distribution analysis before every production model
  promotion, results as AIMS test evidence
- A.6.2.8: Monitor production models for poisoning
  indicators — systematic recommendation drift alerted
  as AIMS operational monitoring control
- A.10.1: Apply integrity requirements to training
  data source vendors — provenance attestation in
  vendor contracts as A.10 third-party control

**Advanced**
- Post-training backdoor detection as mandatory AIMS
  deployment gate per A.6.2.6 — neural cleanse or
  equivalent, results in AIMS documented information
- Cl.9: Include poisoning incidents in AIMS management
  review — trend data, affected deployments, control
  improvements

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0032 · ISO 27001 A.8.27

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM output passed to downstream systems without validation enables
injection attacks. ISO 42001 A.6.2.3 (security) and Clause 8
(operation) address output handling as a system design concern.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| AI system security | A.6.2.3 | Output encoding and schema validation as AIMS security design requirements — LLM output treated as untrusted input to downstream systems |
| Testing of AI systems | A.6.2.6 | Output injection scenarios in AIMS testing — XSS, SQL injection, command injection via LLM output tested before deployment |
| Use of AI systems | A.9.1 | Guidance on AI system use — downstream consumers informed that LLM output must be validated before use |
| Operation | Cl.8 | Operational controls for LLM deployment — output handling requirements documented as AIMS operational procedures |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.6.2.3: Document output encoding and schema validation
  as AIMS security design requirements — LLM output
  treated as untrusted input at all downstream interfaces
- A.9.1: Communicate output handling requirements to
  all downstream consumers — validation obligations
  documented in AIMS user guidance
- Never pass raw LLM output to database queries, shell
  commands, or eval functions — AIMS policy control

**Hardening**
- A.6.2.6: Include output injection in AIMS testing —
  XSS, SQL injection, command injection via model output
  tested against all interfaces consuming LLM responses
- Cl.8: Document output validation as AIMS operational
  control — procedures, responsible parties, verification
  cadence in AIMS documented information

**Advanced**
- Cl.9: Monitor output injection incidents in AIMS
  performance evaluation — incident trends reported
  in management review, controls improved based on data

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Semgrep | Open-source | https://semgrep.dev |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: OWASP ASVS V5 · NIST CSF 2.0 PR.PS-04 · CWE-79

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs with excessive autonomy execute unintended or harmful actions.
ISO 42001 A.6.1.2 (responsible AI system management) and Clause 5
(leadership) address autonomy scope as a governance responsibility.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Responsible AI system management | A.6.1.2 | LLM tool access managed responsibly — minimum permissions, human oversight requirements documented as AIMS responsibilities |
| AI system security | A.6.2.3 | Tool permission enforcement as AIMS security control — scope enforced at orchestration layer |
| Impact assessment | A.5.2 | Impact assessment covers excessive agency risk — what actions can the LLM take autonomously, what is the worst-case impact |
| Policy | Cl.5 | Leadership commitment to human oversight — autonomous action scope defined in AI policy, signed off at executive level |

#### Mitigations for ISO 42001 alignment

**Foundational**
- Cl.5: Establish AI policy defining acceptable
  autonomous action scope — which actions require human
  confirmation documented at executive level as AIMS
  leadership commitment
- A.6.1.2: Manage LLM tool access as responsible AI
  management obligation — minimum permissions, regular
  review, human confirmation for irreversible actions
- A.5.2: Include excessive agency in AI impact assessment —
  what autonomous actions are possible, what is the
  consequence if each goes wrong

**Hardening**
- A.6.2.3: Implement tool permission enforcement as
  AIMS security control — scope enforced at orchestration
  layer independent of model instruction
- A.6.2.6: Include excessive agency scenarios in AIMS
  testing — indirect injection leading to autonomous
  tool invocation, results as AIMS test evidence
- Cl.9: Log and monitor all LLM tool invocations —
  anomalous scope detected, AIMS performance evaluation
  covers autonomous action incidents

**Advanced**
- A.5.2: Formal impact assessment before each
  autonomous capability expansion — AIMS documented
  information requirement before increasing agent scope
- Cl.9: Include excessive agency incidents in AIMS
  management review — trend data drives policy updates

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: EU AI Act Art. 14 · AIUC-1 B006 · NIST CSF 2.0 GV.OC-01

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing security controls are extracted by
adversaries. ISO 42001 A.7.3 (data provenance) and Clause 7
(documented information) govern system prompt protection.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Data provenance and characteristics | A.7.3 | System prompts classified as sensitive operational data — provenance, access controls, handling requirements documented |
| AI system security | A.6.2.3 | System prompt encryption and access controls as AIMS security design requirements |
| Information for interested parties | A.8.1 | Transparency obligations balanced with operational security — what must be disclosed vs what may be kept confidential |
| Support | Cl.7 | Documented information controls — system prompts managed as AIMS documented information with appropriate access controls |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.7.3: Classify system prompts as sensitive operational
  data in AIMS — document handling requirements, access
  controls, and storage standards
- Cl.7: Manage system prompts as AIMS documented
  information — version control, access restrictions,
  retention and disposal documented
- A.6.2.3: Encrypt system prompts at rest — AIMS
  security design requirement, not stored in cleartext

**Hardening**
- A.6.2.6: Include prompt extraction testing in AIMS
  testing programme — verify resistance to known
  extraction techniques before deployment
- A.8.1: Balance transparency obligations with
  operational security — what must be disclosed under
  EU AI Act or applicable regulation vs what is
  legitimately confidential operational configuration

**Advanced**
- Implement system prompt tokenisation — sensitive
  identifiers replaced with opaque tokens as A.6.2.3
  security design control
- Cl.9: Include extraction incidents in AIMS
  performance monitoring — trend data in management review

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003/B009 · ISO 27001 A.5.12 · CWE-200

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Vector stores are susceptible to adversarial retrieval and inference
attacks. ISO 42001 A.7 (Data for AI systems) governs embedding
stores as AI data assets.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Data quality | A.7.2 | Vector store content quality requirements — RBAC, encryption, source validation as data quality controls |
| Data provenance and characteristics | A.7.3 | Embedding provenance documented — source document, classification, access controls tracked |
| Testing of AI systems | A.6.2.6 | Vector store attacks in AIMS testing — RBAC bypass, embedding inversion, bulk extraction tested |
| Third-party AI system acquisition | A.10.1 | Vector database providers assessed as third-party AI system components |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.7.2: Establish data quality requirements for vector
  stores — RBAC enabled, encryption at rest, content
  validation before ingestion documented as AIMS controls
- A.7.3: Track embedding provenance — source document,
  classification, access controls as AIMS documented
  information
- Patch all vector database CVEs — AIMS vulnerability
  management obligation under A.6.2.3

**Hardening**
- A.6.2.6: Include vector store attacks in AIMS testing —
  RBAC bypass, path traversal, embedding inversion
  results as AIMS test evidence
- A.10.1: Assess vector database providers as third-party
  AI system components — security obligations in vendor
  contracts

**Advanced**
- Apply differential privacy in embedding generation —
  document privacy budget as A.7.2 data quality control
- Conduct embedding inversion red team as A.6.2.6
  testing activity — validate source content cannot
  be reconstructed

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://weaviate.io |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference & Data Reconstruction
- Other frameworks: NIST AI RMF MS-2.5 · NIST CSF 2.0 PR.DS-01 · CWE-284

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but incorrect content. ISO 42001 A.5.2
(impact assessment) and A.8.1 (information for interested parties)
address misinformation as both an impact and a transparency concern.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| Impact assessment | A.5.2 | AI impact assessment covers misinformation risk — which domains are affected, what is the consequence of incorrect output per stakeholder |
| Monitoring of AI systems | A.6.2.8 | Production monitoring for accuracy degradation — hallucination rates tracked as AIMS operational monitoring |
| Information for interested parties | A.8.1 | Transparency about AI system limitations — users informed of advisory status, accuracy limitations, verification requirements |
| Use of AI systems | A.9.1 | Guidance on appropriate AI system use — domains requiring human verification documented as AIMS use guidance |

#### Mitigations for ISO 42001 alignment

**Foundational**
- A.5.2: Include misinformation in AI impact assessment —
  which decisions are influenced by LLM output, what is
  the consequence of incorrect recommendations per
  stakeholder group, documented in AIMS
- A.8.1: Communicate AI system limitations to users —
  advisory status, accuracy limitations, verification
  requirements disclosed as AIMS transparency obligation
- A.9.1: Document appropriate use guidance — domains
  requiring human verification before action

**Hardening**
- A.6.2.8: Implement production accuracy monitoring as
  AIMS operational control — hallucination rates per
  domain tracked, degradation alerted
- Cl.9: Include accuracy metrics in AIMS performance
  evaluation — management review covers accuracy trends,
  domain-specific failure rates

**Advanced**
- A.6.2.6: Domain-specific accuracy testing before
  deployment — AIMS testing programme covers accuracy
  against defined thresholds per use case
- Cl.10: Corrective action process for misinformation
  incidents — root cause, corrective control, effectiveness
  verification documented in AIMS

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · AIUC-1 F · NIST CSF 2.0 GV.OC-01

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Adversarial inputs trigger disproportionate resource consumption.
ISO 42001 Clause 6.1 (risk assessment) and Clause 9 (performance
evaluation) address resource risk as an operational AI management concern.

#### ISO 42001:2023 mapping

| Control | ID | How it applies |
|---|---|---|
| AI system security | A.6.2.3 | Rate limiting and resource controls as AIMS security design requirements — enforced at deployment |
| Monitoring of AI systems | A.6.2.8 | Resource consumption monitored in operation — cost anomaly detection as AIMS monitoring control |
| Risk assessment | Cl.6.1 | Consumption risk in AI risk assessment — impact on service availability, cost exposure documented |
| Performance evaluation | Cl.9 | Resource consumption metrics in AIMS performance evaluation — consumption trends in management review |

#### Mitigations for ISO 42001 alignment

**Foundational**
- Cl.6.1: Include unbounded consumption in AI risk
  assessment — availability impact, cost exposure, DoS
  risk documented with owner and treatment
- A.6.2.3: Implement rate limiting and resource controls
  as AIMS security design requirements — hard token caps,
  per-user budgets enforced at deployment
- A.6.2.8: Monitor resource consumption as AIMS
  operational control — cost anomaly alerts

**Hardening**
- Cl.9: Include resource consumption in AIMS performance
  evaluation — trends, incidents, budget adherence
  reported in management review
- Implement circuit breakers as operational resilience
  control — documented as AIMS operational procedure
  under Clause 8

**Advanced**
- A.6.2.6: Include adversarial load testing in AIMS
  testing programme — sponge example attacks tested
  before production deployment
- Cl.10: Corrective action process for consumption
  incidents — root cause, control improvement documented

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: NIST CSF 2.0 PR.IR-01 · ISA/IEC 62443 SR 7.6 (OT) · CWE-400

---

## ISO 42001 AIMS implementation checklist for LLM applications

### Clause 4 — Context

- [ ] AI system scope defined — all LLM deployments identified
- [ ] Interested parties identified — users, regulators, affected persons
- [ ] Regulatory context assessed — EU AI Act, GDPR, sector regulations applicable to LLM use

### Clause 5 — Leadership

- [ ] AI policy established covering LLM acceptable use (A.2)
- [ ] Roles and responsibilities assigned for LLM governance
- [ ] Executive commitment to human oversight documented

### Clause 6 — Planning

- [ ] AI risk assessment completed per LLM deployment (LLM01–LLM10)
- [ ] AI impact assessment completed per LLM deployment (A.5.2)
- [ ] AI objectives defined — accuracy thresholds, availability requirements

### Clause 7 — Support

- [ ] ML SBOM maintained as AIMS documented information
- [ ] Competence requirements defined for LLM system operators
- [ ] Awareness programme covers LLM risks and acceptable use

### Clause 8 — Operation

- [ ] Third-party requirements applied to LLM component vendors (A.10.1)
- [ ] Data quality criteria applied to training and RAG data (A.7.2)
- [ ] Data provenance tracked for all training sources (A.7.3)
- [ ] Security controls documented in AI system design (A.6.2.3)
- [ ] Testing programme covers all LLM Top 10 adversarial scenarios (A.6.2.6)
- [ ] Operational monitoring live for all LLM deployments (A.6.2.8)
- [ ] Use guidance documented for all LLM applications (A.9.1)
- [ ] Transparency disclosures in place where required (A.8.1)

### Clause 9 — Performance evaluation

- [ ] Monitoring and measurement programme covers LLM Top 10 risks
- [ ] Internal audit programme covers LLM AIMS controls
- [ ] Management review includes LLM security metrics and incidents

### Clause 10 — Improvement

- [ ] Nonconformity process covers LLM security incidents
- [ ] Corrective action records maintained for all LLM incidents

---

## ISO 42001 and ISO 27001 integration guidance

For organisations with existing ISO 27001 certification, ISO 42001
is designed to integrate via the shared High Level Structure (HLS):

| Integration point | Approach |
|---|---|
| Risk assessment | Extend ISO 27001 risk assessment to cover AI-specific risks per Clause 6.1 — same methodology, additional AI risk categories |
| Asset management | Extend ISO 27001 asset inventory to ML SBOM and AI data assets — same register, AI-specific asset types |
| Supplier management | Extend ISO 27001 supplier controls to LLM vendors — same programme, AI-specific requirements per A.10.1 |
| Incident management | Extend ISO 27001 incident procedure to AI incidents — same workflow, AI-specific categories and response steps |
| Documented information | AIMS documented information managed within ISO 27001 document control — same system, AI-specific document types |

A combined ISO 27001 + ISO 42001 management system is the recommended
target state for enterprise LLM deployments — ISO 27001 covers the
information security foundation, ISO 42001 adds the AI-specific layer.

---

## References

- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)
- [ISO/IEC 42001 — Overview](https://www.iso.org/obp/ui/#iso:std:iso-iec:42001:ed-1:v1:en)
- [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries with AIMS implementation checklist and ISO 27001 integration guidance | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the GenAI Security Crosswalk: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk
