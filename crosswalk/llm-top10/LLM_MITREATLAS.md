<!--
  GenAI Security Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : MITRE ATLAS — Adversarial Threat Landscape for AI Systems
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × MITRE ATLAS

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to the [MITRE ATLAS](https://atlas.mitre.org) framework — the authoritative
knowledge base of adversary tactics, techniques, and procedures (TTPs)
targeting AI and machine learning systems.

MITRE ATLAS is the primary threat intelligence framework for AI security.
It is maintained by MITRE with contributions from Microsoft, NVIDIA, IBM,
and the broader AI security community. Every LLM vulnerability in the OWASP
Top 10 has one or more direct ATLAS technique mappings, making this the
go-to reference for red teams, threat modellers, and SOC analysts working
on AI systems.

---

## MITRE ATLAS structure

ATLAS organises adversarial AI techniques across a kill chain of tactics:

| Tactic | What it covers |
|---|---|
| Reconnaissance | Gathering information about target AI systems |
| Resource Development | Acquiring capabilities to attack AI systems |
| Initial Access | Gaining entry to AI systems or pipelines |
| ML Attack Staging | Preparing adversarial inputs or poisoned data |
| Execution | Running malicious code or prompts |
| Persistence | Maintaining access to AI systems over time |
| Privilege Escalation | Gaining elevated access within AI systems |
| Defence Evasion | Avoiding detection by AI security controls |
| Discovery | Learning about the target AI environment |
| Collection | Harvesting data from AI systems |
| Exfiltration | Stealing data via AI systems |
| Impact | Disrupting, degrading, or destroying AI functionality |
| Influence Operations | Manipulating AI outputs for deceptive purposes |

---

## Quick-reference summary

| ID | Name | Severity | Primary ATLAS Techniques | Tier | Scope |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | AML.T0051.000, AML.T0051.001, AML.T0054 | Foundational–Advanced | Both |
| LLM02 | Sensitive Information Disclosure | High | AML.T0021, AML.T0030, AML.T0024 | Foundational–Advanced | Both |
| LLM03 | Supply Chain Vulnerabilities | High | AML.T0056, AML.T0048, AML.T0010 | Foundational–Hardening | Both |
| LLM04 | Data and Model Poisoning | Critical | AML.T0032, AML.T0031, AML.T0027 | Hardening–Advanced | Both |
| LLM05 | Insecure Output Handling | High | AML.T0037, AML.T0040 | Foundational–Hardening | Build |
| LLM06 | Excessive Agency | High | AML.T0015, AML.T0068 | Foundational–Hardening | Build |
| LLM07 | System Prompt Leakage | High | AML.T0041, AML.T0051.000 | Foundational–Hardening | Build |
| LLM08 | Vector and Embedding Weaknesses | Medium | AML.T0063, AML.T0025 | Hardening–Advanced | Build |
| LLM09 | Misinformation | Medium | AML.T0045, AML.T0047 | Foundational–Hardening | Both |
| LLM10 | Unbounded Consumption | Medium | AML.T0029, AML.T0034 | Foundational–Hardening | Both |

---

## Audience tags

- **Red teamer** — full file, primary reference for AI adversarial simulation
- **Threat modeller** — full file, use ATLAS techniques as threat catalogue
- **Security engineer** — LLM01, LLM02, LLM04, LLM07
- **Developer** — LLM01, LLM05, LLM06, LLM07
- **SOC analyst** — LLM01, LLM02, LLM04, LLM10
- **ML / AI engineer** — LLM04, LLM08, LLM03
- **OT engineer** — LLM01, LLM04, LLM10 (see ISA 62443 crosswalk for OT context)

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions embedded in user input or processed content
manipulate the LLM's behaviour, bypassing safety measures, executing
unauthorised actions, or leaking data. Direct injection targets the
user input field; indirect injection hides instructions in documents,
emails, RAG content, or web pages the model processes.

**Real-world references:**
- ChatGPT plugin indirect injection (2023) — malicious web content
  hijacked plugin actions
- Samsung source code leak (2023) — employees fed proprietary code
  to LLM, exfiltrated via model outputs
- EchoLeak / Microsoft 365 Copilot (2025) — indirect injection via
  email content caused silent data exfiltration

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| Direct Prompt Injection | [AML.T0051.000](https://atlas.mitre.org/techniques/AML.T0051.000) | Influence Operations | Attacker directly manipulates user-facing prompt to alter model behaviour |
| Indirect Prompt Injection | [AML.T0051.001](https://atlas.mitre.org/techniques/AML.T0051.001) | Influence Operations | Hidden instructions in content the model processes (documents, web, RAG) |
| LLM Jailbreak | [AML.T0054](https://atlas.mitre.org/techniques/AML.T0054) | Execution | Circumventing model safety guardrails via crafted prompt sequences |

#### Mitigations by tier

**Foundational**
- Treat all external content — documents, emails, web results, RAG
  chunks — as untrusted input regardless of source
- Implement input validation and prompt structure enforcement before
  content reaches the model
- Separate system prompt context from user input context at the
  architectural level

**Hardening**
- Deploy runtime prompt injection detection using classifiers or
  heuristic filters on all input channels
- Require human approval before model executes any high-impact action
  triggered by external content
- Maintain adversarial test suite covering direct and indirect injection
  scenarios, run in CI/CD

**Advanced**
- Implement prompt integrity verification — cryptographically signed
  system prompts that cannot be overridden by user input
- Deploy multi-layer defence: input filter + output monitor + action
  guardrail, independent of each other
- Red team quarterly with novel indirect injection scenarios targeting
  your specific RAG and tool configurations

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| PromptBench | Open-source | https://github.com/microsoft/promptbench |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Rebuff | Open-source | https://github.com/protectai/rebuff |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI15 Over-Broad Context Windows
- Other frameworks: MITRE ATT&CK T1059 · STRIDE Tampering/Spoofing · CWE-20 · ASVS V5

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs inadvertently expose PII, financial data, proprietary source code,
API keys, or confidential business information through their outputs —
either from training data memorisation, over-permissive RAG retrieval,
or improperly sanitised responses.

**Real-world references:**
- Samsung source code leak (2023) — proprietary code memorised and
  surfaced in model outputs
- Proof Pudding / CVE-2019-20634 — model inversion attack recovering
  training data

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| Data Leakage | [AML.T0021](https://atlas.mitre.org/techniques/AML.T0021) | Exfiltration | Unintended exposure of training data or sensitive context through model outputs |
| Information Disclosure | [AML.T0030](https://atlas.mitre.org/techniques/AML.T0030) | Collection | Extraction of confidential information via targeted model queries |
| Model Inversion | [AML.T0024](https://atlas.mitre.org/techniques/AML.T0024) | Collection | Reconstructing training data from model outputs or confidence scores |

#### Mitigations by tier

**Foundational**
- Implement output scanning and redaction for PII, secrets, and
  proprietary patterns before responses reach users
- Apply differential privacy techniques during model training to
  limit memorisation of sensitive training data
- Enforce access control on RAG data sources — users should only
  retrieve data they are authorised to see

**Hardening**
- Deploy data loss prevention (DLP) tooling on model output pipelines
- Audit RAG retrieval scope regularly — over-permissive indexes are
  the most common source of disclosure incidents
- Classify all training and retrieval data before ingestion — apply
  handling rules based on classification

**Advanced**
- Implement machine unlearning capability for targeted removal of
  sensitive data from model weights post-training
- Adopt federated learning to avoid centralising sensitive data in
  training pipelines
- Conduct model extraction and inversion red team exercises to
  validate disclosure boundaries

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Amazon Comprehend | Commercial | https://aws.amazon.com/comprehend/ |
| Nightfall AI | Commercial | https://nightfall.ai |
| Private AI | Commercial | https://private-ai.com |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI10 Synthetic Data Pitfalls, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27001 A.8.2 · NIST AI RMF MS-2.5 · CWE-200 · PCIDSS Req 3

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, fine-tuned
adapters, training datasets, libraries, and plugins — any of which
can be compromised to introduce backdoors, biased behaviour, or
malicious functionality before the model reaches production.

**Real-world references:**
- XZ Utils backdoor (2024) — illustrates how supply chain compromise
  in open-source components evades detection
- Hugging Face malicious models — multiple instances of compromised
  model weights uploaded to public repositories

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| Adversarial Model Manipulation | [AML.T0056](https://atlas.mitre.org/techniques/AML.T0056) | ML Attack Staging | Tampering with model weights, adapters, or configurations during supply chain |
| Model Contamination | [AML.T0048](https://atlas.mitre.org/techniques/AML.T0048) | Persistence | Introducing persistent malicious behaviour into model through supply chain |
| Backdoor ML Model | [AML.T0010](https://atlas.mitre.org/techniques/AML.T0010) | Persistence | Embedding trigger-based backdoors in model weights via training or fine-tuning supply chain |

#### Mitigations by tier

**Foundational**
- Maintain a signed ML SBOM (Software Bill of Materials) for every
  model, adapter, dataset, and library in production
- Verify cryptographic signatures of all downloaded model weights
  before deployment
- Pin specific model versions — never pull latest in production without
  review

**Hardening**
- Scan all third-party model weights for known backdoor signatures
  before production promotion
- Implement provenance verification for all training datasets — DBoM
  (Dataset Bill of Materials)
- Conduct integrity checks on all dependencies at build time using
  automated tooling in CI/CD

**Advanced**
- Run sandboxed behavioural evaluation of new model versions before
  production — test against your specific threat scenarios
- Implement model watermarking to detect unauthorised modifications
- Engage in responsible disclosure with model providers for supply
  chain vulnerability reporting

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Snyk | Commercial | https://snyk.io |

#### Cross-references
- Agentic Top 10: ASI04 Agentic Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-218A · BSIMM AM · CycloneDX ML SBOM · CWE-506

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Attackers inject malicious, misleading, or backdoor-triggering data
into training datasets or fine-tuning pipelines — corrupting model
behaviour in ways that are difficult to detect after training. Unlike
prompt injection, the effect is baked into the model weights themselves.

**Real-world references:**
- Adversarial examples achieving 35% success rate in influencing model
  outputs even with defensive mechanisms (2024 research)
- Nightshade (2023) — poison pixels in training images successfully
  corrupted image generation models

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| Data Poisoning | [AML.T0032](https://atlas.mitre.org/techniques/AML.T0032) | ML Attack Staging | Injecting malicious data into training pipelines to corrupt model behaviour |
| Backdoor ML Model | [AML.T0031](https://atlas.mitre.org/techniques/AML.T0031) | Persistence | Embedding hidden trigger-response patterns in model via poisoned training data |
| Model Inversion | [AML.T0027](https://atlas.mitre.org/techniques/AML.T0027) | Collection | Reconstructing sensitive training data from model outputs |

#### Mitigations by tier

**Foundational**
- Validate and audit all training data sources before ingestion —
  apply source allowlisting for critical model training
- Implement data provenance tracking from ingestion through training
  to model version — full lineage
- Run anomaly detection on training datasets to identify unusual
  patterns or outliers before training begins

**Hardening**
- Apply adversarial training — include adversarial examples in
  training data to build model robustness
- Implement multi-stage model validation post-training — test against
  known poisoning signatures before production
- Use differential privacy during training to limit the influence of
  any single training example

**Advanced**
- Conduct post-training backdoor detection using neural cleanse or
  equivalent techniques before every production deployment
- Implement certified robustness mechanisms for high-stakes model
  decisions
- Maintain rollback capability — versioned model registry with ability
  to revert to a known-clean checkpoint

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| BackdoorBench | Open-source | https://github.com/SCLBD/BackdoorBench |
| Great Expectations | Open-source | https://greatexpectations.io |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST AI RMF MS-2.5 · ISO 42001 6.1.2 · CWE-693

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM-generated output is passed to downstream components — browsers,
interpreters, APIs, databases — without sufficient validation or
sanitisation, enabling XSS, command injection, SSRF, or SQL injection
via AI-generated content.

**Real-world references:**
- Multiple bug bounty reports (2024) of XSS via unsanitised LLM
  markdown output rendered in web browsers
- LLM-to-SQL interfaces executing destructive queries from
  AI-generated SQL (see also DSGAI12)

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| Output Manipulation | [AML.T0037](https://atlas.mitre.org/techniques/AML.T0037) | Influence Operations | Crafting inputs that produce dangerous outputs consumed by downstream systems |
| Unsafe Deserialisation via LLM | [AML.T0040](https://atlas.mitre.org/techniques/AML.T0040) | Execution | LLM outputs containing serialised payloads executed by downstream components |

#### Mitigations by tier

**Foundational**
- Treat all LLM output as untrusted input to downstream systems —
  apply the same validation you would to user-supplied data
- Encode and sanitise all LLM output before rendering in browsers
  or passing to interpreters
- Never pass raw LLM output directly to database queries, shell
  commands, or eval functions

**Hardening**
- Implement output schema validation — define and enforce the
  structure of acceptable model responses
- Deploy content security policies (CSP) to limit damage from
  any XSS that reaches the browser
- Apply allowlisting on LLM-generated code before execution —
  reject anything outside the permitted syntax

**Advanced**
- Implement a dedicated output security layer between the LLM and
  all downstream consumers, independent of the model
- Conduct DAST (Dynamic Application Security Testing) on all
  interfaces that consume LLM output
- Include output injection scenarios in your adversarial test suite

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| DOMPurify | Open-source | https://github.com/cure53/DOMPurify |
| Semgrep | Open-source | https://semgrep.dev |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: OWASP ASVS V5 · CWE-79 · CWE-89 · STRIDE Tampering

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs granted too much autonomy — access to tools, APIs, filesystems,
or databases without adequate constraints — can execute unintended or
harmful actions when manipulated through prompt injection or
misaligned goal-following.

**Real-world references:**
- Multiple production incidents of AI assistants autonomously sending
  emails, deleting files, or making API calls following manipulated
  instructions

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| LLM Capability Escalation | [AML.T0015](https://atlas.mitre.org/techniques/AML.T0015) | Privilege Escalation | Exploiting overly permissive LLM tool access to perform actions beyond intended scope |
| Automated Collection | [AML.T0068](https://atlas.mitre.org/techniques/AML.T0068) | Collection | LLM autonomously collecting data beyond its intended access scope |

#### Mitigations by tier

**Foundational**
- Apply principle of least agency — grant the minimum tool access
  and permissions required for the defined task
- Require explicit human confirmation before any irreversible action:
  send, delete, publish, execute
- Define and enforce a tool permission manifest for every LLM
  deployment — reviewed before release

**Hardening**
- Implement action logging with anomaly detection — flag tool
  invocations that deviate from expected patterns
- Scope API credentials per LLM task — no shared high-privilege
  service accounts across multiple LLM use cases
- Deploy action guardrails as an independent layer from the model —
  not just model-level system prompt instructions

**Advanced**
- Formally specify permitted action graphs for each LLM agent — only
  pre-approved action sequences can execute
- Implement runtime intent verification before high-impact actions —
  model must provide a verifiable justification
- Conduct red team exercises specifically targeting excessive agency
  through indirect prompt injection

#### Tools

| Tool | Type | Link |
|---|---|---|
| LangChain (with guardrails) | Open-source | https://github.com/langchain-ai/langchain |
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI10 Rogue Agents
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange, DSGAI16 Endpoint & Browser Overreach
- Other frameworks: AIUC-1 B006 · ISA/IEC 62443 SR 2.1 (OT) · STRIDE Elevation of Privilege

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing internal instructions, business logic,
security controls, or sensitive configuration are extracted by
adversaries through repeated querying, jailbreaking, or indirect
injection — enabling targeted attacks against the model's specific
defences.

**Real-world references:**
- Bing Chat / Sydney (2023) — full system prompt extracted through
  persistent adversarial questioning
- Multiple enterprise LLM deployments with proprietary business
  logic leaked via prompt extraction

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| Configuration Exposure | [AML.T0041](https://atlas.mitre.org/techniques/AML.T0041) | Discovery | Extraction of internal model configuration, instructions, or system prompts |
| Direct Prompt Injection | [AML.T0051.000](https://atlas.mitre.org/techniques/AML.T0051.000) | Influence Operations | Crafting inputs specifically designed to reveal or override system prompt content |

#### Mitigations by tier

**Foundational**
- Never embed secrets, credentials, or sensitive data directly in
  system prompts — use environment variables and secret managers
- Instruct models to refuse requests to repeat or summarise their
  system prompt — enforce at the guardrail layer, not just prompt
- Minimise information density in system prompts — only what is
  strictly necessary for the task

**Hardening**
- Implement prompt confidentiality monitoring — detect response
  patterns that indicate system prompt leakage
- Conduct prompt extraction red team exercises against your specific
  deployment before go-live
- Rotate system prompt versions periodically — limits the shelf life
  of extracted prompts

**Advanced**
- Implement system prompt tokenisation — replace sensitive phrases
  with opaque tokens resolved at runtime
- Deploy output classifiers trained to detect and block responses
  that contain system prompt content
- Treat system prompt design as a security artefact — version
  controlled, access controlled, reviewed on change

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003 · CWE-200 · OWASP ASVS V14

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Weaknesses in vector representations and embedding stores enable
adversarial manipulation of retrieval results, inference of sensitive
information from embeddings, and manipulation of semantic search
to return attacker-controlled content.

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| Embedding Manipulation | [AML.T0063](https://atlas.mitre.org/techniques/AML.T0063) | ML Attack Staging | Crafting inputs whose embeddings manipulate similarity search results |
| Resource Exhaustion via Embedding | [AML.T0025](https://atlas.mitre.org/techniques/AML.T0025) | Impact | Flooding vector stores with adversarial embeddings to degrade retrieval quality |

#### Mitigations by tier

**Foundational**
- Implement access controls on vector store read and write operations —
  not all users should be able to query all namespaces
- Validate and sanitise all content before generating embeddings —
  garbage in, garbage out applies to vector stores too
- Monitor vector store ingestion for anomalous content patterns

**Hardening**
- Encrypt embedding vectors at rest and in transit — embeddings can
  leak information about source content through inversion
- Implement embedding anomaly detection — flag vectors that are
  statistically outlying from the corpus
- Apply trust-tiered retrieval — weight results by source provenance,
  not only semantic similarity

**Advanced**
- Conduct embedding inversion red team exercises to validate that
  your embeddings do not leak source content
- Implement differential privacy in embedding generation for sensitive
  corpora
- Deploy adversarial robustness testing against your specific
  embedding model and vector store configuration

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Qdrant | Open-source | https://qdrant.tech |
| Pinecone Canopy | Open-source | https://github.com/pinecone-io/canopy |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security, DSGAI18 Inference & Data Reconstruction
- Other frameworks: NIST AI RMF MS-2.5 · AIUC-1 A · CWE-327

---

### LLM09 — Misinformation

**Severity:** Medium

LLMs generate plausible but factually incorrect, misleading, or
hallucinated content that users, downstream systems, or automated
pipelines act upon — causing business decisions based on false
information, erosion of trust, or reputational damage.

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| Disinformation | [AML.T0045](https://atlas.mitre.org/techniques/AML.T0045) | Influence Operations | Using AI-generated content to deliberately spread false information |
| Influence via Automated Content | [AML.T0047](https://atlas.mitre.org/techniques/AML.T0047) | Influence Operations | Generating high-volume automated content to shape perception or overwhelm fact-checking |

#### Mitigations by tier

**Foundational**
- Implement RAG (Retrieval-Augmented Generation) to ground responses
  in verified, up-to-date source material
- Display source citations alongside model responses — enable users
  to verify claims independently
- Set clear user expectations about model limitations — especially
  in high-stakes domains (medical, legal, financial)

**Hardening**
- Deploy confidence scoring on model outputs — flag low-confidence
  responses for human review before action
- Implement cross-verification against authoritative sources for
  responses in regulated domains
- Monitor for hallucination patterns in production — track fact
  accuracy metrics over time

**Advanced**
- Build automated fact-checking pipelines for high-stakes outputs
  before they reach end users or downstream systems
- Implement RLHF (Reinforcement Learning from Human Feedback) cycles
  to reduce hallucination in your specific domain
- Deploy adversarial probing to identify topics where your model
  hallucinates most frequently — guard those paths

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks via Data Poisoning
- Other frameworks: EU AI Act Art. 13 · AIUC-1 F · ENISA AI Threat Landscape

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Uncontrolled resource consumption — CPU, memory, API tokens, network
— caused by adversarial inputs designed to trigger expensive model
computations, recursive processing, or excessive API calls, resulting
in denial of service or runaway cost.

**Real-world references:**
- Multiple documented sponge attacks against LLM APIs causing
  disproportionate token consumption (2024)
- Production cost overruns from prompt-driven token amplification
  attacks against public LLM endpoints

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Description |
|---|---|---|---|
| Denial of ML Service | [AML.T0029](https://atlas.mitre.org/techniques/AML.T0029) | Impact | Overloading AI systems with computationally expensive inputs to cause service degradation |
| Cost Harvesting | [AML.T0034](https://atlas.mitre.org/techniques/AML.T0034) | Impact | Crafting inputs that maximise token usage or API costs per request |

#### Mitigations by tier

**Foundational**
- Implement rate limiting per user, session, and API key at the
  application layer before requests reach the model
- Set hard token limits on input and output per request — reject
  requests that exceed thresholds
- Monitor API cost and token usage in real time with automated
  alerting on anomalous spikes

**Hardening**
- Implement request queuing and backpressure — prevent sudden surges
  from overwhelming backend inference capacity
- Apply input complexity scoring — flag or throttle requests that
  appear designed to maximise compute cost
- Set per-tenant cost budgets with automatic suspension on breach

**Advanced**
- Deploy sponge example detection — identify inputs statistically
  designed to maximise token consumption
- Implement adaptive rate limiting that adjusts thresholds based on
  system load in real time
- Conduct load testing with adversarial inputs specifically designed
  to maximise cost and latency

#### Tools

| Tool | Type | Link |
|---|---|---|
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| Nginx (rate limiting) | Open-source | https://nginx.org |
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: CWE-400 · ISA/IEC 62443 SR 7.1 (OT) · NIST SP 800-82 (OT) · AIUC-1 D

---

## Implementation priority

| Phase | LLM entries | Rationale |
|---|---|---|
| 1 — Do now | LLM01, LLM06, LLM07 | Highest exploitability, most active in the wild |
| 2 — This sprint | LLM02, LLM05 | Data exposure and output handling close the most common breach paths |
| 3 — This quarter | LLM03, LLM04 | Supply chain and poisoning require pipeline-level changes |
| 4 — Ongoing | LLM08, LLM09, LLM10 | Defence-in-depth, monitoring, and resilience hardening |

---

## ATLAS navigator layer

A MITRE ATT&CK Navigator layer file for all techniques in this
mapping is available at:
`data/llm-top10/atlas-navigator-layer.json`

This can be imported directly into
[MITRE ATLAS Navigator](https://mitre-atlas.github.io/atlas-navigator/)
to visualise coverage across the LLM Top 10.

---

## References

- [MITRE ATLAS](https://atlas.mitre.org)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [OWASP AI Testing Guide](https://owasp.org/www-project-ai-testing-guide/)
- [OWASP AIVSS](https://aivss.owasp.org)
- [MITRE ATLAS case studies](https://atlas.mitre.org/studies/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
