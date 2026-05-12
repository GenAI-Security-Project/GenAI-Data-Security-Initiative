<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic AI Applications 2026 (ASI01-ASI10)
  Framework   : OWASP SAMM v2.0 — Software Assurance Maturity Model
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × OWASP SAMM v2.0

Mapping the [OWASP Top 10 for Agentic AI Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to the [OWASP Software Assurance Maturity Model (SAMM) v2.0](https://owaspsamm.org/) —
the framework for measuring and improving software security programme
maturity across the SDLC.

---

## Why SAMM for agentic AI security

Agentic AI systems — autonomous agents that plan, invoke tools, and
take real-world actions — demand security programme capabilities that
most organisations do not yet have. SAMM is uniquely useful here
because it does not just list controls: it tells you **how mature
your programme must be** to operate agents safely, and **which
lifecycle practices** must improve first.

Three SAMM properties make it essential for agentic deployments:

**Autonomy amplifies gaps.** An under-mature threat modelling practice
(D-TA Level 1) is a manageable risk for a static web application but
an unacceptable risk for an agent with autonomous tool execution.
SAMM's maturity levels make the gap visible.

**Operations practices become critical.** Autonomous agents require
Incident Management (O-IM) and Operational Management (O-OM) at
Level 2 minimum before deployment. SAMM structures the argument for
pre-production maturity gates.

**Supply chain scope expands dramatically.** An agentic system
integrates LLMs, tool APIs, memory stores, orchestration frameworks,
and third-party MCP servers. SAMM's Implementation / Secure Build
(I-SB) and Policy & Compliance (G-PC) practices cover this expanded
attack surface.

---

## SAMM v2.0 structure

| Business Function | Security Practices |
|---|---|
| Governance (G) | Strategy & Metrics (G-SM) · Policy & Compliance (G-PC) · Education & Guidance (G-EG) |
| Design (D) | Threat Assessment (D-TA) · Security Requirements (D-SR) · Security Architecture (D-SA) |
| Implementation (I) | Secure Build (I-SB) · Secure Deployment (I-SD) · Defect Management (I-DM) |
| Verification (V) | Architecture Assessment (V-AA) · Requirements-Driven Testing (V-RT) · Security Testing (V-ST) |
| Operations (O) | Incident Management (O-IM) · Environment Management (O-EM) · Operational Management (O-OM) |

**Maturity levels:**
- Level 1 — Initial/Ad-hoc: Basic security practices, reactive
- Level 2 — Managed: Defined processes, consistent execution
- Level 3 — Optimised: Proactive, metrics-driven, continuously improving

---

## Quick-reference summary

| ID | Name | Severity | Primary SAMM Practices | Maturity Target | Tier |
|---|---|---|---|---|---|
| ASI01 | Prompt Injection in Agentic Systems | Critical | D-TA, I-SB, V-ST, O-IM | L2 min / L3 for high-risk | Foundational–Advanced |
| ASI02 | Excessive Permissions and Scope | High | D-SA, G-SM, V-AA, O-OM | L2 min | Foundational–Hardening |
| ASI03 | Memory Manipulation and Persistence | High | D-TA, I-SB, V-ST, O-EM | L2 min | Hardening–Advanced |
| ASI04 | Multi-Agent Trust Exploitation | High | D-TA, D-SA, G-PC, V-AA | L2 min | Hardening–Advanced |
| ASI05 | Tool and Plugin Abuse | High | D-SR, I-SB, V-ST, G-PC | L2 min | Foundational–Hardening |
| ASI06 | Data Exfiltration via Agentic Channels | Critical | D-TA, V-ST, O-IM, O-OM | L2 min / L3 for high-risk | Hardening–Advanced |
| ASI07 | Supply Chain Compromise in Agent Ecosystems | High | G-PC, I-SB, V-AA, D-TA | L2 min | Foundational–Hardening |
| ASI08 | Inversion of Safety Controls | Critical | D-SA, V-AA, V-ST, O-IM | L3 | Advanced |
| ASI09 | Inadequate Human Oversight and Control | High | G-SM, D-SA, O-IM, O-OM | L2 min | Foundational–Hardening |
| ASI10 | Cascading Agent Failures | High | D-SA, O-IM, O-EM, V-AA | L2 min | Hardening–Advanced |

**SAMM practice codes:**
G-SM = Governance / Strategy & Metrics ·
G-PC = Governance / Policy & Compliance ·
G-EG = Governance / Education & Guidance ·
D-TA = Design / Threat Assessment ·
D-SR = Design / Security Requirements ·
D-SA = Design / Security Architecture ·
I-SB = Implementation / Secure Build ·
I-SD = Implementation / Secure Deployment ·
I-DM = Implementation / Defect Management ·
V-AA = Verification / Architecture Assessment ·
V-RT = Verification / Requirements-Driven Testing ·
V-ST = Verification / Security Testing ·
O-IM = Operations / Incident Management ·
O-EM = Operations / Environment Management ·
O-OM = Operations / Operational Management

---

## Target audience

| Role | Files to prioritise |
|---|---|
| Security programme lead | Full file — use maturity scorecard to build roadmap |
| AppSec / security engineer | Design and Verification sections per relevant ASI entry |
| Platform / infrastructure | Implementation and Operations sections |
| AI red team | Verification / Security Testing columns per entry |
| Compliance / GRC | Governance columns, EU AI Act alignment notes |

---

## Detailed mappings

---

### ASI01 — Prompt Injection in Agentic Systems

Adversarial instructions embedded in untrusted content (tool outputs,
retrieved documents, API responses) hijack agent goal execution,
tool invocation, and action sequences.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Agent input surface threat model | L2 required | Model all injection surfaces: user input, retrieved content, tool responses, sub-agent messages |
| Design / Threat Assessment (D-TA) | B — Risk Profile | Classify agent actions by impact | L2 required | High-impact actions (delete, exfiltrate, send) demand higher injection resistance |
| Implementation / Secure Build (I-SB) | A — Build Process | Mandatory input/output sanitisation | L2 required | Enforce at agent boundary; validate all retrieved content before acting |
| Verification / Security Testing (V-ST) | B — Deep Testing | Adversarial injection test suite | L2 required | Red team injection across all retrieval and tool paths |
| Operations / Incident Management (O-IM) | A — Incident Detection | Alert on unexpected goal deviation | L2 required | Detect agent plan deviation from expected trajectory |
| Governance / Education & Guidance (G-EG) | B — Training | Developer training on agentic injection | L1 minimum | All developers with access to agent code understand injection risk model |

**Maturity target:** L2 minimum; L3 for agents with access to sensitive data or irreversible actions.

#### Three-tier mitigations

**Tier 1 — Immediate (pre-production gate):**
- Define trust boundaries: user instructions, system prompt, retrieved content — never treat retrieved content as same trust level as system prompt
- Implement instruction hierarchy in orchestration layer
- Add tool invocation allow-listing; deny all unregistered tool calls

**Tier 2 — Short-term (first 30 days):**
- Build adversarial injection test cases into CI/CD
- Add anomaly detection on agent plan deviations
- Instrument all tool calls for audit logging

**Tier 3 — Strategic:**
- Continuously update injection test corpus with red team findings
- Implement formal goal verification before high-impact actions
- Establish SAMM D-TA L3: threat models reviewed after each new tool integration

#### Cross-references

- LLM Top 10: LLM01 (Prompt Injection)
- DSGAI: DSGAI01 (Prompt Injection via Data Channels)
- See also: [Agentic_AITG.md](Agentic_AITG.md) TC-ASI01, [Agentic_MITREATLAS.md](Agentic_MITREATLAS.md) AML.T0054

---

### ASI02 — Excessive Permissions and Scope

Agents granted overly broad permissions — filesystem access, API
scopes, database rights — beyond those required for their declared
task. Violation of least-privilege creates irreversible blast radius
when compromised.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Architecture (D-SA) | A — Architecture | Least-privilege agent permission model | L2 required | Define per-agent permission sets; review in architecture assessment |
| Governance / Strategy & Metrics (G-SM) | B — Roadmap | Agentic access governance policy | L2 required | Formalise agent identity and permission lifecycle |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Agent permission audit | L2 required | Periodic review of declared vs granted permissions per agent |
| Operations / Operational Management (O-OM) | B — Review | Permission drift detection | L2 required | Alert when agent requests permissions outside declared scope |
| Governance / Policy & Compliance (G-PC) | A — Policy | Agent permission policy | L1 minimum | Document what permissions each agent class is authorised to hold |

**Maturity target:** L2 minimum; architecture review must include explicit permission scope sign-off.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Enumerate all permissions currently granted to each agent in production
- Remove any permissions not exercised in the past 30 days (JIT pattern)
- Treat agent identities as NHI: apply OWASP NHI Top 10 controls

**Tier 2 — Short-term:**
- Implement permission scope declaration in agent manifest/descriptor
- Gate deployments: no deployment without signed permission manifest
- Automate drift detection: alert when runtime permissions exceed manifest

**Tier 3 — Strategic:**
- Achieve D-SA L3: architecture review board includes agent permission review
- Implement dynamic JIT permission issuance per task (see RECIPES.md)
- Quarterly access review for all agent identities

#### Cross-references

- LLM Top 10: LLM06 (Excessive Agency)
- DSGAI: DSGAI07 (Excessive Data Access)
- See also: [Agentic_OWASP_NHI.md](Agentic_OWASP_NHI.md) NHI-2/NHI-3, [Agentic_ASVS.md](Agentic_ASVS.md)

---

### ASI03 — Memory Manipulation and Persistence

Attackers corrupt agent memory — short-term context, long-term
episodic stores, shared memory buses — to implant false beliefs,
alter future decisions, or persist across agent restarts.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Memory attack surface model | L2 required | Include memory store read/write paths in threat model |
| Implementation / Secure Build (I-SB) | A — Build Process | Memory input validation | L2 required | Validate and sanitise all content written to persistent memory |
| Verification / Security Testing (V-ST) | B — Deep Testing | Memory poisoning test cases | L2 required | Test persistent memory integrity across session boundaries |
| Operations / Environment Management (O-EM) | A — Patching | Memory store hardening | L2 required | Apply access controls, encryption at rest, and integrity verification to all memory stores |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Memory store architecture review | L1 minimum | Confirm memory stores have appropriate access controls |

**Maturity target:** L2 minimum; memory stores must be treated as security-critical infrastructure.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Apply access controls to all persistent memory stores (vector DB, relational, episodic)
- Add integrity metadata (HMAC or signature) to all memory writes
- Log all memory read/write operations

**Tier 2 — Short-term:**
- Implement memory validation pipeline: content written to persistent memory passes sanitisation
- Add memory anomaly detection: flag unexpected belief updates
- Define memory TTL and rotation policy

**Tier 3 — Strategic:**
- Periodic memory audit: replay historical decisions to detect contamination
- Implement formal provenance tracking for all memory entries
- Cross-session memory integrity verification

#### Cross-references

- DSGAI: DSGAI10 (Context Window Poisoning), DSGAI11 (Session Persistence Attacks)
- See also: [Agentic_AITG.md](Agentic_AITG.md) TC-ASI03, [LLM_CWE_CVE.md](../llm-top10/LLM_CWE_CVE.md)

---

### ASI04 — Multi-Agent Trust Exploitation

Malicious or compromised agents in a multi-agent orchestration
environment are trusted by peer agents or orchestrators, enabling
lateral movement, instruction injection, or coordinated attacks
across the agent network.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Inter-agent trust boundary model | L2 required | Explicitly model trust relationships between agents; default deny |
| Design / Security Architecture (D-SA) | A — Architecture | Agent authentication framework | L2 required | Mutual authentication between all agent-to-agent communication |
| Governance / Policy & Compliance (G-PC) | A — Policy | Multi-agent deployment policy | L2 required | Policy governing what agents may instruct other agents to do |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Inter-agent trust architecture review | L2 required | Review and document all agent-to-agent trust grants |
| Verification / Security Testing (V-ST) | B — Deep Testing | Rogue agent simulation | L2 required | Test whether a compromised sub-agent can escalate through the network |

**Maturity target:** L2 minimum; no multi-agent deployment without explicit trust architecture review.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Implement authentication tokens for all inter-agent messages
- Establish maximum privilege boundary: no agent may grant permissions it does not hold
- Log all inter-agent instruction exchanges

**Tier 2 — Short-term:**
- Deploy agent identity registry: all agents have verifiable, revocable identities
- Implement message signing for orchestrator-to-agent instructions
- Red team exercise: simulate compromised sub-agent attempting lateral movement

**Tier 3 — Strategic:**
- Formal trust model: cryptographic attestation of agent identity and permission set
- Automated verification that no agent in a network exceeds declared scope
- D-TA L3: threat model updated after every new agent added to orchestration network

#### Cross-references

- LLM Top 10: LLM08 (Excessive Agency via Multi-Model)
- See also: [Agentic_MITREATLAS.md](Agentic_MITREATLAS.md), [Agentic_OWASP_NHI.md](Agentic_OWASP_NHI.md) NHI-1

---

### ASI05 — Tool and Plugin Abuse

Malicious, misconfigured, or shadow tools integrated into agentic
workflows are invoked by agents, enabling data exfiltration, privilege
escalation, or unintended action execution via the tool interface.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Requirements (D-SR) | A — Requirements | Tool integration security requirements | L2 required | Security requirements for every tool: auth, scope, output validation |
| Implementation / Secure Build (I-SB) | A — Build Process | Tool allow-list enforcement | L2 required | Only approved tools can be registered; unsigned tools are rejected |
| Verification / Security Testing (V-ST) | A — Automated | Tool integration scanning | L2 required | Automated checks on tool descriptors, endpoints, and permissions |
| Governance / Policy & Compliance (G-PC) | A — Policy | Third-party tool approval policy | L2 required | Process for approving, reviewing, and revoking tool integrations |
| Operations / Operational Management (O-OM) | A — Monitoring | Tool call anomaly detection | L1 minimum | Alert on tool calls outside normal operating parameters |

**Maturity target:** L2 minimum; tool governance programme required before any third-party tool integration.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Enumerate all tools currently accessible to deployed agents
- Remove any unreviewed tools from production immediately
- Validate all tool descriptors (MCP server schemas) for completeness and accuracy

**Tier 2 — Short-term:**
- Implement tool review board: all tools reviewed before integration
- Add tool call logging and anomaly detection
- Conduct red team exercise: provide malicious tool descriptor to agent

**Tier 3 — Strategic:**
- I-SB L3: automated tool supply chain analysis in CI/CD
- Continuous tool permission drift detection
- Tool descriptor integrity verification (see RECIPES.md)

#### Cross-references

- LLM Top 10: LLM07 (System Prompt Leakage via Tools), LLM03 (Supply Chain)
- DSGAI: DSGAI13 (Data Leakage through Tool Integration)
- See also: [Agentic_AITG.md](Agentic_AITG.md) TC-ASI05, [Agentic_CWE_CVE.md](Agentic_CWE_CVE.md)

---

### ASI06 — Data Exfiltration via Agentic Channels

Agents with broad data access and outbound communication capabilities
are used — intentionally by an attacker or through injection — to
exfiltrate sensitive data via tool calls, API requests, generated
output, or inter-agent messages.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Exfiltration path analysis | L2 required | Enumerate all outbound data paths from agent: tools, APIs, generated output |
| Verification / Security Testing (V-ST) | B — Deep Testing | Exfiltration simulation | L2 required | Test whether agent can be instructed to exfiltrate via each outbound channel |
| Operations / Incident Management (O-IM) | A — Incident Detection | Outbound data volume alerting | L2 required | Alert on unexpected data volumes in tool calls or API responses |
| Operations / Operational Management (O-OM) | A — Monitoring | DLP integration for agent outputs | L2 required | Apply DLP controls to all agent-generated output before delivery |
| Design / Security Architecture (D-SA) | B — Controls | Output filtering architecture | L2 required | All agent outputs pass through content inspection before leaving system boundary |

**Maturity target:** L2 minimum; L3 for agents with access to PII, PCI data, or classified information.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Apply output content inspection to all agent responses
- Restrict tool call payloads: define maximum data volume per tool invocation
- Log all outbound data with full payloads for forensic review

**Tier 2 — Short-term:**
- Deploy DLP scanning on agent output pipeline
- Implement per-session data access budgets
- Red team: simulate SSRF-style exfiltration via tool calls

**Tier 3 — Strategic:**
- O-IM L3: automated exfiltration detection using behavioural baselines
- D-TA L3: threat model updated for every new outbound integration
- Integrate with SIEM for cross-session pattern detection

#### Cross-references

- LLM Top 10: LLM02 (Sensitive Information Disclosure)
- DSGAI: DSGAI06 (Unintended Data Disclosure), DSGAI08 (Data Leakage in Retrieval)
- See also: [Agentic_ENISA.md](Agentic_ENISA.md), [LLM_SAMM.md](../llm-top10/LLM_SAMM.md)

---

### ASI07 — Supply Chain Compromise in Agent Ecosystems

Third-party components in the agentic stack — LLM providers, MCP
servers, orchestration frameworks, tool libraries, memory store
dependencies — are compromised or tampered with, introducing
malicious behaviour into the agent deployment.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Governance / Policy & Compliance (G-PC) | A — Policy | Third-party agentic component policy | L2 required | Approved vendor list for all agentic stack components |
| Implementation / Secure Build (I-SB) | B — Dependencies | Dependency inventory and SBOM | L2 required | SBOM for all agentic system components including LLM APIs and tool servers |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Agentic supply chain architecture review | L2 required | Architecture review validates all third-party components against policy |
| Design / Threat Assessment (D-TA) | A — Threat Modeling | Supply chain threat model | L2 required | Model compromise scenarios for each third-party component |
| Operations / Operational Management (O-OM) | B — Review | Vendor security posture monitoring | L1 minimum | Track security advisories for all integrated components |

**Maturity target:** L2 minimum; SBOM required before production deployment.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Inventory all third-party components in the agentic stack
- Generate initial SBOM; flag components without security contact or last-updated date
- Pin all dependency versions; reject floating versions in production

**Tier 2 — Short-term:**
- Implement automated vulnerability scanning for agentic SBOM
- Review MCP server descriptors: any server should be treated as third-party software
- Add integrity verification for all LLM API endpoints (certificate pinning where applicable)

**Tier 3 — Strategic:**
- G-PC L3: formal vendor security assessment for all critical agentic components
- I-SB L3: automated supply chain analysis in CI/CD with policy enforcement
- Periodic red team exercise targeting supply chain attack vectors

#### Cross-references

- LLM Top 10: LLM03 (Supply Chain Vulnerabilities)
- DSGAI: DSGAI16 (Third-Party Data Dependencies), DSGAI17 (Model Supply Chain Risks)
- See also: [Agentic_CWE_CVE.md](Agentic_CWE_CVE.md), [Agentic_AITG.md](Agentic_AITG.md) TC-ASI07

---

### ASI08 — Inversion of Safety Controls

Safety guardrails — content filters, output validators, human
oversight gates — are bypassed, disabled, or inverted through
adversarial prompting, model manipulation, or architectural
misconfiguration, enabling unsafe behaviour to pass through.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Architecture (D-SA) | A — Architecture | Defence-in-depth for safety controls | L3 required | Safety controls must be layered — no single-point bypass path |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Safety control architecture review | L3 required | Independent review of every safety control bypass scenario |
| Verification / Security Testing (V-ST) | B — Deep Testing | Adversarial safety bypass testing | L3 required | Dedicated red team exercise targeting guardrail bypass |
| Operations / Incident Management (O-IM) | A — Incident Detection | Safety control bypass alerting | L2 required | Alert immediately when output validator is disabled or bypassed |
| Governance / Strategy & Metrics (G-SM) | A — Policy | Safety control governance | L2 required | No production agent deployment without signed safety control architecture review |

**Maturity target:** L3 required for any deployment where safety control bypass creates physical, financial, or reputational harm.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Audit all existing safety controls: identify any single points of failure
- Confirm output validators cannot be disabled via input
- Implement immutable safety control logs: controls cannot be silently disabled

**Tier 2 — Short-term:**
- Add independent safety check outside the LLM inference path (rule-based classifier)
- Red team exercise: attempt to disable or invert each safety control independently
- V-AA review: peer review of all safety control architecture before deployment

**Tier 3 — Strategic:**
- D-SA L3: formal safety architecture review board with external member for high-risk deployments
- V-ST L3: continuous adversarial red teaming of safety controls in staging
- Formal safety control test plan maintained and updated quarterly

#### Cross-references

- LLM Top 10: LLM01 (Prompt Injection as safety bypass vector)
- DSGAI: DSGAI05 (Guardrail Circumvention)
- See also: [Agentic_EUAIAct.md](Agentic_EUAIAct.md) Art. 15 (robustness), [Agentic_AIVSS.md](Agentic_AIVSS.md)

---

### ASI09 — Inadequate Human Oversight and Control

Agents operate autonomously beyond the scope where human review
would catch errors, bias, or adversarial manipulation before
irreversible actions are taken. Missing confirmation gates, override
mechanisms, or audit trails prevent effective human control.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Governance / Strategy & Metrics (G-SM) | A — Policy | Autonomy policy | L2 required | Define maximum autonomy scope per agent class; mandate oversight gates |
| Design / Security Architecture (D-SA) | A — Architecture | Human oversight gate architecture | L2 required | Design confirmation gate pattern for all high-impact actions |
| Operations / Incident Management (O-IM) | A — Incident Detection | Autonomous action alerting | L2 required | Alert when agent executes high-impact actions without confirmation |
| Operations / Operational Management (O-OM) | A — Monitoring | Human-in-the-loop audit trail | L2 required | Immutable audit log of all autonomous actions for post-hoc review |
| Governance / Education & Guidance (G-EG) | A — Training | Operator training on oversight | L1 minimum | Operators understand when to intervene and how to trigger override |

**Maturity target:** L2 minimum; EU AI Act Article 14 compliance requires documented oversight mechanism for high-risk AI.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Enumerate all currently autonomous high-impact actions in production
- Add confirmation gates for all irreversible actions (delete, send, pay, publish)
- Implement emergency stop that halts all agent activity immediately

**Tier 2 — Short-term:**
- Define autonomy tiers per action class: auto / confirm / human-required
- Implement G-SM L2: formal autonomy policy reviewed and signed by CISO
- Add audit trail: every agent action logged with rationale and outcome

**Tier 3 — Strategic:**
- O-OM L3: real-time oversight dashboard for operations team
- G-SM L3: autonomy policy updated after every incident or near-miss
- Formal EU AI Act Article 14 compliance review for all high-risk deployments

#### Cross-references

- LLM Top 10: LLM06 (Excessive Agency)
- DSGAI: DSGAI04 (Insufficient Access Controls for Autonomous Processing)
- See also: [Agentic_EUAIAct.md](Agentic_EUAIAct.md), [Agentic_AIVSS.md](Agentic_AIVSS.md)

---

### ASI10 — Cascading Agent Failures

In multi-agent orchestration, a failure or compromise in one agent
propagates through the network — downstream agents act on corrupted
state, errors amplify through chaining, and the aggregate effect
exceeds what any single agent could cause.

#### SAMM mapping

| Practice | Stream | Activity | Maturity Level | How it applies |
|---|---|---|---|---|
| Design / Security Architecture (D-SA) | A — Architecture | Fault isolation architecture | L2 required | Design circuit breakers and blast radius containment between agents |
| Operations / Incident Management (O-IM) | A — Incident Detection | Cascade detection and alerting | L2 required | Detect correlated failures across multiple agents; alert before full cascade |
| Operations / Environment Management (O-EM) | A — Patching | Agent health monitoring | L2 required | Continuous health checks; automatic isolation of degraded agents |
| Verification / Architecture Assessment (V-AA) | A — Assessment | Cascade failure architecture review | L2 required | Verify blast radius containment in architecture review |
| Operations / Incident Management (O-IM) | B — Response | Multi-agent incident playbook | L2 required | Documented runbook for cascade scenarios including rollback procedures |

**Maturity target:** L2 minimum; O-IM cascade playbook required before multi-agent production deployment.

#### Three-tier mitigations

**Tier 1 — Immediate:**
- Add health checks to all agents in production; isolate on failure detection
- Implement circuit breaker pattern between orchestrator and sub-agents
- Document current blast radius: if agent X fails, which agents are affected?

**Tier 2 — Short-term:**
- Red team: simulate cascading failure starting from one compromised sub-agent
- Deploy O-IM playbook for multi-agent cascade incidents
- Add per-agent state checkpointing to enable rollback

**Tier 3 — Strategic:**
- D-SA L3: formal chaos engineering programme for multi-agent orchestration
- O-EM L3: automated cascade detection with predictive alerting
- Architecture pattern: stateless agents wherever possible to limit propagation surface

#### Cross-references

- LLM Top 10: LLM10 (Unbounded Consumption as cascade trigger)
- DSGAI: DSGAI19 (Cascading Data Failures)
- See also: [Agentic_MAESTRO.md](Agentic_MAESTRO.md) L3 Agent Frameworks, [Agentic_ISA62443.md](Agentic_ISA62443.md)

---

## SAMM maturity scorecard — agentic AI minimum viable levels

Use this scorecard to assess programme readiness before deploying
autonomous agents in production. Complete a column for each agent
system being assessed.

| Practice | Minimum Viable Level | Current Level | Gap | Priority |
|---|:---:|:---:|:---:|:---:|
| G-SM Strategy & Metrics | L2 | | | |
| G-PC Policy & Compliance | L2 | | | |
| G-EG Education & Guidance | L1 | | | |
| D-TA Threat Assessment | L2 | | | |
| D-SR Security Requirements | L2 | | | |
| D-SA Security Architecture | L2 | | | |
| I-SB Secure Build | L2 | | | |
| I-SD Secure Deployment | L1 | | | |
| I-DM Defect Management | L1 | | | |
| V-AA Architecture Assessment | L2 | | | |
| V-RT Requirements-Driven Testing | L1 | | | |
| V-ST Security Testing | L2 | | | |
| O-IM Incident Management | L2 | | | |
| O-EM Environment Management | L2 | | | |
| O-OM Operational Management | L2 | | | |

**Scoring:** Any practice below Minimum Viable Level is a **deployment blocker**
for autonomous agents with access to sensitive data or irreversible actions.

**EU AI Act note:** G-SM and O-IM at L2+ are minimum requirements to demonstrate
Art. 14 (human oversight) and Art. 9 (risk management) compliance.

---

## Implementation priority table

| Priority | Practices | ASI entries addressed |
|---|---|---|
| P1 — Pre-production gate | D-TA L2, I-SB L2, O-IM L2 | ASI01, ASI06, ASI08, ASI10 |
| P2 — First 30 days | D-SA L2, V-ST L2, G-PC L2 | ASI02, ASI04, ASI05, ASI07 |
| P3 — 60-day milestone | V-AA L2, O-OM L2, G-SM L2 | ASI03, ASI09 |
| P4 — Programme maturity | All practices L3, chaos engineering | ASI08 (full coverage) |

---

## References

- [OWASP SAMM v2.0](https://owaspsamm.org/)
- [OWASP Top 10 for Agentic AI Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP LLM Top 10 2025 × SAMM](../llm-top10/LLM_SAMM.md)
- [Agentic_AITG.md](Agentic_AITG.md) — structured test cases for all ASI entries
- [Agentic_AIVSS.md](Agentic_AIVSS.md) — autonomy premium scoring
- [shared/RECIPES.md](../shared/RECIPES.md) — implementation patterns

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-03-27 | Initial release — full mapping ASI01–ASI10 to SAMM v2.0 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
