<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : FedRAMP AI Overlay (NIST SP 800-53 Rev 5 AI-specific extensions)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative – https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 – FedRAMP AI Overlay

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [FedRAMP AI Overlay](https://www.fedramp.gov/) extending
[NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
with AI-specific control enhancements.

FedRAMP (Federal Risk and Authorization Management Program) is the US
government's standardised approach to security authorisation for cloud
services. The AI overlay extends FedRAMP baseline controls with
AI-specific requirements addressing model access, inference logging,
adversarial testing, model versioning, AI agent identity, AI incident
handling, and AI supply chain risk. Federal agencies deploying
cloud-hosted AI services must meet FedRAMP AI overlay requirements in
addition to the standard baseline. This mapping enables organisations to
trace each OWASP LLM Top 10 risk to specific FedRAMP AI controls and
implement them within their authorisation boundary.

---

## FedRAMP AI control families

| Family | ID | Purpose |
|---|---|---|
| Access Control | AC | AI service account management, model access enforcement, AI agent least privilege |
| Audit and Accountability | AU | AI decision logging, behaviour monitoring, inference audit trails |
| Security Assessment | CA | AI-specific assessments, model drift monitoring, AI red-teaming |
| Configuration Management | CM | Model versioning, update controls, AI capability restrictions |
| Identification and Authentication | IA | Non-human identity for AI agents, identifier management |
| Incident Response | IR | AI incident handling, AI-specific CISA reporting |
| Program Management | PM | AI risk management strategy, AI threat framing |
| Risk Assessment | RA | AI-specific risk assessment, AI red-teaming |
| System and Services Acquisition | SA | AI SDLC, safety by design, third-party AI services |
| System and Communications Protection | SC | AI API boundaries, model encryption, training data protection at rest |
| System and Information Integrity | SI | Adversarial input protection, AI behaviour monitoring, prompt validation |
| Supply Chain Risk Management | SR | AI supply chain plan, model provenance controls |

---

## Quick-reference summary

| ID | Name | Severity | FedRAMP AI Controls | Scope |
|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | SI-3, SI-10, RA-5, CA-8 | Both |
| LLM02 | Sensitive Information Disclosure | High | SC-28, AU-2, AC-3 | Both |
| LLM03 | Training Data Poisoning | Critical | SR-2, SR-3, SI-3, CM-3 | Both |
| LLM04 | Model DoS | High | SC-7, SI-4, CM-7 | Both |
| LLM05 | Supply Chain Vulnerabilities | High | SR-2, SR-3, SA-9, SA-3 | Both |
| LLM06 | Excessive Agency | High | AC-6, CM-7, AC-3, PM-9 | Build |
| LLM07 | System Prompt Leakage | High | SC-28, AC-3, AU-2 | Build |
| LLM08 | Vector and Embedding Weaknesses | Medium | SC-28, SI-3, RA-5 | Build |
| LLM09 | Misinformation | Medium | SI-4, CA-7, AU-6 | Both |
| LLM10 | Unbounded Consumption | Medium | SC-7, SI-4, CM-7 | Both |

---

## Audience tags

`developer` `security-engineer` `ml-engineer` `compliance-officer` `ciso` `fedramp-assessor`

- **Developer / ML engineer** – SI and CM controls per entry; secure AI development and configuration
- **Security engineer** – SC and AU controls; boundary protection and audit
- **FedRAMP assessor** – full file; control traceability and evidence mapping
- **Compliance officer** – full file; FedRAMP AI overlay alignment
- **CISO** – PM and RA entries; AI risk strategy and governance

---

## Detailed mappings

---

### LLM01 – Prompt Injection

**Severity:** Critical

Malicious instructions embedded in user inputs or external content manipulate
LLM behaviour, bypassing safety controls and executing unauthorised actions.
FedRAMP AI overlay addresses this through malicious code protection extended
to adversarial AI inputs (SI-3), input validation for prompt content (SI-10),
vulnerability scanning including AI red-teaming (RA-5), and penetration
testing covering prompt injection vectors (CA-8).

**Real-world references:**
- EchoLeak (2025) – indirect prompt injection turned Microsoft 365 Copilot
  into a silent exfiltration engine via email content
- Samsung source code leak (2023) – proprietary data surfaced through
  manipulated model queries

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Malicious Code Protection — adversarial AI inputs | SI-3 | SI | Extend malicious code protection to detect and block adversarial inputs including direct and indirect prompt injection payloads |
| Information Input Validation — prompt validation | SI-10 | SI | Validate all inputs to LLM inference endpoints; enforce structural separation between instruction and data contexts; reject known injection patterns |
| Vulnerability Scanning — AI red-teaming | RA-5 | RA | Include prompt injection vectors in vulnerability scanning programme; conduct regular automated and manual injection testing |
| Penetration Testing — AI adversarial testing | CA-8 | CA | Include prompt injection scenarios in penetration testing engagements; cover direct, indirect, and multimodal injection paths |

#### Mitigations

**Foundational**
- SI-10: Implement input validation on all LLM-facing endpoints —
  enforce structural separation between system instructions and user
  content; reject inputs matching known injection signatures
- SI-3: Extend malicious input detection to cover adversarial prompt
  patterns; deploy input scanning as a pre-processing layer before
  model inference
- Establish a policy that all LLM inputs from untrusted sources are
  treated as potentially adversarial; enforce at architecture review

**Hardening**
- CA-8: Include prompt injection in penetration testing scope — cover
  direct injection, indirect injection via RAG sources, jailbreak
  patterns, and multimodal vectors; gate production releases on
  penetration test sign-off
- RA-5: Deploy automated prompt injection scanning tools in CI/CD;
  run against each model version before deployment
- Apply privilege separation — if the model cannot invoke destructive
  tools by design, injection impact is bounded

**Advanced**
- CA-8: Extend adversarial testing to cover your specific RAG document
  corpus, tool descriptors, MCP server schemas, and any email or
  calendar processing pipelines
- SI-3: Integrate injection detection signals into your SIEM and
  FedRAMP continuous monitoring programme; automate session isolation
  on high-confidence injection indicators
- RA-5: Document red-team findings as POA&M items; track remediation
  through the FedRAMP authorisation lifecycle

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| PyRIT | Open-source | https://github.com/Azure/PyRIT |
| NIST SP 800-53A | Reference | https://csrc.nist.gov/publications/detail/sp/800-53a/rev-5/final |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: MITRE ATLAS AML.T0051 – NIST CSF 2.0 PR.AC-5 – SP 800-218A PW.2.1-PS

---

### LLM02 – Sensitive Information Disclosure

**Severity:** High

LLMs inadvertently reveal sensitive data — PII, credentials, proprietary
content, or system architecture details — through model responses. FedRAMP
AI overlay addresses this through protection of information at rest including
training data and model weights (SC-28), comprehensive AI decision and
inference logging (AU-2), and access enforcement on model endpoints and
training data stores (AC-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Protection of Information at Rest — training data and model weights | SC-28 | SC | Encrypt training data, fine-tuning datasets, and model weights at rest; prevent data memorisation exposure through access controls on data stores |
| Event Logging — AI inference logging | AU-2 | AU | Log all model inference requests and responses with sufficient detail to detect sensitive data disclosure; include user identity, query content, and response metadata |
| Access Enforcement — model endpoint access | AC-3 | AC | Enforce role-based access control on model inference endpoints; restrict access to training data, fine-tuning data, and model configuration based on clearance and need-to-know |
| System Monitoring — output content monitoring | SI-4 | SI | Monitor model outputs for sensitive data patterns — PII, credentials, classification markings — and alert on detection |

#### Mitigations

**Foundational**
- SC-28: Encrypt all training data, fine-tuning datasets, and model
  weights at rest using FIPS 140-validated cryptographic modules;
  enforce key management aligned with FedRAMP requirements
- AC-3: Implement role-based access control on all model inference
  endpoints; ensure that only authorised users and services can query
  the model; restrict training data access to approved ML engineers
- AU-2: Log all inference requests and responses with user identity,
  timestamp, and query metadata; retain logs per FedRAMP retention
  requirements

**Hardening**
- SI-4: Deploy output monitoring to detect sensitive data patterns in
  model responses — PII, credentials, API keys, classification
  markings; alert and block on detection
- SC-28: Conduct data memorisation testing on models before deployment;
  verify that training data cannot be extracted through targeted queries
- AU-2: Feed inference logs into your FedRAMP continuous monitoring
  programme; establish alerting for anomalous query patterns

**Advanced**
- Apply differential privacy to training pipelines to bound memorisation
  risk; measure and track privacy budget
- Deploy output classifiers that detect and redact sensitive content
  before responses reach end users
- SC-28: Include data extraction testing in FedRAMP annual assessments;
  document residual memorisation risk in SSP

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| AWS CloudTrail / Azure Monitor | Commercial | https://aws.amazon.com/cloudtrail/ |

#### Cross-references
- Agentic Top 10: ASI03 Privilege Escalation
- DSGAI 2026: DSGAI08 Data Leakage & Exposure, DSGAI16 Erosion of Privacy
- Other frameworks: NIST CSF 2.0 PR.DS-5 – CWE-200 – SP 800-218A PS.1.1-PS

---

### LLM03 – Training Data Poisoning

**Severity:** Critical

Attackers corrupt training data or fine-tuning pipelines to embed backdoors
or bias model behaviour in ways baked into the weights and invisible to
standard inference testing. FedRAMP AI overlay addresses this through supply
chain risk management planning covering AI data sources (SR-2), supply chain
controls for model provenance (SR-3), adversarial input protection for
training pipelines (SI-3), and configuration change control for model
updates (CM-3).

**Real-world references:**
- Nightshade (2023) – poison pixels successfully corrupted image generation
  model behaviour at scale
- BadNets (academic) – backdoor triggers embedded through poisoned training
  labels, activating only on specific inputs in production

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Supply Chain Risk Management Plan — AI data sources | SR-2 | SR | Include AI training data sources, fine-tuning datasets, and pre-trained model weights in the supply chain risk management plan; document provenance and risk assessment for each |
| Supply Chain Controls and Processes — model provenance | SR-3 | SR | Implement supply chain controls for AI model components — verify integrity, provenance, and authenticity of all training data and model weights before use |
| Malicious Code Protection — training pipeline integrity | SI-3 | SI | Extend malicious code protection to training data pipelines; detect and block poisoned data, anomalous labels, and backdoor triggers |
| Configuration Change Control — model update governance | CM-3 | CM | Require formal change control for all model updates, fine-tuning runs, and training data changes; maintain audit trail of all modifications |

#### Mitigations

**Foundational**
- SR-2: Include all AI training data sources in your supply chain risk
  management plan; document data provenance, licensing, and risk
  assessment for each source
- SR-3: Implement integrity verification for all training data and
  model weights — cryptographic checksums, signed attestations, and
  provenance documentation
- CM-3: Require formal change control for all model retraining and
  fine-tuning activities; log all training runs with dataset references

**Hardening**
- SI-3: Apply anomaly detection to training data before each training
  run — flag statistical outliers, unexpected label distributions, and
  content inconsistent with the source domain
- SR-3: Maintain a secure model registry with signed checksums for
  every model version; implement rollback capability to pre-poisoning
  checkpoints on detection
- CM-3: Implement automated validation gates in the training pipeline;
  block promotion of models trained on unvetted data

**Advanced**
- Apply differential privacy during training to bound the influence of
  any single training example — measure and track privacy budget
- SI-3: Conduct backdoor detection (neural cleanse or equivalent) on
  all new model versions trained on external datasets before promotion
  to production
- SR-2: Conduct ongoing monitoring of training data supply chain;
  re-assess risk on schedule aligned with FedRAMP continuous monitoring

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Sigstore | Open-source | https://www.sigstore.dev |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI05 Data Integrity & Validation Failures
- Other frameworks: MITRE ATLAS AML.T0032 – NIST CSF 2.0 PR.DS-8 – SP 800-218A PS.1.1-PS

---

### LLM04 – Model DoS

**Severity:** High

Adversarial inputs trigger disproportionate compute, memory, or token
consumption causing denial of service or runaway inference cost. FedRAMP
AI overlay addresses this through boundary protection for AI API endpoints
(SC-7), system monitoring for consumption anomalies (SI-4), and least
functionality restricting model resource access (CM-7).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Boundary Protection — AI API endpoints | SC-7 | SC | Enforce boundary protection on all AI inference endpoints — rate limiting, token quotas, and cost circuit breakers at the network and application boundary |
| System Monitoring — consumption anomaly detection | SI-4 | SI | Monitor AI inference services for resource consumption anomalies — token spikes, latency degradation, cost overruns; alert and auto-mitigate on threshold breach |
| Least Functionality — AI resource restrictions | CM-7 | CM | Restrict AI inference services to minimum necessary compute, memory, and token budgets; disable unused model capabilities and endpoints |
| Event Logging — resource consumption logging | AU-2 | AU | Log resource consumption per inference request — tokens, latency, cost; enable detection and forensic analysis of DoS patterns |

#### Mitigations

**Foundational**
- SC-7: Implement rate limiting and token quotas at the API gateway
  before requests reach the model; define per-user, per-session, and
  per-API-key limits as boundary controls
- CM-7: Restrict AI inference services to minimum necessary resource
  budgets; disable unused endpoints and model capabilities
- SI-4: Monitor inference services for consumption anomalies; establish
  baseline resource usage and alert on deviations

**Hardening**
- SC-7: Deploy cost circuit breakers that automatically suspend service
  when consumption exceeds thresholds; alerting alone is insufficient
- SI-4: Include resource exhaustion scenarios in continuous monitoring;
  test detection capabilities against sponge example attacks and token
  amplification patterns
- AU-2: Feed consumption logs into FedRAMP continuous monitoring;
  establish trending and alerting for consumption drift

**Advanced**
- Conduct adversarial cost-maximisation testing — identify the specific
  inputs that generate maximum token consumption for your model and
  guard those paths with additional controls
- Implement adaptive rate limiting with real-time system load awareness;
  thresholds adjust dynamically under attack conditions
- Document recovery time objectives (RTO) and recovery point objectives
  (RPO) for AI services in your FedRAMP contingency plan

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| AWS WAF / Azure Front Door | Commercial | https://aws.amazon.com/waf/ |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: CWE-400 – SP 800-218A PW.2.1-PS – NIST CSF 2.0 PR.PT-4

---

### LLM05 – Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, datasets, libraries,
and plugins — any of which can be compromised to introduce backdoors or
malicious functionality. FedRAMP AI overlay addresses this through supply
chain planning (SR-2), supply chain controls and provenance verification
(SR-3), external information system services controls for third-party AI
providers (SA-9), and secure system development lifecycle for AI (SA-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Supply Chain Risk Management Plan — AI components | SR-2 | SR | Include all AI components — models, datasets, adapters, libraries, plugins — in the supply chain risk management plan with provenance and risk assessment |
| Supply Chain Controls — model provenance verification | SR-3 | SR | Implement integrity verification for all AI supply chain components using cryptographic signatures, checksums, and attestation before deployment |
| External Information System Services — third-party AI | SA-9 | SA | Require third-party AI service providers to meet FedRAMP requirements; establish SLAs covering model security, data handling, and incident notification |
| System Development Life Cycle — AI SDLC | SA-3 | SA | Integrate AI-specific security activities into the SDLC — model security review, adversarial testing, supply chain verification at each lifecycle phase |

#### Mitigations

**Foundational**
- SR-2: Establish an approved sources policy for AI components; model
  weights, datasets, adapters, and libraries must come from vetted
  sources with documented provenance
- SR-3: Verify cryptographic signatures or checksums for all model
  artefacts before deployment; do not deploy unsigned or unverified
  components
- Maintain a complete ML SBOM for every production AI system within
  the FedRAMP authorisation boundary

**Hardening**
- SA-9: Require FedRAMP authorisation or equivalent for all third-party
  AI service providers; include AI-specific security requirements in
  service agreements
- SA-3: Integrate model security review and adversarial testing into
  your SDLC; gate production deployment on security sign-off
- SR-3: Implement automated supply chain integrity verification in
  CI/CD; block deployment on verification failure

**Advanced**
- SR-2: Conduct backdoor detection on all new model versions from
  third-party providers before production promotion
- SA-9: Include third-party AI provider security posture in FedRAMP
  continuous monitoring; reassess annually or on significant change
- Extend ML SBOM to cover runtime dynamic components — MCP servers,
  plugins, and tools fetched at inference time

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |
| Sigstore | Open-source | https://www.sigstore.dev |

#### Cross-references
- Agentic Top 10: ASI04 Supply Chain Compromise, ASI10 AI Agent Dependency Failures
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI19 Third-Party Data Risk
- Other frameworks: MITRE ATLAS AML.T0056 – SP 800-218A PW.4.1-PS – CycloneDX ML SBOM

---

### LLM06 – Excessive Agency

**Severity:** High

LLMs granted excessive autonomy over tools, APIs, and systems execute
unintended or harmful actions when manipulated. FedRAMP AI overlay addresses
this through least privilege enforcement for AI agent permissions (AC-6),
least functionality restricting AI capabilities (CM-7), access enforcement
on tool invocations (AC-3), and risk management strategy covering AI
autonomy risk (PM-9).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Least Privilege — AI agent permissions | AC-6 | AC | Enforce least privilege for all AI agent tool access, API permissions, and autonomous action scope; restrict to minimum capabilities needed per deployment |
| Least Functionality — AI capability restrictions | CM-7 | CM | Restrict AI systems to minimum necessary capabilities; disable unused tools, APIs, and action types; enforce capability restrictions in configuration |
| Access Enforcement — tool invocation control | AC-3 | AC | Enforce access control on all AI tool invocations; require authorisation for each tool call based on agent identity, context, and action type |
| Risk Management Strategy — AI autonomy risk | PM-9 | PM | Include AI autonomy and excessive agency in the organisational risk management strategy; define acceptable autonomy thresholds and escalation procedures |

#### Mitigations

**Foundational**
- AC-6: Define explicit least privilege policies for each AI deployment;
  document the maximum permitted tool access, API scope, and autonomous
  action types; enforce before go-live
- CM-7: Disable all AI capabilities and tool access not explicitly
  required; maintain a tool permission manifest per deployment
- AC-3: Require human approval for all irreversible or high-impact
  actions; enforce in architecture, not relying on model judgment

**Hardening**
- PM-9: Include AI autonomy risk in organisational risk assessment;
  define acceptable autonomy thresholds tied to data sensitivity and
  impact level within the FedRAMP authorisation boundary
- AC-6: Log all tool invocations with full parameter capture; feed
  into runtime anomaly detection and FedRAMP continuous monitoring
- CM-7: Review tool permission manifests at each FedRAMP annual
  assessment; remove unused permissions

**Advanced**
- Conduct formal adversarial exercises specifically testing indirect
  injection through every data source that feeds the agent; permission
  manifest must hold under worst-case injection
- AC-6: Include AI autonomy limits in security design reviews;
  autonomous action scope changes require explicit security sign-off
- Formally specify permitted action graphs; only pre-approved action
  sequences can execute in production

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| LangSmith | Commercial | https://smith.langchain.com |
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI07 Lateral Tool Chaining
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange
- Other frameworks: SP 800-218A PW.1.1-PS – MITRE ATLAS AML.T0015 – NIST CSF 2.0 PR.AC-4

---

### LLM07 – System Prompt Leakage

**Severity:** High

System prompts containing internal instructions, business logic, or security
controls are extracted by adversaries — enabling targeted attacks against
specific defences. FedRAMP AI overlay addresses this through protection of
information at rest covering system prompt confidentiality (SC-28), access
enforcement on prompt configuration (AC-3), and inference logging to detect
extraction attempts (AU-2).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Protection of Information at Rest — system prompt confidentiality | SC-28 | SC | Classify system prompts as sensitive configuration; encrypt at rest, enforce access controls, and apply version control and audit logging to all prompt stores |
| Access Enforcement — prompt configuration access | AC-3 | AC | Restrict access to system prompt configurations to authorised personnel; enforce role-based access control and change management on all prompt modifications |
| Event Logging — prompt extraction detection | AU-2 | AU | Log inference interactions with sufficient detail to detect system prompt extraction attempts; alert on query patterns indicative of extraction techniques |
| Malicious Code Protection — prompt extraction defence | SI-3 | SI | Deploy output monitoring to detect and block responses containing system prompt content; treat extraction as a security event |

#### Mitigations

**Foundational**
- SC-28: Classify system prompts as sensitive configuration artefacts;
  encrypt at rest using FIPS 140-validated modules; version control
  with access logging on all modifications
- AC-3: Restrict access to system prompt configurations to authorised
  personnel only; enforce least privilege and change management
- AU-2: Log all inference requests with sufficient detail to detect
  prompt extraction patterns; include in FedRAMP audit scope

**Hardening**
- SI-3: Deploy output monitoring to detect response patterns indicative
  of system prompt disclosure; alert and escalate on detection
- SC-28: Enforce that no credentials, API keys, or sensitive business
  logic that must remain confidential are embedded in system prompts;
  use environment variables and secrets managers
- AC-3: Include system prompt access in FedRAMP access control reviews;
  verify quarterly

**Advanced**
- Conduct structured red team exercises covering all known prompt
  extraction techniques against your specific deployment; document
  residual risk in SSP
- Deploy output classifiers trained to detect and block responses
  containing system prompt content
- AU-2: Integrate prompt extraction detection into FedRAMP continuous
  monitoring; automate alerting and incident creation

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |
| Rebuff | Open-source | https://github.com/protectai/rebuff |
| HashiCorp Vault | Commercial | https://www.vaultproject.io |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI08 Data Leakage & Exposure
- Other frameworks: CWE-200 – SP 800-218A PS.1.1-PS – NIST CSF 2.0 PR.DS-5

---

### LLM08 – Vector and Embedding Weaknesses

**Severity:** Medium

Vulnerabilities in vector databases and embedding pipelines enable data
poisoning, unauthorised access to embedding stores, or extraction of
sensitive information from vector representations. FedRAMP AI overlay
addresses this through protection of information at rest for embedding
stores (SC-28), malicious code protection extended to adversarial embedding
manipulation (SI-3), and vulnerability scanning covering embedding
infrastructure (RA-5).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Protection of Information at Rest — embedding store protection | SC-28 | SC | Encrypt vector databases and embedding stores at rest; enforce access controls and audit logging on all embedding read and write operations |
| Malicious Code Protection — adversarial embedding detection | SI-3 | SI | Extend malicious code protection to detect adversarial manipulation of embeddings — poisoned vectors, out-of-distribution injections, and embedding inversion attacks |
| Vulnerability Scanning — embedding infrastructure | RA-5 | RA | Include vector databases, embedding pipelines, and retrieval infrastructure in vulnerability scanning; test for injection, access control bypass, and data extraction |
| Access Enforcement — embedding store access | AC-3 | AC | Enforce role-based access control on vector database operations; restrict who can read, write, and delete embeddings |

#### Mitigations

**Foundational**
- SC-28: Encrypt all vector databases and embedding stores at rest;
  implement access controls restricting read/write access to authorised
  services and personnel
- SI-3: Validate all content before embedding generation; reject
  content that fails integrity or provenance checks
- RA-5: Include embedding infrastructure in your vulnerability scanning
  programme; scan for known CVEs in vector database software

**Hardening**
- AC-3: Implement tenant isolation in multi-tenant vector databases;
  enforce access control at the namespace or collection level
- SI-3: Deploy anomaly detection on embedding writes — flag vectors
  that are statistical outliers or inconsistent with the source domain
- RA-5: Conduct embedding inversion testing to assess whether
  sensitive source content can be reconstructed from stored embeddings

**Advanced**
- SC-28: Include vector database security in FedRAMP annual assessments;
  document embedding store architecture in SSP
- Deploy embedding watermarking to detect tampering and verify provenance
  of stored vectors
- SI-3: Implement continuous monitoring of embedding store integrity;
  alert on unexpected bulk modifications or access pattern anomalies

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://weaviate.io |
| Milvus | Open-source | https://milvus.io |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| OWASP ZAP | Open-source | https://www.zaproxy.org |

#### Cross-references
- Agentic Top 10: ASI06 Memory Poisoning & Context Confusion
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI05 Data Integrity & Validation Failures
- Other frameworks: MITRE ATLAS AML.T0018 – SP 800-218A PS.1.1-PS – CWE-1395

---

### LLM09 – Misinformation

**Severity:** Medium

LLMs generate factually incorrect, misleading, or fabricated content
(hallucinations) that users or downstream systems treat as authoritative.
FedRAMP AI overlay addresses this through system monitoring for output
quality (SI-4), continuous monitoring for model drift (CA-7), and audit
review of AI behaviour and outputs (AU-6).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| System Monitoring — output quality monitoring | SI-4 | SI | Monitor model outputs for factual accuracy, consistency, and hallucination indicators; alert when confidence scores or factual grounding drops below thresholds |
| Continuous Monitoring — model drift detection | CA-7 | CA | Include model output quality and drift monitoring in FedRAMP continuous monitoring programme; track accuracy metrics, hallucination rates, and output consistency over time |
| Audit Review — AI behaviour review | AU-6 | AU | Regularly review AI inference logs and output samples for hallucination patterns, factual errors, and misleading content; escalate findings through security channels |
| Information Input Validation — grounding and retrieval validation | SI-10 | SI | Validate retrieval sources and grounding data provided to the model; ensure factual grounding sources are authoritative and current |

#### Mitigations

**Foundational**
- SI-4: Monitor model outputs for hallucination indicators — factual
  inconsistencies, unsupported claims, and fabricated references;
  establish baseline accuracy metrics
- CA-7: Include model output quality metrics in FedRAMP continuous
  monitoring; track accuracy, hallucination rate, and factual
  grounding over time
- AU-6: Conduct regular reviews of AI inference logs for hallucination
  patterns; escalate findings to model governance

**Hardening**
- SI-10: Implement retrieval-augmented generation (RAG) with validated,
  authoritative sources; verify that grounding data is current and
  accurate
- CA-7: Establish automated model drift detection; alert when output
  quality metrics deviate from baseline
- Implement confidence scoring and source attribution in model outputs;
  require human review for low-confidence outputs in high-stakes contexts

**Advanced**
- Deploy factual grounding verification — cross-check model outputs
  against authoritative sources before delivery to end users
- CA-7: Include model output quality in FedRAMP annual assessment scope;
  document hallucination risk and mitigations in SSP
- AU-6: Implement automated hallucination detection in continuous
  monitoring; integrate with incident response for high-impact contexts

#### Tools

| Tool | Type | Link |
|---|---|---|
| Ragas | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |
| TruLens | Open-source | https://github.com/truera/trulens |
| LangSmith | Commercial | https://smith.langchain.com |

#### Cross-references
- Agentic Top 10: ASI09 Emerging Agentic Patterns
- DSGAI 2026: DSGAI17 Bias in Data
- Other frameworks: NIST AI RMF MAP 2.3 – SP 800-218A PW.7.2-PS – ISO 42001 A.6.2.6

---

### LLM10 – Unbounded Consumption

**Severity:** Medium

Unrestricted resource usage — compute, memory, tokens, API costs — causes
denial of service or runaway cost. FedRAMP AI overlay addresses this through
boundary protection with rate limiting and cost controls (SC-7), system
monitoring for consumption anomalies (SI-4), and least functionality
restricting resource access (CM-7).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Boundary Protection — rate limiting and cost controls | SC-7 | SC | Enforce rate limiting, token quotas, and cost circuit breakers at the AI service boundary; define per-user and per-session consumption limits |
| System Monitoring — consumption anomaly detection | SI-4 | SI | Monitor AI service consumption metrics — tokens, latency, cost — in real time; alert and auto-mitigate on consumption anomalies |
| Least Functionality — resource budget enforcement | CM-7 | CM | Restrict AI services to defined resource budgets; disable unnecessary model capabilities; enforce compute and cost limits in configuration |
| Incident Handling — consumption incident response | IR-4 | IR | Define incident handling procedures for AI consumption anomalies including automatic throttling, service suspension, and cost cap enforcement |

#### Mitigations

**Foundational**
- SC-7: Define per-user token limits, per-session rate limits, maximum
  context window size, and monthly cost budgets as explicit boundary
  controls; enforce at the API gateway
- CM-7: Restrict AI inference services to minimum necessary resource
  budgets; disable unused endpoints and capabilities
- SI-4: Monitor consumption metrics and establish baseline usage
  patterns; alert on deviations

**Hardening**
- SC-7: Deploy cost circuit breakers that automatically suspend service
  when consumption exceeds thresholds; implement per-tenant cost budgets
  with automatic suspension on breach
- SI-4: Include consumption anomaly detection in FedRAMP continuous
  monitoring; test detection against adversarial consumption patterns
- IR-4: Define and test automated response to consumption incidents;
  exercise procedures quarterly

**Advanced**
- Conduct adversarial cost-maximisation testing to identify maximum-cost
  input patterns; apply additional controls at those paths
- Implement adaptive rate limiting with real-time system load awareness;
  thresholds adjust dynamically under sustained attack
- Document AI service RTO and RPO in FedRAMP contingency plan; include
  consumption incidents in tabletop exercises

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| AWS Budgets / Azure Cost Management | Commercial | https://aws.amazon.com/aws-cost-management/aws-budgets/ |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: CWE-400 – SP 800-218A PW.2.1-PS – ISA/IEC 62443 SR 7.1

---

## Implementation priority

| Phase | AC / AU / IA | SC / SI / CM | CA / RA / SA / SR / IR / PM |
|---|---|---|---|
| 1 – Now | AC-6 least privilege for LLM06; AC-3 access enforcement for LLM02/07; AU-2 inference logging for LLM02/07 | SI-10 input validation for LLM01; SC-28 encryption at rest for LLM02/03/07 | SR-2 supply chain plan for LLM03/05; CA-8 pen testing for LLM01 |
| 2 – This sprint | AC-3 tool invocation controls for LLM06; AU-6 audit review for LLM09 | SI-3 adversarial input protection for LLM01/03/08; CM-3 change control for LLM03; CM-7 resource restrictions for LLM04/10 | SA-9 third-party AI controls for LLM05; RA-5 AI vulnerability scanning for LLM01/08 |
| 3 – This quarter | AU-2 comprehensive logging for all entries; IA-2 NHI identity for AI agents | SC-7 boundary protection for LLM04/10; SI-4 behaviour monitoring for all entries | CA-7 continuous monitoring for LLM09; PM-9 risk strategy for LLM06; SA-3 AI SDLC for LLM05 |
| 4 – Ongoing | Access control reviews; audit log analysis; identity lifecycle management | Continuous monitoring of consumption and behaviour; configuration drift detection | Annual FedRAMP assessment updates; red-team programme; supply chain re-assessment |

---

## References

- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [FedRAMP](https://www.fedramp.gov/)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [MITRE ATLAS](https://atlas.mitre.org)
- [CISA FedRAMP Guidance](https://www.cisa.gov/topics/cyber-threats-and-advisories/federal-information-security-modernization-act)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-28 | 2026-Q1 | Initial mapping – LLM01–LLM10 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) –
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
