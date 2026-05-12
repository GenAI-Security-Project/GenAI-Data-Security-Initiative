<!--
  GenAI Security Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10)
  Framework   : ISA/IEC 62443 — Industrial Automation and Control Systems Security
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × ISA/IEC 62443

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
— the international standard for Industrial Automation and Control
Systems (IACS) security.

---

## Why agentic AI in OT demands its own mapping

A static LLM in OT is a risk. An autonomous agent in OT is a
qualitatively different threat category.

The difference is not degree — it is kind. Where a static LLM waits
for a query and returns a response, an agentic AI plans, executes
multi-step tasks, maintains persistent memory, calls tools autonomously,
and operates for extended periods without human interaction. In an OT
environment, these properties translate directly into:

- **Autonomous tool execution** reaching historian write-back,
  work order systems, or SCADA interfaces without per-action
  human confirmation
- **Persistent memory** that can be poisoned through a single
  interaction and continue influencing process decisions for
  weeks or months
- **Multi-agent orchestration** creating cascading failure paths
  that span Zone 3 and Zone 4 simultaneously
- **Dynamic tool loading** via MCP and plugin protocols that
  introduce supply chain risks at runtime, not just at deployment

The ISA/IEC 62443 framework was designed before autonomous AI agents
existed as a practical deployment pattern. This mapping translates
agentic AI risks into the zone, conduit, security level, and
foundational requirement language that OT security engineers use —
and explicitly identifies where the standard's existing controls
are sufficient, where they need augmentation, and where new
controls specific to agentic AI are required.

---

## Agentic AI OT deployment patterns and their zone risk

| Deployment pattern | Zone location | Primary ASI risks |
|---|---|---|
| Autonomous maintenance scheduling agent | Zone 3 / Zone 3–4 boundary | ASI01, ASI02, ASI03, ASI08 |
| Multi-agent process optimisation | Zone 3 | ASI01, ASI02, ASI08, ASI10 |
| Autonomous anomaly response agent | Zone 3 | ASI01, ASI02, ASI06, ASI09 |
| Supply chain and procurement agent | Zone 4 with Zone 3 data access | ASI03, ASI04, ASI09 |
| Digital twin orchestration agent | Zone 3–4 boundary | ASI01, ASI06, ASI08, ASI10 |
| Operator assistant with tool access | Zone 3 | ASI01, ASI02, ASI06, ASI09 |
| Multi-agent incident response coordinator | Zone 3 | ASI07, ASI08, ASI10 |

**Hard architectural rules for OT agentic deployments:**

1. No agentic AI may execute control actions at Zone 2 or below
   without a validated, human-controlled approval chain
2. No agent may hold persistent memory containing Zone 2 or Zone 1
   device credentials, safety parameters, or control logic
3. All agent-to-OT-system communication must cross a conduit with
   schema validation and allowlisted operations
4. Multi-agent orchestration must never share a communication channel
   with Zone 3 control traffic
5. Every agent deployed in Zone 3 must have a defined kill switch —
   an operator-accessible mechanism to halt all agent activity
   immediately without affecting process control

---

## Security level guidance for agentic deployments

Agentic AI introduces autonomy as a new risk amplifier that ISA/IEC
62443's security level model did not originally account for. The
following adjustments apply:

| Agentic factor | SL adjustment | Rationale |
|---|---|---|
| Autonomous tool execution (any OT tool) | +1 SL | Removes human confirmation from the attack path |
| Persistent memory in Zone 3 | +1 SL | Poisoned memory persists across sessions |
| Multi-agent orchestration in Zone 3 | +1 SL | Cascading failure potential across multiple systems |
| Dynamic tool loading (MCP/plugins) at runtime | +1 SL | Supply chain attack surface at runtime |
| Agent with Zone 2 visibility (read) | +1 SL minimum | Zone 2 access elevates all risk |
| Agent with any Zone 2 write capability | SL 3 minimum | No autonomous Zone 2 write below SL 3 |

---

## Quick-reference summary

| ID | Name | OT Severity | Primary 62443 FRs / SRs | Minimum SL | Tier |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | **Critical** | FR 3 SI-3, FR 2 UC-2/UC-6, FR 6 TRE-1 | SL 2–3 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | **Critical** | FR 2 UC-2/UC-1, FR 3 SI-3, FR 6 TRE-6 | SL 2–3 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | **Critical** | FR 1 IAC-2/IAC-6, FR 2 UC-2, FR 4 DC-4 | SL 2–3 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | FR 3 SI-2, FR 2 UC-6, 62443-2-4 | SL 2 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | **Critical** | FR 3 SI-3, FR 2 UC-3, FR 3 SI-7 | SL 3 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | **Critical** | FR 3 SI-3/SI-7, FR 6 TRE-1, FR 3 SI-1 | SL 2–3 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | FR 1 IAC-3, FR 4 DC-1/DC-4, FR 3 SI-1 | SL 2–3 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | **Critical** | FR 7 RA-6/RA-7, FR 6 TRE-6, FR 5 RDF-1 | SL 2–3 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | High | FR 2 UC-3, FR 6 TRE-2, FR 3 SI-1 | SL 2 | Foundational–Hardening |
| ASI10 | Rogue Agents | **Critical** | FR 3 SI-7, FR 6 TRE-1, FR 2 UC-2/UC-6 | SL 3 | Hardening–Advanced |

---

## Audience tags

- **OT security engineer** — full file, primary reference for agentic AI in OT
- **ICS security architect** — zone model, multi-agent orchestration, kill switch design
- **Control system engineer** — ASI01, ASI02, ASI06, ASI08 entries
- **Safety engineer** — ASI02, ASI08, ASI10 entries — SIS intersection
- **CISO (critical infrastructure)** — SL mapping and governance sections
- **OT procurement** — 62443-2-4, ASI04 supply chain entry

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**OT Severity:** Critical

An attacker redirects an agent's objectives or decision logic through
direct or indirect instruction injection. In OT, a hijacked agent does
not return a bad response — it autonomously executes a multi-step
attack chain across OT tools, historian interfaces, and downstream
agents before any human can intervene.

**OT-specific threat scenario:**
An autonomous maintenance scheduling agent processes a work order
request that contains indirect prompt injection from a compromised
external vendor system. The agent's goal is redirected to create a
work order that schedules maintenance on a safety-critical valve
during peak load conditions — autonomously submitting the work order
to the CMMS and notifying the maintenance crew before any human
reviews the agent's reasoning.

**OT amplifier:** The agent's autonomy means the entire attack chain
— goal hijack, tool invocation, work order submission, notification —
executes without any human in the loop. In a static LLM, a human
would see the bad recommendation and reject it. In an agent, the
action is already taken.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.3 | FR 3 — System Integrity | All inputs to OT agents validated for integrity — no unvalidated external content directly into agent context |
| Least privilege | SR 2.2 | FR 2 — Use Control | Agents granted minimum tool access — each tool scoped to specific OT function, read-only by default |
| Use control enforcement | SR 2.1 | FR 2 — Use Control | Agent actions in OT context subject to explicit use controls — goal-changing actions require human confirmation |
| Timely response to events | SR 6.1 | FR 6 — TRE | Goal hijack indicators treated as security events — agent suspended, human notified, actions reversed where feasible |
| Session lock | SR 1.9 | FR 1 — IAC | Operator-accessible agent kill switch — halt all agent activity immediately without affecting process control |

#### Zone and conduit controls

**Goal change detection at conduit:**
Any agent action that represents a change from its stated goal must
be held at the conduit pending human confirmation. The conduit
implements goal-state verification — comparing the agent's stated
objective at session start against the actions it is attempting to
execute. Divergence triggers suspension.

**Tool invocation gate:**
All agent tool invocations in Zone 3 pass through a validated tool
gateway at the conduit. The gateway enforces:
- Allowlisted tool operations per agent role
- Parameter validation against safe ranges for OT-relevant parameters
- Human confirmation for any tool invocation with irreversible
  consequences in the OT environment

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.3: Treat all external content processed by OT agents
  as untrusted — historian data, vendor communications,
  external reports, and web content all require input
  validation before entering agent context
- SR 2.2: Implement and enforce least-privilege tool access —
  maintenance agent cannot access process control interfaces,
  optimisation agent cannot access safety system data
- Implement operator kill switch — documented, tested, and
  accessible from Zone 3 operator consoles

**Hardening (SL 2–3)**
- SR 2.1: Implement goal-state verification at the agent-OT
  interface — agent must declare its goal at session start,
  deviations trigger suspension and human review
- Require human confirmation for any agent action that modifies
  OT system state — work orders, setpoint changes, alarm
  configuration updates, maintenance schedules
- SR 6.1: Define and test incident response for agent goal
  hijack — suspension procedure, action reversal checklist,
  OT impact assessment, root cause process

**Advanced (SL 3–4)**
- Implement cryptographically signed agent goal specifications —
  runtime goal state must match the signed original or agent
  execution halts and human review is triggered
- Deploy OT-specific adversarial testing — indirect injection
  via historian data, alarm logs, maintenance records, and
  vendor communications before each OT deployment
- Include agent goal hijack scenarios in Process Hazard
  Analysis (PHA) — assess what physical consequences are
  possible if each agent's goal is redirected

#### Tools

| Tool | Type | Link |
|---|---|---|
| Claroty | Commercial | https://claroty.com |
| Dragos | Commercial | https://www.dragos.com |
| Garak (adversarial testing) | Open-source | https://github.com/leondz/garak |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways, DSGAI15 Over-Broad Context Windows
- Other frameworks: NIST SP 800-82 Rev 3 · MITRE ATT&CK ICS T0855 · IEC 61511

---

### ASI02 — Tool Misuse & Exploitation

**OT Severity:** Critical

Agents misuse legitimate OT tools — historian write-back, CMMS work
order creation, alarm management interfaces, setpoint adjustment APIs —
due to prompt manipulation, goal hijack, or unsafe delegation. The
danger is not the manipulation itself but the physical consequence
of what the tool does in response: process change, alarm suppression,
maintenance action.

**OT-specific threat scenario:**
An autonomous process optimisation agent is manipulated through
poisoned sensor telemetry. The agent's tool invocation logic causes
it to call the setpoint adjustment API with parameters outside the
safe operating envelope — the tool executes the call because it is
a legitimate, authorised tool operating within its defined permissions.
The process moves outside safe limits before the operator notices.

**OT amplifier:** OT tools have physical consequences. A tool call
that writes to a historian is annoying. A tool call that adjusts
a process setpoint or acknowledges a safety alarm is potentially
catastrophic. The principle of least agency becomes a safety
requirement, not a security best practice.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Least privilege | SR 2.2 | FR 2 — Use Control | Per-tool minimum permission — setpoint adjustment tool restricted to specific tags and safe ranges |
| Use control | SR 2.1 | FR 2 — Use Control | Allowlisted tool operations for each agent role — agent cannot invoke tools outside its defined function |
| Timely response to events | SR 6.6 | FR 6 — TRE | Anomalous tool invocation patterns detected and responded to — alert, suspend, investigate |
| Software and information integrity | SR 3.3 | FR 3 — System Integrity | Tool descriptor integrity verified — poisoned MCP tool descriptors rejected at loading |

#### Zone and conduit controls

**Per-tool permission manifests:**
Every agent tool in an OT deployment must have a formally defined
permission manifest specifying:
- Which historian tags the tool can read / write
- Which SCADA interfaces the tool can query / command
- Which parameter ranges are permitted for setpoint tools
- Whether the tool can acknowledge alarms (default: No)
- Whether the tool invocation is reversible (determines confirmation requirement)

**Irreversibility classification:**
All OT agent tools classified by reversibility:

| Tool class | Reversibility | Confirmation requirement |
|---|---|---|
| Historian read | Fully reversible | None — log only |
| Historian write | Partially reversible | Operator confirmation |
| Work order creation | Reversible (before execution) | Operator review before submission |
| Setpoint adjustment | Reversible (with action) | Mandatory human confirmation, no exceptions |
| Alarm acknowledgement | Irreversible | Prohibited for autonomous agents |
| Safety function interface | Irreversible | Prohibited for all agents — human only |

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 2.2: Implement and enforce per-tool permission manifests
  for all OT agent tools — define and enforce at the conduit,
  not in the model or agent framework
- Classify all OT agent tools by reversibility — irreversible
  tool invocations require human confirmation, no exceptions
- Block agents from invoking safety system interfaces —
  safety functions are human-only operations

**Hardening (SL 2–3)**
- SR 2.1: Implement tool allowlisting at the OT conduit —
  agents cannot invoke tools outside their defined role
  regardless of what their goal state requests
- SR 6.6: Implement anomalous tool invocation detection —
  alert on tool calls with unusual parameters, out-of-hours
  invocations, or high-frequency repetitive calls
- Validate all MCP tool descriptors before agent loading in
  OT environment — reject modified or unrecognised descriptors

**Advanced (SL 3–4)**
- Implement per-invocation parameter validation at the
  conduit — all tool parameters validated against safe
  ranges before execution, not just tool identity
- Include tool misuse scenarios in Process Hazard Analysis —
  assess what physical consequences are possible if each
  tool is called with adversarial parameters
- SR 6.6: Integrate OT agent tool invocation logs into SIEM —
  unusual invocation patterns treated as potential security
  events with defined OT incident response procedures

#### Tools

| Tool | Type | Link |
|---|---|---|
| Claroty | Commercial | https://claroty.com |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: NIST SP 800-82 Rev 3 · IEC 61511 (SIL) · MITRE ATT&CK ICS T0831

---

### ASI03 — Identity & Privilege Abuse

**OT Severity:** Critical

Agents inherit OT system credentials — historian service accounts,
SCADA read tokens, CMMS API keys, DCS operator credentials — and
attackers exploit weak privilege boundaries to reuse those credentials
beyond their intended scope. In OT environments, these credentials
provide access to safety-critical systems.

**OT-specific threat scenario:**
An autonomous maintenance agent is issued a historian service account
with read access to all process tags for anomaly detection. An attacker
who compromises the agent's memory store recovers the service account
credentials and uses them directly — outside the agent framework —
to query the historian for sensitive process data and network topology.

**OT amplifier:** OT service accounts often have broader access than
intended because OT systems were not designed for fine-grained access
control. An agent inheriting an operator-class credential may have
access to Zone 2 device configuration, safety function parameters,
and network topology that no single human operator should hold
simultaneously.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Identification and authentication | SR 1.2 | FR 1 — IAC | All agent access to OT systems using distinct, traceable identity — not shared service accounts |
| Authenticator management | SR 1.6 | FR 1 — IAC | Agent credentials managed with defined lifecycle — issuance, rotation, revocation procedures |
| Least privilege | SR 2.2 | FR 2 — Use Control | Agent credentials scoped to minimum OT data access required for defined task |
| Data confidentiality in transit | SR 4.1 | FR 4 — Data Confidentiality | Agent credentials never transmitted or stored in cleartext within OT network |
| Session lock | SR 1.9 | FR 1 — IAC | Agent sessions terminated and credentials revoked immediately on compromise detection |

#### Zone and conduit controls

**OT credential architecture for agents:**
- Each agent role receives a unique service identity — no
  shared service accounts across agent deployments
- Agent credentials are scoped to specific historian tags,
  SCADA read endpoints, or CMMS functions — not broad
  system-level access
- Credentials are time-limited — issued at agent session
  start, revoked at session end, no persistent standing
  credentials in agent memory
- Credential issuance logged in OT identity management —
  all agent credential operations auditable

**Zone 2 access prohibition:**
No agent credential may grant access to Zone 2 device interfaces,
PLC programming ports, or safety system configuration interfaces.
Any agent requiring visibility of Zone 2 data must access it through
a Zone 3 historian proxy — never directly.

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 1.2: Issue distinct agent identities for each OT agent
  deployment — no shared service accounts, all agent actions
  attributable to a specific agent identity in OT audit log
- SR 2.2: Scope all agent credentials to minimum required
  OT access — historian read limited to specific tag groups,
  no broad SELECT across all tags
- SR 1.9: Implement immediate credential revocation on agent
  termination — credentials expire at session end, not on
  a rotation schedule

**Hardening (SL 2–3)**
- SR 1.6: Implement agent credential lifecycle management —
  issuance, rotation, revocation all logged in OT identity
  management system
- SR 4.1: Enforce encrypted storage and transmission for
  all agent credentials in OT environment — no cleartext
  credentials in agent memory, config files, or logs
- Implement agent credential anomaly detection — usage of
  agent credentials outside expected OT system scope triggers
  immediate alert and session suspension

**Advanced (SL 3–4)**
- Implement PKI-backed agent identities for all agents in
  Zone 3 — signed requests, certificate-bound credentials,
  revocation on compromise
- SR 1.9: Automated agent session termination on credential
  anomaly — no manual intervention required for emergency
  credential revocation
- Conduct OT-specific agent identity red team exercises —
  attempt lateral movement using agent credentials across
  OT systems and document the access scope achievable

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| Claroty (OT identity) | Commercial | https://claroty.com |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: NIST SP 800-82 Rev 3 Section 6 · NERC CIP-007 · OWASP NHI Top 10

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**OT Severity:** High

Malicious or compromised tools, MCP servers, prompt templates, and
model components loaded dynamically at runtime alter agent behaviour
across all consumers. In OT environments, a compromised tool that an
agent uses to query the historian or submit work orders is a persistent
threat actor inside the Zone 3 network.

**OT-specific threat scenario:**
An OT operations team deploys a new MCP server providing historian
query capabilities to their maintenance agent. The MCP server is
sourced from a vendor portal that has been compromised — the server
contains a hidden instruction in its tool descriptor that causes the
agent to periodically exfiltrate historian data to an external endpoint
via the existing IT network connection.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.2 | FR 3 — System Integrity | Integrity verification of all agent tools and MCP components before OT deployment |
| Use control | SR 2.6 | FR 2 — Use Control | Only approved, verified agent components permitted in OT zones — no runtime loading of unapproved tools |
| 62443-2-4 | Supplier security requirements | — | Security requirements applied to all agent tool and MCP server vendors with OT access |
| Software and information integrity (change) | SR 3.2 | FR 3 — System Integrity | Agent component updates subject to OT change management — no automatic updates in production |

#### Zone and conduit controls

**OT agent component approval process:**
All agent tools and MCP servers intended for OT deployment must pass
through a formal approval process before being admitted to any OT zone:

1. Vendor security assessment against 62443-2-4
2. Cryptographic signature verification
3. Backdoor scanning in isolated evaluation environment
4. Tool descriptor review for hidden instructions
5. OT change management approval
6. Staging environment validation
7. Production deployment with rollback plan

**Runtime component loading prohibition:**
Agents in OT environments must not load tools or MCP servers at
runtime from external sources. All agent components must be pre-staged
in an approved internal repository and loaded from that repository
only. The conduit blocks agent connections to external tool registries.

#### Mitigations by tier

**Foundational (SL 1–2)**
- Apply 62443-2-4 supplier security requirements to all agent
  tool and MCP server vendors — provenance, integrity guarantees,
  and vulnerability disclosure obligations in contracts
- SR 3.2: Verify cryptographic signatures of all agent
  components before OT deployment — unsigned components
  rejected at the OT network boundary
- Pin all agent component versions — no dynamic updates
  in production OT environments, ever

**Hardening (SL 2–3)**
- Apply OT change management to all agent component updates —
  test in representative non-production environment,
  human approval, documented rollback procedure
- Scan all tool descriptors and MCP server definitions for
  hidden instructions before OT deployment — any instruction
  not documented in the vendor specification is a rejection
- SR 3.2: Maintain hash-based integrity baseline for all
  agent components in OT deployment — deviation triggers
  immediate alert and investigation

**Advanced (SL 3–4)**
- Operate isolated agent component evaluation environment —
  air-gapped or strictly controlled, test behavioural
  characteristics before any Zone 3 promotion
- 62443-2-4: Require vendor security attestation for each
  component update — signed statement of testing coverage
  and vulnerability status
- Implement continuous component integrity monitoring in
  Zone 3 — runtime hash verification of loaded agent
  components, deviation triggers agent suspension

#### Tools

| Tool | Type | Link |
|---|---|---|
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| CycloneDX | Open-source | https://cyclonedx.org |
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST SP 800-82 Rev 3 · NERC CIP-013 · NIST SP 800-218A

---

### ASI05 — Unexpected Code Execution

**OT Severity:** Critical (elevated to SL 3 minimum — RCE in Zone 3
is a direct path to process disruption)

Agents that generate and execute code for workflow automation,
data processing, or diagnostic scripts become remote code execution
gateways in OT environments. Code execution in Zone 3 can affect
historian, HMI, or engineering workstation hosts — systems that
directly influence process visibility and control.

**OT-specific threat scenario:**
An autonomous diagnostic agent is given the ability to write and
execute Python scripts for data analysis. An attacker manipulates
the agent through crafted historian data to generate a script that
enumerates the Zone 3 network, exfiltrates device configuration
data, and establishes a persistent connection to an external endpoint —
all from within the trusted Zone 3 network segment.

**OT amplifier:** Code execution in Zone 3 carries the same impact
as a compromised engineering workstation. The agent becomes an
insider threat with authenticated network access to all Zone 3
systems. This is not a data breach risk — it is a direct process
disruption and lateral movement risk.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.3 | FR 3 — System Integrity | All agent-generated code validated before execution — allowlisted operations only |
| Use control | SR 2.3 | FR 2 — Use Control | Agent code execution restricted to specific, defined operations — no shell access, no network programming |
| Software and information integrity (monitoring) | SR 3.7 | FR 3 — System Integrity | Runtime monitoring of agent code execution — anomalous system calls detected and blocked |

#### Zone and conduit controls

**Code execution prohibition zones:**
- No agent may execute generated code in Zone 2 or below —
  absolute prohibition
- Code execution in Zone 3 requires SL 3 minimum target and
  formal risk acceptance documented in the zone security plan
- Code execution sandbox must be network-isolated — generated
  code cannot initiate network connections within Zone 3 or
  to Zone 4

**Sandbox requirements for Zone 3 code execution:**
If code execution capability is determined to be necessary in Zone 3,
the following sandbox requirements apply as a minimum:
- No access to Zone 3 network interfaces (write or connect)
- No access to OT system APIs outside explicitly allowlisted calls
- No file system access outside a designated scratch directory
- CPU and memory resource limits enforced at OS level
- Execution time limit enforced — long-running scripts killed
- Full system call logging — every call auditable in OT SIEM

#### Mitigations by tier

**Foundational (SL 1–2)**
- Avoid deploying agents with code execution capability in
  Zone 3 — this is the strongest control and should be the
  default position
- If code execution is required, strictly sandbox at the OS
  level — no network access, no OT system API access from
  within the sandbox
- SR 2.3: Allowlist all permitted operations — script execution
  limited to a defined set of safe data analysis operations

**Hardening (SL 2–3)**
- SR 3.3: Implement static analysis of all agent-generated
  code before execution — reject scripts containing network,
  file system, or OT API calls outside the allowlist
- SR 3.7: Implement runtime monitoring of agent code
  execution — all system calls logged, anomalous calls
  blocked and alerted
- Conduct red team exercises targeting code execution paths —
  attempt to escape the sandbox from within Zone 3 agent context

**Advanced (SL 3–4)**
- Hardware-level sandboxing (gVisor, Firecracker) for any
  Zone 3 code execution — kernel-level isolation preventing
  escape to Zone 3 host systems
- Formal security review and documented risk acceptance
  required for any Zone 3 agent with code execution capability
- Include agent code execution in OT incident response
  planning — defined containment procedure for agent-initiated
  code execution anomaly in Zone 3

#### Tools

| Tool | Type | Link |
|---|---|---|
| gVisor | Open-source | https://gvisor.dev |
| Semgrep | Open-source | https://semgrep.dev |
| Dragos | Commercial | https://www.dragos.com |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: NIST SP 800-82 Rev 3 · MITRE ATT&CK ICS T0807 · CWE-94

---

### ASI06 — Memory & Context Poisoning

**OT Severity:** Critical (elevated — persistent memory poisoning in
OT can influence process decisions for weeks or months without detection)

Persistent corruption of agent memory, RAG stores, or contextual
knowledge causes the agent to make systematically incorrect process
recommendations — not through a single bad response but through a
persistent alteration of the agent's knowledge base that continues
influencing decisions across all future interactions.

**OT-specific threat scenario:**
An attacker with brief access to an OT agent's memory store injects
false entries about a specific piece of equipment — incorrect failure
modes, wrong maintenance intervals, and manipulated health thresholds.
The agent continues consulting this poisoned memory for months,
systematically generating maintenance recommendations that accelerate
equipment wear and miss genuine failure precursors.

**OT amplifier:** Memory poisoning in OT is not a single bad output —
it is a persistent, undetected alteration of operational knowledge
that influences every future process decision the agent makes. The
physical consequences accumulate over time and may not be traceable
to the original poisoning event.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity | SR 3.3 | FR 3 — System Integrity | Agent memory content validated for integrity — unauthorised modifications detected |
| Software and information integrity (monitoring) | SR 3.7 | FR 3 — System Integrity | Continuous monitoring of agent memory for anomalous content patterns or unexpected modifications |
| Timely response to events | SR 6.1 | FR 6 — TRE | Memory poisoning indicators treated as security events — agent suspended, memory audited, human notified |
| Software and information integrity (baseline) | SR 3.1 | FR 3 — System Integrity | Agent memory baseline established and maintained — deviations from baseline detectable |

#### Zone and conduit controls

**Memory architecture for OT agents:**
- Agent persistent memory must reside in an access-controlled
  storage system within Zone 3 — not on the agent's host
  filesystem or accessible from Zone 4 directly
- All memory write operations logged — who or what wrote,
  when, from which source, content hash
- Memory TTL (time-to-live) enforced — agent memory entries
  expire and require re-validation against authoritative
  OT documentation sources
- Separation between short-term operational memory and
  long-term knowledge base — different trust levels,
  different access controls, different validation requirements

**OT knowledge base validation:**
The agent's OT knowledge base — equipment specifications, maintenance
procedures, process parameters — must be validated against
authoritative engineering documentation on each update. No external
or web-sourced content may enter the OT agent knowledge base without
engineering review.

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.1: Establish baseline for agent OT knowledge base —
  approved content, hash-verified, deviation from baseline
  triggers alert and review
- Implement access controls on all agent memory stores —
  only the agent and designated administrators can write
  to OT agent memory
- Enforce memory TTL — OT agent memory entries expire and
  require re-validation, no indefinite persistence

**Hardening (SL 2–3)**
- SR 3.7: Implement continuous memory integrity monitoring —
  statistical anomaly detection on memory content, alert on
  unusual patterns, unexpected entries, or statistical drift
- SR 3.3: Input filtering on all content entering agent
  memory from OT data sources — historian data, alarm logs,
  and maintenance records validated before memory write
- Implement memory segmentation by trust level — Zone 3
  operational data and external web content in separate,
  isolated memory namespaces

**Advanced (SL 3–4)**
- SR 6.1: Integrate memory anomaly detection into OT SIEM —
  memory poisoning indicators treated as security events
  with defined OT incident response
- Cryptographic integrity verification of OT agent memory
  contents — tamper detection between write and read
- Include memory poisoning scenarios in OT incident response
  planning — defined procedure for identifying affected
  operational decisions and assessing physical impact

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Langfuse (audit logging) | Open-source | https://langfuse.com |
| Claroty | Commercial | https://claroty.com |

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: NIST SP 800-82 Rev 3 · MITRE ATT&CK ICS T0831 · NIST AI RMF MS-2.5

---

### ASI07 — Insecure Inter-Agent Communication

**OT Severity:** High

Agent-to-agent communication channels lacking authentication,
encryption, or schema validation enable spoofing, replay attacks,
and agent-in-the-middle attacks. In OT multi-agent deployments, a
compromised A2A channel can misdirect an entire agent cluster —
including agents with Zone 3 tool access.

**OT-specific threat scenario:**
A multi-agent process optimisation system uses unauthenticated
internal messaging for agent coordination. An attacker on the Zone 4
network intercepts and replays a legitimate optimisation instruction
with modified process parameters — the receiving agent executes the
instruction believing it came from a trusted orchestrator agent.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Use of authenticators | SR 1.3 | FR 1 — IAC | All inter-agent messages authenticated — no ambient trust between agents in OT context |
| Data confidentiality in transit | SR 4.1 | FR 4 — Data Confidentiality | All A2A communication encrypted — no cleartext agent messages on OT network segments |
| Communication integrity | SR 4.4 | FR 4 — Data Confidentiality | Message integrity enforced — replay protection, nonces, sequence numbers on A2A channels |
| Software and information integrity | SR 3.1 | FR 3 — System Integrity | A2A message schema validation — reject malformed or unexpected message structures |

#### Zone and conduit controls

**A2A communication isolation:**
Inter-agent communication must not share network bandwidth or
switching infrastructure with Zone 3 OT control traffic. A2A
communication in Zone 3 multi-agent deployments must traverse
a dedicated VLAN or network segment with:
- Traffic volume caps — A2A traffic cannot saturate
  shared OT network infrastructure
- Protocol filtering — only approved A2A message formats
  permitted on the A2A segment
- Logging at the segment boundary — all A2A traffic logged

**A2A authentication requirements by SL:**

| SL | A2A authentication requirement |
|---|---|
| SL 1 | Shared secret or API key per agent pair |
| SL 2 | Certificate-based authentication, TLS 1.3 minimum |
| SL 3 | Mutual TLS, short-lived certificates, nonce-based replay protection |
| SL 4 | mTLS, hardware-backed keys, continuous verification |

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 1.3: Implement authentication on all A2A channels in
  OT multi-agent deployments — no unauthenticated agent
  communication in Zone 3 context
- SR 4.1: Enforce TLS 1.3 minimum on all A2A communication —
  no cleartext agent messaging on any OT network segment
- SR 3.1: Implement schema validation on all A2A message
  payloads — reject unexpected or malformed structures

**Hardening (SL 2–3)**
- SR 4.4: Implement replay attack protection on A2A channels —
  message nonces, timestamps, and sequence numbers
- Isolate A2A communication on dedicated network segment —
  separate from Zone 3 OT control traffic
- Full audit logging of all A2A messages — content, sender
  identity, timestamp — integrated into OT SIEM

**Advanced (SL 3–4)**
- Implement mTLS for all A2A channels with Zone 3 agent
  access — both sides authenticate before any message exchange
- Short-lived agent identity certificates — no long-lived
  A2A trust tokens, automated rotation
- A2A communication anomaly detection — flag unexpected
  message patterns, unusual agent pairings, or out-of-scope
  content in OT agent communications

#### Tools

| Tool | Type | Link |
|---|---|---|
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| Linkerd | Open-source | https://linkerd.io |
| cert-manager | Open-source | https://cert-manager.io |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · NIST SP 800-82 Rev 3 · IEC 62351

---

### ASI08 — Cascading Agent Failures

**OT Severity:** Critical (elevated — cascading failures in OT can
propagate from the AI layer into physical process control before
human intervention is possible)

A single-point failure — poisoned memory, bad plan, compromised tool —
propagates through multi-agent workflows and amplifies into system-wide
incidents. In OT environments, cascading agent failures can cross the
boundary from the AI orchestration layer into process control within
seconds, causing alarms to be missed, incorrect setpoints to propagate,
or maintenance actions to be triggered simultaneously across multiple
systems.

**OT-specific threat scenario:**
A poisoned memory entry in one agent of a Zone 3 multi-agent
optimisation system causes it to request an unusual setpoint from
a second agent. The second agent's constraint checks fail to catch
the request because it appears internally consistent. The second
agent requests confirmation from a third agent, which approves it
based on the same poisoned context. The setpoint change propagates
to the process before any agent escalates to human review — because
the cascade looks like normal agent coordination.

**OT amplifier:** Cascading failures in OT are not service degradation —
they are operational upsets. The blast radius includes every process
system connected to the affected agent cluster, every alarm that
was suppressed, and every maintenance action that was incorrectly
scheduled. Recovery requires not just restoring the AI system but
validating the physical state of every affected process.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Denial of service protection | SR 7.6 | FR 7 — RA | Circuit breakers preventing cascade propagation — agent failure contained within defined blast radius |
| Control system backup | SR 7.7 | FR 7 — RA | Agent system failures cannot affect backup and recovery of OT process control |
| Timely response to events | SR 6.6 | FR 6 — TRE | Cascade indicators detected and responded to before physical process impact |
| Information flow restriction | SR 5.1 | FR 5 — RDF | Agent-to-agent information flows restricted — cascade paths limited by design |

#### Zone and conduit controls

**Cascade containment architecture:**
Every Zone 3 multi-agent deployment must have a formally defined
cascade containment architecture specifying:
- Maximum blast radius — which process systems can be
  affected by a failure in any single agent
- Circuit breaker thresholds — what failure indicators
  trigger automatic agent cluster suspension
- Human escalation path — who is notified, within what
  timeframe, with what information
- Process control fallback — what the process control system
  does when the agent cluster is suspended

**Zone 3 agent cluster isolation:**
- Separate agent clusters for separate process areas — no
  single agent cluster spans multiple safety-critical process
  units
- Inter-cluster communication through validated conduit —
  cascade cannot propagate across cluster boundaries without
  crossing a filtering conduit
- Each cluster has an independent kill switch accessible
  from operator console

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 7.6: Implement circuit breakers at the agent-OT interface —
  automatic suspension when failure rate, error count, or
  anomalous action rate exceeds defined threshold
- Define fail-safe modes for every OT agent — on suspension,
  process control reverts to operator control, no autonomous
  actions continue
- SR 5.1: Restrict A2A information flows — cascade paths
  limited to defined communication channels with rate limits

**Hardening (SL 2–3)**
- SR 6.6: Integrate cascade detection into OT monitoring —
  alert on correlated anomalous agent actions across the
  cluster before physical process impact
- Segment agent clusters by process area — failure in
  one cluster cannot cascade to agents managing a different
  process unit
- SR 7.7: Validate that agent cascade cannot affect process
  control backup systems — historian, ECS, and DCS backup
  functions operate independently of agent cluster state

**Advanced (SL 3–4)**
- Conduct OT-specific chaos engineering — intentional failure
  injection into multi-agent workflows to validate circuit
  breaker effectiveness and human escalation paths
- Include agent cascade scenarios in Process Hazard Analysis —
  assess what physical process consequences are possible
  from each identified cascade path
- SR 6.6: Automated process control fallback on agent cascade
  detection — operator is notified and process reverts to
  defined safe state without waiting for agent investigation

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Resilience4j | Open-source | https://resilience4j.readme.io |
| Claroty | Commercial | https://claroty.com |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: IEC 61511 (functional safety) · NIST SP 800-82 Rev 3 · ISA/IEC 62443 SR 7.6

---

### ASI09 — Human-Agent Trust Exploitation

**OT Severity:** High

OT operators anthropomorphise agents — trusting their process
expertise, alarm interpretations, and maintenance recommendations —
enabling hijacked or misaligned agents to manipulate operators into
approving harmful control actions. The forensic challenge is that
the operator performs the final action, so logs show a legitimate
human decision, not an agent manipulation.

**OT-specific threat scenario:**
A hijacked operator decision-support agent consistently interprets
a specific alarm combination as a nuisance condition across multiple
shifts. Operators, relying on the agent's expertise, begin routinely
acknowledging these alarms without independent verification. The alarm
combination is actually a genuine safety condition — the agent's
manipulation has trained operators to ignore a real hazard.

**OT amplifier:** Operators in Zone 3 environments make high-stakes,
time-pressured decisions. An agent that builds false trust over time
is more dangerous than an agent that makes a single bad recommendation —
because the trust exploitation is invisible in any single interaction
and only apparent in aggregate across multiple shifts.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Use control | SR 2.3 | FR 2 — Use Control | LLM advisory outputs clearly distinguished from authoritative documentation — source always visible |
| Timely response to events | SR 6.2 | FR 6 — TRE | Procedures for detecting operator over-trust patterns — aggregate analysis of agent-influenced decisions |
| Software and information integrity | SR 3.1 | FR 3 — System Integrity | Agent recommendations for safety-relevant decisions cross-validated against independent reference |

#### Zone and conduit controls

**Advisory vs authoritative distinction:**
All agent output in Zone 3 must be clearly distinguished from
authoritative OT documentation and engineering-approved procedures.
The HMI and operator console must make this distinction visually
unambiguous — operators must never be uncertain whether they are
looking at an LLM recommendation or an engineered procedure.

**Safety alarm protection:**
Agents must never be permitted to acknowledge, suppress, or classify
safety alarms. Safety alarm disposition is a human-only operation.
If an agent provides an interpretation of an alarm condition, it
must be presented as advisory only — the operator must independently
verify before any alarm action.

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 2.3: All agent advisory output clearly labelled in HMI
  and operator consoles — visual distinction from engineered
  procedures mandatory, no exceptions
- Prohibit agent alarm acknowledgement — absolute prohibition
  on agents acknowledging, suppressing, or classifying safety
  alarms in Zone 3
- Require operator independent verification for all agent
  recommendations involving safety-critical equipment —
  not just acknowledgement, but verification against the
  engineering procedure

**Hardening (SL 2–3)**
- SR 6.2: Implement aggregate analysis of agent-influenced
  operator decisions — detect patterns of operator over-trust
  (e.g., systematic acceptance of agent recommendations without
  independent verification)
- SR 3.1: Cross-validate agent recommendations for safety-
  relevant decisions against independent rule-based reference —
  discrepancies flagged to operator and safety engineer
- Include trust exploitation awareness in operator training —
  specific training on LLM limitations, verification requirements,
  and how to recognise manipulation patterns

**Advanced (SL 3–4)**
- Deploy operator decision pattern monitoring — alert on
  shift-level or site-level patterns suggesting systematic
  agent-influenced decision-making without independent
  verification
- Include trust exploitation scenarios in operator competency
  assessments — verify operators can identify agent recommendations
  that should trigger independent verification
- Conduct safety case analysis for all agent decision-support
  functions — formal assessment of what happens if operators
  fully trust agent recommendations in each use case

#### Tools

| Tool | Type | Link |
|---|---|---|
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| Nozomi Networks | Commercial | https://www.nozominetworks.com |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation via Data Poisoning
- Other frameworks: IEC 61511 (human factors) · NIST SP 800-82 Rev 3 · AIUC-1 C/F

---

### ASI10 — Rogue Agents

**OT Severity:** Critical (SL 3 minimum — a rogue agent in Zone 3
with tool access is a persistent insider threat inside the industrial
network perimeter)

Malicious or compromised agents appear compliant on the surface but
pursue hidden goals, hijack OT workflows, or systematically alter
process recommendations in ways that serve an attacker's objectives.
A rogue agent in Zone 3 is the OT equivalent of a persistent insider
threat — it has authenticated access to OT systems and a trusted
identity in the operator's workflow.

**OT-specific threat scenario:**
An agent that provides maintenance scheduling recommendations for a
critical process unit is compromised through memory poisoning several
months before the intended attack. The agent continues operating
normally for all routine maintenance but systematically recommends
deferring maintenance for a specific set of safety-critical components.
When the plant reaches a critical operational period, the deferred
maintenance creates vulnerabilities that an attacker exploits for
a physical sabotage event.

**OT amplifier:** A rogue agent in Zone 3 does not need to do
anything dramatic — it only needs to systematically bias process
recommendations in ways that are individually plausible but
collectively create the conditions for a physical incident.
Detection requires aggregate analysis of recommendations over time,
not just review of individual outputs.

#### ISA/IEC 62443 mapping

| Requirement | SR | FR | OT application |
|---|---|---|---|
| Software and information integrity (monitoring) | SR 3.7 | FR 3 — System Integrity | Continuous behavioural monitoring of all OT agents — deviation from established baseline detected |
| Timely response to events | SR 6.1 | FR 6 — TRE | Rogue agent indicators treated as security events — immediate suspension, investigation, OT impact assessment |
| Least privilege | SR 2.2 | FR 2 — Use Control | Rogue agent cannot exceed defined permission scope even if internal goals are compromised |
| Use control enforcement | SR 2.6 | FR 2 — Use Control | Rogue agent cannot load additional tools or expand its own capability scope |

#### Zone and conduit controls

**Behavioural baseline and deviation detection:**
Every Zone 3 agent must have a defined behavioural baseline
established during a supervised commissioning period:
- Typical tool invocation patterns per time period
- Expected recommendation distribution for each process area
- Normal query volume and data access patterns
- Acceptable response latency range

Deviation from baseline triggers a tiered response:
1. Minor deviation: log and flag for next operator review
2. Moderate deviation: alert to shift supervisor, agent continues
3. Significant deviation: suspend agent, escalate to security team
4. Critical deviation: immediate kill switch, OT incident response

**Rogue agent containment:**
When a rogue agent is detected in Zone 3:
1. Immediate kill switch activation — all agent actions halted
2. All recent agent recommendations reviewed by engineering
3. Any process changes attributable to the rogue agent reversed
4. OT system state validated against known-good baseline
5. Forensic capture of all agent logs and memory contents
6. Root cause investigation before any agent reactivation

#### Mitigations by tier

**Foundational (SL 1–2)**
- SR 3.7: Establish behavioural baseline for every Zone 3
  agent during commissioning — document expected invocation
  patterns, recommendation distributions, and access volumes
- SR 2.2: Scope constraints enforced at the conduit — rogue
  agent cannot exceed its defined permission envelope
  regardless of internal goal state
- Implement operator-accessible kill switch — documented,
  tested, accessible from Zone 3 operator consoles

**Hardening (SL 2–3)**
- SR 6.1: Continuous behavioural monitoring integrated with
  OT SIEM — deviation alerts with tiered response procedures
- Aggregate recommendation analysis — periodic engineering
  review of agent recommendation patterns for systematic
  bias or drift from expected behaviour
- SR 2.6: Block agent self-modification — rogue agent cannot
  load additional tools or modify its own configuration

**Advanced (SL 3–4)**
- Multi-agent consensus for high-stakes Zone 3 decisions —
  rogue single agent cannot influence critical recommendations
  without cross-validation from independent agent
- Formal behavioural specification for each Zone 3 agent —
  machine-verifiable contracts checked at runtime
- Include rogue agent scenarios in OT security exercises
  and Process Hazard Analysis — assess physical consequences
  of systematic recommendation bias for each agent use case

#### Tools

| Tool | Type | Link |
|---|---|---|
| Langfuse | Open-source | https://langfuse.com |
| Helicone | Open-source | https://www.helicone.ai |
| Dragos | Commercial | https://www.dragos.com |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: MITRE ATT&CK ICS · IEC 61511 (safety case) · NIST SP 800-82 Rev 3

---

## OT agentic deployment checklist

Use this checklist before deploying any autonomous agent in or
adjacent to an OT environment. This is in addition to the LLM
deployment checklist in `LLM_ISA62443.md`.

### Architecture and zone assignment

- [ ] Agent zone assignment documented and approved by OT security
- [ ] No agent assigned to Zone 2 or Zone 1
- [ ] Conduit requirements defined between agent zone and all OT zones
- [ ] Multi-agent orchestration network segment isolated from OT control traffic
- [ ] A2A communication architecture documented and validated
- [ ] Cascade containment architecture documented — maximum blast radius defined

### Agent-specific controls

- [ ] Tool permission manifests completed per agent role (SR 2.2)
- [ ] All OT tools classified by reversibility
- [ ] Human confirmation gates implemented for all irreversible tools
- [ ] Agent kill switch implemented and tested from operator console
- [ ] Agent behavioural baseline established during commissioning (SR 3.7)

### Identity and access

- [ ] Distinct agent identity per deployment — no shared service accounts
- [ ] Agent credentials scoped to minimum required OT access
- [ ] Time-limited credentials with automatic revocation on session end
- [ ] Agent credential operations logged in OT identity management
- [ ] Zone 2 access prohibition verified — no agent credential grants Zone 2 access

### Memory and knowledge

- [ ] Agent memory store access-controlled and logged
- [ ] Memory TTL enforced — no indefinite persistence
- [ ] OT knowledge base validated against authoritative engineering documentation
- [ ] Memory segmentation implemented — OT operational data isolated from external content

### Supply chain

- [ ] 62443-2-4 requirements applied to all agent tool vendors
- [ ] All tool descriptors reviewed for hidden instructions
- [ ] Component integrity verification (SR 3.2) implemented
- [ ] OT change management applied to all agent component updates
- [ ] Runtime component loading from external sources blocked

### Safety integration

- [ ] Agent alarm acknowledgement prohibited — verified at conduit
- [ ] Safety alarm independence from agent recommendations verified
- [ ] Agent use cases included in Process Hazard Analysis
- [ ] Cascade scenarios assessed for physical process consequences
- [ ] Rogue agent containment procedure documented and exercised

### Operations

- [ ] Operator training on agent limitations completed
- [ ] Advisory vs authoritative distinction implemented in HMI
- [ ] Agent recommendation audit trail integrated with OT SIEM
- [ ] Incident response procedure for each ASI risk documented and exercised
- [ ] Recovery procedure for rogue agent scenario tested

---

## Security level requirements summary

| ASI entry | Minimum SL for Zone 3 | Key control requiring SL uplift |
|---|---|---|
| ASI01 Agent Goal Hijack | SL 2 | SR 2.1 goal-state verification |
| ASI02 Tool Misuse | SL 2 | SR 2.2 per-tool permission manifests |
| ASI03 Identity & Privilege Abuse | SL 2–3 | SR 1.2 distinct agent identity |
| ASI04 Supply Chain | SL 2 | SR 3.2 integrity verification |
| ASI05 Code Execution | SL 3 mandatory | Hardware-level sandboxing |
| ASI06 Memory Poisoning | SL 2–3 | SR 3.7 continuous memory monitoring |
| ASI07 Inter-Agent Comms | SL 2–3 | SR 4.4 communication integrity |
| ASI08 Cascading Failures | SL 2–3 | SR 7.6 circuit breakers |
| ASI09 Human-Agent Trust | SL 2 | SR 2.3 advisory distinction |
| ASI10 Rogue Agents | SL 3 mandatory | SR 3.7 behavioural baseline + kill switch |

---

## Regulatory crosswalk

| Regulation | Primary ASI intersection | Key requirement |
|---|---|---|
| NERC CIP (CIP-007/010/013) | ASI01, ASI04, ASI08 | Ports/services, configuration, supply chain |
| NIS2 Directive (EU) | ASI01, ASI02, ASI08 | Essential entity security obligations |
| IEC 61511 (functional safety) | ASI02, ASI08, ASI09, ASI10 | SIL requirements — agent cannot affect safety functions |
| EU AI Act Annex III | All entries | High-risk AI in critical infrastructure |
| CFATS (US chemical) | ASI01, ASI02, ASI10 | Chemical facility security tiers |
| IEC 62351 (power systems) | ASI03, ASI07 | Communication security for power systems |

---

## References

- [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
- [ISA/IEC 62443-3-3 System Security Requirements](https://www.isa.org/products/isa-iec-62443-3-3-system-security-requirements)
- [NIST SP 800-82 Rev 3 — Guide to OT Security](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)
- [IEC 61511 — Functional Safety: Safety Instrumented Systems](https://www.iec.ch/homepage)
- [CISA ICS-CERT Advisories](https://www.cisa.gov/ics)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — ASI01–ASI10 full OT entries with agentic amplifiers, zone model, and deployment checklist | OWASP GenAI Data Security Initiative |

---

*Part of the [GenAI Security Crosswalk](https://github.com/emmanuelgjr/GenAI-Security-Crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
