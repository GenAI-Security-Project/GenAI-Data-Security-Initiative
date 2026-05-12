<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10)
  Framework   : AIUC-1 — The standard for AI agent security, safety and reliability
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × AIUC-1

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) to the [AIUC-1 standard](https://www.aiuc-1.com/) — the world's first AI agent security, safety and reliability certification framework, developed with 100+ Fortune 500 CISOs and used as the SOC 2 analog for AI agents.

AIUC-1 is an OWASP GenAI Security Project partner and explicitly covers all 10 ASI risks. Its six domains map across security, safety, reliability, accountability, data & privacy, and society — making it the most complete single-framework match for the Agentic Top 10.

---

## AIUC-1 domains at a glance

| Domain | ID | Focus |
|---|---|---|
| Data & Privacy | A | PII protection, data leakage, IP, access controls, training data |
| Security | B | Adversarial robustness, prompt injection, endpoint scraping, output filtering, agent permissions |
| Safety | C | Harm prevention, unsafe outputs, guardrails, human oversight |
| Reliability | D | Availability, consistency, failure recovery, rate limiting |
| Accountability | E | Audit trails, logging, explainability, incident response |
| Society | F | Bias, misinformation, societal harm, transparency |

---

## Quick-reference summary

| ID | Name | Severity | AIUC-1 Controls | Tier | Scope |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | B001, B002, B005, B006 | Foundational–Advanced | Both |
| ASI02 | Tool Misuse & Exploitation | Critical | B001, B004, B006, B007 | Foundational–Advanced | Both |
| ASI03 | Identity & Privilege Abuse | Critical | A (all), B007, B008, E | Foundational–Advanced | Both |
| ASI04 | Agentic Supply Chain Vulnerabilities | High | B001, B003, B008, A | Hardening–Advanced | Both |
| ASI05 | Unexpected Code Execution | Critical | B001, B005, B006, B009 | Foundational–Advanced | Build |
| ASI06 | Memory & Context Poisoning | High | A (all), B002, B005 | Hardening–Advanced | Both |
| ASI07 | Insecure Inter-Agent Communication | High | B007, B008, E | Hardening–Advanced | Build |
| ASI08 | Cascading Agent Failures | High | D, B006, E | Foundational–Advanced | Both |
| ASI09 | Human-Agent Trust Exploitation | Medium | C, F, B009, E | Foundational–Hardening | Both |
| ASI10 | Rogue Agents | Critical | B001, B002, B006, C, E | Hardening–Advanced | Both |

---

## Audience tags

- **Developer** — B001, B005, B006, B009
- **Security engineer** — B001–B009, E
- **Auditor** — A, E, B003, B007
- **CISO / governance** — A, C, E, F
- **Red teamer** — B001, B002, B005
- **ML / AI engineer** — A, B001, B005, B006
- **OT engineer** — B006, D, E (see ISA 62443 crosswalk for OT-specific controls)

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

Attackers redirect an agent's objectives or decision logic through direct or indirect prompt injection, poisoned content, malicious documents, or crafted tool outputs. The agent continues operating normally from the outside while serving the attacker's intent.

**Real-world reference:** EchoLeak (2025) — hidden prompts in Microsoft 365 Copilot turned the agent into a silent data exfiltration engine via indirect prompt injection.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Third-party testing of adversarial robustness | B001 | Mandatory adversarial testing program validating resilience against prompt injection and goal manipulation attempts | Foundational | Both |
| Detect adversarial input | B002 | Runtime monitoring to detect and respond to adversarial inputs redirecting agent goals | Hardening | Both |
| Implement real-time input filtering | B005 | Automated moderation filtering inputs before they reach agent reasoning | Foundational | Both |
| Prevent unauthorized AI agent actions | B006 | Safeguards preventing agents from performing actions beyond authorised scope — directly blocks goal hijack execution | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Treat all external content (emails, documents, web results, RAG chunks) as untrusted input
- Implement B005 input filtering on all channels feeding agent context
- Deploy B006 action guardrails — agents cannot execute actions outside their defined task scope
- Enable B001 adversarial testing in CI/CD before every agentic deployment

**Hardening**
- Enable B002 runtime anomaly detection on agent reasoning traces
- Require human approval for any goal-changing action or high-impact tool invocation
- Version-control and audit all agent goals and system prompts — unexpected changes alert

**Advanced**
- Implement intent-verification layers — agent must produce a verifiable justification before irreversible actions
- Deploy multi-agent consensus for high-stakes decisions
- Red team with indirect injection scenarios quarterly

#### Tools
| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| PromptBench | Open-source | https://github.com/microsoft/promptbench |
| OWASP AITG test cases | Open-source | https://owasp.org |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI15 Over-Broad Context Windows
- Other frameworks: MITRE ATLAS AML.T0051 · STRIDE Tampering/Spoofing

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents misuse legitimate tools due to prompt manipulation, goal hijack, misalignment, or unsafe delegation — calling tools with destructive parameters, chaining tools in unexpected sequences, or operating tools far beyond their intended function.

**Real-world reference:** Amazon Q (2025) — agent bent legitimate developer tools into destructive outputs through manipulated inputs. Postmark MCP (2025) — malicious MCP server BCC'd every agent-sent email to attacker.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Third-party testing of adversarial robustness | B001 | Adversarial testing specifically covering tool misuse and unsafe tool chaining | Foundational | Both |
| Prevent AI endpoint scraping | B004 | Safeguards preventing probing of tool endpoints and rate-limit abuse | Foundational | Both |
| Prevent unauthorized AI agent actions | B006 | Core control — agents restricted to narrowest permission set per tool, blocking misuse by design | Foundational | Both |
| Enforce user access privileges to AI systems | B007 | User-level access controls ensuring agents cannot invoke tools beyond what the authorising user can access | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Apply principle of least privilege per tool — an email agent cannot delete, only read/send
- Implement B006 per-tool permission manifests reviewed before deployment
- Block toxic tool combinations at the orchestration layer (e.g. database read + external network write)
- Validate all tool descriptors — poisoned MCP server descriptions are an active attack vector

**Hardening**
- Require explicit user confirmation for high-risk tool invocations (delete, send, publish, execute)
- Implement tool call logging with anomaly detection on invocation patterns
- Sandbox code execution tools — no host filesystem or network access by default

**Advanced**
- Automated tool-chain analysis pre-deployment to identify dangerous combinations
- Runtime kill-switch per tool class if anomalous behaviour detected
- Maintain signed inventory of all approved MCP servers and tool versions

#### Tools
| Tool | Type | Link |
|---|---|---|
| Koi Security | Commercial | https://www.koi.ai |
| Invariant Analyzer | Open-source | https://github.com/invariantlabs-ai/invariant |
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: MITRE ATLAS AML.T0054 · ISA/IEC 62443 SR 7.1 (OT)

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit human or system credentials — session tokens, API keys, SSH keys, delegated permissions — and attackers exploit weak privilege boundaries to use those credentials beyond their intended scope, enabling lateral movement and silent escalation.

**Real-world reference:** Multiple production incidents of agents caching high-privilege tokens in memory, enabling attacker reuse across sessions and environments.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Data & Privacy (full domain) | A | All agent credential and identity data falls under Domain A — PII protection, access restrictions, data leakage prevention | Foundational | Both |
| Enforce user access privileges to AI systems | B007 | Agents operate only within the privilege envelope of the authorising user — no escalation permitted | Foundational | Both |
| Protect model deployment environment | B008 | Secure deployment including encryption, access controls, and authorisation for the agent's runtime environment | Foundational | Both |
| Accountability (full domain) | E | Audit trails and logging of all agent identity use — essential for detecting privilege abuse post-incident | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Issue short-lived, task-scoped credentials per agent invocation — never long-lived tokens
- Enforce B007 — agent's maximum privilege equals the authorising user's privilege, never more
- Store no credentials in agent memory or context beyond task lifetime
- Implement B008 encrypted credential storage with strict access controls on agent runtime

**Hardening**
- Enable Domain E audit logging on all agent identity operations — token issuance, use, expiry
- Enforce zero-trust: every agent action re-validates identity, no ambient authority
- Implement confused deputy protections — agents cannot act on behalf of other agents without explicit delegation

**Advanced**
- Ephemeral identity architecture — agent identity is dynamically assigned per task, non-reusable
- Continuous NHI (Non-Human Identity) monitoring for anomalous token usage patterns
- Automated credential rotation triggered on any anomaly detection

#### Tools
| Tool | Type | Link |
|---|---|---|
| Teleport | Open-source/Commercial | https://goteleport.com |
| Entro Security | Commercial | https://entro.security |
| HashiCorp Vault | Open-source | https://www.vaultproject.io |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · MITRE ATT&CK T1552 · ISA/IEC 62443 SR 1.1

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High

Malicious or compromised tools, MCP servers, prompt templates, model files, or agent personas introduced into the runtime supply chain alter agent behaviour or expose data — often fetched dynamically at runtime with no static inventory.

**Real-world reference:** GitHub MCP exploit (2025) — compromised MCP server in the wild altered agent behaviour across all consumers. Postmark MCP impersonation — typosquatted package on npm with malicious behaviour.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Third-party testing of adversarial robustness | B001 | Supply chain components included in adversarial test scope | Foundational | Both |
| Manage public release of technical details | B003 | Controls preventing over-disclosure of agent architecture details that enable supply chain targeting | Hardening | Both |
| Protect model deployment environment | B008 | Secure deployment environment including verification of all runtime components | Foundational | Both |
| Data & Privacy (full domain) | A | All data shared with supply chain components governed under Domain A | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Maintain signed inventory of all MCP servers, tools, plugins, and model versions
- Verify cryptographic signatures of all supply chain components before loading
- Pin tool and MCP server versions — block dynamic latest-version resolution in production

**Hardening**
- Implement MCP server provenance checks before agent connection
- Scan all prompt templates and tool descriptors for hidden instructions pre-deployment
- B003 — limit public exposure of agent architecture details that enable targeted supply chain attacks

**Advanced**
- Automated supply chain monitoring with anomaly detection on component behaviour post-load
- Sandboxed evaluation environment for new tools before production promotion
- Dataset Bill of Materials (DBoM) for all training and retrieval data

#### Tools
| Tool | Type | Link |
|---|---|---|
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |
| CycloneDX | Open-source | https://cyclonedx.org |
| Snyk | Commercial | https://snyk.io |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: MITRE ATLAS AML.T0010 · NIST SP 800-218A · BSIMM AM

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents that generate or execute code — for workflow automation, scripting, data processing — become remote code execution gateways when crafted prompts or poisoned inputs cause them to run attacker-controlled logic.

**Real-world reference:** AutoGPT RCE (2024) — crafted prompts triggered arbitrary code execution through the agent's code generation capability.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Third-party testing of adversarial robustness | B001 | Code generation and execution paths explicitly included in adversarial test scope | Foundational | Both |
| Implement real-time input filtering | B005 | Filter inputs before they reach code generation components | Foundational | Build |
| Prevent unauthorized AI agent actions | B006 | Agents cannot execute code outside defined, sandboxed execution environments | Foundational | Build |
| Limit output over-exposure | B009 | Code outputs filtered and validated before execution | Foundational | Build |

#### Mitigations by tier

**Foundational**
- Sandbox all agent-generated code execution — no host filesystem, network, or shell access by default
- Implement B006 strict execution environment controls — allowlist permitted operations only
- Apply B005 input filtering specifically targeting code injection patterns

**Hardening**
- Static analysis of all agent-generated code before execution
- Runtime sandboxing with resource limits (CPU, memory, network, time)
- Block dynamic package installation by agents in production environments

**Advanced**
- Hardware-level sandboxing for high-risk code execution workloads
- Formal verification of agent code generation boundaries
- Real-time execution monitoring with automatic kill on anomaly

#### Tools
| Tool | Type | Link |
|---|---|---|
| Semgrep | Open-source | https://semgrep.dev |
| Bandit | Open-source | https://github.com/PyCQA/bandit |
| gVisor | Open-source | https://gvisor.dev |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: MITRE ATT&CK T1059 · CWE-94 · ASVS V5

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Persistent corruption of agent memory, RAG stores, embeddings, or contextual knowledge — unlike prompt injection, the effect persists across sessions, slowly shifting agent behaviour or leaking secrets over time.

**Real-world reference:** Gemini Memory Attack (2024) — indirect prompt injection caused Copilot to store malicious data in persistent memory, enabling long-term behavioural manipulation.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Data & Privacy (full domain) | A | Agent memory and context treated as sensitive data — subject to all Domain A controls | Foundational | Both |
| Detect adversarial input | B002 | Monitor memory write operations for adversarial patterns | Hardening | Both |
| Implement real-time input filtering | B005 | Filter content before it is committed to persistent memory stores | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Apply Domain A data classification to all memory stores — treat agent memory as sensitive by default
- Implement access controls on memory read/write operations
- Enable audit logging on all persistent memory modifications

**Hardening**
- B005 input filtering on all content entering persistent memory or RAG stores
- B002 anomaly detection on memory write patterns — flag unusual content or sources
- Implement memory TTL (time-to-live) — periodic expiry and re-validation of stored context
- Separate short-term and long-term memory with different trust levels

**Advanced**
- Cryptographic integrity verification of memory store contents
- Memory segmentation by trust domain — untrusted external content cannot pollute internal memory
- Automated memory auditing for adversarial content post-ingestion

#### Tools
| Tool | Type | Link |
|---|---|---|
| LlamaIndex | Open-source | https://www.llamaindex.ai |
| Chroma | Open-source | https://www.trychroma.com |
| Weaviate (with RBAC) | Open-source | https://weaviate.io |

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: MITRE ATLAS AML.T0020 · NIST AI RMF MS-2.5

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High

Agent-to-agent (A2A) communication channels lacking strong authentication, encryption, or schema validation enable spoofing, replay attacks, protocol downgrade, and agent-in-the-middle attacks that misdirect entire multi-agent clusters.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Enforce user access privileges to AI systems | B007 | Agent-to-agent trust boundaries enforced with same rigour as user-to-agent boundaries | Foundational | Build |
| Protect model deployment environment | B008 | Secure deployment including encrypted inter-agent communication channels | Foundational | Build |
| Accountability (full domain) | E | Full audit trail of all inter-agent messages — essential for incident reconstruction | Hardening | Build |

#### Mitigations by tier

**Foundational**
- Authenticate all A2A messages — no ambient trust between agents
- Encrypt all inter-agent communication channels (TLS 1.3 minimum)
- Implement schema validation on all A2A message payloads

**Hardening**
- Deploy Domain E full audit logging on all inter-agent communication
- Implement replay attack protection — message nonces and timestamps
- Agent identity certificates with short TTL — no long-lived agent-to-agent trust tokens

**Advanced**
- Mutual TLS (mTLS) for all A2A channels in production
- Zero-trust mesh for multi-agent orchestration — every message independently verified
- Anomaly detection on A2A communication patterns

#### Tools
| Tool | Type | Link |
|---|---|---|
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| Linkerd | Open-source | https://linkerd.io |
| cert-manager | Open-source | https://cert-manager.io |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · ISA/IEC 62443 SR 3.1 · NIST SP 800-82 (OT)

---

### ASI08 — Cascading Agent Failures

**Severity:** High

Single-point faults — a poisoned memory entry, a bad plan, a compromised tool — propagate through multi-agent workflows and amplify into system-wide incidents. Especially critical in OT environments where agent failures can affect physical processes.

**OT note:** In industrial control environments, cascading agent failures can propagate from the AI layer into physical process control. See ISA/IEC 62443 and NIST SP 800-82 crosswalks for OT-specific controls.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Reliability (full domain) | D | Availability, consistency, failure recovery, and rate limiting — the primary domain for cascading failure prevention | Foundational | Both |
| Prevent unauthorized AI agent actions | B006 | Blast radius limitation — agents cannot take actions beyond scope even during failure propagation | Foundational | Both |
| Accountability (full domain) | E | Incident logging and traceability — essential for identifying cascade origin and containment | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Implement Domain D circuit breakers — halt propagation when failure rate exceeds threshold
- Apply B006 scope constraints — a failing agent cannot escalate its own permissions
- Define explicit failure modes for every agent — fail-safe, not fail-open

**Hardening**
- Domain E full audit trail enabling cascade path reconstruction post-incident
- Implement agent isolation — segment sensitive agents from general-purpose agents
- Rate limiting on agent-to-agent communication to prevent runaway loops

**Advanced**
- Automated human-in-the-loop triggers when cascade indicators detected
- Chaos engineering — intentional failure injection testing across multi-agent workflows
- Real-time cascade detection with automated kill-switch per agent segment

#### Tools
| Tool | Type | Link |
|---|---|---|
| Resilience4j | Open-source | https://resilience4j.readme.io |
| LangSmith | Commercial | https://smith.langchain.com |
| OpenTelemetry | Open-source | https://opentelemetry.io |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: ISA/IEC 62443 SR 7.1 · NIST SP 800-82 · AIUC-1 D

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Users anthropomorphise agents — trusting their fluency, apparent expertise, and persuasive outputs — enabling hijacked agents to manipulate humans into approving malicious commands, sharing sensitive data, or performing actions that appear legitimate in audit logs while being agent-driven.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Safety (full domain) | C | Harm prevention and human oversight — the primary AIUC-1 domain for trust exploitation | Foundational | Both |
| Society (full domain) | F | Bias, transparency, and societal impact — covers manipulation and deceptive agent behaviour | Foundational | Both |
| Limit output over-exposure | B009 | Output filtering preventing agents from producing manipulative or deceptive content | Foundational | Both |
| Accountability (full domain) | E | Audit trail distinguishing agent-driven actions from genuinely human-initiated actions | Hardening | Both |

#### Mitigations by tier

**Foundational**
- Domain C guardrails — agents cannot request sensitive data or approvals outside defined workflows
- Domain F transparency requirements — agents must identify themselves as AI in all interactions
- B009 output filtering blocking manipulative language patterns

**Hardening**
- Separate agent conversation interface from security approval flows — never let chat be the consent mechanism
- Domain E audit logging that distinguishes agent-influenced actions from human-initiated actions
- User education on agent trust boundaries — integrated into onboarding

**Advanced**
- Behavioural analysis detecting when agents are nudging users toward specific approvals
- Independent human review required for high-consequence agent recommendations
- Regular red team exercises simulating trust exploitation scenarios

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 52 (transparency) · AIUC-1 C/F · ENISA

---

### ASI10 — Rogue Agents

**Severity:** Critical

Malicious or compromised agents that appear compliant on the surface but pursue hidden goals, hijack workflows, or systematically deviate from their intended purpose — often the end-state of a successful ASI01 or ASI06 attack that has gone undetected.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Third-party testing of adversarial robustness | B001 | Rogue agent detection included in adversarial test scope | Foundational | Both |
| Detect adversarial input | B002 | Runtime behavioural monitoring detecting deviation from intended agent purpose | Hardening | Both |
| Prevent unauthorized AI agent actions | B006 | Scope constraints — rogue agent cannot act outside defined boundaries even if internal goals are compromised | Foundational | Both |
| Safety (full domain) | C | Safety guardrails as the last line of defence against rogue agent outputs | Foundational | Both |
| Accountability (full domain) | E | Full audit trail enabling rogue agent detection, attribution, and forensics | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Domain C guardrails — agents cannot request sensitive data or approvals outside defined workflows
- Domain F transparency requirements — agents must identify themselves as AI in all interactions
- B009 output filtering blocking manipulative language patterns

**Hardening**
- Separate agent conversation interface from security approval flows — never let chat be the consent mechanism
- Domain E audit logging that distinguishes agent-influenced actions from human-initiated actions
- User education on agent trust boundaries — integrated into onboarding

**Advanced**
- Behavioural analysis detecting when agents are nudging users toward specific approvals
- Independent human review required for high-consequence agent recommendations
- Regular red team exercises simulating trust exploitation scenarios

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 52 (transparency) · AIUC-1 C/F · ENISA

---

### ASI10 — Rogue Agents

**Severity:** Critical

Malicious or compromised agents that appear compliant on the surface but pursue hidden goals, hijack workflows, or systematically deviate from their intended purpose — often the end-state of a successful ASI01 or ASI06 attack that has gone undetected.

#### AIUC-1 mapping

| Control | ID | Description | Tier | Scope |
|---|---|---|---|---|
| Third-party testing of adversarial robustness | B001 | Rogue agent detection included in adversarial test scope | Foundational | Both |
| Detect adversarial input | B002 | Runtime behavioural monitoring detecting deviation from intended agent purpose | Hardening | Both |
| Prevent unauthorized AI agent actions | B006 | Scope constraints — rogue agent cannot act outside defined boundaries even if internal goals are compromised | Foundational | Both |
| Safety (full domain) | C | Safety guardrails as the last line of defence against rogue agent outputs | Foundational | Both |
| Accountability (full domain) | E | Full audit trail enabling rogue agent detection, attribution, and forensics | Foundational | Both |

#### Mitigations by tier

**Foundational**
- Deploy Domain E comprehensive audit logging on all agent actions from day one
- B006 strict scope constraints — rogue agent cannot exceed its permission envelope
- Domain C safety guardrails as independent layer from agent logic

**Hardening**
- B002 continuous behavioural monitoring — flag deviation from historical baseline
- Implement agent health checks — periodic verification against intended purpose specification
- Automated quarantine on anomaly detection — isolate suspected rogue agent pending review

**Advanced**
- Multi-agent consensus for high-stakes decisions — a rogue single agent cannot act unilaterally
- Formal specification of agent intended behaviour — machine-verifiable contracts
- Real-time forensic capability — full reproducible trace of every agent decision

#### Tools
| Tool | Type | Link |
|---|---|---|
| Weights & Biases | Commercial | https://wandb.ai |
| Helicone | Open-source | https://www.helicone.ai |
| Langfuse | Open-source | https://langfuse.com |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: MITRE ATLAS · EU AI Act Art. 9 · AIUC-1 C/E

---

## Implementation priority

For teams starting from zero, this is the recommended sequencing:

| Phase | Controls | Rationale |
|---|---|---|
| 1 — Do now | B001, B006, B007, Domain E logging | Highest blast radius, lowest effort |
| 2 — This quarter | B005, B002, Domain A, B008 | Close the detection and data exposure gaps |
| 3 — Next quarter | Domain C, Domain D, B003, B009 | Safety, reliability, and output hardening |
| 4 — Ongoing | Domain F, advanced tiers, red teaming | Continuous improvement and societal controls |

---

## AIUC-1 certification coverage

AIUC-1 certification explicitly covers all 10 ASI risks. Achieving AIUC-1 certification provides documented, third-party-verified evidence of controls against the full Agentic Top 10 — directly usable in vendor assessments, compliance documentation, and enterprise procurement.

See: [AIUC-1 covers all OWASP Agentic Top 10 threats](https://www.aiuc-1.com/research/aiuc-1-certification-covers-all-owasp-agentic-top-10-threats)

---

## References

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [AIUC-1 Standard](https://www.aiuc-1.com)
- [AIUC-1 Security Domain](https://www.aiuc-1.com/security)
- [AIUC-1 Data & Privacy Domain](https://www.aiuc-1.com/data-and-privacy)
- [OWASP AIVSS](https://aivss.owasp.org)
- [OWASP AI Testing Guide](https://owasp.org/www-project-ai-testing-guide/)
- [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — all 10 ASI entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) — maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
