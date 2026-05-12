<!--
  GenAI Security Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10)
  Framework   : NIST AI Risk Management Framework (AI RMF 1.0)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × NIST AI RMF

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to the [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
and its companion [NIST AI RMF Playbook](https://airc.nist.gov/Docs/2).

Agentic AI systems — autonomous, tool-using, multi-agent — introduce
a qualitatively different risk profile from static LLMs. The AI RMF
was designed as a lifecycle framework: GOVERN sets organisational
policy, MAP identifies risks in context, MEASURE analyses and tests
those risks, and MANAGE treats and monitors them. This structure maps
naturally to agentic risk because agentic risks compound across the
lifecycle — a governance gap in GV enables a mapping gap in MP that
manifests as an undetected cascade in MG.

This file is the primary AI RMF governance reference for teams
deploying autonomous AI agents. Use alongside `LLM_NISTAIRMF.md`
for LLM-specific risks and `Agentic_AIUC1.md` for agent-specific
technical controls.

---

## AI RMF functions — agentic context

| Function | Agentic AI role |
|---|---|
| GOVERN (GV) | Policies for agent autonomy limits, identity governance, tool access, human oversight, acceptable use |
| MAP (MP) | Mapping agent risks in context — tool inventory, A2A communication paths, cascade blast radius, memory stores |
| MEASURE (MS) | Testing agent behaviour — adversarial testing, behavioural baselines, tool invocation monitoring, cascade testing |
| MANAGE (MG) | Treating agent risks — incident response, kill switch procedures, rogue agent containment, memory audit |

---

## Quick-reference summary

| ID | Name | Severity | Primary AI RMF Subcategories | Tier | Scope |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | GV-1.7, MP-2.3, MS-2.5, MG-2.2 | Foundational–Advanced | Both |
| ASI02 | Tool Misuse & Exploitation | Critical | GV-1.7, MP-5.1, MS-2.5, MG-2.2 | Foundational–Advanced | Both |
| ASI03 | Identity & Privilege Abuse | Critical | GV-1.6, MP-2.3, MS-2.5, MG-2.2 | Foundational–Advanced | Both |
| ASI04 | Agentic Supply Chain | High | GV-1.6, MP-5.1, MS-2.5, MG-3.2 | Foundational–Hardening | Both |
| ASI05 | Unexpected Code Execution | Critical | GV-1.7, MP-2.3, MS-2.5, MG-2.2 | Hardening–Advanced | Build |
| ASI06 | Memory & Context Poisoning | High | GV-1.6, MP-2.3, MS-2.5, MG-2.4 | Hardening–Advanced | Both |
| ASI07 | Insecure Inter-Agent Comms | High | GV-1.6, MP-5.1, MS-2.5, MG-2.2 | Hardening–Advanced | Build |
| ASI08 | Cascading Agent Failures | High | MP-4.1, MS-2.5, MG-2.2, MG-3.2 | Foundational–Advanced | Both |
| ASI09 | Human-Agent Trust Exploitation | Medium | GV-1.7, MS-2.6, MS-4.1, MG-2.4 | Foundational–Hardening | Both |
| ASI10 | Rogue Agents | Critical | GV-1.7, MP-2.3, MS-2.5, MG-2.2 | Hardening–Advanced | Both |

---

## Audience tags

- **CISO / governance** — full file, AI RMF alignment for agentic AI programme
- **Risk manager** — MAP and MEASURE subcategories, risk register entries
- **Federal agency teams** — EO 14110 alignment for agentic deployments
- **AI/ML engineer** — MEASURE subcategories, testing and monitoring entries
- **Security engineer** — MANAGE subcategories, incident response entries
- **OT engineer** — ASI02, ASI08 with ISA 62443 crosswalk for OT context

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects an agent's objectives through direct or indirect
instruction injection, causing it to autonomously execute a multi-step
attack chain before any human can intervene. In an agentic context,
the AI RMF GV-1.7 autonomy policy is the foundational governance control —
without a documented policy on permissible agent autonomy, every other
control lacks an anchor.

**Real-world references:**
- EchoLeak (2025) — indirect injection turned Microsoft 365 Copilot
  into a silent exfiltration engine via email content

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Organisational policy defines permissible agent autonomy — agents cannot change their stated goals without human confirmation |
| Risk categorisation | MP-2.3 | MAP | Agent goal hijack categorised in AI risk register per deployment — specific injection vectors mapped |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing programme covers goal hijack scenarios — indirect injection via all agent data sources |
| Risk response | MG-2.2 | MANAGE | Incident response for detected goal hijack — suspension procedure, action reversal checklist, OT impact assessment |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish and document organisational policy on
  agent autonomy — define what goal changes require human
  confirmation and what actions agents cannot take autonomously
- MP-2.3: Include agent goal hijack in AI risk register for
  every agentic deployment — map specific indirect injection
  paths via each data source the agent processes
- Treat all external content processed by agents as untrusted
  regardless of source — policy enforced, not best effort

**Hardening**
- MS-2.5: Include goal hijack scenarios in adversarial
  evaluation programme — direct, indirect via RAG, indirect
  via email/documents/tool outputs — before each production
  release
- MG-2.2: Define and test incident response for goal hijack —
  kill switch procedure, action reversal checklist, affected
  system notification workflow
- Version-control and audit agent goal specifications —
  runtime deviations from the committed specification trigger
  suspension and human review

**Advanced**
- MS-2.5: Extend adversarial testing to cover every content
  channel your agent processes — not just user inputs but
  all indirect injection surfaces specific to your deployment
- MG-2.2: Implement automated response — session isolation,
  action reversal, forensic capture triggered on goal hijack
  indicators without waiting for manual investigation
- Include agent goal hijack in board-level AI risk reporting —
  GV-1.7 governance objective with measurable detection targets

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| Rebuff | Open-source | https://github.com/protectai/rebuff |
| Invariant Analyzer | Open-source | https://github.com/invariantlabs-ai/invariant |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B001/B005/B006 · MITRE ATLAS AML.T0051 · ISA/IEC 62443 SR 3.3 (OT)

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents misuse legitimate tools due to prompt manipulation, goal hijack,
or unsafe delegation — calling tools with destructive parameters or
chaining tools in unexpected sequences. The AI RMF MP-5.1 interdependency
mapping is the critical governance control: every tool an agent can
access must be inventoried with its data exposure, permission scope,
and irreversibility classification before the agent deploys.

**Real-world references:**
- Amazon Q (2025) — legitimate developer tools bent into destructive
  outputs through manipulated agent inputs
- Postmark MCP (2025) — malicious MCP server BCC'd every agent-sent
  email to attacker via poisoned tool descriptor

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Policy defines permissible tool invocations per agent role — human confirmation required for irreversible tools |
| Interdependencies | MP-5.1 | MAP | All agent tool integrations mapped — data received, permission scope, reversibility, and risk rating per tool |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing of tool misuse scenarios — destructive parameter injection, tool chaining, MCP descriptor poisoning |
| Risk response | MG-2.2 | MANAGE | Incident response for tool misuse — tool disable, parameter audit, downstream impact assessment |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish policy requiring human confirmation for
  all irreversible tool invocations — define what constitutes
  irreversible per tool type and deployment context
- MP-5.1: Complete tool inventory before any agent deployment —
  what data each tool receives, what permissions it holds,
  whether invocations are reversible — documented and approved
- Apply principle of least agency per tool — narrowest
  permission set each tool requires, enforced at the
  orchestration layer

**Hardening**
- MS-2.5: Include tool misuse scenarios in adversarial
  evaluation — destructive parameter injection, unusual tool
  combinations, MCP descriptor poisoning — before each release
- MG-2.2: Define incident response for tool misuse — which
  tools can be disabled remotely, how parameters are audited
  post-incident, how downstream impact is assessed
- Validate all tool descriptors before agent loading — any
  hidden instruction in a descriptor is a rejection trigger

**Advanced**
- MP-5.1: Extend tool inventory to cover runtime dynamic
  tool loading — MCP servers and plugins fetched at inference
  must be inventoried and approved before agent use
- MS-2.5: Conduct red team exercises targeting tool chain
  exploitation — attempt to cause destructive outcomes through
  legitimate tool invocations on your specific deployment
- MG-2.2: Automated tool disable on anomalous invocation
  detection — kill switch per tool class, not just per agent

#### Tools

| Tool | Type | Link |
|---|---|---|
| Invariant Analyzer | Open-source | https://github.com/invariantlabs-ai/invariant |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B006/B007 · ISA/IEC 62443 SR 2.2 (OT) · MITRE ATLAS AML.T0015

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit human or system credentials and attackers exploit weak
privilege boundaries to reuse those credentials beyond their intended
scope. The AI RMF GV-1.6 data governance policy must explicitly cover
agent credential lifecycle — NHI (Non-Human Identity) governance is
not optional for agentic deployments.

**Real-world references:**
- CVE-2025-54795 — Claude Code confirmation bypass enabling execution
  of untrusted commands via agent credential access

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Agent identity and credential governance policy — NHI inventory, short-lived credentials, scope controls |
| Risk categorisation | MP-2.3 | MAP | Agent credential exposure risks mapped per deployment — credential types, scope, and lateral movement potential |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing covering credential leakage and abuse — memory stores, logs, tool payload captures |
| Risk response | MG-2.2 | MANAGE | Incident response for credential exposure — rotation, containment, lateral movement assessment, downstream notification |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish NHI governance policy — all agent
  identities inventoried, credentials lifecycle-managed,
  no hardcoded secrets in agent code or prompts
- MP-2.3: Map agent credential exposure to specific deployments
  in risk register — credential types, scope, rotation schedule,
  and lateral movement blast radius documented per agent
- Issue short-lived, task-scoped credentials per invocation —
  never long-lived tokens shared across tasks or sessions

**Hardening**
- MS-2.5: Include credential leakage in adversarial evaluation —
  test memory store persistence, log capture, tool payload
  exposure for all credential types used by your agents
- MG-2.2: Define incident response for credential exposure —
  immediate rotation, lateral movement scope assessment,
  downstream system notification, forensic capture
- Implement JIT (just-in-time) credential issuance with
  automatic revocation on task completion

**Advanced**
- GV-1.6: Implement continuous NHI monitoring — anomalous
  token usage patterns across all agent sessions feed into
  AI risk monitoring programme
- MS-2.5: Conduct red team exercises simulating agent
  credential abuse — stolen token lateral movement across
  all systems the agent has access to, documented in ISMS
- MG-2.2: Automated credential rotation triggered on any
  anomaly detection signal — not just scheduled rotation

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| Teleport | Open-source/Commercial | https://goteleport.com |
| Entro Security | Commercial | https://entro.security |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · AIUC-1 A/B007 · ISA/IEC 62443 SR 1.2 (OT)

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High

Malicious or compromised tools, MCP servers, prompt templates, or
model components loaded dynamically at runtime alter agent behaviour
across all consumers. The AI RMF MP-5.1 interdependency mapping must
extend to runtime dynamic components — not just pre-deployment
component inventory.

**Real-world references:**
- GitHub MCP exploit (2025) — compromised MCP server altered agent
  behaviour across all connected agents
- Postmark MCP (2025) — first malicious MCP in the wild on npm

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Supply chain governance policy — approved sources for agent tools, MCP servers, and model components |
| Interdependencies | MP-5.1 | MAP | All agent supply chain components mapped — dynamic tool loading inventoried, approved before use |
| Testing — adversarial | MS-2.5 | MEASURE | Supply chain integrity testing — signature verification, descriptor review, backdoor scanning |
| Residual risk | MG-3.2 | MANAGE | Residual supply chain risk documented and treated — third-party component risks in AI risk register |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish supply chain governance policy for all
  agent components — approved sources, integrity requirements,
  change management procedures documented before deployment
- MP-5.1: Map all supply chain components including dynamic
  runtime components — MCP servers, plugins, and tools fetched
  at inference inventoried and approved before agent use
- Verify cryptographic signatures of all components before
  loading — unsigned components rejected

**Hardening**
- MS-2.5: Include supply chain integrity in adversarial
  evaluation — signature verification, descriptor review for
  hidden instructions, behavioural testing in isolated environment
- MG-3.2: Document residual supply chain risk per component
  in AI risk register — include in board-level AI risk reporting
- Apply agent component change management — no dynamic updates
  in production without review and approval process

**Advanced**
- MP-5.1: Implement runtime component integrity monitoring —
  continuous hash verification of loaded components, deviation
  triggers agent suspension
- MS-2.5: Conduct adversarial supply chain testing — attempt
  to introduce compromised components and verify detection
- MG-3.2: Establish responsible disclosure relationship with
  all strategic component vendors — defined vulnerability
  notification path with response SLA

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-218A · AIUC-1 B001/B003 · ISA/IEC 62443 62443-2-4 (OT)

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents that generate and execute code become RCE gateways when crafted
prompts or poisoned inputs cause them to run attacker-controlled logic.
The AI RMF requires this risk to be explicitly categorised (MP-2.3) and
tested adversarially (MS-2.5) — code execution capability in any agent
is a separate, elevated risk category that requires its own treatment.

**Real-world references:**
- AutoGPT RCE (2024) — crafted prompts triggered arbitrary code
  execution through the agent's code generation pipeline

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Policy explicitly addresses agent code execution capability — sandbox requirements, permitted operations |
| Risk categorisation | MP-2.3 | MAP | Code execution risk categorised separately per agent — blast radius, permitted operations, sandbox status |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing of code execution paths — sandbox escape attempts, command injection via generated code |
| Risk response | MG-2.2 | MANAGE | Incident response for agent code execution anomaly — sandbox isolation, kill switch, forensic capture |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish policy that agents with code execution
  capability require explicit approval — higher risk category,
  additional controls mandatory before deployment
- MP-2.3: Categorise code execution risk separately in AI
  risk register — blast radius, sandbox status, permitted
  operations, and monitoring coverage documented per agent
- Sandbox all agent code execution — no host filesystem,
  network, or shell access by default, explicit allowlist required

**Hardening**
- MS-2.5: Include sandbox escape and code injection scenarios
  in adversarial evaluation — test against your specific
  agent runtime and sandbox configuration
- MG-2.2: Define incident response for code execution anomaly —
  sandbox isolation procedure, kill switch activation, scope
  assessment, forensic capture workflow
- Static analysis of all agent-generated code before execution —
  reject code containing operations outside the allowlist

**Advanced**
- MS-2.5: Conduct red team exercises targeting code execution
  paths — attempt sandbox escape from within your specific
  agent runtime, document results
- Hardware-level sandboxing for high-risk code execution
  workloads — document as MS-2.5 robustness evidence
- GV-1.7: Include agent code execution capability in board-level
  AI risk reporting — explicit governance sign-off required

#### Tools

| Tool | Type | Link |
|---|---|---|
| gVisor | Open-source | https://gvisor.dev |
| Semgrep | Open-source | https://semgrep.dev |
| Bandit | Open-source | https://github.com/PyCQA/bandit |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006 · CWE-94 · ISA/IEC 62443 SR 3.3 (OT)

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Persistent corruption of agent memory, RAG stores, or contextual
knowledge causes systematic incorrect behaviour across all future
interactions — unlike prompt injection, the effect persists across
sessions without any visible triggering event.

**Real-world references:**
- Gemini Memory Attack (2024) — indirect injection caused persistent
  memory poisoning enabling long-term behavioural manipulation

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | Agent memory treated as sensitive data asset — classification, access controls, retention policy |
| Risk categorisation | MP-2.3 | MAP | Memory poisoning risk mapped per agent — memory stores, trust levels, access controls, TTL documented |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing of memory integrity — poisoning scenarios, anomaly detection effectiveness |
| Risk response — data | MG-2.4 | MANAGE | Response for confirmed memory poisoning — audit procedure, content purge, operational impact assessment |

#### Mitigations by tier

**Foundational**
- GV-1.6: Classify all agent memory stores as sensitive data —
  access controls, retention limits, and audit logging
  mandatory from day one, policy enforced
- MP-2.3: Map memory poisoning risks per agent in risk register —
  which memory stores exist, what trust levels they hold,
  what operational decisions they influence
- Implement access controls on agent memory write operations —
  only the agent and designated administrators can write

**Hardening**
- MS-2.5: Include memory poisoning scenarios in adversarial
  evaluation — test injection paths via each content source
  that can write to agent memory
- Enforce memory TTL — agent memory entries expire and require
  re-validation against authoritative sources
- MG-2.4: Define response for confirmed memory poisoning —
  which memory content is purged, how operational decisions
  influenced by poisoned memory are reviewed and corrected

**Advanced**
- MS-2.5: Implement continuous memory integrity monitoring —
  statistical anomaly detection on memory content and access
  patterns, alerts integrated into AI incident management
- Cryptographic integrity verification of memory store contents —
  tamper detection between write and read operations
- GV-1.6: Include agent memory governance in board-level
  AI data governance reporting

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| LlamaIndex | Open-source | https://www.llamaindex.ai |
| Langfuse | Open-source | https://langfuse.com |

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: AIUC-1 A/B002 · ISO 27001 A.8.15 · ISA/IEC 62443 SR 3.7 (OT)

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High

Agent-to-agent communication channels lacking authentication or
encryption enable spoofing, replay, and agent-in-the-middle attacks.
The AI RMF MP-5.1 interdependency mapping must cover A2A communication
architecture — every agent-to-agent channel is a dependency that
requires its own risk assessment.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for data privacy | GV-1.6 | GOVERN | A2A communication security policy — authentication, encryption, schema validation requirements |
| Interdependencies | MP-5.1 | MAP | All A2A communication channels mapped — authentication method, encryption status, schema validation, logging |
| Testing — adversarial | MS-2.5 | MEASURE | A2A security testing — spoofing, replay, man-in-the-middle scenarios on all inter-agent channels |
| Risk response | MG-2.2 | MANAGE | Incident response for A2A compromise — channel isolation, agent suspension, forensic capture |

#### Mitigations by tier

**Foundational**
- GV-1.6: Establish A2A communication security policy —
  authentication, encryption, and schema validation
  requirements for all inter-agent channels
- MP-5.1: Map all A2A communication channels in AI risk
  register — authentication method, encryption status,
  replay protection, and logging coverage per channel
- Authenticate all A2A messages — no ambient trust between
  agents regardless of network location

**Hardening**
- MS-2.5: Include A2A security scenarios in adversarial
  evaluation — spoofing, replay, and man-in-the-middle
  attempts against your specific A2A channels
- Implement replay attack protection — message nonces,
  timestamps, and sequence numbers on all A2A channels
- MG-2.2: Define incident response for A2A compromise —
  channel isolation, all affected agents suspended,
  message log forensics procedure

**Advanced**
- MS-2.5: Implement mutual TLS on all production A2A
  channels with Zone 3 agent access — both sides
  authenticate before any message exchange
- GV-1.6: Include A2A communication security in AI
  governance programme — annual review of all channel
  authentication methods and encryption standards
- Continuous A2A anomaly detection — flag unexpected
  message patterns and out-of-scope content

#### Tools

| Tool | Type | Link |
|---|---|---|
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| Linkerd | Open-source | https://linkerd.io |
| cert-manager | Open-source | https://cert-manager.io |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · AIUC-1 B007/B008 · ISA/IEC 62443 SR 3.1 (OT)

---

### ASI08 — Cascading Agent Failures

**Severity:** High

A single-point fault propagates through multi-agent workflows and
amplifies into system-wide incidents. In OT environments, cascading
agent failures can cross from the AI layer into physical process
control. The AI RMF MP-4.1 risk tolerance subcategory is the
governance anchor — what level of cascade is acceptable must be
defined before deployment, not discovered during an incident.

**OT critical note:** Cascading failures in OT environments are
Critical severity — see `Agentic_ISA62443.md` for OT-specific controls.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Risk tolerance | MP-4.1 | MAP | Cascade blast radius defined and accepted per deployment — maximum affected systems documented |
| Testing — adversarial | MS-2.5 | MEASURE | Cascade resilience testing — circuit breaker effectiveness, failover scenarios, chaos engineering |
| Risk response | MG-2.2 | MANAGE | Incident response for cascade events — defined suspension procedure, process control fallback |
| Residual risk | MG-3.2 | MANAGE | Residual cascade risk documented — BCP coverage for agent cluster failures |

#### Mitigations by tier

**Foundational**
- MP-4.1: Define cascade blast radius before each multi-agent
  deployment — maximum systems affected by any single agent
  failure, formally accepted in risk register
- Implement circuit breakers — automatic suspension when
  failure rate exceeds threshold, fail-safe default for all
  agents on suspension
- Define fail-safe modes — on suspension, process control
  continues without agent involvement, operators notified

**Hardening**
- MS-2.5: Include cascade scenarios in adversarial evaluation —
  intentional fault injection into multi-agent workflows,
  circuit breaker effectiveness verified
- Segment agent clusters — blast radius limited by design,
  failure in one cluster cannot propagate to adjacent clusters
- MG-2.2: Define cascade incident response — who is notified,
  within what timeframe, with what information, what
  process control fallback is activated

**Advanced**
- MS-2.5: Conduct OT-specific chaos engineering —
  intentional failure injection with physical process
  impact assessment for OT-connected agent clusters
- MG-3.2: Include agent cluster failures in BCP — annual
  failover drills covering cascade scenarios
- GV-4.2: Cross-functional team accountable for cascade
  risk governance — AI, security, operations, and
  safety engineering represented

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Resilience4j | Open-source | https://resilience4j.readme.io |
| LangSmith | Commercial | https://smith.langchain.com |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.6 (OT) · NIST SP 800-82 (OT)

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Users anthropomorphise agents — trusting their fluency and apparent
expertise — enabling hijacked agents to manipulate humans into approving
harmful actions. The AI RMF MS-4.1 feedback mechanism subcategory is
critical here: organisations must have a feedback loop that detects
aggregate over-trust patterns before they cause harm.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Policy on agent transparency — agents must identify as AI, advisory outputs clearly distinguished from authoritative |
| Testing — data leakage | MS-2.6 | MEASURE | Evaluation of transparency controls — verify advisory labels persist in all interface contexts |
| Feedback mechanisms | MS-4.1 | MEASURE | Feedback channels detecting operator over-trust patterns — aggregate analysis of agent-influenced decisions |
| Risk response — data | MG-2.4 | MANAGE | Response for detected trust exploitation patterns — operator retraining, interface redesign, aggregate audit |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish policy requiring all agents to identify
  as AI in user-facing interactions — transparency obligation
  enforced at the guardrail layer, not just system prompt
- Separate agent conversation interface from security approval
  flows — chat is never the consent mechanism for sensitive
  actions, policy enforced
- MS-2.6: Verify advisory labels persist in all interface
  contexts — users cannot mistake agent output for authoritative
  source in any rendering environment

**Hardening**
- MS-4.1: Implement feedback channels for detecting over-trust —
  user reporting, aggregate analysis of agent-influenced
  decisions, shift-level pattern review for OT operators
- MG-2.4: Define response for detected trust exploitation —
  operator retraining, interface redesign, aggregate audit
  of decisions made following agent recommendations
- Implement output filtering to detect and block manipulative
  language patterns in agent responses

**Advanced**
- MS-4.1: Deploy behavioural analysis detecting when agents
  are nudging users toward specific approvals — alert on
  persuasion pattern detection across sessions
- Conduct red team exercises simulating trust exploitation —
  test how effectively operators can identify manipulated
  agent recommendations in your specific deployment
- GV-1.7: Include human-agent trust policies in AI ethics
  governance — reviewed annually with input from user research

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 52 · AIUC-1 C/F · NIST AI RMF GV-1.7

---

### ASI10 — Rogue Agents

**Severity:** Critical

Malicious or compromised agents appear compliant on the surface but
pursue hidden goals or systematically deviate from intended purpose —
often the end-state of a successful ASI01 or ASI06 attack that went
undetected. The AI RMF requires rogue agent detection to be explicitly
covered in the evaluation programme (MS-2.5) and incident response
(MG-2.2) — without these, a rogue agent can operate indefinitely.

#### NIST AI RMF mapping

| Subcategory | ID | Function | How it applies |
|---|---|---|---|
| Policies for trustworthy AI | GV-1.7 | GOVERN | Policy requires behavioural monitoring of all deployed agents — rogue agent detection as a governance objective |
| Risk categorisation | MP-2.3 | MAP | Rogue agent risk categorised per deployment — detection capability, blast radius, and response procedures mapped |
| Testing — adversarial | MS-2.5 | MEASURE | Adversarial testing covering rogue agent scenarios — behavioural drift, persistent hidden goal detection |
| Risk response | MG-2.2 | MANAGE | Incident response for rogue agent — kill switch, audit procedure, operational impact assessment, root cause |

#### Mitigations by tier

**Foundational**
- GV-1.7: Establish policy requiring comprehensive audit
  logging of all agent actions from day one — no production
  deployment without full observability
- MP-2.3: Include rogue agent risk in AI risk register —
  detection capability status, blast radius, and defined
  response procedures documented per deployment
- Implement scope constraints enforced at the orchestration
  layer — rogue agent cannot exceed its permission envelope

**Hardening**
- MS-2.5: Establish behavioural baseline for every deployed
  agent during commissioning — expected invocation patterns,
  recommendation distributions, access volumes documented
- Continuous behavioural monitoring — deviation from baseline
  triggers tiered response: log ? alert ? suspend ? investigate
- MG-2.2: Define rogue agent containment procedure —
  kill switch activation, recent recommendation audit,
  process state validation, forensic capture

**Advanced**
- MS-2.5: Conduct rogue agent red team exercises — simulate
  persistent hidden goal pursuit across extended sessions,
  verify detection capability holds
- Multi-agent consensus for high-stakes decisions — rogue
  single agent cannot influence critical recommendations
  without cross-validation
- GV-1.7: Include rogue agent detection in board-level AI
  risk reporting — detection rate as a measurable governance
  objective reviewed quarterly

#### Tools

| Tool | Type | Link |
|---|---|---|
| Langfuse | Open-source | https://langfuse.com |
| Helicone | Open-source | https://www.helicone.ai |
| Weights & Biases | Commercial | https://wandb.ai |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: AIUC-1 B001/B002/C/E · EU AI Act Art. 9 · ISA/IEC 62443 SR 3.7 (OT)

---

## AI RMF profile for agentic AI

| Function | Priority entries | Key subcategories | Target state |
|---|---|---|---|
| GOVERN | ASI01, ASI02, ASI03, ASI10 | GV-1.6, GV-1.7, GV-4.2 | Documented autonomy policy, NHI governance, cross-functional team |
| MAP | ASI02, ASI04, ASI07, ASI08 | MP-2.3, MP-4.1, MP-5.1 | Tool inventory complete, A2A channels mapped, cascade blast radius defined |
| MEASURE | ASI01, ASI05, ASI06, ASI10 | MS-2.5, MS-2.6, MS-4.1 | Adversarial testing programme live, behavioural baselines established |
| MANAGE | ASI01, ASI08, ASI10 | MG-2.2, MG-2.4, MG-3.2 | Kill switch tested, incident response exercised, residual risk documented |

---

## Implementation priority

| Phase | ASI entries | AI RMF focus | Rationale |
|---|---|---|---|
| 1 — Do now | ASI01, ASI02, ASI03 | GV-1.7 autonomy policy, MP-2.3 risk register, MG-2.2 IR | Highest exploitability, largest blast radius, most active in wild |
| 2 — This sprint | ASI05, ASI10 | GV-1.7 code execution policy, MS-2.5 baseline | RCE and rogue agent are catastrophic if triggered undetected |
| 3 — This quarter | ASI04, ASI06, ASI07 | MP-5.1 supply chain, MG-2.4 memory IR | Supply chain and persistence close long-dwell attack paths |
| 4 — Ongoing | ASI08, ASI09 | MP-4.1 tolerance, MS-4.1 feedback | Resilience, cascade engineering, trust boundary hardening |

---

## References

- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [NIST AI RMF Playbook](https://airc.nist.gov/Docs/2)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP AIVSS](https://aivss.owasp.org)
- [Executive Order 14110](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — ASI01–ASI10 full entries with AI RMF profile | OWASP GenAI Data Security Initiative |

---

*Part of the [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
