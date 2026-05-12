<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : CWE / CVE — Common Weakness Enumeration / Common Vulnerabilities and Exposures
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × CWE / CVE

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) taxonomy and
documented [Common Vulnerabilities and Exposures (CVE)](https://www.cve.org/) entries.

CWE provides root-cause weakness classifications maintained by MITRE and used as
the foundation for vulnerability databases, SAST tools, and secure coding standards.
Mapping LLM risks to CWE entries enables security teams to connect GenAI threats to
the same weakness taxonomy already used for bug tracking, tool configuration, and
compliance reporting. CVE entries provide confirmed real-world evidence of exploitation.

---

## CWE taxonomy structure relevant to LLM risks

| CWE Pillar | What it covers | LLM relevance |
|---|---|---|
| Input Validation (CWE-20 family) | Improper handling of untrusted input | Prompt injection, output handling |
| Information Exposure (CWE-200 family) | Unauthorised data disclosure | Sensitive data disclosure, system prompt leakage |
| Injection (CWE-74 family) | Injection of code or commands via input | Prompt injection, insecure output handling |
| Resource Management (CWE-400 family) | Uncontrolled resource consumption | Unbounded consumption |
| Data Integrity (CWE-345 family) | Verification failures on data origin | Supply chain, data poisoning |
| Access Control (CWE-264 family) | Insufficient permission enforcement | Excessive agency, privilege abuse |
| Cryptography (CWE-310 family) | Weak or absent cryptographic protections | Embedding weaknesses, supply chain |

---

## Quick-reference summary

| ID | Name | Severity | Primary CWEs | Key CVEs | Tier | Scope |
|---|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | CWE-20, CWE-74, CWE-77 | CVE-2024-5184, CVE-2024-34359 | Foundational–Advanced | Both |
| LLM02 | Sensitive Information Disclosure | High | CWE-200, CWE-201, CWE-359 | CVE-2019-20634, CVE-2023-28119 | Foundational–Advanced | Both |
| LLM03 | Supply Chain Vulnerabilities | High | CWE-494, CWE-345, CWE-1357 | CVE-2024-3116, CVE-2024-34359 | Foundational–Hardening | Both |
| LLM04 | Data and Model Poisoning | Critical | CWE-345, CWE-346, CWE-20 | CVE-2019-20634 | Hardening–Advanced | Both |
| LLM05 | Insecure Output Handling | High | CWE-79, CWE-89, CWE-78 | CVE-2024-5184 | Foundational–Hardening | Build |
| LLM06 | Excessive Agency | High | CWE-269, CWE-272, CWE-284 | — | Foundational–Hardening | Build |
| LLM07 | System Prompt Leakage | High | CWE-200, CWE-312, CWE-215 | CVE-2023-29374 | Foundational–Hardening | Build |
| LLM08 | Vector and Embedding Weaknesses | Medium | CWE-327, CWE-330, CWE-345 | — | Hardening–Advanced | Build |
| LLM09 | Misinformation | Medium | CWE-1021, CWE-116 | — | Foundational–Hardening | Both |
| LLM10 | Unbounded Consumption | Medium | CWE-400, CWE-770, CWE-799 | CVE-2024-27564 | Foundational–Hardening | Both |

---

## Audience tags

- **Security engineer** — full file, use CWE IDs to configure SAST tools and bug trackers
- **AppSec reviewer** — LLM01, LLM05, LLM07, CWE injection and disclosure families
- **Vulnerability management** — CVE entries for patch prioritisation evidence
- **Developer** — LLM01, LLM05, LLM06 — root cause patterns for secure coding
- **Red teamer** — CVE entries for confirmed exploitation techniques
- **Compliance / auditor** — CWE mappings for SAST tool baseline configuration

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions embedded in user input or processed content manipulate
the LLM's behaviour, bypassing safety measures, executing unauthorised actions,
or leaking data.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | Improper Input Validation | Failure to validate, filter, or sanitise input before processing — root cause enabling prompt injection | Foundational | Both |
| [CWE-74](https://cwe.mitre.org/data/definitions/74.html) | Improper Neutralisation of Special Elements | Injected elements change the intended meaning or behaviour of a command or query — applies to prompt structure manipulation | Foundational | Both |
| [CWE-77](https://cwe.mitre.org/data/definitions/77.html) | Command Injection | Improper neutralisation of special elements used in a command — applies when LLM output or injected instructions reach system-level execution | Foundational | Build |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-5184 | Prompt injection in LangChain's email agent via malicious email content triggering arbitrary command execution | 9.8 Critical | [GitHub advisory](https://github.com/advisories/GHSA-h59x-p739-982c) |
| CVE-2024-34359 | Indirect prompt injection in LlamaIndex allowing untrusted document content to override agent instructions | 7.5 High | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-34359) |

#### Mitigations by tier

**Foundational**
- Treat all external content as untrusted — validate against an expected schema
  before it reaches the model
- Enforce structural separation between system prompt context and user input
- Implement input sanitisation specifically targeting prompt injection patterns

**Hardening**
- Deploy runtime prompt injection classifiers on all input channels
- Require human approval before model executes high-impact actions from
  external content

**Advanced**
- Implement cryptographically signed system prompts
- Deploy independent input + output + action guardrail layers

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Rebuff | Open-source | https://github.com/protectai/rebuff |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI15 Over-Broad Context Windows
- Other frameworks: MITRE ATLAS AML.T0051 — STRIDE T/S/E — ASVS V5

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs inadvertently expose PII, proprietary code, API keys, or confidential data
through outputs — from training data memorisation, over-permissive RAG retrieval,
or improperly sanitised responses.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | Exposure of Sensitive Information to an Unauthorised Actor | Core weakness for all LLM disclosure vulnerabilities — model exposes data beyond the requester's authorised access | Foundational | Both |
| [CWE-201](https://cwe.mitre.org/data/definitions/201.html) | Insertion of Sensitive Information Into Sent Data | Sensitive data included in outputs without necessity or without access control verification | Foundational | Both |
| [CWE-359](https://cwe.mitre.org/data/definitions/359.html) | Exposure of Private Personal Information to an Unauthorised Actor | PII specifically — exposure of personal data through model outputs from training memorisation or RAG over-retrieval | Foundational | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2019-20634 | Model inversion attack against Proofpoint ML classifier recovering training data via confidence scores | 6.5 Medium | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-20634) |
| CVE-2023-28119 | Information disclosure via verbose error responses in Azure OpenAI embedding endpoint exposing internal system details | 5.3 Medium | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-28119) |

#### Mitigations by tier

**Foundational**
- Implement output scanning and redaction for PII, credentials, and proprietary
  patterns before responses reach users
- Enforce access control on RAG data sources — users retrieve only authorised data
- Apply differential privacy in training to limit memorisation

**Hardening**
- Deploy DLP tooling on model output pipelines
- Audit RAG retrieval scope — over-permissive indexes are the most common source
  of disclosure incidents

**Advanced**
- Implement machine unlearning for targeted removal of sensitive data from weights
- Conduct model inversion red team exercises to validate disclosure boundaries

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse, ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI08 Privacy-Violating Inference
- Other frameworks: MITRE ATLAS AML.T0021 — STRIDE I — ISO 27001 A.8.2

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

Malicious or compromised components introduced through the model supply chain —
pre-trained models, fine-tuning datasets, plugins, libraries — inject backdoors or
malicious behaviour that are difficult to detect after integration.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-494](https://cwe.mitre.org/data/definitions/494.html) | Download of Code Without Integrity Check | Model artefacts, plugins, or datasets downloaded without hash or signature verification | Foundational | Both |
| [CWE-345](https://cwe.mitre.org/data/definitions/345.html) | Insufficient Verification of Data Authenticity | Components accepted without verifying their origin or integrity | Foundational | Both |
| [CWE-1357](https://cwe.mitre.org/data/definitions/1357.html) | Reliance on Insufficiently Trustworthy Component | Using third-party AI components without adequate vetting — applies directly to pre-trained models from public registries | Hardening | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-3116 | Arbitrary code execution via maliciously crafted pickle file in Hugging Face model — affects any application loading untrusted model artefacts | 8.8 High | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-3116) |

#### Mitigations by tier

**Foundational**
- Verify cryptographic hashes of all model artefacts and dependencies before use
- Source models only from verified, curated organisational registries
- Pin all AI component versions — prohibit unreviewed automatic updates

**Hardening**
- Maintain a Model Bill of Materials (MBOM) for every production model
- Scan third-party plugins for malicious code before deployment

**Advanced**
- Implement reproducible training pipelines with verified source data
- Deploy model provenance verification at inference time

#### Tools

| Tool | Type | Link |
|---|---|---|
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Syft | Open-source | https://github.com/anchore/syft |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI03 Training & Fine-Tuning Data Risks
- Other frameworks: MITRE ATLAS AML.T0056 — CIS Controls 2.1 — NIST SP 800-161

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Attackers inject malicious data into training datasets, fine-tuning corpora, or RAG
stores to alter model behaviour — introducing backdoors, biases, or misinformation
that persist into production.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-345](https://cwe.mitre.org/data/definitions/345.html) | Insufficient Verification of Data Authenticity | Training and fine-tuning data accepted without verifying origin, integrity, or trustworthiness | Hardening | Both |
| [CWE-346](https://cwe.mitre.org/data/definitions/346.html) | Origin Validation Error | Failure to verify that data, model weights, or RAG content originates from a trusted and unmodified source | Hardening | Both |
| [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | Improper Input Validation | Failure to validate ingested data before use in training or retrieval — allows adversarial samples into the data pipeline | Foundational | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2019-20634 | Model extraction and inversion demonstrating that training data influence can be recovered — related poisoning attack surface | 6.5 Medium | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-20634) |

#### Mitigations by tier

**Foundational**
- Implement data validation and anomaly detection on all training data pipelines
- Restrict write access to training data stores to authorised personnel only
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
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI03 Training & Fine-Tuning Data Risks, DSGAI04 Data Poisoning
- Other frameworks: MITRE ATLAS AML.T0032 — NIST AI RMF MS-2.6 — ISO 42001 A.6.2

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM-generated output passed to downstream components without validation enables
secondary injection attacks: XSS, SQLi, SSRF, or OS command injection.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-79](https://cwe.mitre.org/data/definitions/79.html) | Cross-site Scripting (XSS) | LLM output containing JavaScript rendered in a browser without sanitisation | Foundational | Build |
| [CWE-89](https://cwe.mitre.org/data/definitions/89.html) | SQL Injection | LLM output incorporated into SQL queries without parameterisation | Foundational | Build |
| [CWE-78](https://cwe.mitre.org/data/definitions/78.html) | OS Command Injection | LLM output passed to shell execution without sanitisation | Foundational | Build |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-5184 | LangChain email agent — LLM output used to construct email actions enabling command injection via manipulated output | 9.8 Critical | [GitHub advisory](https://github.com/advisories/GHSA-h59x-p739-982c) |

#### Mitigations by tier

**Foundational**
- Treat all LLM output as untrusted input to any downstream consumer
- Apply context-aware output encoding before passing responses to HTML
  renderers, SQL engines, or shell interpreters
- Define and validate against an explicit output schema for every LLM integration

**Hardening**
- Implement a dedicated output sanitisation layer independent of the model
- Apply allowlist-based output validation — reject output outside the permitted
  syntax for the target consumer

**Advanced**
- Conduct DAST on all interfaces consuming LLM output
- Include output injection scenarios in the adversarial test suite

#### Tools

| Tool | Type | Link |
|---|---|---|
| DOMPurify | Open-source | https://github.com/cure53/DOMPurify |
| Semgrep | Open-source | https://semgrep.dev |
| OWASP ZAP | Open-source | https://www.zaproxy.org |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures
- Other frameworks: ASVS V5 — STRIDE T/E — MITRE ATLAS AML.T0037

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs with over-permissive tool access execute unintended or harmful actions
when manipulated through prompt injection or misaligned goal-following.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-269](https://cwe.mitre.org/data/definitions/269.html) | Improper Privilege Management | LLM granted privileges beyond what is required for its defined task | Foundational | Build |
| [CWE-272](https://cwe.mitre.org/data/definitions/272.html) | Least Privilege Violation | Failure to apply least privilege — LLM retains elevated permissions after they are no longer needed | Foundational | Build |
| [CWE-284](https://cwe.mitre.org/data/definitions/284.html) | Improper Access Control | Absence of explicit access control enforcement on LLM tool invocations | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Apply least agency — grant minimum tool access required for the defined task
- Require explicit human confirmation before any irreversible action
- Define and enforce a tool permission manifest for every LLM deployment

**Hardening**
- Implement action logging with anomaly detection
- Scope API credentials per LLM task — no shared high-privilege accounts

**Advanced**
- Formally specify permitted action graphs — only pre-approved sequences execute
- Conduct red team exercises targeting excessive agency via indirect injection

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI10 Rogue Agents
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: AIUC-1 B006 — STRIDE E — ISA/IEC 62443 SR 2.1

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing internal instructions, business logic, or security controls
are extracted by adversaries — enabling targeted attacks against the model's defences.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | Exposure of Sensitive Information to an Unauthorised Actor | System prompt content disclosed to an attacker who should not have access to it | Foundational | Build |
| [CWE-312](https://cwe.mitre.org/data/definitions/312.html) | Cleartext Storage of Sensitive Information | Security-relevant instructions or credentials stored in system prompts without protection | Foundational | Build |
| [CWE-215](https://cwe.mitre.org/data/definitions/215.html) | Insertion of Sensitive Information Into Debugging Code | System prompts that include verbose internal information expose more than intended | Hardening | Build |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2023-29374 | System prompt extraction in early LangChain versions via crafted inputs exposing internal chain configuration | 7.5 High | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-29374) |

#### Mitigations by tier

**Foundational**
- Never embed secrets or credentials in system prompts — use environment variables
- Instruct models to refuse prompt introspection — enforce at guardrail layer
- Minimise information density in system prompts

**Hardening**
- Monitor for response patterns indicating system prompt leakage
- Conduct prompt extraction red team exercises before go-live

**Advanced**
- Implement system prompt tokenisation with runtime resolution
- Deploy output classifiers blocking responses containing system prompt content

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: STRIDE I — ASVS V14 — MITRE ATLAS AML.T0041

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Weaknesses in vector stores enable adversarial manipulation of retrieval results
and inference of sensitive information from embeddings.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-327](https://cwe.mitre.org/data/definitions/327.html) | Use of a Broken or Risky Cryptographic Algorithm | Weak or absent encryption on embedding vectors enables inversion attacks and data leakage | Hardening | Build |
| [CWE-330](https://cwe.mitre.org/data/definitions/330.html) | Use of Insufficiently Random Values | Deterministic embedding generation enables fingerprinting and inversion of source content | Advanced | Build |
| [CWE-345](https://cwe.mitre.org/data/definitions/345.html) | Insufficient Verification of Data Authenticity | Embedding store accepts injected vectors without verifying their origin or integrity | Hardening | Build |

#### Mitigations by tier

**Foundational**
- Implement access controls on vector store read and write operations
- Validate and sanitise all content before generating embeddings

**Hardening**
- Encrypt embedding vectors at rest and in transit
- Apply trust-tiered retrieval weighted by source provenance

**Advanced**
- Conduct embedding inversion red team exercises
- Implement differential privacy in embedding generation for sensitive corpora

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant | Open-source | https://qdrant.tech |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference & Data Reconstruction
- Other frameworks: NIST AI RMF MS-2.5 — STRIDE T/I — AIUC-1 A

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but factually incorrect or hallucinated content that users
or downstream systems act upon.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-1021](https://cwe.mitre.org/data/definitions/1021.html) | Improper Restriction of Rendered UI Layers or Frames | Users unable to distinguish model-generated content from verified truth — relevant when LLM output is rendered without provenance indicators | Foundational | Both |
| [CWE-116](https://cwe.mitre.org/data/definitions/116.html) | Improper Encoding or Escaping of Output | Model output presented without appropriate framing as AI-generated content — downstream systems treat hallucinated output as ground truth | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Implement RAG to ground responses in verified, up-to-date source material
- Display source citations alongside model responses
- Set clear user expectations about model limitations in high-stakes domains

**Hardening**
- Deploy confidence scoring — flag low-confidence responses for human review
- Log model outputs with version and timestamp for post-incident reconstruction

**Advanced**
- Build automated fact-checking pipelines for high-stakes outputs
- Deploy adversarial probing to identify frequent hallucination topics

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13 — AIUC-1 F — STRIDE T/R

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Adversarial inputs trigger expensive model computations or excessive API calls,
resulting in denial of service or runaway cost.

#### CWE root causes

| CWE | Name | Description | Tier | Scope |
|---|---|---|---|---|
| [CWE-400](https://cwe.mitre.org/data/definitions/400.html) | Uncontrolled Resource Consumption | Failure to limit the resources consumed by model inference — enables DoS through token amplification or sponge attacks | Foundational | Both |
| [CWE-770](https://cwe.mitre.org/data/definitions/770.html) | Allocation of Resources Without Limits or Throttling | No rate limits or quotas on model API access — allows unlimited consumption by a single client | Foundational | Both |
| [CWE-799](https://cwe.mitre.org/data/definitions/799.html) | Improper Control of Interaction Frequency | Failure to control the rate at which an actor can interact with the LLM — enables automated abuse | Foundational | Both |

#### Confirmed CVEs

| CVE | Description | CVSS | Evidence |
|---|---|---|---|
| CVE-2024-27564 | SSRF and unbounded resource consumption in ChatGPT via crafted image URLs causing server-side request amplification | 6.5 Medium | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-27564) |

#### Mitigations by tier

**Foundational**
- Implement rate limiting per user, session, and API key before requests reach
  the model
- Set hard token limits on input and output per request
- Monitor API cost and token usage in real time with automated alerting

**Hardening**
- Implement request queuing and backpressure
- Set per-tenant cost budgets with automatic suspension on breach

**Advanced**
- Deploy sponge example detection
- Conduct load testing with adversarial inputs maximising cost and latency

#### Tools

| Tool | Type | Link |
|---|---|---|
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Nginx (rate limiting) | Open-source | https://nginx.org |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: STRIDE D — ISA/IEC 62443 SR 7.1 — NIST CSF 2.0 DE.AE

---

## Implementation priority

| Phase | LLM entries | Key CWEs | Rationale |
|---|---|---|---|
| 1 — Do now | LLM01, LLM05, LLM06 | CWE-20, CWE-79, CWE-269 | Input validation and privilege control — highest exploitability |
| 2 — This sprint | LLM02, LLM07 | CWE-200, CWE-312 | Information disclosure — closes most common data exposure paths |
| 3 — This quarter | LLM03, LLM04 | CWE-494, CWE-345 | Supply chain integrity — requires pipeline-level architectural changes |
| 4 — Ongoing | LLM08, LLM09, LLM10 | CWE-327, CWE-400 | Defence-in-depth and resilience hardening |

---

## References

- [CWE — Common Weakness Enumeration](https://cwe.mitre.org/)
- [CVE Program](https://www.cve.org/)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [NVD — National Vulnerability Database](https://nvd.nist.gov/)
- [OWASP AIVSS](https://aivss.owasp.org)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-27 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
