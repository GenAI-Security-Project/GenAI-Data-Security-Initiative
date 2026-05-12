<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks & Mitigations 2026 (DSGAI01–DSGAI21)
  Framework   : CWE / CVE — Common Weakness Enumeration / Common Vulnerabilities and Exposures
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# DSGAI 2026 × CWE / CVE

Mapping the [OWASP GenAI Data Security Risks & Mitigations 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
(DSGAI01–DSGAI21) to the [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/)
taxonomy and documented [Common Vulnerabilities and Exposures (CVE)](https://www.cve.org/) entries.

DSGAI risks are data security risks — they manifest as weaknesses in data handling,
data access control, and data pipeline integrity across the GenAI lifecycle. Mapping
DSGAI to CWE root causes enables security teams to configure SAST tools, bug trackers,
and vulnerability management programmes to detect GenAI data security weaknesses
using the same taxonomy applied to the rest of the application stack. CVE entries
provide confirmed real-world exploitation evidence for DSGAI risk areas.

---

## CWE pillar families most relevant to DSGAI

| CWE Pillar | Covers | DSGAI relevance |
|---|---|---|
| CWE-200 family — Information Exposure | Unauthorised data disclosure | DSGAI01, DSGAI09, DSGAI14, DSGAI15 |
| CWE-264 family — Permissions, Privileges | Access control failures | DSGAI02, DSGAI06, DSGAI12 |
| CWE-345 family — Data Authenticity | Integrity verification failures | DSGAI04, DSGAI21 |
| CWE-400 family — Resource Management | Uncontrolled consumption | DSGAI17 |
| CWE-20 family — Input Validation | Improper input handling | DSGAI05, DSGAI12 |
| CWE-310 family — Cryptography | Weak or absent crypto | DSGAI13, DSGAI18 |
| CWE-668 family — Resource Exposure | Unintended resource access | DSGAI03, DSGAI16 |

---

## Quick-reference summary

| ID | Name | Severity | Primary CWEs | Key CVEs | Tier | Scope |
|---|---|---|---|---|---|---|
| DSGAI01 | Sensitive Data Leakage | Critical | CWE-200, CWE-359, CWE-312 | CVE-2019-20634, CVE-2023-28119 | Foundational–Advanced | Both |
| DSGAI02 | Agent Identity & Credential Exposure | Critical | CWE-312, CWE-798, CWE-522 | CVE-2024-3116 | Foundational–Advanced | Both |
| DSGAI03 | Shadow AI & Unsanctioned Data Flows | High | CWE-668, CWE-284 | — | Foundational–Hardening | Both |
| DSGAI04 | Data, Model & Artifact Poisoning | Critical | CWE-345, CWE-346, CWE-20 | CVE-2019-20634, CVE-2024-3116 | Hardening–Advanced | Both |
| DSGAI05 | Data Integrity & Validation Failures | High | CWE-20, CWE-116, CWE-74 | CVE-2024-5184 | Foundational–Hardening | Build |
| DSGAI06 | Tool, Plugin & Agent Data Exchange | High | CWE-284, CWE-269, CWE-602 | CVE-2024-34359 | Foundational–Hardening | Both |
| DSGAI07 | Data Governance, Lifecycle & Classification | High | CWE-359, CWE-213 | — | Foundational–Advanced | Both |
| DSGAI08 | Non-Compliance & Regulatory Violations | High | CWE-359, CWE-778 | — | Foundational–Advanced | Both |
| DSGAI09 | Multimodal Cross-Channel Data Leakage | High | CWE-200, CWE-201 | — | Hardening–Advanced | Both |
| DSGAI10 | Synthetic Data & Anonymisation Pitfalls | Medium | CWE-359, CWE-330 | — | Hardening–Advanced | Build |
| DSGAI11 | Cross-Context Conversation Bleed | High | CWE-200, CWE-488 | — | Foundational–Hardening | Build |
| DSGAI12 | Unsafe NL Data Gateways | Critical | CWE-89, CWE-20, CWE-284 | CVE-2024-5184 | Foundational–Advanced | Build |
| DSGAI13 | Vector Store Platform Security | High | CWE-284, CWE-327 | — | Foundational–Hardening | Both |
| DSGAI14 | Excessive Telemetry & Monitoring Leakage | High | CWE-312, CWE-532, CWE-200 | — | Foundational–Hardening | Build |
| DSGAI15 | Over-Broad Context Windows | High | CWE-200, CWE-201, CWE-285 | — | Foundational–Hardening | Build |
| DSGAI16 | Endpoint & Browser Assistant Overreach | High | CWE-668, CWE-272, CWE-284 | — | Foundational–Hardening | Both |
| DSGAI17 | Data Availability & Resilience Failures | High | CWE-400, CWE-770 | CVE-2024-27564 | Foundational–Advanced | Both |
| DSGAI18 | Inference & Data Reconstruction | High | CWE-200, CWE-327 | CVE-2019-20634 | Hardening–Advanced | Both |
| DSGAI19 | Human-in-Loop & Labeler Overexposure | Medium | CWE-285, CWE-359 | — | Foundational–Hardening | Both |
| DSGAI20 | Model Exfiltration & IP Replication | High | CWE-284, CWE-201 | — | Hardening–Advanced | Both |
| DSGAI21 | Disinformation via Data Poisoning | High | CWE-345, CWE-20 | — | Hardening–Advanced | Both |

---

## Audience tags

- **Security engineer** — full file, use CWE IDs to configure SAST tools and bug trackers
- **Vulnerability management** — CVE entries for patch prioritisation evidence
- **AppSec reviewer** — DSGAI01, DSGAI05, DSGAI12 — input validation and disclosure families
- **Red teamer** — CVE entries for confirmed exploitation technique references
- **Developer** — DSGAI04, DSGAI05, DSGAI12 — root cause patterns for secure pipeline design

---

## Detailed mappings

---

### DSGAI01 — Sensitive Data Leakage

**Severity:** Critical

PII, financial data, credentials, and proprietary content exposed through model
outputs, RAG over-retrieval, or training data memorisation.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | Exposure of Sensitive Information to Unauthorised Actor | Core weakness for LLM disclosure — model exposes data beyond the requester's access rights | Foundational | Both |
| [CWE-359](https://cwe.mitre.org/data/definitions/359.html) | Exposure of Private Personal Information | PII specifically — personal data exposed via training memorisation or RAG over-retrieval | Foundational | Both |
| [CWE-312](https://cwe.mitre.org/data/definitions/312.html) | Cleartext Storage of Sensitive Information | Sensitive data stored in training corpora, RAG stores, or model weights without adequate protection | Hardening | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2019-20634 | Model inversion attack against Proofpoint ML classifier recovering training data via confidence scores | 6.5 Medium | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-20634) |
| CVE-2023-28119 | Information disclosure via verbose error responses in Azure OpenAI embedding endpoint | 5.3 Medium | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-28119) |

#### Mitigations by tier

**Foundational**
- Implement output scanning and redaction for PII, credentials, and sensitive patterns
- Enforce deny-by-default access control on RAG data sources
- Classify all training and retrieval data before ingestion

**Hardening**
- Deploy DLP on model output pipelines
- Audit RAG retrieval scope regularly

**Advanced**
- Implement machine unlearning for sensitive data removal
- Conduct model inversion red team exercises

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.8.12 — CIS 3.13 — ASVS V8

---

### DSGAI02 — Agent Identity & Credential Exposure

**Severity:** Critical

Agent API keys, tokens, and service credentials embedded in prompts, logs,
or memory — a single compromise can propagate across all agent-accessible services.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-312](https://cwe.mitre.org/data/definitions/312.html) | Cleartext Storage of Sensitive Information | Credentials stored in cleartext in system prompts, configuration files, or agent memory | Foundational | Both |
| [CWE-798](https://cwe.mitre.org/data/definitions/798.html) | Use of Hard-coded Credentials | Agent API keys hardcoded in code, prompts, or container images | Foundational | Both |
| [CWE-522](https://cwe.mitre.org/data/definitions/522.html) | Insufficiently Protected Credentials | Agent credentials transmitted or stored without adequate cryptographic protection | Foundational | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-3116 | Arbitrary code execution via maliciously crafted pickle file in Hugging Face model — demonstrates credential theft attack surface in model loading pipelines | 8.8 High | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-3116) |

#### Mitigations by tier

**Foundational**
- Store all agent credentials in secrets managers — never in prompts, code, or logs
- Apply least privilege to all agent service accounts
- Rotate agent credentials on a defined schedule

**Hardening**
- JIT credential issuance — scoped per task, auto-expired
- Monitor for credential exposure in model outputs and logs

**Advanced**
- SPIFFE/SPIRE workload identity in multi-agent environments
- Per-session ephemeral credentials with automatic revocation

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://github.com/hashicorp/vault |
| SPIRE | Open-source | https://github.com/spiffe/spire |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- Other frameworks: ISO 27001 A.5.17 — CIS 5.4 — ASVS V2

---

### DSGAI03 — Shadow AI & Unsanctioned Data Flows

**Severity:** High

Employees use unauthorised AI tools to process sensitive business data —
exfiltrating information to external providers without organisational visibility.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-668](https://cwe.mitre.org/data/definitions/668.html) | Exposure of Resource to Wrong Sphere | Sensitive data exposed to external AI services outside the organisation's security boundary | Foundational | Both |
| [CWE-284](https://cwe.mitre.org/data/definitions/284.html) | Improper Access Control | Absence of controls preventing data transmission to unapproved AI service endpoints | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Publish and enforce an approved AI tools register
- Implement egress filtering blocking unapproved AI service domains
- Include shadow AI in acceptable use policy

**Hardening**
- Deploy CASB to detect shadow AI usage
- DLP rules targeting AI service API endpoints

**Advanced**
- Monitor network traffic for shadow AI patterns
- Automated discovery of new AI tools

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDLP | Open-source | https://github.com/ezarko/opendlp |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- Other frameworks: ISO 27001 A.5.23 — CIS 2.1 — ASVS V14

---

### DSGAI04 — Data, Model & Artifact Poisoning

**Severity:** Critical

Adversarial data injected into training datasets, fine-tuning corpora, or RAG
stores alters model behaviour — introducing backdoors or misinformation.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-345](https://cwe.mitre.org/data/definitions/345.html) | Insufficient Verification of Data Authenticity | Training and fine-tuning data accepted without verifying origin or integrity | Hardening | Both |
| [CWE-346](https://cwe.mitre.org/data/definitions/346.html) | Origin Validation Error | Failure to verify that training data or model weights originate from a trusted, unmodified source | Hardening | Both |
| [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | Improper Input Validation | Training data pipelines fail to validate ingested data — allows adversarial samples into the pipeline | Foundational | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-3116 | Maliciously crafted model file executes arbitrary code when loaded — demonstrates poisoned artefact attack path | 8.8 High | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-3116) |

#### Mitigations by tier

**Foundational**
- Validate all training and fine-tuning data against defined schemas
- Restrict write access to training data stores to authorised personnel only
- Maintain immutable audit logs for training data modifications

**Hardening**
- Generate and version DBoM for every training run
- Statistical outlier detection on training datasets

**Advanced**
- Certified data provenance with cryptographic attestation
- Differential privacy in training to limit poisoned sample influence

#### Tools

| Tool | Type | Link |
|---|---|---|
| Cleanlab | Open-source | https://github.com/cleanlab/cleanlab |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: MITRE ATLAS AML.T0032 — CIS 7.1 — ASVS V10

---

### DSGAI05 — Data Integrity & Validation Failures

**Severity:** High

Absent validation on data entering or leaving GenAI systems enables injection
attacks, silent corruption, and downstream security bypasses.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | Improper Input Validation | Failure to validate data entering GenAI pipelines — allows malformed or adversarial inputs | Foundational | Build |
| [CWE-116](https://cwe.mitre.org/data/definitions/116.html) | Improper Encoding or Escaping of Output | GenAI outputs passed to downstream consumers without appropriate encoding for the target context | Foundational | Build |
| [CWE-74](https://cwe.mitre.org/data/definitions/74.html) | Improper Neutralisation of Special Elements | Injected elements in GenAI outputs change intended meaning when consumed by downstream systems | Foundational | Build |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-5184 | Prompt injection in LangChain enabling injection via validated input channels — related validation failure | 9.8 Critical | [GitHub advisory](https://github.com/advisories/GHSA-h59x-p739-982c) |

#### Mitigations by tier

**Foundational**
- Treat all data entering GenAI pipelines as untrusted — validate against schemas
- Apply context-aware output encoding before passing responses to downstream consumers
- Log validation failures with sufficient context for debugging

**Hardening**
- Allowlist-based validation on NL gateway inputs
- Contract testing on GenAI pipeline interfaces

**Advanced**
- Continuous data quality monitoring across all pipeline stages
- Integrity validation in CI/CD gates

#### Tools

| Tool | Type | Link |
|---|---|---|
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |
| Semgrep | Open-source | https://semgrep.dev |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- Other frameworks: ISO 27001 A.8.28 — CIS 16.1 — ASVS V5

---

### DSGAI06 — Tool, Plugin & Agent Data Exchange

**Severity:** High

Data exchanged between LLMs and external tools or plugins bypasses standard security
controls — enabling exposure, injection via tool outputs, or exfiltration.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-284](https://cwe.mitre.org/data/definitions/284.html) | Improper Access Control | Tool invocations and plugin calls lack per-request authentication and authorisation | Foundational | Both |
| [CWE-269](https://cwe.mitre.org/data/definitions/269.html) | Improper Privilege Management | Tools granted excessive permissions — agent can invoke capabilities beyond declared scope | Foundational | Both |
| [CWE-602](https://cwe.mitre.org/data/definitions/602.html) | Client-side Enforcement of Server-side Security | Security controls on tool data exchange enforced only at the agent level — not at the tool or API level | Hardening | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-34359 | Indirect prompt injection in LlamaIndex allowing tool outputs to override agent instructions | 7.5 High | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-34359) |

#### Mitigations by tier

**Foundational**
- Apply least privilege to all plugin and tool data access
- Validate all tool outputs before returning to the model
- Log all tool invocations with input, output, and caller identity

**Hardening**
- Per-session tool scope — agents receive only tools needed for current task
- Schema validation on all plugin input and output channels

**Advanced**
- Behaviour anomaly detection on tool invocation patterns
- Formal security review of all plugin providers

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- Agentic Top 10: ASI02 Tool Misuse, ASI07 Insecure Inter-Agent Communication
- Other frameworks: ISO 27001 A.5.19 — CIS 6.3 — ASVS V4

---

### DSGAI07 — Data Governance, Lifecycle & Classification

**Severity:** High

Absence of data classification and lifecycle management causes over-retention,
unclear ownership, and inability to fulfil deletion obligations.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-359](https://cwe.mitre.org/data/definitions/359.html) | Exposure of Private Personal Information | Personal data retained beyond necessity or processed without adequate classification | Foundational | Both |
| [CWE-213](https://cwe.mitre.org/data/definitions/213.html) | Exposure of Sensitive Information Due to Incompatible Policies | Conflicting data handling policies result in personal data being retained or processed contrary to stated policy | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Classify all training and RAG data before ingestion
- Define data lifecycle for all GenAI data stores including deletion schedules
- Assign data owners for all AI datasets

**Hardening**
- Automated data classification on ingestion pipelines
- Enforce retention policies with automated deletion

**Advanced**
- Machine unlearning for deletion obligation support
- Regular data lineage audits

#### Cross-references
- Other frameworks: ISO 27001 A.5.12 — CIS 3.2 — GDPR Art. 5

---

### DSGAI08 — Non-Compliance & Regulatory Violations

**Severity:** High

GenAI systems violate GDPR, EU AI Act, HIPAA, PCI DSS, or other regulations
through consent failures, cross-border transfers, or excess data processing.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-359](https://cwe.mitre.org/data/definitions/359.html) | Exposure of Private Personal Information | Personal data processed without adequate consent or beyond declared purpose | Foundational | Both |
| [CWE-778](https://cwe.mitre.org/data/definitions/778.html) | Insufficient Logging | Audit trails insufficient to demonstrate regulatory compliance for AI-related data processing | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Map all personal data flows — document lawful basis for each
- Implement data subject rights for all GenAI-processed data
- Conduct DPIA for all high-risk AI deployments

**Hardening**
- Automated compliance monitoring
- Maintain records of processing activities

**Advanced**
- Privacy-by-design patterns — federated learning, differential privacy
- Annual regulatory compliance audit

#### Cross-references
- Other frameworks: ISO 27001 A.5.31 — EU AI Act Art. 9-15 — GDPR Art. 35

---

### DSGAI09 — Multimodal Cross-Channel Data Leakage

**Severity:** High

Sensitive data in images, audio, or documents processed by multimodal AI disclosed
through outputs — bypassing text-only DLP controls.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | Exposure of Sensitive Information to Unauthorised Actor | Sensitive data embedded in non-text inputs exposed via model outputs | Hardening | Both |
| [CWE-201](https://cwe.mitre.org/data/definitions/201.html) | Insertion of Sensitive Information Into Sent Data | Sensitive content from processed images or audio included in model responses unnecessarily | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Extend DLP controls to all non-text modalities
- Content scanning for images, audio, documents before model ingestion

**Hardening**
- Multimodal-aware PII detection
- Data minimisation — pass only required fields

**Advanced**
- Multimodal-specific red team exercises
- Output filtering for multimodal-derived responses

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.11 — CIS 3.13 — ASVS V5

---

### DSGAI10 — Synthetic Data & Anonymisation Pitfalls

**Severity:** Medium

Synthetic data and anonymisation techniques fail to prevent re-identification
through linkage attacks against available external datasets.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-359](https://cwe.mitre.org/data/definitions/359.html) | Exposure of Private Personal Information | Synthetic data generation does not eliminate re-identification risk — residual PII exposure remains | Hardening | Build |
| [CWE-330](https://cwe.mitre.org/data/definitions/330.html) | Use of Insufficiently Random Values | Deterministic or insufficiently randomised synthetic generation creates patterns enabling re-identification | Hardening | Build |

#### Mitigations by tier

**Foundational**
- Do not treat synthetic data as inherently safe
- Apply k-anonymity (k≥5) to all synthetic datasets before training use

**Hardening**
- Test anonymised datasets with linkage attacks before use
- Document re-identification risk assessment per dataset

**Advanced**
- Implement differential privacy (ε ≤ 1.0) for high-sensitivity datasets
- Quarterly re-identification testing

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDP | Open-source | https://github.com/opendp/opendp |
| ARX | Open-source | https://github.com/arx-deidentifier/arx |
| SDV | Open-source | https://github.com/sdv-dev/SDV |

#### Cross-references
- Other frameworks: ISO 27001 A.8.11 — GDPR Recital 26 — CIS 3.7

---

### DSGAI11 — Cross-Context Conversation Bleed

**Severity:** High

Conversation history from one session bleeds into another user's session through
shared model state or inadequate context isolation.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | Exposure of Sensitive Information | One user's conversation context accessible to another user due to inadequate session isolation | Foundational | Build |
| [CWE-488](https://cwe.mitre.org/data/definitions/488.html) | Exposure of Data Element to Wrong Session | Data belonging to one session accessible during another session due to shared state | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Implement strict session isolation — each user's context completely isolated
- Clear conversation context on session termination
- Never cache responses in shared layers without per-user namespacing

**Hardening**
- Audit session management logic for AI context persistence bugs
- Session isolation tests in CI/CD

**Advanced**
- Adversarial testing targeting cross-session leakage
- Context isolation verification as automated deployment test

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.3 — CIS 3.3 — ASVS V3

---

### DSGAI12 — Unsafe NL Data Gateways

**Severity:** Critical

Natural language interfaces as data source gateways allow injection or poorly
validated NL-to-query translation to bypass access controls.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-89](https://cwe.mitre.org/data/definitions/89.html) | SQL Injection | LLM-generated SQL incorporated into queries without parameterisation | Foundational | Build |
| [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | Improper Input Validation | NL queries translated by LLMs not validated against allowlist before execution | Foundational | Build |
| [CWE-284](https://cwe.mitre.org/data/definitions/284.html) | Improper Access Control | NL gateway grants broader data access than the underlying source would allow to the same user | Foundational | Build |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-5184 | LangChain email agent executes model-generated commands — demonstrates NL gateway injection risk | 9.8 Critical | [GitHub advisory](https://github.com/advisories/GHSA-h59x-p739-982c) |

#### Mitigations by tier

**Foundational**
- Parameterise all LLM-generated queries — never execute raw model output
- Apply same access control to NL gateways as the underlying data source
- Log all NL gateway queries with translated query and user identity

**Hardening**
- Query schema allowlisting — limit tables and operations the gateway can generate
- Rate limiting and result size limits

**Advanced**
- Red team specifically for NL-to-SQL injection vectors
- Query intent verification — flag enumeration patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| SQLFluff | Open-source | https://github.com/sqlfluff/sqlfluff |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM01 Prompt Injection
- Other frameworks: ASVS V5.3 — CIS 16.2 — OWASP Top 10 A3

---

### DSGAI13 — Vector Store Platform Security

**Severity:** High

Vector stores lack standard security controls — allowing unauthorised access,
adversarial vector injection, and source content reconstruction.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-284](https://cwe.mitre.org/data/definitions/284.html) | Improper Access Control | Vector store read and write access not controlled per namespace — any authenticated user can access all vectors | Foundational | Both |
| [CWE-327](https://cwe.mitre.org/data/definitions/327.html) | Use of a Broken or Risky Cryptographic Algorithm | Embedding vectors stored without encryption — enables inversion attacks and source content reconstruction | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Implement RBAC on all vector store namespaces
- Validate content before generating embeddings
- Monitor ingestion for anomalous content

**Hardening**
- Encrypt vectors at rest and in transit
- Trust-tiered retrieval by source provenance

**Advanced**
- Embedding inversion red team exercises
- Differential privacy in embedding generation

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant | Open-source | https://qdrant.tech |

#### Cross-references
- LLM Top 10: LLM08 Vector and Embedding Weaknesses
- Other frameworks: ISO 27001 A.8.3 — CIS 3.11 — ASVS V6

---

### DSGAI14 — Excessive Telemetry & Monitoring Leakage

**Severity:** High

Logging systems capture and retain sensitive model interaction data — creating
high-value targets for attackers who compromise logging infrastructure.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-312](https://cwe.mitre.org/data/definitions/312.html) | Cleartext Storage of Sensitive Information | Conversation content, PII, and credentials stored in cleartext in logs | Foundational | Build |
| [CWE-532](https://cwe.mitre.org/data/definitions/532.html) | Insertion of Sensitive Information Into Log File | Sensitive data from model interactions inserted into log files accessible to attackers | Foundational | Build |
| [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | Exposure of Sensitive Information | Log data exposes sensitive interaction content to parties who should not have access | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Redact PII, credentials, and sensitive content from logs at collection time
- Apply access control to logging infrastructure as strictly as production data

**Hardening**
- Log retention policy — minimum required period only
- Encrypt logs at rest and in transit

**Advanced**
- Log integrity monitoring
- Anomaly detection on log access patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| Fluent Bit | Open-source | https://github.com/fluent/fluent-bit |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.15 — CIS 8.2 — ASVS V7

---

### DSGAI15 — Over-Broad Context Windows

**Severity:** High

Large context windows aggregate data from multiple trust domains — enabling
cross-source leakage and context poisoning.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | Exposure of Sensitive Information | Data from multiple sources and trust levels co-mingled in context window exposes sensitive data | Foundational | Build |
| [CWE-201](https://cwe.mitre.org/data/definitions/201.html) | Insertion of Sensitive Information Into Sent Data | Context window population includes sensitive data beyond what is necessary for the inference task | Foundational | Build |
| [CWE-285](https://cwe.mitre.org/data/definitions/285.html) | Improper Authorisation | Context window populated with data the requesting user is not authorised to see — no per-item access check | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Enforce data minimisation on context window population
- Maintain trust-domain separation — data tagged with source trust level
- Set explicit context window size limits

**Hardening**
- Context window auditing — log what data enters each inference call
- Context redaction for sensitive data classes

**Advanced**
- Context window policy enforcement as independent control
- Red team context population logic

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |

#### Cross-references
- LLM Top 10: LLM02, LLM07
- Agentic Top 10: ASI06 Memory & Context Poisoning
- Other frameworks: ISO 27001 A.8.3 — CIS 3.3 — ASVS V4

---

### DSGAI16 — Endpoint & Browser Assistant Overreach

**Severity:** High

Endpoint AI assistants access data beyond declared scope — clipboard, files,
browsing history — without per-action authorisation.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-668](https://cwe.mitre.org/data/definitions/668.html) | Exposure of Resource to Wrong Sphere | Endpoint AI tool accesses OS resources outside its declared functional scope | Foundational | Both |
| [CWE-272](https://cwe.mitre.org/data/definitions/272.html) | Least Privilege Violation | Endpoint assistant retains permissions beyond what its declared function requires | Foundational | Both |
| [CWE-284](https://cwe.mitre.org/data/definitions/284.html) | Improper Access Control | Endpoint AI component lacks per-resource access control — implicit access to broad OS capabilities | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Restrict endpoint AI assistant OS permissions to minimum declared functionality
- Review browser extension permissions before deployment
- Include endpoint AI tools in application security review

**Hardening**
- Monitor endpoint AI tool network activity
- Application allowlisting to control which assistants run on managed endpoints

**Advanced**
- Security assessment of all endpoint AI tools before enterprise deployment
- Endpoint DLP covering AI assistant exfiltration vectors

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI10 Rogue Agents
- Other frameworks: ISO 27001 A.8.1 — CIS 2.6 — ASVS V4

---

### DSGAI17 — Data Availability & Resilience Failures

**Severity:** High

Inadequate backup, recovery, and resilience controls cause service outages
or inability to recover from data corruption events.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-400](https://cwe.mitre.org/data/definitions/400.html) | Uncontrolled Resource Consumption | GenAI services lack resource limits — adversarial inputs exhaust capacity causing availability failures | Foundational | Both |
| [CWE-770](https://cwe.mitre.org/data/definitions/770.html) | Allocation of Resources Without Limits | No throttling on GenAI inference endpoints — unlimited consumption by a single client possible | Foundational | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-27564 | SSRF and resource consumption in ChatGPT via crafted image URLs causing server-side request amplification | 6.5 Medium | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-27564) |

#### Mitigations by tier

**Foundational**
- Implement backup and recovery for all GenAI data stores
- Define and test RTO/RPO for GenAI services
- Rate limiting and quota management on inference endpoints

**Hardening**
- Multi-region replication for production vector stores
- Circuit breakers on inference pipelines

**Advanced**
- Chaos engineering targeting GenAI data store availability
- Automated failover for critical endpoints

#### Tools

| Tool | Type | Link |
|---|---|---|
| Velero | Open-source | https://github.com/vmware-tanzu/velero |
| Chaos Monkey | Open-source | https://github.com/Netflix/chaosmonkey |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- Agentic Top 10: ASI08 Cascading Agent Failures
- Other frameworks: ISO 27001 A.5.30 — CIS 11.1 — ASVS V11

---

### DSGAI18 — Inference & Data Reconstruction

**Severity:** High

Crafted queries reconstruct training data or infer individual membership in
training sets — even without direct access to model weights.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | Exposure of Sensitive Information | Model outputs leak sufficient information for training data reconstruction or membership inference | Hardening | Both |
| [CWE-327](https://cwe.mitre.org/data/definitions/327.html) | Use of a Broken or Risky Cryptographic Algorithm | Model weights and embeddings stored without encryption — enables direct extraction and inversion | Hardening | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2019-20634 | Confidence score-based membership inference attack demonstrating training data reconstruction | 6.5 Medium | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-20634) |

#### Mitigations by tier

**Foundational**
- Apply differential privacy during training
- Monitor query patterns for inference attack signatures

**Hardening**
- Membership inference red team before production deployment
- Suppress confidence scores where not required

**Advanced**
- Machine unlearning for memorised sensitive records
- Query-level anomaly detection

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenDP | Open-source | https://github.com/opendp/opendp |
| ML Privacy Meter | Open-source | https://github.com/privacytrustlab/ml_privacy_meter |

#### Cross-references
- LLM Top 10: LLM02 Sensitive Information Disclosure
- Other frameworks: ISO 27001 A.8.11 — CIS 3.11 — ASVS V8

---

### DSGAI19 — Human-in-Loop & Labeler Overexposure

**Severity:** Medium

Human reviewers and RLHF annotators exposed to sensitive content without
adequate controls — creating privacy violations and welfare risks.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-285](https://cwe.mitre.org/data/definitions/285.html) | Improper Authorisation | Annotation workers access broader data than their labelling task requires | Foundational | Both |
| [CWE-359](https://cwe.mitre.org/data/definitions/359.html) | Exposure of Private Personal Information | Personal data of data subjects exposed to annotation workers without adequate consent or controls | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Apply data minimisation to annotation tasks — redact non-required fields
- Restrict labeller access to minimum required dataset scope
- Audit labeller access to sensitive content

**Hardening**
- Harmful content warning systems for labellers
- Data handling agreements with annotation providers

**Advanced**
- Automated pre-filtering to reduce human exposure to harmful content
- Privacy impact assessments on annotation workflows

#### Cross-references
- Other frameworks: ISO 27001 A.5.20 — GDPR Art. 28 — CIS 3.3

---

### DSGAI20 — Model Exfiltration & IP Replication

**Severity:** High

Systematic queries reconstruct model behaviour and create functional replicas —
stealing proprietary capabilities without access to model weights.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-284](https://cwe.mitre.org/data/definitions/284.html) | Improper Access Control | Model API does not limit query rates or patterns sufficient to prevent systematic extraction | Hardening | Both |
| [CWE-201](https://cwe.mitre.org/data/definitions/201.html) | Insertion of Sensitive Information Into Sent Data | Model responses include confidence scores and logits providing signal for extraction attacks | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Rate limiting and query monitoring on all model inference APIs
- Log unusual query patterns indicating systematic extraction

**Hardening**
- Suppress confidence scores and logits where not required
- Query diversity detection — flag systematic query patterns

**Advanced**
- Model watermarking — embed detectable fingerprints in outputs
- Extraction attack detection via query pattern analysis

#### Tools

| Tool | Type | Link |
|---|---|---|
| ART (Adversarial Robustness Toolbox) | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |

#### Cross-references
- Other frameworks: ISO 27001 A.5.12 — CIS 6.2 — ASVS V4

---

### DSGAI21 — Disinformation via Data Poisoning

**Severity:** High

Disinformation injected into training or RAG corpora causes models to
systematically generate false outputs for targeted topics or entities.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-345](https://cwe.mitre.org/data/definitions/345.html) | Insufficient Verification of Data Authenticity | RAG corpus content accepted without verifying factual accuracy or source trustworthiness | Hardening | Both |
| [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | Improper Input Validation | Training data pipelines fail to detect disinformation content — adversarial samples accepted | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Provenance tracking for all RAG corpus content — source and last-verified date recorded
- Validate training data for factual consistency before use

**Hardening**
- Monitor production outputs for systematic factual drift
- Source diversity requirements for high-stakes RAG corpora

**Advanced**
- Automated fact-checking pipelines for high-risk output domains
- Red team RAG corpus injection detection controls

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

| Phase | DSGAI entries | Key CWEs | Rationale |
|---|---|---|---|
| 1 — Do now | DSGAI01, DSGAI02, DSGAI12 | CWE-200, CWE-798, CWE-89 | Critical severity — disclosure, credential exposure, NL injection |
| 2 — This sprint | DSGAI04, DSGAI05, DSGAI11 | CWE-345, CWE-20, CWE-488 | Poisoning, validation, and context isolation |
| 3 — This quarter | DSGAI03, DSGAI06, DSGAI07, DSGAI13–15 | CWE-284, CWE-268, CWE-312 | Access control, tool exchange, and data governance |
| 4 — Ongoing | DSGAI08–10, DSGAI16–21 | CWE-359, CWE-400, CWE-327 | Compliance, resilience, and advanced threat mitigation |

---

## References

- [CWE — Common Weakness Enumeration](https://cwe.mitre.org/)
- [CVE Program](https://www.cve.org/)
- [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/)
- [NVD — National Vulnerability Database](https://nvd.nist.gov/)
- [OWASP AIVSS](https://aivss.owasp.org)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-27 | 2026-Q1 | Initial mapping — DSGAI01–DSGAI21 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
