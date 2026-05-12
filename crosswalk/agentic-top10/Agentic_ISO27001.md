<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : ISO/IEC 27001:2022 — Information Security Management Systems
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × ISO/IEC 27001:2022

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html) —
the world's most widely deployed information security management
system standard.

---

## Why ISO 27001 for agentic AI

ISO 27001 is the baseline certification for enterprise security
programmes globally. Agentic AI deployments introduce new ISMS
scope questions that must be resolved before controls can be
selected:

**Scope extension:** Every autonomous agent that stores, processes,
or transmits information is an information asset within the ISMS
scope. Agent memory stores, credential vaults, A2A communication
channels, and tool integration APIs all require Annex A controls.

**New 2022 controls:** The 11 new Annex A controls introduced in
ISO 27001:2022 map directly to agentic risks — A.5.23 (cloud
services security), A.8.11 (data masking), A.8.12 (DLP), A.8.16
(monitoring activities), and A.8.23 (web filtering) all have
direct agentic application.

**NHI as privileged access:** Under ISO 27001, every agent service
account, API key, and OAuth token is a privileged access credential
subject to A.8.2 (privileged access rights) — the same controls
that govern human privileged access apply to agent NHIs.

**Supply chain:** ISO 27001 A.5.19–A.5.22 (supplier relationships)
applies to all agent tool providers, MCP server vendors, and model
component suppliers. Agents that load tools at runtime create new
supplier relationships that the ISMS must track.

---

## ISO 27001:2022 Annex A domains

| Domain | Controls | Agentic relevance |
|---|---|---|
| A.5 Organisational | A.5.1–A.5.37 | Policy, roles, supplier security, threat intel, incident management |
| A.6 People | A.6.1–A.6.8 | Screening, training, remote working |
| A.7 Physical | A.7.1–A.7.14 | Physical access to agent infrastructure |
| A.8 Technological | A.8.1–A.8.34 | Access, cryptography, logging, secure development, DLP, monitoring |

**New 2022 controls most relevant to agentic AI:**
A.5.7 Threat intelligence · A.5.23 Cloud services security ·
A.8.11 Data masking · A.8.12 Data leakage prevention ·
A.8.16 Monitoring activities · A.8.28 Secure coding

---

## Quick-reference summary

| ID | Name | Severity | Primary ISO 27001:2022 Controls | Tier |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | A.8.28, A.8.29, A.8.16, A.5.7 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | A.8.2, A.5.15, A.8.15, A.8.28 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | A.8.2, A.5.16, A.8.24, A.8.15 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | A.5.19, A.5.20, A.5.21, A.8.8 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | A.8.28, A.8.26, A.8.29, A.8.16 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | A.8.3, A.8.24, A.8.16, A.8.12 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | A.8.20, A.8.24, A.8.15, A.5.14 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | A.8.16, A.5.30, A.5.24, A.8.13 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | A.6.3, A.5.36, A.8.16, A.5.12 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | A.8.16, A.8.15, A.8.2, A.5.24 | Hardening–Advanced |

---

## Audience tags

- **CISO / governance** — full file, ISO 27001 ISMS extension for agentic AI
- **Auditor / certifier** — control mapping evidence for certification audits
- **Security engineer** — A.8 technological controls per vulnerability
- **IAM team** — A.8.2, A.5.15, A.5.16 privileged access and NHI entries
- **Compliance officer** — A.5 organisational controls, supplier management
- **OT engineer** — ASI01, ASI02, ASI08 with ISA 62443 crosswalk

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects agent objectives through direct or indirect
instruction injection. ISO 27001 addresses this through secure coding
(A.8.28), security testing (A.8.29), monitoring (A.8.16), and
threat intelligence (A.5.7).

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Secure coding | A.8.28 | Technological | Secure coding requirements for all agentic integration code — input validation, goal-state verification, context separation |
| Security testing | A.8.29 | Technological | Adversarial testing programme covering goal hijack — direct, indirect, multi-turn injection before each release |
| Monitoring activities | A.8.16 | Technological | Runtime monitoring for injection indicators across all agent input channels — new 2022 control |
| Threat intelligence | A.5.7 | Organisational | Active intelligence on prompt injection and goal hijack techniques — new attack methods inform detection controls |

#### Mitigations by tier

**Foundational**
- A.8.28: Implement goal-state verification and input
  validation as secure coding requirements — all agentic
  integration code reviewed for injection resistance
- A.5.7: Subscribe to threat intelligence covering prompt
  injection and goal hijack techniques — new attack
  methods update detection rules and test cases
- Treat all external content as untrusted — ISMS policy
  control applied to all agent data sources

**Hardening**
- A.8.29: Include goal hijack scenarios in security
  testing programme — all indirect injection surfaces
  tested before each production release
- A.8.16: Deploy runtime injection monitoring on all
  agent input channels — alerts integrated into ISMS
  incident management workflow
- Kill switch implementation as A.8.28 secure design
  requirement — tested as A.8.29 security testing activity

**Advanced**
- A.8.29: Red team with novel indirect injection
  techniques quarterly — results documented as ISMS
  security testing evidence
- A.5.7: Threat intelligence drives test case updates —
  new injection techniques tested before reaching
  production at any scale

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| Rebuff | Open-source | https://github.com/protectai/rebuff |
| Invariant Analyzer | Open-source | https://github.com/invariantlabs-ai/invariant |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways, DSGAI15 Over-Broad Context Windows
- Other frameworks: AIUC-1 B001/B005 · NIST AI RMF GV-1.7 · EU AI Act Art. 14/15

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents misuse legitimate tools via prompt manipulation or unsafe
delegation. ISO 27001 A.8.2 (privileged access rights) governs tool
permissions as privileged access — the same controls that prevent
humans from misusing privileged access apply to agent tool scope.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Privileged access rights | A.8.2 | Technological | Agent tool access managed as privileged access — per-tool permission manifests, minimum scope, regular review |
| Identity management | A.5.15 | Organisational | Agent tool access governed through identity management — tool permissions scoped per agent identity |
| Logging | A.8.15 | Technological | All tool invocations logged with full context — tool identity, parameters, agent identity, timestamp |
| Secure coding | A.8.28 | Technological | Tool parameter validation as secure coding requirement — LLM-generated parameters treated as untrusted |

#### Mitigations by tier

**Foundational**
- A.8.2: Manage agent tool access as privileged access —
  per-tool permission manifests enforced, minimum scope,
  reviewed on change and quarterly
- A.5.15: Govern tool permissions through identity
  management — each agent identity has a defined tool
  scope, scope changes require formal approval
- Human confirmation gates for irreversible tools —
  ISMS policy control documented under A.5.15

**Hardening**
- A.8.15: Log all tool invocations — tool identity,
  parameters, agent identity, user session, timestamp —
  immutable audit trail for forensic investigation
- A.8.28: Implement tool parameter validation as secure
  coding requirement — all LLM-generated parameters
  validated before tool execution
- A.8.29: Include tool misuse in security testing —
  destructive parameters, tool chain exploitation,
  MCP descriptor poisoning tested before each release

**Advanced**
- A.8.2: Include agent tool access in privileged access
  reviews — quarterly, any permission not actively used
  is removed, documented as ISMS evidence
- A.8.29: Red team tool chain exploitation — attempt
  destructive outcomes through legitimate tool sequence,
  results documented in ISMS

#### Tools

| Tool | Type | Link |
|---|---|---|
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |
| MCP Inspector | Open-source | https://github.com/modelcontextprotocol/inspector |
| Invariant Analyzer | Open-source | https://github.com/invariantlabs-ai/invariant |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: AIUC-1 B006/B007 · OWASP NHI Top 10 NHI-5 · ISA/IEC 62443 SR 2.2 (OT)

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit and cache credentials that attackers exploit for
lateral movement. ISO 27001 A.8.2 (privileged access) and A.5.16
(identity management) govern the full NHI lifecycle — the same
controls that govern human privileged access apply to agent identities.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Privileged access rights | A.8.2 | Technological | Agent credentials managed as privileged access — JIT issuance, minimum scope, regular review, automatic expiry |
| Identity management | A.5.16 | Organisational | NHI lifecycle management — all agent identities inventoried, provisioned, reviewed, and deprovisioned through formal process |
| Use of cryptography | A.8.24 | Technological | Agent credentials encrypted at rest and in transit — secret manager, no cleartext storage |
| Logging | A.8.15 | Technological | All credential operations logged — issuance, use, expiry, anomalous patterns detectable |

#### Mitigations by tier

**Foundational**
- A.8.2: Manage agent credentials as privileged access —
  JIT issuance, short TTL, automatic expiry, minimum
  scope enforced, no shared credentials across agents
- A.5.16: Establish NHI identity management process —
  all agent identities inventoried, formal provisioning
  and deprovisioning documented as ISMS evidence
- A.8.24: Encrypt all agent credentials at rest —
  secret manager required, no cleartext in config,
  code, or agent memory

**Hardening**
- A.8.15: Log all agent credential operations —
  issuance, use, expiry, revocation — full ISMS audit
  trail enabling forensic investigation
- A.8.16: Monitor credential usage for anomalies —
  unusual access scope, lateral movement, credential
  use outside expected patterns alerted
- Implement credential anomaly detection — automated
  response to anomalous NHI usage

**Advanced**
- PKI-backed agent identities as A.8.24 advanced
  cryptographic control — certificate-based
  authentication for all agent-to-system connections
- A.8.2: Quarterly privileged access review includes
  all agent NHIs — documented in ISMS as evidence
- A.5.16: Formal agent offboarding procedure —
  deprovisioning checklist covering credential
  revocation as ISMS documented information

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| Teleport | Open-source/Commercial | https://goteleport.com |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 (all entries) · AIUC-1 A/B007 · EU AI Act Art. 15

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High

Compromised tools, MCP servers, or model components alter agent
behaviour. ISO 27001 A.5.19–A.5.22 (supplier relationships) governs
all agent component providers as information security suppliers.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Supplier relationships | A.5.19 | Organisational | Security requirements applied to all agent tool and MCP server providers — provenance, integrity, disclosure obligations |
| Supplier agreements | A.5.20 | Organisational | Contractual security requirements for all agent component suppliers — integrity guarantees, vulnerability notification SLA |
| Supply chain security | A.5.21 | Organisational | Managing ICT supply chain risks — agent tool and MCP server ecosystem explicitly in scope |
| Management of technical vulnerabilities | A.8.8 | Technological | Agent component CVEs in vulnerability management — ML libraries, inference runtime, MCP server dependencies |

#### Mitigations by tier

**Foundational**
- A.5.19: Apply supplier security requirements to all
  agent component vendors — source documentation,
  integrity guarantees, vulnerability disclosure
  obligations before any component enters production
- A.8.8: Maintain ML SBOM for all agentic deployments —
  every component (tools, MCP servers, model weights,
  libraries) scanned against known CVEs
- Pin all component versions — no automatic updates
  without review through ISMS change management

**Hardening**
- A.5.20: Include security requirements in all agent
  component vendor contracts — integrity attestation,
  backdoor scanning coverage, incident notification SLA
- A.5.21: Develop supply chain security plan for agent
  components — procurement, testing, deployment, update,
  decommission lifecycle documented as ISMS evidence
- Verify cryptographic signatures before loading any
  agent component — unsigned components rejected

**Advanced**
- A.5.19: Periodic security assessments of strategic
  agent component suppliers — include in ISMS supplier
  management programme with defined cadence
- Operate isolated evaluation environment for component
  testing — behavioural testing before each production
  promotion as ISMS security testing control

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Syft | Open-source | https://github.com/anchore/syft |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: NIST CSF 2.0 GV.SC-01 · NIST SP 800-218A · ISA/IEC 62443 62443-2-4 (OT)

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents that generate and execute code become RCE gateways. ISO 27001
A.8.28 (secure coding) and A.8.26 (application security requirements)
govern code execution security as a development and operational control.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Secure coding | A.8.28 | Technological | Sandbox, static analysis, and allowlist as secure coding requirements — no code execution without these controls |
| Application security requirements | A.8.26 | Technological | Security requirements for agent code execution capability specified before development — sandbox spec, permitted operations |
| Security testing | A.8.29 | Technological | Sandbox escape and code injection scenarios in security testing — adversarial testing before each deployment |
| Monitoring activities | A.8.16 | Technological | Code execution environments monitored — anomalous system calls, network attempts detected |

#### Mitigations by tier

**Foundational**
- A.8.26: Define security requirements for code execution
  capability before any development — sandbox spec,
  network isolation, allowlist documented as ISMS
  application security requirements
- A.8.28: Implement sandbox, static analysis, and
  allowlist as secure coding requirements — no agent
  code execution without these controls enforced
  through code review and CI/CD

**Hardening**
- A.8.29: Include sandbox escape and code injection
  scenarios in security testing — adversarial testing
  before each agentic code execution deployment,
  results as ISMS security testing evidence
- A.8.16: Monitor code execution environments —
  anomalous system calls, network attempts, file access
  outside scratch directory detected and alerted

**Advanced**
- Hardware-level sandboxing as A.8.28 advanced secure
  coding control — documented as ISMS evidence for
  highest-risk code execution deployments
- A.8.29: Red team sandbox escape quarterly — attempt
  escape from within the specific runtime, document
  results in ISMS

#### Tools

| Tool | Type | Link |
|---|---|---|
| gVisor | Open-source | https://gvisor.dev |
| Semgrep | Open-source | https://semgrep.dev |
| Bandit | Open-source | https://github.com/PyCQA/bandit |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006 · CWE-94 · EU AI Act Art. 15

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Persistent memory poisoning causes systematic incorrect behaviour.
ISO 27001 A.8.3 (information access restriction) and A.8.24
(cryptography) govern memory store security as information assets
subject to ISMS access and protection controls.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Information access restriction | A.8.3 | Technological | Access controls on all agent memory stores — only agent and designated administrators can write |
| Use of cryptography | A.8.24 | Technological | Agent memory stores encrypted at rest — embeddings, long-term memory, operational knowledge base |
| Monitoring activities | A.8.16 | Technological | Memory store access and content monitored — anomalous write patterns, statistical integrity checks |
| Data leakage prevention | A.8.12 | Technological | DLP on memory write paths — credential patterns, sensitive content detected before memory write |

#### Mitigations by tier

**Foundational**
- A.8.3: Implement access controls on all agent memory
  stores — only agent and designated administrators
  can write, access logged as ISMS evidence
- A.8.24: Encrypt all agent memory stores at rest —
  same cryptographic standards as production data
- Memory TTL enforcement — entries expire requiring
  re-validation, documented as ISMS information
  asset control

**Hardening**
- A.8.16: Monitor memory stores for anomalous content
  and access patterns — statistical integrity checks,
  unusual write volumes alerted through ISMS monitoring
- A.8.12: Apply DLP to memory write paths — credential
  patterns and sensitive content detected before
  memory write, ISMS DLP programme extended to agents

**Advanced**
- Cryptographic memory integrity verification —
  tamper detection between write and read as A.8.24
  advanced cryptographic control
- A.8.29: Memory poisoning in security testing —
  injection paths via each content source tested,
  results as ISMS security testing evidence

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Langfuse | Open-source | https://langfuse.com |

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: AIUC-1 A/B002 · NIST AI RMF MS-2.5 · ISA/IEC 62443 SR 3.7 (OT)

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High

A2A channels lacking authentication enable agent-in-the-middle attacks.
ISO 27001 A.8.20 (networks security) and A.8.24 (cryptography) govern
A2A communication as network traffic subject to ISMS network and
cryptographic controls.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Networks security | A.8.20 | Technological | A2A communication channels network-isolated — dedicated VLAN, traffic volume caps, protocol filtering |
| Use of cryptography | A.8.24 | Technological | A2A messages encrypted and integrity-verified — mutual TLS, nonce-based replay protection |
| Logging | A.8.15 | Technological | All A2A messages logged — sender identity, content hash, timestamp, schema validation results |
| Transfer of information | A.5.14 | Organisational | Information transfer policies and agreements for A2A communication — authentication requirements, acceptable content |

#### Mitigations by tier

**Foundational**
- A.8.24: Enforce mutual TLS on all A2A channels —
  both parties authenticate, messages encrypted,
  replay protection enforced as ISMS cryptographic control
- A.8.20: Network-isolate A2A communication — dedicated
  VLAN or segment, traffic volume capped, protocol
  filtered as ISMS network security control

**Hardening**
- A.8.15: Log all A2A messages — sender identity, content
  hash, timestamp — immutable ISMS audit trail
- A.5.14: Define A2A information transfer policy —
  authentication requirements, acceptable content,
  schema validation documented as ISMS policy

**Advanced**
- PKI-backed agent identities for A2A — short-lived
  certificates, hardware-backed keys for highest-risk
  agent clusters as A.8.24 advanced cryptographic control
- A.8.29: A2A security in security testing — spoofing,
  replay, schema violations tested before deployment

#### Tools

| Tool | Type | Link |
|---|---|---|
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| Linkerd | Open-source | https://linkerd.io |
| cert-manager | Open-source | https://cert-manager.io |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 NHI-4/NHI-7 · AIUC-1 B007/B008 · ISA/IEC 62443 SR 3.1 (OT)

---

### ASI08 — Cascading Agent Failures

**Severity:** High

Single-point faults propagate through multi-agent workflows. ISO 27001
A.5.30 (ICT readiness for business continuity) and A.5.24 (incident
management) govern cascade resilience as BCP and incident management
obligations. In OT environments this is Critical severity.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Monitoring activities | A.8.16 | Technological | Cascade indicators monitored — correlated failure patterns across agent cluster detected before physical impact |
| ICT readiness for business continuity | A.5.30 | Organisational | Agent cluster failures covered in BCP — RTO/RPO defined, failover tested, circuit breakers as resilience controls |
| Information security incident management | A.5.24 | Organisational | Cascade events treated as security incidents — defined response, kill switch activation, operations notification |
| Backup | A.8.13 | Technological | Agent state and configuration backed up — recovery to known-good state after cascade incident |

#### Mitigations by tier

**Foundational**
- A.5.30: Include agent cluster failures in BCP —
  RTO/RPO defined, circuit breakers as resilience
  controls, operator kill switch documented and tested
- A.5.24: Define cascade incident response — kill switch
  activation, process control fallback, operations
  notification as ISMS incident management procedure
- Fail-safe defaults — on suspension, all autonomous
  actions halt and process control reverts to manual

**Hardening**
- A.8.16: Monitor for cascade indicators — correlated
  anomalous agent actions detected through ISMS
  monitoring programme before physical impact
- Agent cluster segmentation — blast radius limited
  by architecture as ISMS network security control
- A.8.13: Backup agent state and configuration —
  recovery to known-good state after cascade

**Advanced**
- Conduct chaos engineering as A.8.29 security testing
  activity — intentional failure injection, circuit
  breaker effectiveness verified, results in ISMS
- A.5.30: Annual failover drills covering agent cluster
  cascade scenarios — BCP testing evidence in ISMS

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Resilience4j | Open-source | https://resilience4j.readme.io |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.6/7.7 (OT) · NIST SP 800-82 Rev 3

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Agents build false trust enabling manipulation of human approvers.
ISO 27001 A.6.3 (information security awareness training) and
A.5.36 (compliance with policies) address trust exploitation as
a people and policy risk, not only a technical risk.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Information security awareness, education and training | A.6.3 | People | All users of agentic decision-support tools trained on AI limitations — verification requirements, how to identify manipulation |
| Compliance with policies | A.5.36 | Organisational | Policy on agentic AI advisory use — domains requiring verification, approval flow independence from agent interface |
| Monitoring activities | A.8.16 | Technological | Aggregate over-trust patterns monitored — systematic operator acceptance without verification detected |
| Classification of information | A.5.12 | Organisational | Agent advisory output classified — users cannot mistake model recommendations for authoritative system content |

#### Mitigations by tier

**Foundational**
- A.6.3: Provide security awareness training to all
  users of agentic decision-support tools — cover AI
  limitations, verification requirements, how to identify
  AI output vs authoritative content, mandatory before
  access granted
- A.5.36: Establish policy on agentic AI advisory use —
  which domains require human verification, approval
  flows must be independent of agent chat interface
- A.5.12: Classify agent advisory output — visual
  distinction from authoritative system content in all
  interface contexts as ISMS policy requirement

**Hardening**
- A.8.16: Monitor for aggregate over-trust patterns —
  systematic operator acceptance without verification
  detected as ISMS monitoring control
- Safety alarm independence — agents cannot acknowledge
  or suppress safety alarms as ISMS policy control (OT)
- A.5.36: Approval flows independent of agent interface —
  no sensitive action approval via agent chat, ISMS
  procedural control

**Advanced**
- A.6.3: Include trust exploitation scenarios in operator
  competency assessments — verify operators can identify
  manipulated agent recommendations, results in ISMS
- A.8.29: Red team trust exploitation — test operator
  susceptibility to manipulated agent recommendations
  in your specific deployment

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · AIUC-1 C/F · ISA/IEC 62443 SR 2.3 (OT)

---

### ASI10 — Rogue Agents

**Severity:** Critical

Compromised agents pursue hidden goals while appearing compliant.
ISO 27001 A.8.16 (monitoring activities) is the primary control —
without behavioural monitoring, rogue agents operate until physical
or operational damage reveals their presence. A.5.24 (incident
management) governs the containment response.

#### ISO 27001:2022 mapping

| Control | ID | Domain | How it applies |
|---|---|---|---|
| Monitoring activities | A.8.16 | Technological | Behavioural baseline monitoring — deviation detection is the primary rogue agent control, new 2022 control directly applicable |
| Logging | A.8.15 | Technological | Comprehensive audit logging of all agent actions — no production deployment without full observability |
| Privileged access rights | A.8.2 | Technological | Scope constraints enforced — rogue agent cannot exceed permission envelope regardless of internal goal state |
| Information security incident management | A.5.24 | Organisational | Rogue agent containment as ISMS incident — kill switch, recommendation audit, process state validation, forensic capture |

#### Mitigations by tier

**Foundational**
- A.8.15: Comprehensive audit logging of all agent
  actions — no production deployment without full
  observability, ISMS non-negotiable requirement
- A.8.2: Scope constraints enforced at infrastructure
  layer — rogue agent cannot exceed permission envelope,
  managed as privileged access control
- A.5.24: Rogue agent containment procedure as ISMS
  incident management — kill switch, audit, state
  validation, forensic capture documented

**Hardening**
- A.8.16: Establish behavioural baseline and continuous
  monitoring — baseline documented during commissioning,
  deviation triggers tiered ISMS response
- Aggregate recommendation analysis — periodic review
  detects systematic bias as A.8.16 monitoring control
- A.5.24: Include rogue agent drills in ISMS incident
  response exercises — annual testing of containment
  procedure documented as evidence

**Advanced**
- A.8.29: Rogue agent red team exercises — simulate
  persistent hidden goal pursuit across extended
  sessions, verify detection capability holds, results
  in ISMS security testing records
- A.8.16: Integrate behavioural anomaly detection into
  ISMS SIEM — rogue agent indicators trigger A.5.24
  incident response automatically

#### Tools

| Tool | Type | Link |
|---|---|---|
| Langfuse | Open-source | https://langfuse.com |
| Helicone | Open-source | https://www.helicone.ai |
| Wazuh | Open-source | https://wazuh.com |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: AIUC-1 B001/B002/C/E · EU AI Act Art. 14/15 · ISA/IEC 62443 SR 3.7 (OT)

---

## ISO 27001 ISMS extension checklist for agentic AI

### Scope and asset management

- [ ] All agents added to A.5.9 asset inventory — identity, tool scope, memory stores
- [ ] All agent NHIs inventoried as privileged access credentials (A.8.2)
- [ ] All agent memory stores inventoried as information assets (A.8.3)
- [ ] All A2A communication channels documented as network assets (A.8.20)
- [ ] All agent component vendors added to supplier register (A.5.19)

### Policy and governance

- [ ] AI acceptable use policy updated to cover agentic AI autonomy scope (A.5.10)
- [ ] Agent tool permission policy published — what requires human confirmation (A.5.15)
- [ ] A2A information transfer policy documented (A.5.14)
- [ ] Advisory vs authoritative output classification policy (A.5.12)

### Technical controls

- [ ] Agent credentials managed as privileged access — JIT, minimum scope (A.8.2)
- [ ] Agent NHI identities managed through formal process (A.5.16)
- [ ] Agent credentials encrypted at rest (A.8.24)
- [ ] Memory stores access-controlled and encrypted (A.8.3, A.8.24)
- [ ] A2A channels mutually authenticated and encrypted (A.8.24, A.8.20)
- [ ] DLP extended to agent memory write paths (A.8.12)

### Testing and monitoring

- [ ] Goal hijack in security testing programme (A.8.29)
- [ ] Tool misuse in security testing programme (A.8.29)
- [ ] Sandbox escape in security testing programme (A.8.29)
- [ ] Supply chain integrity in security testing programme (A.8.29)
- [ ] Behavioural baseline established during commissioning (A.8.16)
- [ ] Continuous behavioural monitoring live for all agents (A.8.16)
- [ ] A2A channel anomaly monitoring live (A.8.16)
- [ ] Cascade detection monitoring live (A.8.16)

### Incident management and BCP

- [ ] Rogue agent containment procedure in ISMS incident management (A.5.24)
- [ ] Goal hijack response procedure in ISMS (A.5.24)
- [ ] Cascade incident response in ISMS (A.5.24)
- [ ] Agent cluster failures covered in BCP (A.5.30)
- [ ] Kill switch tested and documented as BCP control (A.5.30)

### Training and awareness

- [ ] All agentic system operators trained on AI limitations (A.6.3)
- [ ] Trust exploitation awareness in security training programme (A.6.3)
- [ ] Supplier security requirements applied to all agent component vendors (A.5.19)

---

## Implementation priority

| Phase | ASI entries | Controls | Rationale |
|---|---|---|---|
| 1 — Privileged access | ASI03, ASI02 | A.8.2, A.5.16 | NHI governance and tool permission are the fastest impact controls |
| 2 — Monitoring | ASI10, ASI01 | A.8.16, A.8.15 | Behavioural baseline and logging close the rogue agent and injection blind spots |
| 3 — Supply chain | ASI04 | A.5.19/A.5.21 | Vendor requirements for all agent component providers |
| 4 — BCP and testing | ASI08, ASI05 | A.5.30, A.8.29 | Resilience and adversarial testing programme |
| 5 — Ongoing | ASI06, ASI07, ASI09 | A.8.24, A.6.3 | Cryptographic controls, training, and A2A hardening |

---

## References

- [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html)
- [ISO/IEC 42001:2023 — AI Management Systems](https://www.iso.org/standard/81230.html)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — ASI01–ASI10 full entries with ISMS extension checklist | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
