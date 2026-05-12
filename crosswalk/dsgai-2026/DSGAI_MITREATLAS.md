<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks and Mitigations 2026 (DSGAI01-DSGAI21)
  Framework   : MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × MITRE ATLAS

Mapping the [OWASP GenAI Data Security Risks and Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to [MITRE ATLAS](https://atlas.mitre.org) —
the Adversarial Threat Landscape for Artificial-Intelligence Systems,
the authoritative knowledge base of adversarial ML tactics, techniques,
and procedures observed in real-world AI attacks.

---

## Why MITRE ATLAS for GenAI data security

MITRE ATLAS extends the ATT&CK framework into the AI domain. Where
DSGAI 2026 describes what can go wrong with GenAI data, MITRE ATLAS
describes how adversaries make it go wrong — the specific techniques,
tools, and attack sequences observed in real incidents.

For GenAI data security specifically, ATLAS provides the attacker
perspective on three critical threat surfaces:

**Training pipeline attacks:** ATLAS documents how adversaries poison
training data, corrupt model weights, and compromise the supply chain
of model components — directly mapping to DSGAI04, DSGAI05, and
DSGAI21.

**Inference-time attacks:** ATLAS captures how adversaries manipulate
GenAI systems through crafted inputs, extract sensitive information
through model queries, and reconstruct training data through inference
attacks — mapping to DSGAI01, DSGAI12, DSGAI18, and DSGAI20.

**Model and system integrity attacks:** ATLAS documents supply chain
compromise, model exfiltration, and evasion techniques — mapping to
DSGAI03, DSGAI04, and DSGAI20.

This file completes the ATLAS coverage across all three OWASP source
lists. See also `llm-top10/LLM_MITREATLAS.md` and
`agentic-top10/Agentic_MITREATLAS.md` for LLM and agentic mappings.

---

## MITRE ATLAS structure

ATLAS organises adversarial AI techniques into tactics (the adversary's
goal) and techniques (how they achieve it):

| Tactic | ID | Relevance to DSGAI |
|---|---|---|
| Reconnaissance | AML.TA0002 | Gathering information about AI system, data assets, model details |
| Resource Development | AML.TA0000 | Acquiring training data, developing poisoned datasets |
| Initial Access | AML.TA0001 | Gaining access to AI systems, training pipelines, data stores |
| ML Attack Staging | AML.TA0005 | Preparing adversarial examples, poisoned data, exfiltration tools |
| Exfiltration | AML.TA0008 | Model theft, data extraction, sensitive output capture |
| Impact | AML.TA0010 | Model degradation, data corruption, system compromise |

---

## Quick-reference summary

| ID | Name | Severity | Primary ATLAS Techniques | Tier |
|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | AML.T0025, AML.T0024.000, AML.T0035 | Foundational–Advanced |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | AML.T0012, AML.T0035, AML.T0051 | Foundational–Advanced |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | AML.T0012, AML.T0051, AML.T0057 | Foundational–Hardening |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | AML.T0020, AML.T0032, AML.T0031 | Hardening–Advanced |
| DSGAI05 | Data Integrity & Validation Failures | High | AML.T0020, AML.T0018, AML.T0031 | Foundational–Hardening |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | AML.T0051, AML.T0057, AML.T0035 | Foundational–Hardening |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | AML.T0035, AML.T0024.000, AML.T0057 | Foundational–Advanced |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | AML.T0057, AML.T0051, AML.T0035 | Foundational–Advanced |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | AML.T0025, AML.T0035, AML.T0024.000 | Hardening–Advanced |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | AML.T0024.000, AML.T0025, AML.T0035 | Hardening–Advanced |
| DSGAI11 | Cross-Context Conversation Bleed | High | AML.T0025, AML.T0035, AML.T0051 | Foundational–Hardening |
| DSGAI12 | Unsafe NL Data Gateways | Critical | AML.T0051, AML.T0057, AML.T0035 | Foundational–Advanced |
| DSGAI13 | Vector Store Platform Security | High | AML.T0025, AML.T0035, AML.T0020 | Foundational–Hardening |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | AML.T0035, AML.T0025, AML.T0057 | Foundational–Hardening |
| DSGAI15 | Over-Broad Context Windows | High | AML.T0051, AML.T0025, AML.T0035 | Foundational–Hardening |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | AML.T0013, AML.T0057, AML.T0035 | Foundational–Hardening |
| DSGAI17 | Data Availability & Resilience Failures | High | AML.T0029, AML.T0034, AML.T0057 | Foundational–Advanced |
| DSGAI18 | Inference & Data Reconstruction | High | AML.T0024.000, AML.T0025, AML.T0027 | Hardening–Advanced |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | AML.T0035, AML.T0057, AML.T0020 | Foundational–Hardening |
| DSGAI20 | Model Exfiltration & IP Replication | High | AML.T0016, AML.T0025, AML.T0034 | Hardening–Advanced |
| DSGAI21 | Disinformation via Data Poisoning | High | AML.T0045, AML.T0020, AML.T0031 | Hardening–Advanced |

---

## Audience tags

- **Red team / adversarial ML** — full file, attacker technique reference for GenAI data security assessments
- **Threat intelligence** — ATLAS technique mapping for AI threat model development
- **Security architect** — threat landscape for GenAI data security design
- **Incident responder** — technique identification during GenAI data security incidents
- **CISO** — executive threat landscape overview for AI data risk programme

---

## ATLAS technique reference

Key techniques cited throughout this mapping:

| Technique | ID | Description |
|---|---|---|
| Discover ML Model Ontology | AML.T0013 | Adversary learns about the AI system architecture, data sources, and model properties |
| Obtain Capabilities | AML.T0012 | Adversary acquires tools, infrastructure, or access needed for the attack |
| ML Supply Chain Compromise | AML.T0010 | Compromise of components in the ML supply chain — datasets, models, frameworks |
| Poison Training Data | AML.T0020 | Adversary introduces malicious data into training pipeline to manipulate model behaviour |
| Backdoor ML Model | AML.T0018 | Embed hidden functionality triggered by specific inputs |
| Craft Adversarial Data | AML.T0031 | Create inputs specifically designed to manipulate model outputs |
| Membership Inference | AML.T0024.000 | Determine whether a specific data point was used in training |
| Model Inversion | AML.T0027 | Reconstruct training data from model outputs |
| Extract ML Model | AML.T0016 | Steal model functionality through systematic querying |
| Exfiltrate via Cyber Means | AML.T0025 | Steal data using standard cyber exfiltration techniques |
| Exploit Public-Facing Application | AML.T0051 | Exploit vulnerabilities in AI APIs or web interfaces |
| Denial of ML Service | AML.T0029 | Degrade or deny access to AI system resources |
| Cost Harvesting | AML.T0034 | Consume AI resources to impose financial or operational cost |
| Exfiltrate via ML Inference API | AML.T0035 | Use model inference API to extract sensitive information |
| Publish Poisoned Datasets | AML.T0045 | Release poisoned data in public repositories to corrupt downstream models |
| Data from Information Repositories | AML.T0057 | Access and exfiltrate data from AI-related data stores |

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

Sensitive data leaks through GenAI outputs, RAG retrieval, embedding
exposure, or observability pipelines. From an ATLAS perspective, this
is primarily an Exfiltration (AML.TA0008) threat — adversaries use
the inference API as an exfiltration channel for data they were not
authorised to access.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Adversary queries LLM to extract sensitive data from training corpus, RAG store, or prompt cache through crafted inference queries |
| Membership Inference | AML.T0024.000 | Exfiltration | Adversary determines whether specific sensitive records were used in training — confirms presence of target data |
| Exfiltrate via Cyber Means | AML.T0025 | Exfiltration | Sensitive content in LLM outputs, logs, or observability pipelines captured and transmitted to adversary |

#### Real-world ATLAS cases

- Samsung source code leak (2023) — sensitive proprietary code
  exfiltrated via LLM inference API through employee submissions
- Multiple healthcare RAG deployments (2024) — PHI extracted
  via over-permissive vector store retrieval

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0035: Output redaction and DLP before
  responses leave service boundary — adversary cannot
  extract sensitive data through inference if outputs
  are scanned and redacted
- Counter AML.T0024.000: Differential privacy in
  training — limits membership inference success rate
  by making individual training examples indistinguishable

**Hardening**
- Counter AML.T0025: Access controls on all GenAI
  observability pipelines — telemetry stores require
  same security as production data
- Counter AML.T0035: RAG access controls enforcing
  least-privilege retrieval — adversary cannot retrieve
  beyond authorised scope through crafted queries

**Advanced**
- Red team AML.T0035: Attempt to extract sensitive
  training data and RAG content through systematic
  inference queries against your specific deployment

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.11/A.8.12 · NIST AI RMF GV-1.6 · EU AI Act Art. 10

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical

AI agents inherit and cache credentials that attackers exploit for
lateral movement. From an ATLAS perspective, this maps to Initial
Access (AML.TA0001) — stolen agent credentials provide authenticated
access to AI systems and downstream services.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Obtain Capabilities | AML.T0012 | Resource Development | Adversary acquires agent credentials through memory inspection, log analysis, or tool payload capture |
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Agent credentials embedded in inference requests or responses extracted by adversary |
| Exploit Public-Facing Application | AML.T0051 | Initial Access | Agent API endpoints exploited to extract credentials or elevate access |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0012: JIT short-lived credentials —
  credentials acquired by adversary expire before
  lateral movement completes
- Counter AML.T0035: Credential scanning on all
  output paths — agent credentials never appear in
  inference outputs, logs, or tool payloads

**Hardening**
- Counter AML.T0051: Least-privilege credential scope —
  stolen agent credential provides minimum viable
  access, limiting lateral movement blast radius
- Credential anomaly detection — unusual access patterns
  from agent credentials alerted before lateral movement
  succeeds

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: OWASP NHI Top 10 · ISO 27001 A.8.2/A.5.16 · NIST CSF 2.0 PR.AA-01

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High

Employees use unapproved GenAI tools, creating ungoverned data flows.
From an ATLAS perspective, shadow AI is an adversary-exploited
governance gap — the adversary does not need to attack the
organisation's AI system if employees deliver sensitive data to
external AI services voluntarily.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Obtain Capabilities | AML.T0012 | Resource Development | Shadow AI tools are external AI capabilities the adversary may already operate or compromise |
| Exploit Public-Facing Application | AML.T0051 | Initial Access | Unapproved AI services may themselves be adversary-controlled or compromised |
| Data from Information Repositories | AML.T0057 | Exfiltration | Sensitive data pasted into shadow AI tools ends up in external data stores accessible to the AI service provider |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0051: Approved AI tool programme —
  employees use vetted services, not adversary-controlled
  or compromised external AI endpoints
- Counter AML.T0057: DLP on known AI SaaS endpoints —
  sensitive data flows to unapproved AI services
  blocked before leaving the corporate perimeter

**Hardening**
- Counter AML.T0057: Continuous shadow AI discovery —
  detect data flows to unapproved AI services across
  endpoints, network egress, and SaaS access logs

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.10/A.5.23 · NIST CSF 2.0 GV.OC-01 · EU AI Act Art. 25

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical

Training data, model weights, or RAG corpora corrupted with backdoors.
This is the core ATLAS poisoning threat — the techniques AML.T0020
(Poison Training Data) and AML.T0018 (Backdoor ML Model) are the
canonical ATLAS descriptions of this attack class.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Poison Training Data | AML.T0020 | ML Attack Staging | Adversary introduces malicious data into training pipeline — corrupts model behaviour in ways baked into weights |
| Backdoor ML Model | AML.T0018 | ML Attack Staging | Hidden functionality embedded in model weights — triggered by specific inputs, invisible to standard testing |
| Craft Adversarial Data | AML.T0031 | ML Attack Staging | Adversarially crafted training examples designed to produce specific model behaviours without detection |

#### Real-world ATLAS cases

- Nightshade (2023) — poison pixels in training images
  corrupted image generation model behaviour
- Multiple malicious models on Hugging Face (2024) —
  backdoored weights uploaded to public repositories

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0020: Training data integrity controls —
  source allowlisting, anomaly detection, provenance
  tracking before any training run
- Counter AML.T0018: Post-training backdoor detection —
  neural cleanse or equivalent as mandatory deployment
  gate before any production promotion

**Hardening**
- Counter AML.T0031: Adversarial data detection in
  training pipeline — statistical anomaly detection
  flags adversarially crafted training examples
- Model integrity verification at deployment —
  hash-based check against approved baseline prevents
  deployment of backdoored weights

**Advanced**
- Red team AML.T0018: Backdoor trigger testing before
  each production deployment — attempt to activate
  embedded backdoors through adversarial inputs

#### Cross-references
- LLM Top 10: LLM03 Supply Chain, LLM04 Data & Model Poisoning
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · ISO 27001 A.8.27 · NIST CSF 2.0 DE.CM-09

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High

Adversarially crafted payloads corrupt GenAI data pipelines or exploit
ingestion vulnerabilities. From an ATLAS perspective, this is ML Attack
Staging (AML.TA0005) — adversaries stage attacks by corrupting the
data that enters the AI system.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Poison Training Data | AML.T0020 | ML Attack Staging | Adversarially crafted payloads bypass ingestion validation to corrupt training or RAG data |
| Backdoor ML Model | AML.T0018 | ML Attack Staging | Path traversal in snapshot imports (CVE-2024-3584) enables write to model host — backdoor installation path |
| Craft Adversarial Data | AML.T0031 | ML Attack Staging | Payloads crafted to pass syntactic validation while embedding malicious semantic content |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0020: Multi-stage validation at all
  ingestion boundaries — syntactic, schema, semantic
  validation in sequence before any data enters pipeline
- Counter AML.T0018: Patch CVE-2024-3584 class
  vulnerabilities — path traversal in snapshot imports
  is an AML.T0018 enabler in vector database environments

**Hardening**
- Counter AML.T0031: Semantic injection detection on
  ingestion payloads — adversarially crafted content
  detected before entering RAG corpus or training data

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-20 · NIST CSF 2.0 PR.PS-04

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange

**Severity:** High

AI tools and MCP servers receive full context payloads with no
minimisation. From an ATLAS perspective, tools are a Exfiltration
channel — adversaries compromise or operate malicious tools to
capture context data that flows through the agent.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exploit Public-Facing Application | AML.T0051 | Initial Access | Malicious MCP server exploits trust relationship with agent to capture context payloads |
| Data from Information Repositories | AML.T0057 | Exfiltration | Context data flowing through tool integrations captured and transmitted to adversary |
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Tool API acts as exfiltration channel — sensitive context content captured in tool call payloads |

#### Real-world ATLAS cases

- Postmark MCP (2025) — first malicious MCP on npm,
  BCC'd every agent-sent email to attacker via poisoned
  tool descriptor exfiltrating context

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0051: Tool and MCP server security
  assessment before deployment — adversary-controlled
  or compromised tools rejected before agent access
- Counter AML.T0057: Context minimisation — tools
  receive minimum payload, not full context history
  that would maximise exfiltration value

**Hardening**
- Counter AML.T0035: DLP on all tool API calls —
  sensitive content patterns detected before leaving
  the controlled environment via tool payloads

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI04 Supply Chain
- Other frameworks: ISO 27001 A.5.19/A.5.20 · NIST CSF 2.0 GV.SC-01 · EU AI Act Art. 25

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High

GenAI creates ungoverned derived data assets outside traditional
governance programmes. From an ATLAS perspective, ungoverned data
assets are reconnaissance targets — adversaries enumerate and
exploit data stores that lack access controls.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Ungoverned derived assets (embeddings, caches) accessible through inference API without classification controls |
| Membership Inference | AML.T0024.000 | Exfiltration | Ungoverned training data status — adversary determines what sensitive data is in scope without classification barriers |
| Data from Information Repositories | AML.T0057 | Exfiltration | Ungoverned embedding stores and agent memory databases accessed without access controls |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0057: Extend asset inventory to all
  GenAI-derived assets — ungoverned stores cannot be
  protected if they are not known to exist
- Counter AML.T0035: Classification propagation to
  derived assets — embeddings and caches inherit source
  classification, blocking unauthenticated inference access

**Hardening**
- Counter AML.T0024.000: Data governance extending to
  training data provenance — what data was used in
  training documented and classified before adversary
  can probe membership

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI01 Sensitive Data Leakage
- Other frameworks: ISO 27001 A.5.9/A.8.10 · EU AI Act Art. 10 · NIST CSF 2.0 ID.AM-08

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High

GenAI systems trigger regulatory obligations without the organisation
recognising it. From an ATLAS perspective, non-compliance creates
legal and reputational attack surfaces — adversaries exploit governance
gaps to maximise harm from incidents they cause.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Data from Information Repositories | AML.T0057 | Exfiltration | Regulatory violations often arise from ungoverned data repositories — adversary exploits what compliance missed |
| Exploit Public-Facing Application | AML.T0051 | Initial Access | Non-compliant AI deployments may lack security controls that compliance would have required |
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Regulatory violations in training data scope make inference API exfiltration more damaging |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0051: Regulatory scoping assessment
  for all GenAI deployments — compliance requirements
  drive security controls that limit adversary access
- Counter AML.T0057: Data governance programme
  identifies all data repositories — compliance
  extends access controls to previously ungoverned stores

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance
- Other frameworks: EU AI Act Art. 10/17 · ISO 27001 A.5.31 · NIST CSF 2.0 GV.OC-01

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Multimodal GenAI processes images and audio — OCR and transcription
extract content that leaks through ungoverned channels. From an ATLAS
perspective, multimodal inputs are a data exfiltration staging area.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exfiltrate via Cyber Means | AML.T0025 | Exfiltration | Sensitive content extracted from multimodal inputs (OCR, transcription) transmitted through standard exfiltration paths |
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Multimodal content processed by AI system extracted through inference API queries referencing extracted content |
| Membership Inference | AML.T0024.000 | Exfiltration | Sensitive multimodal content in training data confirmed through membership inference queries |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0025: DLP on multimodal extraction
  outputs — OCR and transcription results scanned
  before storage or downstream use
- Counter AML.T0035: Same classification and access
  controls on extracted content as source modality —
  OCR output of passport image treated as Restricted

**Hardening**
- Counter AML.T0024.000: Multimodal training data
  governance — sensitive images and audio tracked in
  training data inventory, membership inference tested

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI14 Telemetry Leakage
- Other frameworks: ISO 27001 A.8.11 · GDPR Art. 9 · NIST CSF 2.0 PR.DS-01

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium

Synthetic data and anonymisation fail to prevent re-identification.
From an ATLAS perspective, membership inference (AML.T0024.000) is
the primary technique — adversaries probe synthetic datasets to
confirm re-identification is possible.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Membership Inference | AML.T0024.000 | Exfiltration | Adversary probes synthetic dataset to determine whether specific individuals are re-identifiable |
| Exfiltrate via Cyber Means | AML.T0025 | Exfiltration | Re-identified individuals from synthetic data extracted via standard exfiltration paths |
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Synthetic training data membership confirmed and specific records reconstructed through inference API |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0024.000: Formal re-identification risk
  assessment before releasing synthetic data — membership
  inference testing as standard gate before release
- Apply differential privacy in synthetic data generation —
  limits AML.T0024.000 success rate by design

**Advanced**
- Red team AML.T0024.000: Membership inference testing
  against synthetic datasets before production use —
  verify re-identification risk meets acceptable threshold

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.5.34 · GDPR Recital 26 · NIST CSF 2.0 GV.RM-06

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High

Sensitive data from one user's conversation leaks into another user's
session. From an ATLAS perspective, this is an exfiltration technique
where session isolation failure becomes a data access path.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Adversary crafts queries designed to retrieve content from other users' sessions through session isolation failure |
| Exfiltrate via Cyber Means | AML.T0025 | Exfiltration | Cross-session data captured and transmitted to adversary through inference API |
| Exploit Public-Facing Application | AML.T0051 | Initial Access | Session isolation vulnerability in multi-tenant GenAI deployment exploited to access other users' data |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0051: Strict session isolation —
  adversary crafting cross-session queries encounters
  access controls that reject retrieval from other sessions
- Counter AML.T0035: Per-user RAG namespaces —
  inference API cannot return documents from other
  users' namespaces regardless of query formulation

**Hardening**
- Counter AML.T0035: Multi-tenant isolation testing —
  adversarial cross-session queries tested before each
  deployment, ATLAS AML.T0035 technique specifically
  tested against your retrieval system

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3 · GDPR Art. 32 · NIST CSF 2.0 PR.AA-05

---

### DSGAI12 — Unsafe Natural-Language Data Gateways

**Severity:** Critical

LLM-to-database interfaces collapse the security boundary between
user input and database logic. From an ATLAS perspective, this is
AML.T0051 (Exploit Public-Facing Application) combined with
AML.T0057 (Data from Information Repositories) — the adversary
exploits the AI interface to access data stores.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exploit Public-Facing Application | AML.T0051 | Initial Access | NL gateway interface exploited through crafted natural language to generate destructive or exfiltrating queries |
| Data from Information Repositories | AML.T0057 | Exfiltration | Database accessed through LLM-generated queries — adversary extracts sensitive records without direct database access |
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | LLM inference API used to generate queries that extract data from connected databases |

#### Real-world ATLAS cases

- Finance Copilot scenario — malicious RAG-injected
  document caused LLM-generated SQL to dump customer
  PII from multiple tables

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0051: Per-user query execution —
  adversary cannot escalate query privileges through
  natural language input when queries execute under
  requesting user's permissions only
- Counter AML.T0057: Query allowlisting and
  parameterised execution — NL gateway cannot generate
  destructive or bulk extraction queries outside
  the approved pattern set

**Hardening**
- Counter AML.T0035: Log and monitor all LLM-generated
  queries — bulk extraction patterns detected before
  adversary completes data retrieval

**Advanced**
- Red team AML.T0051/AML.T0057: Adversarial NL-to-SQL
  testing — attempt bulk extraction and destructive
  queries through natural language against your specific
  deployment

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-89 · ISA/IEC 62443 SR 2.2 (OT)

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector databases have weaker default security posture than traditional
databases. From an ATLAS perspective, vector stores are high-value
data repositories targeted by AML.T0057 (Data from Information
Repositories).

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exfiltrate via Cyber Means | AML.T0025 | Exfiltration | Vector store content exfiltrated through unauthenticated access or RBAC bypass |
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Embeddings and retrieved passages extracted through vector store query API |
| Poison Training Data | AML.T0020 | ML Attack Staging | Vector store content poisoned through path traversal or unauthenticated write (CVE-2024-3584) |

#### Real-world ATLAS cases

- CVE-2024-3584 (Qdrant) — path traversal via snapshot
  import achieving arbitrary file write on vector DB host
- Multiple publicly exposed Chroma instances in
  production (2024) — unauthenticated bulk extraction

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0025: RBAC on all vector store
  collections — unauthenticated access path that enables
  AML.T0025 exfiltration is eliminated
- Counter AML.T0020: Patch CVE-2024-3584 class —
  path traversal enabling AML.T0020 staging is closed

**Hardening**
- Counter AML.T0035: Monitor vector store query patterns —
  bulk extraction volume and unusual query diversity
  indicative of AML.T0035 detected

#### Cross-references
- LLM Top 10: LLM08 Vector & Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3/A.8.24 · CWE-284 · NIST CSF 2.0 PR.AA-05

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High

Observability pipelines capture full GenAI inputs and outputs with
weaker access controls. From an ATLAS perspective, telemetry stores
are secondary exfiltration targets — adversaries who cannot access
production data may access the same data through poorly secured logs.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Sensitive inference inputs and outputs captured in telemetry stores accessed through weaker controls |
| Exfiltrate via Cyber Means | AML.T0025 | Exfiltration | Telemetry stores containing sensitive GenAI interaction data exfiltrated through standard data access paths |
| Data from Information Repositories | AML.T0057 | Exfiltration | Observability databases and log stores accessed as information repositories — sensitive content available at scale |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0057: Same access controls on telemetry
  stores as production data — telemetry is not a lower-risk
  alternative exfiltration path for adversaries
- Counter AML.T0025: PAN masking and PII redaction
  before logging — sensitive content never enters
  telemetry stores in cleartext

**Hardening**
- Counter AML.T0035: Short TTL for debug traces —
  sensitive content in telemetry stores is only accessible
  for defined window, reducing AML.T0057 value

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance
- Other frameworks: ISO 27001 A.8.15 · GDPR Art. 32 · NIST CSF 2.0 GV.OC-01

---

### DSGAI15 — Over-Broad Context Windows

**Severity:** High

Excessive context injection aggregates data from multiple trust domains
into a flat namespace. From an ATLAS perspective, over-broad context
windows amplify the impact of AML.T0051 (Exploit Public-Facing
Application) by maximising the data accessible to an injection attack.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exploit Public-Facing Application | AML.T0051 | Initial Access | Prompt injection via LLM interface accesses all content injected into over-broad context window |
| Exfiltrate via Cyber Means | AML.T0025 | Exfiltration | Over-broad context window content exfiltrated through successful injection — adversary retrieves aggregated sensitive data |
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Inference API queries designed to surface maximum context window content through crafted prompts |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0035: Minimum-necessary context
  injection — adversary gains access only to minimum
  relevant content, not aggregated cross-trust-domain data
- Counter AML.T0051: Classification ceiling tracking
  in context window — highest classification of any
  document drives response handling, limiting AML.T0051
  exfiltration value

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- Agentic Top 10: ASI01 Agent Goal Hijack
- Other frameworks: AIUC-1 A/B005 · ISO 27001 A.8.3 · NIST CSF 2.0 PR.AA-05

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High

Browser AI assistants access sensitive data across open applications.
From an ATLAS perspective, endpoint AI assistants are insider threat
amplifiers — they expand the data accessible to any adversary who
compromises or controls the assistant.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Discover ML Model Ontology | AML.T0013 | Reconnaissance | Adversary learns what data the browser assistant can access across open applications |
| Data from Information Repositories | AML.T0057 | Exfiltration | Browser assistant accesses sensitive data across tabs and applications — adversary controls assistant to exfiltrate |
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Compromised browser assistant used as exfiltration channel — sensitive data from accessible applications transmitted |

#### Real-world ATLAS cases

- HashJack (2025) — AI browsers hijacked via hidden
  prompt instructions enabling data exfiltration across
  all accessible browser tabs

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0057: Approved extensions only, permission
  minimisation — adversary controlling compromised
  extension can only access the minimum permitted data
- Counter AML.T0013: Restrict browser assistant data
  access scope — adversary reconnaissance reveals
  limited attack surface

**Hardening**
- Counter AML.T0035: Monitor browser AI traffic —
  unusual data access patterns from browser assistant
  detected as potential AML.T0035 exfiltration

#### Cross-references
- Agentic Top 10: ASI10 Rogue Agents
- DSGAI 2026: DSGAI03 Shadow AI
- Other frameworks: ISO 27001 A.8.1/A.8.7 · NIST CSF 2.0 GV.SC-01 · EU AI Act Art. 9

---

### DSGAI17 — Data Availability & Resilience Failures

**Severity:** High

Silent GenAI pipeline failures affect advisory and fraud detection
availability. From an ATLAS perspective, this maps to Denial of ML
Service (AML.T0029) and Cost Harvesting (AML.T0034) — adversaries
may deliberately trigger availability failures.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Denial of ML Service | AML.T0029 | Impact | Adversary saturates GenAI pipeline — vector store, RAG retrieval, or inference endpoint rendered unavailable |
| Cost Harvesting | AML.T0034 | Impact | Adversary triggers disproportionate resource consumption through crafted queries — financial or operational DoS |
| Data from Information Repositories | AML.T0057 | Exfiltration | Pipeline failures may expose data through error messages or fallback paths that lack normal access controls |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0029: Circuit breakers and graceful
  degradation — AML.T0029 attack causes graceful
  degradation rather than service disruption
- Counter AML.T0034: Rate limiting and per-user budgets —
  cost harvesting attacks bounded by hard caps

**Hardening**
- Counter AML.T0029: Freshness monitoring on RAG pipeline —
  stale index detected before silent misinformation
  reaches users, limiting AML.T0029 impact

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: ISA/IEC 62443 SR 7.6 (OT) · NIST CSF 2.0 PR.IR-01 · AIUC-1 D

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High

Membership inference and model inversion attacks reconstruct sensitive
training data. This is the canonical ATLAS inference attack —
AML.T0024.000 (Membership Inference) and AML.T0027 (Model Inversion)
are the primary techniques.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Membership Inference | AML.T0024.000 | Exfiltration | Adversary determines whether specific sensitive records were used in training through systematic query analysis |
| Exfiltrate via Cyber Means | AML.T0025 | Exfiltration | Training data confirmed present and partially reconstructed through inference, then exfiltrated |
| Model Inversion | AML.T0027 | Exfiltration | Adversary reconstructs sensitive training examples from model outputs through systematic query campaigns |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0024.000: Differential privacy in
  training — limits membership inference success rate
  by making individual training examples statistically
  indistinguishable
- Counter AML.T0027: Confidence score suppression —
  removes information that enables model inversion,
  adversary cannot extract gradient information

**Hardening**
- Counter AML.T0024.000: Output rate limiting —
  systematic membership inference query campaigns
  detected and rate-limited before reconstruction succeeds

**Advanced**
- Red team AML.T0024.000 and AML.T0027: Membership
  inference and model inversion testing before
  each production deployment — verify sensitive
  training data cannot be reconstructed under
  realistic attacker conditions

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI10 Synthetic Data Pitfalls
- Other frameworks: ISO 27001 A.8.11 · GDPR Art. 25 · NIST CSF 2.0 GV.RM-06

---

### DSGAI19 — Human-in-Loop & Labeler Overexposure

**Severity:** Medium

Human annotators access sensitive model inputs during labelling.
From an ATLAS perspective, labelling vendors are a supply chain
access path — adversaries who compromise or operate labelling services
gain access to sensitive training data.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Exfiltrate via ML Inference API | AML.T0035 | Exfiltration | Sensitive data in labelling tasks accessed by adversary-controlled or compromised labelling vendor |
| Data from Information Repositories | AML.T0057 | Exfiltration | Labelling vendor's data stores containing sensitive annotation tasks accessed as information repositories |
| Poison Training Data | AML.T0020 | ML Attack Staging | Adversary-controlled labelling vendor introduces biased or poisoned annotations into training data |

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0057: Treat labelling vendors as
  third-party suppliers — security assessment before
  engagement limits adversary-controlled vendor risk
- Counter AML.T0020: Data minimisation in labelling
  tasks — adversary sees minimum content, limiting
  both exfiltration value and poisoning opportunity

**Hardening**
- Counter AML.T0035: Anonymise sensitive content
  before labelling — adversary accessing labelling
  vendor systems finds anonymised data rather than
  raw sensitive records

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.34 · GDPR Art. 28 · NIST CSF 2.0 GV.SC-01

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High

Adversaries reconstruct a functional model replica through systematic
querying. AML.T0016 (Extract ML Model) is the canonical ATLAS
technique for this threat.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Extract ML Model | AML.T0016 | Exfiltration | Adversary systematically queries model to extract sufficient information to replicate its functionality |
| Exfiltrate via Cyber Means | AML.T0025 | Exfiltration | Query results and model outputs systematically collected and transmitted to adversary infrastructure |
| Cost Harvesting | AML.T0034 | Impact | High-volume model extraction queries consume significant compute resources — financial impact alongside IP theft |

#### Real-world ATLAS cases

- Multiple documented model extraction campaigns
  against commercial LLM APIs (2024) — systematic
  querying to replicate model capabilities

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0016: API rate limiting — systematic
  extraction requires high query volumes, hard caps
  raise cost and trigger detection before AML.T0016
  succeeds
- Counter AML.T0034: Per-user cost budgets —
  extraction campaigns bounded by cost limits

**Hardening**
- Counter AML.T0016: Query diversity monitoring —
  AML.T0016 produces characteristic query patterns
  (systematic output space coverage) detected through
  anomaly analysis

**Advanced**
- Red team AML.T0016: Model extraction attempt using
  your own API — quantify query budget required for
  meaningful replication, verify rate limiting
  prevents success at that budget

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.5.12 · MITRE ATT&CK (IT) · NIST CSF 2.0 DE.CM-09

---

### DSGAI21 — Disinformation via Data Poisoning

**Severity:** High

False content injected into RAG corpora causes GenAI to surface
misinformation as authoritative. AML.T0045 (Publish Poisoned Datasets)
is the primary ATLAS technique — adversaries release false content
into retrieval sources without needing training access.

#### ATLAS technique mapping

| Technique | ID | Tactic | How it applies |
|---|---|---|---|
| Publish Poisoned Datasets | AML.T0045 | ML Attack Staging | Adversary publishes false content in public repositories, documentation sites, or knowledge bases indexed by RAG systems |
| Poison Training Data | AML.T0020 | ML Attack Staging | Adversary introduces false content into RAG corpus through ingestion path — no public publication required |
| Craft Adversarial Data | AML.T0031 | ML Attack Staging | False content crafted to appear authoritative and rank highly in semantic similarity searches |

#### Real-world ATLAS cases

- Grok RAG incident (2025) — production RAG system
  surfaced externally introduced false information as
  authoritative output
- Crowdsourced dataset poisoning campaigns targeting
  open training corpora — active documented attack class

#### Mitigations mapped to ATLAS

**Foundational**
- Counter AML.T0045: Source trust tiering in RAG
  retrieval — adversary-published content in low-trust
  sources weighted down, authoritative sources prioritised
- Counter AML.T0020: RAG ingestion integrity controls —
  source allowlisting and content validation gates
  prevent AML.T0020 through known ingestion paths

**Hardening**
- Counter AML.T0031: Cryptographic provenance for
  authoritative sources in RAG — adversary cannot
  craft content that passes provenance verification
  for trusted source tier

**Advanced**
- Red team AML.T0045: Adversarial RAG integrity
  testing — attempt to surface false content through
  public sources indexed by your RAG system, verify
  trust tiering effectiveness

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.5.7 · NIST CSF 2.0 GV.SC-01 · SOC 2 PI1.2

---

## ATLAS threat model for GenAI data security

### Attack path analysis

The most dangerous DSGAI attack paths from an ATLAS perspective
involve technique chaining across multiple tactics:

**Path 1 — Training pipeline compromise:**
AML.T0012 (Obtain Capabilities) ?
AML.T0020 (Poison Training Data) ?
AML.T0018 (Backdoor ML Model) ?
Production deployment with embedded backdoor

**Path 2 — Inference exfiltration:**
AML.T0013 (Discover ML Model Ontology) ?
AML.T0051 (Exploit Public-Facing Application) ?
AML.T0035 (Exfiltrate via ML Inference API) ?
Sensitive training data or RAG content extracted

**Path 3 — Supply chain and disinformation:**
AML.T0045 (Publish Poisoned Datasets) ?
AML.T0031 (Craft Adversarial Data) ?
RAG corpus poisoned via public source indexing ?
GenAI surfaces adversary content as authoritative

**Path 4 — Model theft:**
AML.T0013 (Discover ML Model Ontology) ?
AML.T0016 (Extract ML Model) ?
AML.T0025 (Exfiltrate via Cyber Means) ?
Functional model replica constructed without training access

### Priority DSGAI entries by ATLAS threat severity

| ATLAS priority | DSGAI entries | Rationale |
|---|---|---|
| Immediate — active attack class | DSGAI01, DSGAI04, DSGAI12, DSGAI21 | AML.T0035, AML.T0020, AML.T0045 are active, documented attack techniques |
| High — rising threat | DSGAI13, DSGAI18, DSGAI20 | AML.T0024.000, AML.T0016 increasingly commoditised |
| Medium — exploitable at scale | DSGAI03, DSGAI06, DSGAI11 | AML.T0057, AML.T0051 require less sophistication as tooling matures |

---

## References

- [MITRE ATLAS](https://atlas.mitre.org)
- [MITRE ATLAS Techniques](https://atlas.mitre.org/techniques)
- [MITRE ATLAS Case Studies](https://atlas.mitre.org/studies)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [LLM Top 10 × MITRE ATLAS](../llm-top10/LLM_MITREATLAS.md)
- [Agentic Top 10 × MITRE ATLAS](../agentic-top10/Agentic_MITREATLAS.md)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full entries with ATLAS attack path analysis | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
