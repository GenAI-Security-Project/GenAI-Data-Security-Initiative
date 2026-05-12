<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : ENISA — Multilayer Framework for Good Cybersecurity Practices for AI
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × ENISA Multilayer Framework

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [ENISA Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai) —
published by the European Union Agency for Cybersecurity (ENISA) to
support the cybersecurity requirements of the EU AI Act and NIS2 Directive.

---

## Why ENISA for LLM security

ENISA's Multilayer Framework is the primary European technical
reference for AI cybersecurity. It bridges three layers:

**Layer 1 — General ICT security:** Baseline security practices that
apply to all ICT systems hosting AI — network security, access
control, incident response, supply chain security. These are
largely equivalent to established frameworks (ISO 27001, NIS2 baseline
measures) applied to AI infrastructure.

**Layer 2 — AI-specific security:** Security practices specifically
addressing the AI system lifecycle — training data security, model
integrity, adversarial robustness, AI supply chain, and monitoring
of AI-specific failure modes. This layer maps most directly to the
LLM Top 10.

**Layer 3 — AI sector-specific security:** Security practices for
AI deployed in high-risk sectors (critical infrastructure, healthcare,
finance) — directly relevant to operators subject to NIS2 and
EU AI Act Annex III high-risk classification.

For organisations subject to EU AI Act obligations or NIS2 essential
entity requirements, ENISA's framework provides the technical
implementation guidance that supports compliance evidence. The August
2026 EU AI Act deadline for high-risk AI system obligations makes
this mapping time-critical for European LLM deployments.

---

## ENISA framework structure

| Layer | Focus | LLM security relevance |
|---|---|---|
| L1 — General ICT | Network, access control, patch management, incident response, supply chain | LLM infrastructure security — the platform on which LLMs run |
| L2 — AI-specific | Training data, model integrity, adversarial robustness, AI supply chain, AI monitoring | LLM-specific attack surface — the model itself and its data pipeline |
| L3 — Sector-specific | Critical infrastructure, healthcare, finance AI security | Sector-specific LLM deployments in NIS2 essential entity scope |

**Key ENISA security domains for LLM:**

| Domain | Abbreviation | Scope |
|---|---|---|
| Data and model security | DMS | Training data integrity, model weights, embeddings |
| AI system integrity | ASI | Model behaviour verification, adversarial robustness |
| Supply chain security | SCS | Model providers, datasets, plugins, inference runtime |
| Monitoring and detection | MON | AI-specific anomaly detection, output monitoring |
| Incident response | IRS | AI incident handling, model rollback, disclosure |
| Governance and risk | GOV | AI risk management, policy, accountability |

---

## Quick-reference summary

| ID | Name | Severity | Primary ENISA Domains | Layer | Tier |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | ASI, MON, GOV | L1–L2 | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | DMS, MON, GOV | L1–L2 | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | SCS, DMS, GOV | L1–L2 | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | Critical | DMS, ASI, MON | L2 | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | ASI, MON, L1 | L1–L2 | Foundational–Hardening |
| LLM06 | Excessive Agency | High | GOV, ASI, MON | L2–L3 | Foundational–Hardening |
| LLM07 | System Prompt Leakage | High | DMS, GOV, MON | L1–L2 | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | DMS, ASI, MON | L2 | Hardening–Advanced |
| LLM09 | Misinformation | Medium | ASI, GOV, MON | L2 | Foundational–Hardening |
| LLM10 | Unbounded Consumption | Medium | L1, MON, IRS | L1 | Foundational–Hardening |

---

## Audience tags

- **EU organisation subject to NIS2** — full file, ENISA framework alignment for LLM programme
- **EU AI Act compliance lead** — L2 AI-specific controls, high-risk AI system evidence
- **CISO (European enterprise)** — GOV domain entries, risk management alignment
- **Security engineer** — ASI, DMS, MON technical control entries
- **Incident responder** — IRS domain entries
- **OT engineer (NIS2 essential entity)** — L3 sector-specific entries, LLM01/LLM04/LLM10

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions in user input or processed content manipulate
LLM behaviour. ENISA L2 (AI-specific security) addresses this through
AI system integrity (ASI) and adversarial robustness requirements.
For NIS2 essential entities, prompt injection against an LLM
integrated with operational systems is a significant incident
category requiring reporting under Article 23.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| AI System Integrity (ASI) | L2 | Adversarial input testing | LLM applications tested against prompt injection before deployment — adversarial inputs validated as part of AI system integrity verification |
| Monitoring and Detection (MON) | L1–L2 | AI-specific monitoring | Runtime monitoring for injection indicators across all LLM input channels — AI-specific anomaly detection |
| Governance and Risk (GOV) | L2 | AI risk management | Prompt injection documented in AI risk register — risk assessment per deployment, treatment controls, review cadence |
| General ICT — Secure Development | L1 | Secure coding practices | Input validation and context separation as secure development requirements for all LLM integrations |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Secure Development: Implement input validation
  as a secure development requirement — all LLM
  integrations reviewed for injection resistance before
  deployment
- L1 Network Security: Filter known injection patterns
  at network boundary — WAF or API gateway rules
  covering LLM input endpoints
- GOV: Document prompt injection in AI risk register —
  risk owner, treatment controls, review cadence

**Hardening (L2)**
- ASI: Include adversarial injection testing in AI
  system integrity verification — direct, indirect,
  and multi-turn injection scenarios tested before
  each production release
- MON: Deploy AI-specific runtime monitoring covering
  injection indicators — ENISA L2 monitoring practice
  extends to LLM-specific attack patterns
- Implement architectural separation between system
  prompt and user input as L2 AI system integrity control

**Advanced (L2–L3)**
- ASI: Red team with novel indirect injection techniques
  quarterly — ENISA adversarial testing practice applied
  to RAG, tool return, and document processing pipelines
- L3 (NIS2 essential entities): Include prompt injection
  in NIS2 significant incident assessment — determine
  whether successful injection constitutes a reportable
  incident under Article 23

#### EU AI Act alignment

For high-risk AI systems (Annex III), Article 15 requires technical
robustness and cybersecurity — ENISA ASI adversarial testing practices
are the technical implementation of Article 15 for prompt injection.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISO 27001 A.8.28 · NIST CSF 2.0 PR.PS-04 · EU AI Act Art. 15

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs expose PII, financial data, or confidential information through
outputs. ENISA DMS (Data and Model Security) provides the data
protection framework — training data governance, output scanning,
and privacy-preserving techniques are DMS practices.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Training data governance | All data in LLM scope classified and governed — training corpora, RAG sources, embeddings, outputs |
| Monitoring and Detection (MON) | L1–L2 | Output monitoring | DLP on all LLM output channels — AI-specific monitoring covering sensitive data patterns |
| Governance and Risk (GOV) | L2 | Privacy risk management | GDPR and EU AI Act Article 10 data governance obligations addressed for LLM deployments |
| General ICT — Data Protection | L1 | Encryption and access control | Training data, embeddings, and RAG stores encrypted at rest and in transit |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Data Protection: Encrypt all sensitive data
  in LLM scope at rest and in transit — training
  datasets, embedding stores, RAG document stores,
  prompt caches
- L1 Access Control: Least-privilege access to all
  LLM data sources — RAG retrieval enforces user
  authorisation scope

**Hardening (L2)**
- DMS: Implement data classification policy covering
  all GenAI data assets — training data, embeddings,
  outputs all classified with handling requirements
  documented as DMS evidence
- MON: Deploy DLP on all LLM output channels —
  AI-specific monitoring practice covering PII and
  sensitive patterns before delivery
- GOV: Document data governance for LLM in AI risk
  management programme — GDPR Article 30 records of
  processing updated to cover LLM training and inference

**Advanced (L2)**
- DMS: Apply differential privacy in training for
  sensitive corpora — ENISA privacy-preserving
  technique practice
- ASI: Conduct model inversion red team — ENISA
  adversarial testing applied to data reconstruction
  attacks against your specific deployment

#### EU AI Act alignment

Article 10 data governance obligations apply to all data used in
training — ENISA DMS practices are the technical implementation
guidance for Article 10 compliance.

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
libraries, and plugins. ENISA SCS (Supply Chain Security) is the
primary domain — ENISA provides specific AI supply chain guidance
that extends general ICT supply chain practices to model weights,
training datasets, and inference runtime components.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Supply Chain Security (SCS) | L1–L2 | AI supply chain management | LLM component vendors assessed — model providers, dataset vendors, inference runtime suppliers subject to SCS practices |
| Data and Model Security (DMS) | L2 | Model integrity | Model weight integrity verification — cryptographic signatures, hash-based baseline |
| Governance and Risk (GOV) | L2 | Third-party AI risk | Vendor risk management extended to AI component suppliers — contractual security obligations |
| General ICT — Supply Chain | L1 | ICT supply chain security | ML SBOM as software asset inventory — all LLM components inventoried, CVEs monitored |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Supply Chain: Maintain ML SBOM as part of ICT
  asset inventory — every LLM component (model, adapters,
  libraries) inventoried with version, source, hash
- L1 Patch Management: Include LLM component CVEs in
  vulnerability management — ML libraries and inference
  runtime dependencies scanned and patched on schedule

**Hardening (L2)**
- SCS: Apply ENISA AI supply chain security practices
  to all LLM component vendors — security obligations,
  provenance documentation, vulnerability disclosure SLA
  documented before any component enters production
- DMS: Verify model weight integrity before deployment —
  cryptographic signatures as ENISA model integrity
  practice
- GOV: Include LLM vendor risk in AI risk register —
  third-party AI risk assessment per vendor

**Advanced (L2)**
- SCS: Periodic security assessments of strategic LLM
  component suppliers — ENISA supply chain audit
  practice applied to model and dataset vendors
- Operate isolated evaluation environment — ENISA
  adversarial testing applied to component behaviour
  before each production promotion

#### EU AI Act alignment

Article 25 value chain responsibilities and Article 17 quality
management both require supply chain security documentation — ENISA
SCS practices provide the technical evidence base.

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

Adversaries corrupt training data or model weights. ENISA L2 DMS
(Data and Model Security) and ASI (AI System Integrity) are the
primary domains — training data security and model integrity
verification are explicit ENISA AI-specific security practices.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Training data security | Training data integrity controls — source allowlisting, anomaly detection, provenance tracking as DMS practices |
| AI System Integrity (ASI) | L2 | Model integrity verification | Post-training backdoor detection and model integrity verification as ASI practices before deployment |
| Monitoring and Detection (MON) | L2 | AI-specific anomaly detection | Production monitoring for poisoning indicators — systematic output anomalies detected through AI-specific monitoring |
| Incident Response (IRS) | L1–L2 | AI incident handling | Model rollback and poisoning incident response as ENISA IRS practice for AI-specific incidents |

#### Mitigations for ENISA alignment

**Foundational (L1–L2)**
- DMS: Implement training data integrity controls —
  source allowlisting, anomaly detection on data
  distributions, provenance tracking from source to
  training dataset, documented as DMS practice evidence
- ASI: Model integrity verification as deployment gate —
  hash-based check against approved baseline, documented
  as ASI practice before each production promotion

**Hardening (L2)**
- ASI: Post-training backdoor detection as mandatory
  deployment gate — ENISA adversarial testing practice
  applied to poisoning detection
- MON: Production monitoring for poisoning indicators —
  systematic recommendation drift detected as AI-specific
  anomaly through ENISA L2 monitoring
- IRS: Define AI-specific incident response for
  poisoning — model rollback procedure, affected
  deployment scope assessment, disclosure assessment

**Advanced (L2)**
- ASI: Include poisoning scenarios in adversarial
  testing programme — OT-specific trigger conditions
  tested for industrial deployments
- DMS: Apply differential privacy during training —
  ENISA privacy-preserving technique limits poisoning
  influence of individual training examples

#### EU AI Act alignment

Article 9 risk management must cover poisoning as a foreseeable
attack — ENISA ASI and DMS practices provide the technical controls
that satisfy Article 9 risk treatment requirements.

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0020 · ISO 27001 A.8.27

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM output passed to downstream systems without validation enables
injection attacks. ENISA L1 secure development practices and L2
AI system integrity (ASI) both address output handling — output
security is an ICT secure development requirement amplified by
AI-specific output characteristics.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| General ICT — Secure Development | L1 | Secure coding | Output encoding and schema validation as L1 secure development requirements — LLM output treated as untrusted |
| AI System Integrity (ASI) | L2 | Output validation | AI-specific output validation — schema enforcement, injection pattern detection before downstream consumption |
| Monitoring and Detection (MON) | L1–L2 | Output monitoring | Runtime monitoring of LLM output channels — injection patterns in model responses detected |
| General ICT — Application Security | L1 | Application testing | DAST on all interfaces consuming LLM output as L1 application security practice |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Secure Development: Output encoding and schema
  validation as secure coding requirements — LLM output
  treated as untrusted input to all downstream systems
- L1 Application Security: DAST on all interfaces
  consuming LLM output — XSS, SQL injection, command
  injection via model output tested

**Hardening (L2)**
- ASI: Implement output schema validation as AI system
  integrity control — only outputs conforming to defined
  safe structures passed to downstream consumers
- MON: Monitor LLM output channels for injection
  patterns — AI-specific anomaly detection covering
  output security

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

LLMs with excessive autonomy over tools and systems execute unintended
or harmful actions. ENISA GOV (Governance and Risk) and L2 AI-specific
security both address autonomous action scope — human oversight of
AI systems is a GOV practice with direct EU AI Act Article 14
alignment.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Governance and Risk (GOV) | L2 | Human oversight | Human oversight requirements for autonomous LLM actions — acceptable autonomy scope defined in AI governance policy |
| AI System Integrity (ASI) | L2 | Action validation | Tool permission enforcement and action guardrails as ASI controls — LLM cannot exceed defined scope |
| Monitoring and Detection (MON) | L1–L2 | Behavioural monitoring | All LLM tool invocations logged and monitored — anomalous scope detected through AI-specific monitoring |
| General ICT — Access Control | L1 | Least privilege | LLM tool access managed as privileged access — minimum permissions, regular review |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Access Control: Manage LLM tool access as
  privileged access — minimum permissions enforced,
  reviewed on change and quarterly
- GOV: Establish policy on acceptable LLM autonomous
  action scope — which actions require human confirmation
  documented in AI governance policy

**Hardening (L2)**
- ASI: Implement action guardrails as AI system
  integrity control — tool permission enforcement
  independent of the model instruction
- MON: Log and monitor all LLM tool invocations —
  AI-specific monitoring covering autonomous action
  scope and anomalous parameters
- GOV: Include excessive agency in AI risk register —
  blast radius per deployment, owner, treatment

**Advanced (L2–L3)**
- ASI: Red team excessive agency via indirect injection —
  ENISA adversarial testing applied to autonomous
  action scenarios
- L3 (NIS2 essential entities): Excessive agency in
  critical infrastructure is a significant incident
  category — include in NIS2 incident assessment

#### EU AI Act alignment

Article 14 human oversight is the primary EU AI Act article for
excessive agency — ENISA GOV human oversight practices are the
technical implementation guidance for Article 14 compliance.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: EU AI Act Art. 14 · AIUC-1 B006 · ISO 27001 A.8.2

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing security controls are extracted by
adversaries. ENISA DMS (Data and Model Security) governs system
prompts as sensitive AI system configuration data requiring
classification and protection.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | AI system configuration security | System prompts classified as sensitive AI system configuration — encrypted, access-controlled, version-managed |
| Governance and Risk (GOV) | L2 | Information classification | System prompt security as AI governance obligation — operational security value assessed |
| Monitoring and Detection (MON) | L1–L2 | Access monitoring | System prompt access logged and monitored — anomalous access detected |
| General ICT — Data Protection | L1 | Configuration security | System prompts not stored in cleartext — encryption at rest as L1 data protection practice |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Data Protection: Encrypt system prompts at rest —
  not stored in cleartext configuration, source code,
  or environment variables
- L1 Access Control: Restrict system prompt access
  to authorised personnel — version controlled,
  access logged

**Hardening (L2)**
- DMS: Classify system prompts as sensitive AI system
  configuration — ENISA DMS practice for AI-specific
  sensitive configuration data
- ASI: Include prompt extraction testing in ENISA
  adversarial testing programme — verify resistance
  before each deployment

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003/B009 · ISO 27001 A.5.12 · CWE-200

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Vector stores are susceptible to adversarial retrieval and inference
attacks. ENISA DMS (Data and Model Security) governs embedding stores
as AI data assets requiring specific security controls beyond standard
database practices.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Embedding security | Vector stores classified as AI data assets — RBAC, encryption, provenance tracking as DMS practices |
| AI System Integrity (ASI) | L2 | Adversarial retrieval testing | Vector store attacks in ENISA adversarial testing — RBAC bypass, embedding inversion, bulk extraction |
| Monitoring and Detection (MON) | L2 | AI-specific anomaly detection | Vector store query patterns monitored — bulk extraction and unusual diversity detected |
| Supply Chain Security (SCS) | L1–L2 | Component vulnerability management | Vector database CVEs in vulnerability management — CVE-2024-3584 class urgent |

#### Mitigations for ENISA alignment

**Foundational (L1–L2)**
- DMS: Apply ENISA AI data asset protection to
  all vector stores — RBAC enabled, content encrypted,
  provenance documented as DMS practice evidence
- SCS: Vector database CVEs in vulnerability management
  — CVE-2024-3584 class as urgent findings

**Hardening (L2)**
- ASI: Include vector store attacks in ENISA adversarial
  testing — RBAC bypass, path traversal, embedding
  inversion tested before each deployment
- MON: Monitor vector store access patterns — bulk
  extraction and unusual query diversity detected
  through AI-specific anomaly detection

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://weaviate.io |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference & Data Reconstruction
- Other frameworks: NIST AI RMF MS-2.5 · ISO 27001 A.8.3/A.8.24 · CWE-284

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but incorrect content. ENISA GOV (Governance
and Risk) and ASI (AI System Integrity) address misinformation as
both a governance obligation (disclosure, accuracy policy) and a
technical integrity concern (accuracy monitoring, drift detection).

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Governance and Risk (GOV) | L2 | AI accuracy policy | Acceptable accuracy thresholds defined per use case — domains requiring human verification documented in AI governance |
| AI System Integrity (ASI) | L2 | Accuracy verification | Production accuracy monitoring as ASI practice — hallucination rates tracked per domain, drift detected |
| Monitoring and Detection (MON) | L2 | AI-specific monitoring | Accuracy degradation monitoring — ENISA L2 monitoring covering AI-specific failure modes |
| General ICT — Awareness | L1 | User awareness | Users of LLM decision-support tools trained on output limitations — ENISA awareness practice |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Awareness: Train all users of LLM decision-support
  tools on output limitations — ENISA awareness practice
  mandatory before access granted
- GOV: Define accuracy policy per LLM use case —
  domains requiring verification, advisory vs
  authoritative output distinction

**Hardening (L2)**
- ASI: Production accuracy monitoring as ENISA AI
  system integrity practice — hallucination rates
  per domain tracked, degradation alerted
- MON: Include accuracy drift in AI-specific monitoring
  programme — ENISA L2 monitoring covering AI failure modes

#### EU AI Act alignment

Article 13 transparency obligations require disclosure of AI system
limitations — ENISA GOV accuracy policy practices support Article 13
compliance by defining and communicating accuracy thresholds.

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
ENISA L1 general ICT security covers DoS protection and resilience —
LLM-induced resource exhaustion is a new instantiation of documented
DoS threat patterns addressed by ENISA L1 availability practices.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| General ICT — Availability | L1 | DoS protection and resilience | Rate limiting and resource controls as L1 availability practices — LLM infrastructure protected against exhaustion |
| Monitoring and Detection (MON) | L1–L2 | Resource consumption monitoring | LLM resource consumption monitored — cost anomaly detection as ENISA monitoring practice |
| Incident Response (IRS) | L1 | Availability incident response | Incident response for consumption anomalies — automated rate limiting, circuit breakers, cost budgets |
| Governance and Risk (GOV) | L2 | AI availability risk | LLM availability in risk management — RTO/RPO defined, consumption risk in AI risk register |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Availability: Rate limiting and resource controls
  as ENISA DoS protection practice — hard token caps,
  per-user budgets enforced at API gateway
- IRS: Define incident response for consumption anomalies —
  automated rate tightening, cost circuit breakers,
  owner notification as ENISA IRS practice

**Hardening (L1–L2)**
- MON: Monitor LLM resource consumption in real time —
  ENISA monitoring practice covering consumption anomalies
- GOV: Include LLM availability in AI risk register —
  RTO/RPO defined, consumption risk documented

**Advanced (L2)**
- ASI: Adversarial load testing as ENISA adversarial
  testing practice — sponge example attacks tested
  before production deployment

#### NIS2 alignment

For NIS2 essential entities, DoS against AI systems supporting
critical operations may constitute a significant incident under
Article 23 — ENISA L1 availability practices and IRS incident
response procedures support NIS2 incident notification obligations.

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

## ENISA framework profile for LLM security

| Layer | LLM priority entries | Key domains | Target state |
|---|---|---|---|
| L1 — General ICT | LLM03, LLM05, LLM10 | Secure Development, Supply Chain, Availability | Baseline ICT security for all LLM infrastructure |
| L2 — AI-specific | LLM01, LLM02, LLM04 | ASI, DMS, MON | AI-specific controls verified — adversarial testing, data governance, AI monitoring live |
| L3 — Sector-specific | LLM01, LLM06, LLM10 | GOV, IRS | NIS2 essential entity obligations met — incident assessment, reporting procedures tested |

---

## EU AI Act and NIS2 compliance alignment

| Regulation | Article | ENISA domain | LLM entries |
|---|---|---|---|
| EU AI Act | Art. 9 — Risk management | GOV | All entries |
| EU AI Act | Art. 10 — Data governance | DMS | LLM02, LLM04, LLM08 |
| EU AI Act | Art. 13 — Transparency | GOV | LLM09 |
| EU AI Act | Art. 14 — Human oversight | GOV | LLM06 |
| EU AI Act | Art. 15 — Robustness and cybersecurity | ASI | LLM01, LLM04, LLM05 |
| NIS2 | Art. 21 — Security measures | L1/L2 | All entries |
| NIS2 | Art. 23 — Incident reporting | IRS | LLM01, LLM06, LLM10 |

---

## Implementation priority

| Phase | LLM entries | ENISA domains | Rationale |
|---|---|---|---|
| 1 — L1 baseline | LLM03, LLM05, LLM10 | L1 Supply Chain, Secure Dev, Availability | ICT security foundation before AI-specific controls |
| 2 — L2 AI-specific | LLM01, LLM02, LLM04 | ASI, DMS, MON | AI-specific controls address highest-severity risks |
| 3 — Governance | LLM06, LLM09 | GOV | Policy and risk management covering autonomy and accuracy |
| 4 — Advanced testing | LLM07, LLM08 | ASI adversarial testing | Configuration and embedding security hardening |

---

## References

- [ENISA Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai)
- [ENISA AI Cybersecurity Risks Report](https://www.enisa.europa.eu/publications/artificial-intelligence-cybersecurity-challenges)
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [NIS2 Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries with EU AI Act and NIS2 alignment table | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
