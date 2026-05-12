<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : OWASP Application Security Verification Standard (ASVS) 4.0.3
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × OWASP ASVS 4.0.3

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [OWASP Application Security Verification Standard (ASVS) 4.0.3](https://owasp.org/www-project-application-security-verification-standard/)
— the framework for testing and verifying the security of web
applications and APIs, organised into 14 chapters with three
verification levels (L1/L2/L3).

ASVS is the go-to reference for security architects, developers,
and penetration testers building and assessing application security
controls. LLM applications are web applications and APIs with
additional AI-specific attack surfaces — all standard ASVS controls
apply, with specific requirements amplified by the LLM context.

---

## ASVS structure

| Chapter | Title | LLM relevance |
|---|---|---|
| V1 | Architecture, Design, and Threat Modeling | LLM integration architecture, threat modelling |
| V2 | Authentication | LLM API authentication, model access control |
| V3 | Session Management | LLM session isolation, context persistence |
| V4 | Access Control | LLM tool permissions, RAG access control |
| V5 | Validation, Sanitization and Encoding | Prompt injection, output handling — most critical for LLMs |
| V6 | Stored Cryptography | Embedding encryption, training data at rest |
| V7 | Error Handling and Logging | LLM audit logging, exception handling |
| V8 | Data Protection | RAG data protection, PII in LLM scope |
| V9 | Communication | LLM API communication security |
| V10 | Malicious Code | Supply chain — LLM components as software supply chain |
| V11 | Business Logic | LLM autonomous action logic validation |
| V12 | Files and Resources | RAG file uploads, embedding store resources |
| V13 | API and Web Service | LLM API security — rate limiting, output validation |
| V14 | Configuration | LLM secure deployment configuration |

**Verification levels:**
- L1 — Opportunistic: passively verifiable, minimal security requirement
- L2 — Standard: most applications with sensitive data
- L3 — Advanced: high-value targets, high assurance required

---

## Quick-reference summary

| ID | Name | Severity | Primary ASVS Chapters / Requirements | Level | Tier |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | V5.1, V5.2, V1.1, V11.1 | L1–L3 | Foundational–Advanced |
| LLM02 | Sensitive Information Disclosure | High | V8.1, V8.3, V4.1, V6.1 | L1–L3 | Foundational–Advanced |
| LLM03 | Supply Chain Vulnerabilities | High | V10.2, V14.2, V1.1 | L2–L3 | Foundational–Hardening |
| LLM04 | Data and Model Poisoning | Critical | V5.1, V10.2, V12.1 | L2–L3 | Hardening–Advanced |
| LLM05 | Insecure Output Handling | High | V5.2, V5.3, V13.1 | L1–L3 | Foundational–Hardening |
| LLM06 | Excessive Agency | High | V4.1, V11.1, V7.2 | L1–L3 | Foundational–Hardening |
| LLM07 | System Prompt Leakage | High | V8.1, V4.1, V7.2 | L1–L2 | Foundational–Hardening |
| LLM08 | Vector and Embedding Weaknesses | Medium | V4.1, V6.1, V12.1 | L2–L3 | Hardening–Advanced |
| LLM09 | Misinformation | Medium | V11.1, V7.4, V5.2 | L1–L2 | Foundational–Hardening |
| LLM10 | Unbounded Consumption | Medium | V13.1, V11.1, V7.4 | L1–L3 | Foundational–Hardening |

---

## Audience tags

- **Developer** — full file, specific ASVS requirements to implement
- **Security architect** — V1 architecture requirements, V11 business logic
- **Penetration tester** — verification requirements per level for test planning
- **Security engineer** — V5 validation, V4 access control, V13 API security
- **Auditor** — ASVS level mapping for assurance assessment
- **OT engineer** — LLM01, LLM06, LLM10 with ISA 62443 crosswalk for OT context

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions in user input or processed content manipulate
LLM behaviour. ASVS Chapter V5 (Validation, Sanitisation and Encoding)
is the primary chapter — it directly governs input handling, which is
the core of prompt injection defence.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify all user input validated against an allowlist or rejected | V5.1.1 | L1 | All inputs to LLMs validated — indirect injection through processed content equally in scope |
| Verify that HTTP request parts are validated, sanitised, or rejected | V5.1.2 | L1 | LLM API request validation — prompt structure, content type, and character set enforced |
| Verify output encoding prevents injection attacks | V5.2.1 | L1 | LLM output encoding before passing to downstream renderers or interpreters |
| Verify application protects against OS command injection | V5.2.5 | L1 | LLM-generated content validated before execution in any shell or interpreter context |
| Threat modelling of all data flows | V1.1.2 | L2 | LLM data flows threat-modelled — all injection paths identified and documented |
| Verify business logic limits prevent abuse of LLM functions | V11.1.2 | L2 | Business logic controls preventing prompt injection from triggering unauthorised actions |

#### Mitigations by tier

**Foundational (L1)**
- V5.1.1: Implement input validation for all LLM API inputs —
  allowlist of permitted content structures, reject inputs
  containing known injection patterns
- V5.1.2: Validate all HTTP request parts feeding the LLM —
  headers, query parameters, request body, and file uploads
  all validated before LLM processing
- V5.2.1: Implement output encoding for all LLM responses
  before rendering in browsers or passing to interpreters

**Hardening (L2)**
- V1.1.2: Include all LLM data flows in threat modelling —
  every injection path from user input to model context
  documented and mitigated
- V11.1.2: Implement business logic controls — prompt injection
  cannot trigger actions outside the defined LLM use case
  regardless of what the model generates
- Deploy runtime prompt injection detection — active monitoring
  on all input channels

**Advanced (L3)**
- Implement architectural separation between system prompt
  and user input — structural guarantee at the platform level
- Conduct adversarial testing covering all injection vectors —
  direct, indirect via RAG, jailbreak, and multi-turn attacks
- V5.2.5: Verify LLM-generated content is never executed
  without explicit allowlist validation — no shell or eval
  access from model outputs

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| OWASP ZAP (for API testing) | Open-source | https://www.zaproxy.org |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: CIS Controls CIS 16 · ISO 27001 A.8.28 · MITRE ATLAS AML.T0051

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs expose PII, financial data, proprietary code, or confidential
information through outputs — from training data memorisation or
over-permissive RAG retrieval.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify sensitive data is not cached or exposed in logs | V8.1.1 | L1 | LLM outputs containing sensitive data not logged in cleartext or cached without protection |
| Verify PII is identified and protected | V8.3.4 | L1 | PII in LLM training data, RAG sources, and outputs identified and handled per policy |
| Verify access control decisions enforce least privilege | V4.1.3 | L1 | RAG retrieval access controls — users retrieve only data they are authorised to access |
| Verify all sensitive data encrypted at rest | V6.1.1 | L2 | Training data, embeddings, RAG document stores, and prompt caches encrypted at rest |
| Verify all sensitive data encrypted in transit | V9.1.1 | L1 | All LLM API communication and data flows encrypted in transit — TLS 1.2 minimum |

#### Mitigations by tier

**Foundational (L1)**
- V8.1.1: Ensure LLM outputs containing sensitive data are
  not logged in cleartext — redact before logging, mask
  before caching
- V8.3.4: Identify all PII in LLM scope — training data,
  RAG sources, prompt templates, outputs — and apply
  handling requirements per classification
- V4.1.3: Implement least-privilege access on RAG data sources —
  enforce at the retrieval layer, not just application layer

**Hardening (L2)**
- V6.1.1: Encrypt all sensitive data at rest in LLM scope —
  embedding databases, training data stores, prompt caches,
  and observability logs containing sensitive content
- Deploy output scanning for PII before responses are
  delivered — V8.3.4 technical enforcement
- Audit RAG access controls per release — verify retrieval
  scope matches authorised user access rights

**Advanced (L3)**
- Apply differential privacy in training and embedding
  generation for sensitive corpora
- Conduct model inversion red team exercises — validate
  sensitive training data cannot be reconstructed from outputs
- Implement machine unlearning readiness — versioned
  data-to-model linkage for erasure response

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.8.11/A.8.12 · CIS Controls CIS 3 · GDPR Art. 25

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, datasets,
libraries, and plugins — any of which can be compromised.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify third-party components are current and free from vulnerabilities | V10.2.1 | L2 | All LLM component libraries and dependencies scanned for CVEs — ML SBOM maintained |
| Verify only minimal approved external libraries are used | V10.2.2 | L2 | Approved component list for LLM deployments — unsigned or unverified components rejected |
| Verify build pipelines include security checks | V14.2.2 | L2 | CI/CD pipeline for LLM components includes integrity verification and vulnerability scanning |

#### Mitigations by tier

**Foundational (L1)**
- Maintain ML SBOM as part of software asset inventory —
  every LLM component inventoried with version and source
- Pin all LLM component versions — no automatic updates
  in production without review

**Hardening (L2)**
- V10.2.1: Include LLM component CVE scanning in CI/CD
  pipeline — model inference libraries and dependencies
  scanned before each deployment
- V10.2.2: Establish approved component list — only sourced
  from approved vendors, cryptographic signatures verified
- V14.2.2: Integrate LLM component integrity checks into
  build pipeline — unsigned or modified components rejected

**Advanced (L3)**
- Operate isolated model evaluation environment — backdoor
  detection before each production promotion
- Conduct adversarial supply chain testing — attempt to
  introduce compromised components and verify detection
- Establish responsible disclosure relationship with LLM
  vendors — defined vulnerability notification SLA

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: ISO 27001 A.5.19/A.5.21 · CIS Controls CIS 2 · NIST SP 800-218A

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Attackers inject malicious data into training datasets or fine-tuning
pipelines — corrupting model behaviour in ways baked into the weights.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify all inputs validated against allowlist | V5.1.1 | L1 | Training data pipeline input validation — anomalous data rejected before training |
| Verify third-party components free of vulnerabilities | V10.2.1 | L2 | Training pipeline components scanned — compromised dependencies rejected |
| Verify file uploads scanned for malware | V12.1.1 | L2 | Training data uploads scanned before ingestion — adversarial content detected |

#### Mitigations by tier

**Foundational (L1)**
- V5.1.1: Implement input validation on training data
  pipeline — anomaly detection, source validation, and
  schema verification before any training run
- Establish model rollback capability — approved clean
  version available for immediate revert
- Source allowlisting for training data — only approved
  sources enter production training pipelines

**Hardening (L2)**
- V10.2.1: Scan all training pipeline dependencies for
  vulnerabilities — compromised libraries as a poisoning
  attack vector
- V12.1.1: Scan all training data uploads before ingestion —
  adversarial content detected at the pipeline boundary
- Include poisoning detection in security testing programme —
  backdoor trigger testing before each model promotion

**Advanced (L3)**
- Conduct post-training backdoor detection as mandatory
  pre-deployment gate — neural cleanse or equivalent
- Apply differential privacy during training — limits
  influence of any single training example
- Conduct adversarial testing specifically targeting
  your training pipeline and data sources

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: ISO 27001 A.8.27/A.8.29 · CIS Controls CIS 7 · NIST AI RMF MS-3.3

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM output passed to downstream systems without validation enables
XSS, command injection, or SQL injection via AI-generated content.
ASVS V5 is the most critical chapter for this vulnerability.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify output encoding of untrusted data in HTML context | V5.2.1 | L1 | LLM responses rendered in browser contexts encoded against XSS |
| Verify output encoding in SQL query context | V5.3.5 | L1 | LLM-generated SQL parameterised — never raw LLM output in SQL context |
| Verify output encoding in OS command context | V5.2.5 | L1 | LLM-generated commands validated — never raw output in shell context |
| Verify application does not use eval or dynamic code | V5.2.4 | L1 | No eval or dynamic code execution of LLM-generated content |
| Verify anti-CSRF tokens in state-changing operations | V4.2.2 | L1 | CSRF protection on endpoints where LLM output triggers state changes |

#### Mitigations by tier

**Foundational (L1)**
- V5.2.1: Encode all LLM output before rendering in HTML —
  treat model responses as untrusted user input for rendering
- V5.3.5: Parameterise all database queries — never interpolate
  LLM-generated content directly into SQL or NoSQL queries
- V5.2.4: Never use eval, exec, or equivalent on LLM-generated
  content — absolute prohibition enforced through code review

**Hardening (L2)**
- Implement output schema validation — only outputs conforming
  to defined safe structures passed to downstream consumers
- V5.2.5: Maintain allowlist of permitted operations for
  any LLM-generated commands — reject anything outside
  the allowlist before execution
- Conduct DAST on all interfaces consuming LLM output —
  test XSS, injection, and command execution via model responses

**Advanced (L3)**
- Deploy dedicated output security layer independent of
  the LLM — structural guarantee against output injection
- Conduct adversarial output testing — attempt to generate
  injection payloads through crafted inputs against your
  specific deployment and downstream consumers
- Implement runtime output monitoring — flag responses
  containing injection-pattern content before delivery

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Semgrep | Open-source | https://semgrep.dev |
| DOMPurify | Open-source | https://github.com/cure53/DOMPurify |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: CIS Controls CIS 16 · ISO 27001 A.8.28 · CWE-79/CWE-89

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs with excessive autonomy over tools, APIs, and systems execute
unintended or harmful actions when manipulated.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify access control enforces least privilege | V4.1.3 | L1 | LLM tool access enforced at minimum required scope — read-only by default |
| Verify all sensitive functions have access control | V4.1.1 | L1 | LLM cannot access sensitive functions (write, delete, execute) without explicit authorisation |
| Verify all business logic decisions logged | V7.2.2 | L2 | All LLM tool invocations logged with full context — every tool call auditable |
| Verify business logic abuse scenarios identified | V11.1.2 | L2 | Business logic controls preventing tool misuse through prompt manipulation |

#### Mitigations by tier

**Foundational (L1)**
- V4.1.3: Enforce least privilege on all LLM tool access —
  read-only by default, write access requires explicit
  justification and is scoped to minimum required operations
- V4.1.1: Implement access controls on all sensitive LLM
  functions — delete, write, execute, send all require
  verified authorisation, not just model instruction
- Require human confirmation for all irreversible actions —
  separate confirmation interface, not the LLM chat

**Hardening (L2)**
- V7.2.2: Log all LLM tool invocations with full context —
  tool identity, parameters, user session, timestamp —
  immutable audit trail for incident investigation
- V11.1.2: Identify and document business logic abuse
  scenarios — prompt injection paths to tool misuse
  in threat model, mitigations verified in testing
- Deploy action guardrails as independent layer from model —
  structural enforcement of permitted scope

**Advanced (L3)**
- Formally specify permitted action graphs — only
  pre-approved action sequences can execute in production
- Conduct red team exercises specifically testing excessive
  agency through indirect prompt injection
- Include LLM excessive agency in formal security testing
  scope — verify guardrails hold under adversarial conditions

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: ISO 27001 A.8.2 · CIS Controls CIS 5/6 · AIUC-1 B006

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing internal instructions or security controls
are extracted by adversaries — enabling targeted attacks.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify sensitive data not cached in cleartext | V8.1.1 | L1 | System prompts not stored in cleartext application configuration or source code |
| Verify access control enforces least privilege | V4.1.3 | L1 | System prompt access restricted to authorised personnel — read access logged |
| Verify access control decisions logged | V7.2.1 | L2 | All access to system prompts logged — unauthorised access attempts detectable |
| Verify secrets not in source code | V14.2.3 | L2 | System prompts not hardcoded in source code — stored in secret management system |

#### Mitigations by tier

**Foundational (L1)**
- V8.1.1: Do not store system prompts in cleartext — not
  in source code, configuration files, or environment
  variables without secret manager encryption
- V4.1.3: Restrict system prompt access to minimum required
  personnel — version controlled, access controlled,
  all access logged
- Remove all secrets, credentials, and sensitive identifiers
  from system prompts — use runtime token resolution

**Hardening (L2)**
- V7.2.1: Log all access to system prompt storage and
  configuration — audit trail for unauthorised access
  detection and investigation
- V14.2.3: Enforce no secrets in source code — system
  prompts stored in secret management system, never
  committed to version control
- Conduct prompt extraction testing before each deployment —
  verify extraction resistance under known attack techniques

**Advanced (L3)**
- Implement system prompt tokenisation — sensitive phrases
  replaced with opaque tokens resolved at runtime
- Deploy output classifier to detect and block responses
  containing system prompt content
- Red team exercises targeting system prompt recovery —
  document results and verify mitigations hold

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: ISO 27001 A.5.12/A.8.24 · CIS Controls CIS 3/CIS 4 · CWE-200

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Weaknesses in vector stores enable adversarial retrieval manipulation
and inference of sensitive information from embeddings.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify least privilege access control on data | V4.1.3 | L1 | RBAC on all vector store collections — no unauthenticated access |
| Verify all sensitive data encrypted at rest | V6.1.1 | L2 | All vector store content encrypted at rest |
| Verify file upload malware scanning | V12.1.1 | L2 | Content validation on all vector store ingestion — adversarial content detected |

#### Mitigations by tier

**Foundational (L1)**
- V4.1.3: Enable RBAC on all vector store collections —
  enforce least privilege, no unauthenticated access in
  any environment including development
- Validate all content before embedding — input quality
  and integrity controls at the ingestion boundary
- Patch all known vector database CVEs promptly

**Hardening (L2)**
- V6.1.1: Encrypt all vector store content at rest —
  embeddings are sensitive derived data requiring the
  same protection as source documents
- V12.1.1: Implement content validation on ingestion —
  anomalous content, adversarial patterns, and path
  traversal attempts detected and rejected
- Implement anomaly detection on query patterns — alert
  on bulk extraction and unusual retrieval volumes

**Advanced (L3)**
- Conduct embedding inversion testing — validate that
  source content cannot be reconstructed from embeddings
- Apply differential privacy in embedding generation
  for sensitive corpora
- Adversarial retrieval testing — attempt to manipulate
  retrieval results through crafted queries

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant | Open-source | https://qdrant.tech |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3/A.8.24 · CIS Controls CIS 3 · CWE-284

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but incorrect content that users or downstream
systems act upon.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify business logic assumptions documented | V11.1.1 | L2 | LLM accuracy limitations documented as business logic assumptions — verification requirements defined |
| Verify all security controls logged | V7.4.1 | L1 | LLM accuracy metrics and hallucination rate logged — production monitoring for output quality |
| Verify outputs encoded before rendering | V5.2.1 | L1 | LLM advisory outputs clearly labelled — users cannot mistake model output for authoritative source |

#### Mitigations by tier

**Foundational (L1)**
- V5.2.1: Label all LLM advisory output — clear visual
  distinction from authoritative content in all interfaces
- V7.4.1: Log accuracy metrics and user feedback — enable
  production monitoring for hallucination patterns
- Require source citation in all LLM responses — users
  verify against cited sources before acting

**Hardening (L2)**
- V11.1.1: Document LLM accuracy limitations as business
  logic constraints — define which domains require
  independent verification before action
- Deploy confidence scoring — low-confidence responses
  flagged prominently, escalated to human review
- Implement RAG grounded on authoritative, version-controlled
  sources — not uncontrolled web content

**Advanced (L3)**
- Conduct domain-specific accuracy testing before deployment —
  hallucination rate measured per domain against acceptable
  thresholds
- Build automated fact-checking for high-stakes output domains —
  accuracy gate before responses reach regulated workflows
- Continuous drift detection in production — alert when
  accuracy degrades beyond defined thresholds

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: ISO 27001 A.8.16 · CIS Controls CIS 14 · EU AI Act Art. 13

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Adversarial inputs trigger disproportionate resource consumption —
causing denial of service or runaway API cost.

#### ASVS mapping

| Requirement | ID | Level | How it applies |
|---|---|---|---|
| Verify API rate limiting | V13.1.1 | L1 | Rate limiting on all LLM API endpoints — per user, per session, per API key |
| Verify API rejects large unexpected payloads | V13.1.3 | L1 | Token limits on LLM API inputs — requests exceeding limits rejected at the gateway |
| Verify business logic rate limits | V11.1.4 | L2 | Business logic controls on LLM usage — per-tenant cost budgets, rate limit policies |
| Verify error handling does not expose sensitive data | V7.4.1 | L1 | LLM resource exhaustion errors handled gracefully — no sensitive information in error responses |

#### Mitigations by tier

**Foundational (L1)**
- V13.1.1: Implement rate limiting on all LLM API endpoints —
  hard caps per user, per session, and per API key
  enforced at the gateway before reaching the model
- V13.1.3: Set hard token limits on input and output per
  request — reject requests exceeding thresholds with
  a 429 response before inference begins
- V7.4.1: Handle resource exhaustion errors gracefully —
  no sensitive system information in error responses

**Hardening (L2)**
- V11.1.4: Implement per-tenant cost budgets with automatic
  suspension — business logic control, not just monitoring
- Implement circuit breakers — LLM service degradation
  isolated from other system availability
- Per-tenant cost monitoring with automated alerting —
  anomalous consumption detected and responded to

**Advanced (L3)**
- Deploy sponge example detection — inputs designed to
  maximise computation identified and rejected
- Adaptive rate limiting — thresholds adjust dynamically
  based on system load
- Conduct adversarial cost-maximisation testing — identify
  inputs generating maximum token consumption for your
  model and guard those paths

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: ISO 27001 A.5.30 · CIS Controls CIS 4/CIS 12 · CWE-400

---

## ASVS verification checklist for LLM applications

### L1 — Baseline (all LLM applications)

- [ ] V5.1.1: Input validation on all LLM API inputs
- [ ] V5.2.1: Output encoding before rendering in HTML contexts
- [ ] V5.2.4: No eval or dynamic code execution of LLM output
- [ ] V5.3.5: All LLM-generated SQL parameterised
- [ ] V4.1.1/V4.1.3: Least privilege on all LLM tool and data access
- [ ] V8.1.1: Sensitive data not logged in cleartext from LLM outputs
- [ ] V8.3.4: PII in LLM scope identified and handled per policy
- [ ] V9.1.1: All LLM API communication encrypted in transit
- [ ] V13.1.1: Rate limiting on all LLM API endpoints
- [ ] V13.1.3: Token limits enforced at the gateway

### L2 — Standard (applications with sensitive data)

- [ ] V1.1.2: LLM data flows included in threat model
- [ ] V6.1.1: All sensitive data encrypted at rest in LLM scope
- [ ] V7.2.1: All LLM access control decisions logged
- [ ] V7.2.2: All LLM tool invocations logged
- [ ] V10.2.1: LLM component CVEs in vulnerability management
- [ ] V10.2.2: Approved component list enforced
- [ ] V11.1.1: LLM accuracy limitations documented as business logic
- [ ] V11.1.2: Business logic abuse scenarios identified and mitigated
- [ ] V11.1.4: Per-tenant cost budgets and rate limit policies
- [ ] V14.2.2: Build pipeline includes LLM component integrity checks

### L3 — Advanced (high-assurance requirements)

- [ ] Adversarial testing covering all injection vectors
- [ ] Adversarial supply chain testing
- [ ] Model inversion and embedding inversion testing
- [ ] Post-training backdoor detection as deployment gate
- [ ] Domain-specific accuracy testing with defined thresholds

---

## Implementation priority by ASVS level

| Phase | LLM entries | ASVS level | Priority requirements |
|---|---|---|---|
| 1 — L1 baseline | LLM01, LLM05, LLM06, LLM10 | L1 | V5.1.1, V5.2.1, V4.1.3, V13.1.1 |
| 2 — L1 complete | LLM02, LLM07 | L1 | V8.1.1, V8.3.4, V4.1.1 |
| 3 — L2 standard | LLM03, LLM04, LLM08 | L2 | V10.2.1, V10.2.2, V6.1.1, V12.1.1 |
| 4 — L2 complete | LLM09 | L2 | V11.1.1, V7.2.2 |
| 5 — L3 advanced | All | L3 | Adversarial testing, red team, inversion testing |

---

## References

- [OWASP ASVS 4.0.3](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP ASVS GitHub](https://github.com/OWASP/ASVS)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [OWASP AI Testing Guide](https://owasp.org/www-project-ai-testing-guide/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries with L1/L2/L3 verification requirements | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
