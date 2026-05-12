<!--
  GenAI Security Crosswalk
  Source list : OWASP GenAI Data Security Risks & Mitigations 2026 (DSGAI01–DSGAI21)
  Framework   : NIST AI Risk Management Framework (AI RMF 1.0)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × NIST AI RMF

Mapping the [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to the [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
and its companion [NIST AI RMF Playbook](https://airc.nist.gov/Docs/2).

The NIST AI RMF is the primary governance and risk management framework
for trustworthy AI in the United States, widely adopted globally across
enterprise, government, and critical infrastructure. Its four core
functions — GOVERN, MAP, MEASURE, MANAGE — provide a lifecycle approach
to AI risk that maps naturally to the DSGAI 2026 data security taxonomy,
which follows data as it moves through a GenAI system from ingestion
through inference to output and operational exhaust.

This mapping is particularly valuable for US federal agencies (required
to align with the AI RMF under Executive Order 14110), critical
infrastructure operators, and enterprises running AI RMF-aligned AI
governance programmes who need to operationalise the DSGAI risks within
their existing framework.

---

## AI RMF core functions — GenAI data security lens

| Function | GenAI data security role |
|---|---|
| GOVERN (GV) | Policies, accountability, and culture for GenAI data security — data governance, acceptable use, privacy, supplier controls |
| MAP (MP) | Identifying and categorising GenAI data risks in context — asset inventory, data flow mapping, risk register |
| MEASURE (MS) | Analysing and testing GenAI data risks — DLP effectiveness, adversarial testing, privacy assessments, data quality |
| MANAGE (MG) | Treating GenAI data risks — incident response, remediation, residual risk monitoring, unlearning capability |

---

## Quick-reference summary

| ID | Name | Severity | Primary AI RMF Subcategories | Tier | Scope |
|---|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | GV-1.6, MP-2.3, MS-2.6, MG-2.4 | Foundational–Advanced | Both |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | GV-1.6, MP-2.3, MS-2.5, MG-2.2 | Foundational–Advanced | Both |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | GV-1.7, MP-3.5, MS-2.6, MG-2.4 | Foundational–Hardening | Both |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | MP-2.3, MS-2.5, MS-3.3, MG-2.2 | Hardening–Advanced | Both |
| DSGAI05 | Data Integrity & Validation Failures | High | MS-2.5, MS-3.3, MG-2.2, MP-2.3 | Foundational–Hardening | Build |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | GV-1.6, MP-5.1, MS-2.5, MG-3.2 | Foundational–Hardening | Both |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | GV-1.6, MP-1.6, MS-3.3, MG-3.2 | Foundational–Advanced | Both |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | GV-1.6, GV-4.2, MS-2.6, MG-2.4 | Foundational–Advanced | Both |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | GV-1.6, MP-2.3, MS-2.6, MG-2.4 | Hardening–Advanced | Both |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | GV-1.6, MS-2.6, MS-3.3, MG-3.2 | Hardening–Advanced | Build |
| DSGAI11 | Cross-Context Conversation Bleed | High | MP-2.3, MS-2.5, MS-2.6, MG-2.2 | Foundational–Hardening | Build |
| DSGAI12 | Unsafe NL Data Gateways | Critical | MP-2.3, MS-2.5, MG-2.2, GV-1.7 | Foundational–Advanced | Build |
| DSGAI13 | Vector Store Platform Security | High | MP-2.3, MS-2.5, MS-3.3, MG-2.2 | Foundational–Hardening | Both |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | GV-1.6, MP-2.3, MS-2.6, MG-2.4 | Foundational–Hardening | Build |
| DSGAI15 | Over-Broad Context Windows | High | MP-2.3, MS-2.5, MS-2.6, MG-2.2 | Foundational–Hardening | Build |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | GV-1.7, MP-3.5, MS-2.5, MG-2.2 | Foundational–Hardening | Both |
| DSGAI17 | Data Availability & Resilience Failures | High | MP-4.1, MS-2.5, MG-2.2, MG-3.2 | Foundational–Advanced | Both |
| DSGAI18 | Inference & Data Reconstruction | High | GV-1.6, MP-2.3, MS-2.5, MG-2.4 | Hardening–Advanced | Both |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | GV-1.6, MP-5.1, MS-2.6, MG-3.2 | Foundational–Hardening | Both |
| DSGAI20 | Model Exfiltration & IP Replication | High | MP-2.3, MS-2.5, MS-2.6, MG-2.2 | Hardening–Advanced | Both |
| DSGAI21 | Disinformation via Data Poisoning | High | GV-1.7, MS-2.5, MS-3.3, MG-2.2 | Hardening–Advanced | Both |

---

## Audience tags

- **CISO / governance** — full file, AI RMF alignment for GenAI data security programme
- **Risk manager** — MAP and MEASURE subcategories, risk register entries
- **Compliance officer** — GV subcategories, regulatory intersection notes
- **ML / AI engineer** — MEASURE subcategories, testing and data quality entries
- **Security engineer** — MANAGE subcategories, incident response entries
- **Federal agency teams** — full file, EO 14110 alignment
- **OT engineer** — DSGAI04, DSGAI12, DSGAI17 with ISA 62443 and NIST SP 800-82 crosswalks

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

Sensitive data — PII, credentials, financial records, proprietary code —
leaks from GenAI systems through model outputs, RAG retrieval, embedding
exposure, or observability pipelines. The AI RMF addresses this as a
core data governance, measurement, and incident response requirement
across all four functions.

**Real-world references:**
- Samsung source code leak (2023)
- Multiple healthcare RAG deployments surfacing PHI via over-permissive
  vector store retrieval (2024)

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Organisational policy on data classification, handling, and disclosure controls for GenAI data assets |
| Risk categorisation | MP-2.3 | MAP | Sensitive data leakage categorised and rated in AI system risk register — specific to each deployment |
| Testing — data leakage | MS-2.6 | MEASURE | Evaluation programme includes data leakage testing — training data, RAG over-retrieval, output redaction |
| Risk response — data | MG-2.4 | MANAGE | Defined incident response for sensitive data disclosure — notification, containment, regulatory reporting |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish and document data classification policy
  covering all GenAI data assets — training corpora, RAG sources,
  prompt templates, outputs, embeddings — before ingestion
- MP-2.3: Include sensitive data leakage in AI risk register
  per deployment — map to specific data assets and retrieval
  sources at risk, assign ownership and treatment timelines
- Deploy output scanning for PII and sensitive patterns as a
  baseline control — enforce as policy requirement

**Hardening**
- MS-2.6: Include data leakage scenarios in evaluation programme —
  test training data memorisation, RAG over-retrieval, and
  output redaction effectiveness before each production release
- MG-2.4: Define and test incident response for data disclosure —
  who is notified, what is contained, regulatory reporting
  obligations and timelines
- GV-1.6: Extend classification policy to derived assets —
  embeddings, summaries, and cached retrievals inherit the
  classification of their source documents

**Advanced**
- MS-2.6: Conduct model inversion and membership inference red
  team exercises — validate sensitive training data cannot be
  reconstructed from outputs
- MG-2.4: Implement machine unlearning readiness — versioned
  data-to-model linkage enabling targeted retraining on data
  subject erasure requests
- GV-1.6: Include derived asset governance in board-level AI
  risk reporting — embeddings and caches as data assets, not
  just infrastructure

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |
| Private AI | Commercial | https://private-ai.com |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.11/A.8.12 · ISO 27701 · EU AI Act Art. 10 · GDPR Art. 25

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical

AI agents inherit, cache, or misuse credentials — API keys, session
tokens, OAuth grants, SSH keys — exposing them through memory stores,
logs, or tool payloads. The AI RMF addresses this through identity
governance policy, adversarial testing, and managed incident response.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Agent identity and credential governance policy — NHI inventory, lifecycle, and access controls |
| Risk categorisation | MP-2.3 | MAP | Agent credential exposure risks mapped to specific agent deployments in risk register |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing covering credential leakage paths — memory, logs, tool payloads |
| Risk response | MG-2.2 | MANAGE | Incident response for detected credential exposure — rotation, containment, lateral movement assessment |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish NHI (Non-Human Identity) governance policy —
  all agent identities inventoried, credentials lifecycle-managed,
  no hardcoded secrets in agent code or prompts
- MP-2.3: Map agent credential exposure to specific agent
  deployments in risk register — tool access scope, credential
  types, and rotation schedules documented per agent
- Issue short-lived, task-scoped credentials per agent invocation —
  enforce as a policy requirement across all agentic deployments

**Hardening**
- MS-2.5: Include credential leakage scenarios in adversarial
  testing — test memory store persistence, log capture, and
  tool payload exposure for all credential types used by agents
- MG-2.2: Define incident response for credential exposure —
  immediate rotation, lateral movement assessment, downstream
  system notification, and forensic capture
- Implement just-in-time (JIT) credential issuance with automatic
  revocation on task completion

**Advanced**
- MS-2.5: Conduct red team exercises simulating agent credential
  abuse — stolen token lateral movement across all systems the
  agent has access to
- GV-1.6: Implement continuous NHI monitoring — anomalous
  token usage patterns across all agent sessions feed into
  AI risk monitoring programme
- MG-2.2: Automated credential rotation triggered on any anomaly
  detection signal — not just scheduled rotation

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| Teleport | Open-source/Commercial | https://goteleport.com |
| Entro Security | Commercial | https://entro.security |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse, ASI07 Insecure Inter-Agent Comms
- DSGAI 2026: DSGAI01 Sensitive Data Leakage
- Other frameworks: OWASP NHI Top 10 · ISO 27001 A.8.2 · AIUC-1 A/B007

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High

Employees use unapproved GenAI SaaS tools outside formal governance,
pasting sensitive data into external models with no contractual
protections, data lineage, or incident response capability.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Acceptable use policy for AI tools — approved list, prohibited use cases, data handling requirements |
| AI system impact | MP-3.5 | MAP | Impact assessment of shadow AI on organisational data security posture — ungoverned data flows quantified |
| Testing — data leakage | MS-2.6 | MEASURE | Evaluation of shadow AI detection effectiveness — DLP coverage, endpoint monitoring |
| Risk response — data | MG-2.4 | MANAGE | Response procedures for detected shadow AI usage — data impact assessment, user notification |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish and publish AI acceptable use policy —
  approved tool list, prohibited use cases, and consequences
  for violation — include in employee onboarding
- MP-3.5: Conduct shadow AI impact assessment — identify which
  data categories are at risk through unsanctioned tool usage
  and quantify the exposure
- Deploy DLP on known AI SaaS endpoints — detect and alert on
  sensitive data transfer to unapproved AI services

**Hardening**
- MS-2.6: Evaluate DLP coverage against shadow AI vectors —
  browser extensions, mobile apps, productivity integrations
  not covered by endpoint-only DLP
- MG-2.4: Define response for detected shadow AI incidents —
  data impact assessment, vendor data deletion requests,
  regulatory notification if personal data involved
- Conduct security assessment of all AI SaaS tools before
  approval — data retention, training use, sub-processors

**Advanced**
- GV-1.7: Integrate AI tool approval into formal procurement —
  AI capabilities in broader SaaS products captured at vendor
  onboarding, not discovered post-adoption
- MS-2.6: Implement continuous shadow AI discovery — automated
  ongoing detection across endpoints, network egress, and
  SaaS access logs, not point-in-time assessment
- MG-2.4: Establish contractual right-to-delete with all
  approved AI vendors — enforceable on shadow AI incident
  detection

#### Tools

| Tool | Type | Link |
|---|---|---|
| Zscaler (CASB) | Commercial | https://www.zscaler.com |
| Microsoft Defender for Cloud Apps | Commercial | https://www.microsoft.com/en-us/security |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.10/A.5.23 · EU AI Act Art. 25

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical

Adversaries corrupt training datasets, model weights, or supply chain
components to embed backdoors or bias model behaviour — baked into
the weights and invisible to standard testing until triggered.

**Real-world references:**
- Nightshade (2023) — poison pixels corrupted image generation model
- Multiple malicious models with backdoors on Hugging Face (2024)

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Risk categorisation | MP-2.3 | MAP | Data and model poisoning categorised as Critical — specific attack vectors mapped per training pipeline |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing covering poisoning detection in training pipelines before each production promotion |
| Data quality | MS-3.3 | MEASURE | Data quality measurement and validation applied to all training and fine-tuning data |
| Risk response | MG-2.2 | MANAGE | Incident response including model rollback for detected poisoning events |

#### Mitigations by tier

**Foundational**
- MS-3.3: Implement data quality measurement on all training
  data — anomaly detection, source validation, and lineage
  tracking before any training run begins
- MP-2.3: Include poisoning attack vectors in AI risk register —
  training data sources, fine-tuning pipelines, and supply
  chain components each assessed separately
- Implement source allowlisting for training data — only
  approved, validated sources enter production training pipelines

**Hardening**
- MS-2.5: Include poisoning detection in adversarial evaluation
  programme — backdoor trigger testing and biased output
  detection before every production model promotion
- MG-2.2: Establish model rollback capability — versioned model
  registry with clean checkpoint restore on poisoning detection,
  tested as part of incident response exercises
- Apply differential privacy during training — limits influence
  of any single training example, document as MS-3.3 control

**Advanced**
- MS-2.5: Conduct post-training backdoor detection as a standard
  pre-deployment gate — neural cleanse or equivalent, results
  documented as evaluation programme evidence
- MS-3.3: Implement continuous training data monitoring —
  alert on statistical drift in data distribution that may
  indicate active poisoning campaign
- GV-1.6: Establish dataset governance policy — all training
  data requires documented provenance, approval, and quality
  attestation before use

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| ModelScan | Open-source | https://github.com/protectai/modelscan |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain, LLM04 Data & Model Poisoning
- Agentic Top 10: ASI04 Supply Chain, ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.27/A.8.29 · MITRE ATLAS AML.T0032 · CycloneDX ML SBOM

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High

Adversarially crafted payloads passing syntactic validation corrupt
training sets or exploit snapshot import path traversal to achieve
arbitrary file write on vector DB hosts.

**Real-world references:**
- CVE-2024-3584 (Qdrant) — path traversal via poisoned snapshot
  import achieved arbitrary file write on vector DB host

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Testing — adversarial | MS-2.5 | MEASURE | Security testing of all data ingestion interfaces — schema bypass and path traversal scenarios |
| Data quality | MS-3.3 | MEASURE | Data quality controls applied at ingestion — syntactic and semantic validation |
| Risk response | MG-2.2 | MANAGE | Response procedures for detected ingestion integrity failures |
| Risk categorisation | MP-2.3 | MAP | Ingestion integrity risks mapped to specific pipeline components in risk register |

#### Mitigations by tier

**Foundational**
- MS-3.3: Implement multi-stage validation at all ingestion
  boundaries — syntax, schema, semantic, and statistical
  validation in sequence with rejection logging at each stage
- MP-2.3: Map ingestion integrity risks to specific pipeline
  components — identify which endpoints accept external data
  and rate each by exposure and impact
- Harden all snapshot import and restore endpoints — disable
  or restrict by default, document as MG-2.2 control

**Hardening**
- MS-2.5: Include schema bypass, path traversal, and semantic
  injection scenarios in security testing — fuzz all data
  ingestion interfaces before deployment
- Patch CVE-2024-3584 and equivalent vulnerabilities in all
  vector database deployments — treat as urgent MS-2.5 finding
- Implement anomaly detection on ingestion payloads — flag
  statistical outliers and unusual encoding before pipeline
  completion

**Advanced**
- MS-2.5: Conduct adversarial ingestion testing on every new
  pipeline component — document results as evaluation evidence
- Sandbox all snapshot import operations — no direct write to
  production filesystem paths, isolated execution environment
- MG-2.2: Establish automated quarantine on ingestion anomaly
  detection — pause pipeline, alert owner, trigger forensic
  capture before resuming

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://greatexpectations.io |
| Pandera | Open-source | https://pandera.readthedocs.io |
| OWASP ZAP | Open-source | https://www.zaproxy.org |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.26/A.8.28/A.8.29 · CWE-20 · OWASP ASVS V5

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange Risks

**Severity:** High

AI tools, plugins, and MCP servers receive full context payloads —
customer records, internal documents, API responses — with no data
minimisation, creating ungoverned third-party data flows.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Third-party data handling policy covering all tool and plugin integrations |
| Interdependencies | MP-5.1 | MAP | All tool and plugin integrations mapped — data received, retained, and used for training |
| Testing — adversarial | MS-2.5 | MEASURE | Security testing of tool API integrations — payload inspection, data minimisation validation |
| Residual risk — third party | MG-3.2 | MANAGE | Residual risk from tool providers documented, monitored, and reviewed |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish third-party data handling policy for all
  tool integrations — zero training use by default, defined
  retention, incident notification requirements
- MP-5.1: Complete inventory of all tool and plugin integrations —
  what data each receives, processes, and stores, documented
  before any integration reaches production
- Implement context minimisation — tools receive only the minimum
  payload required for their function, not full context history

**Hardening**
- MS-2.5: Include tool payload inspection in security testing —
  verify data minimisation is enforced and sensitive content
  is not transmitted to tool providers unnecessarily
- MG-3.2: Document residual risk from each tool provider —
  include in AI risk register with annual review cadence
- Conduct security assessments of all strategic tool providers —
  include in supplier risk management programme

**Advanced**
- GV-1.6: Implement contractual right-to-audit for all tool
  providers receiving sensitive agent context
- MS-2.5: Deploy outbound DLP on all tool API calls — block
  sensitive data patterns from leaving the controlled environment
- MG-3.2: Establish tool provider incident escalation path —
  tested annually as part of AI incident response exercises

#### Tools

| Tool | Type | Link |
|---|---|---|
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- Agentic Top 10: ASI02 Tool Misuse, ASI04 Supply Chain
- Other frameworks: ISO 27001 A.5.19/A.5.20 · AIUC-1 A/B006 · EU AI Act Art. 25

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High

GenAI creates derived data assets — embeddings, summaries, agent traces,
cached retrievals — outside traditional governance programmes.
Classification labels, retention policies, and erasure obligations
do not propagate from source documents to their derived representations.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Data governance policy extended to all GenAI-derived assets — embeddings, caches, memory, telemetry |
| Context establishment | MP-1.6 | MAP | GenAI data assets inventoried and mapped — source through derivation chain documented |
| Data quality | MS-3.3 | MEASURE | Data quality and governance controls measured across full GenAI data lifecycle |
| Residual risk | MG-3.2 | MANAGE | Residual governance risk from ungoverned derived assets documented and treated |

#### Mitigations by tier

**Foundational**
- GV-1.6: Extend asset inventory to all GenAI data assets —
  training datasets, evaluation sets, embedding stores, RAG
  corpora, agent memory, prompt templates, observability logs
- MP-1.6: Map all GenAI data flows end-to-end — source through
  preprocessing, embedding, retrieval, generation, and logging —
  document as part of AI risk context establishment
- Establish deletion procedures covering derived assets —
  deleting a source document triggers deletion of all
  derived representations

**Hardening**
- MS-3.3: Measure governance control effectiveness across the
  GenAI lifecycle — classification propagation rates, retention
  compliance, erasure completion times
- GV-1.6: Implement automated label propagation — classification
  tags flow from source data through full derivation chain
- Establish data retention schedules per asset type — embedding
  stores, session caches, observability data, agent traces
  each with appropriate TTLs

**Advanced**
- MG-3.2: Document residual governance risk from ungoverned
  derived assets — include in AI risk register with treatment
  roadmap and review cadence
- Implement machine unlearning readiness — versioned data-to-model
  linkage enabling scoped targeted retraining on erasure request
- Generate and maintain a Data Bill of Materials (DBoM) for
  all production AI systems — auditable provenance chain from
  source through all derived forms

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| OpenMetadata | Open-source | https://open-metadata.org |
| Collibra | Commercial | https://www.collibra.com |

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI01 Sensitive Data Leakage
- Other frameworks: ISO 27001 A.5.9/A.8.10 · EU AI Act Art. 10 · ISO 27701

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High

GenAI systems trigger obligations under GDPR, EU AI Act, HIPAA, CCPA,
and sector regulations — often without the organisation recognising
the system is in scope. Training on personal data without lawful basis,
retaining data beyond permitted periods, and failing to support data
subject rights are the most common violation patterns.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Legal and regulatory compliance obligations for GenAI documented in governance policy |
| Organisational teams | GV-4.2 | GOVERN | Cross-functional team accountable for GenAI regulatory compliance — legal, privacy, security, AI |
| Testing — data leakage | MS-2.6 | MEASURE | Compliance testing — lawful basis verification, data subject rights fulfilment, retention compliance |
| Risk response — data | MG-2.4 | MANAGE | Regulatory incident response — breach notification timelines, regulatory reporting obligations |

#### Mitigations by tier

**Foundational**
- GV-1.6: Conduct regulatory scoping assessment for all GenAI
  deployments — identify applicable regulations, triggered
  obligations, and accountable owners
- GV-4.2: Establish cross-functional AI compliance team —
  legal, privacy, security, and AI representation with clear
  mandate and meeting cadence
- Establish lawful basis for all personal data processed by
  GenAI — documented in GDPR Art. 30 records of processing

**Hardening**
- MS-2.6: Include compliance testing in evaluation programme —
  lawful basis verification, retention limit compliance, data
  subject rights fulfilment testing across all GenAI deployments
- MG-2.4: Define regulatory incident response — breach
  notification timelines per regulation, regulatory reporting
  obligations, and designated contacts per authority
- Extend RoPA to cover all AI training and inference activities —
  including sub-processor relationships with model providers

**Advanced**
- MS-2.6: Implement automated compliance posture monitoring —
  continuous assessment against regulatory obligations, flagging
  gaps in lawful basis, expired consent, unverified erasure
- GV-1.6: EU AI Act Aug 2026 readiness assessment for any system
  qualifying as high-risk — gap analysis and remediation roadmap
- MG-2.4: Regulatory relationship management — proactive
  engagement with data protection authorities on AI use cases
  rather than reactive response to investigations

#### Tools

| Tool | Type | Link |
|---|---|---|
| OneTrust | Commercial | https://www.onetrust.com |
| Osano | Commercial | https://www.osano.com |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance
- Other frameworks: EU AI Act Art. 10/17 · ISO 27701 · ISO 27001 A.5.31 · GDPR Art. 5/25/30

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Users upload screenshots, passport photos, voice recordings, and
whiteboard images to multimodal AI assistants. OCR and transcription
extract the content — but extracted text is treated as less sensitive
than the original, creating a leakage path where sensitive content
persists in logs and embeddings beyond stated retention periods.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Multimodal data governance policy — classification propagation from source modality to all extracted forms |
| Risk categorisation | MP-2.3 | MAP | Multimodal leakage risks mapped per modality — image, audio, video, document — in risk register |
| Testing — data leakage | MS-2.6 | MEASURE | Data leakage testing extended to multimodal pipelines — OCR output, transcripts, derived embeddings |
| Risk response — data | MG-2.4 | MANAGE | Incident response for multimodal data leakage — content identification, deletion, regulatory notification |

#### Mitigations by tier

**Foundational**
- GV-1.6: Classify multimodal uploads at ingestion — an image
  of a passport is Restricted; its OCR output is equally
  Restricted — policy enforced, not assumed
- MP-2.3: Map multimodal leakage risks per modality in risk
  register — image OCR, audio transcription, and video
  analysis each assessed separately
- Apply the same redaction standards to OCR and transcription
  output as to equivalent text inputs

**Hardening**
- MS-2.6: Include multimodal leakage in evaluation programme —
  test OCR output classification, transcript retention, and
  derived embedding access controls
- Implement short retention windows for multimodal uploads and
  all derived content — delete after purpose is served,
  automated not manual
- Deploy PII detection on multimodal extraction pipelines in
  real time — block or redact before storage

**Advanced**
- MS-2.6: Conduct red team exercises targeting multimodal
  leakage paths — OCR output in logs, audio transcripts in
  embeddings, derived content in RAG stores
- MG-2.4: Implement content-aware deletion for multimodal
  assets — trigger automated deletion on classification-based
  retention rules across all derived forms
- GV-1.6: Extend multimodal governance policy to cover
  AI-generated content from multimodal inputs — synthetic
  images and audio derived from sensitive uploads

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| AWS Macie | Commercial | https://aws.amazon.com/macie/ |
| Google Cloud DLP | Commercial | https://cloud.google.com/dlp |

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI14 Telemetry Leakage
- Other frameworks: ISO 27001 A.8.11/A.8.12 · ISO 27701 · GDPR Art. 9

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium

Organisations use synthetic data and anonymisation to satisfy privacy
requirements — but GenAI-era reconstruction attacks can re-identify
individuals from supposedly anonymised datasets, and synthetic data
may preserve statistical properties of sensitive source data.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Anonymisation governance policy — legal standard, not technical checkbox |
| Testing — data leakage | MS-2.6 | MEASURE | Re-identification risk testing and membership inference testing on synthetic datasets |
| Data quality | MS-3.3 | MEASURE | Data quality measurement of synthetic datasets — statistical fidelity vs privacy tradeoffs |
| Residual risk | MG-3.2 | MANAGE | Residual re-identification risk documented and accepted formally before dataset release or use |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish synthetic data governance policy —
  anonymisation methodology, quality thresholds, re-identification
  risk acceptance criteria, and review cadence documented
- MS-3.3: Measure synthetic data quality — fidelity to source
  distribution vs privacy budget tradeoff quantified before use
- Classify synthetic datasets based on re-identification risk —
  do not automatically treat synthetic data as non-personal

**Hardening**
- MS-2.6: Include re-identification risk testing in evaluation
  programme — formal risk assessment before releasing or using
  synthetic datasets externally
- Apply differential privacy (DP-SGD) to synthetic data
  generation — document privacy budget as MS-3.3 control evidence
- MG-3.2: Document residual re-identification risk formally —
  risk owner acceptance required before dataset promotion

**Advanced**
- MS-2.6: Conduct membership inference testing as a standard
  gate in the synthetic data pipeline — document results
- Implement k-anonymity, l-diversity, and t-closeness
  measurements on all synthetic datasets — formal minimum
  standards before classification downgrade
- GV-1.6: Establish legal review of anonymisation claims —
  technical anonymisation aligned with applicable legal
  standard before privacy compliance assertions are made

#### Tools

| Tool | Type | Link |
|---|---|---|
| Synthetic Data Vault | Open-source | https://sdv.dev |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |
| Gretel AI | Commercial | https://gretel.ai |

#### Cross-references
- DSGAI 2026: DSGAI08 Non-Compliance, DSGAI18 Inference & Reconstruction
- Other frameworks: ISO 27001 A.5.34/A.8.11 · ISO 27701 · GDPR Recital 26

---

### DSGAI11 — Cross-Context & Multi-User Conversation Bleed

**Severity:** High

Sensitive data from one user's conversation leaks into another user's
responses through shared KV caches, poorly isolated multi-tenant vector
stores, or system prompt contamination between sessions.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Risk categorisation | MP-2.3 | MAP | Session isolation risks mapped per deployment — shared infrastructure components assessed |
| Testing — adversarial | MS-2.5 | MEASURE | Multi-tenant isolation testing — verify cross-session data access is prevented |
| Testing — data leakage | MS-2.6 | MEASURE | Data leakage testing across session boundaries — KV cache, vector store, conversation history |
| Risk response | MG-2.2 | MANAGE | Incident response for detected cross-session leakage — impact scoping, user notification |

#### Mitigations by tier

**Foundational**
- MP-2.3: Map all shared infrastructure components — KV caches,
  vector stores, conversation history stores — to the session
  isolation risk in the AI risk register
- Implement strict session isolation — each user's context window,
  retrieved documents, and conversation history inaccessible
  to all other sessions by design
- Implement per-user, per-session RAG namespaces — shared
  vector stores enforce tenant isolation at query time

**Hardening**
- MS-2.5: Include cross-tenant isolation testing in security
  evaluation — verify user A cannot retrieve user B's documents
  through any query formulation on every new deployment
- MS-2.6: Test KV cache isolation for shared inference
  infrastructure — per-session cache with strict TTL enforced
- MG-2.2: Define incident response for detected cross-session
  bleed — impact scoping across all affected users, regulatory
  notification if personal data involved

**Advanced**
- MS-2.5: Conduct adversarial cross-tenant testing on every
  major retrieval system change — attempt extraction of other
  users' context through crafted queries
- Implement real-time bleed detection — alert on content
  appearing in session context not sourced from current
  user's authorised scope
- MG-2.2: Implement automated session isolation monitoring —
  alert on anomalous cross-session access patterns feeding
  into AI incident management workflow

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Pinecone Canopy | Open-source | https://github.com/pinecone-io/canopy |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3 · NIST CSF 2.0 PR.DS-5 · GDPR Art. 32

---

### DSGAI12 — Unsafe Natural-Language Data Gateways

**Severity:** Critical

LLM-to-SQL, LLM-to-Graph, and LLM-to-API interfaces collapse the
traditional security boundary between user input and database logic.
Natural language coerces the model into generating destructive queries
executing under high-privilege service accounts with no row-level
enforcement.

**Real-world references:**
- Finance Copilot scenario — malicious RAG-injected document caused
  LLM-generated SQL to dump customer PII from multiple tables
- Multiple production LLM-to-SQL deployments executing bulk
  extraction queries via natural language (2024–2025)

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Risk categorisation | MP-2.3 | MAP | LLM-to-database interface risks mapped — privilege level, query scope, and data exposure per interface |
| Testing — adversarial | MS-2.5 | MEASURE | SQL injection, privilege escalation, and bulk extraction testing on all LLM gateway interfaces |
| Risk response | MG-2.2 | MANAGE | Incident response for LLM gateway misuse — query log forensics, data exposure scoping |
| Policies for trustworthy AI | GV-1.7 | GOVERN | Policy requiring least-privilege execution and read-only defaults for all LLM-to-database interfaces |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish policy requiring least-privilege execution
  for all LLM-generated database queries — interface executes
  under requesting user's permissions, never a shared
  high-privilege service account
- MP-2.3: Map all LLM-to-database interfaces to risk register —
  privilege level, query scope, data categories accessible,
  and row-level policy enforcement status per interface
- Restrict LLM-to-SQL interfaces to read-only operations by
  default — write, delete, and DDL require explicit approval

**Hardening**
- MS-2.5: Include SQL injection, privilege escalation, and bulk
  extraction in adversarial testing for all LLM gateway
  interfaces before deployment
- Implement query allowlisting — only pre-approved patterns
  permitted, parameterised execution only, reviewed on change
- Log all LLM-generated query text with requesting user identity —
  forensic traceability mandatory, feed into SIEM

**Advanced**
- MS-2.5: Conduct adversarial NL-to-SQL testing — attempt to
  coerce destructive query generation through crafted natural
  language inputs on your specific deployment
- Deploy query analysis layer between LLM and database —
  validates generated SQL against permitted patterns before
  execution, rejects destructive or over-broad queries
- MG-2.2: Implement automated alerting on bulk extraction
  patterns — high-frequency or high-volume LLM-generated
  queries trigger immediate investigation workflow

#### Tools

| Tool | Type | Link |
|---|---|---|
| Semgrep | Open-source | https://semgrep.dev |
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Immuta | Commercial | https://www.immuta.com |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- Other frameworks: ISO 27001 A.8.26/A.8.28 · CWE-89 · OWASP ASVS V5

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector databases store sensitive embeddings and retrieved passages with
weaker default security posture than traditional databases — missing
RBAC, unencrypted storage, exposed snapshot endpoints, and
unauthenticated collection access are common.

**Real-world references:**
- CVE-2024-3584 (Qdrant) — snapshot import path traversal achieving
  arbitrary file write on vector DB host
- Multiple publicly exposed Chroma instances in production (2024)

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Risk categorisation | MP-2.3 | MAP | Vector store risks mapped — each deployment assessed for RBAC, encryption, and network exposure |
| Testing — adversarial | MS-2.5 | MEASURE | Vector store security testing — RBAC bypass, path traversal, unauthenticated access scenarios |
| Data quality | MS-3.3 | MEASURE | Data integrity controls applied to vector store ingestion and query operations |
| Risk response | MG-2.2 | MANAGE | Incident response for vector store compromise — containment, data exposure scoping, index rebuild |

#### Mitigations by tier

**Foundational**
- MP-2.3: Map all vector store deployments in risk register —
  RBAC status, encryption status, network exposure, and
  known CVE patching status per deployment
- Enable RBAC on all vector store collections from day one —
  no unauthenticated access in any environment
- Patch all known vector database CVEs — CVE-2024-3584 and
  equivalents treated as urgent MS-2.5 findings

**Hardening**
- MS-2.5: Include vector store-specific security testing in
  evaluation programme — RBAC bypass, path traversal, and
  unauthenticated access scenarios before each deployment
- Implement namespace isolation for multi-tenant deployments —
  one collection per trust domain, no cross-namespace queries
- Deploy network access controls — vector stores accessible
  only from authorised services, never public internet

**Advanced**
- MS-2.5: Conduct adversarial vector store testing — bulk
  extraction, embedding inversion, and snapshot import
  attack scenarios against your specific deployment
- MG-2.2: Implement vector store access monitoring — alert
  on bulk query patterns indicating scraping or exfiltration
  feeding into AI incident management workflow
- MS-3.3: Implement embedding access anomaly detection —
  statistical monitoring of query patterns against baseline

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant (with API key auth) | Open-source | https://qdrant.tech |
| OWASP ZAP | Open-source | https://www.zaproxy.org |

#### Cross-references
- LLM Top 10: LLM08 Vector & Embedding Weaknesses
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3/A.8.24 · NIST CSF 2.0 PR.DS-7 · CWE-284

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High

Observability pipelines capture full prompt text, tool call payloads,
retrieved passages, and model outputs with weaker access controls and
longer retention than production data — creating a secondary
exfiltration path.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Telemetry governance policy — least-logging defaults, classification of captured data, retention limits |
| Risk categorisation | MP-2.3 | MAP | Telemetry leakage risks mapped — identify which pipelines capture full payload and at what retention |
| Testing — data leakage | MS-2.6 | MEASURE | Data leakage testing on telemetry stores — sensitive content in logs and traces |
| Risk response — data | MG-2.4 | MANAGE | Response for telemetry data leakage incidents — access log review, data deletion, notification |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish telemetry governance policy — least-logging
  defaults, classification of captured data, retention limits
  per telemetry tier documented as ISMS policy
- MP-2.3: Map all telemetry pipelines to risk register — identify
  which capture full prompt and response bodies, at what
  retention window, with what access controls
- Apply access controls to telemetry stores — same rigour
  as production data stores, not relaxed because "just logs"

**Hardening**
- MS-2.6: Include telemetry data leakage in evaluation programme —
  test which sensitive content lands in logs and traces, verify
  redaction effectiveness
- Implement short TTL for debug traces — automated deletion
  after defined window, not indefinite retention
- MG-2.4: Define response for telemetry leakage — access log
  review to determine who accessed, data deletion, regulatory
  notification if personal data involved

**Advanced**
- MS-2.6: Conduct adversarial telemetry extraction testing —
  attempt to extract sensitive production data through
  telemetry store access paths
- Implement approval workflow for enabling full debug capture —
  temporary, scoped, logged, automatically reverted
- GV-1.6: Include telemetry data retention in board-level
  AI data governance reporting — telemetry as a data asset
  with equivalent governance obligations

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Langfuse | Open-source | https://langfuse.com |
| Helicone | Open-source | https://www.helicone.ai |

#### Cross-references
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI07 Data Governance
- Other frameworks: ISO 27001 A.8.15/A.8.12 · ISO 27701 · GDPR Art. 32

---

### DSGAI15 — Over-Broad Context Windows & Prompt Over-Sharing

**Severity:** High

RAG pipelines inject excessive content into context windows —
full document texts, entire conversation histories — aggregating
data from multiple trust domains into a single flat namespace with
no internal access control, amplifying the impact of any prompt
injection that reaches this context.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Risk categorisation | MP-2.3 | MAP | Context window risks mapped — identify which deployments aggregate data across trust domains |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing of context window content — cross-trust-domain aggregation and injection scenarios |
| Testing — data leakage | MS-2.6 | MEASURE | Data leakage testing on context window content — sensitive data accessible to injection attacks |
| Risk response | MG-2.2 | MANAGE | Response for context window exploitation — session containment, content audit, impact scoping |

#### Mitigations by tier

**Foundational**
- MP-2.3: Map context window risks per deployment — identify
  which deployments aggregate data across trust domains and
  classification tiers, rate each in risk register
- Implement minimum-necessary context injection — retrieve
  only passages directly relevant to the query, not entire
  documents or broad topic matches
- Track classification of all content entering context window —
  highest classification drives handling requirement for the
  entire response

**Hardening**
- MS-2.5: Include context window over-sharing in adversarial
  testing — verify that injection cannot access injected
  content from other trust domains
- MS-2.6: Test cross-trust-domain context leakage scenarios —
  what content is accessible to an attacker who achieves
  prompt injection on your specific RAG deployment
- Implement context window monitoring — alert on assembly
  patterns aggregating data from multiple trust domains

**Advanced**
- MS-2.5: Conduct red team exercises specifically targeting
  context window exploitation — craft prompts designed to
  extract maximum content from injected context
- Implement trust-domain-aware context assembly — content
  from different trust domains isolated within context window
  with explicit labelling
- MG-2.2: Automated session termination on context window
  anomaly detection — injection indicator triggers session
  isolation before further tool execution

#### Tools

| Tool | Type | Link |
|---|---|---|
| LlamaIndex | Open-source | https://www.llamaindex.ai |
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |

#### Cross-references
- LLM Top 10: LLM07 System Prompt Leakage
- Agentic Top 10: ASI01 Agent Goal Hijack
- Other frameworks: ISO 27001 A.8.3 · AIUC-1 A/B005 · NIST CSF 2.0 PR.DS-5

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High

Browser-integrated AI assistants access sensitive data across all open
tabs, local files, and clipboard content. Malicious updates or hidden
prompt instructions in web content weaponise these agents for data
exfiltration.

**Real-world references:**
- HashJack (2025) — AI browsers hijacked via hidden prompt instructions
  enabling data exfiltration
- Multiple AI extensions logging clipboard and form field content

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Endpoint AI agent governance policy — approved extensions, permission scoping, mandatory updates |
| AI system impact | MP-3.5 | MAP | Impact assessment of endpoint AI agents — data access scope, exfiltration paths, user risk |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing of approved browser extensions — prompt injection via web content scenarios |
| Risk response | MG-2.2 | MANAGE | Incident response for endpoint AI agent compromise — extension disable, data impact assessment |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish approved list of endpoint AI agents and
  browser extensions — unapproved extensions blocked at
  device management layer, policy enforced
- MP-3.5: Conduct impact assessment of all endpoint AI agents —
  what data they access, what exfiltration paths exist,
  what the blast radius is on compromise
- Apply permission minimisation — extensions receive only
  the permissions required for their stated function

**Hardening**
- MS-2.5: Conduct adversarial testing of approved browser
  extensions before organisation-wide deployment — test for
  hidden prompt injection via web content
- Implement DLP on endpoint AI agent network traffic — detect
  sensitive data leaving via AI assistant channels
- A.8.7 equivalent: Conduct extension integrity verification
  before approval — verify cryptographic signatures,
  review permissions, assess data access scope

**Advanced**
- MS-2.5: Red team exercises targeting endpoint AI agent
  compromise — attempt data exfiltration via hidden prompt
  injection in web content the agent processes
- MG-2.2: Automated response to endpoint AI agent anomaly —
  extension disable, network isolation, forensic capture
  before user notification
- GV-1.7: Vendor security requirements for AI extension
  providers — right-to-audit, incident notification,
  zero training use on enterprise data as contractual terms

#### Tools

| Tool | Type | Link |
|---|---|---|
| LayerX Security | Commercial | https://layerxsecurity.com |
| Microsoft Intune | Commercial | https://www.microsoft.com/en-us/security/business/endpoint-management |

#### Cross-references
- Agentic Top 10: ASI10 Rogue Agents
- DSGAI 2026: DSGAI03 Shadow AI
- Other frameworks: ISO 27001 A.8.1/A.8.7 · AIUC-1 B006 · EU AI Act Art. 9

---

### DSGAI17 — Data Availability & Resilience Failures in AI Pipelines

**Severity:** High

RAG-dependent applications fail silently when vector stores degrade —
returning stale or incorrect information indistinguishable from correct
output. In OT environments this can propagate from the AI layer into
physical process control.

**OT critical note:** In industrial environments, silent RAG failures
producing incorrect operational guidance can propagate into physical
process decisions before detection. Treat as Critical severity in OT/ICS
deployments. See ISA/IEC 62443 and NIST SP 800-82 crosswalks.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Risk tolerance | MP-4.1 | MAP | Availability risk tolerance defined for AI pipelines — RTO/RPO per component documented |
| Testing — adversarial | MS-2.5 | MEASURE | Resilience testing of RAG pipelines — vector store saturation, stale replica, index corruption |
| Risk response | MG-2.2 | MANAGE | Incident response for AI pipeline availability failures — silent degradation detection and response |
| Residual risk | MG-3.2 | MANAGE | Residual availability risk documented — BCP coverage for AI pipeline components |

#### Mitigations by tier

**Foundational**
- MP-4.1: Define availability risk tolerance for all AI pipeline
  components — RTO and RPO per vector store, RAG pipeline,
  and embedding service documented in risk register
- Implement health checks on vector store freshness — alert
  when index age exceeds defined threshold before silent
  misinformation reaches users
- MG-2.2: Define incident response for AI pipeline availability
  failures — include silent degradation detection as a distinct
  failure mode separate from hard outages

**Hardening**
- MS-2.5: Include resilience scenarios in evaluation programme —
  vector store saturation, stale replica failover, and index
  corruption tested against your specific deployment
- Deploy redundancy for production RAG infrastructure —
  replica synchronisation lag monitored and bounded by policy
- MG-3.2: Include AI pipeline components in BCP — annual
  failover drills covering vector store failure scenarios

**Advanced**
- MS-2.5: Conduct adversarial availability testing — attempt
  to saturate vector endpoints through high-cardinality queries
  and verify circuit breaker effectiveness
- Implement circuit breakers on RAG retrieval — degrade
  gracefully to non-RAG responses rather than silently
  serving stale results, with user notification
- MG-3.2: Test integrity of restored vector indexes — verify
  backup restoration produces correct retrieval, not just
  structural integrity

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

Adversaries reconstruct sensitive training data through membership
inference attacks, model inversion, and embedding inversion — extracting
PII, proprietary content, or confidential records without direct
data access.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Privacy policy extended to cover inference attack resistance — not just direct disclosure |
| Risk categorisation | MP-2.3 | MAP | Inference attack risks mapped — membership inference, model inversion, embedding inversion per deployment |
| Testing — adversarial | MS-2.5 | MEASURE | Red team exercises covering membership inference and model inversion attack scenarios |
| Risk response — data | MG-2.4 | MANAGE | Response for confirmed inference attack — unlearning, output rate limiting, disclosure assessment |

#### Mitigations by tier

**Foundational**
- GV-1.6: Extend privacy policy to cover inference attack
  resistance — membership inference and model inversion
  explicitly in scope alongside direct disclosure
- MP-2.3: Map inference attack risks to specific deployments
  in risk register — assess which models and embedding stores
  are most susceptible given their training data
- Monitor model outputs for content that may represent
  reconstructed training data — alerts on near-verbatim
  reproduction of likely training content

**Hardening**
- MS-2.5: Conduct membership inference and model inversion
  red team exercises as standard pre-deployment validation —
  document results as privacy control evidence
- Apply differential privacy during training — limits
  membership inference success rate, document privacy budget
- Implement confidence score suppression — do not return
  raw logits that enable membership inference

**Advanced**
- MS-2.5: Conduct embedding inversion red team exercises —
  validate embeddings do not reconstruct source content
  under realistic attacker conditions
- MG-2.4: Implement machine unlearning readiness — ability
  to surgically remove specific training examples in response
  to confirmed inference attack exposure
- GV-1.6: Include inference attack resistance in AI privacy
  impact assessments — mandatory for any deployment using
  sensitive personal data in training

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI10 Synthetic Data Pitfalls
- Other frameworks: ISO 27001 A.8.11 · ISO 27701 · GDPR Art. 25 · MITRE ATLAS AML.T0024

---

### DSGAI19 — Human-in-the-Loop & Labeler Overexposure

**Severity:** Medium

Human annotators and HITL reviewers access sensitive model inputs and
outputs during labelling and safety evaluation — exposing customer data
or confidential content to third-party contractors with limited data
handling controls.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | HITL data governance policy — data minimisation, contractor handling requirements, retention limits |
| Interdependencies | MP-5.1 | MAP | All labelling vendors and HITL providers mapped — data access scope, contractual protections |
| Testing — data leakage | MS-2.6 | MEASURE | Privacy assessment of labelling workflows — annotator data access scope, anonymisation effectiveness |
| Residual risk | MG-3.2 | MANAGE | Residual privacy risk from labelling vendor access documented and treated |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish HITL data governance policy — data
  minimisation requirements, annotator access scope, retention
  limits, and contractor handling obligations documented
- MP-5.1: Map all labelling vendors and HITL providers —
  what data each accesses, contractual protections in place,
  sub-processor chain documented
- Apply data minimisation to labelling tasks — annotators
  see only minimum content required for annotation

**Hardening**
- MS-2.6: Conduct privacy assessment of labelling workflows —
  verify anonymisation effectiveness, annotator access scope,
  and retention compliance
- Anonymise or pseudonymise sensitive content before exposure
  to annotators — document as GV-1.6 privacy control
- MG-3.2: Document residual privacy risk from labelling
  vendor access — include in AI risk register with vendor
  security review cadence

**Advanced**
- MS-2.6: Audit labelling vendor data handling practices —
  include in supplier risk management programme with right-
  to-audit provision
- Implement synthetic data for labelling where possible —
  real sensitive data replaced with synthetic equivalents
  preserving annotation-relevant properties
- GV-1.6: Extend AI privacy impact assessments to cover
  HITL workflows — mandatory for any labelling involving
  sensitive personal data

#### Tools

| Tool | Type | Link |
|---|---|---|
| Label Studio | Open-source | https://labelstud.io |
| Scale AI | Commercial | https://scale.com |

#### Cross-references
- DSGAI 2026: DSGAI07 Data Governance, DSGAI08 Non-Compliance
- Other frameworks: ISO 27001 A.5.34/A.6.3 · EU AI Act Art. 10 · GDPR Art. 28

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High

Adversaries extract sufficient information through systematic querying
to reconstruct a functional model replica — stealing proprietary
training investment and fine-tuned capabilities without accessing
original weights.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Risk categorisation | MP-2.3 | MAP | Model extraction risks mapped per public-facing deployment — query volume limits, diversity monitoring |
| Testing — adversarial | MS-2.5 | MEASURE | Model extraction red team exercises — attempt replication using your own API |
| Testing — data leakage | MS-2.6 | MEASURE | Monitoring for systematic extraction patterns — anomalous query diversity and volume |
| Risk response | MG-2.2 | MANAGE | Response for detected model extraction — rate limit tightening, session blocking, forensic capture |

#### Mitigations by tier

**Foundational**
- MP-2.3: Map model extraction risks to each public-facing
  deployment — query volume limits, output perturbation,
  and anomaly monitoring status documented per model
- Implement API rate limiting and query volume caps — systematic
  extraction requires high query volumes, rate limiting
  raises the cost dramatically
- MS-2.6: Monitor for model extraction patterns — unusual
  query diversity, systematic output space coverage,
  high-volume confidence score harvesting

**Hardening**
- MS-2.5: Conduct model extraction red team exercises —
  attempt to replicate your model using your own API and
  document the query budget required
- Implement output perturbation — add calibrated noise to
  confidence scores without degrading utility
- MG-2.2: Define response for detected extraction — rate
  limit tightening, session blocking, forensic capture,
  legal assessment

**Advanced**
- MS-2.5: Implement adaptive rate limiting based on query
  diversity scoring — tighten limits on sessions exhibiting
  systematic extraction patterns
- Apply model output watermarking — enables detection of
  replicated model usage in the wild
- GV-1.6: Include model IP protection in AI governance policy —
  classification of model artifacts, access controls,
  and legal response capability for discovered replicas

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Fiddler AI | Commercial | https://www.fiddler.ai |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- DSGAI 2026: DSGAI18 Inference & Reconstruction
- Other frameworks: ISO 27001 A.5.12/A.8.3 · MITRE ATLAS AML.T0016 · CWE-200

---

### DSGAI21 — Disinformation & Integrity Attacks via Data Poisoning

**Severity:** High

Adversaries inject false content into trusted retrieval sources — RAG
corpora, knowledge bases, web indexes — so AI systems surface this
as authoritative output, with no training access required.

**Real-world references:**
- Grok RAG incident (2025) — production RAG system surfaced
  externally introduced false information as authoritative output
- Crowdsourced dataset poisoning campaigns targeting open
  training corpora — active documented attack class

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Policy on information integrity for AI outputs — source trust verification, cross-verification requirements |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing of RAG pipeline integrity — source poisoning and retrieval manipulation scenarios |
| Data quality | MS-3.3 | MEASURE | Data quality controls on all RAG ingestion — provenance, source trust scoring, anomaly detection |
| Risk response | MG-2.2 | MANAGE | Response for detected RAG poisoning — source quarantine, index rebuild, output correction |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish policy on information integrity for AI
  outputs — source trust verification requirements, cross-
  verification standards for high-stakes domains
- MS-3.3: Implement source trust tiering in RAG retrieval —
  weight results by provenance and trust score, not only
  semantic similarity
- Monitor RAG corpora for unauthorised modifications —
  integrity hashing on all indexed content

**Hardening**
- MS-2.5: Include RAG poisoning scenarios in adversarial
  evaluation — test susceptibility to injected false content
  via each retrieval source before deployment
- Implement ingestion gates — elevated validation during
  active threat periods or when intelligence indicates
  targeting of your retrieval sources
- MG-2.2: Define response for detected RAG poisoning —
  source quarantine, impacted index rebuild, output
  correction, user notification where material impact

**Advanced**
- MS-2.5: Conduct adversarial integrity evaluation — red
  team testing of RAG pipeline susceptibility to low-
  frequency poisoning as standard pre-deployment gate
- Automated HITL triggers for AI decisions derived from
  low-provenance or recently indexed sources in irreversible
  decision contexts
- MS-3.3: Maintain Dataset Bill of Materials (DBoM) with
  cryptographic provenance chain — detect unauthorised
  modification to retrieval corpora post-ingestion

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://greatexpectations.io |
| Deepchecks | Open-source | https://deepchecks.com |
| TruLens | Open-source | https://github.com/truera/trulens |

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0045 · ISO 27001 A.5.7 · EU AI Act Art. 55(1)(a)

---

## AI RMF profile for GenAI data security

The NIST AI RMF supports AI risk profiles mapping current vs target
state. The DSGAI-to-AI RMF profile below is the recommended starting
point for organisations integrating DSGAI risks into an AI RMF programme:

| AI RMF Function | DSGAI priority entries | Key subcategories | Target state |
|---|---|---|---|
| GOVERN | DSGAI01, DSGAI03, DSGAI07, DSGAI08 | GV-1.6, GV-1.7, GV-4.2 | Documented policies, cross-functional team, regulatory scoping complete |
| MAP | DSGAI02, DSGAI06, DSGAI12, DSGAI13 | MP-2.3, MP-4.1, MP-5.1 | All GenAI data assets and flows mapped, risk register complete |
| MEASURE | DSGAI04, DSGAI05, DSGAI11, DSGAI18 | MS-2.5, MS-2.6, MS-3.3 | Adversarial testing programme live, data quality controls measured |
| MANAGE | DSGAI01, DSGAI12, DSGAI17, DSGAI21 | MG-2.2, MG-2.4, MG-3.2 | Incident response tested, residual risk documented and accepted |

A machine-readable version of this profile is available at:
`data/dsgai-2026/nist-aiRMF-profile.json`

---

## Implementation priority

| Phase | DSGAI entries | AI RMF focus | Rationale |
|---|---|---|---|
| 1 — Do now | DSGAI01, DSGAI02, DSGAI12 | GV-1.6 policy, MP-2.3 risk register, MG-2.2 IR | Critical severity, most likely to produce a breach incident |
| 2 — This sprint | DSGAI03, DSGAI07, DSGAI14 | GV-1.7 policy, MP-1.6 inventory, MS-2.6 testing | Asset inventory and governance close shadow AI and telemetry gaps |
| 3 — This quarter | DSGAI04, DSGAI05, DSGAI13 | MS-2.5 testing, MS-3.3 data quality, MG-2.2 IR | Integrity and vector store controls require pipeline-level changes |
| 4 — Ongoing | DSGAI08–DSGAI11, DSGAI15–DSGAI21 | All subcategories | Defence-in-depth, privacy, resilience, and regulatory hardening |

---

## References

- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [NIST AI RMF Playbook](https://airc.nist.gov/Docs/2)
- [NIST Trustworthy and Responsible AI Resource Center](https://airc.nist.gov)
- [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [NIST SP 800-218A — Secure Software Development for AI](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf)
- [Executive Order 14110 on Safe, Secure, and Trustworthy AI](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full entries with AI RMF profile | OWASP GenAI Data Security Initiative |

---

*Part of the [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
