<!--
  GenAI Security Crosswalk
  Source list : OWASP GenAI Data Security Risks and Mitigations 2026 (DSGAI01-DSGAI21)
  Framework   : SOC 2 Type II — AICPA Trust Services Criteria
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 x SOC 2

Mapping the [OWASP GenAI Data Security Risks and Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01-DSGAI21) to [SOC 2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
— the AICPA Trust Services Criteria.

The DSGAI taxonomy follows data as it moves through a GenAI system.
SOC 2 Trust Services Criteria follow the obligations a service
organisation makes to its customers and stakeholders about data
handling, availability, and integrity. This mapping connects the
two: for each GenAI data security risk, it identifies which SOC 2
criteria are implicated and what auditor-ready controls address them.

The DSGAI-SOC 2 intersection is more extensive than the LLM Top 10
intersection because the DSGAI taxonomy explicitly covers data
lifecycle management, regulatory compliance, privacy, and operational
data security — all of which have direct SOC 2 criteria parallels.
Confidentiality (C), Privacy (P), and Processing Integrity (PI) criteria
are implicated throughout the DSGAI taxonomy, not only in the
obviously data-focused entries.

---

## Quick-reference summary

| ID | Name | Severity | Primary SOC 2 Criteria | Tier |
|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | C1, C2, CC6, P5, CC7 | Foundational-Advanced |
| DSGAI02 | Agent Identity and Credential Exposure | Critical | CC6, CC9, CC7, CC5 | Foundational-Advanced |
| DSGAI03 | Shadow AI and Unsanctioned Data Flows | High | CC5, CC9, CC3, C1 | Foundational-Hardening |
| DSGAI04 | Data, Model and Artifact Poisoning | Critical | CC3, CC8, CC9, CC7 | Hardening-Advanced |
| DSGAI05 | Data Integrity and Validation Failures | High | PI1, CC5, CC7, CC3 | Foundational-Hardening |
| DSGAI06 | Tool, Plugin and Agent Data Exchange | High | CC9, C2, CC6, CC5 | Foundational-Hardening |
| DSGAI07 | Data Governance, Lifecycle and Classification | High | C1, P4, CC5, CC3 | Foundational-Advanced |
| DSGAI08 | Non-Compliance and Regulatory Violations | High | CC5, CC3, P1, CC2 | Foundational-Advanced |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | C2, P5, CC6, CC7 | Hardening-Advanced |
| DSGAI10 | Synthetic Data and Anonymisation Pitfalls | Medium | P4, P5, CC3, C2 | Hardening-Advanced |
| DSGAI11 | Cross-Context Conversation Bleed | High | CC6, C2, P5, CC7 | Foundational-Hardening |
| DSGAI12 | Unsafe NL Data Gateways | Critical | CC6, CC5, PI1, CC7 | Foundational-Advanced |
| DSGAI13 | Vector Store Platform Security | High | C2, CC6, CC7, CC8 | Foundational-Hardening |
| DSGAI14 | Excessive Telemetry and Monitoring Leakage | High | C2, P5, CC6, CC7 | Foundational-Hardening |
| DSGAI15 | Over-Broad Context Windows | High | CC6, C2, CC5, CC3 | Foundational-Hardening |
| DSGAI16 | Endpoint and Browser Assistant Overreach | High | CC6, CC5, CC9, CC3 | Foundational-Hardening |
| DSGAI17 | Data Availability and Resilience Failures | High | A1, CC7, CC3, CC5 | Foundational-Advanced |
| DSGAI18 | Inference and Data Reconstruction | High | C2, P5, CC7, CC3 | Hardening-Advanced |
| DSGAI19 | Human-in-Loop and Labeler Overexposure | Medium | CC9, C2, P3, P5 | Foundational-Hardening |
| DSGAI20 | Model Exfiltration and IP Replication | High | C2, CC6, CC7, CC3 | Hardening-Advanced |
| DSGAI21 | Disinformation via Data Poisoning | High | PI1, CC9, CC7, CC3 | Hardening-Advanced |

---

## Audience tags

- **CISO / compliance lead** — full file, SOC 2 criteria mapping for GenAI data programme
- **SOC 2 audit preparation team** — criteria-to-control mapping for auditor evidence
- **DPO** — Privacy criteria entries throughout (P1-P8)
- **Data governance lead** — DSGAI07, DSGAI08, DSGAI10 entries
- **SaaS / cloud AI product team** — vendor trust, confidentiality, privacy criteria
- **Security engineer** — CC6/CC7 technical control entries

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

Sensitive data leaks from GenAI systems through model outputs, RAG
retrieval, embedding exposure, or observability pipelines. SOC 2
Confidentiality (C) and Privacy (P) criteria are directly implicated —
this is the data security risk most likely to appear in a SOC 2
customer inquiry or audit finding for AI-powered SaaS providers.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C1.1 — Confidentiality policy | Policy identifying confidential information in GenAI scope — training data, RAG corpus, embeddings, outputs |
| C2.1 — Confidential information protection | Technical controls protecting confidential data in GenAI pipelines — encryption, access controls, output scanning |
| CC6.1 — Logical access | Access controls on RAG retrieval — users retrieve only data they are authorised to access |
| P5.1 — Personal information use | Personal information in GenAI scope used only for authorised purposes — LLM processing limited to agreed use cases |
| CC7.2 — Anomaly detection | DLP monitoring on all GenAI output channels — sensitive patterns detected before delivery to users |

#### Mitigations for SOC 2 evidence

**Control implementation**
- C1.1: Document confidentiality policy covering all GenAI
  data assets — training data, RAG sources, embeddings,
  outputs, observability data — classification and handling
  requirements
- C2.1: Implement technical protection controls —
  encryption at rest and in transit, access-controlled
  retrieval, output redaction — documented as auditor evidence
- CC7.2: Deploy DLP monitoring on all output channels —
  monitoring configuration, alert records, and response
  procedures for auditor review

**Audit evidence preparation**
- Confidentiality policy covering GenAI data assets (C1.1)
- Encryption configuration for GenAI data stores (C2.1)
- Access control configuration for RAG retrieval (CC6.1)
- DLP monitoring configuration and alert samples (CC7.2)
- Privacy documentation for personal data in GenAI scope (P5.1)

**Hardening**
- Apply output redaction — C2.1 technical control evidence
- Audit RAG access controls quarterly — CC4.1 monitoring
  of access control effectiveness evidence
- CC7.4: Conduct model inversion testing — security testing
  evidence of confidentiality control effectiveness

**Advanced**
- Apply differential privacy in training — C2.1 advanced
  technical control evidence
- Machine unlearning readiness — P7.1 personal information
  disposal capability evidence

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity and Privilege Abuse
- Other frameworks: ISO 27001 A.8.11/A.8.12 · EU AI Act Art. 10 · GDPR Art. 25

---

### DSGAI02 — Agent Identity and Credential Exposure

**Severity:** Critical

AI agents inherit and cache credentials that, when compromised,
expose all systems the agent has access to. SOC 2 CC6 (logical
access — privileged access management) is the primary criterion.
CC9 (vendor risk — NHI governance as a vendor-like obligation)
and CC7 (monitoring — credential anomaly detection) also apply.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC6.1 — Logical access | Agent credentials managed as privileged access — minimum scope, documented justification, regular review |
| CC6.3 — Access removal | Agent credentials revoked on decommission and anomaly detection — no dormant agent NHIs |
| CC9.1 — Vendor risk | Agent tool providers assessed — data handling, credential security requirements in vendor agreements |
| CC7.2 — Anomaly detection | Agent credential anomaly monitoring — unusual usage patterns detected and alerted |
| CC5.2 — Control activities | Agent credential lifecycle procedures — issuance, rotation, revocation documented |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC6.1: Manage agent credentials under privileged access
  programme — access control configuration, scope
  documentation, review records for auditors
- CC5.2: Document agent credential lifecycle procedures —
  issuance, rotation, revocation procedures, secret
  manager configuration
- CC7.2: Implement credential anomaly monitoring — alert
  configuration and sample alerts for auditor review

**Audit evidence preparation**
- Agent credential access control configuration (CC6.1)
- Privileged access review records for agent NHIs (CC6.1)
- Agent credential lifecycle procedure documentation (CC5.2)
- Credential anomaly monitoring configuration (CC7.2)
- Vendor agreements with credential security obligations (CC9.2)

**Hardening**
- CC6.3: Formal agent offboarding procedure — credential
  revocation records as access removal evidence
- Implement JIT credential issuance — CC6.1 advanced
  access control evidence
- CC7.2: Continuous NHI monitoring — anomalous usage
  pattern detection evidence

#### Cross-references
- Agentic Top 10: ASI03 Identity and Privilege Abuse
- Other frameworks: OWASP NHI Top 10 · ISO 27001 A.8.2/A.5.16 · EU AI Act Art. 15

---

### DSGAI03 — Shadow AI and Unsanctioned Data Flows

**Severity:** High

Employees use unapproved GenAI SaaS tools creating ungoverned data
flows. SOC 2 CC5 (control activities — acceptable use procedures)
and CC9 (vendor risk — unapproved vendors not in the programme)
are the primary criteria. This is a common SOC 2 gap finding for
organisations with AI governance programmes that do not explicitly
cover shadow AI.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC5.2 — Control activities | Acceptable use procedures for AI tools — approved list, prohibited use cases, employee acknowledgement |
| CC9.1 — Vendor risk | Shadow AI vendors not in vendor risk programme — shadow AI discovery identifies unapproved vendors |
| CC3.2 — Risk assessment | Shadow AI usage identified as a risk in assessment — ungoverned data flows, training use by vendors |
| C1.1 — Confidentiality policy | Confidentiality policy covers AI tool use — employees informed of restrictions on sharing confidential data |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC5.2: Document AI acceptable use procedures — approved
  tool list, prohibited use cases, employee acknowledgement
  records as control activity evidence
- CC9.1: Include AI tool approval in vendor risk programme —
  approved AI tool list with assessment records, shadow
  AI discovery as vendor monitoring evidence
- CC3.2: Include shadow AI in risk assessment — ungoverned
  data flows to AI vendors as documented risk

**Audit evidence preparation**
- AI acceptable use policy and employee acknowledgement records (CC5.2)
- Approved AI tool list and assessment records (CC9.1)
- Shadow AI discovery programme configuration (CC9.1, CC7.2)
- Risk assessment entries for shadow AI (CC3.2)
- Confidentiality policy covering AI tool use (C1.1)

**Hardening**
- Implement shadow AI discovery — CC9.1 ongoing vendor
  monitoring evidence, CC7.2 anomaly detection evidence
- Deploy DLP on AI SaaS endpoints — CC5.2 technical
  enforcement evidence, C2.1 confidentiality protection

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.10/A.5.23 · NIST CSF 2.0 GV.RM-06

---

### DSGAI04 — Data, Model and Artifact Poisoning

**Severity:** Critical

Adversaries corrupt training data or model weights. SOC 2 CC3 (risk
assessment), CC8 (change management — model promotions as system
changes), CC9 (vendor risk — training data providers), and CC7
(monitoring — poisoning detection) all apply.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC3.2 — Risk assessment | Poisoning threats documented in GenAI risk assessment — training data, supply chain, model update vectors |
| CC8.1 — Change management | Model promotions through change management — integrity verification before production deployment |
| CC9.1 — Vendor risk | Training data providers in vendor risk programme — provenance, quality, integrity requirements assessed |
| CC7.2 — Anomaly detection | Model output anomaly monitoring — poisoning indicators detected before operational impact |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC3.2: Document poisoning risks in GenAI risk assessment —
  training data sources, fine-tuning pipeline, and supply
  chain attack vectors
- CC8.1: Include model promotions in change management —
  integrity verification, testing requirements, and
  rollback capability documented in change records
- CC9.1: Assess training data providers in vendor risk
  programme — provenance and quality requirements in
  vendor agreements

**Audit evidence preparation**
- Risk assessment entries for poisoning (CC3.2)
- Change management records for model promotions (CC8.1)
- Vendor assessment records for training data providers (CC9.1)
- Model output anomaly monitoring configuration (CC7.2)
- Incident response procedure for poisoning events (CC7.3)

**Hardening**
- CC8.1: Automated integrity verification in deployment
  pipeline — change management control evidence
- CC7.4: Include poisoning detection in security testing —
  results documented as testing evidence
- Model rollback capability — CC8.1 rollback procedure
  in change management

#### Cross-references
- LLM Top 10: LLM03 Supply Chain, LLM04 Data and Model Poisoning
- Agentic Top 10: ASI06 Memory and Context Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · ISO 27001 A.8.27 · MITRE ATLAS AML.T0032

---

### DSGAI05 — Data Integrity and Validation Failures

**Severity:** High

Adversarially crafted payloads corrupt training sets or exploit
snapshot import path traversal. SOC 2 Processing Integrity (PI1)
is the primary criterion — data integrity at ingestion is a
processing integrity requirement. CC5 (control activities —
validation procedures) and CC7 (monitoring — ingestion anomaly
detection) also apply.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| PI1.2 — System inputs complete and accurate | Ingestion validation controls — schema and semantic validation ensuring only accurate inputs enter processing |
| CC5.2 — Control activities | Documented ingestion validation procedures — multi-stage validation, path traversal prevention |
| CC7.2 — Anomaly detection | Ingestion anomaly detection — unusual payloads detected before pipeline completion |
| CC3.2 — Risk assessment | Ingestion integrity risks in GenAI risk assessment — schema bypass, path traversal, adversarial payload vectors |

#### Mitigations for SOC 2 evidence

**Control implementation**
- PI1.2: Document ingestion validation procedures —
  multi-stage validation, schema enforcement, path
  traversal prevention as processing integrity controls
- CC5.2: Include ingestion security in control activities —
  documented procedures, implementation records
- CC7.2: Deploy ingestion anomaly detection — alert
  configuration and sample findings for auditors

**Audit evidence preparation**
- Ingestion validation procedure documentation (PI1.2, CC5.2)
- CVE patching records for vector databases (CC8.1)
- Ingestion anomaly monitoring configuration (CC7.2)
- Risk assessment entries for ingestion integrity (CC3.2)
- Security testing results for ingestion interfaces (CC7.4)

**Hardening**
- CC7.4: Include schema bypass and path traversal in
  security testing — results documented as audit evidence
- Patch CVE-2024-3584 class vulnerabilities — CC8.1
  change management evidence showing timely remediation

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-20 · OWASP ASVS V5

---

### DSGAI06 — Tool, Plugin and Agent Data Exchange Risks

**Severity:** High

AI tools and plugins receive full context payloads with no data
minimisation. SOC 2 CC9 (vendor risk — tool providers as vendors)
is the primary criterion. C2 (confidentiality protection — data
minimisation for tool calls) and CC6 (access control — tool
permissions) also apply.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC9.1 — Vendor risk | Tool and plugin providers assessed in vendor risk programme — what data they receive, retain, and use |
| CC9.2 — Vendor agreements | Contractual data handling obligations for tool providers — data minimisation, retention, training use restrictions |
| C2.1 — Confidential information protection | Context minimisation for tool calls — tools receive minimum confidential data required for function |
| CC6.1 — Logical access | Tool access scoped to minimum required — agent tool permissions as privileged access |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC9.1: Include tool and plugin providers in vendor risk
  assessment programme — security questionnaires, data
  handling review, assessment records
- CC9.2: Establish vendor agreements covering tool data
  handling — zero training use, retention limits,
  incident notification as contractual evidence
- C2.1: Document context minimisation procedures —
  tools receive minimum required data, not full context

**Audit evidence preparation**
- Tool provider vendor assessment records (CC9.1)
- Vendor agreements with data handling obligations (CC9.2)
- Context minimisation procedure documentation (C2.1)
- Tool access control configuration (CC6.1)
- Payload inspection configuration for tool calls (CC7.2)

**Hardening**
- Deploy outbound DLP on tool API calls — C2.1 technical
  confidentiality protection evidence
- CC9.2: Right-to-audit provision in tool vendor agreements —
  contractual control evidence

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI04 Supply Chain
- Other frameworks: ISO 27001 A.5.19/A.5.20 · NIST AI RMF MP-5.1

---

### DSGAI07 — Data Governance, Lifecycle and Classification

**Severity:** High

GenAI creates ungoverned derived data assets outside traditional
governance programmes. SOC 2 Confidentiality (C1) and Privacy (P4)
are the primary criteria — classification of what data exists and
retention management for derived assets are SOC 2 audit requirements.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C1.1 — Confidentiality policy | Policy identifies all confidential information in GenAI scope — including derived assets (embeddings, caches, traces) |
| P4.1 — Privacy information lifecycle | Personal information lifecycle management covers GenAI-derived assets — embeddings inherit source data obligations |
| CC5.2 — Control activities | Data lifecycle procedures documented — classification propagation, retention schedules, deletion procedures |
| CC3.2 — Risk assessment | Ungoverned derived asset risks identified in assessment — embeddings, caches, agent memory outside governance scope |

#### Mitigations for SOC 2 evidence

**Control implementation**
- C1.1: Extend confidentiality policy to all GenAI-derived
  assets — embeddings, summaries, caches, agent memory,
  observability logs — classification and handling
  requirements documented
- P4.1: Document personal information lifecycle for
  GenAI-derived assets — embeddings of personal data
  subject to same lifecycle obligations as source data
- CC5.2: Document classification propagation and retention
  procedures — policy-driven expiry, deletion verification

**Audit evidence preparation**
- Confidentiality policy covering GenAI-derived assets (C1.1)
- Personal information lifecycle documentation for AI assets (P4.1)
- Retention schedule and deletion procedure documentation (CC5.2)
- Asset inventory including derived GenAI data assets (CC3.2)
- Data flow maps showing classification propagation

**Hardening**
- Implement automated classification propagation — C1.1
  and P4.1 technical enforcement evidence
- Document machine unlearning readiness — P7.1 personal
  information disposal capability evidence

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI01 Sensitive Data Leakage
- Other frameworks: ISO 27001 A.5.9/A.8.10 · EU AI Act Art. 10 · ISO 27701

---

### DSGAI08 — Non-Compliance and Regulatory Violations

**Severity:** High

GenAI systems trigger regulatory obligations without organisations
recognising they are in scope. SOC 2 CC5 (control activities —
compliance procedures) and CC3 (risk assessment — regulatory risks
identified) are the primary criteria. Privacy (P1) applies where
personal data regulatory obligations are implicated.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC5.1 — Control environment | Commitment to compliance with applicable laws and regulations including AI-specific obligations |
| CC3.2 — Risk assessment | Regulatory risks identified in GenAI risk assessment — GDPR, EU AI Act, sector-specific regulations |
| P1.1 — Privacy management | Privacy programme covers GenAI processing of personal information — policies, notices, accountability |
| CC2.1 — Communication | Regulatory compliance status communicated to management — AI Act obligations, NIS2 requirements |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC3.2: Include regulatory risks in GenAI risk assessment —
  GDPR, EU AI Act, NIS2, HIPAA, sector-specific obligations
  — documented, owned, treated
- P1.1: Extend privacy programme to cover GenAI processing —
  notices, lawful basis documentation, data subject
  rights procedures for AI-processed data
- CC5.1: Document commitment to AI regulatory compliance —
  board or senior management statement, ownership assigned

**Audit evidence preparation**
- Regulatory risk assessment entries for GenAI (CC3.2)
- Privacy programme documentation covering GenAI (P1.1)
- Compliance monitoring records (CC4.1, CC5.1)
- EU AI Act readiness assessment if applicable (CC3.2)
- Regulatory incident response procedures (CC7.3)

**Hardening**
- Implement automated compliance monitoring — CC4.1
  ongoing monitoring of compliance controls evidence
- EU AI Act August 2026 gap assessment — CC3.2 forward-
  looking risk assessment evidence

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance
- Other frameworks: EU AI Act Art. 10/17 · ISO 27001 A.5.31 · GDPR Art. 5/25/30

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Multimodal AI systems process sensitive visual and audio data —
OCR and transcription extract content that is treated as less
sensitive than the original. SOC 2 C2 (confidential information
protection — derived content inherits source classification) and P5
(personal information use — extracted content subject to same
privacy obligations) are the primary criteria.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C2.1 — Confidential information protection | Multimodal derived content (OCR output, transcripts) protected at same level as source uploads |
| P5.1 — Personal information use | Personal information extracted from multimodal inputs subject to same use restrictions as source data |
| CC6.1 — Logical access | Access controls on multimodal content stores — same rigour as equivalent text data stores |
| CC7.2 — Anomaly detection | DLP monitoring on multimodal extraction pipelines — PII in OCR output and transcripts detected |

#### Mitigations for SOC 2 evidence

**Control implementation**
- C2.1: Document that derived content from multimodal
  inputs inherits source classification — OCR output
  of a confidential document is equally confidential
- CC7.2: Deploy DLP monitoring on multimodal extraction
  pipelines — alert configuration and samples for auditors
- P5.1: Document that personal information use restrictions
  apply to extracted content, not only source uploads

**Audit evidence preparation**
- Multimodal data classification policy documentation (C2.1)
- Access controls on multimodal content stores (CC6.1)
- DLP monitoring configuration for multimodal pipelines (CC7.2)
- Retention procedures for multimodal derived content (P4.1)

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI14 Telemetry Leakage
- Other frameworks: ISO 27001 A.8.11/A.8.12 · GDPR Art. 9

---

### DSGAI10 — Synthetic Data and Anonymisation Pitfalls

**Severity:** Medium

Synthetic data and anonymisation that fails the legal standard of
anonymisation creates undisclosed personal data obligations. SOC 2
Privacy (P4, P5) are the primary criteria — if synthetic data is
not truly anonymous under applicable law, privacy obligations
continue to apply.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| P4.2 — Retention of personal information | Synthetic datasets that are not truly anonymous subject to same retention obligations as source personal data |
| P5.1 — Personal information use | Synthetic data use must respect underlying privacy commitments if re-identification risk exists |
| CC3.2 — Risk assessment | Re-identification risk in synthetic datasets identified in risk assessment |
| C2.1 — Confidential information protection | Synthetic OT data and business data protected at source classification level until re-identification risk formally assessed |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC3.2: Include re-identification risk in GenAI risk
  assessment — synthetic datasets assessed before use
  or release, risk acceptance documented
- P4.2/P5.1: Document privacy obligations for synthetic
  datasets — classification based on re-identification
  risk, not assumed to be non-personal
- Conduct formal re-identification risk assessment —
  results documented as CC3.2 and P4.2 evidence

**Audit evidence preparation**
- Re-identification risk assessment records (CC3.2)
- Synthetic data governance policy (CC5.2)
- Privacy documentation for synthetic datasets (P4.2, P5.1)
- Differential privacy configuration and budget records (C2.1)

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI18 Inference and Data Reconstruction
- Other frameworks: ISO 27001 A.5.34 · GDPR Recital 26 · EU AI Act Art. 10

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High

One user's session context leaks into another user's responses.
SOC 2 CC6 (logical access — session isolation) and C2
(confidentiality protection — user context is confidential
information) are the primary criteria. P5 (personal information
use — cross-user context leakage is a privacy violation) also
applies where personal data is involved.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC6.1 — Logical access | Strict session isolation — each user's context inaccessible to all other sessions |
| C2.1 — Confidential information protection | User session context classified as confidential — technical isolation controls |
| P5.1 — Personal information use | Personal information in user sessions used only for that user's authorised purposes — cross-session leakage is a P5 violation |
| CC7.2 — Anomaly detection | Cross-session access anomalies monitored — unusual retrieval patterns detected |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC6.1: Document and implement session isolation controls —
  per-user RAG namespaces, KV cache isolation, configuration
  evidence for auditors
- C2.1: Document user session context as confidential —
  technical protection controls for session data
- CC7.2: Implement cross-session anomaly monitoring —
  alert configuration and samples as monitoring evidence

**Audit evidence preparation**
- Session isolation configuration documentation (CC6.1)
- User context classification and protection evidence (C2.1)
- Cross-session monitoring configuration (CC7.2)
- Security testing results for multi-tenant isolation (CC7.4)

**Hardening**
- CC7.4: Conduct adversarial cross-tenant testing — results
  documented as security testing evidence
- Cryptographic session isolation — CC6.1 advanced
  technical access control evidence

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3 · GDPR Art. 32 · NIST AI RMF MS-2.5

---

### DSGAI12 — Unsafe Natural-Language Data Gateways

**Severity:** Critical

LLM-to-SQL and LLM-to-SCADA interfaces collapse the security boundary
between user input and data/process systems. SOC 2 CC6 (logical
access — least privilege on NL gateway queries) and PI1 (processing
integrity — LLM-generated queries are system processing that must
be authorised) are the primary criteria.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC6.1 — Logical access | LLM-generated queries execute under requesting user's permissions — least privilege, no shared high-privilege accounts |
| PI1.1 — Processing integrity policy | Policy requiring LLM-generated queries to be validated before execution — only authorised processing permitted |
| PI1.3 — Outputs complete and accurate | LLM-generated query results validated — destructive or over-broad queries blocked before execution |
| CC7.2 — Anomaly detection | LLM-generated query anomaly monitoring — bulk extraction, unusual patterns, out-of-scope queries alerted |
| CC5.2 — Control activities | Query allowlisting and human confirmation procedures documented |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC6.1: Document and implement per-user query execution —
  LLM queries execute under requesting user's permissions,
  access control configuration for auditors
- PI1.1: Document processing integrity policy for NL
  gateways — what constitutes authorised query processing,
  validation requirements
- CC5.2: Document query allowlisting and human confirmation
  procedures — implemented, tested, and reviewed

**Audit evidence preparation**
- Query execution access control configuration (CC6.1)
- Processing integrity policy for NL gateways (PI1.1)
- Query allowlisting procedure documentation (CC5.2)
- Query audit logs with user identity (CC7.2)
- Security testing results for NL gateway injection (CC7.4)

**Hardening**
- CC7.4: Include SQL injection and bulk extraction in
  security testing — documented results as audit evidence
- CC7.2: Implement query anomaly detection — alert
  configuration and samples for auditors

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- Other frameworks: ISO 27001 A.8.26/A.8.28 · OWASP ASVS V4.1 · CWE-89

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector databases store sensitive embeddings with weaker default
security than traditional databases. SOC 2 C2 (confidentiality
protection — embeddings of confidential data protected) and CC6
(logical access — RBAC on vector stores) are the primary criteria.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C2.1 — Confidential information protection | Vector store content encrypted at rest — embeddings of confidential data protected |
| CC6.1 — Logical access | RBAC on all vector store collections — no unauthenticated access |
| CC8.1 — Change management | Vector database CVE patching managed through change management — timely remediation documented |
| CC7.2 — Anomaly detection | Vector store query anomaly monitoring — bulk extraction patterns detected |

#### Mitigations for SOC 2 evidence

**Control implementation**
- C2.1: Document vector store encryption and classification —
  embeddings protected at same level as source content
- CC6.1: Implement and document RBAC on all vector stores —
  access control configuration for auditors, access logs
- CC8.1: Include vector database CVE patching in change
  management — timely remediation records

**Audit evidence preparation**
- Vector store encryption configuration (C2.1)
- RBAC configuration and access records (CC6.1)
- CVE patching records for vector databases (CC8.1)
- Query anomaly monitoring configuration (CC7.2)
- Penetration testing results for vector stores (CC7.4)

**Hardening**
- CC7.4: Conduct vector store penetration testing — RBAC
  bypass and bulk extraction scenarios documented as evidence

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses
- Agentic Top 10: ASI06 Memory and Context Poisoning
- Other frameworks: ISO 27001 A.8.3/A.8.24 · NIST AI RMF MS-2.5

---

### DSGAI14 — Excessive Telemetry and Monitoring Leakage

**Severity:** High

Observability pipelines capture sensitive content with weaker
controls than production data. SOC 2 C2 (confidentiality protection —
telemetry data classified and protected) and P5 (personal information
use — telemetry containing personal data subject to privacy
obligations) are the primary criteria.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C2.1 — Confidential information protection | GenAI telemetry classified and encrypted — content captured in traces protected at same level as source data |
| P5.1 — Personal information use | Personal information in telemetry used only for authorised purposes — same restrictions as production data |
| CC6.1 — Logical access | Access controls on telemetry stores — same rigour as production data stores |
| CC7.2 — Monitoring | Access anomaly monitoring on telemetry stores — bulk access patterns detected |

#### Mitigations for SOC 2 evidence

**Control implementation**
- C2.1: Classify telemetry data at same level as most
  sensitive content it contains — encryption at rest,
  access controls documented
- P5.1: Document personal information handling in
  telemetry — use restrictions, retention limits, deletion
- CC6.1: Implement equivalent access controls on telemetry
  stores as production data — access records for auditors

**Audit evidence preparation**
- Telemetry classification and protection documentation (C2.1)
- Access controls on telemetry stores (CC6.1)
- Retention and deletion procedures for telemetry (P4.2)
- Least-logging configuration evidence (CC5.2)

**Hardening**
- Implement PII redaction in telemetry pipelines — C2.1
  and P5.1 technical protection evidence
- Short TTL for debug traces — P4.2 retention control evidence

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance
- Other frameworks: ISO 27001 A.8.15 · GDPR Art. 32 · ISO 27701

---

### DSGAI15 — Over-Broad Context Windows and Prompt Over-Sharing

**Severity:** High

Excessive context injection aggregates data from multiple trust
domains amplifying injection impact. SOC 2 CC6 (logical access —
context assembly respects access boundaries) and C2 (confidentiality
protection — context classification ceiling) are the primary criteria.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC6.1 — Logical access | Context window assembly respects user authorisation — no content from higher classification tier than user's access level |
| C2.1 — Confidential information protection | Highest classification in context window drives handling — response treated as confidential if context contains confidential data |
| CC5.2 — Control activities | Minimum-necessary context injection procedures — documented and enforced |
| CC3.2 — Risk assessment | Over-broad context risks identified — cross-trust-domain aggregation assessed |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC6.1: Document context assembly access controls —
  users cannot receive context from sources above their
  authorisation level, verified in access control records
- C2.1: Document context classification ceiling policy —
  response handling requirements when context contains
  confidential data
- CC5.2: Document minimum-necessary context injection
  procedure — implemented and tested

**Audit evidence preparation**
- Context assembly access control documentation (CC6.1)
- Context classification ceiling policy (C2.1)
- Context injection procedure documentation (CC5.2)
- Risk assessment entries for over-broad context (CC3.2)

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- Agentic Top 10: ASI01 Agent Goal Hijack
- Other frameworks: AIUC-1 A/B005 · NIST AI RMF MS-2.5

---

### DSGAI16 — Endpoint and Browser Assistant Overreach

**Severity:** High

Browser AI assistants access sensitive data beyond task scope.
SOC 2 CC6 (logical access — approved assistant permission scope)
and CC9 (vendor risk — browser AI providers as vendors) are the
primary criteria.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC6.1 — Logical access | Approved AI assistants with scoped permissions — permission minimisation documented and enforced |
| CC9.1 — Vendor risk | Browser AI extension providers assessed in vendor risk programme — data handling, telemetry, update security |
| CC5.2 — Control activities | Endpoint AI acceptable use procedures — approved extension list, prohibited data access, employee acknowledgement |
| CC3.2 — Risk assessment | Endpoint AI overreach risks identified — data access scope, exfiltration paths assessed |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC9.1: Include browser AI extension vendors in vendor
  risk programme — security assessments, data handling
  review, assessment records
- CC6.1: Document approved extension list with permission
  scope — access control configuration evidence
- CC5.2: Document endpoint AI acceptable use procedures —
  employee acknowledgement records

**Audit evidence preparation**
- Approved extension list with vendor assessments (CC9.1)
- Extension permission configuration (CC6.1)
- Acceptable use procedure and acknowledgement records (CC5.2)
- DLP configuration for endpoint AI traffic (CC7.2)

#### Cross-references
- Agentic Top 10: ASI10 Rogue Agents
- DSGAI 2026: DSGAI03 Shadow AI
- Other frameworks: ISO 27001 A.8.1/A.8.7 · EU AI Act Art. 9

---

### DSGAI17 — Data Availability and Resilience Failures

**Severity:** High

RAG pipelines fail silently producing stale or incorrect information.
SOC 2 Availability (A1) is the primary criterion — availability
commitments extend to the accuracy and currency of AI-generated
responses, not just uptime.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| A1.1 — Availability policy | LLM service availability commitments cover RAG freshness — stale data producing misinformation is an availability failure |
| A1.2 — Environmental protections | Circuit breakers and freshness monitoring protect availability commitments — graceful degradation over silent failure |
| CC7.2 — Anomaly detection | RAG freshness monitoring — alert when index staleness exceeds threshold before misinformation reaches users |
| CC3.2 — Risk assessment | Silent RAG degradation identified as availability risk in assessment |

#### Mitigations for SOC 2 evidence

**Control implementation**
- A1.1: Document availability commitments covering RAG
  freshness — stale index producing misinformation is an
  availability commitment breach, policy documented
- A1.2: Implement and document circuit breakers and
  freshness monitoring — configuration evidence showing
  graceful degradation rather than silent failure
- CC7.2: RAG freshness monitoring — alert configuration
  and sample alerts for auditors

**Audit evidence preparation**
- Availability policy covering RAG freshness (A1.1)
- Circuit breaker and freshness monitoring configuration (A1.2)
- BCP coverage for GenAI pipeline failures (A1.2)
- Availability monitoring and alert records (CC7.2)
- RTO/RPO documentation for GenAI services (A1.1)

**Hardening**
- A1.2: Test BCP for GenAI pipeline failures — drill
  records demonstrating availability control effectiveness
- A1.2: Deploy redundancy for production RAG — configuration
  evidence of environmental availability protection

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: ISA/IEC 62443 SR 7.6 (OT) · NIST SP 800-82 (OT) · AIUC-1 D

---

### DSGAI18 — Inference and Data Reconstruction

**Severity:** High

Adversaries reconstruct sensitive data through membership inference
and model inversion. SOC 2 C2 (confidentiality protection) and P5
(personal information use restrictions — inference attacks use
model outputs in ways beyond authorised purposes) are the primary
criteria.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C2.1 — Confidential information protection | Inference attack resistance as confidentiality protection — technical measures limiting reconstruction success |
| P5.1 — Personal information use | Using model outputs to reconstruct personal information beyond authorised purposes is a P5 violation |
| CC7.2 — Anomaly detection | Output monitoring for reconstruction indicators — systematic query patterns detected |
| CC3.2 — Risk assessment | Inference attack risks identified in GenAI risk assessment — membership inference, model inversion vectors |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC3.2: Include inference attack risks in GenAI risk
  assessment — membership inference and model inversion
  as documented threat vectors
- C2.1: Document technical inference attack resistance
  measures — differential privacy, confidence score
  suppression, rate limiting as technical control evidence
- CC7.2: Implement systematic query pattern monitoring —
  extraction and inference attack patterns detected

**Audit evidence preparation**
- Risk assessment entries for inference attacks (CC3.2)
- Differential privacy configuration and privacy budget (C2.1)
- Output rate limiting configuration (A1.2)
- Query pattern monitoring configuration (CC7.2)
- Security testing results for inference attacks (CC7.4)

**Hardening**
- CC7.4: Conduct membership inference red team — results
  documented as security testing evidence
- C2.1: Apply differential privacy in training — technical
  confidentiality protection evidence

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI10 Synthetic Data Pitfalls
- Other frameworks: ISO 27001 A.8.11 · GDPR Art. 25 · EU AI Act Art. 10

---

### DSGAI19 — Human-in-Loop and Labeler Overexposure

**Severity:** Medium

Human annotators access sensitive model inputs during labelling.
SOC 2 CC9 (vendor risk — labelling vendors as third parties with
data access) and Privacy (P3 — personal information collection
by labellers, P5 — use restrictions applying to labelled data)
are the primary criteria.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| CC9.1 — Vendor risk | Labelling vendors assessed in vendor risk programme — data access scope, handling requirements, sub-processor chain |
| CC9.2 — Vendor agreements | Contractual data handling obligations for labelling vendors — data minimisation, retention, permitted use |
| P3.1 — Personal information collection | Personal information accessed by labellers documented — purpose, scope, and safeguards |
| P5.1 — Personal information use | Labelling vendor use of personal information restricted — no secondary use, training, or retention beyond task |

#### Mitigations for SOC 2 evidence

**Control implementation**
- CC9.1: Include labelling vendors in vendor risk programme —
  security assessment, data access scope review, records
- CC9.2: Establish vendor agreements with data handling
  obligations — data minimisation, retention limits, no
  secondary use, incident notification
- P3.1/P5.1: Document personal information handling in
  labelling workflows — collection purpose, use restrictions,
  safeguards applied

**Audit evidence preparation**
- Labelling vendor assessment records (CC9.1)
- Vendor agreements with data handling obligations (CC9.2)
- Personal information handling documentation for labelling (P3.1)
- Data minimisation procedure for labelling tasks (CC5.2)

**Hardening**
- Anonymise labelling tasks — C2.1 and P3.1 minimisation
  evidence showing technical data protection in labelling
- CC9.2: Right-to-audit provision for labelling vendors —
  contractual control evidence

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.34/A.6.3 · EU AI Act Art. 10 · GDPR Art. 28

---

### DSGAI20 — Model Exfiltration and IP Replication

**Severity:** High

Adversaries reconstruct a functional model replica through systematic
querying. SOC 2 C2 (confidentiality protection — model IP as
confidential information) and CC6 (logical access — API rate
limiting as access control) are the primary criteria.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| C2.1 — Confidential information protection | Proprietary model artifacts classified as confidential — access controls, rate limiting, extraction detection |
| CC6.1 — Logical access | API rate limiting as access control limiting systematic model extraction |
| CC7.2 — Anomaly detection | Model extraction pattern monitoring — unusual query diversity and volume detected |
| CC3.2 — Risk assessment | Model extraction risks identified in risk assessment — extraction vectors, IP exposure assessed |

#### Mitigations for SOC 2 evidence

**Control implementation**
- C2.1: Document proprietary model artifact classification —
  model IP protection policy, access controls, rate
  limiting as technical protection evidence
- CC6.1: Implement and document API rate limiting —
  access control configuration showing systematic
  extraction prevention
- CC7.2: Deploy extraction pattern monitoring — alert
  configuration and samples for auditors

**Audit evidence preparation**
- Model IP classification and protection policy (C2.1)
- API rate limiting configuration (CC6.1)
- Extraction pattern monitoring configuration (CC7.2)
- Risk assessment entries for model extraction (CC3.2)
- Security testing results for extraction resistance (CC7.4)

**Hardening**
- Implement model watermarking — C2.1 advanced technical
  protection evidence enabling replicated model detection
- CC7.4: Conduct model extraction red team — attempt
  replication and document query budget required

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference and Data Reconstruction
- Other frameworks: ISO 27001 A.5.12/A.8.3 · MITRE ATLAS AML.T0016

---

### DSGAI21 — Disinformation and Integrity Attacks via Data Poisoning

**Severity:** High

Adversaries inject false content into RAG corpora causing AI systems
to surface it as authoritative. SOC 2 Processing Integrity (PI1)
is the primary criterion — RAG retrieval is a processing function
and injected false content represents a PI failure. CC9 (vendor risk —
RAG data source providers as vendors) also applies.

#### SOC 2 criteria mapping

| Criteria | How it applies |
|---|---|
| PI1.2 — System inputs complete and accurate | RAG corpus integrity controls — only accurate, verified content enters the retrieval index |
| PI1.3 — Outputs complete and accurate | LLM outputs derived from poisoned RAG are a processing integrity failure — detection before delivery |
| CC9.1 — Vendor risk | RAG corpus data source providers assessed — content quality, update process, integrity guarantees |
| CC7.2 — Anomaly detection | RAG corpus anomaly detection — unusual content or modifications detected before reaching production |

#### Mitigations for SOC 2 evidence

**Control implementation**
- PI1.2: Document RAG corpus integrity controls —
  source trust tiering, content hashing, ingestion
  validation as processing integrity evidence
- CC9.1: Include RAG data source providers in vendor
  risk programme — content quality and integrity
  assessment, records retained
- CC7.2: Deploy RAG corpus monitoring — alert configuration
  and sample findings for auditors

**Audit evidence preparation**
- RAG corpus integrity procedure documentation (PI1.2)
- Source trust tiering configuration (PI1.2)
- Vendor assessment records for data source providers (CC9.1)
- Ingestion anomaly monitoring configuration (CC7.2)
- Incident response procedure for RAG poisoning (CC7.3)

**Hardening**
- Implement cryptographic provenance for RAG corpus —
  PI1.2 advanced processing integrity evidence
- CC7.4: Conduct adversarial RAG integrity testing —
  attempt injection via documentation sources, results
  documented as security testing evidence

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory and Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0045 · ISO 27001 A.5.7 · EU AI Act Art. 55(1)(a)

---

## SOC 2 audit preparation checklist for GenAI data security

### Risk management (CC3)

- [ ] All 21 DSGAI risks assessed in GenAI risk register
- [ ] Poisoning, shadow AI, and inference attack risks documented
- [ ] Re-identification risk in synthetic datasets assessed
- [ ] Model extraction and IP replication risks assessed
- [ ] Regulatory risks (GDPR, EU AI Act) documented

### Control activities (CC5)

- [ ] Data classification procedures covering GenAI-derived assets
- [ ] Context minimisation procedures for tool and RAG calls
- [ ] Least-logging defaults documented for GenAI telemetry
- [ ] Query allowlisting procedures for NL data gateways
- [ ] AI acceptable use procedures covering shadow AI

### Logical access (CC6)

- [ ] RBAC on all vector stores and RAG data sources
- [ ] Session isolation for multi-user GenAI deployments
- [ ] Agent credentials managed as privileged access
- [ ] Context assembly respects user authorisation levels
- [ ] API rate limiting protecting against model extraction

### Monitoring (CC7)

- [ ] DLP monitoring on all GenAI output channels
- [ ] RAG corpus integrity and freshness monitoring
- [ ] Agent credential anomaly detection in SIEM
- [ ] Query anomaly detection for NL gateways
- [ ] Telemetry access monitoring active
- [ ] Security testing covering key DSGAI entries

### Vendor risk (CC9)

- [ ] Tool and plugin providers in vendor risk programme
- [ ] Training data providers assessed
- [ ] Labelling vendors in vendor risk programme
- [ ] RAG data source providers assessed
- [ ] Browser AI extension vendors assessed

### Confidentiality and privacy (C, P)

- [ ] Confidentiality policy covers all GenAI-derived assets
- [ ] Embeddings of confidential data classified and protected
- [ ] Personal information lifecycle covers GenAI scope
- [ ] Multimodal derived content classified at source level
- [ ] Synthetic data re-identification risk assessed

### Availability (A)

- [ ] Availability commitments cover RAG freshness
- [ ] Circuit breakers and graceful degradation implemented
- [ ] BCP coverage for GenAI pipeline failures documented

### Processing integrity (PI)

- [ ] Ingestion validation documented as processing integrity control
- [ ] NL gateway query validation as PI control
- [ ] RAG corpus integrity controls as PI evidence

---

## Implementation priority

| Phase | DSGAI entries | SOC 2 criteria | Rationale |
|---|---|---|---|
| 1 — Audit readiness | DSGAI01, DSGAI02, DSGAI03 | C1/C2, CC6, CC9 | Data classification, access control, and vendor risk are first auditor asks |
| 2 — This sprint | DSGAI07, DSGAI08, DSGAI17 | P4, CC5, A1 | Data governance, compliance documentation, and availability commitments |
| 3 — This quarter | DSGAI04, DSGAI05, DSGAI21 | CC8, PI1, CC9 | Change management, processing integrity, and source trust controls |
| 4 — Ongoing | DSGAI09-DSGAI16, DSGAI18-DSGAI20 | C2/P5, CC7 | Privacy, advanced monitoring, and IP protection hardening |

---

## References

- AICPA SOC 2 Trust Services Criteria: https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services
- AICPA Trust Services Criteria 2017 (updated 2022): https://us.aicpa.org/content/dam/aicpa/interestareas/frc/assuranceadvisoryservices/downloadabledocuments/trust-services-criteria.pdf
- OWASP GenAI Data Security Risks 2026: https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/
- LLM Top 10 x SOC 2 mapping: see LLM_SOC2.md in this repository

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-25 | 2026-Q1 | Initial mapping — DSGAI01-DSGAI21 full entries with SOC 2 audit preparation checklist | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the GenAI Security Crosswalk: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk
