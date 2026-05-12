<!--
  GenAI Security Crosswalk
  Source list : OWASP GenAI Data Security Risks and Mitigations 2026 (DSGAI01-DSGAI21)
  Framework   : NIST Cybersecurity Framework 2.0 (CSF 2.0)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × NIST CSF 2.0

Mapping the [OWASP GenAI Data Security Risks and Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to the [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework).

The DSGAI taxonomy follows sensitive data through the full GenAI
system lifecycle. CSF 2.0 provides the organisational control
structure to govern, identify, protect, detect, respond to, and
recover from data security failures across that lifecycle. The
new GOVERN function in CSF 2.0 is the critical addition for GenAI
data security — data governance policy, supply chain oversight,
and acceptable use requirements are GOVERN responsibilities.

---

## Quick-reference summary

| ID | Name | Severity | Primary CSF 2.0 Categories | Tier |
|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | PR.DS-01, PR.DS-02, DE.CM-01, GV.RM-06 | Foundational–Advanced |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | PR.AA-01, PR.AA-05, DE.CM-01, GV.RM-06 | Foundational–Advanced |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | GV.OC-01, PR.AT-01, DE.CM-09, GV.SC-01 | Foundational–Hardening |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | PR.DS-01, DE.CM-09, RS.AN-03, GV.SC-01 | Hardening–Advanced |
| DSGAI05 | Data Integrity & Validation Failures | High | PR.PS-04, PR.DS-01, DE.CM-09, ID.RA-01 | Foundational–Hardening |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | GV.SC-01, PR.AA-05, DE.CM-01, ID.AM-08 | Foundational–Hardening |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | GV.OC-01, ID.AM-08, PR.DS-01, DE.CM-09 | Foundational–Advanced |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | GV.OC-01, GV.RM-01, ID.RA-01, RS.CO-03 | Foundational–Advanced |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | PR.DS-01, PR.DS-02, DE.CM-01, ID.AM-08 | Hardening–Advanced |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | GV.RM-06, ID.RA-01, PR.DS-01, DE.CM-09 | Hardening–Advanced |
| DSGAI11 | Cross-Context Conversation Bleed | High | PR.AA-05, PR.DS-01, DE.CM-01, ID.RA-01 | Foundational–Hardening |
| DSGAI12 | Unsafe NL Data Gateways | Critical | PR.AA-05, PR.PS-04, DE.CM-01, ID.RA-01 | Foundational–Advanced |
| DSGAI13 | Vector Store Platform Security | High | PR.DS-01, PR.AA-05, PR.PS-02, DE.CM-09 | Foundational–Hardening |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | GV.OC-01, PR.DS-01, PR.AA-05, DE.CM-09 | Foundational–Hardening |
| DSGAI15 | Over-Broad Context Windows | High | PR.AA-05, PR.DS-01, DE.CM-01, ID.RA-01 | Foundational–Hardening |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | GV.SC-01, PR.PS-02, DE.CM-01, ID.AM-08 | Foundational–Hardening |
| DSGAI17 | Data Availability & Resilience Failures | High | PR.IR-01, DE.CM-01, RS.MI-01, RC.RP-01 | Foundational–Advanced |
| DSGAI18 | Inference & Data Reconstruction | High | PR.DS-01, DE.CM-09, ID.RA-01, GV.RM-06 | Hardening–Advanced |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | GV.SC-01, PR.AA-05, GV.OC-01, PR.AT-01 | Foundational–Hardening |
| DSGAI20 | Model Exfiltration & IP Replication | High | PR.AA-05, DE.CM-01, DE.CM-09, ID.RA-01 | Hardening–Advanced |
| DSGAI21 | Disinformation via Data Poisoning | High | GV.SC-01, DE.CM-09, RS.AN-03, PR.DS-01 | Hardening–Advanced |

---

## Audience tags

- **CISO / governance** — full file, CSF 2.0 integration for GenAI data security programme
- **Data governance lead** — DSGAI07, DSGAI08, DSGAI10 entries
- **Risk manager** — GOVERN and IDENTIFY entries throughout
- **Security operations** — DETECT and RESPOND entries throughout
- **Federal agency / FISMA** — CSF 2.0 as NIST reference framework

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

Sensitive data leaks through GenAI outputs, RAG retrieval, embedding
exposure, or observability pipelines. CSF 2.0 data security (PR.DS)
and continuous monitoring (DE.CM) are the primary categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Data Security | PR.DS-01 | PROTECT | Sensitive data at rest protected — training data, embeddings, RAG stores, prompt caches encrypted |
| Data Security | PR.DS-02 | PROTECT | Sensitive data in transit protected — all GenAI API calls and RAG retrieval paths encrypted |
| Continuous Monitoring | DE.CM-01 | DETECT | Networks and assets monitored — DLP on all GenAI output channels |
| Risk Management Strategy | GV.RM-06 | GOVERN | Risk tolerance established — acceptable sensitive data disclosure risk defined per GenAI use case |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-06: Establish risk tolerance for sensitive data
  disclosure per GenAI use case — document acceptable
  classification levels in LLM scope
- GV.OC-01: Data classification policy extended to all
  GenAI data assets — training data, embeddings, outputs

**IDENTIFY**
- ID.AM-08: Inventory all data assets in GenAI scope —
  training corpora, RAG sources, embedding stores,
  prompt caches, observability logs

**PROTECT**
- PR.DS-01: Encrypt all sensitive data at rest in GenAI
  scope — embedding stores, training datasets, RAG stores
- PR.DS-02: Encrypt all GenAI data flows in transit —
  TLS 1.2 minimum on all API calls and retrieval paths
- PR.AA-05: Least-privilege retrieval — users access
  only data they are authorised to retrieve via GenAI

**DETECT**
- DE.CM-01: DLP on all GenAI output channels —
  sensitive patterns detected before delivery to users

**RESPOND**
- RS.AN-03: Investigate disclosure incidents — scope,
  affected data subjects, regulatory reporting obligations
- RS.CO-03: Report incidents as required — breach
  notification per applicable regulation

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.11/A.8.12 · NIST AI RMF GV-1.6 · EU AI Act Art. 10

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical

AI agents inherit and cache credentials that attackers exploit for
lateral movement. CSF 2.0 identity management (PR.AA) governs the
NHI lifecycle that determines how exposed agent credentials are.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Identity Management, Authentication & Access Control | PR.AA-01 | PROTECT | Identities and credentials managed — NHI inventory, lifecycle, short-lived JIT issuance |
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Access permissions managed — agent credential scope enforced at minimum required |
| Continuous Monitoring | DE.CM-01 | DETECT | Credential usage monitored — anomalous access patterns, lateral movement detected |
| Risk Management Strategy | GV.RM-06 | GOVERN | Agent credential exposure in risk register — blast radius per deployment documented |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-06: Include NHI exposure in risk register —
  credential scope, TTL, rotation programme, blast
  radius documented per agent deployment

**IDENTIFY**
- ID.AM-08: Inventory all agent NHIs — permissions,
  TTL, rotation schedule, associated systems documented

**PROTECT**
- PR.AA-01: Short-lived JIT credentials per agent
  session — no long-lived tokens, automatic expiry
- PR.AA-05: Least privilege per agent — minimum scope,
  reviewed quarterly, no shared credentials
- PR.DS-01: Credentials stored encrypted — secret
  manager, no cleartext in config or agent memory

**DETECT**
- DE.CM-01: Monitor credential usage continuously —
  anomalous access scope or lateral movement alerted

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: OWASP NHI Top 10 · ISO 27001 A.8.2 · AIUC-1 A/B007

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High

Employees use unapproved GenAI tools outside formal governance,
creating ungoverned data flows. CSF 2.0 GOVERN and awareness
training (PR.AT) are the primary categories.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Organisational Context | GV.OC-01 | GOVERN | Acceptable use policy for AI tools — approved list, prohibited use cases, data handling requirements |
| Awareness and Training | PR.AT-01 | PROTECT | Users trained on shadow AI risk — policy awareness, prohibited tool use, reporting obligations |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for use of unauthorised software — shadow AI tool usage detected on endpoints and network |
| Supply Chain Risk Management | GV.SC-01 | GOVERN | All approved AI tools managed as suppliers — TPSP assessment, contractual obligations |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Publish and enforce AI acceptable use
  policy — approved tools, prohibited use cases, data
  handling requirements, consequences for violations
- GV.SC-01: Treat all approved AI SaaS tools as third-party
  suppliers — security assessment before approval, contracts
  with data handling obligations

**PROTECT**
- PR.AT-01: Train all employees on shadow AI risk —
  what data must not be used with unapproved tools,
  how to request tool approval

**DETECT**
- DE.CM-09: Monitor for shadow AI usage — DLP on
  known AI SaaS endpoints, endpoint monitoring,
  network egress analysis

**RESPOND**
- RS.AN-03: Investigate shadow AI incidents — what data
  was exposed, which vendor received it, regulatory
  notification if personal data involved

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.10/A.5.23 · EU AI Act Art. 25 · CIS Controls CIS 14

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical

Training data, model weights, or RAG corpora corrupted with
backdoors. CSF 2.0 supply chain (GV.SC) and data security
(PR.DS) govern the pipeline integrity controls.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Supply Chain Risk Management | GV.SC-01 | GOVERN | Training data providers treated as suppliers — provenance, quality, integrity requirements in contracts |
| Data Security | PR.DS-01 | PROTECT | Training data protected at rest — integrity verification, source allowlisting, provenance tracking |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for unauthorised software — model integrity verification at deployment, output anomaly detection |
| Incident Analysis | RS.AN-03 | RESPOND | Poisoning incidents analysed — affected training runs, deployed models, downstream impact assessed |

#### Mitigations by CSF function

**GOVERN**
- GV.SC-01: Apply supply chain programme to training
  data sources — provenance guarantees, quality
  attestation, incident notification requirements

**PROTECT**
- PR.DS-01: Implement training data integrity controls —
  hash-based provenance, source allowlisting, anomaly
  detection on data distributions before training
- Model rollback capability — clean checkpoint always
  available for immediate revert

**DETECT**
- DE.CM-09: Model integrity verification at each
  deployment — hash check against approved baseline,
  production output anomaly monitoring

**RESPOND**
- RS.AN-03: Investigate poisoning — affected deployments,
  downstream impact, physical or operational consequences
- RS.MI-02: Rollback to clean checkpoint, quarantine
  affected training data sources

#### Cross-references
- LLM Top 10: LLM03 Supply Chain, LLM04 Data & Model Poisoning
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · ISO 27001 A.8.27 · MITRE ATLAS AML.T0032

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High

Adversarially crafted payloads corrupt GenAI data pipelines or
exploit ingestion vulnerabilities (CVE-2024-3584 class). CSF 2.0
platform security (PR.PS) governs secure development requirements
for ingestion code.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Platform Security | PR.PS-04 | PROTECT | Secure software development — multi-stage validation, path traversal prevention in ingestion code |
| Data Security | PR.DS-01 | PROTECT | Data at rest integrity — snapshot import operations sandboxed, path traversal blocked |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for anomalous data — unusual ingestion patterns, schema violations detected |
| Risk Assessment | ID.RA-01 | IDENTIFY | Ingestion interface vulnerabilities documented in risk assessment — CVE-2024-3584 class |

#### Mitigations by CSF function

**IDENTIFY**
- ID.RA-01: Document ingestion integrity risks in risk
  assessment — all ingestion interfaces identified,
  CVE-2024-3584 class as urgent findings

**PROTECT**
- PR.PS-04: Multi-stage validation at all ingestion
  boundaries — schema, semantic, path traversal
  prevention as secure development requirements
- PR.PS-02: Patch all known vector database CVEs —
  CVE-2024-3584 class treated as urgent

**DETECT**
- DE.CM-09: Monitor ingestion pipelines for anomalous
  payloads — unusual encoding, schema violations alerted

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-20 · OWASP ASVS V5

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange

**Severity:** High

AI tools and MCP servers receive full context payloads with no data
minimisation. CSF 2.0 supply chain (GV.SC) governs third-party tool
data handling obligations.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Supply Chain Risk Management | GV.SC-01 | GOVERN | Tool and plugin providers treated as suppliers — data handling requirements in contracts |
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Context minimisation — tools receive minimum required payload, not full context history |
| Continuous Monitoring | DE.CM-01 | DETECT | All tool API calls monitored — DLP on outbound tool payloads |
| Asset Management | ID.AM-08 | IDENTIFY | All tool integrations inventoried — data received, retained, training use, security assessment status |

#### Mitigations by CSF function

**GOVERN**
- GV.SC-01: Treat all tool and plugin providers as
  third-party suppliers — security assessment before
  approval, contracts with data handling obligations,
  zero training use by default

**IDENTIFY**
- ID.AM-08: Inventory all tool integrations — what data
  each receives, whether it is retained, sub-processor
  chain, security assessment status

**PROTECT**
- PR.AA-05: Implement context minimisation — tools
  receive only minimum required payload for their function

**DETECT**
- DE.CM-01: DLP on all tool API calls — sensitive data
  patterns detected before leaving controlled environment

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI04 Supply Chain
- Other frameworks: ISO 27001 A.5.19/A.5.20 · EU AI Act Art. 25 · SOC 2 CC9.1

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High

GenAI creates ungoverned derived data assets outside traditional
governance programmes. CSF 2.0 organisational context (GV.OC)
and asset management (ID.AM) address this as a governance and
inventory problem.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Organisational Context | GV.OC-01 | GOVERN | Data governance policy extended to all GenAI-derived assets — embeddings, caches, agent memory |
| Asset Management | ID.AM-08 | IDENTIFY | GenAI data assets inventoried — training datasets, embeddings, RAG stores, agent memory, telemetry logs |
| Data Security | PR.DS-01 | PROTECT | All GenAI data assets protected per classification — derived assets inherit source classification |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for ungoverned data assets — new GenAI deployments creating untracked data flows detected |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Extend data governance policy to all GenAI
  data assets — training data, embeddings, caches,
  agent memory, telemetry all covered
- GV.RM-06: Include ungoverned derived asset risk in
  risk register — scope, protection, deletion lifecycle

**IDENTIFY**
- ID.AM-08: Extend asset inventory to all GenAI-derived
  assets — embeddings, summaries, agent traces, caches
  all inventoried as data assets with classification

**PROTECT**
- PR.DS-01: Classification propagation — derived assets
  inherit the classification of their source documents,
  protection requirements applied automatically
- Deletion procedures covering derived assets — deleting
  source triggers deletion of all derived representations

**DETECT**
- DE.CM-09: Monitor for new ungoverned GenAI data flows —
  alert on new deployments creating data assets outside
  the governance programme

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI01 Sensitive Data Leakage
- Other frameworks: ISO 27001 A.5.9/A.8.10 · EU AI Act Art. 10 · SOC 2 C1.1

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High

GenAI systems trigger regulatory obligations without the organisation
recognising it. CSF 2.0 GOVERN is the primary function — compliance
is a governance responsibility.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Organisational Context | GV.OC-01 | GOVERN | Regulatory obligations inform cybersecurity risk management — GenAI regulatory scope assessed and documented |
| Risk Management Strategy | GV.RM-01 | GOVERN | Risk management strategy includes regulatory compliance risk — GenAI-specific obligations in risk programme |
| Risk Assessment | ID.RA-01 | IDENTIFY | Compliance risks identified per GenAI deployment — applicable regulations, triggered obligations, controls gaps |
| Communication | RS.CO-03 | RESPOND | Regulatory incident communication — breach notification, regulatory reporting, authority contact procedures |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Conduct regulatory scoping assessment for
  all GenAI deployments — identify applicable regulations
  (GDPR, EU AI Act, HIPAA, CCPA, PCI DSS), obligations,
  accountable owners
- GV.RM-01: Include regulatory compliance in risk
  management strategy — GenAI-specific obligations
  in risk programme with defined treatment

**IDENTIFY**
- ID.RA-01: Risk assessment includes compliance gap
  analysis — identify which obligations are met, which
  are gaps, remediation priority

**RESPOND**
- RS.CO-03: Regulatory incident communication procedures —
  breach notification timelines, regulatory reporting,
  authority contacts documented and tested

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance
- Other frameworks: EU AI Act Art. 10/17 · ISO 27001 A.5.31 · GDPR Art. 5/25/30

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Multimodal GenAI processes images and audio — OCR and transcription
pipelines extract sensitive content that may not be treated as
sensitive data. CSF 2.0 data security (PR.DS) and asset management
(ID.AM) address this.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Data Security | PR.DS-01 | PROTECT | Extracted content from multimodal inputs protected — OCR output of sensitive document classified and protected |
| Data Security | PR.DS-02 | PROTECT | Extracted sensitive content encrypted in transit — multimodal extraction pipelines covered |
| Continuous Monitoring | DE.CM-01 | DETECT | Multimodal extraction output monitored — DLP on OCR results, transcription outputs |
| Asset Management | ID.AM-08 | IDENTIFY | Multimodal processing pipelines inventoried — what modalities are processed, what is extracted and stored |

#### Mitigations by CSF function

**IDENTIFY**
- ID.AM-08: Inventory all multimodal processing pipelines —
  what inputs are accepted, what is extracted, where
  extracted content is stored and for how long

**PROTECT**
- PR.DS-01: Apply same data protection to extracted
  content as source modality — OCR output of a passport
  image is as sensitive as the passport
- Short retention for multimodal uploads and derived
  content — automated deletion after purpose is served

**DETECT**
- DE.CM-01: DLP on multimodal extraction outputs —
  PII detected in OCR results and transcription before
  storage or downstream use

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI14 Telemetry Leakage
- Other frameworks: ISO 27001 A.8.11 · GDPR Art. 9 · SOC 2 C2.1

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium

Synthetic data and anonymisation techniques fail to remove
re-identification risk in GenAI contexts. CSF 2.0 risk management
(GV.RM) and risk assessment (ID.RA) govern acceptable anonymisation
standards.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Risk Management Strategy | GV.RM-06 | GOVERN | Risk tolerance defined for re-identification risk in synthetic datasets — legal standard, not technical checkbox |
| Risk Assessment | ID.RA-01 | IDENTIFY | Re-identification risk assessed for all synthetic datasets before use or distribution |
| Data Security | PR.DS-01 | PROTECT | Synthetic datasets not automatically excluded from data protection — protected until re-identification risk formally assessed |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for re-identification attempts against synthetic datasets |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-06: Establish risk tolerance for re-identification
  risk — anonymisation standard, privacy budget, formal
  risk acceptance process before dataset release

**IDENTIFY**
- ID.RA-01: Formal re-identification risk assessment before
  any synthetic dataset is used externally — membership
  inference testing as part of assessment

**PROTECT**
- PR.DS-01: Treat synthetic datasets as in-scope for
  data protection until formal re-identification risk
  assessment is complete and accepted

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.5.34 · GDPR Recital 26 · SOC 2 P4.2

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High

Sensitive data from one user's conversation leaks into another
user's session. CSF 2.0 access control (PR.AA) governs session
isolation requirements.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Access permissions managed — per-user session isolation, per-tenant RAG namespaces enforced |
| Data Security | PR.DS-01 | PROTECT | Session data protected — per-user context encrypted, KV cache isolation prevents cross-session exposure |
| Continuous Monitoring | DE.CM-01 | DETECT | Session isolation monitored — cross-session access anomalies detected |
| Risk Assessment | ID.RA-01 | IDENTIFY | Session isolation risks documented per deployment — shared infrastructure components assessed |

#### Mitigations by CSF function

**PROTECT**
- PR.AA-05: Strict session isolation for all GenAI
  deployments — per-user context, RAG namespaces,
  KV cache isolation enforced at platform layer
- PR.DS-01: Encrypt per-user session data — session
  isolation technical control documented

**DETECT**
- DE.CM-01: Monitor for cross-session access anomalies —
  unusual retrieval patterns across session boundaries alerted

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3 · GDPR Art. 32 · SOC 2 CC6.1

---

### DSGAI12 — Unsafe Natural-Language Data Gateways

**Severity:** Critical

LLM-to-database interfaces collapse the security boundary between
user input and database logic. CSF 2.0 access control (PR.AA) and
platform security (PR.PS) address this as an access control and
secure development problem.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | LLM-generated queries execute under requesting user's permissions — not shared high-privilege service account |
| Platform Security | PR.PS-04 | PROTECT | Secure development — query allowlisting, parameterised execution as platform security requirements |
| Continuous Monitoring | DE.CM-01 | DETECT | All LLM-generated queries to data systems logged and monitored — bulk extraction patterns detected |
| Risk Assessment | ID.RA-01 | IDENTIFY | NL gateway interfaces documented in risk assessment — privilege level, query scope, data categories accessible |

#### Mitigations by CSF function

**IDENTIFY**
- ID.RA-01: Map all NL data gateways in risk assessment —
  privilege level, query scope, data categories, row-level
  policy enforcement status

**PROTECT**
- PR.AA-05: Per-user query execution — LLM queries execute
  under requesting user's permissions, not shared
  high-privilege service account
- PR.PS-04: Query allowlisting and parameterised execution
  as secure development requirements — injection addressed
  as a known vulnerability class

**DETECT**
- DE.CM-01: Log and monitor all LLM-generated queries —
  bulk extraction patterns, unusual query scope detected

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-89 · ISA/IEC 62443 SR 2.2 (OT)

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector databases have weaker default security posture than traditional
databases. CSF 2.0 data security (PR.DS) and platform security
(PR.PS) govern the baseline technical requirements.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Data Security | PR.DS-01 | PROTECT | Vector store content encrypted at rest — embeddings treated as sensitive derived data assets |
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | RBAC on all vector stores — no unauthenticated access in any environment |
| Platform Security | PR.PS-02 | PROTECT | Software managed to reduce risk — vector database CVEs patched promptly |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for anomalous access — bulk extraction, RBAC bypass attempts detected |

#### Mitigations by CSF function

**PROTECT**
- PR.DS-01: Encrypt all vector store content at rest
- PR.AA-05: RBAC enabled on all collections from day one —
  no unauthenticated access in any environment
- PR.PS-02: Patch all vector database CVEs promptly —
  CVE-2024-3584 class as urgent findings

**DETECT**
- DE.CM-09: Monitor vector store access patterns —
  bulk extraction, unusual query diversity alerted

#### Cross-references
- LLM Top 10: LLM08 Vector & Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3/A.8.24 · CWE-284 · SOC 2 CC6.1

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High

Observability pipelines capture full GenAI inputs and outputs with
weaker access controls and longer retention than production data.
CSF 2.0 GOVERN and data security (PR.DS) address telemetry governance.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Organisational Context | GV.OC-01 | GOVERN | Telemetry governance policy — least-logging defaults, classification of captured data, retention limits |
| Data Security | PR.DS-01 | PROTECT | Telemetry stores containing sensitive data protected — same requirements as production data stores |
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Access controls on telemetry stores — need-to-know enforced, not open access because "just logs" |
| Continuous Monitoring | DE.CM-09 | DETECT | Telemetry store access monitored — anomalous access patterns detected |

#### Mitigations by CSF function

**GOVERN**
- GV.OC-01: Establish telemetry governance policy —
  least-logging defaults, data classification applied
  to telemetry content, retention limits per tier

**PROTECT**
- PR.DS-01: Protect telemetry stores containing sensitive
  data — PAN masking before logging, encryption at rest
- PR.AA-05: Need-to-know access controls on all telemetry
  stores — restrict to authorised personnel

**DETECT**
- DE.CM-09: Monitor telemetry store access — anomalous
  patterns alerted as potential exfiltration via logs

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance
- Other frameworks: ISO 27001 A.8.15 · GDPR Art. 32 · SOC 2 C2.1

---

### DSGAI15 — Over-Broad Context Windows

**Severity:** High

RAG pipelines inject excessive content into context windows,
aggregating data from multiple trust domains into a single flat
namespace. CSF 2.0 access control (PR.AA) governs context
assembly controls.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Access permissions applied to context assembly — minimum-necessary context injection enforced |
| Data Security | PR.DS-01 | PROTECT | Context window content protected — highest classification of any included document drives handling |
| Continuous Monitoring | DE.CM-01 | DETECT | Context assembly monitored — over-broad injection patterns detected |
| Risk Assessment | ID.RA-01 | IDENTIFY | Context window risks documented — which deployments aggregate data across trust domains |

#### Mitigations by CSF function

**PROTECT**
- PR.AA-05: Minimum-necessary context injection — retrieve
  only passages directly relevant to the query, not broad
  datasets or full documents
- PR.DS-01: Track classification ceiling in context window —
  highest classification of any document drives response
  handling requirements

**DETECT**
- DE.CM-01: Monitor context assembly — over-broad injection
  aggregating data from multiple trust domains detected

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- Agentic Top 10: ASI01 Agent Goal Hijack
- Other frameworks: AIUC-1 A/B005 · ISO 27001 A.8.3 · SOC 2 CC6.1

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High

Browser AI assistants access sensitive data across open applications.
CSF 2.0 supply chain (GV.SC) governs endpoint AI tool approval.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Supply Chain Risk Management | GV.SC-01 | GOVERN | Browser AI extension providers with sensitive data access treated as third-party suppliers |
| Platform Security | PR.PS-02 | PROTECT | Software managed to reduce risk — browser AI extensions version-controlled, patched, approved before deployment |
| Continuous Monitoring | DE.CM-01 | DETECT | AI assistant access to sensitive data on endpoints monitored |
| Asset Management | ID.AM-08 | IDENTIFY | Approved browser AI extensions inventoried — data access scope, security assessment status |

#### Mitigations by CSF function

**GOVERN**
- GV.SC-01: Treat approved browser AI extension providers
  as third-party suppliers — security assessment before
  approval, written agreements with data handling obligations

**IDENTIFY**
- ID.AM-08: Inventory all approved AI extensions —
  data access scope, version, security assessment date

**PROTECT**
- PR.PS-02: Approved extensions only, patched and
  version-controlled — unapproved extensions blocked
  at device management layer

**DETECT**
- DE.CM-01: Monitor AI assistant data access on endpoints —
  unusual data access patterns alerted

#### Cross-references
- Agentic Top 10: ASI10 Rogue Agents
- DSGAI 2026: DSGAI03 Shadow AI
- Other frameworks: ISO 27001 A.8.1/A.8.7 · SOC 2 CC9.1 · EU AI Act Art. 9

---

### DSGAI17 — Data Availability & Resilience Failures

**Severity:** High

Silent GenAI pipeline failures affect advisory and fraud detection
availability. CSF 2.0 infrastructure resilience (PR.IR) and
recovery (RC.RP) govern availability requirements.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Infrastructure Resilience | PR.IR-01 | PROTECT | Networks and environments protected for resilience — circuit breakers, freshness monitoring, redundancy |
| Continuous Monitoring | DE.CM-01 | DETECT | GenAI pipeline health monitored — freshness, availability metrics reviewed continuously |
| Incident Mitigation | RS.MI-01 | RESPOND | Pipeline failures contained — circuit breaker activation, graceful degradation, user notification |
| Incident Recovery | RC.RP-01 | RECOVER | Recovery plan includes GenAI pipeline failures — BCP covers AI availability, RTO/RPO defined |

#### Mitigations by CSF function

**PROTECT**
- PR.IR-01: Circuit breakers and graceful degradation as
  resilience measures — explicit unavailability notice
  rather than silent misinformation

**DETECT**
- DE.CM-01: Monitor GenAI pipeline health continuously —
  freshness alerts when index age exceeds threshold

**RESPOND**
- RS.MI-01: Graceful degradation — notify users explicitly
  when retrieval is unavailable rather than serving
  stale results as current

**RECOVER**
- RC.RP-01: BCP covers GenAI pipeline failures — RTO/RPO
  defined, failover tested annually

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: ISA/IEC 62443 SR 7.6 (OT) · SOC 2 A1.1 · AIUC-1 D

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High

Membership inference and model inversion attacks reconstruct sensitive
training data from GenAI model outputs. CSF 2.0 risk management
(GV.RM) and data security (PR.DS) govern reconstruction risk controls.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Data Security | PR.DS-01 | PROTECT | Reconstruction resistance as data protection measure — differential privacy in training, confidence score suppression |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for inference attack patterns — systematic output space probing detected |
| Risk Assessment | ID.RA-01 | IDENTIFY | Inference attack risks documented per deployment — models trained on sensitive data assessed |
| Risk Management Strategy | GV.RM-06 | GOVERN | Risk tolerance for inference attacks established — acceptable reconstruction risk defined per use case |

#### Mitigations by CSF function

**GOVERN**
- GV.RM-06: Define risk tolerance for inference attacks —
  what reconstruction risk is acceptable, what training
  data sensitivity triggers differential privacy

**IDENTIFY**
- ID.RA-01: Assess inference attack risk per model —
  which models trained on sensitive data, what is the
  reconstruction attack surface

**PROTECT**
- PR.DS-01: Apply differential privacy in training for
  sensitive corpora — privacy budget documented as
  data protection control
- Suppress confidence scores in production outputs —
  limits membership inference success rate

**DETECT**
- DE.CM-09: Monitor for inference attack patterns —
  systematic output space probing alerted

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI10 Synthetic Data Pitfalls
- Other frameworks: ISO 27001 A.8.11 · GDPR Art. 25 · SOC 2 C2.1

---

### DSGAI19 — Human-in-Loop & Labeler Overexposure

**Severity:** Medium

Human annotators access sensitive model inputs during labelling.
CSF 2.0 supply chain (GV.SC) governs labelling vendor data
handling obligations.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Supply Chain Risk Management | GV.SC-01 | GOVERN | Labelling vendors treated as suppliers — data handling requirements in contracts, compliance monitored |
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | Data minimisation — annotators access minimum content required for annotation function |
| Organisational Context | GV.OC-01 | GOVERN | Acceptable use policy covers labelling activities — what data may be used in labelling workflows |
| Awareness and Training | PR.AT-01 | PROTECT | Labelling staff trained on data handling — classification, prohibited use, incident reporting |

#### Mitigations by CSF function

**GOVERN**
- GV.SC-01: Treat labelling vendors as third-party
  suppliers — assess before engagement, contractual
  data handling obligations, right-to-audit
- GV.OC-01: Define acceptable use for labelling
  workflows — which data may be used, anonymisation
  requirements, retention limits

**PROTECT**
- PR.AA-05: Data minimisation in labelling tasks —
  annotators see minimum content required, not full
  sensitive records

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.34 · GDPR Art. 28 · EU AI Act Art. 10

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High

Adversaries reconstruct a functional model replica through systematic
API querying. CSF 2.0 access control (PR.AA) and detection (DE.CM)
govern the extraction prevention controls.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Identity Management, Authentication & Access Control | PR.AA-05 | PROTECT | API rate limiting as access control — systematic extraction requires high query volumes |
| Continuous Monitoring | DE.CM-01 | DETECT | Production API monitoring — unusual query diversity and volume indicative of extraction alerted |
| Continuous Monitoring | DE.CM-09 | DETECT | Monitoring for extraction behaviour — systematic output space coverage pattern detected |
| Risk Assessment | ID.RA-01 | IDENTIFY | Model extraction risk documented — IP exposure, CHD reconstruction potential assessed |

#### Mitigations by CSF function

**PROTECT**
- PR.AA-05: Rate limiting as access control — systematic
  extraction requires high query volumes, rate limiting
  raises cost and triggers detection

**DETECT**
- DE.CM-01: Monitor for extraction patterns —
  unusual query diversity, high volume, systematic
  output space coverage alerted
- DE.CM-09: Adaptive monitoring — alert on extraction
  behaviour patterns specific to your model

**RESPOND**
- RS.MI-01: Contain extraction attempts — rate limit
  tightening, session blocking, legal assessment

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.5.12 · MITRE ATLAS AML.T0016 · SOC 2 C2.1

---

### DSGAI21 — Disinformation via Data Poisoning

**Severity:** High

False content injected into RAG corpora causes GenAI to surface
misinformation as authoritative. CSF 2.0 supply chain (GV.SC) and
detection (DE.CM) govern RAG corpus integrity.

#### CSF 2.0 mapping

| Category | ID | Function | How it applies |
|---|---|---|---|
| Supply Chain Risk Management | GV.SC-01 | GOVERN | RAG data source providers treated as suppliers — content integrity requirements in contracts |
| Continuous Monitoring | DE.CM-09 | DETECT | RAG corpus integrity monitored — anomalous content changes, unusual ingestion patterns detected |
| Incident Analysis | RS.AN-03 | RESPOND | RAG poisoning incidents analysed — affected content identified, operational decisions influenced reviewed |
| Data Security | PR.DS-01 | PROTECT | RAG corpus content integrity protected — hash-based verification, source trust tiering |

#### Mitigations by CSF function

**GOVERN**
- GV.SC-01: Include RAG data source providers in supply
  chain programme — content integrity guarantees, incident
  notification requirements in contracts

**PROTECT**
- PR.DS-01: RAG corpus integrity controls — source trust
  tiering, hash-based content verification, ingestion
  gates during elevated threat periods

**DETECT**
- DE.CM-09: Monitor RAG corpus for unauthorised
  modifications — integrity hashing on all indexed
  content, anomalous changes alerted

**RESPOND**
- RS.AN-03: Investigate poisoning incidents — source
  quarantine, impacted index rebuild, output correction,
  user notification where material impact

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0045 · ISO 27001 A.5.7 · SOC 2 PI1.2

---

## CSF 2.0 profile for GenAI data security

| CSF Function | DSGAI priority entries | Key categories | Target state |
|---|---|---|---|
| GOVERN | DSGAI01, DSGAI03, DSGAI07, DSGAI08 | GV.OC-01, GV.SC-01, GV.RM-01/06 | Data governance policy extended to GenAI assets, supply chain programme live, regulatory scoping complete |
| IDENTIFY | DSGAI02, DSGAI06, DSGAI13, DSGAI16 | ID.AM-08, ID.RA-01, ID.RA-08 | All GenAI data assets inventoried, risk assessments complete, tool integrations mapped |
| PROTECT | DSGAI01, DSGAI11, DSGAI12, DSGAI14 | PR.DS-01/02, PR.AA-01/05, PR.PS-04, PR.IR-01 | Encryption, access controls, session isolation, and NL gateway validation implemented |
| DETECT | DSGAI04, DSGAI20, DSGAI21 | DE.CM-01/09, DE.AE-02 | Production monitoring live for all DSGAI risks, anomaly alerts operational |
| RESPOND | DSGAI01, DSGAI04, DSGAI17 | RS.AN-03, RS.MI-01/02, RS.CO-03 | Incident response procedures tested for all DSGAI scenarios |
| RECOVER | DSGAI17 | RC.RP-01 | BCP covers GenAI pipeline failures, RTO/RPO defined and tested |

---

## Implementation priority

| Phase | DSGAI entries | CSF focus | Rationale |
|---|---|---|---|
| 1 — GOVERN + IDENTIFY | DSGAI01, DSGAI07, DSGAI08 | GV.OC-01, ID.AM-08 | Data inventory and governance before technical controls |
| 2 — PROTECT | DSGAI02, DSGAI11, DSGAI12 | PR.AA, PR.DS, PR.PS-04 | Access control and NL gateway security close most common breach paths |
| 3 — DETECT | DSGAI04, DSGAI21, DSGAI20 | DE.CM-09, DE.AE-02 | Poisoning, disinformation, and extraction detection programme |
| 4 — RESPOND + RECOVER | All | RS.AN, RS.MI, RC.RP | Incident response tested, BCP covers all GenAI data scenarios |

---

## References

- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [LLM Top 10 × CSF 2.0](../llm-top10/LLM_NISTCSF2.md)
- [Agentic Top 10 × CSF 2.0](../agentic-top10/Agentic_NISTCSF2.md)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full entries with CSF 2.0 profile | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the GenAI Security Crosswalk: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk
