<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks & Mitigations 2026 (DSGAI01-DSGAI21)
  Framework   : ENISA Multilayer Framework for Good Cybersecurity Practices for AI
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 — ENISA Multilayer Framework

Mapping the [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to the [ENISA Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai) —
published by the European Union Agency for Cybersecurity (ENISA) to
support the cybersecurity requirements of the EU AI Act and NIS2 Directive.

---

## Why ENISA for DSGAI data security

ENISA's Multilayer Framework is the primary European technical
reference for AI cybersecurity. For organisations managing GenAI
data security risks, ENISA is particularly relevant because:

- **EU AI Act Article 10** mandates data governance for high-risk
  AI systems — ENISA's Data and Model Security (DMS) domain provides
  the technical implementation guidance
- **NIS2 Directive** essential entities deploying GenAI must apply
  ENISA's L1 ICT baseline controls to the AI infrastructure,
  extending to L2 AI-specific controls for the data pipeline
- **DSGAI's data-centric taxonomy** aligns naturally with ENISA's
  DMS domain, which covers training data integrity, model security,
  embedding stores, and output data governance

The DSGAI 2026 risks follow data through a GenAI system from ingestion
through inference to output — ENISA's layered approach mirrors this
by distinguishing infrastructure (L1), AI-specific (L2), and
sector-specific (L3) security controls for each stage.

---

## ENISA framework structure

| Layer | Focus | DSGAI security relevance |
|---|---|---|
| L1 — General ICT | Network security, access control, patch management, incident response, supply chain | GenAI infrastructure security — the platform on which GenAI data flows |
| L2 — AI-specific | Training data governance, model integrity, adversarial robustness, AI supply chain, AI monitoring | GenAI-specific data attack surface — pipelines, RAG stores, embeddings, inference |
| L3 — Sector-specific | Critical infrastructure, healthcare, finance AI security | Sector-specific GenAI deployments in NIS2 essential entity or EU AI Act high-risk scope |

**Key ENISA security domains for DSGAI:**

| Domain | Abbreviation | Scope |
|---|---|---|
| Data and Model Security | DMS | Training data integrity, model weights, embeddings, RAG stores |
| AI System Integrity | ASI | Model behaviour verification, adversarial robustness, output safety |
| Supply Chain Security | SCS | Model providers, datasets, plugins, agents, inference runtime |
| Monitoring and Detection | MON | AI-specific anomaly detection, output monitoring, DLP |
| Incident Response | IRS | AI incident handling, model rollback, data breach response |
| Governance and Risk | GOV | AI risk management, data governance policy, accountability |

---

## Quick-reference summary

| ID | Name | Severity | Primary ENISA Domains | Layer | Tier |
|---|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | DMS, MON, GOV | L1–L2 | Foundational–Advanced |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | ASI, GOV, MON | L1–L2 | Foundational–Advanced |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | GOV, MON, SCS | L1–L2 | Foundational–Hardening |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | DMS, ASI, MON | L2 | Hardening–Advanced |
| DSGAI05 | Data Integrity & Validation Failures | High | DMS, ASI, MON | L2 | Foundational–Hardening |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | SCS, ASI, MON | L1–L2 | Foundational–Hardening |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | GOV, DMS, MON | L1–L2 | Foundational–Advanced |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | GOV, DMS, IRS | L2–L3 | Foundational–Advanced |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | DMS, MON, GOV | L2 | Hardening–Advanced |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | DMS, GOV, MON | L2 | Hardening–Advanced |
| DSGAI11 | Cross-Context Conversation Bleed | High | DMS, ASI, MON | L2 | Foundational–Hardening |
| DSGAI12 | Unsafe NL Data Gateways | Critical | ASI, MON, DMS | L1–L2 | Foundational–Advanced |
| DSGAI13 | Vector Store Platform Security | High | DMS, SCS, MON | L1–L2 | Foundational–Hardening |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | GOV, MON, DMS | L1–L2 | Foundational–Hardening |
| DSGAI15 | Over-Broad Context Windows | High | DMS, ASI, GOV | L2 | Foundational–Hardening |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | ASI, GOV, MON | L1–L2 | Foundational–Hardening |
| DSGAI17 | Data Availability & Resilience Failures | High | L1, IRS, MON | L1–L2 | Foundational–Advanced |
| DSGAI18 | Inference & Data Reconstruction | High | DMS, ASI, GOV | L2 | Hardening–Advanced |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | GOV, DMS, MON | L2 | Foundational–Hardening |
| DSGAI20 | Model Exfiltration & IP Replication | High | DMS, ASI, MON | L2 | Hardening–Advanced |
| DSGAI21 | Disinformation via Data Poisoning | High | DMS, ASI, GOV | L2–L3 | Hardening–Advanced |

---

## Audience tags

- **EU organisation subject to NIS2** — full file, ENISA framework alignment for GenAI data security programme
- **EU AI Act compliance lead** — L2 AI-specific DMS controls, high-risk AI system evidence under Articles 10 and 15
- **CISO (European enterprise)** — GOV domain entries, risk management alignment
- **Data protection officer** — DMS, GOV entries for GDPR Article 30 records of processing
- **Security engineer** — ASI, DMS, MON technical control entries
- **Incident responder** — IRS domain entries, breach response for GenAI data
- **OT / critical infrastructure operator** — L3 sector-specific entries, DSGAI04/DSGAI12/DSGAI17

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

Sensitive data — PII, credentials, financial records, proprietary
code — leaks from GenAI systems through model outputs, RAG retrieval,
embedding exposure, or observability pipelines. ENISA DMS (Data and
Model Security) is the primary domain — covering training data
governance, output monitoring, and privacy-preserving techniques
as core L2 AI-specific controls.

**Real-world references:**
- Samsung source code leak via ChatGPT (2023)
- Multiple healthcare RAG deployments surfacing PHI through
  over-permissive vector store retrieval (2024)

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Training data governance | All data in GenAI scope classified and governed — training corpora, RAG sources, embeddings, and outputs subject to DMS practices |
| Monitoring and Detection (MON) | L1–L2 | Output monitoring and DLP | DLP on all GenAI output channels — AI-specific monitoring covering sensitive data patterns before delivery to consumers |
| Governance and Risk (GOV) | L2 | Privacy risk management | GDPR and EU AI Act Article 10 data governance obligations addressed for all GenAI data assets |
| General ICT — Data Protection | L1 | Encryption and access control | Training data, embeddings, and RAG stores encrypted at rest and in transit; least-privilege access enforced |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Data Protection: Encrypt all sensitive data in
  GenAI scope at rest and in transit — training datasets,
  embedding stores, RAG document stores, prompt caches
- L1 Access Control: Least-privilege access to all GenAI
  data sources — RAG retrieval enforces user authorisation
  scope per document classification
- GOV: Establish AI data governance policy — classify all
  GenAI assets, assign data owners, document in GDPR
  Article 30 records of processing

**Hardening (L2)**
- DMS: Implement data classification policy covering all
  GenAI assets — training data, embeddings, and outputs
  all classified with handling requirements documented
  as DMS evidence
- MON: Deploy DLP on all GenAI output channels —
  AI-specific monitoring covering PII and sensitive
  patterns before delivery

**Advanced (L2)**
- DMS: Apply differential privacy in training for sensitive
  corpora — ENISA privacy-preserving technique practice
- ASI: Conduct model inversion red team — ENISA
  adversarial testing applied to data reconstruction attacks

#### EU AI Act alignment

Article 10 data governance obligations apply to all data used in
training and inference — ENISA DMS practices are the technical
implementation guidance for Article 10 compliance.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.11/A.8.12 — NIST AI RMF MS-2.6 — EU AI Act Art. 10

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical

AI agents inherit and cache credentials that attackers exploit
for lateral movement. ENISA ASI (AI System Integrity) addresses
this through agent-specific access control requirements — agents
must not accumulate or retain credentials beyond the scope required
for the current task.

**Real-world references:**
- LangChain agent credential caching vulnerabilities (2024)
- AutoGPT API key exposure in agent memory (2023)

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| AI System Integrity (ASI) | L2 | Agent access control | Agents operate under least-privilege credential scope — credential lifetime bounded to agent session, scope documented in AI risk assessment |
| Governance and Risk (GOV) | L2 | AI risk management | Agent credential policy documented in AI governance framework — scope, lifetime, rotation, revocation all covered |
| Monitoring and Detection (MON) | L1–L2 | Credential usage monitoring | All agent credential operations logged — anomaly detection covers unexpected scope expansion or access outside session bounds |
| General ICT — Access Control | L1 | Identity and access management | Short-lived tokens for all agent interactions — secrets management integrated with IAM platform |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Access Control: Issue short-lived tokens for all
  agent interactions — credentials expire at session end,
  no persistent credential caching in agent memory
- L1 Secrets Management: Store all agent secrets in a
  secrets manager — never in environment variables,
  configuration files, or agent memory stores

**Hardening (L2)**
- ASI: Enforce least-privilege credential scope per agent
  role — scope defined in AI risk assessment, reviewed
  at each deployment
- GOV: Document agent credential policy in AI governance
  framework — lifetime, scope, rotation interval, and
  revocation procedure
- MON: Log all agent credential operations — anomaly
  detection for scope expansion or after-session access

**Advanced (L2)**
- ASI: Red team agent credential extraction paths —
  test whether credentials appear in outputs, logs,
  memory stores, or tool payloads
- Implement per-task ephemeral credentials — each
  agent task receives a fresh, scoped credential that
  cannot be reused after task completion

#### EU AI Act alignment

Article 15 technical robustness requirements for high-risk AI
systems include identity and access control — ENISA ASI agent
access control practices provide the technical implementation.

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://github.com/hashicorp/vault |
| AWS Secrets Manager | Commercial | https://aws.amazon.com/secrets-manager/ |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: OWASP NHI Top 10 — NIST AI RMF GV-1.6 — EU AI Act Art. 15

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High

Employees use unapproved AI tools and services, creating unsanctioned
data flows outside the organisation's governance and monitoring
perimeter. ENISA GOV (Governance and Risk) addresses this through
AI risk management policies that require all AI system use to be
authorised and all data flows to be documented.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Governance and Risk (GOV) | L2 | AI use policy and authorisation | Acceptable use policy covers all GenAI services — unapproved use is a policy violation; AI asset register maintained |
| Monitoring and Detection (MON) | L1–L2 | Network monitoring and DLP | Network-level detection of data flows to unapproved AI endpoints — DLP covering SaaS AI API calls |
| Supply Chain Security (SCS) | L2 | Third-party AI risk | All AI services assessed before authorisation — vendor security review, data processing agreement, sub-processor disclosure |
| General ICT — Network | L1 | Network access control | Egress filtering to block unapproved AI service domains; proxy logging of AI API calls |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Network: Block known unsanctioned AI service
  domains at egress — maintain approved list, log
  all AI API calls through proxy
- GOV: Publish and enforce AI acceptable use policy —
  all GenAI service use requires prior authorisation,
  consequences for policy violation documented

**Hardening (L2)**
- GOV: Maintain AI asset register — all approved AI
  services inventoried with data classification, business
  owner, and vendor risk assessment documented
- SCS: Require vendor security review and DPA before
  any AI service is approved — sub-processor disclosure
  required for all AI services processing personal data
- MON: Deploy DLP covering AI API call patterns —
  alert on data volume, classification, or destination
  anomalies in AI-related traffic

**Advanced (L2)**
- Implement CASB or AI-aware proxy for all AI service
  access — enforce data classification labels at the
  network boundary
- GOV: Regular AI asset register audits — identify
  services in use that are not in the register

#### EU AI Act alignment

AI governance obligations require organisations to maintain
visibility over all AI systems in use — ENISA GOV practices
provide the framework for AI asset management and acceptable
use policy.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Netskope CASB | Commercial | https://www.netskope.com |
| Microsoft Defender for Cloud Apps | Commercial | https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-cloud-apps |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- Agentic Top 10: ASI04 Agentic Supply Chain
- Other frameworks: ISO 27001 A.5.23 — NIST AI RMF GV-1.7 — EU AI Act Art. 9

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical

Attackers corrupt training data, model weights, embeddings, or
fine-tuning corpora to introduce backdoors or biased behaviour.
ENISA DMS (Data and Model Security) is the primary domain —
covering data integrity, model verification, and adversarial
robustness as L2 AI-specific controls directly addressing
poisoning attacks.

**Real-world references:**
- Nightshade image poisoning tool (2024) — demonstrated
  training data corruption at scale
- RAG corpus poisoning enabling downstream prompt injection (2024)

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Training data integrity | All training data sources verified — provenance documented, anomaly detection on data pipelines, integrity checks before ingestion |
| AI System Integrity (ASI) | L2 | Model integrity verification | Model weights verified before deployment — cryptographic signatures, behavioural baseline testing for unexpected outputs |
| Monitoring and Detection (MON) | L2 | AI-specific anomaly detection | Runtime monitoring for unexpected model behaviour — output distribution drift, sudden accuracy changes, anomalous activation patterns |
| Supply Chain Security (SCS) | L1–L2 | Dataset supply chain | All external training datasets treated as untrusted supply chain components — provenance, quality review, and integrity verification before use |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- DMS: Implement data provenance tracking for all
  training corpora — source, version, integrity hash
  documented before any data enters the pipeline
- DMS: Deploy anomaly detection on training and
  fine-tuning data pipelines — statistical outlier
  detection, label consistency checks
- ASI: Verify model weight integrity before deployment
  — cryptographic signatures and hash-based baseline
  as ENISA model integrity practice
- SCS: Treat all external datasets as untrusted supply
  chain components — security review before ingestion

**Advanced (L2)**
- ASI: Red team deployed models for backdoor behaviour
  — test with trigger inputs across all deployment
  configurations before production release
- DMS: Apply data sanitisation techniques —
  uncertainty training, activation clustering, spectral
  signatures to detect poisoned samples
- L3 (critical infrastructure): Apply IEC 62443 data
  integrity requirements to OT AI training pipelines

#### EU AI Act alignment

Article 10 requires data governance for training data integrity —
ENISA DMS practices implement Article 10 requirements for poisoning
risk. Article 15 adversarial robustness requirements are addressed
by ASI red teaming for backdoor detection.

#### Tools

| Tool | Type | Link |
|---|---|---|
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| Armory | Open-source | https://github.com/twosixlabs/armory |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0020 — NIST AI RMF MS-3.3 — EU AI Act Art. 10/15

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High

GenAI systems ingest data without sufficient validation — malformed,
adversarial, or inconsistent data corrupts model behaviour or
pipeline outputs. ENISA DMS data integrity practices and ASI
verification controls together address this as both a data pipeline
and system integrity concern.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Data quality and validation | All data entering GenAI pipelines validated — schema checks, anomaly detection, and quality gates before model ingestion or RAG indexing |
| AI System Integrity (ASI) | L2 | Input validation requirements | LLM and embedding inputs validated for format, length, and content — AI system integrity requirements extend to data pipeline boundaries |
| Monitoring and Detection (MON) | L2 | Pipeline anomaly detection | Continuous monitoring of data pipeline quality metrics — alerts on schema violations, unexpected distributions, or sudden quality drops |
| General ICT — Secure Development | L1 | Input validation as secure development | Data validation implemented as a secure development requirement for all GenAI pipeline ingestion points |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Secure Development: Implement data validation
  at all GenAI pipeline ingestion points — schema
  validation, type checks, and content bounds enforced
  as secure development requirements

**Hardening (L2)**
- DMS: Deploy data quality gates before model ingestion
  and RAG indexing — schema validation, statistical
  profiling, and outlier detection at each pipeline stage
- ASI: Include data validation in AI system integrity
  verification — test with malformed, adversarial, and
  boundary inputs before each deployment
- MON: Monitor pipeline data quality metrics continuously
  — alert on schema violations or distribution anomalies

**Advanced (L2)**
- DMS: Implement data lineage tracking — every data
  record traceable from ingestion source to model output
  with quality check results at each stage
- ASI: Red team data validation controls — test whether
  adversarially crafted inputs can bypass validation gates

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |
| Pandera | Open-source | https://github.com/unionai-oss/pandera |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning
- Other frameworks: ISO 27001 A.8.28 — NIST AI RMF MS-2.5 — EU AI Act Art. 10

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange

**Severity:** High

Data exchanged between GenAI systems and external tools, plugins,
or sub-agents is insufficiently secured — credentials, sensitive
data, or malicious payloads traverse these interfaces. ENISA SCS
(Supply Chain Security) and ASI together address this through
third-party component security and AI system integrity controls.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Supply Chain Security (SCS) | L1–L2 | Third-party component security | All tools, plugins, and agent connectors treated as supply chain components — security assessment before integration, ongoing monitoring |
| AI System Integrity (ASI) | L2 | Tool and plugin integrity | Tool descriptors and API responses validated before use — content received from external tools treated as untrusted input |
| Monitoring and Detection (MON) | L1–L2 | Tool call monitoring | All tool invocations logged — data volumes, destination, and content patterns monitored for anomalies |
| General ICT — Supply Chain | L1 | ICT supply chain security | Plugin SBOM maintained — all integration components inventoried, vulnerabilities tracked |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Supply Chain: Maintain plugin and tool SBOM —
  every integration component inventoried with version,
  source, security review status
- L1 Network: Restrict tool API calls to approved
  destinations — egress filtering on agent outbound
  connections

**Hardening (L2)**
- SCS: Apply ENISA third-party security practices to
  all tool and plugin vendors — security assessment,
  DPA where personal data is shared, vulnerability
  disclosure SLA before integration
- ASI: Validate tool responses before processing —
  treat all external tool output as untrusted input,
  schema and content validation enforced
- MON: Log all tool invocations with data context —
  alert on data exfiltration patterns or unexpected
  destination addresses

**Advanced (L2)**
- ASI: Red team tool integration points — test whether
  poisoned tool responses can manipulate agent behaviour
  or extract sensitive data
- Implement tool call sandboxing — isolate tool
  execution from agent memory and credential store

#### Tools

| Tool | Type | Link |
|---|---|---|
| Semgrep | Open-source | https://github.com/returntocorp/semgrep |
| OWASP Dependency-Check | Open-source | https://github.com/jeremylong/DependencyCheck |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities, LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse & Exploitation, ASI04 Agentic Supply Chain
- Other frameworks: NIST AI RMF MP-5.1 — ISO 27001 A.5.22 — EU AI Act Art. 9

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High

GenAI systems lack data classification, lifecycle management, or
governance policies — data accumulates across training, RAG, and
embedding stores without clear ownership, retention limits, or
deletion capability. ENISA GOV (Governance and Risk) is the primary
domain — AI data governance is an explicit ENISA L2 requirement.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Governance and Risk (GOV) | L2 | AI data governance | Comprehensive data governance policy for all GenAI assets — classification, ownership, retention, deletion, and unlearning capability documented |
| Data and Model Security (DMS) | L2 | Data lifecycle management | Data lifecycle controls for training corpora, embeddings, and RAG stores — retention periods enforced, deletion verified |
| Monitoring and Detection (MON) | L1–L2 | Data asset monitoring | Data asset inventory monitored for stale or unclassified assets — alerts on policy violations |
| General ICT — Data Protection | L1 | Encryption and access control | Classified data protected per classification level — access control enforced at storage layer |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- GOV: Establish AI data classification policy —
  all GenAI data assets classified before use;
  handling requirements per classification level
  documented and enforced
- L1 Data Protection: Apply access controls based
  on data classification — least-privilege enforced
  at storage layer for all GenAI data assets

**Hardening (L2)**
- GOV: Implement data lifecycle management for all
  GenAI assets — retention periods, archival procedures,
  and verified deletion documented per asset
- DMS: Maintain GenAI data asset inventory — all
  training datasets, RAG corpora, embedding stores,
  and fine-tuning datasets registered with owner,
  classification, and lifecycle status
- GOV: Establish AI unlearning capability — mechanism
  to remove specific data subjects' data from deployed
  models in response to GDPR Article 17 requests

**Advanced (L2)**
- DMS: Implement automated classification on all
  GenAI data ingestion — classify before storage,
  not after
- GOV: Quarterly data governance review — audit
  asset inventory against classification policy,
  remediate stale assets

#### EU AI Act alignment

Articles 10 and 12 require data governance and record-keeping
for high-risk AI systems — ENISA GOV data governance practices
provide the technical implementation of these obligations.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.5.12/A.5.13 — NIST AI RMF GV-1.6 — EU AI Act Art. 10/12

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High

GenAI deployments violate data protection, AI regulation, or
sector-specific requirements through inadequate controls or
undocumented processing. ENISA GOV addresses this through AI
risk management programme requirements that explicitly incorporate
regulatory obligations — EU AI Act and NIS2 compliance are
designed as outcomes of the GOV domain.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Governance and Risk (GOV) | L2–L3 | Regulatory compliance management | All applicable regulations identified and mapped to AI controls — EU AI Act, GDPR, NIS2, sector-specific obligations tracked in AI governance programme |
| Data and Model Security (DMS) | L2 | Compliance-driven data controls | Data controls designed to meet regulatory requirements — GDPR Article 10 training data obligations, NIS2 data security measures |
| Incident Response (IRS) | L2–L3 | Regulatory breach reporting | AI incident response plan includes regulatory notification procedures — NIS2 Article 23 significant incident reporting, GDPR breach notification |
| General ICT — Governance | L1 | Policies and procedures | AI acceptable use and data protection policies document regulatory obligations and controls |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- GOV: Document all applicable regulatory requirements
  for each GenAI deployment — EU AI Act risk class,
  GDPR lawful basis, NIS2 entity classification,
  sector-specific obligations
- L1 Governance: Update AI-related policies to
  reflect current regulatory requirements — review
  at least annually or when regulations change

**Hardening (L2)**
- GOV: Map each regulatory requirement to a specific
  technical control in the AI security programme —
  traceability from obligation to implementation evidence
- IRS: Include regulatory breach procedures in AI
  incident response plan — NIS2 Article 23 notification
  timeline, GDPR 72-hour breach notification, sector
  regulator reporting requirements
- DMS: Ensure technical controls provide audit-ready
  evidence — logs, records, and testing results
  retained per regulatory minimum

**Advanced (L2–L3)**
- GOV: Maintain regulatory watch programme — monitor
  EU AI Act implementing acts, ENISA guidelines, and
  sector-specific AI regulation developments
- L3 (NIS2 essential entities): Align AI security
  programme with NIS2 technical measures — audit
  annually against ENISA NIS2 guidelines

#### EU AI Act alignment

ENISA's framework is designed to support EU AI Act compliance.
GOV domain practices address Articles 9 (risk management system),
17 (quality management), and 72 (post-market monitoring) directly.

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| IBM OpenPages | Commercial | https://www.ibm.com/products/openpages |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI07 Data Governance, Lifecycle & Classification
- Other frameworks: ISO 27001 A.5.31 — NIST AI RMF GV-4.2 — EU AI Act Art. 9/17/72

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Sensitive data embedded in images, audio, video, or documents
passes through GenAI systems without adequate controls — modality
switching creates blind spots in DLP and monitoring. ENISA DMS
extends to all modalities processed by AI systems as part of the
data governance scope.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Multimodal data governance | Data classification and handling requirements apply equally across all modalities — images, audio, video, and documents governed as GenAI assets |
| Monitoring and Detection (MON) | L2 | Multimodal output monitoring | DLP and monitoring extended to cover all output modalities — AI-specific monitoring for sensitive content in generated images, audio, or documents |
| Governance and Risk (GOV) | L2 | Multimodal risk assessment | AI risk assessment explicitly covers multimodal data flows — blind spots between modality types documented and controlled |
| General ICT — Data Protection | L1 | Cross-channel data controls | Encryption and access control applied uniformly across all modalities stored or processed by GenAI systems |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- DMS: Extend data classification scope to all GenAI
  modalities — images, audio, video, and documents
  classified with the same rigour as text data
- MON: Deploy multimodal DLP on all GenAI output
  channels — optical character recognition and image
  classification on generated content before delivery
- GOV: Update AI risk assessment to explicitly cover
  multimodal data flows — document controls for each
  modality type in scope

**Advanced (L2)**
- ASI: Red team multimodal data extraction paths —
  test whether sensitive data embedded in one modality
  can be extracted via a different output modality
- DMS: Implement content watermarking for generated
  multimodal outputs — enable forensic attribution
  of leaked content

#### Tools

| Tool | Type | Link |
|---|---|---|
| AWS Rekognition | Commercial | https://aws.amazon.com/rekognition/ |
| Google Cloud DLP | Commercial | https://cloud.google.com/dlp |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.12 — NIST AI RMF MS-2.6 — EU AI Act Art. 10

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium

Synthetic data used for training or testing re-identifies original
subjects, or anonymisation is insufficient against inference attacks.
ENISA DMS privacy-preserving techniques address this through
specific L2 AI controls for synthetic data quality and re-identification
risk assessment.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Privacy-preserving techniques | Synthetic data generation validated against re-identification risk — formal anonymisation assessments documented as DMS evidence |
| Governance and Risk (GOV) | L2 | Privacy risk management | Re-identification risk included in AI privacy impact assessment — treatment controls and residual risk accepted by data protection officer |
| Monitoring and Detection (MON) | L2 | Synthetic data quality monitoring | Quality and privacy metrics monitored for all synthetic datasets — drift in re-identification risk triggers re-assessment |
| General ICT — Data Protection | L1 | Data protection by design | Anonymisation requirements established at design time — not applied as an afterthought to an already-designed pipeline |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- DMS: Conduct formal anonymisation assessment for
  all synthetic datasets used in GenAI — evaluate
  k-anonymity, l-diversity, and differential privacy
  metrics before use
- GOV: Include re-identification risk in AI privacy
  impact assessment — document residual risk and
  obtain data protection officer sign-off
- MON: Monitor synthetic data quality over time —
  re-assess anonymisation strength if the underlying
  model or data distribution changes

**Advanced (L2)**
- DMS: Apply differential privacy with proven epsilon
  budgets to all synthetic data generation for sensitive
  corpora — ENISA privacy-preserving technique practice
- ASI: Red team re-identification attacks against
  synthetic datasets before production use

#### Tools

| Tool | Type | Link |
|---|---|---|
| ARX Data Anonymization Tool | Open-source | https://arx.deidentifier.org |
| Gretel.ai | Commercial | https://gretel.ai |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.8.11 — NIST AI RMF GV-1.6 — GDPR Recital 26

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High

Context from one user session leaks into another — conversation
history, cached embeddings, or shared context windows expose one
user's data to another. ENISA DMS and ASI together address this
as both a data isolation failure and an AI system integrity issue.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Session isolation requirements | Strict session boundary enforcement for all GenAI deployments — conversation context not shared across user sessions |
| AI System Integrity (ASI) | L2 | Context isolation testing | AI system integrity verification includes cross-session isolation testing — no context leakage across session boundaries |
| Monitoring and Detection (MON) | L2 | Cross-session anomaly detection | Monitoring for unexpected data patterns that indicate context leakage between sessions |
| General ICT — Data Protection | L1 | Tenant isolation | Multi-tenant GenAI deployments implement strict tenant isolation at the infrastructure layer |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Data Protection: Implement tenant isolation at
  the infrastructure layer for all multi-tenant GenAI
  deployments — separate context stores per tenant

**Hardening (L2)**
- DMS: Enforce session boundary controls — conversation
  history, cached context, and embeddings isolated per
  user session with cryptographic separation
- ASI: Include cross-session isolation in AI system
  integrity testing — test data leakage across session
  boundaries before each deployment
- MON: Monitor for cross-session data patterns —
  alert on unexpected content appearing in sessions
  where it was not introduced

**Advanced (L2)**
- ASI: Red team session isolation controls — test
  whether crafted inputs can extract prior session
  context from shared infrastructure
- DMS: Implement context window scrubbing — verify
  no PII or sensitive data persists in shared caches
  after session termination

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Azure AI Content Safety | Commercial | https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM07 System Prompt Leakage
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3 — NIST AI RMF MP-2.3 — EU AI Act Art. 10

---

### DSGAI12 — Unsafe NL Data Gateways

**Severity:** Critical

Natural language interfaces to databases and APIs execute
unvalidated queries — prompt injection drives unauthorised data
access or exfiltration through the NL gateway. ENISA ASI and MON
address this as both an AI system integrity failure and a monitoring
gap requiring AI-specific controls.

**Real-world references:**
- Text-to-SQL injection attacks against enterprise NL database
  interfaces surfacing unrestricted data access (2024)

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| AI System Integrity (ASI) | L2 | Input validation and query control | All NL gateway inputs validated and query scope enforced — generated queries reviewed before execution as AI system integrity requirement |
| Monitoring and Detection (MON) | L1–L2 | Query monitoring | All NL gateway queries logged — anomaly detection for unexpected data volumes, query patterns, or access scope |
| Data and Model Security (DMS) | L2 | Data access governance | Data access through NL gateways governed by the same classification and authorisation controls as direct API access |
| General ICT — Access Control | L1 | Query authorisation | NL gateway operates under database least-privilege credentials — cannot execute DDL, cannot access tables outside defined scope |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Access Control: Issue least-privilege database
  credentials to all NL gateways — read-only where
  appropriate, table scope restricted to business need
- L1 Secure Development: Implement query scope
  enforcement — NL gateway cannot execute DDL or
  access data outside authorised scope

**Hardening (L2)**
- ASI: Deploy query validation layer between NL
  model and database — generated queries reviewed
  against authorised query patterns before execution
- MON: Log all NL gateway query executions with
  data volume and table access — alert on anomalous
  access patterns or unusual data volumes
- DMS: Apply same data classification controls to
  NL gateway access as to direct API access —
  authorisation enforced at the data layer

**Advanced (L2)**
- ASI: Red team NL gateway with prompt injection
  payloads — test whether injection can bypass query
  scope restrictions or extract out-of-scope data
- Implement NL query output DLP — scan query results
  before delivery to the requesting user or agent

#### EU AI Act alignment

Article 15 technical robustness requirements for high-risk AI
systems apply to NL interfaces accessing sensitive data — ENISA
ASI controls provide the implementation framework.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Rebuff | Open-source | https://github.com/protectai/rebuff |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM05 Insecure Output Handling
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse & Exploitation
- Other frameworks: OWASP ASVS V5 — NIST AI RMF MP-2.3 — EU AI Act Art. 15

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector databases storing embeddings are inadequately secured —
injection attacks, unauthorised access, or metadata leakage expose
sensitive data encoded in embedding space. ENISA DMS covers
embedding stores as AI-specific data assets requiring L2 security
controls beyond standard database protection.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Embedding store security | Vector stores governed as sensitive AI data assets — classified, access-controlled, encrypted, and integrity-verified |
| Supply Chain Security (SCS) | L1–L2 | Vector database supply chain | Vector database platforms assessed as AI supply chain components — CVEs tracked, security configuration reviewed |
| Monitoring and Detection (MON) | L1–L2 | Vector store access monitoring | All vector store query and mutation operations logged — anomaly detection for unexpected access patterns |
| General ICT — Access Control | L1 | Database access control | Vector stores require authentication and authorisation — no unauthenticated access, least-privilege query scopes |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Access Control: Enforce authentication and
  authorisation on all vector store access —
  no unauthenticated endpoints, least-privilege
  query credentials per application
- L1 Data Protection: Encrypt embeddings at rest
  and in transit — vector stores treated as sensitive
  data assets equivalent to production databases

**Hardening (L2)**
- DMS: Classify embeddings and implement handling
  requirements — embedding stores registered in
  GenAI data asset inventory with classification
  and access policy documented
- SCS: Apply ENISA supply chain practices to vector
  database vendors — security configuration review,
  CVE monitoring, patch management SLA
- MON: Log all vector store operations — alert on
  bulk retrieval, schema modification, or access
  from unexpected sources

**Advanced (L2)**
- DMS: Implement embedding isolation per tenant
  and data classification — prevent cross-tenant
  retrieval through namespace and access control
- ASI: Red team vector store for injection attacks
  and metadata extraction — test whether embedding
  inversion can recover training data

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://github.com/weaviate/weaviate |
| Qdrant | Open-source | https://github.com/qdrant/qdrant |

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3 — NIST AI RMF MP-2.3 — EU AI Act Art. 10

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High

Observability pipelines capture sensitive data in logs, traces,
and metrics — telemetry stores become a high-value target containing
the full history of GenAI system operation including user inputs
and model outputs. ENISA MON and GOV address this as a data
governance failure in the observability layer.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Governance and Risk (GOV) | L2 | Observability data governance | Telemetry data classified and governed — observability pipelines subject to the same data governance policy as primary data assets |
| Monitoring and Detection (MON) | L1–L2 | Log and trace security | Observability stores protected against unauthorised access — access controls, encryption, and retention limits applied to all telemetry |
| Data and Model Security (DMS) | L2 | PII in telemetry | Telemetry pipelines scanned for sensitive data before storage — redaction and masking applied to GenAI inputs and outputs in logs |
| General ICT — Logging | L1 | Log protection | Logs protected from tampering and unauthorised access — separation between security logs and operational telemetry |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Logging: Protect all observability stores from
  unauthorised access — access control and encryption
  equivalent to primary data assets
- GOV: Classify telemetry data — prompts, completions,
  and embeddings in logs are sensitive data assets
  subject to the same classification and handling policy

**Hardening (L2)**
- DMS: Deploy PII scanning on telemetry pipeline —
  redact or mask sensitive data in GenAI logs before
  storage in observability platforms
- GOV: Establish telemetry retention policy — minimum
  necessary retention, automated deletion after
  retention period expires
- MON: Monitor observability store access — alert on
  bulk retrieval or access from non-operational sources

**Advanced (L2)**
- DMS: Implement structured redaction — define what
  fields may appear in telemetry and what must be
  suppressed before storage
- Implement separate security audit log vs operational
  telemetry — security-relevant events retained longer,
  operational data purged per retention policy

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Grafana Loki | Open-source | https://github.com/grafana/loki |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI07 Data Governance, Lifecycle & Classification
- Other frameworks: ISO 27001 A.8.15/A.8.16 — NIST AI RMF GV-1.6 — EU AI Act Art. 12

---

### DSGAI15 — Over-Broad Context Windows

**Severity:** High

Context windows populated with excessive or over-privileged data
expose sensitive information to the model and create exfiltration
opportunities. ENISA DMS and ASI address this through data
minimisation requirements as both a data governance and AI system
integrity concern.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Data minimisation in AI pipelines | Context window population governed by data minimisation principle — only data necessary for the current task included |
| AI System Integrity (ASI) | L2 | Context boundary enforcement | AI system integrity controls include context window scope limits — over-broad context documented as a risk in AI risk assessment |
| Governance and Risk (GOV) | L2 | AI risk assessment | Over-broad context included as a risk factor in AI risk assessment — treatment controls and data minimisation requirements documented |
| General ICT — Data Protection | L1 | Data minimisation | Data minimisation principle applied as a baseline data protection requirement for all AI system design |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Data Protection: Apply data minimisation
  principle to all context window design — only
  data necessary for the task included; excess
  context prevented at design time

**Hardening (L2)**
- DMS: Implement context scope controls — RAG
  retrieval scoped to user authorisation level,
  system prompt reviewed for unnecessary sensitive
  context before deployment
- ASI: Include context scope review in AI system
  integrity verification — document maximum permitted
  context scope per use case
- GOV: Add over-broad context to AI risk register —
  document treatment controls and residual risk

**Advanced (L2)**
- DMS: Implement dynamic context redaction —
  classify context content at runtime and redact
  above-threshold classifications before model ingestion
- ASI: Red team context window extraction paths —
  test whether crafted inputs can surface sensitive
  context content in model outputs

#### Tools

| Tool | Type | Link |
|---|---|---|
| LlamaIndex | Open-source | https://github.com/run-llama/llama_index |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM07 System Prompt Leakage
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: GDPR Art. 5(1)(c) — NIST AI RMF MS-2.5 — EU AI Act Art. 10

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High

AI assistants deployed on endpoints or in browsers access data
beyond their defined scope — reading files, browser history,
or application data without explicit user authorisation for
each access. ENISA ASI and GOV address this through AI agent
scope control as an AI system integrity and governance requirement.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| AI System Integrity (ASI) | L2 | Agent scope enforcement | Endpoint AI assistants operate under explicit, minimal permissions — scope defined and enforced by the underlying platform |
| Governance and Risk (GOV) | L2 | Acceptable use and privacy policy | Privacy policy explicitly covers endpoint AI assistant data collection — user consent, scope disclosure, and opt-out mechanism required |
| Monitoring and Detection (MON) | L1–L2 | Endpoint AI monitoring | Endpoint AI assistant activity logged — data access, network calls, and file operations monitored |
| General ICT — Access Control | L1 | Endpoint access control | Endpoint AI assistants installed with least-privilege permissions — no broad file system or browser data access without per-action authorisation |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Access Control: Deploy endpoint AI assistants
  with least-privilege permissions — no broad file
  system or browser data access; explicit permissions
  required per data category
- GOV: Publish clear privacy policy for endpoint AI
  assistants — scope of data access, retention,
  sharing disclosed before deployment

**Hardening (L2)**
- ASI: Define and enforce explicit scope boundaries
  for endpoint AI assistants — document permitted
  data access in AI risk assessment, enforce at
  the platform level
- MON: Log all endpoint AI assistant data access
  and network calls — alert on access outside
  defined scope
- GOV: Include endpoint AI assistants in AI
  acceptable use policy — employee guidance on
  permitted use and data sharing

**Advanced (L2)**
- ASI: Red team endpoint AI assistant scope controls
  — test whether crafted inputs or application state
  can trigger access to data outside defined scope
- Implement per-session scope confirmation — user
  explicitly approves data access scope at session
  start for sensitive operations

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Intune | Commercial | https://www.microsoft.com/en-us/security/business/endpoint-management/microsoft-intune |
| Carbon Black | Commercial | https://www.vmware.com/products/carbon-black-cloud.html |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- Agentic Top 10: ASI02 Tool Misuse & Exploitation, ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.19 — NIST AI RMF GV-1.7 — EU AI Act Art. 9

---

### DSGAI17 — Data Availability & Resilience Failures

**Severity:** High

GenAI systems lack resilience controls — training data, model
weights, embedding stores, or RAG corpora are deleted, corrupted,
or unavailable, causing service failure or irrecoverable data loss.
ENISA L1 General ICT controls provide the primary resilience
baseline, extended by L2 AI-specific controls for model artefact
recovery.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| General ICT — Business Continuity | L1 | Backup and recovery | All GenAI critical assets backed up — training data, model weights, embedding stores, RAG corpora subject to backup and recovery testing |
| Incident Response (IRS) | L1–L2 | AI incident response | AI incident response plan covers availability failures — model rollback procedure, RAG corpus recovery, embedding store restoration |
| Monitoring and Detection (MON) | L1–L2 | Availability monitoring | GenAI asset availability monitored — alerts on data store unavailability, model health degradation, pipeline failures |
| Data and Model Security (DMS) | L2 | Model artefact protection | Model weights and training artefacts protected against accidental or malicious deletion — versioned storage, immutable backups |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Business Continuity: Implement backup and
  recovery for all GenAI critical assets — training
  data, model weights, embeddings, and RAG corpora
  backed up with tested recovery procedures
- L1 Monitoring: Monitor availability of all GenAI
  data services — alerting on pipeline failures,
  store unavailability, or model health degradation

**Hardening (L2)**
- DMS: Protect model artefacts with versioned,
  immutable storage — model weights and training
  checkpoints stored with deletion protection
  and version history
- IRS: Include AI availability failures in incident
  response plan — model rollback procedure, RACI,
  and recovery time objective documented per asset
- MON: Implement GenAI-specific availability SLIs —
  track model inference latency, RAG retrieval
  success rate, embedding store query health

**Advanced (L2)**
- IRS: Test AI disaster recovery annually —
  verify model rollback, data restoration, and
  service recovery within defined RTOs
- L3 (critical infrastructure): Align GenAI
  resilience requirements with sector-specific
  availability obligations under NIS2

#### EU AI Act alignment

Article 15 requires accuracy, robustness, and cybersecurity
for high-risk AI systems — availability and resilience controls
are a direct Article 15 compliance requirement.

#### Tools

| Tool | Type | Link |
|---|---|---|
| DVC (Data Version Control) | Open-source | https://github.com/iterative/dvc |
| MLflow | Open-source | https://github.com/mlflow/mlflow |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: ISO 27001 A.8.14 — NIST AI RMF MG-2.2 — EU AI Act Art. 15

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High

Attackers extract training data or infer sensitive attributes
through model outputs using membership inference, model inversion,
or attribute inference attacks. ENISA DMS privacy-preserving
techniques and ASI adversarial testing address this as an L2
AI-specific attack requiring specialised controls beyond standard
data protection.

**Real-world references:**
- CVE-2019-20634: Proofpoint model inversion via prediction
  API (CVSS 6.5)
- Multiple membership inference demonstrations against
  large language models using shadow model attacks (2023–2024)

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Privacy-preserving techniques | Differential privacy, output perturbation, and prediction API rate limiting applied as DMS privacy-preserving controls |
| AI System Integrity (ASI) | L2 | Adversarial robustness testing | Inference attack red teaming included in AI system integrity verification — membership inference, model inversion, attribute inference tested before deployment |
| Governance and Risk (GOV) | L2 | Inference attack risk assessment | Inference attack risk documented in AI risk assessment — treatment controls (differential privacy, output restrictions) justified |
| Monitoring and Detection (MON) | L2 | Inference attack monitoring | Prediction API monitoring for inference attack patterns — high-volume, systematic query patterns that indicate shadow model training |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- DMS: Implement prediction output restrictions —
  confidence score truncation, output perturbation,
  and query rate limiting as DMS inference attack
  mitigations
- GOV: Document inference attack risk in AI risk
  assessment — treatment controls justified against
  sensitivity of training data
- MON: Monitor prediction API for inference attack
  patterns — alert on high-volume, systematic query
  patterns

**Advanced (L2)**
- DMS: Apply differential privacy to model training
  for high-sensitivity corpora — formal privacy
  guarantees with documented epsilon budget
- ASI: Red team inference attacks before deployment
  — test membership inference, model inversion, and
  attribute inference against the specific deployment
- DMS: Implement machine unlearning capability for
  GDPR Article 17 compliance — ability to remove
  specific records from trained model behaviour

#### Tools

| Tool | Type | Link |
|---|---|---|
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |
| TensorFlow Privacy | Open-source | https://github.com/tensorflow/privacy |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI10 Synthetic Data & Anonymisation Pitfalls
- Other frameworks: ISO 27001 A.8.11 — NIST AI RMF MS-2.5 — GDPR Art. 17

---

### DSGAI19 — Human-in-Loop & Labeler Overexposure

**Severity:** Medium

Human reviewers and labelers access sensitive data during
fine-tuning, RLHF, or content moderation workflows — exposure
is insufficiently governed, logged, or controlled. ENISA GOV
addresses this through third-party AI supply chain controls
as data labeling services are a supply chain component of the
AI development lifecycle.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Governance and Risk (GOV) | L2 | Third-party human review governance | Data labeling and human review services governed as AI supply chain components — DPA, access controls, and data handling requirements contractually mandated |
| Data and Model Security (DMS) | L2 | Labeling data protection | Data provided to human reviewers classified and minimised — no unnecessary sensitive data in labeling batches |
| Monitoring and Detection (MON) | L1–L2 | Labeler access monitoring | All human reviewer data access logged — access scope, duration, and data volume tracked |
| Supply Chain Security (SCS) | L2 | Labeling supply chain security | Labeling service providers assessed as supply chain components — security controls, sub-contractor restrictions, jurisdiction reviewed |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Access Control: Issue least-privilege, time-limited
  access to human reviewers — access scoped to
  specific labeling task, revoked on completion
- GOV: Execute DPA with all labeling service providers
  — data handling requirements, sub-processor
  restrictions, and breach notification documented

**Hardening (L2)**
- DMS: Minimise sensitive data in labeling batches
  — remove unnecessary PII and sensitive content
  before providing data to reviewers
- SCS: Apply supply chain security assessment to
  labeling vendors — jurisdiction, security controls,
  sub-contractor chain reviewed before engagement
- MON: Log all reviewer data access — track access
  scope, duration, and data volume for audit

**Advanced (L2)**
- DMS: Implement privacy-preserving labeling
  techniques — data perturbation or synthetic
  replacement where full fidelity is not required
  for the labeling task
- GOV: Conduct periodic labeling supply chain audits
  — verify controls are operating as contractually
  required

#### Tools

| Tool | Type | Link |
|---|---|---|
| Scale AI | Commercial | https://scale.com |
| Label Studio | Open-source | https://github.com/HumanSignal/label-studio |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI07 Data Governance, Lifecycle & Classification
- Other frameworks: ISO 27001 A.5.22 — NIST AI RMF MP-5.1 — EU AI Act Art. 10

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High

Adversaries extract model weights, architecture details, or
functional equivalents through model stealing attacks — a targeted
exfiltration of AI intellectual property. ENISA DMS model integrity
controls and SCS supply chain security together address the
protection of model artefacts as high-value AI assets.

**Real-world references:**
- Systematic API query attacks demonstrating functional
  model extraction against commercial LLM APIs (2023–2024)

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Model artefact protection | Model weights and training artefacts protected as high-value IP — access controls, encryption, and exfiltration monitoring |
| AI System Integrity (ASI) | L2 | Model extraction defence | Output restrictions, query rate limiting, and watermarking applied as ASI model extraction defences |
| Monitoring and Detection (MON) | L2 | Model extraction monitoring | API query patterns monitored for model extraction signatures — systematic, high-volume queries from single sources |
| Supply Chain Security (SCS) | L2 | Model distribution security | Model weights protected throughout distribution — signed artefacts, access-controlled distribution channels |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- DMS: Classify model weights as critical IP assets —
  access controls, encryption at rest and in transit,
  and access audit logging equivalent to source code
- ASI: Implement prediction API defences — output
  perturbation, confidence truncation, and per-user
  rate limiting to degrade model extraction attack
  fidelity
- MON: Deploy model extraction detection — alert on
  high-volume, systematic API queries that match
  model extraction signatures

**Advanced (L2)**
- DMS: Apply model watermarking — embed detectable
  signatures in model weights and outputs to enable
  forensic attribution of extracted models
- ASI: Red team model extraction attacks — test
  whether the deployment's API defences prevent
  functional model replication
- SCS: Protect model distribution pipeline —
  cryptographic signatures, access-controlled
  distribution channels, and delivery audit logging

#### Tools

| Tool | Type | Link |
|---|---|---|
| Knockoff Nets detection | Research | https://arxiv.org/abs/1812.02766 |
| ModelScan | Open-source | https://github.com/protectai/modelscan |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning
- Other frameworks: ISO 27001 A.8.24 — NIST AI RMF MS-2.6 — EU AI Act Art. 15

---

### DSGAI21 — Disinformation via Data Poisoning

**Severity:** High

Attackers poison training or fine-tuning data with false information
to cause the model to generate systematic disinformation. ENISA DMS
data integrity controls and ASI adversarial robustness together
address this as both a supply chain and AI system integrity threat
with significant L3 sector-specific implications for critical
infrastructure, healthcare, and financial services.

**Real-world references:**
- Research demonstrations of targeted disinformation injection
  via fine-tuning corpus poisoning (2023–2024)
- RAG corpus poisoning to produce factually incorrect citations
  in academic and legal GenAI applications (2024)

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Training data integrity and provenance | Provenance verification for all fine-tuning corpora — source credibility assessed, integrity verified before ingestion |
| AI System Integrity (ASI) | L2 | Factual accuracy verification | AI system integrity testing includes factual accuracy validation — model outputs tested against ground truth before deployment |
| Governance and Risk (GOV) | L2 | Disinformation risk assessment | Disinformation risk documented in AI risk register — sector-specific severity assessed for healthcare, finance, critical infrastructure |
| L3 — Sector-specific | L3 | High-risk sector controls | For NIS2 essential entities and EU AI Act Annex III deployments — disinformation risk treated as a significant incident category |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- DMS: Verify provenance and credibility of all
  fine-tuning and RAG corpora — source credibility
  scoring, cross-source consistency checking before
  ingestion
- ASI: Include factual accuracy testing in AI system
  integrity verification — test against benchmark
  datasets before deployment and after fine-tuning
- GOV: Document disinformation risk in AI risk register
  — sector-specific impact assessment, treatment controls

**Advanced (L2–L3)**
- ASI: Red team targeted disinformation injection —
  test whether adversarially poisoned content can
  survive data quality controls and affect model outputs
- DMS: Implement output source attribution — model
  outputs include provenance citations enabling
  factual verification
- L3 (NIS2 essential entities, EU AI Act Annex III):
  Treat systematic AI disinformation as a significant
  incident category — include in NIS2 Article 23
  incident reporting threshold assessment

#### EU AI Act alignment

Article 52 transparency obligations require disclosure when AI
generates content that could mislead users — disinformation
controls are a direct Article 52 compliance measure. For
high-risk systems (Annex III), Article 15 robustness requirements
extend to disinformation resilience.

#### Tools

| Tool | Type | Link |
|---|---|---|
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| FactScore | Research | https://github.com/shmsw25/FActScoring |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0020 — NIST AI RMF MS-3.3 — EU AI Act Art. 52

---

## Implementation priority

| Priority | DSGAI IDs | Rationale | ENISA Layer |
|---|---|---|---|
| P1 — Critical, deploy first | DSGAI01, DSGAI02, DSGAI04, DSGAI12 | Critical severity — data leakage, credential exposure, poisoning, NL gateway attacks | L1–L2 |
| P2 — High, deploy within 90 days | DSGAI05, DSGAI06, DSGAI07, DSGAI11, DSGAI13 | Data integrity, tool exchange, governance, context isolation, vector store security | L1–L2 |
| P3 — High, deploy within 180 days | DSGAI03, DSGAI08, DSGAI09, DSGAI14, DSGAI15, DSGAI16, DSGAI17 | Governance, compliance, multimodal, telemetry, context, endpoint, resilience | L1–L3 |
| P4 — Medium/Advanced, deploy within 1 year | DSGAI10, DSGAI18, DSGAI19, DSGAI20, DSGAI21 | Synthetic data, inference attacks, labeler overexposure, model exfiltration, disinformation | L2 |

---

## References

- [ENISA Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai)
- [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [EU AI Act — Official text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [NIS2 Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555)
- [GDPR Article 10 — Data used for training](https://gdpr-info.eu/art-10-gdpr/)
- [ENISA AI Cybersecurity Guidelines for the EU AI Act](https://www.enisa.europa.eu/topics/artificial-intelligence)

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-27 | Initial release — full DSGAI01–DSGAI21 mapping to ENISA Multilayer Framework |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the OWASP GenAI Data Security Initiative.
Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
