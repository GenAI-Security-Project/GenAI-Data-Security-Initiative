<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for LLM Applications 2025 (LLM01–LLM10)
  Framework   : ISO/IEC 27001:2022 — Information Security Management Systems
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# LLM Top 10 2025 × ISO/IEC 27001:2022

Mapping the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
to [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html) — the world's most
widely deployed information security management system standard,
certified by over 70,000 organisations globally.

ISO 27001:2022 is the baseline certification for enterprise supplier
assessments, regulated industry compliance, and public sector
procurement worldwide. Its 2022 revision introduced 11 new Annex A
controls — including A.8.11 data masking, A.8.12 data leakage
prevention, A.5.7 threat intelligence, and A.8.28 secure coding —
that map directly to LLM application security requirements.

This file covers LLM01–LLM10 mapped to ISO 27001:2022 Annex A controls.
For the DSGAI 2026 × ISO 27001 mapping covering the full GenAI data
security surface, see `dsgai-2026/DSGAI_ISO27001.md`.

---

## ISO 27001:2022 Annex A domains

| Domain | Controls | Scope |
|---|---|---|
| A.5 Organisational | A.5.1–A.5.37 | Policies, roles, supplier security, threat intel, incident management |
| A.6 People | A.6.1–A.6.8 | Screening, training, remote working |
| A.7 Physical | A.7.1–A.7.14 | Physical access, secure areas, equipment |
| A.8 Technological | A.8.1–A.8.34 | Access, cryptography, logging, secure development, DLP |

**New in 2022 most relevant to LLMs:**
A.5.7 Threat intelligence · A.5.23 Cloud services security ·
A.8.11 Data masking · A.8.12 Data leakage prevention ·
A.8.16 Monitoring activities · A.8.28 Secure coding

---

## Quick-reference summary

| ID | Name | Severity | Primary ISO 27001:2022 Controls | Tier | Scope |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | Critical | A.8.28, A.8.29, A.5.7, A.8.16 | Foundational–Advanced | Both |
| LLM02 | Sensitive Information Disclosure | High | A.8.11, A.8.12, A.5.12, A.8.3 | Foundational–Advanced | Both |
| LLM03 | Supply Chain Vulnerabilities | High | A.5.19, A.5.20, A.5.21, A.8.8 | Foundational–Hardening | Both |
| LLM04 | Data and Model Poisoning | Critical | A.8.8, A.8.27, A.8.29, A.5.7 | Hardening–Advanced | Both |
| LLM05 | Insecure Output Handling | High | A.8.28, A.8.26, A.8.29, A.8.16 | Foundational–Hardening | Build |
| LLM06 | Excessive Agency | High | A.8.2, A.5.10, A.8.15, A.5.15 | Foundational–Hardening | Build |
| LLM07 | System Prompt Leakage | High | A.5.12, A.8.3, A.8.24, A.8.15 | Foundational–Hardening | Build |
| LLM08 | Vector and Embedding Weaknesses | Medium | A.8.3, A.8.24, A.8.16, A.8.11 | Hardening–Advanced | Build |
| LLM09 | Misinformation | Medium | A.8.16, A.5.7, A.6.3, A.5.36 | Foundational–Hardening | Both |
| LLM10 | Unbounded Consumption | Medium | A.8.16, A.5.30, A.8.13, A.5.24 | Foundational–Hardening | Both |

---

## Audience tags

- **CISO / governance** — full file, ISO 27001 ISMS extension for LLM applications
- **Auditor / certifier** — control mapping evidence for ISO 27001 certification audits
- **Security engineer** — A.8 technological controls per vulnerability
- **Developer** — A.8.28 secure coding, A.8.26 application security requirements
- **Compliance officer** — A.5 organisational controls, supplier management entries
- **OT engineer** — LLM01, LLM04, LLM10 with ISA 62443 crosswalk for OT context

---

## Detailed mappings

---

### LLM01 — Prompt Injection

**Severity:** Critical

Malicious instructions in user input or processed content manipulate
LLM behaviour, bypassing safety controls and executing unauthorised
actions. ISO 27001 addresses this through secure coding requirements,
security testing, threat intelligence, and monitoring controls.

**Real-world references:**
- EchoLeak (2025) — indirect injection via email turned Microsoft 365
  Copilot into a silent exfiltration engine
- Samsung source code leak (2023) — proprietary code surfaced through
  manipulated model queries

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Secure coding | A.8.28 | Technological | Secure coding requirements for all LLM integration code — input validation, sanitisation, context separation |
| Security testing | A.8.29 | Technological | Adversarial testing programme covering prompt injection scenarios before each release |
| Threat intelligence | A.5.7 | Organisational | Active intelligence on prompt injection techniques — new attack patterns inform detection controls |
| Monitoring activities | A.8.16 | Technological | Runtime monitoring for prompt injection indicators in LLM inputs and outputs |

#### Mitigations by tier

**Foundational**
- A.8.28: Implement input validation and prompt structure
  enforcement as secure coding requirements — enforce through
  code review and CI/CD gates, not just guidelines
- A.5.7: Subscribe to threat intelligence feeds covering
  prompt injection techniques — new methods inform filter
  updates and adversarial test cases
- Treat all external content processed by the LLM as untrusted —
  documents, emails, web results, and RAG chunks regardless
  of source

**Hardening**
- A.8.29: Include prompt injection scenarios in security
  testing programme — direct, indirect, and jailbreak vectors
  tested before each production release
- A.8.16: Deploy runtime monitoring for injection indicators
  on all input channels — alerts integrated into incident
  management workflow
- Implement architectural separation between system prompt
  and user input — structural control at the code level

**Advanced**
- A.8.29: Extend adversarial testing to cover your specific
  RAG sources, tool descriptors, and document processing
  pipelines — not just generic injection scenarios
- A.5.7: Use threat intelligence to drive quarterly red team
  exercises — novel injection techniques tested before they
  reach production
- Document prompt injection controls in ISMS as a formal
  security objective with measurable targets

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Rebuff | Open-source | https://github.com/protectai/rebuff |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI15 Over-Broad Context Windows
- Other frameworks: NIST AI RMF MS-2.5 · MITRE ATLAS AML.T0051 · CWE-20

---

### LLM02 — Sensitive Information Disclosure

**Severity:** High

LLMs expose PII, financial data, proprietary code, or confidential
information through outputs — from training data memorisation,
over-permissive RAG retrieval, or improperly sanitised responses.

**Real-world references:**
- Samsung source code leak (2023)
- Multiple healthcare RAG deployments surfacing PHI through
  over-permissive vector store retrieval (2024)

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Data masking | A.8.11 | Technological | Output redaction for PII and sensitive patterns before responses reach users |
| Data leakage prevention | A.8.12 | Technological | DLP on all LLM output channels — API, chat interface, logs |
| Classification of information | A.5.12 | Organisational | All data in LLM scope classified — training data, RAG sources, outputs, embeddings |
| Information access restriction | A.8.3 | Technological | Access controls on RAG retrieval — users retrieve only data they are authorised to access |

#### Mitigations by tier

**Foundational**
- A.5.12: Classify all data entering LLM scope before
  ingestion — training corpora, RAG sources, prompt templates,
  and outputs — apply handling requirements per classification
- A.8.3: Implement access controls on RAG data sources —
  users should only retrieve documents they are authorised
  to access, enforced at the retrieval layer
- A.8.12: Deploy DLP on all model output channels — scan
  for PII and sensitive patterns before responses are delivered

**Hardening**
- A.8.11: Implement output redaction for sensitive patterns —
  PII, API keys, internal system names masked before responses
  leave the LLM service boundary
- Audit RAG access controls per sprint — verify retrieval
  scope matches authorised user access rights
- Classify embeddings and derived assets at the same level
  as source documents — A.5.12 propagation requirement

**Advanced**
- Apply differential privacy in training and embedding
  generation for sensitive corpora — document as A.8.11
  technical control evidence
- Conduct model inversion red team exercises — validate that
  sensitive training data cannot be reconstructed from outputs
- A.8.12: Implement real-time DLP with automated blocking —
  not just alerting — on sensitive pattern detection

#### Tools

| Tool | Type | Link |
|---|---|---|
| Microsoft Presidio | Open-source | https://github.com/microsoft/presidio |
| Nightfall AI | Commercial | https://nightfall.ai |
| Private AI | Commercial | https://private-ai.com |

#### Cross-references
- Agentic Top 10: ASI03 Identity & Privilege Abuse
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI18 Inference & Data Reconstruction
- Other frameworks: ISO 27701 · EU AI Act Art. 10 · NIST AI RMF GV-1.6 · GDPR Art. 25

---

### LLM03 — Supply Chain Vulnerabilities

**Severity:** High

LLM applications depend on third-party model weights, fine-tuned
adapters, training datasets, libraries, and plugins — any of which
can be compromised to introduce backdoors or malicious functionality.

**Real-world references:**
- Multiple malicious models with embedded backdoors uploaded to
  public model repositories (2024)
- XZ Utils backdoor — illustrates how open-source supply chain
  compromise evades long-term detection

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Supplier relationships | A.5.19 | Organisational | Security requirements applied to all LLM model and data vendors — provenance, integrity, disclosure obligations |
| Supplier agreements | A.5.20 | Organisational | Contractual security requirements for LLM component suppliers — integrity guarantees, vulnerability notification |
| Supply chain security | A.5.21 | Organisational | Managing ICT supply chain risks — LLM model and library supply chain explicitly in scope |
| Management of technical vulnerabilities | A.8.8 | Technological | Scanning and patching LLM component vulnerabilities — model weights and inference runtime libraries |

#### Mitigations by tier

**Foundational**
- A.5.19: Apply supplier security requirements to all LLM
  component vendors — source documentation, integrity
  guarantees, and vulnerability disclosure obligations
  required before any component enters production
- A.8.8: Maintain ML SBOM for every production LLM deployment —
  model, adapters, datasets, inference libraries — and
  scan against known vulnerability databases
- Pin all component versions — no automatic updates in
  production without review and approval

**Hardening**
- A.5.20: Include LLM-specific requirements in supplier
  contracts — model provenance documentation, backdoor
  scanning attestation, security testing coverage statement
- A.5.21: Develop a supply chain security plan for LLM
  components covering procurement, testing, deployment,
  update, and decommission lifecycle
- Implement cryptographic signature verification for all
  LLM components before deployment

**Advanced**
- A.5.19: Conduct periodic security assessments of strategic
  LLM component suppliers — include in supplier management
  programme with defined assessment cadence
- Operate isolated model evaluation environment — backdoor
  detection testing before each production promotion
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
- Other frameworks: NIST AI RMF MP-5.1 · NIST SP 800-218A · CycloneDX ML SBOM

---

### LLM04 — Data and Model Poisoning

**Severity:** Critical

Attackers inject malicious data into training datasets or fine-tuning
pipelines — corrupting model behaviour in ways baked into the weights
and invisible to standard testing until a trigger condition is reached.

**Real-world references:**
- Nightshade (2023) — poison pixels in training images corrupted
  image generation model behaviour
- Adversarial examples achieving 35% success rate influencing
  model outputs even with defensive mechanisms

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Management of technical vulnerabilities | A.8.8 | Technological | Training pipeline dependency scanning — vulnerabilities in training infrastructure components |
| Secure system architecture | A.8.27 | Technological | Training pipeline designed with integrity controls — data validation, source allowlisting, lineage tracking |
| Security testing | A.8.29 | Technological | Adversarial testing covering poisoning detection before each production model promotion |
| Threat intelligence | A.5.7 | Organisational | Intelligence on active data poisoning campaigns targeting your sector and model type |

#### Mitigations by tier

**Foundational**
- A.8.27: Design training pipelines with integrity controls —
  source allowlisting, anomaly detection on data distributions,
  cryptographic lineage from source to training dataset
- Apply supplier security requirements (A.5.19) to all
  training data sources — provenance, quality, and integrity
  guarantees required before data enters training pipelines
- Implement model rollback capability — versioned model
  registry with clean checkpoint restore on detection

**Hardening**
- A.8.29: Include poisoning detection in security testing
  programme — backdoor trigger testing and biased output
  detection before every production model promotion
- A.8.8: Apply continuous vulnerability monitoring to training
  pipeline dependencies — alert on compromised components
- Apply differential privacy during training — document
  as A.8.11 data masking control evidence

**Advanced**
- Conduct post-training backdoor detection as a mandatory
  pre-deployment gate — neural cleanse or equivalent
- A.5.7: Use threat intelligence to identify poisoning
  campaigns targeting your training data sources — proactive
  source validation based on intelligence signals
- Include model poisoning in ISMS risk register as a
  formal risk with documented treatment and review cadence

#### Tools

| Tool | Type | Link |
|---|---|---|
| IBM Adversarial Robustness Toolbox | Open-source | https://github.com/Trusted-AI/adversarial-robustness-toolbox |
| CleanLab | Open-source | https://github.com/cleanlab/cleanlab |
| Great Expectations | Open-source | https://greatexpectations.io |

#### Cross-references
- Agentic Top 10: ASI06 Memory & Context Poisoning
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI21 Disinformation via Data Poisoning
- Other frameworks: NIST AI RMF MS-3.3 · MITRE ATLAS AML.T0032 · ISO 42001 6.1.2

---

### LLM05 — Insecure Output Handling

**Severity:** High

LLM output passed to downstream systems without validation enables
XSS, command injection, SSRF, or SQL injection via AI-generated
content.

**Real-world references:**
- Multiple bug bounty reports of XSS via unsanitised LLM markdown
  output rendered in web browsers (2024)
- LLM-to-SQL interfaces executing destructive queries from
  AI-generated SQL

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Secure coding | A.8.28 | Technological | Output encoding, sanitisation, and schema validation as secure coding requirements |
| Application security requirements | A.8.26 | Technological | Security requirements for all interfaces consuming LLM output — specified before development |
| Security testing | A.8.29 | Technological | Output injection scenarios in security testing — XSS, SQL injection, command injection via LLM output |
| Monitoring activities | A.8.16 | Technological | Runtime monitoring for output handling incidents — injection attempts in LLM output channels |

#### Mitigations by tier

**Foundational**
- A.8.28: Establish secure coding requirements mandating that
  all LLM output is treated as untrusted input to downstream
  systems — encoding, validation, and sanitisation mandatory
- A.8.26: Define security requirements for all application
  interfaces that consume LLM output before development —
  specify acceptable output formats, validation requirements
- Never pass raw LLM output to database queries, shell
  commands, or eval functions — enforced through code review

**Hardening**
- A.8.29: Include output injection scenarios in security
  testing programme — XSS, SQL injection, and command
  injection via LLM output tested on each significant release
- A.8.16: Deploy runtime monitoring on all LLM output
  channels — detect injection patterns in model responses
  before they reach downstream consumers
- Implement output schema validation — reject responses
  that do not conform to defined safe structures

**Advanced**
- Conduct DAST on all interfaces consuming LLM output —
  include in A.8.29 security testing programme
- Deploy dedicated output security layer independent of
  the LLM — A.8.27 secure architecture principle applied
  to output handling
- A.8.28: Include output security in developer training —
  specific module on LLM output injection risks and mitigations

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP ZAP | Open-source | https://www.zaproxy.org |
| Semgrep | Open-source | https://semgrep.dev |
| DOMPurify | Open-source | https://github.com/cure53/DOMPurify |

#### Cross-references
- Agentic Top 10: ASI02 Tool Misuse, ASI05 Unexpected Code Execution
- DSGAI 2026: DSGAI05 Data Integrity & Validation Failures, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: OWASP ASVS V5 · NIST AI RMF MS-2.6 · CWE-79

---

### LLM06 — Excessive Agency

**Severity:** High

LLMs granted too much autonomy over tools, APIs, and systems execute
unintended or harmful actions when manipulated through prompt injection
or misaligned goal-following.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Privileged access rights | A.8.2 | Technological | LLM tool access managed as privileged access — minimum scope, reviewed regularly |
| Acceptable use of assets | A.5.10 | Organisational | Policy defining acceptable LLM autonomous actions — approved tool use cases documented |
| Logging | A.8.15 | Technological | All LLM tool invocations logged with full context — every tool call auditable |
| Identity management | A.5.15 | Organisational | LLM tool access governed through identity management — tool permissions scoped per deployment |

#### Mitigations by tier

**Foundational**
- A.8.2: Manage LLM tool access as privileged access —
  minimum scope enforced, regular access reviews, no
  standing broad permissions
- A.5.10: Establish acceptable use policy for LLM autonomous
  actions — approved tool use cases documented, human
  confirmation required for irreversible actions
- A.8.15: Log all LLM tool invocations with full context —
  tool identity, parameters, user session, timestamp —
  immutable audit trail

**Hardening**
- A.5.15: Govern LLM tool permissions through identity
  management — tool access scoped per deployment, reviewed
  on change and quarterly
- Implement action guardrails as an independent layer from
  the model — A.8.27 secure architecture applied to
  autonomous action scope
- Define and enforce a tool permission manifest for every
  LLM deployment — reviewed before each release

**Advanced**
- A.8.2: Include LLM tool access in privileged access
  reviews — any permission not actively used is removed
- Formally specify permitted action graphs — only
  pre-approved action sequences can execute in production
- Conduct red team exercises testing excessive agency via
  indirect prompt injection — document results in ISMS
  security testing records

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| LangSmith | Commercial | https://smith.langchain.com |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI10 Rogue Agents
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: AIUC-1 B006 · MITRE ATLAS AML.T0015 · ISA/IEC 62443 SR 2.1 (OT)

---

### LLM07 — System Prompt Leakage

**Severity:** High

System prompts containing internal instructions, business logic, or
security controls are extracted by adversaries — enabling targeted
attacks against specific defences.

**Real-world references:**
- Bing Chat / Sydney (2023) — full system prompt extracted through
  persistent adversarial questioning
- Multiple enterprise LLM deployments with proprietary business
  logic leaked via prompt extraction

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Classification of information | A.5.12 | Organisational | System prompts classified as sensitive configuration — subject to data governance policy |
| Information access restriction | A.8.3 | Technological | Access controls on system prompt storage — version controlled, access logged |
| Use of cryptography | A.8.24 | Technological | System prompts encrypted at rest — not stored in cleartext configuration files |
| Logging | A.8.15 | Technological | Access to system prompts logged — unauthorised access attempts detectable |

#### Mitigations by tier

**Foundational**
- A.5.12: Classify system prompts as sensitive operational
  configuration — subject to the same access controls as
  application secrets and configuration data
- A.8.24: Encrypt system prompts at rest — never stored
  in cleartext source code, configuration files, or
  environment variables without encryption
- A.8.3: Implement version control and access controls
  on system prompt storage — who can read, who can modify,
  all access logged

**Hardening**
- A.8.15: Protect and retain system prompt access logs —
  detect and alert on anomalous access attempts
- Conduct prompt extraction testing before each deployment —
  verify that transparency obligations can be met without
  disclosing security-sensitive configuration
- Remove all secrets, credentials, and sensitive data from
  system prompts — use environment variables and secret
  managers instead

**Advanced**
- Implement system prompt tokenisation — sensitive phrases
  replaced with opaque tokens resolved at runtime
- Deploy output classifiers trained to detect and block
  responses containing system prompt content
- A.5.12: Include system prompt security in ISMS design
  reviews — formal security objective with measurable
  extraction resistance targets

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- Agentic Top 10: ASI01 Agent Goal Hijack
- DSGAI 2026: DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B003/B009 · NIST AI RMF GV-1.6 · CWE-200

---

### LLM08 — Vector and Embedding Weaknesses

**Severity:** Medium

Weaknesses in vector stores enable adversarial retrieval manipulation,
inference of sensitive information from embeddings, and semantic
search poisoning to return attacker-controlled content.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Information access restriction | A.8.3 | Technological | RBAC on all vector store collections — no unauthenticated access to any collection |
| Use of cryptography | A.8.24 | Technological | Encryption of all vector store data at rest and in transit |
| Monitoring activities | A.8.16 | Technological | Anomaly detection on vector store query patterns — bulk extraction and poisoning indicators |
| Data masking | A.8.11 | Technological | Differential privacy in embedding generation for sensitive corpora |

#### Mitigations by tier

**Foundational**
- A.8.3: Enable RBAC on all vector store collections —
  no unauthenticated access in any environment including
  development
- A.8.24: Encrypt all vector store content at rest and
  in transit — embeddings can leak source content through
  inversion attacks if unencrypted
- Validate and sanitise all content before generating
  embeddings — quality and security controls at ingestion

**Hardening**
- A.8.16: Implement anomaly detection on vector store
  query patterns — alert on bulk extraction, unusual query
  diversity, or high-volume confidence score harvesting
- Apply trust-tiered retrieval — weight results by source
  provenance and trust score, not only semantic similarity
- Conduct embedding inversion testing — validate that
  embeddings do not reconstruct sensitive source content

**Advanced**
- Apply differential privacy in embedding generation —
  document privacy budget as A.8.11 masking control evidence
- A.8.16: Integrate vector store anomaly alerts into SIEM —
  unusual retrieval patterns treated as potential
  reconnaissance or extraction activity
- Conduct adversarial retrieval testing — attempt to
  manipulate retrieval results through crafted queries

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

LLMs generate plausible but factually incorrect or hallucinated
content that users, downstream systems, or automated pipelines
act upon — causing incorrect decisions, erosion of trust, or
reputational harm.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Monitoring activities | A.8.16 | Technological | Production monitoring for output accuracy — hallucination rate tracking, anomaly detection on model drift |
| Threat intelligence | A.5.7 | Organisational | Intelligence on disinformation campaigns and active manipulation of RAG sources |
| Information security awareness training | A.6.3 | People | User training on LLM output limitations — verification requirements and critical evaluation |
| Compliance with policies | A.5.36 | Organisational | Policy on AI-generated content accuracy — disclosure requirements, human verification thresholds |

#### Mitigations by tier

**Foundational**
- A.5.36: Establish policy on LLM content accuracy — define
  domains requiring human verification before action, especially
  medical, legal, financial, and safety-critical contexts
- A.6.3: Provide awareness training on LLM output limitations —
  all users of LLM decision-support tools trained before
  access is granted
- Deploy RAG grounded on authoritative, version-controlled
  sources — display citations alongside responses

**Hardening**
- A.8.16: Implement production monitoring for hallucination
  patterns — track accuracy metrics per domain, alert on
  significant drift from baseline
- A.5.7: Monitor threat intelligence for disinformation
  campaigns targeting your RAG sources — proactive source
  validation based on intelligence signals
- Implement confidence scoring — low-confidence responses
  flagged for human review before action

**Advanced**
- Build automated fact-checking pipelines for high-stakes
  output domains — accuracy gates before responses reach
  regulated or safety-critical decision workflows
- A.8.16: Implement continuous drift detection — alert when
  hallucination rates exceed defined thresholds per domain
- Include misinformation scenarios in ISMS risk register —
  formal risk with defined treatment and measurement criteria

#### Tools

| Tool | Type | Link |
|---|---|---|
| TruLens | Open-source | https://github.com/truera/trulens |
| RAGAS | Open-source | https://github.com/explodinggradients/ragas |
| DeepEval | Open-source | https://github.com/confident-ai/deepeval |

#### Cross-references
- Agentic Top 10: ASI09 Human-Agent Trust Exploitation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · AIUC-1 F · NIST AI RMF GV-1.7

---

### LLM10 — Unbounded Consumption

**Severity:** Medium

Adversarial inputs trigger disproportionate resource consumption —
CPU, memory, tokens, API costs — causing denial of service or
runaway cost in production LLM deployments.

**Real-world references:**
- Multiple documented sponge attacks against LLM APIs causing
  disproportionate token consumption (2024)
- Production cost overruns from prompt-driven token amplification
  attacks against public LLM endpoints

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Monitoring activities | A.8.16 | Technological | Real-time monitoring of LLM resource consumption — cost anomaly detection and alerting |
| ICT readiness for business continuity | A.5.30 | Organisational | LLM availability requirements in BCP — RTO/RPO defined, rate limiting as resilience control |
| Backup | A.8.13 | Technological | Backup and recovery for LLM service infrastructure — failover capability tested |
| Incident management | A.5.24 | Organisational | Incident response procedures for LLM availability failures and cost overruns |

#### Mitigations by tier

**Foundational**
- A.8.16: Implement real-time monitoring of LLM resource
  consumption — API token usage, compute cost, request
  rates — with automated alerting on anomalous spikes
- Implement rate limiting per user, session, and API key —
  hard caps enforced before requests reach the model
- Set hard token limits on input and output per request —
  reject requests exceeding thresholds at the API gateway

**Hardening**
- A.5.30: Include LLM services in BCP — define RTO and RPO,
  implement circuit breakers, test failover procedures
- A.5.24: Define incident response for consumption anomalies —
  automated rate limit tightening, session suspension, cost
  circuit breakers, owner notification workflow
- Implement per-tenant cost budgets with automatic suspension
  on breach — not just alerting

**Advanced**
- A.8.16: Deploy sponge example detection — identify inputs
  statistically designed to maximise token consumption and
  reject before inference
- Conduct adversarial cost-maximisation testing — identify
  inputs generating maximum token consumption for your model
  and guard those paths
- A.5.30: Include LLM availability SLAs in operational policy —
  reviewed quarterly against actual consumption data

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Kong Gateway | Open-source | https://github.com/Kong/kong |
| OpenTelemetry | Open-source | https://opentelemetry.io |

#### Cross-references
- Agentic Top 10: ASI08 Cascading Agent Failures
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.6 (OT) · NIST SP 800-82 (OT) · CWE-400

---

## ISO 27001 ISMS extension checklist for LLM applications

### Scope and asset management

- [ ] LLM assets added to A.5.9 asset inventory — model versions, APIs, RAG sources
- [ ] Classification policy extended to LLM training data, embeddings, and outputs
- [ ] Data flow maps updated to include all LLM data paths

### Policy and governance

- [ ] Acceptable use policy updated to include LLM tool access (A.5.10)
- [ ] Supplier agreements updated for LLM vendors (A.5.20)
- [ ] AI content accuracy policy published (A.5.36)
- [ ] LLM governance included in ISMS scope statement

### Technical controls

- [ ] Output DLP deployed on all LLM output channels (A.8.12)
- [ ] Output masking / redaction implemented (A.8.11)
- [ ] RAG access controls verified — retrieval scope matches user authorisation
- [ ] Vector store RBAC and encryption confirmed (A.8.3, A.8.24)
- [ ] Privileged access review applied to LLM tool permissions (A.8.2)
- [ ] System prompts encrypted and access-controlled (A.8.24, A.8.3)

### Testing and monitoring

- [ ] Prompt injection in security testing programme (A.8.29)
- [ ] Output injection in security testing programme (A.8.29)
- [ ] Supply chain integrity verification for LLM components (A.5.19)
- [ ] Production monitoring active for LLM resource consumption (A.8.16)
- [ ] Incident response procedures updated for LLM-specific scenarios (A.5.24)

---

## Implementation priority

| Phase | LLM entries | Controls | Rationale |
|---|---|---|---|
| 1 — Do now | LLM01, LLM06, LLM07 | A.8.28, A.8.2, A.5.12 | Highest exploitability, most active in wild |
| 2 — This sprint | LLM02, LLM05 | A.8.11/A.8.12, A.8.26 | Data exposure and output handling close common breach paths |
| 3 — This quarter | LLM03, LLM04 | A.5.19/A.5.21, A.8.27 | Supply chain and poisoning require pipeline-level changes |
| 4 — Ongoing | LLM08, LLM09, LLM10 | A.8.16, A.5.30, A.6.3 | Monitoring, resilience, and training hardening |

---

## References

- [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html)
- [ISO/IEC 27001:2022 Annex A summary](https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-3:v1:en)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/)
- [ISO/IEC 27701 — Privacy extension](https://www.iso.org/standard/71670.html)
- [ISO/IEC 42001 — AI management systems](https://www.iso.org/standard/81230.html)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — LLM01–LLM10 full entries with ISMS checklist | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
