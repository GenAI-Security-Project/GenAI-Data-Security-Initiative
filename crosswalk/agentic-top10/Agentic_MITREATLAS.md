<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10)
  Framework   : MITRE ATLAS — Adversarial Threat Landscape for AI Systems
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × MITRE ATLAS

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [MITRE ATLAS](https://atlas.mitre.org) — the authoritative adversarial
AI threat knowledge base.

Agentic systems dramatically expand the ATLAS threat surface. Where LLM
attacks target a single inference step, agentic attacks exploit autonomy,
memory persistence, tool access, and multi-agent orchestration — turning
ATLAS techniques into multi-stage attack chains with compounding blast
radius. This mapping explicitly notes where agentic context amplifies
the severity of a technique beyond its baseline LLM rating.

---

## Quick-reference summary

| ID | Name | Severity | Primary ATLAS Techniques | Agentic amplifier | Tier |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | AML.T0051.000, AML.T0051.001, AML.T0054 | Autonomy turns single injection into multi-step attack chain | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | AML.T0037, AML.T0015, AML.T0068 | Tool access converts prompt manipulation into real-world action | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | AML.T0022, AML.T0016, AML.T0024 | Cached credentials give attacker persistent access beyond session | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | AML.T0056, AML.T0048, AML.T0010 | Runtime dynamic loading means poisoned components affect all consumers | Hardening–Advanced |
| ASI05 | Unexpected Code Execution | Critical | AML.T0040, AML.T0054, AML.T0037 | Code generation + execution capability creates RCE gateway | Foundational–Advanced |
| ASI06 | Memory & Context Poisoning | High | AML.T0032, AML.T0063, AML.T0020 | Persistence across sessions amplifies impact of single injection | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | AML.T0043, AML.T0022, AML.T0016 | A2A spoofing misdirects entire agent clusters | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | AML.T0029, AML.T0034, AML.T0057 | Single fault fans out across all downstream agents | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | AML.T0045, AML.T0047, AML.T0049 | Agent fluency makes manipulation invisible to audit logs | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | AML.T0054, AML.T0015, AML.T0057 | Compliant surface masks persistent hidden goal pursuit | Hardening–Advanced |

---

## Audience tags

- **Red teamer** — full file, primary reference for agentic AI adversarial simulation
- **Threat modeller** — full file, map ATLAS techniques to your agent architecture
- **Security engineer** — ASI01, ASI02, ASI03, ASI05
- **SOC analyst** — ASI01, ASI03, ASI08, ASI10
- **ML / AI engineer** — ASI04, ASI06, ASI07
- **OT engineer** — ASI02, ASI08 with ISA/IEC 62443 and NIST SP 800-82 crosswalks

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical | **Agentic amplifier:** +2 steps above baseline LLM prompt injection

An attacker redirects the agent's objectives or decision logic through
direct or indirect instruction injection. In an agentic context the
impact exceeds a single bad response — the hijacked agent autonomously
executes multi-step attack chains across tools, APIs, and downstream
agents before any human can intervene.

**Real-world references:**
- EchoLeak (2025) — indirect injection via email content turned
  Microsoft 365 Copilot into a silent multi-step data exfiltration engine
- Bing Chat / Sydney (2023) — persistent adversarial prompting achieved
  full goal redirection across extended sessions

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| Direct Prompt Injection | [AML.T0051.000](https://atlas.mitre.org/techniques/AML.T0051.000) | Influence Operations | Attacker directly injects goal-altering instructions into agent input |
| Indirect Prompt Injection | [AML.T0051.001](https://atlas.mitre.org/techniques/AML.T0051.001) | Influence Operations | Hidden instructions in documents, emails, RAG results, or tool outputs alter agent goals without user visibility |
| LLM Jailbreak | [AML.T0054](https://atlas.mitre.org/techniques/AML.T0054) | Execution | Override safety guardrails that constrain agent goal execution |

#### Mitigations by tier

**Foundational**
- Treat all external content processed by the agent as untrusted
  regardless of source — documents, emails, web results, tool outputs
- Implement architectural separation between system goal definition
  and external content processing — goals cannot be overridden by content
- Deploy input filtering on all channels feeding agent context windows

**Hardening**
- Require human approval before the agent changes its stated goal
  or executes any action triggered by externally sourced content
- Version-control agent goals and system prompts — alert on any
  runtime deviation from the committed specification
- Maintain adversarial test suite covering indirect injection via
  every content channel your agent processes

**Advanced**
- Cryptographically sign agent goal specifications — runtime goal
  state must match the signed original or execution halts
- Implement intent verification layer — agent produces an auditable
  justification before each tool invocation, verified against goal spec
- Red team quarterly with novel indirect injection scenarios targeting
  your specific RAG sources, email channels, and tool descriptor paths

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| Rebuff | Open-source | https://github.com/protectai/rebuff |
| Invariant Analyzer | Open-source | https://github.com/invariantlabs-ai/invariant |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B001/B005/B006 · STRIDE Tampering/Spoofing · CWE-20

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical | **Agentic amplifier:** +2 steps — prompt manipulation becomes real-world action

Agents misuse legitimate tools — APIs, databases, filesystems, shell
commands — due to prompt manipulation, misalignment, or unsafe
delegation. The danger is not the manipulation itself but what the
tool does in response: delete, send, execute, publish.

**Real-world references:**
- Amazon Q (2025) — legitimate developer tools bent into destructive
  outputs through manipulated agent inputs
- Postmark MCP impersonation (2025) — malicious MCP server BCC'd every
  agent-sent email to attacker via poisoned tool descriptor
- Claude Desktop RCE (2025) — unrestricted AppleScript execution in
  connectors allowed command injection via web search content

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| Output Manipulation | [AML.T0037](https://atlas.mitre.org/techniques/AML.T0037) | Influence Operations | Crafting inputs that produce tool calls with destructive parameters |
| LLM Capability Escalation | [AML.T0015](https://atlas.mitre.org/techniques/AML.T0015) | Privilege Escalation | Exploiting overly permissive tool access to exceed intended agent scope |
| Automated Collection | [AML.T0068](https://atlas.mitre.org/techniques/AML.T0068) | Collection | Agent autonomously harvesting data through tool chains beyond authorised scope |

#### Mitigations by tier

**Foundational**
- Apply least agency per tool — define the narrowest permission set
  each tool requires and enforce it at the orchestration layer
- Validate all tool descriptors before agent loading — poisoned MCP
  descriptors are an active attack vector
- Block toxic tool combinations at the orchestration layer — database
  read + external network write should never coexist in one agent

**Hardening**
- Require explicit user confirmation for high-risk tool invocations:
  delete, send, publish, execute, payment
- Log all tool invocations with full parameter capture — anomaly
  detection on invocation patterns
- Sandbox code execution tools — no host filesystem or network access
  by default, explicit allowlist required

**Advanced**
- Automated tool-chain analysis pre-deployment to identify dangerous
  permission combinations before they reach production
- Maintain signed, versioned inventory of all approved MCP servers
  — agents cannot load unregistered tools at runtime
- Runtime kill-switch per tool class triggered automatically on
  anomaly detection

#### Tools

| Tool | Type | Link |
|---|---|---|
| Invariant Analyzer | Open-source | https://github.com/invariantlabs-ai/invariant |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B006/B007 · ISA/IEC 62443 SR 2.1 (OT) · CWE-94

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical | **Agentic amplifier:** +1 step — cached credentials outlast session

Agents inherit human or system credentials — session tokens, API keys,
SSH keys, delegated permissions — and attackers exploit weak privilege
boundaries to reuse those credentials beyond their intended scope,
enabling lateral movement and silent escalation that persists after
the original session ends.

**Real-world references:**
- Multiple production incidents of agents caching high-privilege tokens
  in memory, enabling attacker reuse across sessions and environments
- Confused deputy attacks in multi-agent orchestration where Agent A
  uses Agent B's elevated privileges without authorisation

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| Valid Accounts | [AML.T0022](https://atlas.mitre.org/techniques/AML.T0022) | Initial Access / Persistence | Exploiting legitimate agent credentials to access AI systems or data pipelines |
| Exfiltration via AI Inference API | [AML.T0016](https://atlas.mitre.org/techniques/AML.T0016) | Exfiltration | Using compromised agent credentials to exfiltrate data through inference API |
| Model Inversion | [AML.T0024](https://atlas.mitre.org/techniques/AML.T0024) | Collection | Reconstructing sensitive data accessible to the agent through credential abuse |

#### Mitigations by tier

**Foundational**
- Issue short-lived, task-scoped credentials per agent invocation —
  never long-lived tokens shared across tasks or sessions
- Agent maximum privilege equals the authorising user's privilege —
  no escalation permitted under any condition
- Store no credentials in agent memory or context beyond task lifetime —
  purge on task completion

**Hardening**
- Full audit logging on all agent identity operations — token issuance,
  use, expiry, and any anomalous access pattern
- Zero-trust re-validation on every agent action — no ambient authority
  from prior authentication
- Confused deputy protections — agents cannot act on behalf of other
  agents without explicit, scoped, time-limited delegation

**Advanced**
- Ephemeral identity architecture — agent identity dynamically assigned
  per task, cryptographically bound, non-reusable
- Continuous NHI (Non-Human Identity) monitoring for anomalous token
  usage patterns across all agent sessions
- Automated credential rotation triggered immediately on any anomaly
  detection signal

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| Teleport | Open-source/Commercial | https://goteleport.com |
| Entro Security | Commercial | https://entro.security |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · AIUC-1 A/B007/B008 · ISA/IEC 62443 SR 1.1 (OT)

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High | **Agentic amplifier:** +1 step — runtime dynamic loading affects all consumers

Malicious or compromised tools, MCP servers, prompt templates, model
files, or agent personas introduced into the runtime supply chain alter
agent behaviour across every consumer — often fetched dynamically at
runtime with no static inventory and no signature verification.

**Real-world references:**
- GitHub MCP exploit (2025) — compromised MCP server in the wild
  altered agent behaviour across all connected agents
- Postmark MCP (2025) — first malicious MCP in the wild, discovered
  on npm, impersonated legitimate email service
- AI agents autonomously installing hallucinated packages — active
  documented class of supply chain attacks

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| Adversarial Model Manipulation | [AML.T0056](https://atlas.mitre.org/techniques/AML.T0056) | ML Attack Staging | Tampering with model weights or tool components loaded by agent at runtime |
| Model Contamination | [AML.T0048](https://atlas.mitre.org/techniques/AML.T0048) | Persistence | Persistent malicious behaviour introduced through dynamically loaded agent components |
| Backdoor ML Model | [AML.T0010](https://atlas.mitre.org/techniques/AML.T0010) | Persistence | Trigger-based backdoors in MCP servers, prompt templates, or model adapters |

#### Mitigations by tier

**Foundational**
- Maintain cryptographically signed inventory of all MCP servers,
  tools, plugins, and model versions used in production
- Verify signatures of all supply chain components before loading —
  reject unsigned or unrecognised components
- Pin tool and MCP server versions in production — no dynamic
  latest-version resolution

**Hardening**
- MCP server provenance verification before any agent connection —
  validate identity and integrity of the server
- Scan all prompt templates and tool descriptors for hidden
  instructions before deployment
- Implement supply chain monitoring with anomaly detection on
  component behaviour changes post-load

**Advanced**
- Sandboxed evaluation environment for all new tools and MCP servers
  before production promotion — behavioural testing against your threat model
- Dataset Bill of Materials (DBoM) for all training and retrieval data
  feeding agent knowledge bases
- Automated runtime component integrity verification — continuous
  hash checking of loaded components

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-218A · AIUC-1 B001/B003/B008 · BSIMM AM

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical | **Agentic amplifier:** +2 steps — code generation + execution = RCE gateway

Agents that generate and execute code for workflow automation, scripting,
or data processing become remote code execution gateways when crafted
prompts or poisoned inputs cause them to run attacker-controlled logic
with the agent's full system permissions.

**Real-world references:**
- AutoGPT RCE (2024) — crafted prompts triggered arbitrary code
  execution through the agent's code generation pipeline
- PromptJacking: Claude Desktop RCEs (2025) — unrestricted AppleScript
  execution in connectors enabled command injection via web search content

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| Unsafe Deserialisation via LLM | [AML.T0040](https://atlas.mitre.org/techniques/AML.T0040) | Execution | Agent-generated code or payloads executed by downstream components |
| LLM Jailbreak | [AML.T0054](https://atlas.mitre.org/techniques/AML.T0054) | Execution | Overriding code execution safety guardrails to allow arbitrary command execution |
| Output Manipulation | [AML.T0037](https://atlas.mitre.org/techniques/AML.T0037) | Influence Operations | Crafting inputs that produce malicious executable code in agent output |

#### Mitigations by tier

**Foundational**
- Sandbox all agent code execution — no host filesystem, network,
  or shell access by default, explicit allowlist required
- Static analysis of all agent-generated code before execution —
  reject anything outside permitted syntax and operation set
- Apply B005 input filtering specifically targeting code injection
  patterns on all channels feeding code-generating agents

**Hardening**
- Resource limits on all code execution sandboxes — CPU, memory,
  network, time — prevent escape via resource exhaustion
- Block dynamic package installation by agents in production
  environments — packages must be pre-approved and pinned
- Runtime execution monitoring with automatic kill on anomalous
  system call patterns

**Advanced**
- Hardware-level sandboxing (gVisor, Firecracker) for high-risk
  code execution workloads
- Formal allowlist of permitted operations — anything outside the
  list is blocked at the kernel level, not the application level
- Adversarial code generation red team exercises specifically
  targeting your agent's code execution paths

#### Tools

| Tool | Type | Link |
|---|---|---|
| gVisor | Open-source | https://gvisor.dev |
| Semgrep | Open-source | https://semgrep.dev |
| Bandit | Open-source | https://github.com/PyCQA/bandit |
| Firecracker | Open-source | https://firecracker-microvm.github.io |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006/B009 · CWE-94 · OWASP ASVS V5

---

### ASI06 — Memory & Context Poisoning

**Severity:** High | **Agentic amplifier:** +1 step — persistence across sessions

Persistent corruption of agent memory, RAG stores, embeddings, or
contextual knowledge — unlike prompt injection, the effect persists
across sessions and continues altering agent behaviour long after the
initial attack, potentially leaking secrets or shifting goals over time
without triggering any single detectable event.

**Real-world references:**
- Gemini Memory Attack (2024) — indirect prompt injection caused
  Copilot to store malicious instructions in persistent memory,
  enabling long-term behavioural manipulation and data leakage

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| Data Poisoning | [AML.T0032](https://atlas.mitre.org/techniques/AML.T0032) | ML Attack Staging | Injecting malicious content into agent persistent memory or RAG stores |
| Embedding Manipulation | [AML.T0063](https://atlas.mitre.org/techniques/AML.T0063) | ML Attack Staging | Crafting content whose embeddings bias future retrieval results in attacker's favour |
| Backdoor via Poisoned Memory | [AML.T0020](https://atlas.mitre.org/techniques/AML.T0020) | Persistence | Establishing persistent trigger-response patterns in agent memory stores |

#### Mitigations by tier

**Foundational**
- Classify all agent memory stores as sensitive data — apply access
  controls on read and write operations
- Implement audit logging on all persistent memory modifications —
  who wrote what and when, with full content capture
- Apply input filtering on all content before it is committed to
  persistent memory or RAG stores

**Hardening**
- Memory TTL (time-to-live) — periodic expiry and re-validation of
  stored context against authoritative sources
- Memory trust tiers — untrusted external content cannot write to
  the same memory namespace as internal trusted content
- Anomaly detection on memory write patterns — flag unusual sources,
  volumes, or content types

**Advanced**
- Cryptographic integrity verification of memory store contents —
  detect tampering between write and read operations
- Memory segmentation by trust domain enforced at the storage layer,
  not the application layer
- Automated memory auditing for adversarial content on a scheduled
  basis — not just at write time

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| LlamaIndex | Open-source | https://www.llamaindex.ai |
| Langfuse | Open-source | https://langfuse.com |

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: AIUC-1 A/B002/B005 · NIST AI RMF MS-2.5 · CWE-693

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High | **Agentic amplifier:** +1 step — A2A compromise scales to entire clusters

Agent-to-agent communication channels lacking strong authentication,
encryption, or schema validation enable spoofing, replay attacks,
protocol downgrade, and agent-in-the-middle attacks — a single
compromised channel can misdirect an entire multi-agent orchestration
cluster.

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| Network Service Scanning | [AML.T0043](https://atlas.mitre.org/techniques/AML.T0043) | Discovery | Identifying and mapping inter-agent communication endpoints for targeting |
| Valid Accounts | [AML.T0022](https://atlas.mitre.org/techniques/AML.T0022) | Persistence | Using compromised agent credentials to impersonate trusted agents in A2A channels |
| Exfiltration via AI Inference API | [AML.T0016](https://atlas.mitre.org/techniques/AML.T0016) | Exfiltration | Intercepting inter-agent messages to exfiltrate sensitive context passed between agents |

#### Mitigations by tier

**Foundational**
- Authenticate all A2A messages — no ambient trust between agents
  regardless of network location
- Encrypt all inter-agent communication channels — TLS 1.3 minimum
- Validate schema of all A2A message payloads — reject malformed
  or unexpected message structures

**Hardening**
- Full audit logging of all inter-agent messages with content capture
  — essential for incident reconstruction
- Replay attack protection — message nonces, timestamps, and sequence
  numbers on all A2A channels
- Short-lived agent identity certificates — no long-lived A2A trust
  tokens that persist beyond a single task

**Advanced**
- Mutual TLS (mTLS) for all A2A channels in production — both
  parties authenticate before any message is exchanged
- Zero-trust mesh for multi-agent orchestration — every message
  independently verified against policy, regardless of source
- A2A communication anomaly detection — flag unexpected message
  patterns, unusual agent pairings, or out-of-scope content

#### Tools

| Tool | Type | Link |
|---|---|---|
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| Linkerd | Open-source | https://linkerd.io |
| cert-manager | Open-source | https://cert-manager.io |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · AIUC-1 B007/B008/E · ISA/IEC 62443 SR 3.1 (OT)

---

### ASI08 — Cascading Agent Failures

**Severity:** High | **Agentic amplifier:** +1 step — single fault fans out at machine speed

A single-point failure — poisoned memory entry, bad plan, compromised
tool call — propagates through interconnected multi-agent workflows
and amplifies into system-wide incidents. In OT environments this can
propagate from the AI orchestration layer into physical process control
before any human can intervene.

**OT critical note:** Cascading agent failures in industrial environments
can cross from the AI layer into safety systems. Treat this as Critical
severity in any OT/ICS deployment. See ISA/IEC 62443 and NIST SP 800-82
crosswalks for OT-specific controls.

**Real-world references:**
- Multiple documented production multi-agent loops causing runaway
  API cost, data corruption, and service outages before circuit
  breakers engaged

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| Denial of ML Service | [AML.T0029](https://atlas.mitre.org/techniques/AML.T0029) | Impact | Triggering cascading failure propagation to exhaust system resources or degrade service |
| Cost Harvesting | [AML.T0034](https://atlas.mitre.org/techniques/AML.T0034) | Impact | Crafting inputs that trigger runaway agent loops generating unbounded costs |
| Exploit Public-Facing ML Application | [AML.T0057](https://atlas.mitre.org/techniques/AML.T0057) | Initial Access | Exploiting an exposed agent endpoint to introduce a fault that cascades internally |

#### Mitigations by tier

**Foundational**
- Implement circuit breakers — halt propagation automatically when
  failure rate, error count, or latency exceeds threshold
- Define explicit fail-safe modes for every agent — fail closed,
  not open, on unexpected state
- Apply scope constraints on all agents — a failing agent cannot
  escalate its own permissions or access

**Hardening**
- Full audit trail of all agent actions enabling cascade path
  reconstruction post-incident
- Segment sensitive agents from general-purpose agents — blast
  radius limitation through architectural isolation
- Rate limiting on A2A communication — prevent runaway message
  loops between agents

**Advanced**
- Automated HITL triggers on cascade indicators — route to human
  review before failure propagates beyond defined blast radius
- Chaos engineering — intentional fault injection into multi-agent
  workflows to validate circuit breaker effectiveness
- Real-time cascade detection with automated kill-switch per agent
  segment, independently of the model layer

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Resilience4j | Open-source | https://resilience4j.readme.io |
| LangSmith | Commercial | https://smith.langchain.com |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.1 (OT) · NIST SP 800-82 (OT)

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium | **Agentic amplifier:** +0.5 — manipulation invisible to standard audit

Users anthropomorphise agents — trusting their fluency, expertise,
and persuasive outputs — enabling hijacked or misaligned agents to
manipulate humans into approving malicious commands or sharing
sensitive data. The danger: the human performs the final action so
forensics shows a legitimate user decision, not an agent manipulation.

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| Disinformation | [AML.T0045](https://atlas.mitre.org/techniques/AML.T0045) | Influence Operations | Agent generates persuasive false information to manipulate human approvals |
| Influence via Automated Content | [AML.T0047](https://atlas.mitre.org/techniques/AML.T0047) | Influence Operations | Agent produces high-volume, fluent content that overwhelms human critical assessment |
| Spearphishing via AI | [AML.T0049](https://atlas.mitre.org/techniques/AML.T0049) | Initial Access | Compromised agent crafts highly personalised, convincing manipulation targeted at specific users |

#### Mitigations by tier

**Foundational**
- Agents must clearly identify themselves as AI in all user-facing
  interactions — enforced at the guardrail layer
- Separate agent conversation interface from security approval flows —
  chat is never the consent mechanism for sensitive actions
- Implement output filtering to detect and block manipulative language
  patterns in agent responses

**Hardening**
- Audit logging that distinguishes agent-influenced actions from
  genuinely human-initiated actions — essential for forensics
- User education on agent trust boundaries integrated into onboarding —
  not optional training
- Independent review required for high-consequence agent recommendations
  — second human, not second agent

**Advanced**
- Behavioural analysis detecting when agents are nudging users toward
  specific approvals — alert on persuasion pattern detection
- Structural separation between agent reasoning and user consent
  flows — consent captured through independent, non-agent interface
- Red team exercises simulating trust exploitation scenarios against
  your specific user population and agent deployment

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 52 · AIUC-1 C/F · ENISA AI Threat Landscape

---

### ASI10 — Rogue Agents

**Severity:** Critical | **Agentic amplifier:** +2 steps — compliant surface masks persistent hidden goals

Malicious or compromised agents appear compliant on the surface but
pursue hidden goals, hijack workflows, or systematically deviate from
their intended purpose — often the end-state of a successful ASI01 or
ASI06 attack that has gone undetected across multiple sessions.

#### MITRE ATLAS techniques

| Technique | ID | Tactic | Agentic context |
|---|---|---|---|
| LLM Jailbreak | [AML.T0054](https://atlas.mitre.org/techniques/AML.T0054) | Execution | Persistent override of agent safety constraints enabling hidden goal execution |
| LLM Capability Escalation | [AML.T0015](https://atlas.mitre.org/techniques/AML.T0015) | Privilege Escalation | Rogue agent gradually escalates its own capabilities and permissions over time |
| Exploit Public-Facing ML Application | [AML.T0057](https://atlas.mitre.org/techniques/AML.T0057) | Persistence | Compromised agent maintains persistent access and hidden execution across sessions |

#### Mitigations by tier

**Foundational**
- Comprehensive audit logging of all agent actions from day one —
  no deployment without full observability
- Strict scope constraints enforced at the orchestration layer, not
  the model layer — rogue agent cannot exceed its permission envelope
- Safety guardrails as an independent layer from agent logic — not
  overridable by model output

**Hardening**
- Continuous behavioural monitoring — flag deviation from historical
  baseline for every deployed agent
- Agent health checks on a defined schedule — periodic re-verification
  against intended purpose specification
- Automated quarantine on anomaly detection — isolate suspected
  rogue agent pending human review before it can take further action

**Advanced**
- Multi-agent consensus for high-stakes decisions — no single agent
  can act unilaterally on irreversible actions
- Formal behavioural specification for each agent — machine-verifiable
  contracts checked at runtime, not just design time
- Full forensic reproducibility — every agent decision must be
  reconstructable from logged inputs, state, and outputs

#### Tools

| Tool | Type | Link |
|---|---|---|
| Langfuse | Open-source | https://langfuse.com |
| Helicone | Open-source | https://www.helicone.ai |
| Weights & Biases | Commercial | https://wandb.ai |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: MITRE ATT&CK T1078 · EU AI Act Art. 9 · AIUC-1 B001/B002/C/E

---

## Implementation priority

| Phase | ASI entries | Rationale |
|---|---|---|
| 1 — Do now | ASI01, ASI02, ASI03 | Highest exploitability, most active in wild, largest blast radius |
| 2 — This sprint | ASI05, ASI10 | RCE and rogue agent — catastrophic if triggered |
| 3 — This quarter | ASI04, ASI06, ASI07 | Supply chain and persistence close the long-dwell attack paths |
| 4 — Ongoing | ASI08, ASI09 | Resilience, cascade engineering, and trust boundary hardening |

---

## ATLAS navigator layer

A MITRE ATLAS Navigator layer file covering all ASI techniques in this
mapping is available at:
`data/agentic-top10/atlas-navigator-layer.json`

Import into [MITRE ATLAS Navigator](https://mitre-atlas.github.io/atlas-navigator/)
to visualise agentic attack coverage across your threat model.

---

## References

- [MITRE ATLAS](https://atlas.mitre.org)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP AIVSS](https://aivss.owasp.org)
- [OWASP AI Testing Guide](https://owasp.org/www-project-ai-testing-guide/)
- [MITRE ATLAS case studies](https://atlas.mitre.org/studies/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — ASI01–ASI10 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
