<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks and Mitigations 2026 (DSGAI01-DSGAI21)
  Framework   : MAESTRO — Multi-Agent Environment, Security, Threat, Risk, and Outcome
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × MAESTRO

Mapping the [OWASP GenAI Data Security Risks and Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to [MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
(Multi-Agent Environment, Security, Threat, Risk, and Outcome) —
the Cloud Security Alliance's threat modeling framework for agentic AI.

**Created by:** Ken Huang, CEO & Chief AI Officer, DistributedApps.ai;
Co-Chair of AI Safety Working Groups, Cloud Security Alliance.

---

## MAESTRO and GenAI data security

The DSGAI 2026 taxonomy follows sensitive data through the full GenAI
system lifecycle — from ingestion through training through inference
through disposal. MAESTRO's seven-layer architecture provides the
structural map that explains *where* each data security risk lives
and *how* it propagates.

The critical insight for data security practitioners is that MAESTRO
Layer 2 (Data Operations) is the originating layer for the majority
of DSGAI entries. MAESTRO explicitly designates data operations as
the layer responsible for all data that shapes AI agent behaviour —
not just training corpora, but operational data stores, RAG pipelines,
embedding infrastructure, and telemetry. The security of these assets
is a first-class MAESTRO concern, not a footnote.

Five DSGAI entries originate at layers other than L2 and propagate
into it — DSGAI02 (credential exposure at L6), DSGAI03 (shadow AI
governance at L7), DSGAI12 (NL gateway exploitation at L3), DSGAI16
(endpoint overreach at L4), and DSGAI17 (availability at L4/L7).
Understanding the originating layer for each entry directs remediation
to the right team and system component.

---

## MAESTRO layer reference

| Layer | ID | Description |
|---|---|---|
| Foundation Models | L1 | Base LLMs — reasoning, generation, instruction following |
| Data Operations | L2 | Ingestion, storage, RAG, embeddings, vector stores, memory |
| Agent Frameworks | L3 | Orchestration, tool registries, MCP, plugins |
| Deployment & Infrastructure | L4 | Servers, containers, networks, CI/CD, runtime |
| Evaluation & Observability | L5 | Monitoring, logging, telemetry, drift detection |
| Security & Compliance | L6 | Identity, access control, audit, governance |
| Agent Ecosystem | L7 | Multi-agent interaction, A2A, cascade dynamics |

---

## DSGAI-to-MAESTRO layer mapping

| ID | Name | Originating Layer | Secondary Layers |
|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | L2 | L1, L5, L6 |
| DSGAI02 | Agent Identity & Credential Exposure | L6 | L2, L7 |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | L7 | L6, L2 |
| DSGAI04 | Data, Model & Artifact Poisoning | L2 | L1, L4, L5 |
| DSGAI05 | Data Integrity & Validation Failures | L2 | L4, L3 |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | L3 | L2, L6 |
| DSGAI07 | Data Governance, Lifecycle & Classification | L2 | L6, L5 |
| DSGAI08 | Non-Compliance & Regulatory Violations | L6 | L2, L7 |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | L2 | L1, L5 |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | L2 | L1, L6 |
| DSGAI11 | Cross-Context Conversation Bleed | L2 | L6, L3 |
| DSGAI12 | Unsafe NL Data Gateways | L3 | L2, L6 |
| DSGAI13 | Vector Store Platform Security | L2 | L4, L6 |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | L5 | L2, L6 |
| DSGAI15 | Over-Broad Context Windows | L2 | L1, L3 |
| DSGAI16 | Endpoint & Browser Assistant Overreach | L4 | L2, L6 |
| DSGAI17 | Data Availability & Resilience Failures | L4 | L7, L5 |
| DSGAI18 | Inference & Data Reconstruction | L1 | L2, L5 |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | L2 | L6, L7 |
| DSGAI20 | Model Exfiltration & IP Replication | L1 | L5, L6 |
| DSGAI21 | Disinformation via Data Poisoning | L2 | L1, L5 |

---

## Quick-reference summary

| ID | Name | Severity | Primary MAESTRO Layer | Tier |
|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | L2 Data Operations | Foundational–Advanced |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | L6 Security & Compliance | Foundational–Advanced |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | L7 Agent Ecosystem | Foundational–Hardening |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | L2 Data Operations | Hardening–Advanced |
| DSGAI05 | Data Integrity & Validation Failures | High | L2 Data Operations | Foundational–Hardening |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | L3 Agent Frameworks | Foundational–Hardening |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | L2 Data Operations | Foundational–Advanced |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | L6 Security & Compliance | Foundational–Advanced |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | L2 Data Operations | Hardening–Advanced |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | L2 Data Operations | Hardening–Advanced |
| DSGAI11 | Cross-Context Conversation Bleed | High | L2 Data Operations | Foundational–Hardening |
| DSGAI12 | Unsafe NL Data Gateways | Critical | L3 Agent Frameworks | Foundational–Advanced |
| DSGAI13 | Vector Store Platform Security | High | L2 Data Operations | Foundational–Hardening |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | L5 Evaluation & Observability | Foundational–Hardening |
| DSGAI15 | Over-Broad Context Windows | High | L2 Data Operations | Foundational–Hardening |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | L4 Deployment & Infrastructure | Foundational–Hardening |
| DSGAI17 | Data Availability & Resilience Failures | High | L4 Deployment & Infrastructure | Foundational–Advanced |
| DSGAI18 | Inference & Data Reconstruction | High | L1 Foundation Models | Hardening–Advanced |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | L2 Data Operations | Foundational–Hardening |
| DSGAI20 | Model Exfiltration & IP Replication | High | L1 Foundation Models | Hardening–Advanced |
| DSGAI21 | Disinformation via Data Poisoning | High | L2 Data Operations | Hardening–Advanced |

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical | **Originating layer:** L2 — Data Operations

Sensitive data leakage through GenAI systems is fundamentally an L2
failure — the data is in the data operations layer (training corpora,
RAG stores, embeddings, prompt caches) and the leakage path runs
through L1 inference output, evading L5 monitoring, and bypassing
L6 access controls.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
The data operations layer holds all sensitive data that can leak
through GenAI outputs. Classification, access control, and encryption
at L2 determine whether sensitive data is even accessible for leakage.
Over-permissive RAG retrieval — where the retrieval system returns
documents beyond the querying user's authorisation scope — is the
most common L2 leakage enabler.

**L1 — Foundation Models (leakage channel)**
The model extracts and surfaces sensitive content from its training
data or context window through inference outputs. Membership inference
and model inversion are L1 attack techniques that exploit the model's
encoding of training data.

**L5 — Evaluation & Observability (detection)**
DLP on model outputs is an L5 observability control. Without L5
output scanning, sensitive data leakage goes undetected until
downstream consequence.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Encrypt all data at rest in GenAI scope. RBAC on all RAG collections. Least-privilege retrieval aligned to user authorisation. |
| L1 | Differential privacy in training for sensitive corpora. Confidence score suppression to limit membership inference. |
| L5 | DLP on all model output channels. Sensitive pattern detection before delivery. |
| L6 | Access controls on observability pipelines — telemetry stores containing sensitive inference data protected as production data. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Over-permissive RAG retrieval returning unauthorised documents | L2 | P1 |
| Sensitive training data extraction via inference API | L1 | P1 |
| Sensitive content in cleartext observability logs | L5 | P1 |
| DLP bypass via multimodal output (image, audio) | L2 → L1 | P2 |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.11/A.8.12 · NIST CSF 2.0 PR.DS-01 · EU AI Act Art. 10

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical | **Originating layer:** L6 — Security & Compliance

Agent credential exposure is an L6 failure — the credential lifecycle
management, scope controls, and storage security that govern NHIs
live in the Security & Compliance layer. When they fail, credentials
leak to L2 (logs, memory stores) or enable L7 lateral movement.

#### MAESTRO layer analysis

**L6 — Security & Compliance (primary)**
Long-lived credentials, over-privileged scope, cleartext storage in
configuration or agent memory, and shared credentials across instances
are all L6 failures. Each represents a failure in the NHI lifecycle
management that L6 is responsible for.

**L2 — Data Operations (leakage destination)**
Credentials frequently appear in L2 data stores: agent memory, RAG
indexes seeded from operational data, and telemetry logs capturing
request headers. L2 controls prevent credential content from
being indexed or persisted.

**L7 — Agent Ecosystem (lateral movement)**
A compromised credential is used at L7 to move laterally across the
agent ecosystem — directing sub-agents, accessing shared memory,
or invoking cross-cluster tools.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L6 | Short-lived JIT credentials per session. Unique NHI per agent. Minimum scope. Credential anomaly detection. |
| L2 | Credential scanning before any content enters memory or RAG index. No cleartext credential in telemetry. |
| L7 | Inter-agent trust boundaries preventing credential-enabled lateral movement beyond defined cluster scope. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Credential in cleartext agent memory | L6 → L2 | P1 |
| Long-lived credential enabling post-session access | L6 | P1 |
| Credential leakage via tool call payload | L6 → L3 | P1 |
| Lateral movement via stolen agent credential | L7 ← L6 | P2 |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: OWASP NHI Top 10 · NIST CSF 2.0 PR.AA-01 · ISO 27001 A.8.2

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High | **Originating layer:** L7 — Agent Ecosystem

Shadow AI is an L7 governance failure — unsanctioned AI services are
external ecosystem participants that the organisation's agent
governance programme does not cover. The data flows to these services
are ungoverned L7 interactions.

#### MAESTRO layer analysis

**L7 — Agent Ecosystem (primary)**
Shadow AI tools are part of the broader agent ecosystem the
organisation's employees interact with — they are ecosystem
participants outside governance scope. MAESTRO's L7 model requires
that all ecosystem interactions be governed, including those with
external AI services not operated by the organisation.

**L6 — Security & Compliance (policy gap)**
The absence of an acceptable use policy covering AI tools is an L6
governance gap. L6 is responsible for defining what ecosystem
interactions are authorised.

**L2 — Data Operations (data exposure)**
Sensitive data pasted into shadow AI tools leaves the organisation's
L2 data operations perimeter and enters an external data store with
unknown controls.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L7 | Approved AI tool programme — only ecosystem-approved AI services. DLP at network egress blocking unapproved AI endpoints. |
| L6 | Acceptable use policy covering all AI tools. Shadow AI detection programme. |
| L2 | Data classification awareness training — what L2 data must not be used with unapproved tools. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Sensitive data submitted to adversary-controlled AI service | L7 | P1 |
| Unapproved AI SaaS vendor with insufficient data protection | L7 | P1 |
| Shadow AI use evading DLP controls | L7 → L2 | P2 |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: NIST CSF 2.0 GV.OC-01 · ISO 27001 A.5.10/A.5.23 · EU AI Act Art. 25

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical | **Originating layer:** L2 — Data Operations

Training data and RAG corpus poisoning originates at L2. Model weight
poisoning (backdooring) originates at L4 during the build pipeline
phase. Both manifest their effects at L1, and both evade L5 detection
through plausible-but-wrong outputs.

#### MAESTRO layer analysis

**L2 — Data Operations (primary — training and RAG)**
The training data pipeline and RAG ingestion pipeline are L2 systems.
Adversary-controlled content entering either pipeline is an L2
integrity failure. MAESTRO treats both training data and operational
retrieval data as equally critical L2 assets — a poisoned RAG corpus
causes production harm equivalent to a poisoned training corpus for
the systems that rely on it.

**L4 — Deployment & Infrastructure (model weight poisoning)**
Model weight backdoors are introduced at L4 — either through a
compromised training infrastructure or through a supply chain attack
delivering pre-poisoned weights. The effect manifests at L1 but the
attack originates at L4.

**L1 — Foundation Models (manifestation)**
Poisoned behaviour — whether from L2 data or L4 weights — is a
property of the L1 model at inference time. Detection requires
testing at L1 (trigger-based backdoor detection) before deployment.

**L5 — Evaluation & Observability (detection)**
Poisoning is designed to evade L5 monitoring through outputs that
appear statistically normal. L5 must actively test for poisoning
rather than passively monitoring output distributions.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Source allowlisting. Anomaly detection on data distributions before training runs. Provenance tracking from source to training dataset. |
| L4 | ML SBOM. Model weight integrity verification at deployment. Isolated evaluation environment for new components. |
| L1 | Post-training backdoor detection as mandatory deployment gate. Model rollback capability always available. |
| L5 | Active poisoning detection — output monitoring designed to detect systematic bias, not just statistical anomalies. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Adversary-controlled content in training corpus | L2 | P1 |
| Poisoned RAG corpus via compromised documentation source | L2 | P1 |
| Backdoored model weights via supply chain | L4 → L1 | P1 |
| Poisoning evading L5 through plausible output | L5 | P1 |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain, LLM04 Data & Model Poisoning
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0020 · NIST AI RMF MS-3.3 · ISO 27001 A.8.27

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High | **Originating layer:** L2 — Data Operations

Adversarially crafted payloads exploiting ingestion vulnerabilities
originate at L2 — the ingestion boundary is an L2 trust boundary.
CVE-2024-3584 class path traversal vulnerabilities enable attackers
to escalate from L2 ingestion access to L4 infrastructure write access.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
The ingestion interface is the L2 trust boundary where external
content enters the data operations layer. Insufficient validation
at this boundary allows crafted payloads to exploit parser
vulnerabilities or inject malicious content before any downstream
control sees it.

**L4 — Deployment & Infrastructure (escalation)**
Path traversal vulnerabilities in L2 snapshot import operations
achieve arbitrary file write on L4 hosts — a direct path from L2
compromise to L4 infrastructure control.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Multi-stage validation at all ingestion boundaries — syntactic, schema, semantic, path traversal prevention. |
| L4 | Patch CVE-2024-3584 class immediately. Sandbox snapshot import operations. |
| L3 | Enforce schema validation on all content entering agent framework through tool payloads. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Path traversal in snapshot import | L2 → L4 | P1 |
| Adversarial payload bypassing syntactic validation | L2 | P1 |
| Semantic injection passing schema validation | L2 → L1 | P2 |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-20 · NIST CSF 2.0 PR.PS-04

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange

**Severity:** High | **Originating layer:** L3 — Agent Frameworks

Tools and plugins are L3 components. The data exchange between the
agent framework and external tools crosses an L3 trust boundary —
context payloads flowing to tools may contain sensitive L2 data,
and adversary-controlled or compromised tools can capture and
exfiltrate that data.

#### MAESTRO layer analysis

**L3 — Agent Frameworks (primary)**
The tool registry, plugin loader, and MCP protocol handler are all
L3 components. They determine what data is included in tool call
payloads. Over-broad context payloads — sending full conversation
history or broad process data to a tool that needs only a specific
field — create unnecessary data exposure at every L3 tool call.

**L2 — Data Operations (data source)**
The sensitive data that reaches tools originates in L2 — retrieved
documents, memory entries, and data store content that the agent
includes in its context and passes to tool payloads.

**L6 — Security & Compliance (vendor governance)**
Tool providers are third-party supply chain participants. L6 vendor
governance controls determine whether tool providers are assessed,
whether contracts include data handling obligations, and whether
tools are subject to the organisation's security requirements.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L3 | Context minimisation — tools receive minimum payload required, not full conversation context. DLP on outbound tool payloads. |
| L2 | Data classification tracked through to tool call — tool receives data at the classification level it is authorised to handle. |
| L6 | Tool providers assessed under vendor security programme. Contracts include data handling and zero-training obligations. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Sensitive context captured by adversary-controlled tool | L3 | P1 |
| Full conversation history in tool payload — over-broad context | L3 → L2 | P1 |
| Tool vendor using call data for model training without consent | L6 | P2 |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI04 Supply Chain
- Other frameworks: ISO 27001 A.5.19/A.5.20 · NIST CSF 2.0 GV.SC-01 · EU AI Act Art. 25

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High | **Originating layer:** L2 — Data Operations

GenAI creates ungoverned L2 data assets — embeddings, prompt caches,
fine-tuned model adapters, and telemetry traces derived from sensitive
source data. These assets inherit the sensitivity of their sources
but fall outside traditional data governance programmes because they
were not anticipated by the classification framework.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
The data operations layer is where ungoverned derived assets are
created. Every embedding generation run, every RAG cache refresh,
and every telemetry trace is an L2 data creation event that the
governance programme must capture.

**L6 — Security & Compliance (governance gap)**
The absence of classification policies covering L2 derived assets
is an L6 governance gap. L6 is responsible for defining what assets
require governance, not just traditional structured data.

**L5 — Evaluation & Observability (discovery)**
New ungoverned L2 data stores are often first discoverable through
L5 observability — data flow monitoring reveals stores that the
governance programme did not know existed.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Classification propagation — derived assets inherit source classification. Deletion of source triggers deletion of all derived representations. |
| L6 | Extend governance programme to cover all L2 derived asset types. Asset inventory includes embeddings, caches, traces, adapters. |
| L5 | Data flow monitoring detects ungoverned L2 stores — alert on new data flows not covered by governance programme. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Sensitive embeddings not classified as sensitive | L2 | P1 |
| Prompt cache containing PII with no retention policy | L2 | P1 |
| Ungoverned L2 store discovered by adversary | L2 → L6 | P2 |

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI01 Sensitive Data Leakage
- Other frameworks: ISO 27001 A.5.9/A.8.10 · EU AI Act Art. 10 · NIST CSF 2.0 ID.AM-08

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High | **Originating layer:** L6 — Security & Compliance

Regulatory compliance is an L6 responsibility. GenAI deployments
trigger obligations (GDPR, EU AI Act, HIPAA, PCI DSS, NERC CIP) that
L6 must identify, document, and satisfy. Non-compliance creates legal
exposure in addition to the underlying security risk.

#### MAESTRO layer analysis

**L6 — Security & Compliance (primary)**
The Security & Compliance layer is explicitly responsible for
governance frameworks and auditability in MAESTRO's architecture.
Regulatory scoping, obligation mapping, and compliance evidence
generation are L6 functions.

**L2 — Data Operations (compliance scope)**
Most GenAI regulatory obligations — EU AI Act Art. 10 data governance,
GDPR data processing records, HIPAA PHI controls — focus on L2 data
assets. L6 compliance programme must cover L2 data handling.

**L7 — Agent Ecosystem (regulatory surface expansion)**
Multi-agent deployments expand the regulatory surface by creating
additional data flows, additional processors, and additional
jurisdictional interactions at L7.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L6 | Regulatory scoping assessment before each GenAI deployment. Obligation mapping per regulation. Incident notification procedures documented and tested. |
| L2 | Article 30 records of processing updated to cover all L2 GenAI data assets. Data handling aligned to applicable regulations. |
| L7 | Multi-agent data flow mapping — all cross-agent data flows documented for regulatory records. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| GenAI deployment triggering unrecognised obligations | L6 | P1 |
| L2 training data violating GDPR Art. 5 lawful basis | L2 → L6 | P1 |
| Multi-agent data flow creating cross-border transfer obligation | L7 → L6 | P2 |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance
- Other frameworks: EU AI Act Art. 10/17 · ISO 27001 A.5.31 · NIST CSF 2.0 GV.OC-01

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High | **Originating layer:** L2 — Data Operations

Multimodal GenAI processes images and audio — OCR and transcription
pipelines are L2 data operations that extract content from non-text
sources. The extracted content may be sensitive but is often not
treated with the same classification as the source modality.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
OCR and transcription are L2 data processing operations. Their output
— text extracted from images or audio — is an L2 data asset that
inherits the classification of the source. A passport image and the
OCR text extracted from it are equally sensitive; the extracted text
must be treated as Restricted data, not general text.

**L1 — Foundation Models (multimodal inference)**
The foundation model processes multimodal inputs at L1. Sensitive
content embedded in images or audio enters the L1 context window
through the multimodal inference path.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Classification inheritance for all OCR/transcription output. Short retention for multimodal uploads and derived text. DLP on extraction pipeline output before storage. |
| L1 | No persistent storage of multimodal inference context beyond session boundary. |
| L5 | DLP monitoring on multimodal extraction output channels. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| OCR of sensitive document treated as unclassified text | L2 | P1 |
| Sensitive content in audio transcription not protected | L2 | P1 |
| Multimodal extraction output in cleartext telemetry | L5 → L2 | P2 |

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI14 Telemetry Leakage
- Other frameworks: ISO 27001 A.8.11 · GDPR Art. 9 · NIST CSF 2.0 PR.DS-01

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium | **Originating layer:** L2 — Data Operations

Synthetic data generation and anonymisation are L2 data processing
operations. Their outputs are L2 assets that may retain re-identification
risk — making them potentially as sensitive as the source data despite
their apparent anonymisation.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
Synthetic datasets and anonymised corpora are created through L2
processing pipelines. The risk is that the L2 output inherits
re-identification properties of the L2 source — differential privacy
budget exhaustion, embedding-level linkage, and statistical inference
can all reconstruct individual-level information from apparently
de-identified L2 assets.

**L1 — Foundation Models (inference attack surface)**
A model trained on synthetic data may expose the re-identification
risk through its L1 outputs — membership inference attacks against
the model can confirm the presence of specific individuals in the
training corpus even when the training data was described as synthetic.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Treat synthetic datasets as sensitive until formal re-identification risk assessment is complete. Apply differential privacy during generation. |
| L1 | Membership inference testing before any model trained on synthetic data is deployed. |
| L6 | Formal risk acceptance process before any synthetic dataset is released externally. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Re-identification of synthetic dataset via membership inference | L2 → L1 | P2 |
| Privacy budget exhaustion enabling reconstruction | L2 | P2 |
| Synthetic data released without re-identification assessment | L6 | P1 |

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.5.34 · GDPR Recital 26 · NIST CSF 2.0 GV.RM-06

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High | **Originating layer:** L2 — Data Operations

Session isolation failure is an L2 data boundary failure — user
session data is an L2 asset that must be isolated per user. When
the L2 isolation controls fail, one user's conversation context
becomes accessible to another user's inference query.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
Per-user session data, RAG namespace isolation, and KV cache
separation are L2 data operations controls. Their failure allows
L2 data from one user context to contaminate another.

**L6 — Security & Compliance (access control)**
Per-user authorisation boundaries are L6 controls. The RAG retrieval
system must enforce L6 authorisation at the L2 retrieval boundary —
a user's query can only retrieve documents within their authorised
namespace.

**L3 — Agent Frameworks (context assembly)**
The agent framework assembles context at L3. Framework-level
isolation controls ensure that context assembled for one user's
session does not include content from another user's session.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Per-user RAG namespaces. KV cache isolation. Session data encrypted and scoped to user identity. |
| L6 | L6 authorisation enforced at L2 retrieval boundary — queries can only retrieve from authorised namespace. |
| L3 | Framework-level context isolation — no cross-user context assembly regardless of query formulation. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Crafted query retrieving another user's documents | L2 ← L6 | P1 |
| KV cache containing previous user's context | L2 | P1 |
| Framework assembling cross-user context | L3 → L2 | P2 |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3 · GDPR Art. 32 · NIST CSF 2.0 PR.AA-05

---

### DSGAI12 — Unsafe Natural-Language Data Gateways

**Severity:** Critical | **Originating layer:** L3 — Agent Frameworks

NL-to-data interfaces are L3 components — they are tools in the
agent framework layer that translate natural language queries into
structured data operations. The security failure is an L3 design
flaw: the tool executes under a high-privilege credential, applies
no query allowlisting, and passes LLM-generated queries directly to
backend data systems without validation.

#### MAESTRO layer analysis

**L3 — Agent Frameworks (primary)**
The NL data gateway is a tool registered in the L3 framework. Its
design determines whether it applies least privilege, query
allowlisting, and parameter validation. These are L3 design decisions,
not model behaviours.

**L2 — Data Operations (data exposure)**
The backend data systems — historian, CMMS, database — are L2 assets.
The NL gateway creates a direct L3 → L2 access path that bypasses
the access controls the L2 system would normally enforce if accessed
through a conventional interface.

**L6 — Security & Compliance (privilege scope)**
The credential under which the NL gateway executes is an L6 asset.
Per-user execution — the gateway queries under the requesting user's
permissions rather than a shared high-privilege service account —
is an L6 control that limits the blast radius of any L3 injection.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L3 | Query allowlisting enforced at L3 dispatch. Parameterised execution. Read-only by default — no write operations through NL gateway without explicit approval. |
| L2 | Row-level security on backend data systems. No bulk export permitted through NL gateway credentials. |
| L6 | Per-user query execution — NL gateway uses requesting user's credential, not shared high-privilege account. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Injection via NL query generating bulk extraction SQL | L3 → L2 | P1 |
| Destructive query (DELETE, DROP) via NL gateway | L3 | P1 |
| NL gateway executing under shared high-privilege account | L6 → L3 | P1 |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-89 · ISA/IEC 62443 SR 2.2 (OT)

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High | **Originating layer:** L2 — Data Operations

Vector databases are L2 data operations infrastructure. Their default
security posture — often unauthenticated access, no encryption at
rest, and known path traversal vulnerabilities — makes them a
high-risk L2 target. They are frequently treated as caches rather
than sensitive data stores, creating a protection gap.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
The vector store is an L2 asset containing embeddings of potentially
sensitive source documents. Its security posture must match that of
the source documents, not a lesser "derived data" standard.

**L4 — Deployment & Infrastructure (CVE surface)**
Vector database CVEs — CVE-2024-3584 (Qdrant path traversal) class —
represent L4 vulnerabilities in the infrastructure hosting L2 data.
They must be patched with the same urgency as production database CVEs.

**L6 — Security & Compliance (access control)**
RBAC on vector store collections is an L6 access control applied
to an L2 asset. No vector store collection should be accessible
without authentication in any environment.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Encrypt vector store content at rest. Content classified at same level as source documents. |
| L4 | Patch all vector database CVEs immediately. Network-isolate vector stores to authorised consumers only. |
| L6 | RBAC on all collections from day one. No unauthenticated access in any environment including development. |
| L5 | Monitor vector store query patterns — bulk extraction and unusual diversity alerted. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Unauthenticated bulk extraction from exposed vector store | L2 ← L6 | P1 |
| Path traversal achieving host write via snapshot import | L4 | P1 |
| Embedding inversion reconstructing source documents | L2 → L1 | P2 |

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3/A.8.24 · CWE-284 · NIST CSF 2.0 PR.AA-05

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High | **Originating layer:** L5 — Evaluation & Observability

Observability pipelines are L5 systems. They capture full inference
inputs, outputs, and context windows — making them secondary data
stores containing sensitive L2 content at scale, often with weaker
access controls and longer retention than production systems.

#### MAESTRO layer analysis

**L5 — Evaluation & Observability (primary)**
The observability layer is both the necessary monitoring control and
a potential data leakage vector. The same L5 pipeline that enables
security monitoring also creates a high-value target for adversaries
who cannot access the production L2 data directly.

**L2 — Data Operations (data captured)**
The sensitive data appearing in L5 telemetry originated in L2 —
it was retrieved from L2 stores, processed at L1, and captured at
L5. L2 controls (PAN masking, PII redaction before logging) reduce
what enters L5.

**L6 — Security & Compliance (access governance)**
L5 telemetry stores require the same L6 access controls as production
L2 data. "Just logs" is not a justification for weaker protection
when those logs contain sensitive inference content.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L5 | Least-logging defaults — capture only what is needed for defined monitoring purposes. Short TTL for debug traces. |
| L2 | PAN masking and PII redaction before any content enters the L5 telemetry pipeline. |
| L6 | Access controls on all L5 telemetry stores equivalent to production L2 data. Need-to-know enforced. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Sensitive inference content in cleartext telemetry | L5 ← L2 | P1 |
| Telemetry store with weaker access controls than production data | L5 ← L6 | P1 |
| Extended telemetry retention creating persistent data exposure | L5 | P2 |

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance
- Other frameworks: ISO 27001 A.8.15 · GDPR Art. 32 · NIST CSF 2.0 GV.OC-01

---

### DSGAI15 — Over-Broad Context Windows

**Severity:** High | **Originating layer:** L2 — Data Operations

Context window assembly is a joint L2 (what data is retrieved) and
L3 (how the framework assembles context) operation. Over-broad
context injection aggregates data from multiple trust domains into a
single flat namespace, maximising the value of any successful injection
that reaches the context.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
The RAG retrieval system is an L2 component. Minimum-necessary
retrieval — returning only passages directly relevant to the query,
not broad datasets — is an L2 design principle. Over-retrieval is
an L2 failure that amplifies every downstream risk.

**L1 — Foundation Models (amplification)**
The over-broad context window reaches L1 as a large, data-rich
context. Any injection that succeeds at L1 has access to the entire
aggregated context, maximising the data available for exfiltration.

**L3 — Agent Frameworks (context assembly)**
The framework's context assembly logic determines what retrieved L2
content is included in the final context window. Framework-level
minimum-necessary enforcement limits context window breadth
independently of retrieval system behaviour.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Minimum-necessary retrieval — return only passages directly relevant to query, not broad datasets. Source trust level carried through retrieval. |
| L3 | Framework-level context size limits. Classification ceiling tracking — highest classification of any injected document drives response handling. |
| L1 | Structural prompt architecture separating content from different trust levels within the context window. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Injection gaining access to aggregated cross-domain context | L1 ← L2 | P1 |
| Classification ceiling not tracked — classified content drives unclassified output | L2 → L3 | P1 |
| Context window containing data from incompatible trust domains | L2 → L1 | P2 |

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- Agentic Top 10: ASI01 Agent Goal Hijack
- Other frameworks: ISO 27001 A.8.3 · NIST CSF 2.0 PR.AA-05 · AIUC-1 A/B005

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High | **Originating layer:** L4 — Deployment & Infrastructure

Browser AI assistants are L4 deployment assets — software installed
on endpoint devices that operate within the local execution environment.
Their access to sensitive data across open applications is a function
of their L4 deployment configuration and the permissions granted by
the endpoint's operating system.

#### MAESTRO layer analysis

**L4 — Deployment & Infrastructure (primary)**
The browser extension or assistant is an L4 deployment on an endpoint
device. Its permission model — what applications, tabs, and data
sources it can access — is configured at L4 through device management
and browser permission controls.

**L2 — Data Operations (data at risk)**
The sensitive data accessible to browser assistants — documents in
open applications, browser tabs containing authenticated sessions,
clipboard content — is effectively L2 data from the assistant's
perspective, available for capture and exfiltration.

**L6 — Security & Compliance (vendor governance)**
Browser AI extension providers are L6 supply chain participants.
Vendor assessment before deployment and contractual data handling
obligations are L6 controls.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L4 | Approved extensions only on managed devices. Permission minimisation — browser assistant access restricted to minimum required scope. Unapproved extensions blocked at device management layer. |
| L2 | Sensitive application data access by browser assistants monitored and alerted. |
| L6 | Browser AI extension providers assessed under vendor security programme before deployment. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Browser assistant capturing sensitive data across all open tabs | L4 → L2 | P1 |
| Compromised browser extension acting as endpoint backdoor | L4 | P1 |
| Unapproved extension with data exfiltration capability | L4 → L6 | P2 |

#### Cross-references
- Agentic Top 10: ASI10 Rogue Agents
- DSGAI 2026: DSGAI03 Shadow AI
- Other frameworks: ISO 27001 A.8.1/A.8.7 · NIST CSF 2.0 GV.SC-01 · EU AI Act Art. 9

---

### DSGAI17 — Data Availability & Resilience Failures

**Severity:** High | **Originating layer:** L4 — Deployment & Infrastructure

Silent pipeline failures in GenAI advisory systems originate at L4 —
the infrastructure hosting the vector store, retrieval system, or
inference endpoint degrades without the L5 monitoring system detecting
the degradation in time. The consequence — serving stale or incorrect
data as current — propagates through L7 in multi-agent deployments.

#### MAESTRO layer analysis

**L4 — Deployment & Infrastructure (primary)**
The deployment infrastructure — vector store refresh jobs, RAG
pipeline schedulers, inference endpoint health — is where silent
failures originate. Circuit breakers and graceful degradation are
L4 design controls.

**L7 — Agent Ecosystem (cascade propagation)**
In multi-agent deployments, an L4 availability failure in one
pipeline component can cascade through L7 — downstream agents
consuming stale outputs from a degraded upstream agent compound
the error across the ecosystem.

**L5 — Evaluation & Observability (detection gap)**
Silent availability failures evade L5 monitoring when monitoring
is configured for binary up/down status rather than data freshness.
L5 must monitor the age of the data being served, not just whether
the service is responding.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L4 | Circuit breakers and graceful degradation — explicit unavailability notice when pipeline is degraded, not silent misinformation. Freshness monitoring on all data pipelines. |
| L7 | Circuit breakers at L7 agent-to-agent boundaries — a degraded upstream agent does not propagate incorrect data downstream. |
| L5 | Freshness monitoring as L5 observability control — alert when data age exceeds defined threshold before incorrect data reaches users. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Stale RAG index serving outdated information as current | L4 → L5 | P1 |
| Silent inference endpoint degradation with no operator notification | L4 | P1 |
| Availability failure cascading through multi-agent pipeline | L7 ← L4 | P2 |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: ISA/IEC 62443 SR 7.6 (OT) · NIST CSF 2.0 PR.IR-01 · AIUC-1 D

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High | **Originating layer:** L1 — Foundation Models

Inference attacks — membership inference and model inversion — are
L1 attacks. They exploit properties of the foundation model's weights
that encode information about training data, using the L1 inference
API as the exfiltration channel.

#### MAESTRO layer analysis

**L1 — Foundation Models (primary)**
The model's weights encode statistical information about training data
that can be recovered through systematic querying. This is an inherent
property of current model architectures, not a deployment
misconfiguration. L1 mitigations focus on limiting the information
available for inference attacks (differential privacy, confidence
score suppression).

**L2 — Data Operations (training data source)**
The sensitive data that can be reconstructed through L1 inference
attacks originates in L2 — the training corpus that was used to build
the model. Stronger L2 controls at training time (differential privacy,
data minimisation) reduce the L1 reconstruction attack surface.

**L5 — Evaluation & Observability (detection)**
Systematic inference attack campaigns produce characteristic query
patterns that L5 monitoring can detect — high query volume, systematic
output space coverage, unusual input diversity.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L1 | Differential privacy during training. Confidence score suppression in production outputs. Output rate limiting. |
| L2 | Data minimisation in training corpus — only include data whose potential reconstruction is an acceptable risk. |
| L5 | Monitor for inference attack patterns — systematic query campaigns detected through L5 anomaly detection. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Membership inference confirming sensitive individual in training data | L1 | P2 |
| Model inversion reconstructing training examples | L1 → L2 | P2 |
| Systematic query campaign for model extraction | L1 → L5 | P1 |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM08 Vector and Embedding Weaknesses
- DSGAI 2026: DSGAI10 Synthetic Data Pitfalls
- Other frameworks: ISO 27001 A.8.11 · GDPR Art. 25 · MITRE ATLAS AML.T0024.000

---

### DSGAI19 — Human-in-Loop & Labeler Overexposure

**Severity:** Medium | **Originating layer:** L2 — Data Operations

Human annotation workflows are L2 data operations — they process
sensitive source data to produce training labels. The annotation
pipeline is an L2 data pathway that extends outside the organisation
to third-party labeling vendors.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
Annotation tasks are L2 operations that expose sensitive source data
to the annotation workflow and by extension to labeling vendor
infrastructure. Sensitive records used as annotation examples are
effectively L2 assets shared with a third-party.

**L6 — Security & Compliance (vendor governance)**
Labeling vendors are L6 supply chain participants with direct access
to sensitive L2 data. The same L6 vendor governance that applies to
other third-party AI components applies here.

**L7 — Agent Ecosystem (poisoning risk)**
A compromised or adversary-controlled labeling vendor can introduce
biased or poisoned annotations into the training corpus — an L2
poisoning attack that reaches L1 through the training pipeline.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Data minimisation in annotation tasks — annotators see minimum content required. Anonymise sensitive records before annotation where possible. |
| L6 | Labeling vendors assessed under vendor security programme before engagement. Contractual data handling and zero-training obligations. |
| L7 | Annotation quality monitoring detecting systematic bias indicative of adversary-controlled labeling. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Sensitive training data exposed to inadequately vetted labeling vendor | L2 → L6 | P1 |
| Adversary-controlled labeling vendor injecting biased annotations | L7 → L2 | P2 |
| Labeling vendor retaining sensitive data beyond contract term | L6 | P2 |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.34 · GDPR Art. 28 · NIST CSF 2.0 GV.SC-01

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High | **Originating layer:** L1 — Foundation Models

Model extraction attacks are L1 attacks — they exploit the foundation
model's inference capability to reconstruct a functional replica
through systematic querying. The attack surface is the L1 inference
API, and the extracted asset is the proprietary model capability that
the L1 layer encodes.

#### MAESTRO layer analysis

**L1 — Foundation Models (primary)**
Model extraction is only possible because the foundation model encodes
sufficient information about its decision surface to be partially
reconstructed from its outputs. Rate limiting and output modification
are L1 mitigations that raise the cost of extraction attacks.

**L5 — Evaluation & Observability (detection)**
Model extraction campaigns produce characteristic L5 signals:
high query volume, systematic input diversity designed to map the
output space, and unusual query patterns that do not match normal
usage. L5 monitoring specifically tuned for extraction patterns
can detect campaigns before reconstruction succeeds.

**L6 — Security & Compliance (access control)**
Authentication and rate limiting on the L1 inference API are L6
access controls. Unauthenticated systematic querying is blocked
at L6 before the L1 model is ever reached.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L1 | Rate limiting. Output perturbation (watermarking) to detect extracted model replicas. |
| L5 | Monitor for extraction campaign signatures — unusual query diversity, systematic output space coverage, high volume from single source. |
| L6 | Authentication on all inference API endpoints. Per-user query budgets. Anomalous usage triggers investigation. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Systematic API querying to reconstruct model functionality | L1 → L5 | P2 |
| Unauthenticated inference access enabling high-volume extraction | L1 ← L6 | P1 |
| Extracted model deployed as competing service | L1 | P2 |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference & Data Reconstruction
- Other frameworks: MITRE ATLAS AML.T0016 · ISO 27001 A.5.12 · NIST CSF 2.0 DE.CM-09

---

### DSGAI21 — Disinformation via Data Poisoning

**Severity:** High | **Originating layer:** L2 — Data Operations

RAG corpus disinformation is an L2 integrity failure — false content
enters the data operations layer through the ingestion pipeline and
is indexed as authoritative knowledge. The model at L1 retrieves
and surfaces it without any inherent ability to distinguish it from
legitimate content.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**
The RAG corpus is an L2 asset. Its integrity — the trustworthiness
of its content — determines the trustworthiness of every response
that draws on it. Source trust tiering, content integrity verification,
and ingestion gates are all L2 controls on RAG corpus integrity.

MAESTRO's treatment of data operations as a security-critical layer
is directly applicable here: the RAG corpus is not a cache or a
convenience store, it is a data operations asset whose integrity
must be maintained with the same rigour as any other data system.

**L1 — Foundation Models (manifestation)**
The model retrieves from the poisoned corpus and generates responses
that present adversary-controlled content as authoritative. This is
an L1 consequence of an L2 integrity failure.

**L5 — Evaluation & Observability (detection)**
Corpus poisoning is most detectable through L5 monitoring of content
changes — integrity hashing on indexed content detects unauthorised
modifications before they reach L1 inference.

#### MAESTRO mitigations

| Layer | Mitigation |
|---|---|
| L2 | Source trust tiering. Cryptographic provenance for authoritative sources. Ingestion gates blocking external content during elevated threat periods. |
| L1 | Citations in responses — L1 output includes source provenance, allowing users to verify authoritativeness. |
| L5 | RAG corpus integrity monitoring — hash-based change detection, anomalous content changes trigger alert and engineering review. |

#### Threat model output

| Threat | Layer | Priority |
|---|---|---|
| Adversary publishes false content indexed by RAG system | L2 | P1 |
| Modified authoritative document injected via documentation pipeline | L2 | P1 |
| Poisoned corpus content surfaced as authoritative output | L1 ← L2 | P1 |
| Corpus modification evading L5 monitoring | L5 | P2 |

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0045 · ISO 27001 A.5.7 · ISA/IEC 62443 SR 3.3 (OT)

---

## MAESTRO data security threat model summary

### Threats by originating layer

| Layer | DSGAI entries | Count |
|---|---|---|
| L1 — Foundation Models | DSGAI18, DSGAI20 | 2 |
| L2 — Data Operations | DSGAI01, DSGAI04, DSGAI05, DSGAI07, DSGAI09, DSGAI10, DSGAI11, DSGAI13, DSGAI15, DSGAI19, DSGAI21 | 11 |
| L3 — Agent Frameworks | DSGAI06, DSGAI12 | 2 |
| L4 — Deployment & Infrastructure | DSGAI16, DSGAI17 | 2 |
| L5 — Evaluation & Observability | DSGAI14 | 1 |
| L6 — Security & Compliance | DSGAI02, DSGAI08 | 2 |
| L7 — Agent Ecosystem | DSGAI03 | 1 |

**The L2 Data Operations layer accounts for 52% of DSGAI entries.** This
is the quantitative basis for MAESTRO's designation of data operations
as the highest-priority security layer for GenAI data security
programmes. An organisation that does not treat its RAG corpora,
embedding stores, training pipelines, and memory systems as security-
critical infrastructure is under-defended against the majority of
the DSGAI threat landscape.

### Top propagation paths for DSGAI

**Path 1 — L2 to L1 (highest frequency):**
Data in L2 (poisoned, exfiltrated, or reconstructed) surfaces through
L1 inference — the model presents adversary-controlled or sensitive
content as its own output.
Entries: DSGAI01, DSGAI04, DSGAI15, DSGAI21.

**Path 2 — L6 to L2 (credential → data access):**
L6 credential failures enable unauthorised access to L2 data stores
— compromised credentials provide direct access to embedding stores,
RAG corpora, and training data.
Entries: DSGAI02, DSGAI11, DSGAI13.

**Path 3 — L3 to L2 (tool → data):**
L3 tool integrations create data flows from L2 stores to external
services — context minimisation failures expose L2 content through
tool call payloads.
Entries: DSGAI06, DSGAI12.

**Path 4 — L4 to L7 (infrastructure → ecosystem cascade):**
L4 availability failures propagate through the L7 agent ecosystem,
compounding degraded data quality across multiple downstream agents.
Entries: DSGAI17.

---

## Using this file in a data security programme

**Threat modeling session:** Use the originating layer for each DSGAI
entry to scope threat modeling sessions by system component. Run L2
threat modeling with the data engineering team, L6 with the IAM
team, L3 with the integration engineering team.

**Control selection:** After identifying threats by layer, select
controls from the companion DSGAI files:
- `DSGAI_ISO27001.md` — ISMS controls per entry
- `DSGAI_NISTCSF2.md` — CSF 2.0 functions per entry
- `DSGAI_MITREATLAS.md` — adversarial techniques per entry
- `DSGAI_ISA62443.md` — OT-specific controls per entry

**Prioritisation:** The originating layer plus propagation path
determines priority. L2-origin threats that propagate to L1 and
evade L5 are P1. Layer-contained threats with defined mitigations
are P2.

---

## References

- [MAESTRO Framework — CSA](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
- [MAESTRO GitHub Repository](https://github.com/CloudSecurityAlliance/MAESTRO)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [Agentic Top 10 × MAESTRO](../agentic-top10/Agentic_MAESTRO.md)
- [DSGAI × MITRE ATLAS](DSGAI_MITREATLAS.md)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full MAESTRO layer analysis with propagation paths and data security summary | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.  
Created by Emmanuel Guilherme Junior.  
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
