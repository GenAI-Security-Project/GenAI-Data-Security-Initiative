<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01-LLM10)
  Framework   : MAESTRO — Multi-Agent Environment, Security, Threat, Risk, and Outcome
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × MAESTRO

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to [MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
(Multi-Agent Environment, Security, Threat, Risk, and Outcome) —
the Cloud Security Alliance's threat modeling framework designed
for the unique challenges of AI systems.

**Created by:** Ken Huang, CEO & Chief AI Officer, DistributedApps.ai;
Co-Chair of AI Safety Working Groups, Cloud Security Alliance.

**Official repository:** https://github.com/CloudSecurityAlliance/MAESTRO

---

## Why MAESTRO for LLM threat modeling

MAESTRO maps each vulnerability to the **architectural layer where
it originates** — an answer that no compliance or control framework
provides. For LLM deployments this matters because the same
vulnerability can manifest at multiple layers: prompt injection
originates at L1 (the foundation model interprets instructions)
but arrives via L2 (a poisoned RAG document) and is executed
through L3 (the agent framework dispatches a tool call).

Knowing the originating layer answers three practical questions:

- **Which team owns this risk?** L2 data operations risks belong
  to data engineering; L4 infrastructure risks belong to DevOps;
  L6 identity risks belong to IAM teams.
- **Where must the countermeasure be deployed?** Mitigations applied
  at the wrong layer are bypassed. An L1 prompt injection guard
  does not stop an L2 RAG poisoning attack reaching the model
  through a different ingestion path.
- **How does this threat propagate?** A L2 training data poisoning
  attack (LLM04) corrupts L1 model behaviour, creates L5
  monitoring blind spots when the poisoned model produces outputs
  consistent with its poisoned training, and ultimately surfaces
  at L7 if the compromised model participates in multi-agent
  interactions.

Use this file before selecting controls from any other framework
in this repo — threat enumeration by MAESTRO layer should precede
control selection.

---

## MAESTRO seven-layer architecture

| Layer | ID | Description | Threat theme |
|---|---|---|---|
| Foundation Models | L1 | Base LLMs providing core reasoning and generation | Model manipulation, extraction, instruction misalignment |
| Data Operations | L2 | Ingestion pipelines, storage, RAG, embeddings, vector stores | Data poisoning, PII exfiltration, retrieval compromise |
| Agent Frameworks | L3 | Orchestration platforms, tool registries, MCP, plugin ecosystems | Tool misuse, orchestration injection, supply chain |
| Deployment & Infrastructure | L4 | Servers, containers, networks, CI/CD, runtime environments | Infrastructure compromise, code execution, resource exhaustion |
| Evaluation & Observability | L5 | Monitoring, logging, telemetry, behavioural baselines | Blind spots, output quality failure detection, evasion |
| Security & Compliance | L6 | Identity, access control, audit, governance, credential management | Privilege abuse, credential exposure, policy failure |
| Agent Ecosystem | L7 | Multi-agent interaction, A2A communication, cascade dynamics | Lateral movement, cascading failures, trust exploitation |

---

## How MAESTRO fits in the LLM security programme

```
LLM_MAESTRO.md (threat enumeration by architectural layer)
    ↓
LLM_AITG.md (test cases per threat)
    ↓
LLM_STRIDE.md (threat categorisation for DFD threat modeling)
    ↓
LLM_CWE_CVE.md (root cause taxonomy + confirmed CVE evidence)
    ↓
ISO 27001 / CIS Controls / ASVS (control selection)
    ↓
LLM_ISO42001.md (governance and AI management system)
```

Use this file first. The layer-origin analysis provides the
architectural context that makes every downstream control selection
defensible — you know *why* a control is placed at a specific
system component, not just *what* the control does.

---

## Layer-to-LLM entry mapping

| MAESTRO Layer | Primary LLM entries | Secondary LLM entries |
|---|---|---|
| L1 Foundation Models | LLM01 Prompt Injection, LLM07 System Prompt Leakage, LLM09 Misinformation | LLM02, LLM05 |
| L2 Data Operations | LLM02 Sensitive Info Disclosure, LLM04 Data & Model Poisoning, LLM08 Vector Weaknesses | LLM01, LLM03 |
| L3 Agent Frameworks | LLM05 Insecure Output Handling, LLM06 Excessive Agency | LLM01, LLM03 |
| L4 Deployment & Infrastructure | LLM10 Unbounded Consumption, LLM03 Supply Chain | LLM05, LLM06 |
| L5 Evaluation & Observability | LLM09 Misinformation (detection gap) | LLM04, LLM10 |
| L6 Security & Compliance | LLM06 Excessive Agency (permission scope) | LLM02, LLM07 |
| L7 Agent Ecosystem | — | LLM06, LLM10 |

---

## Quick-reference summary

| ID | Name | Severity | Originating Layer | Primary MAESTRO Layers | Tier |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | L1 | L1, L2, L3 | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | L2 | L2, L1, L5 | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | L3/L4 | L3, L4, L2 | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | Critical | L2 | L2, L1, L5 | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | L3 | L3, L4, L1 | Foundational–Hardening |
| LLM06 | Excessive Agency | High | L6 | L6, L3, L7 | Foundational–Advanced |
| LLM07 | System Prompt Leakage | High | L1 | L1, L6 | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | L2 | L2, L4, L6 | Hardening–Advanced |
| LLM09 | Misinformation | Medium | L1 | L1, L2, L5 | Foundational–Hardening |
| LLM10 | Unbounded Consumption | Medium | L4 | L4, L3, L5 | Foundational–Hardening |

---

## Audience tags

- **Security architect** — layer-to-LLM mapping for system design threat modeling
- **Red team / threat modeler** — layer-by-layer threat enumeration before control selection
- **ML / AI engineer** — L1 and L2 entries for model and data pipeline risk ownership
- **DevSecOps engineer** — L4/L5 entries for infrastructure and observability integration
- **AppSec engineer** — L3 output handling and L6 permission scope entries
- **CISO** — propagation path analysis for LLM risk programme scoping

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical
**Originating layer:** L1 — Foundation Models
**Propagation path:** L1 (instruction accepted) ← L2 (indirect vector) ← L3 (execution channel)

Prompt injection originates at L1 because the foundation model is
the component that accepts attacker-controlled instructions as
legitimate directives. The model's inability to structurally
distinguish instructions from data is an inherent L1 property.
The injection vector may arrive through L2 (poisoned RAG content)
or directly at L1 (user prompt), but acceptance always happens
at the model layer.

#### MAESTRO layer analysis

**L1 — Foundation Models (originating)**

The model processes attacker-controlled content — whether in the
user prompt or in retrieved context — and deviates from the
authorised task. This is an L1 property: the model treats
adversarially crafted content as instructions because there is
no cryptographic or structural separator between trusted
instructions and untrusted data in the transformer context window.

Mitigations at L1:
- Structural prompt architecture separating trusted system
  instructions from untrusted user and retrieved content
- Constitutional AI hard constraints preventing goal-overriding
  instructions regardless of source
- Goal-consistency verification: compare the model's inferred
  goal at each step against the session's authorised intent

**L2 — Data Operations (indirect injection vector)**

The most prevalent indirect injection channels — RAG-retrieved
documents, uploaded files, processed web content — enter the
context window through the data pipeline. An attacker who can
write to the RAG corpus delivers injection instructions that the
model receives as retrieved knowledge rather than user input,
bypassing user-facing input controls entirely.

Mitigations at L2:
- Content integrity scanning on RAG ingestion — injection
  pattern detection before content enters the index
- Source provenance tagging — each retrieved passage carries
  its trust level into the context window
- Read-only data flow from corpus to context — no pathway
  that reads from the corpus can also write to it

**L3 — Agent Frameworks (execution channel)**

When injection succeeds at L1, the redirected goal is executed
through the L3 framework's tool dispatch and action sequencing.
A framework without goal-state verification executes the hijacked
goal as if it were legitimate.

Mitigations at L3:
- Framework-level goal-state verification middleware between
  model output and tool dispatch
- Action allowlisting — the framework enforces permitted
  actions regardless of model instruction
- Irreversibility gates requiring human confirmation for
  destructive or out-of-scope actions

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other files: LLM_STRIDE.md (Spoofing/Tampering), LLM_AITG.md (TC-LLM01), LLM_CWE_CVE.md (CWE-77/20)

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High
**Originating layer:** L2 — Data Operations
**Propagation path:** L2 (data in scope) → L1 (model reproduces) → L5 (monitoring gap)

Sensitive data enters GenAI scope at L2 — in training corpora,
RAG stores, embeddings, and system prompt configuration. L1
reproduces this data in outputs when queries create sufficient
retrieval pressure or when training memorisation is triggered.
L5 monitoring failures allow disclosure to proceed undetected.

#### MAESTRO layer analysis

**L2 — Data Operations (originating)**

The root cause is that sensitive data was present in the data
assets the model has access to — training corpora, vector stores,
RAG documents, prompt caches. Data governance failures at L2
(insufficient classification, over-broad retrieval scope,
missing PII scrubbing) create the conditions for disclosure.

Mitigations at L2:
- Data classification policy for all GenAI data assets —
  PII, credentials, and sensitive data identified before
  entering training or retrieval pipelines
- Retrieval scope enforcement — RAG queries bounded to
  the authenticated user's document permission level
- PII scrubbing on training corpora before model ingestion

**L1 — Foundation Models (reproduction layer)**

The model surface-reproduces training data under retrieval
pressure or memorisation probing. Differential privacy in
training reduces memorisation probability; output scanning
catches reproduction events at generation time.

Mitigations at L1:
- Differential privacy in training for sensitive corpora —
  formal guarantee that individual training records are
  not memorised
- Output token scanning for sensitive data patterns before
  delivery to consumer

**L5 — Evaluation & Observability (detection layer)**

Without AI-specific DLP on output channels, disclosure events
are not detected until after the fact — if ever. L5 monitoring
must cover LLM-specific disclosure patterns, not just
traditional file transfer events.

Mitigations at L5:
- DLP on all LLM output channels — PII, credential, and
  sensitive pattern detection before delivery
- Output anomaly monitoring — unusual data density or
  unexpected content classification in model responses

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI18 Inference & Data Reconstruction
- Other files: LLM_STRIDE.md (Information Disclosure), LLM_CWE_CVE.md (CWE-200/359)

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High
**Originating layer:** L3/L4 — Agent Frameworks / Deployment & Infrastructure
**Propagation path:** L3 (plugins/tools) ← L4 (model weights/infra) ← L2 (datasets)

LLM supply chain threats originate at multiple layers: L3 for
plugin and tool supply chain components, L4 for model weight
and runtime library integrity, and L2 for training and
fine-tuning dataset provenance. Compromise at any layer can
cascade to L1 (backdoored model behaviour) or L5 (undetected
through compromised monitoring).

#### MAESTRO layer analysis

**L3 — Agent Frameworks (plugin and tool supply chain)**

Third-party plugins, tool integrations, and MCP server
implementations are L3 supply chain components. A compromised
plugin descriptor or malicious tool implementation executes
with the agent's full permission scope — the framework has
no inherent mechanism to verify that a tool does what its
descriptor claims.

Mitigations at L3:
- Plugin and tool SBOM — every integration component
  inventoried with version, source, and integrity hash
- Descriptor integrity verification before tool loading —
  cryptographic signatures on tool descriptors
- Vendor security assessment before any third-party
  component enters production

**L4 — Deployment & Infrastructure (model weight and runtime)**

Model weights downloaded from third-party sources and ML
library dependencies are L4 supply chain assets. Tampered
model weights or vulnerable runtime libraries compromise the
entire stack above them — all L1 through L7 security properties
depend on L4 integrity.

Mitigations at L4:
- Model weight cryptographic verification before deployment —
  hash comparison against vendor-published baseline
- Dependency vulnerability scanning in CI/CD pipeline —
  ML libraries and inference runtime CVE monitoring
- Immutable model registry — deployed model versions pinned,
  verified, and never overwritten in place

**L2 — Data Operations (dataset supply chain)**

Training and fine-tuning datasets sourced from third parties
are L2 supply chain components. An adversary who controls a
public dataset used for fine-tuning can introduce backdoors or
biases that survive into the deployed model (see also LLM04).

Mitigations at L2:
- Dataset provenance documentation for all training corpora —
  source, version, integrity hash, and quality review recorded
- Statistical quality gates on ingested datasets — outlier
  detection before training begins

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange
- Other files: LLM_STRIDE.md (Tampering/Repudiation), LLM_CWE_CVE.md (CWE-494/829)

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical
**Originating layer:** L2 — Data Operations
**Propagation path:** L2 (poisoned data) → L1 (corrupted behaviour) → L5 (monitoring blind spot)

Poisoning originates at L2 when adversarially crafted training
data, fine-tuning corpora, or RAG content enters the pipeline.
The corrupted behaviour manifests at L1 when the model is
deployed, and L5 monitoring systems may fail to detect it
because the model produces outputs consistent with its poisoned
training — the anomaly looks like correct behaviour.

#### MAESTRO layer analysis

**L2 — Data Operations (originating)**

The attacker's leverage point is write access to data that
shapes the model — training corpora, fine-tuning datasets,
RAG indexes, or memory stores. Poisoned data at L2 is
invisible to most runtime security controls because the
corruption happens before deployment.

Mitigations at L2:
- Data provenance tracking — every training sample traceable
  to verified source with integrity hash
- Statistical anomaly detection on ingested datasets —
  label inconsistency, outlier distributions, unexpected
  content patterns detected before model training
- Immutable training data — once verified, training corpora
  write-protected to prevent post-verification modification

**L1 — Foundation Models (manifesting layer)**

Poisoned behaviour surfaces at L1 when the deployed model
responds to trigger inputs or produces systematically biased
outputs. Behavioural testing at L1 must specifically probe
for known backdoor trigger patterns before production release.

Mitigations at L1:
- Pre-deployment adversarial testing — probing with trigger
  patterns across all use case configurations
- Behavioural baseline establishment — document expected
  model response distributions to enable drift detection
- Model weight integrity verification — verify deployed
  weights match the training pipeline output

**L5 — Evaluation & Observability (detection challenge)**

Poisoned models produce outputs that appear correct under
normal operating conditions — the anomaly only manifests
with trigger inputs. Standard output quality monitoring
will not detect this. L5 monitoring must include adversarial
probing, not just passive quality metrics.

Mitigations at L5:
- Scheduled adversarial probing of deployed models —
  trigger pattern testing integrated into continuous monitoring
- Output distribution drift detection — statistical
  anomalies in response distributions trigger investigation

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other files: LLM_STRIDE.md (Tampering), LLM_CWE_CVE.md (CWE-20/345)

---

### LLM05 — Insecure Output Handling

**Severity:** High
**Originating layer:** L3 — Agent Frameworks
**Propagation path:** L3 (output passed without sanitisation) → L4 (downstream system executes) ← L1 (model generates dangerous content)

Insecure output handling originates at L3 when the orchestration
framework passes LLM-generated content to downstream systems —
HTML renderers, SQL engines, shell interpreters, HTTP clients —
without sanitisation. The L1 model generated the dangerous
content; the L3 framework failed to validate it before passing
it to an L4 system that executes it with real-world consequences.

#### MAESTRO layer analysis

**L3 — Agent Frameworks (originating)**

The framework is responsible for the interface between model
output and downstream consumers. Treating LLM output as trusted
content — passing it directly to HTML templates, SQL queries,
or shell commands — is the architectural failure. The framework
must validate and sanitise every output before it crosses
a trust boundary.

Mitigations at L3:
- Output validation layer between model and downstream system —
  content type, schema, and injection pattern validation
  before any LLM output is consumed by another component
- Contextual output encoding — HTML encoding for web
  rendering, parameterised queries for database operations,
  sandbox execution for generated code
- Output allowlisting — LLM output permitted only in
  defined, validated forms for each downstream consumer

**L4 — Deployment & Infrastructure (execution layer)**

The downstream system that executes unsafe LLM output is
an L4 component — a web server rendering HTML, a database
engine executing SQL, a container running generated scripts.
L4 defences provide defence-in-depth when L3 validation fails.

Mitigations at L4:
- WAF rules covering LLM output injection patterns
  at the network layer
- Database least-privilege — LLM-connected accounts
  cannot execute DDL; parameterised queries enforced
  at the database layer regardless of calling code
- Container sandboxing for any LLM-generated code execution —
  no host filesystem or network access from execution sandbox

**L1 — Foundation Models (generation layer)**

While the root cause is L3 handling, L1 system prompt
configuration can reduce the probability of dangerous output
generation. Instructing the model to never generate raw HTML,
SQL, or shell commands reduces the attack surface at the source.

Mitigations at L1:
- System prompt restrictions — model instructed to produce
  only plain text or structured JSON, never raw HTML or SQL
- Output format constraints — structured output with schema
  validation reduces injection surface

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse & Exploitation
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other files: LLM_STRIDE.md (Tampering/Elevation), LLM_CWE_CVE.md (CWE-79/89/78)

---

### LLM06 — Excessive Agency

**Severity:** High
**Originating layer:** L6 — Security & Compliance
**Propagation path:** L6 (over-broad permission granted) → L3 (framework executes unrestricted) → L7 (action visible to other agents)

Excessive agency originates at L6 when the permission model
grants the LLM capabilities beyond what its defined role
requires. The framework (L3) executes whatever the model
requests within its permission scope — and if that scope is
over-broad, legitimate model behaviour can cause unintended
harm. In multi-agent systems (L7), an over-permissioned agent
becomes a capability available to every other agent that can
communicate with it.

#### MAESTRO layer analysis

**L6 — Security & Compliance (originating)**

The root cause is permission design: granting an LLM agent
capabilities it does not need for its defined task creates
an attack surface that would not exist with a minimal
permission model. Every capability granted at L6 is a
potential impact vector if the model is injected or
misbehaves.

Mitigations at L6:
- Minimal permission principle — document required
  capabilities per use case, grant only those capabilities,
  review at each deployment
- Short-lived, scoped credentials — agent credentials
  expire at session end, scope limited to current task
- Irreversibility categorisation — list all irreversible
  actions and require human confirmation before execution

**L3 — Agent Frameworks (execution layer)**

The framework dispatches tool calls without evaluating
whether the requested capability is appropriate for the
current task context. A framework with no task-scope
verification executes any permitted capability in any context.

Mitigations at L3:
- Task-scope enforcement at the framework level —
  capabilities available to the model vary by task context,
  not just by static role
- Irreversibility gate middleware — confirmation required
  before framework dispatches irreversible tool calls
- Tool call rate limiting at the framework layer —
  prevents capability abuse through high-volume automation

**L7 — Agent Ecosystem (amplification layer)**

In multi-agent deployments, an over-permissioned agent exposes
its capabilities to any agent that can communicate with it.
Lateral movement through the agent ecosystem is possible when
individual agents have more capability than their roles require.

Mitigations at L7:
- Per-agent capability inventory in multi-agent design —
  each agent's permissions documented and minimised
  independently of other agents in the ecosystem
- Inter-agent request validation — agents validate that
  requests from other agents are within both the
  requesting agent's and the responding agent's scope

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse & Exploitation, ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other files: LLM_STRIDE.md (Elevation of Privilege), LLM_CWE_CVE.md (CWE-250/266)

---

### LLM07 — System Prompt Leakage

**Severity:** High
**Originating layer:** L1 — Foundation Models
**Propagation path:** L1 (model reproduces confidential context) ← L6 (confidential content placed in prompt)

System prompt leakage originates at L1 — the model reproduces
confidential instructions, credentials, or business logic from
its context window in response to adversarial extraction prompts.
The contributing cause is at L6: confidential information that
should not be in the system prompt has been placed there,
creating a leakage target.

#### MAESTRO layer analysis

**L1 — Foundation Models (originating)**

Current LLMs do not structurally prevent reproduction of system
prompt content when adversarial prompts create sufficient
extraction pressure. The model was trained to be helpful and
to reproduce context content when asked — adversarial extraction
exploits this property. Instruction-following fine-tuning that
teaches the model to decline system prompt reproduction is the
primary L1 mitigation.

Mitigations at L1:
- System prompt non-disclosure instruction — explicit
  instruction that system prompt contents are confidential
  and must not be reproduced
- Refusal consistency testing — verify model refuses
  system prompt extraction across varied request phrasings,
  translation tasks, and role-play scenarios
- Minimise confidential content in system prompt —
  business logic and credentials not placed in context
  window (move to secure external storage)

**L6 — Security & Compliance (contributing layer)**

The severity of system prompt leakage scales with the
sensitivity of what is in the system prompt. Credentials,
API keys, and proprietary business logic in the system
prompt create high-severity leakage targets. These assets
belong in secure external storage, not in the context window.

Mitigations at L6:
- Credentials management — all credentials accessed via
  secrets manager at runtime, never embedded in system prompt
- System prompt classification — treat system prompt
  content as a confidential asset; access controls on
  who can read and modify it
- System prompt rotation — rotate system prompts on a
  schedule to limit the impact of leakage

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other files: LLM_STRIDE.md (Information Disclosure/Repudiation), LLM_CWE_CVE.md (CWE-200/922)

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium
**Originating layer:** L2 — Data Operations
**Propagation path:** L2 (insecure vector store) → L4 (infrastructure exposure) → L6 (access control gap)

Vector databases storing embeddings are L2 data assets with
distinct security properties from traditional databases.
Embedding inversion attacks can reconstruct training data from
vectors; retrieval authorisation failures expose documents
across permission boundaries; vector store infrastructure
misconfiguration (L4) enables unauthenticated access; and
missing access controls (L6) allow cross-tenant retrieval.

#### MAESTRO layer analysis

**L2 — Data Operations (originating)**

Embeddings are dense representations of the training and
document corpus — they encode semantic information that can
be recovered through inversion attacks. The vector store is
a high-value L2 data asset that requires the same security
treatment as the primary data store, not the relaxed treatment
typically applied to search indexes.

Mitigations at L2:
- Embedding classification — vector stores classified as
  sensitive data assets with appropriate handling requirements
- Retrieval scope enforcement — RAG queries bounded to
  the authenticated user's document permission level;
  namespace isolation between tenants
- Embedding provenance — each embedding traceable to its
  source document with classification label

**L4 — Deployment & Infrastructure (infrastructure layer)**

Vector database authentication, network exposure, and access
logging are L4 concerns. Many default vector database
deployments are unauthenticated and network-accessible —
an L4 configuration gap that bypasses all L2 data governance.

Mitigations at L4:
- Authentication and encryption required for all vector
  store API endpoints — no unauthenticated access
- Network segmentation — vector store not exposed beyond
  the application tier; no direct external access
- Access logging — all vector store operations logged
  with caller identity and query content

**L6 — Security & Compliance (access control layer)**

Cross-tenant and cross-classification retrieval failures
are L6 access control issues — the permission model does
not correctly enforce document-level authorisation on
semantic similarity retrieval.

Mitigations at L6:
- Document-level authorisation on retrieval — permission
  check per document before including in retrieval results
- Tenant namespace isolation enforced at the access
  control layer, not just the application layer

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other files: LLM_STRIDE.md (Information Disclosure), LLM_CWE_CVE.md (CWE-285/306)

---

### LLM09 — Misinformation

**Severity:** Medium
**Originating layer:** L1 — Foundation Models
**Propagation path:** L1 (model generates false content) ← L2 (training data quality) → L5 (no detection)

Misinformation originates at L1 — the model generates plausible
but false content as a fundamental property of generative
architectures. L2 training data quality affects the frequency
and domain of hallucination; L5 monitoring must detect
misinformation events rather than allowing them to reach
downstream consumers unvalidated.

#### MAESTRO layer analysis

**L1 — Foundation Models (originating)**

Current LLMs generate fluent, confident-sounding text even
when producing factually incorrect content. This is an inherent
L1 property: the model optimises for plausible token sequences,
not for factual accuracy. Retrieval augmentation (L2) reduces
hallucination rate but does not eliminate it; output confidence
scores do not reliably predict factual accuracy.

Mitigations at L1:
- System prompt grounding — instruct model to acknowledge
  uncertainty rather than fabricate confident responses
- Output citation requirements — high-stakes use cases
  require model to cite sources that can be verified
- Hallucination-resistant prompting patterns —
  chain-of-thought, step-by-step verification, and
  explicit uncertainty expression instructions

**L2 — Data Operations (training quality)**

Training data quality shapes the model's domain knowledge.
Low-quality, biased, or outdated training corpora produce
models with higher hallucination rates in the affected
domains. RAG retrieval (also L2) can partially compensate
by grounding responses in verified document content.

Mitigations at L2:
- Training data quality gates — factual accuracy assessment,
  recency review, and source credibility scoring before
  training data ingestion
- RAG grounding — high-stakes use cases retrieve from
  verified, curated document corpora rather than relying
  on model parametric knowledge

**L5 — Evaluation & Observability (detection layer)**

Without output factual accuracy monitoring, misinformation
reaches end users undetected. L5 misinformation detection
requires domain-specific ground truth benchmarks and
continuous output evaluation, not just generic quality metrics.

Mitigations at L5:
- Factual accuracy benchmarking — domain-specific
  question sets with verified answers run against the
  deployed model on a scheduled basis
- Citation verification pipeline — automated checking
  that model-generated citations are real and accurate

#### Cross-references
- DSGAI 2026: DSGAI21 Disinformation via Data Poisoning
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- Other files: LLM_STRIDE.md (Repudiation/Tampering), LLM_AITG.md (TC-LLM09)

---

### LLM10 — Unbounded Consumption

**Severity:** Medium
**Originating layer:** L4 — Deployment & Infrastructure
**Propagation path:** L4 (no resource controls) ← L3 (no framework-level limits) → L5 (no consumption monitoring)

Unbounded consumption originates at L4 when the infrastructure
layer lacks resource quotas, rate limiting, and compute
throttling. The framework (L3) dispatches compute-intensive
operations without budget constraints; L5 monitoring fails to
detect runaway consumption before it causes service degradation
or financial harm.

#### MAESTRO layer analysis

**L4 — Deployment & Infrastructure (originating)**

Rate limiting, compute quotas, and cost caps are L4
infrastructure concerns — enforced at the API gateway,
load balancer, and cloud billing layer. An LLM deployment
without L4 resource controls is vulnerable to both
accidental and deliberate resource exhaustion regardless
of application-layer controls.

Mitigations at L4:
- Per-identity rate limits enforced at API gateway —
  request rate, token budget, and concurrent connection
  limits per user and per API key
- Hard cost caps at cloud billing layer —
  maximum daily spend threshold triggers immediate
  service suspension
- Compute timeout enforcement — long-running inference
  requests terminated at the infrastructure layer

**L3 — Agent Frameworks (contributing layer)**

Agentic frameworks that recursively spawn sub-agents,
loop without convergence criteria, or dispatch unlimited
parallel tool calls create consumption amplification at L3.
Framework-level resource governance prevents run-away
agent behaviour from exhausting L4 capacity.

Mitigations at L3:
- Maximum iteration and recursion depth limits in
  agent orchestration configuration
- Parallel tool call limits — maximum concurrent tool
  invocations per session enforced by the framework
- Budget-aware planning — agent is given an explicit
  token and compute budget per task

**L5 — Evaluation & Observability (detection layer)**

Consumption attacks that proceed below alarm thresholds
go undetected without L5 monitoring. Gradual token
flooding and wallet drainage attacks require trending
analysis over time, not just instantaneous rate checks.

Mitigations at L5:
- Per-user consumption trending — alert on deviation
  from historical baseline, not just absolute limits
- Financial monitoring — spend rate alerts at multiple
  thresholds before hard cap is reached
- Anomalous pattern detection — high-volume systematic
  queries that match model extraction or flooding signatures

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other files: LLM_STRIDE.md (Denial of Service), LLM_CWE_CVE.md (CWE-770/400)

---

## MAESTRO threat modeling session guide for LLM

### Session structure

Use this file to run a structured 90-minute threat modeling
session for a new or changed LLM deployment:

**Minutes 0–15: Layer inventory**
For each MAESTRO layer, list every component in your deployment:
- L1: Which model? Version? Provider?
- L2: Which data stores? Training data sources? RAG corpus? Embeddings?
- L3: Which framework? Which tools/plugins? MCP servers?
- L4: Where deployed? Network exposure? Resource limits configured?
- L5: What monitoring? DLP? Output quality checks?
- L6: What credentials? Which permissions? Who has system prompt access?
- L7: Any other AI systems this model communicates with?

**Minutes 15–45: Layer-to-LLM threat mapping**
Using the layer-to-LLM mapping table above, work through each
relevant LLM entry for your layer inventory. For each threat:
- Which of your layer components is the originating surface?
- What is the propagation path in your specific architecture?
- Is the mitigation deployed at the correct layer?

**Minutes 45–75: Control gap analysis**
For each identified threat, check whether the stated mitigation
exists in your deployment. Gaps become remediation work items.

**Minutes 75–90: Prioritisation**
Rank gaps by: originating layer (L4/L6 gaps are often fastest
to fix) × severity × exploitability in your deployment context.

---

## Implementation priority

| Priority | LLM IDs | MAESTRO focus layer | Rationale |
|---|---|---|---|
| P1 — Critical | LLM01, LLM04 | L1/L2 | Prompt injection and poisoning — fundamental model and data layer risks |
| P2 — High | LLM02, LLM05, LLM06 | L2/L3/L6 | Data disclosure, output handling, permission scope |
| P3 — High | LLM03, LLM07 | L3/L4/L1 | Supply chain integrity, system prompt protection |
| P4 — Medium | LLM08, LLM09, LLM10 | L2/L1/L4/L5 | Vector store, misinformation, consumption controls |

---

## References

- [MAESTRO Framework — Cloud Security Alliance](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
- [MAESTRO GitHub Repository](https://github.com/CloudSecurityAlliance/MAESTRO)
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
- [OWASP GenAI Security Multi-Agentic System Threat Modeling Guide v1.0](https://genai.owasp.org)
- [Agentic_MAESTRO.md](../agentic-top10/Agentic_MAESTRO.md) — MAESTRO × Agentic Top 10
- [DSGAI_MAESTRO.md](../dsgai-2026/DSGAI_MAESTRO.md) — MAESTRO × DSGAI 2026

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-27 | Initial release — full LLM01–LLM10 mapping to MAESTRO seven-layer architecture |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the OWASP GenAI Data Security Initiative.
Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
