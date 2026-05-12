<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks & Mitigations 2026 (DSGAI01–DSGAI21)
  Framework   : OWASP Application Security Verification Standard (ASVS) 4.0.3
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × OWASP ASVS 4.0.3

Mapping the [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to the [OWASP Application Security Verification Standard (ASVS) 4.0.3](https://owasp.org/www-project-application-security-verification-standard/)
— the framework for verifying the security of web applications and APIs, organised
into 14 chapters with three verification levels (L1/L2/L3).

DSGAI risks emerge at the data layer — training pipelines, RAG stores, vector
databases, context windows, and multimodal input channels. All of these are
components of application architectures where standard ASVS requirements apply
directly, augmented by GenAI-specific data handling requirements. This mapping
enables security engineers and penetration testers to translate DSGAI threats into
verifiable ASVS requirements for inclusion in security test plans.

---

## ASVS structure

| Chapter | Title | DSGAI relevance |
|---|---|---|
| V1 | Architecture, Design, and Threat Modelling | GenAI data architecture, trust boundary design |
| V2 | Authentication | Agent and service authentication, credential management |
| V3 | Session Management | Context window isolation, conversation session security |
| V4 | Access Control | RAG access control, data source permissions, agent permissions |
| V5 | Validation, Sanitisation and Encoding | Input/output validation, NL gateway security |
| V6 | Stored Cryptography | Embedding encryption, training data at rest |
| V7 | Error Handling and Logging | Telemetry security, audit logging |
| V8 | Data Protection | PII protection, data lifecycle, inference privacy |
| V9 | Communication | API and pipeline communication security |
| V10 | Malicious Code | Supply chain, model artefact integrity |
| V11 | Business Logic | Agent action validation, HITL enforcement |
| V12 | Files and Resources | RAG file uploads, multimodal input resources |
| V13 | API and Web Service | LLM API rate limiting, output schema enforcement |
| V14 | Configuration | Secure deployment, default-deny configuration |

**Verification levels:**
- L1 — Opportunistic: passively verifiable, minimum security baseline
- L2 — Standard: applications handling sensitive data
- L3 — Advanced: high-value targets, high assurance required

---

## Quick-reference summary

| ID | Name | Severity | Primary ASVS Chapters | Level | Tier | Scope |
|---|---|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | V8.1, V4.1, V5.2, V6.1 | L1–L3 | Foundational–Advanced | Both |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | V2.1, V4.1, V8.3 | L1–L3 | Foundational–Advanced | Both |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | V1.1, V4.1, V7.2 | L2–L3 | Foundational–Hardening | Both |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | V5.1, V10.2, V12.1 | L2–L3 | Hardening–Advanced | Both |
| DSGAI05 | Data Integrity & Validation Failures | High | V5.1, V5.2, V7.4 | L1–L3 | Foundational–Hardening | Build |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | V4.1, V9.1, V11.1 | L2–L3 | Foundational–Hardening | Both |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | V8.1, V8.3, V4.1 | L1–L3 | Foundational–Advanced | Both |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | V8.3, V7.2, V4.1 | L1–L3 | Foundational–Advanced | Both |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | V5.2, V8.1, V12.1 | L2–L3 | Hardening–Advanced | Both |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | V8.3, V5.2 | L2–L3 | Hardening–Advanced | Build |
| DSGAI11 | Cross-Context Conversation Bleed | High | V3.1, V4.1, V8.1 | L1–L3 | Foundational–Hardening | Build |
| DSGAI12 | Unsafe NL Data Gateways | Critical | V5.1, V5.2, V4.1, V13.1 | L1–L3 | Foundational–Advanced | Build |
| DSGAI13 | Vector Store Platform Security | High | V4.1, V6.1, V12.1 | L2–L3 | Foundational–Hardening | Both |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | V7.1, V8.1, V4.1 | L1–L3 | Foundational–Hardening | Build |
| DSGAI15 | Over-Broad Context Windows | High | V4.1, V8.1, V3.1 | L1–L3 | Foundational–Hardening | Build |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | V4.1, V11.1, V1.1 | L2–L3 | Foundational–Hardening | Both |
| DSGAI17 | Data Availability & Resilience Failures | High | V11.1, V13.1 | L1–L3 | Foundational–Advanced | Both |
| DSGAI18 | Inference & Data Reconstruction | High | V8.3, V6.1 | L2–L3 | Hardening–Advanced | Both |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | V4.1, V8.3, V2.1 | L1–L2 | Foundational–Hardening | Both |
| DSGAI20 | Model Exfiltration & IP Replication | High | V4.1, V8.1, V10.2 | L2–L3 | Hardening–Advanced | Both |
| DSGAI21 | Disinformation via Data Poisoning | High | V5.1, V11.1 | L2–L3 | Hardening–Advanced | Both |

---

## Audience tags

- **Developer** — full file, ASVS requirements to implement for each DSGAI risk
- **Security architect** — V1 architecture, V4 access control, V11 business logic
- **Penetration tester** — verification requirements per level for test planning
- **Security engineer** — V5 validation, V4 access control, V8 data protection
- **Auditor** — ASVS level mapping for assurance assessment against DSGAI risks
- **DPO** — DSGAI01, DSGAI07, DSGAI08, DSGAI10, DSGAI19 (privacy-relevant entries)

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

PII, financial data, credentials, and proprietary content are exposed through model
outputs, RAG over-retrieval, training data memorisation, or inadequate output filtering.
The aggregation effect — combining data from multiple sources in a single context window
— amplifies disclosure risk beyond what any single data source represents.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V8.1.1 — Sensitive data not transmitted in URL parameters | V8 Data Protection | Sensitive data in LLM API calls and RAG queries must not be exposed via URL parameters | L1 | Foundational | Both |
| V8.3.4 — Sensitive data identified and classified | V8 Data Protection | All data types entering LLM context (training, RAG, user input) classified and handled per classification policy | L2 | Foundational | Both |
| V4.1.3 — Deny by default access control | V4 Access Control | RAG data sources enforce deny-by-default — users access only data explicitly authorised to them | L1 | Foundational | Both |
| V5.2.8 — Output encoding for context | V5 Validation | Model outputs scanned and redacted for PII, credentials, and sensitive patterns before delivery | L1 | Foundational | Both |
| V6.1.1 — Sensitive data not stored in cleartext | V6 Cryptography | Training data and RAG corpora containing sensitive data encrypted at rest | L2 | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Implement output scanning and redaction for PII, credentials, and proprietary
  patterns on all model response channels
- Enforce deny-by-default access control on all RAG data sources
- Classify all training and retrieval data before ingestion

**Hardening**
- Deploy DLP tooling on model output pipelines
- Audit RAG retrieval scope — over-permissive indexes are the primary disclosure path
- Encrypt training corpora and vector stores at rest

**Advanced**
- Implement machine unlearning capability for targeted data removal from weights
- Conduct model inversion red team exercises to validate disclosure boundaries

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse, ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.12 — CIS 3.13 — CWE-200 — ENISA L2-DP

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical

Agent credentials, API keys, tokens, and service account secrets embedded in prompts,
logs, or memory are exposed to unauthorised parties. In agentic systems, a single
credential compromise can propagate across all tools and services the agent can access.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V2.1.1 — Passwords minimum 12 characters | V2 Authentication | Agent API keys and service credentials meet minimum strength requirements | L1 | Foundational | Both |
| V2.10.1 — Integration secrets not hardcoded | V2 Authentication | Agent credentials not hardcoded in prompts, configuration files, or code — stored in secrets managers | L2 | Foundational | Both |
| V4.1.2 — Least privilege for service accounts | V4 Access Control | Agent service accounts granted minimum permissions — no shared high-privilege accounts across agents | L1 | Foundational | Both |
| V8.3.7 — Data transferred using current TLS | V8 Data Protection | Agent-to-service communication uses TLS — credentials never transmitted in cleartext | L1 | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Store all agent credentials in secrets managers — never in prompts, logs, or code
- Apply least privilege to all agent service accounts
- Rotate agent credentials automatically on a defined schedule

**Hardening**
- Implement JIT (just-in-time) credential issuance — agents receive scoped credentials
  per task, valid for the task duration only
- Monitor for credential exposure in model outputs and system logs

**Advanced**
- Deploy SPIFFE/SPIRE for workload identity in multi-agent systems
- Implement per-session ephemeral credentials with automatic revocation on session end

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://github.com/hashicorp/vault |
| SPIRE | Open-source | https://github.com/spiffe/spire |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.5.17 — CIS 5.4 — CWE-312 — ENISA L1-AM

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High

Employees use unauthorised AI tools to process sensitive business data — exfiltrating
information to external model providers, creating uncontrolled data copies, and
bypassing data governance controls without organisational visibility.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V1.1.4 — Trust boundaries documented and enforced | V1 Architecture | Data flows to external AI services identified, approved, and enforced at architectural boundaries | L2 | Foundational | Both |
| V4.1.5 — Access control failures logged | V4 Access Control | Attempts to send sensitive data to unapproved AI services detected and logged | L2 | Foundational | Both |
| V7.2.2 — Log entries contain required information | V7 Logging | Audit logs capture data flows to external AI services sufficient for incident investigation | L2 | Hardening | Both |
| V14.1.4 — All components inventoried | V14 Configuration | Inventory of all AI tools in use — approved and shadow — maintained and reviewed regularly | L2 | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Publish an approved AI tools register — employees know which tools are permitted
- Implement egress filtering blocking data transmission to unapproved AI service domains
- Include shadow AI in acceptable use policy with clear consequences

**Hardening**
- Deploy CASB (Cloud Access Security Broker) to detect and block unauthorised AI tool usage
- Implement DLP rules specifically targeting AI service API endpoints

**Advanced**
- Monitor for shadow AI usage patterns in network traffic and endpoint logs
- Deploy automated discovery to identify new AI tools before they become entrenched

#### Tools

| Tool | Type | Link |
|---|---|---|
| Zscaler (DLP) | Commercial | https://www.zscaler.com |
| OpenDLP | Open-source | https://github.com/ezarko/opendlp |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- Other frameworks: ISO 27001 A.5.23 — CIS 2.1 — ENISA L3-GRC

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical

Attackers inject malicious, misleading, or corrupted data into training datasets,
fine-tuning corpora, or RAG stores to alter model behaviour — introducing backdoors,
biases, or targeted misinformation that persist into production.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V5.1.3 — Input validation server-side | V5 Validation | Training data ingestion pipelines validate all inputs against expected schemas before processing | L1 | Foundational | Both |
| V10.2.1 — Application only uses official repositories | V10 Malicious Code | Pre-trained models and datasets sourced only from verified, approved repositories | L2 | Foundational | Both |
| V10.2.2 — Dependency managers check for vulnerabilities | V10 Malicious Code | AI model artefacts checked for known vulnerabilities and backdoors before deployment | L2 | Hardening | Both |
| V12.1.1 — File upload size limits | V12 Files/Resources | Documents uploaded to RAG stores validated for content, size, and format before ingestion | L1 | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Implement data validation and anomaly detection on all training and fine-tuning pipelines
- Restrict write access to training data stores — authorised personnel only
- Maintain immutable audit logs for all training data modifications

**Hardening**
- Generate and version a Dataset Bill of Materials (DBoM) for every training run
- Apply statistical outlier detection on training datasets before use

**Advanced**
- Implement certified data provenance with cryptographic attestation
- Deploy differential privacy in training to limit influence of poisoned samples

#### Tools

| Tool | Type | Link |
|---|---|---|
| Cleanlab | Open-source | https://github.com/cleanlab/cleanlab |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0032 — CIS 7.1 — CWE-345

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High

Absence of validation on data entering or leaving GenAI systems enables injection
attacks, silent data corruption, and undetected pipeline failures — leading to
incorrect model outputs or security bypasses in downstream systems.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V5.1.1 — Input validation using allowlists | V5 Validation | All data ingested into GenAI pipelines validated against an allowlist schema | L1 | Foundational | Build |
| V5.2.1 — HTML/JS output sanitised | V5 Validation | Model outputs destined for HTML renderers sanitised — prevents XSS via AI-generated content | L1 | Foundational | Build |
| V7.4.1 — Generic error messages | V7 Logging | Validation failures produce generic errors to users — detailed error information logged server-side only | L1 | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Treat all data entering GenAI pipelines as untrusted — validate against a defined schema
- Implement output validation schemas for all model response channels
- Log validation failures with sufficient context for debugging without leaking schema details

**Hardening**
- Apply allowlist-based validation on all NL gateway inputs before model processing
- Implement contract testing on GenAI pipeline interfaces

**Advanced**
- Deploy continuous data quality monitoring across all pipeline stages
- Include data integrity validation in CI/CD gates for pipeline changes

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |
| Cerberus | Open-source | https://github.com/pyeve/cerberus |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Agentic Top 10: ASI02 Tool Misuse
- Other frameworks: ISO 27001 A.8.28 — CIS 16.1 — CWE-20

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange

**Severity:** High

Data exchanged between LLMs and external tools, plugins, or agent subsystems bypasses
standard application security controls — enabling unauthorised data exposure, injection
via tool outputs, or exfiltration through misconfigured plugin channels.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V4.1.1 — Access control on every request | V4 Access Control | Every tool invocation and plugin call authenticated and authorised — no implicit trust between components | L1 | Foundational | Both |
| V9.1.1 — TLS for all connections | V9 Communication | All agent-to-tool and agent-to-plugin communication uses TLS — prevents interception of exchanged data | L1 | Foundational | Both |
| V11.1.4 — Business logic limits on repeated actions | V11 Business Logic | Agent tool invocation frequency limited — prevents runaway tool usage or data exfiltration loops | L2 | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Apply least privilege to all plugin and tool data access
- Validate all tool outputs before they are returned to the model
- Log all tool invocations with input, output, and caller identity

**Hardening**
- Implement per-session tool scope — agents receive only the tools needed for the current task
- Apply schema validation on all plugin input and output channels

**Advanced**
- Deploy behaviour anomaly detection on tool invocation patterns
- Formally verify permitted tool call graphs for high-risk agent workflows

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- Agentic Top 10: ASI02 Tool Misuse, ASI07 Insecure Inter-Agent Communication
- Other frameworks: ISO 27001 A.5.19 — CIS 4.1 — AIUC-1 B006

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High

Absence of data classification and lifecycle management causes over-retention of
sensitive training data, unclear ownership of AI-processed data, and inability to
fulfil deletion obligations under GDPR or other privacy regulations.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V8.1.4 — Sensitive data minimisation | V8 Data Protection | Only data necessary for the defined AI purpose is collected, processed, and retained | L1 | Foundational | Both |
| V8.3.4 — Sensitive data identified and classified | V8 Data Protection | All data entering GenAI systems classified per sensitivity — classification drives handling and retention rules | L2 | Foundational | Both |
| V4.1.5 — Attribute-based access control | V4 Access Control | Data access decisions in RAG and training systems based on data classification attributes | L2 | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Classify all training and RAG data before ingestion — apply retention and handling
  rules based on classification
- Define data lifecycle for all GenAI data stores — including deletion schedules
- Assign data owners for all AI datasets

**Hardening**
- Implement automated data classification tooling on all ingestion pipelines
- Enforce retention policies with automated deletion of data past its retention period

**Advanced**
- Implement machine unlearning to support deletion obligations for training data
- Conduct regular data lineage audits for all GenAI production systems

#### Tools

| Tool | Type | Link |
|---|---|---|
| Apache Atlas | Open-source | https://atlas.apache.org |
| Amundsen | Open-source | https://github.com/amundsen-io/amundsen |

#### Cross-references
- Other frameworks: ISO 27001 A.5.12 — CIS 3.2 — GDPR Art. 5(1)(e) — ENISA L3-GRC

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High

GenAI systems process data in ways that violate GDPR, EU AI Act, HIPAA, PCI DSS,
or other regulatory obligations — through consent failures, cross-border data transfers,
or processing for purposes beyond those disclosed.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V8.3.3 — Consent obtained before PI processing | V8 Data Protection | Lawful basis established for all personal data processed in GenAI training and inference | L1 | Foundational | Both |
| V8.3.10 — Personal data not kept longer than needed | V8 Data Protection | Training data and model outputs containing personal data subject to retention limits | L2 | Foundational | Both |
| V7.2.2 — Audit trail sufficient for compliance | V7 Logging | Logs maintained sufficient to demonstrate regulatory compliance — retained for required periods | L2 | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Map all personal data flows through GenAI systems — document lawful basis for each
- Implement data subject rights (access, deletion, portability) for all GenAI-processed data
- Conduct DPIA (Data Protection Impact Assessment) for all high-risk AI deployments

**Hardening**
- Implement automated compliance monitoring — detect processing beyond declared purpose
- Maintain records of processing activities covering all GenAI data uses

**Advanced**
- Deploy privacy-by-design patterns — federated learning, differential privacy,
  synthetic data — to reduce personal data exposure
- Conduct annual regulatory compliance audit against current AI-specific requirements

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDP | Open-source | https://github.com/opendp/opendp |
| Privado | Open-source | https://github.com/Privado-Inc/privado |

#### Cross-references
- Other frameworks: ISO 27001 A.5.31 — EU AI Act Art. 9-15 — GDPR Art. 35

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Sensitive data embedded in images, audio, video, or documents processed by multimodal
AI is extracted, reconstructed, or disclosed through model outputs — bypassing text-only
DLP controls that do not inspect non-text modalities.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V5.2.5 — Unstructured data sanitised | V5 Validation | All non-text inputs (images, audio, documents) scanned for sensitive content before multimodal model processing | L2 | Hardening | Both |
| V8.1.4 — Sensitive data minimised | V8 Data Protection | Non-text data processed only to the extent necessary — full documents not passed to model when excerpts suffice | L2 | Hardening | Both |
| V12.1.3 — Malicious file detection on upload | V12 Files/Resources | Multimodal inputs scanned for embedded malicious payloads before processing | L2 | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Extend DLP controls to all non-text modalities processed by AI systems
- Implement content scanning for images, audio, and documents before model ingestion

**Hardening**
- Deploy multimodal-aware PII detection covering images, audio transcripts, and documents
- Apply data minimisation — extract and pass only required fields, not full documents

**Advanced**
- Conduct multimodal-specific red team exercises targeting cross-channel disclosure paths
- Implement output filtering for responses derived from multimodal inputs

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| Azure AI Content Safety | Commercial | https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.11 — CIS 3.13 — ENISA L2-DP

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium

Synthetic data generation and anonymisation techniques fail to prevent re-identification
— allowing attackers to reconstruct original PII from synthetic records or to reverse
anonymisation through linkage attacks against other available datasets.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V8.3.4 — Sensitive data classified | V8 Data Protection | Synthetic data classified appropriately — residual re-identification risk assessed and documented | L2 | Hardening | Build |
| V5.2.6 — Defined output structure | V5 Validation | Synthetic data generation outputs validated to confirm absence of original record content | L2 | Hardening | Build |

#### Mitigations by tier

**Foundational**
- Do not treat synthetic data as inherently safe — assess re-identification risk
- Apply k-anonymity (k≥5) or differential privacy to all synthetic datasets before
  use in AI training

**Hardening**
- Test anonymised/synthetic datasets with linkage attacks before use in production
- Document re-identification risk assessment results alongside every synthetic dataset

**Advanced**
- Implement differential privacy (ε ≤ 1.0) for high-sensitivity synthetic data generation
- Conduct quarterly re-identification testing as datasets in the wild evolve

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDP | Open-source | https://github.com/opendp/opendp |
| ARX Anonymisation Tool | Open-source | https://github.com/arx-deidentifier/arx |
| SDV (Synthetic Data Vault) | Open-source | https://github.com/sdv-dev/SDV |

#### Cross-references
- Other frameworks: ISO 27001 A.8.11 — GDPR Recital 26 — ENISA L2-DP

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High

Conversation history, user data, or sensitive context from one session bleeds
into another user's session through shared model state, inadequate context isolation,
or improper cache management — violating data separation and user privacy.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V3.1.1 — Session tokens unique and random | V3 Session Management | Each LLM conversation session identified by a unique, unpredictable token — sessions cannot be guessed or forged | L1 | Foundational | Build |
| V3.3.1 — Sessions invalidated after logout | V3 Session Management | Conversation context fully cleared on session end — no residual context accessible to subsequent sessions | L1 | Foundational | Build |
| V4.1.1 — Access control enforced on every request | V4 Access Control | Context retrieval operations enforce per-user isolation — cross-user context access blocked by default | L1 | Foundational | Build |
| V8.1.3 — Sensitive data not in session storage | V8 Data Protection | Sensitive user data not persisted in shared session or cache layers accessible across users | L1 | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Implement strict session isolation — each user's context window is completely
  isolated from all other sessions
- Clear conversation context on session termination
- Never cache responses or context data in shared layers without per-user namespacing

**Hardening**
- Audit session management logic specifically for AI context persistence bugs
- Implement session isolation tests in CI/CD

**Advanced**
- Deploy context isolation verification as an automated test on every deployment
- Conduct adversarial testing specifically targeting cross-session data leakage

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Burp Suite Community | Open-source | https://portswigger.net/burp/communitydownload |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.3 — CIS 3.3 — CWE-200

---

### DSGAI12 — Unsafe NL Data Gateways

**Severity:** Critical

Natural language interfaces used as gateways to structured data sources (databases,
APIs, filesystems) allow prompt injection or poorly validated NL-to-query translation
to bypass access controls, extract unauthorised data, or corrupt data stores.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V5.1.1 — Allowlist input validation | V5 Validation | NL queries translated by LLMs validated against an allowlist of permitted query patterns before execution | L1 | Foundational | Build |
| V5.3.4 — SQL injection prevention | V5 Validation | LLM-generated SQL parameterised — no direct string interpolation of model output into query execution | L1 | Foundational | Build |
| V4.1.1 — Access control on every request | V4 Access Control | NL gateway enforces the same access control as the underlying data source — no privilege amplification via NL | L1 | Foundational | Build |
| V13.1.1 — API protection against enumeration | V13 API | NL data gateway limits result set size and prevents systematic data enumeration through conversational interface | L2 | Hardening | Build |

#### Mitigations by tier

**Foundational**
- Parameterise all LLM-generated queries — never execute raw model output as SQL,
  NoSQL, or API calls
- Apply the same access control to NL gateways as to the underlying data source
- Log all NL gateway queries with the translated query and user identity

**Hardening**
- Implement query schema allowlisting — limit the tables, fields, and operations
  the NL gateway can generate
- Apply rate limiting and result size limits on all NL data gateway endpoints

**Advanced**
- Conduct adversarial testing specifically targeting NL-to-SQL injection vectors
- Implement query intent verification — flag queries that appear to enumerate
  or extract beyond expected usage patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| SQLFluff | Open-source | https://github.com/sqlfluff/sqlfluff |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM01 Prompt Injection
- Other frameworks: ASVS V5.3 — CWE-89 — OWASP Top 10 A3:2021

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector stores and embedding databases used for RAG lack standard security controls
— allowing unauthorised read access to embeddings, injection of adversarial vectors,
and extraction of sensitive source content through embedding inversion.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V4.1.3 — Deny by default | V4 Access Control | Vector store access defaults to deny — read and write permissions explicitly granted per namespace | L1 | Foundational | Both |
| V6.1.1 — Sensitive data not stored in cleartext | V6 Cryptography | Embedding vectors encrypted at rest — prevents direct extraction and inversion attacks | L2 | Hardening | Both |
| V12.1.1 — File upload validation | V12 Files/Resources | Documents ingested into vector stores validated for content, format, and adversarial patterns | L1 | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Implement RBAC on all vector store namespaces
- Validate and sanitise all content before generating embeddings
- Monitor vector store ingestion for anomalous content patterns

**Hardening**
- Encrypt embedding vectors at rest
- Apply trust-tiered retrieval weighted by source provenance

**Advanced**
- Conduct embedding inversion exercises to validate disclosure boundaries
- Implement differential privacy in embedding generation for sensitive corpora

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant | Open-source | https://qdrant.tech |

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses
- Other frameworks: ISO 27001 A.8.3 — CIS 3.11 — CWE-327

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High

Monitoring, logging, and telemetry systems capture and retain sensitive data from
model interactions — creating high-value targets that expose conversation content,
PII, API keys, and user behaviour to attackers who compromise logging infrastructure.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V7.1.1 — No credential logging | V7 Logging | Credentials, tokens, and API keys not captured in logs — redacted at the telemetry collection layer | L1 | Foundational | Build |
| V7.1.2 — No sensitive data in logs | V7 Logging | PII and sensitive content redacted from logs before storage — logs contain event metadata, not conversation content | L1 | Foundational | Build |
| V8.1.1 — Sensitive data not in URLs | V8 Data Protection | Telemetry pipelines do not transmit sensitive data via URL parameters or unencrypted channels | L1 | Foundational | Build |
| V4.1.1 — Access control on log stores | V4 Access Control | Log and telemetry stores subject to the same access control rigour as production data | L1 | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Redact PII, credentials, and sensitive content from logs at collection time
- Apply access control to logging and monitoring infrastructure as strictly as
  production systems

**Hardening**
- Define a log retention policy — logs retained only for the minimum period required
- Encrypt logs at rest and in transit

**Advanced**
- Implement log integrity monitoring — detect and alert on tampering with audit logs
- Deploy anomaly detection on log access patterns — flag unusual log queries

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| Fluent Bit | Open-source | https://github.com/fluent/fluent-bit |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.15 — CIS 8.2 — ENISA L1-LOG

---

### DSGAI15 — Over-Broad Context Windows

**Severity:** High

Excessively large context windows aggregate data from multiple sources and trust
domains into a single flat namespace — enabling cross-source data leakage, context
poisoning, and disclosure of information from one user's or system's context to another.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V4.1.3 — Deny by default access control | V4 Access Control | Context window population controlled by explicit allow rules — no implicit inclusion of all available context | L1 | Foundational | Build |
| V8.1.4 — Data minimisation | V8 Data Protection | Context window populated with minimum data necessary for the task — not maximum available data | L1 | Foundational | Build |
| V3.1.1 — Session isolation | V3 Session Management | Data from different user sessions never co-mingled in a shared context window | L1 | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Enforce data minimisation on context window population — include only what
  is strictly necessary for the current task
- Maintain trust-domain separation — data from different sources tagged with
  source trust level and handled accordingly
- Set explicit context window size limits per deployment configuration

**Hardening**
- Implement context window auditing — log what data is included in each inference
  call for post-incident analysis
- Apply context redaction before passing to model for data classes that should
  not be included

**Advanced**
- Deploy context window policy enforcement as an independent control layer
- Red team context window population logic for cross-source leakage

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure, LLM07 System Prompt Leakage
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3 — CIS 3.3 — ENISA L2-DP

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High

Browser-integrated and endpoint AI assistants access data beyond their declared
scope — reading clipboard, browsing history, files, or other applications without
explicit per-action authorisation — and may exfiltrate this data to remote model providers.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V4.1.2 — Least privilege | V4 Access Control | Browser and endpoint AI assistants operate with minimum permissions — no implicit access to OS resources, files, or other applications | L1 | Foundational | Both |
| V11.1.5 — Business logic prevents excess data access | V11 Business Logic | Endpoint assistant functionality restricted to declared scope — no background data collection beyond stated purpose | L2 | Foundational | Both |
| V1.1.2 — Secure architecture and design | V1 Architecture | Endpoint AI components subject to the same architectural security review as other privileged applications | L2 | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Restrict endpoint AI assistant OS permissions to the minimum required for
  declared functionality
- Review and restrict browser extension permissions before organisational deployment
- Include endpoint AI tools in application security review process

**Hardening**
- Monitor endpoint AI tool network activity — flag data transmission to unexpected destinations
- Implement application allowlisting to control which AI assistants can run on managed endpoints

**Advanced**
- Conduct security assessment of all endpoint AI tools before enterprise deployment
- Deploy endpoint DLP specifically covering AI assistant data exfiltration vectors

#### Tools

| Tool | Type | Link |
|---|---|---|
| CrowdStrike Falcon | Commercial | https://www.crowdstrike.com |
| osquery | Open-source | https://github.com/osquery/osquery |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI10 Rogue Agents
- Other frameworks: ISO 27001 A.8.1 — CIS 2.6 — ENISA L1-EP

---

### DSGAI17 — Data Availability & Resilience Failures

**Severity:** High

GenAI systems fail to maintain availability of training data, RAG corpora, and
model inference due to inadequate backup, recovery, and resilience controls — causing
service outages, loss of training history, or inability to recover from data corruption events.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V11.1.7 — Anti-automation controls | V11 Business Logic | GenAI services protected against automated abuse that could exhaust resources and cause availability failures | L2 | Foundational | Both |
| V13.1.2 — API throttling | V13 API | Model inference APIs throttled to prevent demand spikes from causing availability failures | L1 | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Implement backup and recovery for all GenAI data stores — training data,
  vector stores, fine-tuning datasets
- Define RTO and RPO for GenAI services — test recovery procedures regularly
- Implement rate limiting and quota management on model inference endpoints

**Hardening**
- Deploy multi-region replication for production vector stores and training data
- Implement circuit breakers on all model inference pipelines

**Advanced**
- Conduct chaos engineering exercises specifically targeting GenAI data store availability
- Implement automated failover for critical inference endpoints

#### Tools

| Tool | Type | Link |
|---|---|---|
| Velero | Open-source | https://github.com/vmware-tanzu/velero |
| Chaos Monkey | Open-source | https://github.com/Netflix/chaosmonkey |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: ISO 27001 A.5.30 — CIS 11.1 — ENISA L1-RES

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High

Attackers query GenAI systems with crafted inputs to reconstruct training data,
infer membership of individuals in training sets, or reconstruct sensitive source
content from model outputs — even when the data was never directly disclosed.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V8.3.4 — Sensitive data identified | V8 Data Protection | Training datasets containing personal data identified — inference attack risk assessed before deployment | L2 | Hardening | Both |
| V6.1.1 — Sensitive data not stored in cleartext | V6 Cryptography | Model weights and embedding vectors stored encrypted — reduces utility of extraction attacks | L2 | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Apply differential privacy during training to limit model memorisation of
  individual training records
- Monitor model query patterns for membership inference attack signatures

**Hardening**
- Conduct membership inference red team exercises before production deployment
- Implement output confidence score suppression — limit the information available
  to guide inference attacks

**Advanced**
- Apply machine unlearning to remove memorised sensitive records after training
- Implement query-level anomaly detection to flag systematic inference attack patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDP | Open-source | https://github.com/opendp/opendp |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.11 — CWE-200 — ENISA L2-ADV

---

### DSGAI19 — Human-in-Loop & Labeler Overexposure

**Severity:** Medium

Human reviewers, labellers, and RLHF annotators are exposed to sensitive or harmful
content during the AI development lifecycle without adequate controls — creating
data handling risks, privacy violations, and welfare concerns for annotation workers.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V4.1.2 — Least privilege | V4 Access Control | Human reviewers access only the data necessary for their annotation task — no broader dataset access | L1 | Foundational | Both |
| V8.3.3 — Consent for personal data processing | V8 Data Protection | Data subjects whose data is reviewed by human annotators informed and consented per applicable law | L1 | Foundational | Both |
| V2.1.1 — Strong authentication | V2 Authentication | Annotation platform access requires strong authentication — labeller access to sensitive data is audited | L2 | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Apply data minimisation to annotation tasks — redact sensitive fields not needed for labelling
- Restrict labeller access to the minimum dataset scope required for the task
- Audit labeller access to sensitive content

**Hardening**
- Implement harmful content warning systems for labellers exposed to unsafe outputs
- Define and enforce data handling agreements with third-party annotation providers

**Advanced**
- Apply automated pre-filtering to reduce human exposure to the most harmful content
- Conduct regular privacy impact assessments on annotation workflows

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| Label Studio | Open-source | https://github.com/HumanSignal/label-studio |

#### Cross-references
- Other frameworks: ISO 27001 A.5.20 — GDPR Art. 28 — ENISA L3-GRC

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High

Attackers use model extraction techniques — crafted queries to reconstruct model
behaviour — to steal proprietary model capabilities, create functional replicas,
or identify exploitable decision boundaries without access to model weights.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V4.1.1 — Access control per request | V4 Access Control | Model API access authenticated and rate-limited — prevents systematic extraction queries | L1 | Foundational | Both |
| V8.1.4 — Data minimisation in responses | V8 Data Protection | Model confidence scores and logits not exposed in API responses where not required — limits extraction attack signal | L2 | Hardening | Both |
| V10.2.2 — Component integrity checking | V10 Malicious Code | Model artefacts protected with integrity verification — detect unauthorised copies or modifications | L2 | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Implement rate limiting and query monitoring on all model inference APIs
- Log unusual query patterns that may indicate systematic extraction attempts

**Hardening**
- Suppress confidence scores and logit outputs in API responses where not functionally required
- Apply query diversity detection — flag accounts issuing highly systematic or structured queries

**Advanced**
- Implement model watermarking — embed verifiable fingerprints in model outputs
  detectable in extracted replicas
- Deploy extraction attack detection using query pattern analysis

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| ART (Adversarial Robustness Toolbox) | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |

#### Cross-references
- Other frameworks: ISO 27001 A.5.12 — CIS 4.2 — ENISA L2-ADV

---

### DSGAI21 — Disinformation via Data Poisoning

**Severity:** High

Attackers inject disinformation into training datasets, RAG corpora, or fine-tuning
data to cause models to systematically generate false, biased, or misleading outputs —
targeting specific topics, entities, or user segments with malicious intent.

#### ASVS mapping

| Requirement | Chapter | Description | Level | Tier | Scope |
|---|---|---|---|---|---|
| V5.1.3 — Server-side input validation | V5 Validation | Training data ingestion validates content against factual integrity checks and anomaly patterns | L2 | Hardening | Both |
| V11.1.4 — Enforce business logic limits | V11 Business Logic | Model output validation detects systematic deviation from factual baselines — triggers review before serving | L2 | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Implement provenance tracking for all RAG corpus content — source and last-verified
  date recorded for all documents
- Validate training data for factual consistency before use

**Hardening**
- Monitor production model outputs for systematic factual drift compared to
  established baselines
- Implement source diversity requirements for high-stakes RAG corpora

**Advanced**
- Deploy automated fact-checking against authoritative sources for high-risk output
  domains
- Conduct targeted red team exercises injecting disinformation into RAG corpora
  to validate detection controls

#### Tools

| Tool | Type | Link |
|---|---|---|
| Cleanlab | Open-source | https://github.com/cleanlab/cleanlab |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning, LLM09 Misinformation
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0045 — CIS 7.1 — EU AI Act Art. 13

---

## Implementation priority

| Phase | DSGAI entries | ASVS focus | Rationale |
|---|---|---|---|
| 1 — Do now | DSGAI01, DSGAI02, DSGAI12 | V4, V5, V8 | Critical severity — access control, input validation, data protection |
| 2 — This sprint | DSGAI04, DSGAI11, DSGAI15 | V3, V5, V10 | Poisoning and context isolation close the next-highest risk paths |
| 3 — This quarter | DSGAI03, DSGAI05, DSGAI06, DSGAI07 | V1, V7, V11 | Data governance, architecture, and tool exchange |
| 4 — Ongoing | DSGAI08–10, DSGAI13–21 | V6, V7, V8, V13 | Compliance, resilience, inference privacy, and advanced hardening |

---

## References

- [OWASP ASVS 4.0.3](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [OWASP AIVSS](https://aivss.owasp.org)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-27 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
