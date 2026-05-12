<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : STRIDE — threat modelling taxonomy (Microsoft)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × STRIDE

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [STRIDE threat modelling taxonomy](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)
— Microsoft's structured method for enumerating threats across six categories:
Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service,
and Elevation of Privilege.

STRIDE is the most widely adopted threat modelling taxonomy in enterprise security.
Mapping LLM risks to STRIDE categories integrates GenAI threats into existing threat
models, enabling security architects and engineers to reason about LLM vulnerabilities
using the same language already used for the rest of the application stack.

---

## STRIDE categories at a glance

| Category | Letter | Core question | Classic example |
|---|---|---|---|
| Spoofing | S | Can an attacker impersonate a trusted identity or source? | Fake login, forged token |
| Tampering | T | Can an attacker modify data or behaviour without authorisation? | SQL injection, file overwrite |
| Repudiation | R | Can an action be denied without a traceable audit trail? | Log deletion, unsigned transactions |
| Information Disclosure | I | Can sensitive data be accessed by unauthorised parties? | Data leakage, verbose errors |
| Denial of Service | D | Can an attacker degrade or deny availability? | Flood attack, resource exhaustion |
| Elevation of Privilege | E | Can an attacker gain permissions beyond their authorisation? | Privilege escalation, IDOR |

---

## Quick-reference summary

| ID | Name | Severity | Primary STRIDE Categories | Tier | Scope |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | T, S, E | Foundational–Advanced | Both |
| LLM02 | Sensitive Information Disclosure | High | I, R | Foundational–Advanced | Both |
| LLM03 | Supply Chain Vulnerabilities | High | T, S, E | Foundational–Hardening | Both |
| LLM04 | Data and Model Poisoning | Critical | T, R | Hardening–Advanced | Both |
| LLM05 | Insecure Output Handling | High | T, E | Foundational–Hardening | Build |
| LLM06 | Excessive Agency | High | E, T, D | Foundational–Hardening | Build |
| LLM07 | System Prompt Leakage | High | I, R | Foundational–Hardening | Build |
| LLM08 | Vector and Embedding Weaknesses | Medium | T, I | Hardening–Advanced | Build |
| LLM09 | Misinformation | Medium | T, R | Foundational–Hardening | Both |
| LLM10 | Unbounded Consumption | Medium | D | Foundational–Hardening | Both |

---

## Audience tags

- **Security architect** — full file, primary reference for LLM threat model design
- **Threat modeller** — full file, integrate STRIDE categories into existing DFD-based models
- **Developer** — LLM01, LLM05, LLM06, LLM07
- **Security engineer** — LLM01, LLM02, LLM04, LLM07
- **AppSec reviewer** — LLM05, LLM07, LLM08
- **SOC analyst** — LLM01, LLM02, LLM06, LLM10
- **OT engineer** — LLM01, LLM04, LLM06 (see ISA 62443 crosswalk for OT-specific controls)

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions embedded in user input or processed content manipulate
the LLM's behaviour, bypassing safety measures, executing unauthorised actions,
or leaking data. Direct injection targets the user input field; indirect injection
hides instructions in documents, emails, RAG content, or web pages the model processes.

**Real-world references:**
- EchoLeak / Microsoft 365 Copilot (2025) — indirect injection via email content
  caused silent data exfiltration
- ChatGPT plugin indirect injection (2023) — malicious web content hijacked plugin actions

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Instruction Spoofing | S | Attacker impersonates the system prompt or a trusted instruction source, causing the model to act on attacker-controlled directives | Foundational | Both |
| Behaviour Tampering | T | Injected instructions alter the model's intended behaviour, bypassing safety controls or changing output logic | Foundational | Both |
| Privilege Elevation via Injection | E | Injected instruction executes actions scoped to the system prompt or higher-privilege context, exceeding the attacker's authorised access | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Treat all external content — documents, emails, web results, RAG chunks — as
  untrusted regardless of source
- Enforce strict separation between system prompt context and user input context
  at the architectural level
- Implement input validation and prompt structure enforcement before content
  reaches the model

**Hardening**
- Deploy runtime prompt injection detection using classifiers or heuristic
  filters on all input channels
- Require human approval before the model executes any high-impact action
  triggered by external content
- Maintain an adversarial test suite covering direct and indirect injection
  scenarios, run in CI/CD

**Advanced**
- Implement prompt integrity verification — cryptographically signed system
  prompts that cannot be overridden by user input
- Deploy multi-layer defence: input filter + output monitor + action guardrail,
  independent of each other
- Red team quarterly with novel indirect injection scenarios targeting your
  specific RAG and tool configurations

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Rebuff | Open-source | https://github.com/protectai/rebuff |
| PromptBench | Open-source | https://github.com/microsoft/promptbench |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI15 Over-Broad Context Windows
- Other frameworks: MITRE ATLAS AML.T0051 — ASVS V5 — CWE-20 — AIUC-1 B001

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs inadvertently expose PII, financial data, proprietary source code, API keys,
or confidential business information through their outputs — either from training
data memorisation, over-permissive RAG retrieval, or improperly sanitised responses.

**Real-world references:**
- Samsung source code leak (2023) — proprietary code memorised and surfaced in outputs
- Proof Pudding / CVE-2019-20634 — model inversion attack recovering training data

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Sensitive Data Disclosure | I | Model outputs expose PII, secrets, proprietary code, or confidential data to unauthorised recipients | Foundational | Both |
| Disclosure Without Audit Trail | R | Data exposure events lack logging sufficient to determine what was disclosed, to whom, and when — enabling deniability | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Implement output scanning and redaction for PII, secrets, and proprietary
  patterns before responses reach users
- Apply differential privacy techniques during model training to limit
  memorisation of sensitive training data
- Enforce access control on RAG data sources — users should only retrieve data
  they are authorised to see

**Hardening**
- Deploy DLP tooling on model output pipelines
- Audit RAG retrieval scope regularly — over-permissive indexes are the most
  common source of disclosure incidents
- Log all model interactions with enough fidelity to reconstruct what data was
  exposed to which user in any given session

**Advanced**
- Implement machine unlearning capability for targeted removal of sensitive data
  from model weights post-training
- Adopt federated learning to avoid centralising sensitive data in training pipelines
- Conduct model extraction and inversion red team exercises to validate disclosure
  boundaries

#### Tools

| Tool | Type | Link |
|---|---|---|
| Presidio | Open-source | https://github.com/microsoft/presidio |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse, ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI08 Privacy-Violating Inference
- Other frameworks: MITRE ATLAS AML.T0021 — ASVS V8 — CWE-200 — ISO 27001 A.8.2

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

Malicious or compromised components introduced through the model supply chain —
pre-trained models, fine-tuning datasets, plugins, libraries, or third-party APIs
— inject backdoors, biases, or malicious behaviour that are difficult to detect
after integration.

**Real-world references:**
- PoisonGPT (2023) — surgically poisoned Llama model uploaded to Hugging Face
  spreading targeted misinformation undetected
- Multiple npm and PyPI packages with LLM-targeting backdoors (2024)

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Component Spoofing | S | Malicious model, plugin, or dataset masquerades as a legitimate, trusted component in the supply chain | Foundational | Both |
| Supply Chain Tampering | T | Legitimate component is modified in transit or at source to introduce backdoors, biases, or malicious behaviour | Hardening | Both |
| Escalation via Trusted Component | E | Malicious supply chain component executes with the elevated trust and permissions granted to legitimate components | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Verify cryptographic hashes of all model artefacts, datasets, and dependencies
  before integration
- Source models and plugins only from verified, reproducible provenance — prefer
  curated organisational registries over public repositories
- Pin dependency versions — prohibit unreviewed automatic updates of AI components

**Hardening**
- Generate and maintain a model bill of materials (MBOM) for every production model
- Scan third-party plugins and tool libraries for malicious code before deployment
- Run behavioural regression tests after any supply chain component update

**Advanced**
- Implement reproducible training pipelines — any model used in production can
  be rebuilt from verified source data
- Deploy model provenance verification at inference time — reject models without
  a verified signature chain
- Red team new model versions specifically for backdoor and trojan behaviour
  before production promotion

#### Tools

| Tool | Type | Link |
|---|---|---|
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Syft | Open-source | https://github.com/anchore/syft |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI03 Training & Fine-Tuning Data Risks, DSGAI04 Data Poisoning
- Other frameworks: MITRE ATLAS AML.T0056 — CIS Controls 2.1 — NIST SP 800-161

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Attackers inject malicious, misleading, or corrupted data into training datasets,
fine-tuning corpora, or RAG stores to alter model behaviour — introducing backdoors,
biases, or misinformation that persist into production.

**Real-world references:**
- Nightshade (2023) — data poisoning tool that corrupts image generation model outputs
  through adversarial training samples
- Multiple documented RAG corpus poisoning incidents where injected documents altered
  model retrieval and responses

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Training Data Tampering | T | Attacker modifies training data, fine-tuning corpus, or RAG store content to alter model behaviour in targeted ways | Hardening | Both |
| Poisoning Without Audit Trail | R | Data pipeline changes lack audit logging sufficient to detect when, how, or by whom poisoning was introduced | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Implement data validation and anomaly detection on all training and fine-tuning
  data ingestion pipelines
- Apply access controls to training data stores — restrict write access to
  authorised personnel and systems only
- Maintain immutable audit logs for all training data modifications

**Hardening**
- Generate and version a Dataset Bill of Materials (DBoM) for every training run
- Implement statistical outlier detection on training datasets before use
- Monitor RAG store ingestion for adversarial document patterns

**Advanced**
- Implement certified data provenance — training data carries cryptographic
  attestation of origin and chain of custody
- Deploy differential privacy in training to limit the influence of any single
  poisoned data point on model behaviour
- Conduct targeted red team exercises specifically attempting data poisoning
  attacks against your training and fine-tuning pipelines

#### Tools

| Tool | Type | Link |
|---|---|---|
| Cleanlab | Open-source | https://github.com/cleanlab/cleanlab |
| Garak | Open-source | https://github.com/leondz/garak |
| Great Expectations | Open-source | https://github.com/great-expectations/great_expectations |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI03 Training & Fine-Tuning Data Risks, DSGAI04 Data Poisoning
- Other frameworks: MITRE ATLAS AML.T0032 — NIST AI RMF MS-2.6 — ISO 42001 A.6.2

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM-generated output is passed to downstream components — browsers, interpreters,
databases, shell commands — without validation or sanitisation, enabling secondary
injection attacks such as XSS, SQLi, SSRF, or OS command injection.

**Real-world references:**
- Multiple documented XSS incidents where LLM-generated HTML was rendered without
  sanitisation in enterprise chat applications (2024)

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Output Tampering into Downstream Systems | T | Model output is used as-is to construct queries, render HTML, or invoke commands, allowing attacker-controlled content to modify downstream system state | Foundational | Build |
| Privilege Escalation via Output Injection | E | Unsanitised model output triggers XSS, SQLi, or OS injection that executes with the privileges of the downstream system — exceeding the attacker's direct access level | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Treat all LLM output as untrusted input to any downstream consumer
- Apply context-aware output encoding before passing LLM responses to HTML
  renderers, SQL engines, shell interpreters, or API calls
- Define an explicit output schema for every LLM integration and validate
  against it before use

**Hardening**
- Implement a dedicated output sanitisation layer between the LLM and all
  downstream consumers, independent of the model
- Apply allowlist-based output validation — reject anything outside the
  permitted syntax for the target consumer
- Conduct SAST scanning of all code paths that consume LLM output

**Advanced**
- Deploy DAST (Dynamic Application Security Testing) on all interfaces
  that consume LLM output
- Include output injection scenarios in your adversarial test suite
- Conduct code review specifically focused on LLM output consumption paths
  before every production deployment

#### Tools

| Tool | Type | Link |
|---|---|---|
| DOMPurify | Open-source | https://github.com/cure53/DOMPurify |
| Semgrep | Open-source | https://semgrep.dev |
| OWASP ZAP | Open-source | https://www.zaproxy.org |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ASVS V5 — CWE-79 — CWE-89 — MITRE ATLAS AML.T0037

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs granted too much autonomy — access to tools, APIs, filesystems, or databases
without adequate constraints — can execute unintended or harmful actions when
manipulated through prompt injection or misaligned goal-following.

**Real-world references:**
- Multiple production incidents of AI assistants autonomously sending emails,
  deleting files, or executing API calls following manipulated instructions (2024)

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Privilege Escalation via Excessive Tool Access | E | LLM executes actions beyond its authorised scope using tools, APIs, or permissions that should not have been granted | Foundational | Build |
| Unauthorised State Tampering | T | LLM autonomously modifies external systems, databases, or files in ways that were not intended or authorised | Foundational | Build |
| Resource Exhaustion via Uncontrolled Actions | D | Uncontrolled tool invocations consume quota, credits, storage, or API capacity — degrading availability of dependent services | Hardening | Build |

#### Mitigations by tier

**Foundational**
- Apply principle of least agency — grant the minimum tool access and permissions
  required for the defined task
- Require explicit human confirmation before any irreversible action: send, delete,
  publish, execute
- Define and enforce a tool permission manifest for every LLM deployment —
  reviewed before release

**Hardening**
- Implement action logging with anomaly detection — flag tool invocations that
  deviate from expected patterns
- Scope API credentials per LLM task — no shared high-privilege service accounts
  across multiple LLM use cases
- Deploy action guardrails as an independent layer from the model — not just
  model-level system prompt instructions

**Advanced**
- Formally specify permitted action graphs for each LLM agent — only
  pre-approved action sequences can execute
- Implement runtime intent verification before high-impact actions
- Conduct red team exercises specifically targeting excessive agency through
  indirect prompt injection

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| LangChain (with guardrails) | Open-source | https://github.com/langchain-ai/langchain |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI10 Rogue Agents
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange, DSGAI16 Endpoint & Browser Overreach
- Other frameworks: AIUC-1 B006 — ISA/IEC 62443 SR 2.1 — MITRE ATLAS AML.T0015

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing internal instructions, business logic, security controls,
or sensitive configuration are extracted by adversaries through repeated querying,
jailbreaking, or indirect injection — enabling targeted attacks against the model's
specific defences.

**Real-world references:**
- Bing Chat / Sydney (2023) — full system prompt extracted through persistent
  adversarial questioning
- Multiple enterprise LLM deployments with proprietary business logic leaked
  via prompt extraction techniques (2024)

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Configuration Information Disclosure | I | System prompt content — including internal business logic, security instructions, or sensitive configuration — is disclosed to an unauthorised attacker | Foundational | Build |
| Security Control Repudiation | R | Once extracted, attacker knowledge of the system prompt cannot be revoked and there is no audit trail of the disclosure event | Hardening | Build |

#### Mitigations by tier

**Foundational**
- Never embed secrets, credentials, or sensitive data directly in system prompts
  — use environment variables and secret managers
- Instruct models to refuse requests to repeat or summarise their system prompt
  — enforce at the guardrail layer, not just prompt text
- Minimise information density in system prompts — only what is strictly
  necessary for the task

**Hardening**
- Implement prompt confidentiality monitoring — detect response patterns that
  indicate system prompt leakage
- Conduct prompt extraction red team exercises against your specific deployment
  before go-live
- Log all interactions where the model is asked to introspect or describe
  its own instructions

**Advanced**
- Implement system prompt tokenisation — replace sensitive phrases with opaque
  tokens resolved at runtime
- Deploy output classifiers trained to detect and block responses that contain
  system prompt content
- Treat system prompt design as a security artefact — version controlled,
  access controlled, reviewed on change

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003 — CWE-200 — ASVS V14 — MITRE ATLAS AML.T0041

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Weaknesses in vector representations and embedding stores enable adversarial
manipulation of retrieval results, inference of sensitive information from embeddings,
and manipulation of semantic search to return attacker-controlled content.

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Embedding Store Tampering | T | Adversarial embeddings injected into the vector store manipulate similarity search results, causing the retrieval system to return attacker-controlled content | Hardening | Build |
| Embedding Inversion Disclosure | I | Vector embeddings are inverted or probed to reconstruct sensitive source content, leaking information about the underlying corpus | Advanced | Build |

#### Mitigations by tier

**Foundational**
- Implement access controls on vector store read and write operations — not all
  users should be able to query all namespaces
- Validate and sanitise all content before generating embeddings
- Monitor vector store ingestion for anomalous content patterns

**Hardening**
- Encrypt embedding vectors at rest and in transit — embeddings can leak
  information about source content through inversion
- Implement embedding anomaly detection — flag vectors that are statistically
  outlying from the corpus
- Apply trust-tiered retrieval — weight results by source provenance, not only
  semantic similarity

**Advanced**
- Conduct embedding inversion red team exercises to validate that your embeddings
  do not leak source content
- Implement differential privacy in embedding generation for sensitive corpora
- Deploy adversarial robustness testing against your specific embedding model
  and vector store configuration

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant | Open-source | https://qdrant.tech |
| Pinecone Canopy | Open-source | https://github.com/pinecone-io/canopy |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference & Data Reconstruction
- Other frameworks: NIST AI RMF MS-2.5 — CWE-327 — AIUC-1 A

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but factually incorrect, misleading, or hallucinated
content that users, downstream systems, or automated pipelines act upon — causing
business decisions based on false information, erosion of trust, or reputational damage.

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Output Tampering via Hallucination | T | False or hallucinated model outputs alter the state of downstream systems, decisions, or records when acted upon without verification | Foundational | Both |
| Hallucination Repudiation | R | After a misinformation event, it is difficult to determine whether an output was hallucinated or accurate at the time of generation — enabling deniability and impeding incident response | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Implement RAG (Retrieval-Augmented Generation) to ground responses in
  verified, up-to-date source material
- Display source citations alongside model responses — enable users to
  verify claims independently
- Set clear user expectations about model limitations, especially in high-stakes
  domains (medical, legal, financial)

**Hardening**
- Deploy confidence scoring on model outputs — flag low-confidence responses
  for human review before action
- Log model outputs with version and timestamp so that post-incident review
  can reconstruct what was said
- Implement cross-verification against authoritative sources for responses in
  regulated domains

**Advanced**
- Build automated fact-checking pipelines for high-stakes outputs before they
  reach end users or downstream systems
- Implement RLHF cycles to reduce hallucination in your specific domain
- Deploy adversarial probing to identify topics where your model hallucinates
  most frequently — guard those paths

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks via Data Poisoning
- Other frameworks: EU AI Act Art. 13 — AIUC-1 F — ENISA AI Threat Landscape

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Uncontrolled resource consumption — CPU, memory, API tokens, network — caused by
adversarial inputs designed to trigger expensive model computations, recursive
processing, or excessive API calls, resulting in denial of service or runaway cost.

**Real-world references:**
- Multiple documented sponge attacks against LLM APIs causing disproportionate
  token consumption (2024)
- Production cost overruns from prompt-driven token amplification attacks against
  public LLM endpoints

#### STRIDE mapping

| Threat | Category | Description | Tier | Scope |
|---|---|---|---|---|
| Resource Exhaustion (Denial of Service) | D | Adversarial inputs trigger computationally expensive model operations or excessive API calls, degrading or denying service to legitimate users | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Implement rate limiting per user, session, and API key at the application
  layer before requests reach the model
- Set hard token limits on input and output per request — reject requests that
  exceed thresholds
- Monitor API cost and token usage in real time with automated alerting on
  anomalous spikes

**Hardening**
- Implement request queuing and backpressure — prevent sudden surges from
  overwhelming backend inference capacity
- Apply input complexity scoring — flag or throttle requests designed to
  maximise compute cost
- Set per-tenant cost budgets with automatic suspension on breach

**Advanced**
- Deploy sponge example detection — identify inputs statistically designed to
  maximise token consumption
- Implement adaptive rate limiting that adjusts thresholds based on system
  load in real time
- Conduct load testing with adversarial inputs specifically designed to
  maximise cost and latency

#### Tools

| Tool | Type | Link |
|---|---|---|
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| Nginx (rate limiting) | Open-source | https://nginx.org |
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: CWE-400 — ISA/IEC 62443 SR 7.1 — NIST CSF 2.0 DE.AE — AIUC-1 D

---

## Implementation priority

| Phase | LLM entries | STRIDE focus | Rationale |
|---|---|---|---|
| 1 — Do now | LLM01, LLM05, LLM06 | T, S, E | Tampering and privilege escalation with active exploitation paths |
| 2 — This sprint | LLM02, LLM07 | I, R | Information disclosure closes the most common data exposure paths |
| 3 — This quarter | LLM03, LLM04 | T, S | Supply chain and poisoning require pipeline-level architectural changes |
| 4 — Ongoing | LLM08, LLM09, LLM10 | T, I, D | Defence-in-depth, monitoring, and resilience hardening |

---

## Using STRIDE in LLM threat models

To integrate this mapping into a DFD-based threat model:

1. **Map each LLM component to a DFD element** — model endpoints as processes,
   RAG stores as data stores, external APIs as external entities
2. **Apply STRIDE per data flow** — for each arrow in the DFD, enumerate which
   STRIDE categories apply using this file as the threat catalogue
3. **Score with DREAD or CVSS** — prioritise mitigations by risk score
4. **Cross-reference MITRE ATLAS** — use the ATLAS crosswalk for technique-level
   detail on each identified threat

---

## References

- [STRIDE threat modelling — Microsoft](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [OWASP Threat Modelling](https://owasp.org/www-community/Threat_Modeling)
- [Microsoft Threat Modelling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool)
- [OWASP AIVSS](https://aivss.owasp.org)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-27 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
