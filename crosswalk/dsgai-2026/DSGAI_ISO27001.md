<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks & Mitigations 2026 (DSGAI01–DSGAI21)
  Framework   : ISO/IEC 27001:2022 — Information Security Management Systems
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × ISO/IEC 27001:2022

Mapping the [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html) —
the world's most widely adopted information security management system
standard, certified by over 70,000 organisations globally.

ISO 27001:2022 is the baseline information security certification for
enterprise supplier assessments, regulated industry compliance, and
public sector procurement across Europe, Asia-Pacific, and the Americas.
Its 2022 revision introduced 11 new controls directly relevant to cloud,
threat intelligence, and data leakage prevention — making it the most
applicable version for GenAI data security mapping.

This file covers all 21 DSGAI entries. ISO 27001 controls are from
Annex A of the 2022 edition. Where a DSGAI entry also intersects with
GDPR or EU AI Act compliance obligations, this is noted — ISO 27001
certification does not substitute for those obligations but provides
foundational evidence of security controls.

---

## ISO 27001:2022 Annex A control domains

| Domain | Controls | Scope |
|---|---|---|
| A.5 Organisational controls | A.5.1–A.5.37 | Policies, roles, supplier security, incident management |
| A.6 People controls | A.6.1–A.6.8 | Screening, training, remote working |
| A.7 Physical controls | A.7.1–A.7.14 | Physical access, secure areas, equipment |
| A.8 Technological controls | A.8.1–A.8.34 | Access, cryptography, logging, secure development, DLP |

**New in 2022 (directly relevant to GenAI):**
A.5.7 Threat intelligence · A.5.23 Cloud services security ·
A.5.30 ICT readiness for business continuity ·
A.8.9 Configuration management · A.8.10 Information deletion ·
A.8.11 Data masking · A.8.12 Data leakage prevention ·
A.8.16 Monitoring activities · A.8.23 Web filtering ·
A.8.28 Secure coding

---

## Quick-reference summary

| ID | Name | Severity | Primary ISO 27001:2022 Controls | Tier | Scope |
|---|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | A.8.11, A.8.12, A.5.12, A.8.3 | Foundational–Advanced | Both |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | A.8.2, A.5.16, A.5.17, A.8.15 | Foundational–Advanced | Both |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | A.5.10, A.5.23, A.8.12, A.5.1 | Foundational–Hardening | Both |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | A.8.8, A.5.19, A.8.27, A.8.29 | Hardening–Advanced | Both |
| DSGAI05 | Data Integrity & Validation Failures | High | A.8.26, A.8.28, A.8.29, A.8.9 | Foundational–Hardening | Build |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | A.5.19, A.5.20, A.8.3, A.5.23 | Foundational–Hardening | Both |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | A.5.9, A.5.12, A.5.13, A.8.10 | Foundational–Advanced | Both |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | A.5.31, A.5.34, A.5.36, A.5.1 | Foundational–Advanced | Both |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | A.8.11, A.8.12, A.5.12, A.8.24 | Hardening–Advanced | Both |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | A.5.34, A.8.11, A.5.12, A.8.33 | Hardening–Advanced | Build |
| DSGAI11 | Cross-Context Conversation Bleed | High | A.8.3, A.5.14, A.8.11, A.8.15 | Foundational–Hardening | Build |
| DSGAI12 | Unsafe NL Data Gateways | Critical | A.8.26, A.8.3, A.8.28, A.8.29 | Foundational–Advanced | Build |
| DSGAI13 | Vector Store Platform Security | High | A.8.3, A.8.24, A.8.15, A.8.12 | Foundational–Hardening | Both |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | A.8.15, A.8.12, A.5.12, A.8.11 | Foundational–Hardening | Build |
| DSGAI15 | Over-Broad Context Windows | High | A.8.3, A.5.12, A.8.11, A.5.14 | Foundational–Hardening | Build |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | A.8.1, A.8.7, A.5.10, A.8.12 | Foundational–Hardening | Both |
| DSGAI17 | Data Availability & Resilience Failures | High | A.5.30, A.8.13, A.8.14, A.5.24 | Foundational–Advanced | Both |
| DSGAI18 | Inference & Data Reconstruction | High | A.8.11, A.5.34, A.8.24, A.8.12 | Hardening–Advanced | Both |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | A.5.34, A.6.3, A.5.20, A.8.11 | Foundational–Hardening | Both |
| DSGAI20 | Model Exfiltration & IP Replication | High | A.5.12, A.8.3, A.8.12, A.5.19 | Hardening–Advanced | Both |
| DSGAI21 | Disinformation via Data Poisoning | High | A.5.7, A.8.8, A.8.27, A.8.29 | Hardening–Advanced | Both |

---

## Audience tags

- **CISO / governance** — full file, ISO 27001 ISMS extension for GenAI
- **Auditor / certifier** — control mapping evidence for ISO 27001 audits
- **DPO** — DSGAI01, DSGAI02, DSGAI08, DSGAI10, DSGAI19
- **Security engineer** — DSGAI04, DSGAI05, DSGAI12, DSGAI13
- **ML / AI engineer** — DSGAI04, DSGAI07, DSGAI10, DSGAI18
- **Compliance officer** — DSGAI07, DSGAI08, DSGAI10
- **OT engineer** — DSGAI04, DSGAI12, DSGAI17 with ISA 62443 crosswalk

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

Sensitive data — PII, credentials, financial records, proprietary source
code — leaks from GenAI systems through model outputs, RAG retrieval,
embedding exposure, or observability pipelines. The attack surface includes
model memorisation of training data, over-permissive RAG retrieval,
and improperly redacted outputs.

**Real-world references:**
- Samsung source code leak (2023) — employees fed proprietary code
  to LLM, surfaced in outputs
- Multiple healthcare RAG deployments surfacing PHI through
  over-permissive vector store retrieval (2024)

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Data masking | A.8.11 | Technological | Masking or redaction of sensitive data in LLM outputs, RAG results, and prompts |
| Data leakage prevention | A.8.12 | Technological | DLP controls on all GenAI output channels — model API, chat interfaces, logs |
| Classification of information | A.5.12 | Organisational | All data in GenAI scope classified — training data, RAG corpora, outputs, embeddings |
| Information access restriction | A.8.3 | Technological | Access controls on RAG data sources limiting retrieval to authorised user scope |
| Labelling of information | A.5.13 | Organisational | Classification labels propagated to derived assets — embeddings, caches, summaries |

#### Mitigations by tier

**Foundational**
- A.5.12: Classify all data entering GenAI scope — training corpora,
  RAG sources, prompt templates, and outputs — before ingestion
- A.8.3: Implement access controls on RAG retrieval — users should
  only retrieve documents they are authorised to access
- A.8.12: Deploy DLP on all model output channels — API responses,
  chat interfaces, log pipelines — scanning for PII and secrets

**Hardening**
- A.8.11: Implement output redaction for sensitive patterns before
  responses reach users — PII, API keys, internal system names
- A.5.13: Propagate classification labels to all derived assets —
  an embedding of a Confidential document is also Confidential
- Audit RAG access controls per quarter — verify retrieval scope
  matches authorised user access rights

**Advanced**
- Apply differential privacy in training and embedding generation
  for sensitive corpora — document as A.8.11 technical control
- Conduct model inversion red team exercises — validate that
  sensitive training data cannot be reconstructed from outputs
- A.8.12: Implement real-time DLP with automated blocking on
  sensitive pattern detection in output streams

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |
| Private AI | Commercial | https://private-ai.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27701 · EU AI Act Art. 10 · NIST AI RMF GV-1.6 · GDPR Art. 25

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical

AI agents inherit, cache, or misuse credentials — API keys, session
tokens, OAuth grants, SSH keys — exposing them through memory stores,
logs, or tool payloads. Compromised agent credentials enable lateral
movement across all systems the agent has access to.

**Real-world references:**
- Hugging Face Spaces incident — token exposure paths into AI
  data infrastructure
- CVE-2025-54795 — Claude Code confirmation bypass enabling
  execution of untrusted commands

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Privileged access rights | A.8.2 | Technological | Agent credentials managed as privileged access — short-lived, scoped, reviewed |
| Identity management | A.5.16 | Organisational | All agent identities inventoried and lifecycle-managed as non-human identities |
| Authentication information | A.5.17 | Organisational | Secure management of agent credentials — no hardcoding, rotation enforced |
| Logging | A.8.15 | Technological | All agent credential use logged with full context — issuance, invocation, expiry |
| Information access restriction | A.8.3 | Technological | Agent access restricted to minimum scope required per task |

#### Mitigations by tier

**Foundational**
- A.5.16: Inventory all agent identities — include in NHI
  (Non-Human Identity) register alongside service accounts
- A.5.17: Enforce no hardcoded credentials in agent code or
  prompts — use secret managers, rotate on schedule
- A.8.2: Issue short-lived, task-scoped credentials per agent
  invocation — never long-lived shared tokens

**Hardening**
- A.8.15: Log all agent credential operations — issuance, use,
  expiry, and anomalous access patterns — feed into SIEM
- A.8.3: Implement just-in-time (JIT) credential issuance —
  agent receives credentials only for task duration, revoked
  on completion
- Detect credential exposure in agent memory, logs, and tool
  payloads using automated scanning

**Advanced**
- Implement PKI-backed agent identities with signed requests
  for all agents in multi-agent ecosystems
- A.8.2: Apply continuous NHI monitoring — alert on anomalous
  token usage patterns across agent sessions
- Automated credential rotation triggered on any anomaly
  detection signal — not just scheduled rotation

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| Teleport | Open-source/Commercial | https://goteleport.com |
| Entro Security | Commercial | https://entro.security |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- Agentic Top 10: ASI03 Identity & Privilege Abuse, ASI07 Insecure Inter-Agent Comms
- Other frameworks: OWASP NHI Top 10 · AIUC-1 A/B007 · NIST AI RMF MS-2.5

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High

Employees use unapproved GenAI SaaS tools — ChatGPT, Copilot, browser
agents, productivity plugins — and paste sensitive data into external
models outside any formal governance. Vendors may retain, train on, or
mishandle this data with no contractual protections in place.

**Real-world references:**
- Multiple documented incidents of employees pasting customer
  records, internal designs, and source code into public AI tools
- AI-enabled browser extensions retaining sensitive context beyond
  session (2024–2025)

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Acceptable use of assets | A.5.10 | Organisational | Policy explicitly covering acceptable use of AI tools — approved list and prohibited use cases |
| Security for cloud services | A.5.23 | Organisational | Due diligence and security requirements for any cloud-based AI service including shadow AI SaaS |
| Data leakage prevention | A.8.12 | Technological | DLP controls detecting and blocking sensitive data transfer to unapproved AI endpoints |
| Policies for information security | A.5.1 | Organisational | AI acceptable use policy as a formal ISMS policy document |

#### Mitigations by tier

**Foundational**
- A.5.1: Establish and publish an AI acceptable use policy —
  approved tools list, prohibited use cases, data handling
  requirements, and consequences for violation
- A.5.10: Include AI tool usage in acceptable use agreements —
  employees acknowledge restrictions on pasting sensitive data
  into external AI services
- A.8.12: Configure DLP to detect and alert on sensitive data
  transfer to known AI SaaS endpoints

**Hardening**
- A.5.23: Conduct security assessment of all AI SaaS tools before
  approval — data retention, training use, sub-processors,
  cross-border transfers, incident notification terms
- A.8.12: Implement blocking DLP for unapproved AI endpoints —
  not just alerting
- Deploy continuous shadow AI discovery across endpoint, network
  egress, and SaaS access logs

**Advanced**
- Integrate AI security review into formal procurement process —
  AI capabilities embedded in broader SaaS products captured
  at vendor onboarding
- A.5.23: Establish contractual AI data processing requirements
  for all approved AI vendors — zero training use by default
- Implement AI usage analytics — monitor which approved tools
  are used, what data categories are shared, and compliance
  with the acceptable use policy

#### Tools

| Tool | Type | Link |
|---|---|---|
| Zscaler (CASB) | Commercial | https://www.zscaler.com |
| Microsoft Defender for Cloud Apps | Commercial | https://www.microsoft.com/en-us/security |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: EU AI Act Art. 25 · ISO 42001 · NIST AI RMF GV-1.6

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical

Adversaries corrupt training datasets, model weights, fine-tuned
adapters, or supply chain components to embed backdoors or bias model
behaviour — effects are baked into the model and persist across all
downstream deployments until detected and remediated.

**Real-world references:**
- Nightshade (2023) — poison pixels in training images corrupted
  image generation model behaviour
- Multiple malicious models on Hugging Face with embedded backdoors

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Management of technical vulnerabilities | A.8.8 | Technological | Scanning and patching model components and training pipeline dependencies |
| Supplier relationships | A.5.19 | Organisational | Security requirements applied to all third-party training data and model sources |
| Secure system architecture | A.8.27 | Technological | Training pipeline designed with integrity controls and supply chain verification |
| Security testing | A.8.29 | Technological | Adversarial testing of model outputs for poisoning indicators before deployment |
| Configuration management | A.8.9 | Technological | Model versions, adapters, and datasets managed with integrity and change controls |

#### Mitigations by tier

**Foundational**
- A.5.19: Apply supplier security requirements to all training
  data sources — provenance, quality, and integrity guarantees
  required in contractual arrangements
- A.8.9: Implement model version control with integrity hashing —
  detect any unauthorised changes to model artifacts
- Maintain a complete ML SBOM for all production models —
  model, adapters, datasets, training libraries

**Hardening**
- A.8.29: Include poisoning detection in your security testing
  programme — test for backdoor triggers and biased outputs
  before every production promotion
- A.8.27: Design training pipelines with integrity controls —
  anomaly detection on training data distributions, source
  allowlisting, lineage tracking
- Implement model rollback capability — versioned registry
  with clean checkpoint restore on poisoning detection

**Advanced**
- Conduct post-training backdoor detection as a standard
  pre-deployment gate — neural cleanse or equivalent
- A.8.8: Apply continuous vulnerability monitoring to training
  pipeline dependencies — alert on compromised components
- Apply differential privacy during training — document
  privacy budget as evidence of A.8.11 data masking control

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain, LLM04 Data & Model Poisoning
- Agentic Top 10: ASI04 Supply Chain, ASI06 Memory & Context Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · CycloneDX ML SBOM · MITRE ATLAS AML.T0032

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High

AI pipelines ingest data from APIs, uploaded files, snapshot imports,
and labelling queues with insufficient validation — adversarially
crafted payloads that pass syntactic validation corrupt training sets,
shift feature distributions, or exploit snapshot import path traversal
to achieve arbitrary file write on the vector DB host.

**Real-world references:**
- CVE-2024-3584 (Qdrant) — poisoned snapshot import achieved
  arbitrary file write via path traversal on the vector DB host
  with no authentication bypass required

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Application security requirements | A.8.26 | Technological | Input validation requirements specified for all GenAI data ingestion interfaces |
| Secure coding | A.8.28 | Technological | Secure coding practices applied to data ingestion, parsing, and snapshot import code |
| Security testing | A.8.29 | Technological | Security testing of all data ingestion interfaces including schema and semantic validation |
| Configuration management | A.8.9 | Technological | Snapshot import and restore functionality hardened and version controlled |

#### Mitigations by tier

**Foundational**
- A.8.26: Define and enforce input validation requirements for
  all data ingestion interfaces — schema validation is necessary
  but not sufficient, semantic validation required
- A.8.28: Apply secure coding practices to all data parsing
  code — path traversal prevention mandatory for snapshot and
  archive import functionality
- A.8.9: Harden all snapshot import and restore endpoints —
  disable or restrict by default, explicit allowlist required

**Hardening**
- A.8.29: Include schema bypass and path traversal scenarios
  in security testing — fuzz all data ingestion interfaces
  before deployment
- Implement anomaly detection on ingestion payloads — flag
  statistical outliers, unusual encoding, or boundary values
  before they enter training or retrieval pipelines
- Patch CVE-2024-3584 and equivalent vulnerabilities in all
  vector database deployments — treat as urgent A.8.8

**Advanced**
- Implement multi-stage validation — syntax, schema, semantic,
  and statistical validation in pipeline stages with rejection
  logging at each stage
- Sandbox all snapshot import operations — no direct write to
  production filesystem paths
- Deploy content-aware ingestion monitoring — detect and alert
  on adversarially crafted payloads before pipeline completion

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://greatexpectations.io |
| Pandera | Open-source | https://pandera.readthedocs.io |
| OWASP ZAP (API fuzzing) | Open-source | https://www.zaproxy.org |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: OWASP ASVS V5 · CWE-20 · NIST AI RMF MS-3.3

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange Risks

**Severity:** High

AI tools, plugins, and agents exchange sensitive context — customer
records, internal documents, API responses — with third-party services
that may store, train on, or expose this data. MCP servers and plugin
APIs receive full context payloads with no data minimisation.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Supplier relationships | A.5.19 | Organisational | Security due diligence on all tool and plugin providers receiving agent context |
| Supplier agreements | A.5.20 | Organisational | Contractual requirements covering data minimisation, retention, and training use for tool providers |
| Information access restriction | A.8.3 | Technological | Tools receive only the minimum context required for their function — not full conversation history |
| Security for cloud services | A.5.23 | Organisational | Cloud-based tool and plugin providers assessed against A.5.23 security requirements |

#### Mitigations by tier

**Foundational**
- A.5.19: Conduct security assessment of all tool and plugin
  providers before integration — what data do they receive,
  retain, and use for training?
- A.8.3: Implement context minimisation — tools receive only
  the minimum payload required for their function, not full
  conversation history or system prompt content
- A.5.20: Include data processing requirements in all tool
  provider contracts — zero training use, defined retention,
  incident notification

**Hardening**
- Inventory all tool integrations with data flow mapping —
  what data category each tool receives, processes, and stores
- Implement payload inspection on all tool call outputs —
  scan for sensitive data before returning to agent context
- A.5.23: Conduct annual security assessments of all cloud
  tool providers — include in supplier management programme

**Advanced**
- Implement just-enough context delivery — dynamically scope
  tool payloads per invocation based on minimum requirement
- Deploy outbound DLP on all tool API calls — block sensitive
  data patterns from leaving the controlled environment
- Contractual right-to-audit for all strategic tool providers
  receiving sensitive agent context

#### Tools

| Tool | Type | Link |
|---|---|---|
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- Agentic Top 10: ASI02 Tool Misuse, ASI04 Supply Chain
- Other frameworks: AIUC-1 A/B006 · EU AI Act Art. 25

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High

GenAI systems create new derived data assets — embeddings, summaries,
cached retrievals, agent traces — that fall outside traditional data
governance programmes. Classification labels, retention policies, and
erasure obligations do not propagate from source documents to their
derived AI representations.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Inventory of assets | A.5.9 | Organisational | All GenAI data assets inventoried — training data, embeddings, caches, agent memory, logs |
| Classification of information | A.5.12 | Organisational | Classification extended to GenAI-derived assets — embeddings inherit source classification |
| Labelling of information | A.5.13 | Organisational | Classification labels propagate through the full GenAI data lifecycle |
| Information deletion | A.8.10 | Technological | Deletion and erasure obligations enforced across all derived assets — embeddings, caches, backups |

#### Mitigations by tier

**Foundational**
- A.5.9: Extend asset inventory to cover all GenAI data assets —
  training datasets, evaluation sets, embedding stores, RAG
  corpora, agent memory, prompt templates, observability logs
- A.5.12: Classify all GenAI assets at ingestion — classification
  must propagate to all derived forms including embeddings,
  summaries, and cached retrievals
- A.8.10: Establish deletion procedures covering derived assets —
  deleting a source document must also delete its embeddings,
  cached retrievals, and any agent memory containing its content

**Hardening**
- A.5.13: Implement automated label propagation — classification
  tags flow from source data through the full derivation chain
- Establish data retention schedules for all GenAI asset types —
  embedding stores, session caches, observability data, agent
  traces each have appropriate TTLs
- Map all GenAI data flows end-to-end — source through
  preprocessing, embedding, retrieval, generation, and logging

**Advanced**
- Implement machine unlearning readiness — versioned
  data-to-model linkage enabling scoped targeted retraining
  in response to erasure obligations
- Automated retention enforcement across all GenAI pipeline
  components — policy-driven expiry, not manual deletion
- Generate and maintain a Data Bill of Materials (DBoM) for
  all production AI systems — auditable provenance chain

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| OpenMetadata | Open-source | https://open-metadata.org |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI01 Sensitive Data Leakage
- Other frameworks: EU AI Act Art. 10 · ISO 27701 · NIST AI RMF GV-1.6

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High

GenAI systems trigger regulatory obligations under GDPR, EU AI Act,
HIPAA, CCPA, and sector-specific regulations — often without the
organisation recognising that the AI system is in scope. Training on
personal data without lawful basis, retaining data beyond permitted
periods, and failing to support data subject rights are the most
common violation patterns.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Compliance with legal requirements | A.5.31 | Organisational | Identifying and complying with all legal, regulatory, and contractual requirements applicable to GenAI |
| Privacy and PII protection | A.5.34 | Organisational | Privacy requirements for GenAI-processed personal data — lawful basis, minimisation, rights support |
| Compliance with policies | A.5.36 | Organisational | Internal policies for GenAI compliance — reviewed and enforced |
| Policies for information security | A.5.1 | Organisational | Governance policies covering regulatory obligations for GenAI |

#### Mitigations by tier

**Foundational**
- A.5.31: Conduct regulatory scoping assessment for all GenAI
  deployments — identify which regulations apply, what
  obligations are triggered, and who is accountable
- A.5.34: Establish lawful basis for all personal data
  processed by GenAI systems — documented in records of
  processing activities (RoPA) under GDPR Art. 30
- A.5.1: Publish and enforce an AI compliance policy —
  covers data minimisation, retention limits, consent
  management, and data subject rights

**Hardening**
- Extend RoPA to cover all AI training and inference activities —
  including sub-processor relationships with model providers
  and vector store vendors
- Implement data subject rights workflows for GenAI —
  access, erasure, and rectification requests must be
  fulfilled across source data and all derived assets
- A.5.36: Conduct periodic compliance reviews against each
  applicable regulation — document findings and remediation

**Advanced**
- Implement automated compliance posture monitoring —
  continuous assessment against regulatory obligations,
  flagging gaps in lawful basis, expired consent, and
  unverified erasure
- EU AI Act Aug 2026 readiness assessment for any system
  qualifying as high-risk — gap analysis and remediation
  roadmap required
- Contractual compliance cascade — ensure all AI vendors
  and sub-processors carry equivalent compliance obligations

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| Osano | Commercial | https://www.osano.com |
| GDPR.eu compliance guides | Reference | https://gdpr.eu |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance
- Other frameworks: EU AI Act Art. 10/17 · ISO 27701 · GDPR Art. 5/25/30 · HIPAA

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Users upload screenshots, passport photos, voice recordings, and
whiteboard images to multimodal AI assistants. These are OCR'd,
transcribed, and stored — but the extracted text is treated as less
sensitive than the original image, creating a leakage path where
highly sensitive visual or audio data persists in logs and embeddings
long after the stated retention period.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Data masking | A.8.11 | Technological | Masking and redaction applied to extracted text from OCR and audio transcription — same as source |
| Data leakage prevention | A.8.12 | Technological | DLP applied to all modality-extracted content — text, OCR output, transcripts |
| Classification of information | A.5.12 | Organisational | Classification of multimodal inputs must propagate to all derived extracted content |
| Use of cryptography | A.8.24 | Technological | Encryption of multimodal uploads and all derived content at rest and in transit |

#### Mitigations by tier

**Foundational**
- A.5.12: Classify multimodal uploads at ingestion — an image
  of a passport is Restricted; its OCR output is equally Restricted
- A.8.24: Encrypt all multimodal uploads and extracted content
  at rest and in transit — classification-aware encryption keys
- A.8.11: Apply the same redaction standards to OCR and
  transcription output as to equivalent text inputs

**Hardening**
- A.8.12: Deploy DLP on all multimodal extraction pipelines —
  OCR output, audio transcripts, and image analysis results
  scanned for PII before storage
- Implement short retention windows for multimodal uploads and
  all derived content — delete after purpose is served
- Audit all storage paths where multimodal content lands —
  include in A.5.9 asset inventory and apply classification

**Advanced**
- Implement content-aware retention — multimodal uploads
  containing sensitive content automatically scheduled for
  deletion on classification trigger
- Deploy PII detection on audio and image extraction pipelines
  in real time — block or redact before storage
- A.8.12: Monitor for multimodal content appearing in
  unexpected contexts — logs, embeddings, or outputs containing
  content derived from sensitive uploads

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| AWS Macie | Commercial | https://aws.amazon.com/macie/ |
| Google Cloud DLP | Commercial | https://cloud.google.com/dlp |

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI14 Telemetry Leakage
- Other frameworks: ISO 27701 · GDPR Art. 9 (special category data) · NIST AI RMF MS-2.6

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium

Organisations use synthetic data generation and anonymisation to
satisfy privacy requirements — but GenAI-era reconstruction attacks
can re-identify individuals from supposedly anonymised datasets,
and synthetic data may inadvertently preserve statistical properties
of sensitive source data.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Privacy and PII protection | A.5.34 | Organisational | Anonymisation must meet the standard required by applicable privacy law — not just technical anonymisation |
| Data masking | A.8.11 | Technological | Technical anonymisation and pseudonymisation controls applied to synthetic data generation |
| Classification of information | A.5.12 | Organisational | Synthetic datasets classified based on re-identification risk, not assumed to be non-personal |
| Test information | A.8.33 | Technological | Appropriate protection of test and synthetic data used in AI development |

#### Mitigations by tier

**Foundational**
- A.5.34: Treat anonymisation as a legal standard, not a
  technical checkbox — verify compliance with applicable
  privacy law definition of anonymisation before relying on it
- A.5.12: Classify synthetic datasets based on re-identification
  risk — do not automatically treat synthetic data as non-personal
- A.8.33: Apply the same access controls to synthetic training
  data as to source data until re-identification risk is
  formally assessed and accepted

**Hardening**
- Implement formal re-identification risk assessment before
  releasing or using synthetic datasets — document as A.5.34
  privacy control evidence
- Apply differential privacy (DP-SGD) to synthetic data
  generation — document privacy budget as A.8.11 control
- Conduct re-identification attack testing on synthetic
  datasets before use in external or public contexts

**Advanced**
- Implement k-anonymity, l-diversity, and t-closeness
  measurements on all synthetic datasets — formal minimum
  standards before classification downgrade
- Deploy membership inference testing as a standard gate
  in the synthetic data generation pipeline
- A.5.34: Establish a synthetic data governance policy —
  generation methodology, quality thresholds, re-identification
  risk acceptance criteria, and review cadence

#### Tools

| Tool | Type | Link |
|---|---|---|
| Gretel AI | Commercial | https://gretel.ai |
| Synthetic Data Vault | Open-source | https://sdv.dev |
| ARX Anonymisation Tool | Open-source | https://arx.deidentifier.org |

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI18 Inference & Reconstruction
- Other frameworks: ISO 27701 · GDPR Recital 26 · EU AI Act Art. 10

---

### DSGAI11 — Cross-Context & Multi-User Conversation Bleed

**Severity:** High

Sensitive data from one user's conversation, session context, or
retrieved documents leaks into another user's responses — through
shared KV caches, poorly isolated multi-tenant vector stores, or
system prompt contamination between sessions.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Information access restriction | A.8.3 | Technological | Strict session and tenant isolation — one user's context cannot be accessed by another |
| Information transfer | A.5.14 | Organisational | Controls on context transfer between sessions — prohibition on cross-session data leakage |
| Data masking | A.8.11 | Technological | Redaction of any cross-session content that reaches an output channel |
| Logging | A.8.15 | Technological | Logging of cross-session access anomalies for detection and forensics |

#### Mitigations by tier

**Foundational**
- A.8.3: Implement strict session isolation — each user's
  context window, retrieved documents, and conversation
  history inaccessible to all other sessions
- Implement per-user, per-session RAG namespaces — shared
  vector stores must enforce tenant isolation at query time
- A.8.15: Log all context retrieval operations — anomalous
  cross-session access patterns detectable from logs

**Hardening**
- Test multi-tenant isolation explicitly in security testing —
  verify that user A cannot retrieve user B's documents
  through any query formulation
- Implement KV cache isolation for shared inference
  infrastructure — per-session cache with strict TTL
- A.5.14: Establish formal controls on context persistence —
  define what data survives session end and what is purged

**Advanced**
- Conduct adversarial cross-tenant testing — attempt to
  extract other users' context through crafted queries
  on every new retrieval system deployment
- Implement real-time bleed detection — monitor for
  unexpected content appearing in session context that
  is not sourced from the current user's authorised scope
- Cryptographic session isolation for highest-risk tenants —
  per-tenant encryption keys on all stored context

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Pinecone Canopy | Open-source | https://github.com/pinecone-io/canopy |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: NIST AI RMF MS-2.5 · AIUC-1 A · GDPR Art. 32

---

### DSGAI12 — Unsafe Natural-Language Data Gateways

**Severity:** Critical

LLM-to-SQL, LLM-to-Graph, and LLM-to-API interfaces collapse the
traditional security boundary between user input and database logic.
Natural language instructions coerce the model into generating
destructive queries — DELETE, DROP, bulk SELECT — which execute under
a high-privilege service account with no row-level enforcement.

**Real-world references:**
- Finance Copilot scenario — malicious document injected via RAG
  caused LLM-generated SQL to dump customer PII from multiple tables
- Multiple production LLM-to-SQL deployments executing attacker-
  directed bulk extraction queries (2024–2025)

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Application security requirements | A.8.26 | Technological | Security requirements for LLM-to-SQL interfaces — read-only by default, parameterisation mandatory |
| Information access restriction | A.8.3 | Technological | LLM-generated queries execute under least-privilege credentials matching the requesting user's access |
| Secure coding | A.8.28 | Technological | Parameterised queries, allowlisted operations, and row-level policy enforcement in LLM gateway code |
| Security testing | A.8.29 | Technological | SQL injection and privilege escalation testing on all LLM-to-database interfaces |

#### Mitigations by tier

**Foundational**
- A.8.3: LLM-generated queries must execute under the requesting
  user's database permissions — never a shared high-privilege
  service account
- A.8.26: Restrict LLM-to-SQL interfaces to read-only operations
  by default — write, delete, and DDL require explicit approval
  and additional controls
- A.8.28: Implement query allowlisting — only pre-approved query
  patterns permitted, parameterised execution only

**Hardening**
- A.8.29: Include SQL injection, privilege escalation, and bulk
  extraction scenarios in security testing for all LLM-gateway
  interfaces before deployment
- Implement row-level security (RLS) in the database layer —
  LLM-generated queries cannot exceed what the user can access
  through direct database access
- Log all LLM-generated query text with the requesting user's
  identity — forensic traceability mandatory

**Advanced**
- Deploy query analysis layer between LLM and database —
  validates generated SQL against permitted patterns before
  execution, rejects destructive or over-broad queries
- Implement rate limiting on LLM-generated database queries —
  bulk extraction through high-frequency queries detectable
  and blockable
- Conduct adversarial NL-to-SQL testing — attempt to coerce
  the model into generating destructive queries through
  crafted natural language inputs

#### Tools

| Tool | Type | Link |
|---|---|---|
| Semgrep | Open-source | https://semgrep.dev |
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Immuta | Commercial | https://www.immuta.com |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- Other frameworks: OWASP ASVS V5 · CWE-89 · NIST AI RMF MS-2.5

---

### DSGAI13 — Vector Store Platform Data Security

**Severity:** High

Vector databases — Pinecone, Weaviate, Qdrant, Chroma — store sensitive
embeddings and retrieved passages with weaker default security posture
than traditional databases. Missing RBAC, unencrypted storage, exposed
snapshot endpoints, and unauthenticated collection access are common.

**Real-world references:**
- CVE-2024-3584 (Qdrant) — snapshot import path traversal achieving
  arbitrary file write on the vector DB host
- Multiple publicly exposed Chroma instances with no authentication
  discovered in production deployments (2024)

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Information access restriction | A.8.3 | Technological | RBAC enforced on all vector store collections — collection-level and namespace-level access control |
| Use of cryptography | A.8.24 | Technological | Encryption of all vector store data at rest and in transit |
| Logging | A.8.15 | Technological | Audit logging on all vector store read, write, and admin operations |
| Data leakage prevention | A.8.12 | Technological | DLP controls on vector store query results — sensitive content in retrieved passages detected |

#### Mitigations by tier

**Foundational**
- A.8.3: Enable RBAC on all vector store collections from day
  one — no unauthenticated access to any collection in any
  environment including development
- A.8.24: Encrypt all vector store data at rest — use
  platform-provided encryption or external KMS
- A.8.15: Enable audit logging on all vector store operations —
  feed into SIEM for anomaly detection

**Hardening**
- Patch all known vector database CVEs — treat CVE-2024-3584
  and equivalents as urgent A.8.8 vulnerability management
- Implement namespace isolation for multi-tenant deployments —
  one collection per trust domain, no cross-namespace queries
- Deploy network access controls — vector stores accessible
  only from authorised services, never public internet

**Advanced**
- A.8.12: Implement DLP on vector store query results — scan
  retrieved passages for sensitive content before returning
  to RAG pipeline
- Conduct vector store-specific penetration testing — include
  snapshot import, path traversal, and RBAC bypass scenarios
- Implement embedding access monitoring — alert on bulk
  vector extraction patterns indicating scraping or exfiltration

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant (with API key auth) | Open-source | https://qdrant.tech |
| OWASP ZAP | Open-source | https://www.zaproxy.org |

#### Cross-references
- LLM Top 10: LLM08 Vector & Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: NIST AI RMF MS-2.5 · AIUC-1 A · CWE-284

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High

Observability and debugging pipelines — traces, logs, spans — capture
full prompt text, tool call payloads, retrieved passages, and model
outputs. These telemetry stores often have weaker access controls and
longer retention windows than production data, creating a secondary
exfiltration path for sensitive information.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Logging | A.8.15 | Technological | Logging controls applied to AI telemetry — least-logging defaults, no full payload capture by default |
| Data leakage prevention | A.8.12 | Technological | DLP applied to telemetry streams — sensitive content redacted before storage |
| Classification of information | A.5.12 | Organisational | Telemetry data classified — full prompt captures classified at same level as content they contain |
| Data masking | A.8.11 | Technological | Masking of sensitive content in logs and traces before storage |

#### Mitigations by tier

**Foundational**
- A.8.15: Apply least-logging defaults — do not capture full
  prompt and response bodies in production telemetry by default
- A.5.12: Classify all telemetry data at the same level as the
  most sensitive content it may contain — treat full prompt
  logs as Confidential until demonstrated otherwise
- Apply access controls to telemetry stores — same rigour
  as production data, not relaxed because it is "just logs"

**Hardening**
- A.8.11: Redact PII and sensitive patterns from telemetry
  streams before storage — tokenisation or masking applied
  at the telemetry ingestion pipeline
- A.8.12: Deploy DLP on telemetry pipelines — block sensitive
  content from landing in observability stores in cleartext
- Implement short TTL for debug traces — automated deletion
  after defined window, not indefinite retention

**Advanced**
- Implement approval workflow for enabling full debug capture —
  temporary, scoped, logged, automatically reverted
- Deploy telemetry access monitoring — alert on bulk access
  to telemetry stores that may indicate exfiltration
- A.8.15: Separate telemetry tiers by sensitivity — operational
  metrics with long retention, full payload traces with short
  retention and elevated access controls

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Langfuse | Open-source | https://langfuse.com |
| Helicone | Open-source | https://www.helicone.ai |

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance
- Other frameworks: ISO 27701 · GDPR Art. 32 · NIST AI RMF GV-1.6

---

### DSGAI15 — Over-Broad Context Windows & Prompt Over-Sharing

**Severity:** High

RAG pipelines and agent orchestration layers inject excessive content
into context windows — full document texts, entire conversation
histories, broad retrieval results — creating a single flat namespace
aggregating data from multiple trust domains with no internal access
control. Any prompt injection reaching this context can access all
injected content.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Information access restriction | A.8.3 | Technological | Context window content restricted to minimum required — no cross-trust-domain aggregation without access control |
| Classification of information | A.5.12 | Organisational | All content injected into context window classified — highest classification drives handling requirement |
| Data masking | A.8.11 | Technological | Sensitive content redacted or masked before injection into shared context windows |
| Information transfer | A.5.14 | Organisational | Controls on content transfer into context windows — documented data flow for each RAG pipeline |

#### Mitigations by tier

**Foundational**
- A.8.3: Implement minimum-necessary context injection —
  retrieve only the passages directly relevant to the query,
  not entire documents or broad topic matches
- A.5.12: Track the classification of all content entering
  the context window — highest classification in context
  drives the handling requirement for the entire response
- Never inject content from a higher classification tier
  than the requesting user is authorised to access

**Hardening**
- A.8.11: Redact sensitive content from retrieved passages
  before injection — PII and secrets masked even from
  authorised users unless the specific task requires it
- Implement context window monitoring — alert on context
  assembly patterns that aggregate data from multiple
  trust domains or classification tiers
- Limit conversation history injection — rolling window
  with classification-aware pruning, not unbounded history

**Advanced**
- Implement trust-domain-aware context assembly — content
  from different trust domains isolated within the context
  window with explicit labelling
- Deploy real-time context analysis before completion —
  validate that injected content does not exceed the
  requesting user's authorised access scope
- A.5.14: Formal data flow documentation for every RAG
  pipeline — reviewed on change, auditable

#### Tools

| Tool | Type | Link |
|---|---|---|
| LlamaIndex | Open-source | https://www.llamaindex.ai |
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- Agentic Top 10: ASI01 Agent Goal Hijack
- Other frameworks: AIUC-1 A/B005 · NIST AI RMF MS-2.5

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High

Browser-integrated AI assistants and endpoint agents access sensitive
data across all open tabs, local files, and clipboard content —
far beyond the scope of any individual task. Malicious updates or
hidden prompt instructions in web content can weaponise these agents
for data exfiltration.

**Real-world references:**
- HashJack (2025) — AI browsers hijacked via hidden prompt
  instructions in web content enabling data exfiltration
- Multiple AI browser extensions discovered logging sensitive
  clipboard and form field content

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Endpoint device management | A.8.1 | Technological | Endpoint AI agents managed under device management policy — approved versions, permissions scoped |
| Protection against malware | A.8.7 | Technological | Endpoint AI agents subject to malware protection — extension integrity verification |
| Acceptable use of assets | A.5.10 | Organisational | Policy governing permitted browser AI extensions and endpoint agent permissions |
| Data leakage prevention | A.8.12 | Technological | DLP controls on endpoint AI agent data access and exfiltration paths |

#### Mitigations by tier

**Foundational**
- A.5.10: Establish approved list of endpoint AI agents and
  browser extensions — unapproved extensions blocked at
  the device management layer
- A.8.1: Apply device management policy to all endpoint AI
  agents — version control, permission scoping, mandatory updates
- A.8.12: Implement DLP on endpoint AI agent network traffic —
  detect sensitive data leaving via AI assistant channels

**Hardening**
- A.8.7: Conduct extension integrity verification before
  approval — verify cryptographic signatures, review permissions,
  assess data access scope
- Conduct adversarial testing of approved browser AI extensions —
  test for hidden prompt injection via web content before
  organisation-wide approval
- Implement permission minimisation — extensions receive only
  the permissions required for their stated function

**Advanced**
- A.8.12: Real-time DLP monitoring on endpoint AI agent
  data access — alert on access patterns inconsistent with
  stated extension function
- Deploy browser isolation for highest-risk tasks — AI
  extensions cannot access data from isolated sessions
- Establish vendor security requirements for AI extension
  providers — right-to-audit, incident notification,
  zero training use on enterprise data

#### Tools

| Tool | Type | Link |
|---|---|---|
| LayerX Security | Commercial | https://layerxsecurity.com |
| Microsoft Intune | Commercial | https://www.microsoft.com/en-us/security/business/endpoint-management |

#### Cross-references
- Agentic Top 10: ASI10 Rogue Agents
- DSGAI 2026: DSGAI03 Shadow AI
- Other frameworks: AIUC-1 B006 · EU AI Act Art. 9 · NIST AI RMF GV-1.7

---

### DSGAI17 — Data Availability & Resilience Failures in AI Pipelines

**Severity:** High

RAG-dependent applications fail silently when vector stores degrade —
returning stale or incorrect information as if it were current, invisible
to monitoring stacks and indistinguishable from correct output. Vector
DB saturation, stale replica failover, and index corruption all produce
silent misinformation at inference time.

**Real-world references:**
- Multiple production RAG outages where stale replica failover
  caused AI systems to surface outdated information with full
  confidence for hours before detection (2024–2025)

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| ICT readiness for business continuity | A.5.30 | Organisational | AI pipeline availability requirements included in BCP — RTO/RPO defined for vector stores and RAG components |
| Backup | A.8.13 | Technological | Backup and recovery for all AI data assets — vector stores, embedding indexes, RAG corpora |
| Redundancy | A.8.14 | Technological | Redundancy and failover for production RAG and vector store infrastructure |
| Incident management | A.5.24 | Organisational | Incident management procedures covering AI pipeline availability failures |

#### Mitigations by tier

**Foundational**
- A.8.13: Implement backup and recovery for all vector stores
  and RAG data assets — encrypted backups, tested restores,
  documented RTO and RPO
- A.5.24: Establish incident response procedures for AI pipeline
  availability failures — including silent degradation detection
- Implement health checks on vector store freshness — alert
  when index age exceeds defined threshold

**Hardening**
- A.8.14: Deploy redundancy for production RAG infrastructure —
  replica synchronisation lag monitored and bounded
- A.5.30: Include AI pipeline components in BCP testing —
  annual failover drills covering vector store failure scenarios
- Implement circuit breakers on RAG retrieval — degrade
  gracefully to non-RAG responses rather than silently
  serving stale or empty retrieval results

**Advanced**
- Implement embedding freshness monitoring — track index
  staleness per collection with automated alerting
- Rate limiting on vector similarity search endpoints —
  prevent adversarial saturation attacks on retrieval tier
- A.8.13: Test integrity of restored vector indexes — verify
  that backup restoration produces correct retrieval results,
  not just structural integrity

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Resilience4j | Open-source | https://resilience4j.readme.io |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.6 (OT) · NIST SP 800-82 (OT)

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High

Adversaries reconstruct sensitive training data from model outputs
through membership inference attacks, model inversion, and embedding
inversion — extracting PII, proprietary content, or confidential
records that were present in training or retrieval corpora.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Data masking | A.8.11 | Technological | Differential privacy and output masking reducing information available for reconstruction attacks |
| Privacy and PII protection | A.5.34 | Organisational | Privacy requirements extended to cover inference attack resistance — not just direct disclosure |
| Use of cryptography | A.8.24 | Technological | Cryptographic protection of embedding vectors preventing inversion attacks |
| Data leakage prevention | A.8.12 | Technological | Output monitoring for responses that reconstruct training data or sensitive source content |

#### Mitigations by tier

**Foundational**
- A.5.34: Assess inference attack risk as part of privacy
  impact assessment — membership inference and model inversion
  explicitly in scope alongside direct disclosure risks
- A.8.12: Monitor model outputs for content that may represent
  reconstructed training data — alerts on verbatim or near-
  verbatim reproduction of likely training content
- A.8.24: Encrypt all embedding vectors at rest — prevents
  offline inversion attacks on stolen embedding stores

**Hardening**
- Apply differential privacy during training — limits
  the information any single training example contributes,
  reducing membership inference success rate
- Implement output rate limiting per user per time window —
  limits the number of inference queries an attacker can
  submit to reconstruct training data
- A.8.11: Implement confidence score suppression — do not
  return raw confidence or probability values that enable
  membership inference

**Advanced**
- Conduct membership inference and model inversion red team
  exercises as standard pre-deployment validation — document
  results as privacy control evidence
- A.5.34: Implement machine unlearning readiness — ability to
  surgically remove specific training examples in response to
  confirmed inference attack exposure
- Deploy adversarial robustness testing specifically targeting
  reconstruction attacks on your model and embedding configuration

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI10 Synthetic Data Pitfalls
- Other frameworks: ISO 27701 · GDPR Art. 25 · MITRE ATLAS AML.T0024

---

### DSGAI19 — Human-in-the-Loop & Labeler Overexposure

**Severity:** Medium

Human annotators and HITL reviewers access sensitive model inputs
and outputs during labelling, fine-tuning review, and safety evaluation
— exposing customer data, internal documents, or confidential content
to third-party contractors with limited data handling controls.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Privacy and PII protection | A.5.34 | Organisational | Data minimisation and privacy controls for all HITL labelling workflows |
| Information security awareness training | A.6.3 | People | Security training for all labellers — internal and third-party — covering data handling requirements |
| Supplier agreements | A.5.20 | Organisational | Contractual data handling requirements for labelling vendors and HITL service providers |
| Data masking | A.8.11 | Technological | Anonymisation and redaction applied to labelling tasks before exposure to annotators |

#### Mitigations by tier

**Foundational**
- A.5.34: Apply data minimisation to labelling tasks — annotators
  see only the minimum content required for their annotation,
  not full source records
- A.5.20: Include data handling requirements in all labelling
  vendor contracts — no retention beyond task, no secondary
  use, defined incident notification
- A.6.3: Provide security awareness training to all annotators
  covering data handling, non-disclosure, and incident reporting

**Hardening**
- A.8.11: Anonymise or pseudonymise sensitive content in
  labelling tasks before exposure — annotators work on
  de-identified versions where possible
- Implement access controls on labelling platforms — annotators
  see only their assigned tasks, no browsing of full datasets
- Conduct security assessments of labelling vendors —
  include in A.5.19 supplier security programme

**Advanced**
- Implement differential privacy in labelling pipeline —
  aggregate annotations without exposing individual annotator
  access to full sensitive corpora
- Deploy synthetic data for labelling where possible —
  real sensitive data replaced with synthetic equivalents
  that preserve annotation-relevant properties
- Right-to-audit contractual provision for all strategic
  labelling vendors handling sensitive data

#### Tools

| Tool | Type | Link |
|---|---|---|
| Label Studio | Open-source | https://labelstud.io |
| Scale AI | Commercial | https://scale.com |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: EU AI Act Art. 10 · ISO 27701 · GDPR Art. 28

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High

Adversaries extract sufficient information from a deployed model through
systematic querying to reconstruct a functional replica — stealing
proprietary training investment, fine-tuned capabilities, and
commercially sensitive model behaviour without accessing the
original weights.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Classification of information | A.5.12 | Organisational | Model weights, architectures, and fine-tuning configurations classified as intellectual property |
| Information access restriction | A.8.3 | Technological | API rate limiting, query restrictions, and anomaly detection limiting systematic model extraction |
| Data leakage prevention | A.8.12 | Technological | Monitoring for systematic querying patterns indicative of model extraction attacks |
| Supplier relationships | A.5.19 | Organisational | Security requirements for any third-party access to proprietary model capabilities |

#### Mitigations by tier

**Foundational**
- A.5.12: Classify all proprietary model artifacts as
  Confidential or higher — model weights, fine-tuning datasets,
  training configurations, and evaluation sets
- A.8.3: Implement API rate limiting and query volume caps —
  systematic extraction requires high query volumes, rate
  limiting raises the cost dramatically
- A.8.12: Monitor for model extraction patterns — unusual
  query diversity, systematic coverage of output space,
  high-volume confidence score harvesting

**Hardening**
- Implement output perturbation — add calibrated noise to
  confidence scores and logits without degrading utility,
  increasing extraction noise
- Deploy query anomaly detection — flag sessions exhibiting
  systematic exploration of model output space
- A.5.12: Apply watermarking to proprietary model outputs —
  enables detection of replicated model usage in the wild

**Advanced**
- Conduct model extraction red team exercises — attempt to
  replicate your model using your own API and document the
  query budget required
- Implement adaptive rate limiting based on query diversity
  scoring — tighten limits on sessions exhibiting extraction
  patterns
- Legal and technical response capability for discovered
  replicated models — include in incident response planning

#### Tools

| Tool | Type | Link |
|---|---|---|
| Watermarking via Watermark-Anything | Open-source | https://github.com/facebookresearch/watermark-anything |
| Fiddler AI | Commercial | https://www.fiddler.ai |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference & Reconstruction
- Other frameworks: MITRE ATLAS AML.T0016 · NIST AI RMF MS-2.5 · CWE-200

---

### DSGAI21 — Disinformation & Integrity Attacks via Data Poisoning

**Severity:** High

Adversaries inject false, misleading, or politically motivated content
into trusted retrieval sources — RAG corpora, knowledge bases, web
indexes — so that AI systems surface this content as authoritative
output. Unlike direct model poisoning, this targets the data plane
rather than the model, requiring no training access.

**Real-world references:**
- Grok RAG incident (2025) — production RAG system ingested and
  surfaced externally introduced false information as authoritative
  output
- Crowdsourced dataset poisoning campaigns targeting open training
  corpora — active documented attack class

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Threat intelligence | A.5.7 | Organisational | Active intelligence on disinformation campaigns and RAG poisoning techniques targeting your sector |
| Management of technical vulnerabilities | A.8.8 | Technological | Vulnerability management extended to cover data integrity vulnerabilities in RAG pipelines |
| Secure system architecture | A.8.27 | Technological | RAG pipeline designed with source trust verification and integrity controls |
| Security testing | A.8.29 | Technological | Integrity testing of RAG corpora — anomaly detection, source validation, content verification |

#### Mitigations by tier

**Foundational**
- A.8.27: Implement source trust tiering in RAG retrieval —
  weight results by source provenance and trust score, not
  solely semantic similarity
- A.8.8: Apply vulnerability management to RAG data integrity —
  monitor for unauthorised changes to retrieval corpora
- A.5.7: Maintain threat intelligence on disinformation
  campaigns targeting your specific domain and RAG sources

**Hardening**
- A.8.29: Implement ingestion anomaly detection — statistical
  and semantic scanning for unusual content before it enters
  production retrieval indexes
- Deploy ingestion gates — elevated validation during active
  high-tempo periods or when threat intelligence indicates
  active targeting of your retrieval sources
- Implement cross-verification for high-stakes outputs —
  AI-generated content verified against multiple independent
  authoritative sources before publication

**Advanced**
- Automated human-in-the-loop triggers for AI decisions
  derived from low-provenance or recently indexed sources
  in irreversible decision contexts
- Adversarial integrity evaluation — red team testing of
  RAG pipeline susceptibility to low-frequency poisoning
  in training corpora as standard pre-deployment validation
- Dataset Bill of Materials (DBoM) with cryptographic
  provenance chain — detect any unauthorised modification
  to retrieval corpora post-ingestion

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://greatexpectations.io |
| Deepchecks | Open-source | https://deepchecks.com |
| TruLens | Open-source | https://github.com/truera/trulens |

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0045 · EU AI Act Art. 55(1)(a) · ENISA

---

## ISO 27001 ISMS extension checklist for GenAI

Use this checklist to extend your existing ISO 27001 ISMS to cover
GenAI data security obligations:

### Scope extension
- [ ] GenAI data assets added to A.5.9 asset inventory
- [ ] Classification policy extended to cover embeddings, caches, agent memory, telemetry
- [ ] Data flow maps updated to include all GenAI pipelines

### Policy updates
- [ ] Acceptable use policy updated to cover AI tools (A.5.10)
- [ ] Cloud services policy extended to AI SaaS (A.5.23)
- [ ] Supplier agreements updated for AI vendors (A.5.20)
- [ ] AI data governance policy published (A.5.1)

### Technical controls
- [ ] DLP deployed on all model output channels (A.8.12)
- [ ] Output masking/redaction implemented (A.8.11)
- [ ] RAG access controls audited (A.8.3)
- [ ] Vector store RBAC and encryption confirmed (A.8.3, A.8.24)
- [ ] Telemetry least-logging defaults applied (A.8.15)
- [ ] NHI inventory and credential lifecycle controls live (A.8.2, A.5.16)

### Testing and monitoring
- [ ] GenAI scenarios added to internal audit programme (A.8.29)
- [ ] Penetration test scope extended to include LLM and RAG interfaces
- [ ] Vulnerability management covers AI pipeline components (A.8.8)
- [ ] Incident response procedures updated for AI-specific scenarios (A.5.24)

---

## Implementation priority

| Phase | DSGAI entries | ISO 27001 controls | Rationale |
|---|---|---|---|
| 1 — Do now | DSGAI01, DSGAI02, DSGAI12 | A.8.12, A.8.2, A.8.3 | Highest severity, most likely to be in scope for existing ISO 27001 audit |
| 2 — This sprint | DSGAI03, DSGAI07, DSGAI14 | A.5.10, A.5.9, A.8.15 | Asset inventory and governance close the shadow AI and telemetry gaps |
| 3 — This quarter | DSGAI04, DSGAI05, DSGAI13 | A.8.27, A.8.29, A.8.24 | Integrity and vector store controls require pipeline-level changes |
| 4 — Ongoing | DSGAI08–DSGAI11, DSGAI15–DSGAI21 | All remaining | Defence-in-depth, privacy, and resilience hardening |

---

## References

- [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html)
- [ISO/IEC 27001:2022 Annex A controls summary](https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-3:v1:en)
- [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [ISO/IEC 27701 — Privacy extension](https://www.iso.org/standard/71670.html)
- [ISO/IEC 42001 — AI management systems](https://www.iso.org/standard/81230.html)
- [NIST AI RMF](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full entries with ISMS checklist | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
