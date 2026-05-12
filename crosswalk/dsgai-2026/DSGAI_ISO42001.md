<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks & Mitigations 2026 (DSGAI01-DSGAI21)
  Framework   : ISO/IEC 42001:2023 — Artificial Intelligence Management System
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 — ISO/IEC 42001:2023

Mapping the [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) —
the international standard for Artificial Intelligence Management Systems (AIMS).

---

## Why ISO 42001 for DSGAI data security

ISO/IEC 42001 is the AI-specific management system standard — the
AI equivalent of ISO 27001 for information security. For
organisations managing GenAI data security, ISO 42001 provides
the governance and lifecycle framework that ISO 27001 alone
cannot:

**AI-specific data governance:** ISO 42001 Annex A control A.7
(Data for AI Systems) explicitly addresses training data quality,
provenance, and governance — the direct responsibility domain
of the DSGAI 2026 risks. ISO 27001 has no equivalent clause
for training data, embedding stores, or inference data pipelines.

**Lifecycle coverage for data:** ISO 42001 Clause 8 covers the
full AI system lifecycle — acquisition, development, testing,
deployment, monitoring, and decommissioning. Each DSGAI risk
maps to one or more lifecycle phases where data security controls
must be applied.

**Impact assessment for data risks:** ISO 42001 Annex A control
A.5 (Assessing Impacts of AI Systems) requires organisations
to assess the impacts of their AI deployments on affected
persons — directly applicable to DSGAI risks involving PII
leakage, disinformation, and inference attacks.

**Integration with ISO 27001:** ISO 42001 shares the High-Level
Structure (HLS) with ISO 27001 and is designed for integrated
deployment. Organisations with ISO 27001 certification should
extend their ISMS with an AIMS for GenAI data security using
ISO 42001 as the framework.

---

## ISO 42001:2023 structure

| Clause | Title | DSGAI relevance |
|---|---|---|
| 4 | Context of the organisation | AI system scope, regulatory context, interested parties for data security |
| 5 | Leadership | AI governance, data security policy, roles and accountability |
| 6 | Planning | AI risk assessment, data security objectives, change management |
| 7 | Support | Resources, competence, awareness, documented data governance |
| 8 | Operation | AI data lifecycle — ingestion, training, deployment, decommissioning |
| 9 | Performance evaluation | Data quality monitoring, internal audit, management review |
| 10 | Improvement | Nonconformity, corrective action, continual improvement |

**Annex A — AI controls reference:**

| Section | Title | DSGAI relevance |
|---|---|---|
| A.2 | Policies related to AI | Data governance policy, acceptable use, AI ethics |
| A.3 | Internal organisation | Roles, accountability, training for data security |
| A.4 | Resources for AI systems | Data assets, compute, expertise |
| A.5 | Assessing impacts of AI systems | Privacy impact, data subject rights, disclosure risks |
| A.6 | AI system lifecycle | Design, development, testing, deployment data controls |
| A.7 | Data for AI systems | Training data governance, quality, provenance, privacy |
| A.8 | Information for interested parties | Transparency, disclosure, user information |
| A.9 | Use of AI systems | Acceptable use, user guidance, data handling |
| A.10 | Third-party and customer relationships | Vendor management, data processor obligations |

---

## Quick-reference summary

| ID | Name | Severity | Primary ISO 42001 Controls | Tier | Scope |
|---|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | A.7.2, A.7.3, A.6.2.3, A.5.2 | Foundational–Advanced | Both |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | A.6.2.3, A.6.1.2, A.3.3, Cl.5 | Foundational–Advanced | Both |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | A.2.2, A.9.1, A.10.1, Cl.4 | Foundational–Hardening | Both |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | A.7.2, A.7.3, A.6.2.6, A.6.1.2 | Hardening–Advanced | Both |
| DSGAI05 | Data Integrity & Validation Failures | High | A.7.2, A.7.3, A.6.2.3, Cl.8 | Foundational–Hardening | Build |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | A.10.1, A.10.2, A.6.1.2, A.7.2 | Foundational–Hardening | Both |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | A.7.2, A.7.3, A.2.2, Cl.6.1 | Foundational–Advanced | Both |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | A.2.2, A.8.1, Cl.4.2, Cl.6.1 | Foundational–Advanced | Both |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | A.7.2, A.6.2.3, A.5.2, Cl.8 | Hardening–Advanced | Both |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | A.7.2, A.5.2, A.7.3, Cl.6.1 | Hardening–Advanced | Build |
| DSGAI11 | Cross-Context Conversation Bleed | High | A.7.2, A.6.2.3, A.6.2.6, Cl.8 | Foundational–Hardening | Build |
| DSGAI12 | Unsafe NL Data Gateways | Critical | A.6.2.3, A.6.2.6, A.7.2, A.9.1 | Foundational–Advanced | Build |
| DSGAI13 | Vector Store Platform Security | High | A.7.2, A.7.3, A.6.1.2, A.10.1 | Foundational–Hardening | Both |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | A.7.2, A.2.2, A.6.2.6, Cl.9 | Foundational–Hardening | Build |
| DSGAI15 | Over-Broad Context Windows | High | A.7.2, A.6.2.3, A.5.2, Cl.8 | Foundational–Hardening | Build |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | A.9.1, A.6.1.2, A.2.2, Cl.4 | Foundational–Hardening | Both |
| DSGAI17 | Data Availability & Resilience Failures | High | A.6.2.8, A.6.2.6, Cl.8, Cl.10 | Foundational–Advanced | Both |
| DSGAI18 | Inference & Data Reconstruction | High | A.7.2, A.5.2, A.6.2.6, Cl.6.1 | Hardening–Advanced | Both |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | A.7.2, A.10.1, A.3.3, Cl.7 | Foundational–Hardening | Both |
| DSGAI20 | Model Exfiltration & IP Replication | High | A.7.3, A.6.1.2, A.6.2.6, Cl.6.1 | Hardening–Advanced | Both |
| DSGAI21 | Disinformation via Data Poisoning | High | A.7.2, A.7.3, A.5.2, A.8.1 | Hardening–Advanced | Both |

---

## Audience tags

- **AI governance / AIMS programme lead** — full file, ISO 42001 AIMS implementation for GenAI data security
- **ISO 27001 ISMS manager** — Annex A integration guidance, ISMS extension controls
- **Data governance officer** — A.7 data controls per DSGAI entry
- **Privacy / DPO** — A.5 impact assessment entries, GDPR Article 30 intersection
- **ML / AI engineer** — Clause 8 lifecycle controls, A.7 data quality entries
- **Vendor risk manager** — A.10 third-party control entries
- **Auditor** — documented evidence requirements per control

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

Sensitive data leaks from GenAI systems through model outputs,
RAG retrieval, embedding exposure, or observability pipelines.
ISO 42001 A.7 (Data for AI Systems) is the primary domain —
covering all data lifecycle stages from acquisition through
use through disposal for data in the AI system scope.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data for AI — acquisition | All training data and RAG corpora acquired with documented classification, purpose, and provenance | L1 | Foundational |
| A.7.3 | Data for AI — preparation | PII and sensitive data removed or masked in training data preparation; residual risk documented | L2 | Hardening |
| A.6.2.3 | Lifecycle — operational | Operational controls on AI data access — retrieval scope enforcement, output scanning | L2 | Foundational |
| A.5.2 | Impact assessment | Privacy impact assessment covering sensitive data disclosure risks — GDPR Article 35 DPIA where required | L2 | Hardening |

#### Mitigations by tier

**Foundational**
- A.7.2: Establish data acquisition policy for all
  GenAI data assets — classification, purpose limitation,
  provenance documentation required before data enters
  AI system scope
- A.6.2.3: Implement retrieval scope enforcement —
  RAG queries bounded to user's document permission
  level as an AIMS operational control

**Hardening**
- A.7.3: Apply PII scrubbing to training data
  preparation pipeline — sensitive data identified,
  masked, or removed before model training
- A.5.2: Conduct privacy impact assessment covering
  sensitive data disclosure risk per GenAI deployment —
  DPIA where processing is high risk under GDPR

**Advanced**
- A.7.3: Apply differential privacy for sensitive
  training corpora — formal privacy-preserving technique
  documented as A.7.3 evidence
- A.5.2: Conduct model inversion red team as part of
  impact assessment — quantify data reconstruction risk

#### EU AI Act alignment

ISO 42001 A.7.2 and A.7.3 provide the technical framework
for EU AI Act Article 10 data governance compliance. Annex
A A.5.2 supports Article 9 risk management obligations.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MS-2.6), DSGAI_ENISA.md (DMS L2)

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical

AI agents inherit and cache credentials that attackers exploit
for lateral movement. ISO 42001 addresses this through A.6
lifecycle controls for agent design and A.3.3 roles and
responsibilities for credential ownership and policy.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.6.2.3 | Lifecycle — operational | Agent credential scope defined and enforced as AI system operational control | L2 | Foundational |
| A.6.1.2 | Lifecycle — design | Minimal privilege design principle applied at AI system design stage | L1 | Foundational |
| A.3.3 | Internal organisation — roles | Credential ownership and rotation responsibility assigned to named role | L1 | Foundational |
| Cl.5 | Leadership | Accountability for agent identity management established at governance level | L1 | Foundational |

#### Mitigations by tier

**Foundational**
- A.6.1.2: Apply minimal privilege at AI system
  design stage — document required credential scope
  per agent role before development begins
- A.3.3: Assign named accountability for agent
  credential lifecycle management — rotation, revocation,
  and audit trail ownership documented

**Hardening**
- A.6.2.3: Implement session-scoped credentials —
  agent credentials expire at session end, scope
  limited to current task, documented as operational control
- Cl.5: Establish AI credential management policy
  at governance level — all agent identity assets
  subject to AIMS policy, audit scope includes
  agent credentials

**Advanced**
- A.6.2.3: Implement per-task ephemeral credentials —
  each agent task receives a fresh, scoped credential
  as an advanced AIMS operational control
- A.6.2.6: Red team agent credential extraction paths —
  test as part of AI system verification activities

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://github.com/hashicorp/vault |
| AWS Secrets Manager | Commercial | https://aws.amazon.com/secrets-manager/ |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI frameworks: DSGAI_NISTAIRMF.md (GV-1.6), DSGAI_CISControls.md (CIS 5)

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High

Employees use unapproved AI tools creating unsanctioned data
flows outside the governance perimeter. ISO 42001 Clause 4
(Context) requires organisations to identify all AI systems
in scope, and A.2.2 requires an AI acceptable use policy
that covers all AI system use within the organisation.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.2.2 | Policies — acceptable use | AI acceptable use policy published, covering all GenAI services; approval process defined | L1 | Foundational |
| A.9.1 | Use of AI systems | Guidance to users on permitted AI use; responsibilities for approved service use documented | L1 | Foundational |
| A.10.1 | Third-party relationships | All AI service providers approved before use; security assessment and DPA required | L2 | Hardening |
| Cl.4 | Context | All AI systems in organisation scope identified and registered in AIMS scope document | L1 | Foundational |

#### Mitigations by tier

**Foundational**
- Cl.4: Define AIMS scope to cover all AI systems
  in use — inventory all approved AI services as part
  of context-setting activities
- A.2.2: Publish AI acceptable use policy — all
  GenAI service use requires prior authorisation under
  the AIMS policy; unapproved use is a policy violation
- A.9.1: Communicate AI use policy to all users —
  training on approved services, restrictions, and
  reporting obligations for suspected policy violations

**Hardening**
- A.10.1: Implement third-party AI service approval
  process — security assessment, DPA, sub-processor
  review before any AI service is approved
- A.2.2: Establish AI asset register — all approved
  services registered with business owner, data
  classification, and vendor risk status

**Advanced**
- A.10.1: Conduct periodic approved AI service audits —
  verify controls are operating as assessed; remove
  services that no longer meet approval criteria
- Deploy network-level detection for unsanctioned
  AI service traffic as technical compensating control

#### Tools

| Tool | Type | Link |
|---|---|---|
| Netskope CASB | Commercial | https://www.netskope.com |
| Microsoft Defender for Cloud Apps | Commercial | https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-cloud-apps |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI frameworks: DSGAI_NISTAIRMF.md (GV-1.7), DSGAI_EUAIAct.md (Art. 9)

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical

Attackers corrupt training data, model weights, or fine-tuning
corpora. ISO 42001 A.7.2 and A.7.3 are the primary controls —
covering data acquisition security, quality, and preparation
integrity throughout the AI data lifecycle.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — acquisition | All training data sourced with provenance documentation; integrity verification before ingestion | L2 | Hardening |
| A.7.3 | Data — preparation | Data preparation pipeline includes quality gates, anomaly detection, and statistical validation | L2 | Hardening |
| A.6.2.6 | Lifecycle — testing | Adversarial testing of deployed models for backdoor behaviour as part of AI system verification | L2 | Hardening |
| A.6.1.2 | Lifecycle — design | Data pipeline integrity controls designed in at the system design stage | L1 | Foundational |

#### Mitigations by tier

**Foundational**
- A.6.1.2: Design data pipeline integrity controls
  at system design stage — do not add data validation
  as an afterthought; integrity requirements documented
  in AI system design specification

**Hardening**
- A.7.2: Require provenance documentation for all
  training corpora — source, version, integrity hash,
  and quality review documented before ingestion
- A.7.3: Deploy data quality gates at each pipeline
  stage — statistical anomaly detection, label
  consistency, and outlier detection before model training
- A.6.2.6: Include adversarial testing for backdoor
  behaviour in AI system testing activities — test
  with trigger patterns before production deployment

**Advanced**
- A.7.3: Apply data sanitisation techniques —
  uncertainty training, activation clustering as
  advanced A.7.3 data preparation controls
- A.6.2.6: Red team poisoning attacks against
  training pipeline — as part of AI system security
  testing under Clause 8 operational activities

#### Tools

| Tool | Type | Link |
|---|---|---|
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| Armory | Open-source | https://github.com/twosixlabs/armory |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MS-3.3), DSGAI_ENISA.md (DMS L2)

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High

GenAI systems ingest data without sufficient validation. ISO 42001
A.7.2 and A.7.3 data governance controls, combined with Clause 8
operational requirements, address data validation as a lifecycle
concern throughout the AI system development and operation phases.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — acquisition | Data quality requirements defined at acquisition stage; schema and format validation documented | L1 | Foundational |
| A.7.3 | Data — preparation | Data validation gates implemented at preparation stage; anomalous data rejected before ingestion | L2 | Hardening |
| A.6.2.3 | Lifecycle — operational | Runtime data validation at all AI system ingestion points as an operational control | L2 | Foundational |
| Cl.8 | Operation | Operational procedures for data pipeline validation documented and followed | L1 | Foundational |

#### Mitigations by tier

**Foundational**
- A.7.2: Define data quality requirements at
  acquisition stage — schema, format, value ranges,
  and content constraints documented before data
  enters AI system scope
- Cl.8: Document operational procedures for data
  pipeline validation — who validates, what is checked,
  what happens on failure

**Hardening**
- A.7.3: Implement data quality gates at each
  preparation stage — automated validation before
  model training or RAG indexing
- A.6.2.3: Deploy runtime data validation at
  all AI system ingestion points — operational
  control documented in AIMS operational procedures

**Advanced**
- A.7.3: Implement data lineage tracking — every
  data record traceable from source to model output,
  quality check results at each stage retained as
  documented information per Clause 7.5
- A.6.2.6: Red team data validation controls —
  test whether adversarially crafted inputs bypass
  validation gates

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |
| Pandera | Open-source | https://github.com/unionai-oss/pandera |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MS-2.5), DSGAI_EUAIAct.md (Art. 10)

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange

**Severity:** High

Data exchanged with external tools, plugins, or sub-agents
is insufficiently secured. ISO 42001 A.10 third-party controls
are the primary domain — tool and plugin vendors are third-party
AI system components subject to vendor management requirements.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.10.1 | Third-party — AI supply chain | All tool and plugin vendors assessed as third-party AI system components before integration | L2 | Hardening |
| A.10.2 | Third-party — customer data | Data handling requirements for tools that process customer or sensitive data documented contractually | L2 | Hardening |
| A.6.1.2 | Lifecycle — design | Tool and plugin integration security requirements specified at design stage | L1 | Foundational |
| A.7.2 | Data — acquisition | Data received from external tools treated with same governance as other AI data assets | L2 | Hardening |

#### Mitigations by tier

**Foundational**
- A.6.1.2: Specify tool and plugin security
  requirements at design stage — integration points
  documented with data classification and trust level
  for each external component

**Hardening**
- A.10.1: Apply AIMS third-party assessment to
  all tool vendors — security assessment, contractual
  security obligations, vulnerability disclosure SLA
- A.10.2: Require data processing agreements for
  tools handling personal or sensitive data — sub-processor
  obligations documented and reviewed
- A.7.2: Treat tool-returned data as externally
  sourced data — same validation and governance
  requirements as other external data ingestion

**Advanced**
- A.10.1: Periodic tool vendor re-assessment —
  security posture reviewed at defined intervals;
  vendors with material changes re-assessed
- A.6.2.6: Red team tool integration points —
  test whether tool responses can influence model
  behaviour or extract sensitive data

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP Dependency-Check | Open-source | https://github.com/jeremylong/DependencyCheck |
| Semgrep | Open-source | https://github.com/returntocorp/semgrep |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse & Exploitation, ASI04 Agentic Supply Chain
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MP-5.1), DSGAI_EUAIAct.md (Art. 9)

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High

GenAI systems lack data classification, lifecycle management,
or governance policies. ISO 42001 A.7 is the dedicated data
governance domain — data classification, lifecycle requirements,
and retention policies are core A.7 controls.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — acquisition | Data classification policy covering all AI data assets — training, RAG, embeddings, outputs | L1 | Foundational |
| A.7.3 | Data — preparation | Data lifecycle controls implemented — retention, archival, deletion, unlearning capability | L2 | Hardening |
| A.2.2 | Policies | AI data governance policy published and enforced — covers all GenAI data asset categories | L1 | Foundational |
| Cl.6.1 | Planning — risk | Data governance gaps identified and treated in AI risk register | L2 | Hardening |

#### Mitigations by tier

**Foundational**
- A.7.2: Establish data classification policy for
  all AI data assets — training data, embeddings,
  RAG corpora, and model outputs all classified with
  handling requirements documented
- A.2.2: Publish AI data governance policy —
  covers all data categories in AI system scope,
  ownership, lifecycle requirements, and controls

**Hardening**
- A.7.3: Implement data lifecycle management for
  all AI assets — retention periods, archival procedures,
  and verified deletion documented per asset type
- Cl.6.1: Include data governance gaps in AI risk
  register — risk owners, treatment plans, and
  review cadence documented

**Advanced**
- A.7.3: Implement AI unlearning capability as
  an A.7.3 data disposal control — mechanism to
  remove specific records from trained model behaviour
  in response to GDPR Article 17 requests
- A.7.2: Automate classification at data ingestion —
  classify before storage, not after

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI frameworks: DSGAI_NISTAIRMF.md (GV-1.6), DSGAI_EUAIAct.md (Art. 10/12)

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High

GenAI deployments violate data protection and AI regulation
requirements. ISO 42001 Clause 4.2 (Interested parties and
legal requirements) and A.2.2 provide the AIMS framework for
maintaining regulatory compliance across the GenAI data security
programme.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.2.2 | Policies | AI governance policy incorporates all applicable regulatory requirements | L1 | Foundational |
| A.8.1 | Information for interested parties | Transparency obligations to regulators, customers, and affected persons documented and met | L2 | Hardening |
| Cl.4.2 | Context — interested parties | All regulatory requirements identified, documented, and mapped to AIMS controls | L1 | Foundational |
| Cl.6.1 | Planning — risk | Regulatory non-compliance treated as an AI risk — regulatory requirements in risk register | L2 | Hardening |

#### Mitigations by tier

**Foundational**
- Cl.4.2: Identify all applicable regulatory
  requirements for each GenAI deployment — EU AI Act
  risk class, GDPR lawful basis, NIS2, sector-specific
  obligations documented in AIMS context
- A.2.2: Incorporate regulatory requirements into
  AI governance policy — policy reviewed when
  applicable regulations change

**Hardening**
- Cl.6.1: Map regulatory requirements to AIMS
  controls — traceability from obligation to
  implementation evidence maintained in documented
  information under Clause 7.5
- A.8.1: Maintain transparency records per
  regulatory obligations — records of processing,
  model card, user disclosure requirements

**Advanced**
- Cl.4.2: Maintain regulatory watch programme
  as a context monitoring activity — EU AI Act
  implementing acts, ENISA guidelines, sector-specific
  AI regulation developments
- Cl.9: Include regulatory compliance in AIMS
  internal audit scope — verify controls address
  current obligations annually

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| IBM OpenPages | Commercial | https://www.ibm.com/products/openpages |

#### Cross-references
- DSGAI frameworks: DSGAI_EUAIAct.md (Art. 9/17), DSGAI_NISTAIRMF.md (GV-4.2)

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Sensitive data in images, audio, video, or documents traverses
GenAI systems without adequate controls. ISO 42001 A.7.2 data
governance and A.5.2 impact assessment extend to all modalities
processed by AI systems — modality is not a basis for exclusion
from data governance scope.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — acquisition | Data classification and governance applies to all modalities — images, audio, video, documents treated as sensitive data assets equally | L2 | Hardening |
| A.6.2.3 | Lifecycle — operational | Operational DLP controls extended to all output modalities | L2 | Hardening |
| A.5.2 | Impact assessment | Privacy impact assessment explicitly covers multimodal data flows and cross-channel disclosure risks | L2 | Hardening |
| Cl.8 | Operation | Operational procedures for multimodal data handling documented | L2 | Hardening |

#### Mitigations by tier

**Hardening**
- A.7.2: Extend data classification to all GenAI
  modalities — images, audio, video, and documents
  classified with same requirements as text data
- A.6.2.3: Deploy multimodal DLP as an AIMS
  operational control — OCR and image classification
  on generated content before delivery
- A.5.2: Update privacy impact assessments to
  explicitly cover multimodal data flows

**Advanced**
- A.6.2.6: Red team multimodal extraction paths —
  test whether sensitive data in one modality can be
  recovered via a different output modality
- A.7.2: Implement content watermarking for
  generated multimodal outputs as an advanced
  data governance control

#### Tools

| Tool | Type | Link |
|---|---|---|
| AWS Rekognition | Commercial | https://aws.amazon.com/rekognition/ |
| Google Cloud DLP | Commercial | https://cloud.google.com/dlp |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MS-2.6), DSGAI_EUAIAct.md (Art. 10)

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium

Synthetic data re-identifies original subjects or anonymisation
is insufficient against inference attacks. ISO 42001 A.7.2
privacy-preserving data acquisition and A.5.2 impact assessment
address re-identification risk as a data governance and AI
impact concern.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — acquisition | Anonymisation requirements documented for all synthetic datasets; formal re-identification risk assessment required | L2 | Hardening |
| A.5.2 | Impact assessment | Re-identification risk included in AI impact assessment — residual risk accepted by accountable role | L2 | Hardening |
| A.7.3 | Data — preparation | Anonymisation techniques applied as a data preparation control; quality of anonymisation verified | L2 | Hardening |
| Cl.6.1 | Planning — risk | Re-identification risk documented in AI risk register with treatment controls | L2 | Hardening |

#### Mitigations by tier

**Hardening**
- A.7.2: Conduct formal re-identification risk
  assessment for all synthetic datasets — k-anonymity,
  l-diversity, differential privacy metrics evaluated
  before use
- A.5.2: Include re-identification risk in AI impact
  assessment — documented, with residual risk accepted
  by DPO or equivalent accountable role
- A.7.3: Verify anonymisation quality as a data
  preparation control — re-assess when model or
  data distribution changes

**Advanced**
- A.7.2: Apply differential privacy with formal
  epsilon budgets as an advanced A.7.2 data
  acquisition control for sensitive corpora
- A.6.2.6: Red team re-identification attacks
  against synthetic datasets as part of AI system
  security testing under Clause 8

#### Tools

| Tool | Type | Link |
|---|---|---|
| ARX Data Anonymization Tool | Open-source | https://arx.deidentifier.org |
| TensorFlow Privacy | Open-source | https://github.com/tensorflow/privacy |

#### Cross-references
- DSGAI 2026: DSGAI18 Inference & Data Reconstruction
- DSGAI frameworks: DSGAI_NISTAIRMF.md (GV-1.6), DSGAI_EUAIAct.md (Art. 10)

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High

Context from one user session leaks into another. ISO 42001 A.7.2
data isolation requirements and A.6.2.3 operational controls
address session boundary enforcement as an AI system data
governance and operational concern.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — acquisition | Session isolation requirements documented for all multi-tenant or multi-user GenAI deployments | L2 | Foundational |
| A.6.2.3 | Lifecycle — operational | Session boundary controls implemented as an AIMS operational control | L2 | Foundational |
| A.6.2.6 | Lifecycle — testing | Cross-session isolation testing in AI system testing activities | L2 | Hardening |
| Cl.8 | Operation | Operational procedures for session data management documented | L1 | Foundational |

#### Mitigations by tier

**Foundational**
- A.7.2: Document session isolation requirements
  for all GenAI deployments — conversation history,
  context stores, and embeddings isolated per session
- A.6.2.3: Implement session boundary controls as
  an AIMS operational control — cryptographic separation
  of session context stores

**Hardening**
- A.6.2.6: Include cross-session isolation testing
  in AI system testing activities — test data leakage
  across session boundaries before each deployment
- Cl.8: Document session data disposal procedures —
  context cleared at session end, retained data
  subject to data lifecycle policy

**Advanced**
- A.6.2.6: Red team session isolation — test whether
  crafted inputs can extract prior session context
  from shared infrastructure

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Azure AI Content Safety | Commercial | https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM07 System Prompt Leakage
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MP-2.3), DSGAI_EUAIAct.md (Art. 10)

---

### DSGAI12 — Unsafe NL Data Gateways

**Severity:** Critical

Natural language interfaces to databases execute unvalidated
queries. ISO 42001 A.6.2.3 and A.6.2.6 operational and testing
controls directly address NL gateway security — output handling
and adversarial testing are core lifecycle requirements.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.6.2.3 | Lifecycle — operational | Query validation layer required between NL model and database as an AI system operational control | L2 | Foundational |
| A.6.2.6 | Lifecycle — testing | Prompt injection testing against NL gateways in AI system testing activities | L2 | Hardening |
| A.7.2 | Data — access control | Data access through NL gateways subject to same classification and authorisation as direct API access | L1 | Foundational |
| A.9.1 | Use of AI systems | User guidance on permitted queries; scope limitations disclosed | L1 | Foundational |

#### Mitigations by tier

**Foundational**
- A.6.2.3: Implement query validation layer as
  an AIMS operational control — generated queries
  reviewed against authorised patterns before execution
- A.7.2: Apply data classification controls to NL
  gateway access — authorisation enforced at data layer

**Hardening**
- A.6.2.6: Include prompt injection testing in
  AI system testing activities — test NL gateway
  with injection payloads before each deployment
- A.6.2.3: Implement least-privilege database
  credentials for NL gateways — read-only where
  appropriate, table scope restricted to business need

**Advanced**
- A.6.2.6: Red team NL gateway with known
  text-to-SQL injection patterns — as part of
  AI system security testing under Clause 8
- A.7.2: Implement NL query output DLP — scan
  query results before delivery

#### Tools

| Tool | Type | Link |
|---|---|---|
| Rebuff | Open-source | https://github.com/protectai/rebuff |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM05 Insecure Output Handling
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MP-2.3), DSGAI_EUAIAct.md (Art. 15)

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector databases are inadequately secured — injection attacks
and unauthorised access expose sensitive embedding data. ISO 42001
A.7.2 covers embedding stores as AI data assets; A.10.1 covers
vector database vendors as third-party AI components.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — acquisition | Embedding stores classified and governed as sensitive AI data assets — access controlled and encrypted | L1 | Foundational |
| A.7.3 | Data — preparation | Embedding data subject to same preparation governance as primary data assets | L2 | Hardening |
| A.6.1.2 | Lifecycle — design | Vector store security requirements specified at AI system design stage | L1 | Foundational |
| A.10.1 | Third-party | Vector database platform vendors assessed as third-party AI system components | L2 | Hardening |

#### Mitigations by tier

**Foundational**
- A.7.2: Classify embedding stores as sensitive
  AI data assets — access controls and encryption
  equivalent to primary data stores
- A.6.1.2: Specify vector store security requirements
  at design stage — authentication, encryption, namespace
  isolation documented in AI system design

**Hardening**
- A.10.1: Apply AIMS third-party assessment to
  vector database vendors — security configuration
  review, CVE monitoring, patch management SLA
- A.7.3: Implement namespace isolation for multi-tenant
  deployments — cross-tenant retrieval prevention
  as a data preparation governance control

**Advanced**
- A.6.2.6: Red team vector store for injection
  attacks and metadata extraction as part of AI
  system security testing under Clause 8

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://github.com/weaviate/weaviate |
| Qdrant | Open-source | https://github.com/qdrant/qdrant |

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MP-2.3), DSGAI_ENISA.md (DMS L2)

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High

Observability pipelines capture sensitive data in logs and traces.
ISO 42001 A.7.2 data governance extends to telemetry as a
data category; Clause 9 performance evaluation requirements
create a governance obligation to manage the security of
monitoring systems.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — governance | Telemetry data classified and governed — prompts, completions, and embeddings in logs treated as sensitive AI data assets | L2 | Foundational |
| A.2.2 | Policies | Data governance policy explicitly covers telemetry data — retention, access, and disposal requirements | L1 | Foundational |
| A.6.2.6 | Lifecycle — testing | Telemetry data leakage testing in AI system testing activities | L2 | Hardening |
| Cl.9 | Performance evaluation | Monitoring infrastructure protected as part of performance evaluation control environment | L2 | Hardening |

#### Mitigations by tier

**Foundational**
- A.7.2: Classify telemetry data — prompts,
  completions in logs are sensitive AI data assets
  subject to data classification policy
- A.2.2: Extend data governance policy to cover
  telemetry — retention, access, and disposal
  requirements documented for observability stores

**Hardening**
- A.6.2.6: Test telemetry data leakage as part
  of AI system testing — verify sensitive data
  is redacted before storage
- Cl.9: Protect monitoring infrastructure under
  AIMS performance evaluation controls — access
  controls, encryption, and audit logging for
  all telemetry stores

**Advanced**
- A.7.2: Implement structured telemetry redaction —
  define permitted and prohibited fields in telemetry
  as a formal data governance control

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Grafana Loki | Open-source | https://github.com/grafana/loki |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, Lifecycle & Classification
- DSGAI frameworks: DSGAI_NISTAIRMF.md (GV-1.6), DSGAI_EUAIAct.md (Art. 12)

---

### DSGAI15 — Over-Broad Context Windows

**Severity:** High

Context windows populated with excessive data create exfiltration
opportunities. ISO 42001 A.7.2 data minimisation requirements
and A.5.2 impact assessment address context window scope as both
a data governance and AI impact concern.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — minimisation | Data minimisation principle applied to context window design — only data necessary for the task included | L1 | Foundational |
| A.6.2.3 | Lifecycle — operational | Context scope controls implemented as an AIMS operational control | L2 | Foundational |
| A.5.2 | Impact assessment | Over-broad context included as a data disclosure risk in AI impact assessment | L2 | Hardening |
| Cl.8 | Operation | Context window management procedures documented in operational procedures | L1 | Foundational |

#### Mitigations by tier

**Foundational**
- A.7.2: Apply data minimisation to context window
  design — only task-necessary data included;
  data minimisation principle documented as A.7.2
  data acquisition control
- A.6.2.3: Implement context scope controls as
  AIMS operational controls — RAG retrieval scoped
  to user permission level

**Hardening**
- A.5.2: Include over-broad context in AI impact
  assessment — disclosure risk documented with
  treatment controls
- A.6.2.6: Include context scope review in AI
  system testing — document maximum permitted
  context scope per use case

**Advanced**
- A.6.2.6: Red team context window extraction
  as part of AI system security testing under Clause 8

#### Tools

| Tool | Type | Link |
|---|---|---|
| LlamaIndex | Open-source | https://github.com/run-llama/llama_index |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MS-2.5), DSGAI_EUAIAct.md (Art. 10)

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High

AI assistants on endpoints access data beyond defined scope.
ISO 42001 A.9.1 (Use of AI Systems) and A.2.2 (Policies) address
endpoint AI assistant scope definition and user guidance as
AIMS use policy and operational controls.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.9.1 | Use of AI systems | Endpoint AI assistant scope documented — permitted data access, restrictions, and user responsibilities disclosed | L1 | Foundational |
| A.6.1.2 | Lifecycle — design | Minimal permission design applied to endpoint AI assistant — data access scope specified at design | L1 | Foundational |
| A.2.2 | Policies | AI acceptable use policy covers endpoint AI assistants — permitted use, data handling, user obligations | L1 | Foundational |
| Cl.4 | Context | Endpoint AI assistants included in AIMS scope — all AI systems in organisational use inventoried | L1 | Foundational |

#### Mitigations by tier

**Foundational**
- A.6.1.2: Apply minimal permission design to
  endpoint AI assistants — data access scope specified
  at design stage, no broad file system access by default
- A.9.1: Document scope and data access limitations
  for endpoint AI assistants — disclosed to users
  before deployment
- A.2.2: Include endpoint AI assistants in AI
  acceptable use policy — employee guidance on
  permitted use and data sharing

**Hardening**
- A.6.2.3: Implement scope enforcement as an AIMS
  operational control — platform-level permission
  enforcement, not relying on user compliance
- A.6.2.6: Include scope boundary testing in AI
  system testing activities

**Advanced**
- A.6.2.6: Red team endpoint AI assistant scope
  controls — test whether crafted inputs trigger
  access to data outside defined scope

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Intune | Commercial | https://www.microsoft.com/en-us/security/business/endpoint-management/microsoft-intune |
| Carbon Black | Commercial | https://www.vmware.com/products/carbon-black-cloud.html |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI frameworks: DSGAI_NISTAIRMF.md (GV-1.7), DSGAI_EUAIAct.md (Art. 9)

---

### DSGAI17 — Data Availability & Resilience Failures

**Severity:** High

GenAI systems lack resilience controls — training data, model
weights, or RAG corpora are lost or unavailable causing
irrecoverable failures. ISO 42001 Clause 8 operation and
Clause 10 improvement together address availability and recovery
as lifecycle management responsibilities.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.6.2.8 | Lifecycle — decommissioning | AI system decommissioning procedures ensure data and model artefact preservation and recovery capability | L2 | Foundational |
| A.6.2.6 | Lifecycle — testing | Recovery testing as part of AI system testing activities | L2 | Hardening |
| Cl.8 | Operation | Backup and recovery procedures for all AI system critical data assets documented in operational procedures | L1 | Foundational |
| Cl.10 | Improvement | Recovery gaps identified in management review addressed through corrective action | L2 | Hardening |

#### Mitigations by tier

**Foundational**
- Cl.8: Document backup and recovery procedures
  for all AI system critical assets — training data,
  model weights, embeddings, RAG corpora
- A.6.2.8: Include data preservation requirements
  in AI system decommissioning procedures —
  artefacts preserved or securely deleted per policy

**Hardening**
- A.6.2.6: Include recovery testing in AI system
  testing activities — verify model rollback, data
  restoration, and service recovery within RTOs
- Cl.10: Address recovery gaps through AIMS
  corrective action process — findings from recovery
  tests documented and remediated

**Advanced**
- A.6.2.6: Annual AI disaster recovery test —
  full validation of all recovery procedures
  documented as AIMS performance evaluation evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| DVC (Data Version Control) | Open-source | https://github.com/iterative/dvc |
| MLflow | Open-source | https://github.com/mlflow/mlflow |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MG-2.2), DSGAI_EUAIAct.md (Art. 15)

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High

Attackers extract training data through membership inference,
model inversion, or attribute inference attacks. ISO 42001 A.7.2
privacy-preserving data techniques and A.5.2 impact assessment
are the primary AIMS controls for inference attack risk.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — privacy-preserving | Differential privacy and output restrictions applied as A.7.2 data acquisition controls for sensitive corpora | L2 | Hardening |
| A.5.2 | Impact assessment | Inference attack risk documented in AI impact assessment — membership inference, model inversion, attribute inference | L2 | Hardening |
| A.6.2.6 | Lifecycle — testing | Inference attack red teaming in AI system testing activities | L2 | Advanced |
| Cl.6.1 | Planning — risk | Inference attack risk documented in AI risk register with treatment controls | L2 | Hardening |

#### Mitigations by tier

**Hardening**
- A.7.2: Implement prediction output restrictions
  as A.7.2 inference attack mitigations —
  confidence truncation, output perturbation, rate limiting
- A.5.2: Document inference attack risk in AI
  impact assessment — treatment controls justified
  against sensitivity of training data
- Cl.6.1: Include inference attack risk in AI
  risk register — treatment controls and residual risk

**Advanced**
- A.7.2: Apply differential privacy to model
  training for high-sensitivity corpora — formal
  epsilon budget documented as A.7.2 evidence
- A.6.2.6: Red team membership inference and model
  inversion attacks as part of AI system security
  testing under Clause 8

#### Tools

| Tool | Type | Link |
|---|---|---|
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |
| TensorFlow Privacy | Open-source | https://github.com/tensorflow/privacy |

#### Cross-references
- DSGAI 2026: DSGAI10 Synthetic Data & Anonymisation Pitfalls
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MS-2.5), DSGAI_EUAIAct.md (Art. 10)

---

### DSGAI19 — Human-in-Loop & Labeler Overexposure

**Severity:** Medium

Human reviewers and labelers access sensitive data without
adequate controls. ISO 42001 A.10 third-party controls and A.7.2
data minimisation are the primary AIMS controls — data labeling
services are third-party components of the AI development lifecycle.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — minimisation | Data provided to human reviewers minimised — unnecessary sensitive data removed before labeling batches | L2 | Foundational |
| A.10.1 | Third-party | Labeling service providers assessed as third-party AI system components | L2 | Hardening |
| A.3.3 | Internal organisation — roles | Accountability for labeling data governance assigned to named role | L1 | Foundational |
| Cl.7 | Support | Competence requirements for staff with access to labeling data documented | L1 | Foundational |

#### Mitigations by tier

**Foundational**
- A.7.2: Apply data minimisation to labeling batches —
  remove unnecessary PII and sensitive content before
  providing data to reviewers
- A.3.3: Assign accountability for labeling data
  governance — named role responsible for reviewer
  data access, DPA, and audit

**Hardening**
- A.10.1: Apply AIMS third-party assessment to
  labeling service vendors — jurisdiction, security
  controls, sub-contractor chain reviewed
- A.10.1: Execute DPA with all labeling service
  providers — data handling requirements, sub-processor
  restrictions, breach notification documented

**Advanced**
- A.7.2: Implement privacy-preserving labeling
  techniques where full fidelity is not required —
  data perturbation or synthetic replacement
- A.10.1: Periodic labeling vendor re-assessment —
  verify controls are operating as contracted

#### Tools

| Tool | Type | Link |
|---|---|---|
| Label Studio | Open-source | https://github.com/HumanSignal/label-studio |
| Scale AI | Commercial | https://scale.com |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, Lifecycle & Classification
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MP-5.1), DSGAI_EUAIAct.md (Art. 10)

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High

Adversaries extract model weights or functional equivalents
through model stealing attacks. ISO 42001 A.7.3 model artefact
protection and Cl.6.1 IP risk management address model
exfiltration as both a data security and AI system integrity risk.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.3 | Data — model artefacts | Model weights and training artefacts classified as high-value IP assets — access controls, encryption, and audit logging equivalent to source code | L2 | Hardening |
| A.6.1.2 | Lifecycle — design | Model distribution and access controls designed in at system design stage | L1 | Foundational |
| A.6.2.6 | Lifecycle — testing | Model extraction attack testing in AI system security testing activities | L2 | Advanced |
| Cl.6.1 | Planning — risk | Model exfiltration risk documented in AI risk register — treatment controls and residual risk |  L2 | Hardening |

#### Mitigations by tier

**Foundational**
- A.6.1.2: Specify model artefact access controls
  at design stage — model weights distribution
  channels documented, access controls designed in

**Hardening**
- A.7.3: Classify model weights as critical IP assets —
  access controls, encryption, and access audit logging
  as A.7.3 data controls for AI artefacts
- Cl.6.1: Document model exfiltration risk in AI
  risk register — treatment controls and residual risk

**Advanced**
- A.6.2.6: Red team model extraction attacks —
  test whether API defences prevent functional model
  replication as part of AI system security testing
- A.7.3: Apply model watermarking as an advanced
  data governance control — enable forensic attribution
  of extracted models

#### Tools

| Tool | Type | Link |
|---|---|---|
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Knockoff Nets detection | Research | https://arxiv.org/abs/1812.02766 |

#### Cross-references
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MS-2.6), DSGAI_EUAIAct.md (Art. 15)

---

### DSGAI21 — Disinformation via Data Poisoning

**Severity:** High

Attackers poison training or RAG data to cause systematic
disinformation in model outputs. ISO 42001 A.7.2 and A.7.3
data integrity controls, combined with A.5.2 impact assessment
for societal impact, address disinformation risk as a data
governance and AI impact concern.

#### ISO 42001 control mapping

| Control | Section | Description | Level | Tier |
|---|---|---|---|---|
| A.7.2 | Data — provenance | Source credibility assessment and provenance verification for all fine-tuning and RAG corpora | L2 | Hardening |
| A.7.3 | Data — quality | Factual accuracy validation in data preparation — cross-source consistency, credibility scoring | L2 | Hardening |
| A.5.2 | Impact assessment | Disinformation risk included in AI impact assessment — sector-specific severity assessed | L2 | Hardening |
| A.8.1 | Transparency | Output source attribution requirements documented — users informed when AI generates potentially unverifiable content | L2 | Hardening |

#### Mitigations by tier

**Hardening**
- A.7.2: Verify provenance and credibility of all
  fine-tuning and RAG corpora as A.7.2 data
  acquisition controls — source credibility scoring,
  cross-source consistency checking before ingestion
- A.5.2: Include disinformation risk in AI impact
  assessment — sector-specific impact for healthcare,
  finance, critical infrastructure assessed
- A.8.1: Implement output source attribution for
  high-stakes use cases — citations enable factual
  verification by consumers

**Advanced**
- A.7.3: Red team targeted disinformation injection —
  test whether adversarially poisoned content survives
  data quality controls as AI system security testing
- A.5.2: Treat systematic AI disinformation as a
  significant incident category for high-risk AI systems —
  include in incident response plan and reporting procedures

#### Tools

| Tool | Type | Link |
|---|---|---|
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| FactScore | Research | https://github.com/shmsw25/FActScoring |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning, LLM09 Misinformation
- DSGAI frameworks: DSGAI_NISTAIRMF.md (MS-3.3), DSGAI_EUAIAct.md (Art. 52)

---

## Implementation priority

| Priority | DSGAI IDs | ISO 42001 focus | Rationale |
|---|---|---|---|
| P1 — Critical, address first | DSGAI01, DSGAI02, DSGAI04, DSGAI12 | A.7.2/A.7.3, A.6.1.2, A.6.2.3 | Critical severity — data leakage, credential exposure, poisoning, NL gateway |
| P2 — High, within 90 days | DSGAI05, DSGAI06, DSGAI07, DSGAI11, DSGAI13 | Cl.8, A.10.1/A.10.2, A.7.2/A.7.3 | Data integrity, tool governance, data lifecycle, session isolation, vector store |
| P3 — High, within 180 days | DSGAI03, DSGAI08, DSGAI09, DSGAI14, DSGAI15, DSGAI16, DSGAI17 | Cl.4, A.2.2, A.5.2, Cl.9 | Shadow AI, compliance, multimodal, telemetry, context, endpoint, resilience |
| P4 — Medium/Advanced, within 1 year | DSGAI10, DSGAI18, DSGAI19, DSGAI20, DSGAI21 | A.5.2, A.6.2.6, A.7.2/A.7.3 | Synthetic data, inference attacks, labeler overexposure, model exfiltration, disinformation |

---

## ISO 42001 + ISO 27001 integration note

ISO 42001 is designed to operate alongside ISO 27001 using the
same High-Level Structure. For organisations with an ISO 27001
ISMS, the DSGAI risks map to AIMS controls (ISO 42001) that extend
the existing ISMS rather than replacing it:

- **ISO 27001 Annex A A.8.11/A.8.12** (data masking/leakage prevention)
  extends to **ISO 42001 A.7.2** (AI-specific data governance) for training data and embeddings
- **ISO 27001 A.5.22** (third-party ICT services)
  extends to **ISO 42001 A.10.1** (third-party AI components)
- **ISO 27001 A.8.28** (secure coding)
  extends to **ISO 42001 A.6.2.3** (AI system operational controls)

Run a gap analysis against ISO 27001 controls first; the gaps
that cannot be addressed through existing ISMS controls are
where ISO 42001 AIMS controls are needed.

---

## References

- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)
- [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [ISO/IEC 42001 Implementation Guide](https://www.iso.org/standard/81230.html)
- [LLM_ISO42001.md](../llm-top10/LLM_ISO42001.md) — ISO 42001 × LLM Top 10
- [Agentic_ISO42001.md](../agentic-top10/Agentic_ISO42001.md) — ISO 42001 × Agentic Top 10

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-27 | Initial release — full DSGAI01–DSGAI21 mapping to ISO/IEC 42001:2023 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the OWASP GenAI Data Security Initiative.
Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
