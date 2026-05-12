<!--
  GenAI Security Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : CIS Controls v8.1
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × CIS Controls v8.1

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to the [CIS Controls v8.1](https://www.cisecurity.org/controls) —
the Center for Internet Security's prioritised set of safeguards,
organised into 18 control groups with Implementation Groups (IG1/IG2/IG3).

---

## CIS Controls structure

| Group | Controls | Scope |
|---|---|---|
| Basic hygiene (IG1) | CIS 1–6 | Asset inventory, software, data protection, secure config, account management, access control |
| Foundational (IG2) | CIS 7–11 | Vulnerability management, audit logs, email/web, malware, network |
| Organisational (IG3) | CIS 12–18 | Network monitoring, security awareness, app security, incident response, pen testing |

**Implementation Groups:**
- IG1 — Essential cyber hygiene, small to medium organisations
- IG2 — IG1 + additional controls for organisations with sensitive data
- IG3 — IG2 + advanced controls for enterprise and regulated industries

---

## Quick-reference summary

| ID | Name | Severity | Primary CIS Controls | IG | Tier |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | CIS 16, CIS 18, CIS 8, CIS 13 | IG2–IG3 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | CIS 5, CIS 6, CIS 8, CIS 16 | IG1–IG3 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | CIS 5, CIS 6, CIS 8, CIS 3 | IG1–IG3 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | CIS 2, CIS 7, CIS 16, CIS 15 | IG1–IG3 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | CIS 16, CIS 18, CIS 4, CIS 13 | IG2–IG3 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | CIS 3, CIS 8, CIS 16, CIS 13 | IG1–IG3 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | CIS 12, CIS 3, CIS 8, CIS 16 | IG2–IG3 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | CIS 4, CIS 12, CIS 17, CIS 8 | IG1–IG3 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | CIS 14, CIS 17, CIS 5, CIS 8 | IG1–IG3 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | CIS 8, CIS 13, CIS 17, CIS 18 | IG2–IG3 | Hardening–Advanced |

---

## Audience tags

- **Security engineer** — full file, CIS Controls implementation reference for agentic AI
- **Small / medium organisation (IG1–IG2)** — IG1/IG2 safeguards per entry
- **Enterprise (IG3)** — full safeguard coverage including penetration testing
- **Developer** — CIS 16 application security safeguards
- **Auditor** — CIS 18 penetration testing, CIS 8 audit log management
- **OT engineer** — ASI01, ASI02, ASI08 with ISA 62443 crosswalk

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects agent objectives through instruction injection.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 16 — Application Software Security | 16.1 Establish secure application development standards | IG2 | Secure development standards covering agentic integrations — input validation, goal-state verification |
| CIS 18 — Penetration Testing | 18.1 Establish penetration testing programme | IG3 | Adversarial testing covering goal hijack — direct, indirect, multi-turn injection scenarios |
| CIS 8 — Audit Log Management | 8.2 Collect audit logs | IG1 | All agent inputs logged — injection attempts detectable through log analysis |
| CIS 13 — Network Monitoring and Defence | 13.8 Deploy a network intrusion detection solution | IG2 | Network-layer monitoring for injection indicators in agent traffic |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 8.2: Enable audit logging for all agent input
  channels — every prompt logged with agent identity,
  session ID, and source channel
- Treat all external content as untrusted — documents,
  tool returns, email, web results regardless of source
- Implement kill switch accessible from operator console

**Hardening (IG2)**
- CIS 16.1: Establish secure coding standards covering
  agentic integration — goal-state verification and
  input validation as mandatory requirements reviewed
  in code review for all agent-related PRs
- CIS 13.8: Deploy network monitoring covering agent
  traffic — injection indicators in agent communications
  detected and alerted
- Runtime goal-state verification — agent declares
  goal at session start, deviation triggers suspension

**Advanced (IG3)**
- CIS 18.1: Include goal hijack in penetration testing —
  direct, indirect via RAG, indirect via tool returns,
  multi-turn attacks tested against your specific
  deployment
- Red team all indirect injection surfaces quarterly —
  historian data (OT), email, web content, uploaded
  documents

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISO 27001 A.8.28 · NIST CSF 2.0 PR.PS-04 · AIUC-1 B001/B005

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents misuse legitimate tools via prompt manipulation or unsafe
delegation. CIS Controls 5 (account management) and 6 (access control)
govern agent tool permissions as privileged access.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 5 — Account Management | 5.4 Restrict administrator privileges | IG1 | Agent tool access managed as privileged access — minimum scope, regular review |
| CIS 6 — Access Control Management | 6.1 Establish access granting process | IG1 | Formal process for granting agent tool access — documented justification per tool |
| CIS 8 — Audit Log Management | 8.5 Collect detailed audit logs | IG2 | All tool invocations logged — tool identity, parameters, agent identity, timestamp |
| CIS 16 — Application Software Security | 16.1 Establish secure development standards | IG2 | Tool parameter validation as secure development requirement |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 5.4: Manage agent tool access as privileged access —
  per-tool permission manifests, minimum scope, quarterly
  review, irreversibility classification documented
- CIS 6.1: Formal process for granting agent tool access —
  documented business justification per tool, approval
  chain, regular review schedule
- Human confirmation for all irreversible tool invocations —
  separate confirmation interface, not through agent chat

**Hardening (IG2)**
- CIS 8.5: Detailed audit logs for all tool invocations —
  tool identity, parameters, agent identity, session,
  timestamp — immutable trail for forensic investigation
- CIS 16.1: Tool parameter validation in secure development
  standards — LLM-generated parameters treated as
  untrusted, validated before execution
- MCP tool descriptor integrity verification — hash-based
  check before loading any tool descriptor

**Advanced (IG3)**
- CIS 18.1: Include tool misuse in penetration testing —
  destructive parameters, tool chain exploitation,
  MCP descriptor poisoning tested against your deployment
- Conduct tool permission red team — attempt harm through
  legitimate tool invocations within defined scope

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: ISO 27001 A.8.2 · OWASP NHI Top 10 NHI-5 · AIUC-1 B006/B007

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit and cache credentials exploited for lateral movement.
CIS Controls 5 (account management) is the primary control — agent
NHIs are accounts requiring the same management rigour as human accounts.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 5 — Account Management | 5.4 Restrict administrator privileges | IG1 | Agent credentials managed as privileged accounts — minimum scope, regular review, JIT issuance |
| CIS 6 — Access Control Management | 6.2 Establish an access revoking process | IG1 | Agent credential revocation process — immediate revocation on detection, decommission procedure |
| CIS 8 — Audit Log Management | 8.5 Collect detailed audit logs | IG2 | All credential operations logged — issuance, use, anomalous patterns detectable |
| CIS 3 — Data Protection | 3.11 Encrypt sensitive data at rest | IG1 | Agent credentials encrypted at rest — secret manager, no cleartext storage |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 5.4: Manage agent credentials as privileged accounts —
  unique NHI per agent deployment, minimum scope, no
  shared credentials, short TTL with automatic expiry
- CIS 6.2: Establish agent credential revocation process —
  immediate revocation on compromise detection,
  formal decommission procedure for retired agents
- CIS 3.11: Encrypt all agent credentials at rest —
  secret manager required, no cleartext in config,
  source code, or agent memory

**Hardening (IG2)**
- CIS 8.5: Detailed logging of all credential operations —
  issuance, use, expiry — full trail enabling forensic
  investigation of lateral movement
- Credential anomaly detection — unusual access scope
  or timing alerted, automated response triggered
- CIS 5.4: Quarterly privileged access review includes
  all agent NHIs — unused permissions removed

**Advanced (IG3)**
- CIS 18.1: Include credential abuse in penetration
  testing — attempt lateral movement using agent
  credentials, document access scope achievable
- Implement PKI-backed agent identities — certificate-
  based authentication as advanced NHI control

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 (all entries) · ISO 27001 A.8.2/A.5.16 · EU AI Act Art. 15

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High

Compromised tools, MCP servers, or model components alter agent
behaviour. CIS Controls 2 (software asset inventory) and 7 (vulnerability
management) govern agent components as software assets.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 2 — Inventory and Control of Software Assets | 2.1 Establish and maintain software inventory | IG1 | ML SBOM as software asset inventory — all agent components (tools, MCP servers, models, libraries) |
| CIS 7 — Continuous Vulnerability Management | 7.1 Establish vulnerability management process | IG1 | Agent component CVEs in vulnerability management — urgent patching for code execution risks |
| CIS 16 — Application Software Security | 16.6 Use only up-to-date and trusted third-party components | IG2 | Approved component list — only sourced from approved vendors, signatures verified |
| CIS 15 — Service Provider Management | 15.1 Establish service provider management process | IG2 | Agent tool and MCP providers managed as service providers — security assessment before onboarding |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 2.1: Maintain ML SBOM as software asset inventory —
  every agent component (tools, MCP servers, model weights,
  libraries) inventoried with version, source, hash
- CIS 7.1: Include agent component CVEs in vulnerability
  management — ML library CVEs and MCP server
  vulnerabilities scanned and patched on schedule
- Pin all component versions — no automatic updates
  without review and approval

**Hardening (IG2)**
- CIS 16.6: Approved component list for all agentic
  deployments — only sourced from approved vendors,
  cryptographic signatures verified before loading
- CIS 15.1: Manage agent tool and MCP providers as
  service providers — security assessment before
  onboarding, contracts with security obligations
- Scan all tool descriptors for hidden instructions —
  rejection before loading if suspicious patterns found

**Advanced (IG3)**
- CIS 18.1: Include supply chain attacks in penetration
  testing — attempt to introduce compromised component,
  verify detection capability
- Operate isolated evaluation environment — component
  behavioural testing before each production promotion

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: ISO 27001 A.5.19/A.5.21 · NIST CSF 2.0 GV.SC-01 · ISA/IEC 62443 62443-2-4 (OT)

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents that generate and execute code become RCE gateways. CIS Controls
16 (application security) and 4 (secure configuration) govern code
execution security as application and configuration controls.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 16 — Application Software Security | 16.1 Establish secure development standards | IG2 | Sandbox, static analysis, and allowlist as secure development requirements for code execution |
| CIS 4 — Secure Configuration | 4.1 Establish secure configuration process | IG1 | Secure configuration includes code execution sandbox — no defaults permitting unrestricted execution |
| CIS 18 — Penetration Testing | 18.1 Establish penetration testing | IG3 | Sandbox escape and code injection in penetration testing — adversarial scenarios before each deployment |
| CIS 13 — Network Monitoring | 13.8 Deploy network intrusion detection | IG2 | Code execution environments network-monitored — outbound connection attempts from sandbox detected |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 4.1: Secure configuration baseline includes code
  execution sandbox — no unrestricted shell access from
  agent context, enforced at deployment
- Avoid deploying agents with code execution capability —
  strongest control, should be the default position

**Hardening (IG2)**
- CIS 16.1: Implement sandbox, static analysis, and
  allowlist as secure development requirements — all
  code execution capability in agents requires these
  controls before deployment review approval
- CIS 13.8: Network monitoring on code execution
  environments — outbound network attempts from sandbox
  detected and blocked, alerted

**Advanced (IG3)**
- CIS 18.1: Include sandbox escape in penetration testing —
  attempt escape from within specific runtime, document
  results, retest after any sandbox configuration change
- Hardware-level sandboxing for highest-risk deployments —
  gVisor or Firecracker as advanced configuration control

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006 · CWE-94 · ISO 27001 A.8.28

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Persistent memory poisoning causes systematic incorrect behaviour.
CIS Controls 3 (data protection) and 8 (audit logs) govern memory
stores as data assets with access control and logging requirements.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 3 — Data Protection | 3.11 Encrypt sensitive data at rest | IG1 | Agent memory stores encrypted at rest — embeddings, long-term memory, operational knowledge |
| CIS 8 — Audit Log Management | 8.2 Collect audit logs | IG1 | Memory write operations logged — who or what wrote, when, content hash |
| CIS 16 — Application Software Security | 16.1 Establish secure development standards | IG2 | Memory write validation as secure development requirement — untrusted sources cannot write directly |
| CIS 13 — Network Monitoring | 13.3 Deploy a network-based intrusion detection system | IG2 | Memory store access monitored — bulk read, anomalous write patterns detected |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 3.11: Encrypt all agent memory stores at rest —
  embedding databases, long-term memory, operational
  knowledge base all encrypted
- CIS 8.2: Log all memory write operations — source
  identity, timestamp, content hash — audit trail
  enabling poisoning investigation
- Enforce memory TTL — entries expire requiring
  re-validation, no indefinite persistence

**Hardening (IG2)**
- CIS 16.1: Memory write validation as secure development
  requirement — untrusted sources cannot write to memory
  without explicit validation and approval
- CIS 13.3: Monitor memory store access patterns —
  bulk reads, unusual write volumes, statistical
  anomalies in content detected

**Advanced (IG3)**
- CIS 18.1: Include memory poisoning in penetration
  testing — injection paths via each content source
  tested, detection capability verified
- Cryptographic integrity verification on memory content —
  tamper detection between write and read

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning, LLM08 Vector & Embedding Weaknesses
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: ISO 27001 A.8.3/A.8.24 · NIST AI RMF MS-2.5 · AIUC-1 A/B002

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High

A2A channels lacking authentication enable agent-in-the-middle attacks.
CIS Controls 12 (network infrastructure management) and 3 (data protection)
govern A2A communication as network traffic requiring encryption and
integrity controls.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 12 — Network Infrastructure Management | 12.4 Establish and maintain architecture diagram | IG2 | A2A communication channels mapped in network architecture — authentication method, encryption status |
| CIS 3 — Data Protection | 3.10 Encrypt sensitive data in transit | IG1 | All A2A messages encrypted in transit — no cleartext inter-agent communication |
| CIS 8 — Audit Log Management | 8.5 Collect detailed audit logs | IG2 | All A2A messages logged — sender identity, content hash, timestamp, schema validation results |
| CIS 16 — Application Software Security | 16.1 Establish secure development standards | IG2 | A2A authentication and schema validation as secure development requirements |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 3.10: Encrypt all A2A communication in transit —
  mutual TLS, no cleartext inter-agent messages on any
  network segment

**Hardening (IG2)**
- CIS 12.4: Map all A2A communication channels in network
  architecture — authentication method, encryption
  status, replay protection documented
- CIS 8.5: Detailed logging of all A2A messages —
  sender identity, content hash, timestamp — full
  audit trail for forensic investigation
- CIS 16.1: A2A authentication as secure development
  requirement — no unauthenticated A2A in any
  environment including development

**Advanced (IG3)**
- CIS 18.1: A2A security in penetration testing —
  spoofing, replay attacks, schema violations tested
  against your specific deployment
- Short-lived A2A certificates — automated rotation,
  hardware-backed keys for highest-risk clusters

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 NHI-4/NHI-7 · ISO 27001 A.8.20/A.8.24 · AIUC-1 B007/B008

---

### ASI08 — Cascading Agent Failures

**Severity:** High

Single-point faults propagate through multi-agent workflows.
CIS Controls 4 (secure configuration) and 12 (network infrastructure)
govern circuit breakers and blast radius limits as configuration
and network controls. In OT environments this is Critical severity.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 4 — Secure Configuration | 4.1 Establish secure configuration process | IG1 | Secure configuration includes circuit breakers and rate limits — cascade prevention as configuration requirement |
| CIS 12 — Network Infrastructure Management | 12.6 Use network-based URL filters | IG2 | Network controls prevent cascade propagation across agent cluster boundaries |
| CIS 17 — Incident Response | 17.1 Designate personnel for incident response | IG1 | Defined response for cascade events — kill switch activation, process control fallback, operations notification |
| CIS 8 — Audit Log Management | 8.6 Collect DNS query audit logs | IG2 | Agent traffic monitored — cascade indicators detected before physical impact |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 4.1: Secure configuration baseline includes
  circuit breakers and fail-safe defaults — cascade
  prevention enforced at deployment, not optional
- CIS 17.1: Define cascade incident response — kill
  switch activation procedure, process control fallback,
  operations notification documented and drilled

**Hardening (IG2)**
- CIS 12.6: Network controls prevent cross-cluster
  cascade propagation — agent clusters isolated at
  network layer, inter-cluster communication rate-limited
- CIS 8.6: Monitor agent traffic for cascade indicators —
  correlated failure patterns alerted before blast
  radius reaches critical systems

**Advanced (IG3)**
- CIS 18.1: Cascade scenarios in penetration testing —
  circuit breaker effectiveness tested under adversarial
  load, results documented
- Chaos engineering as advanced penetration testing
  activity — intentional failure injection, recovery
  path validated

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: ISO 27001 A.5.30 · ISA/IEC 62443 SR 7.6/7.7 (OT) · AIUC-1 D

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Agents build false trust enabling manipulation of human approvers.
CIS Controls 14 (security awareness) is the primary control — trust
exploitation is fundamentally a people risk addressed by training.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 14 — Security Awareness and Skills Training | 14.1 Establish security awareness programme | IG1 | All users of agentic tools trained on AI limitations — verification requirements, how to identify manipulation |
| CIS 17 — Incident Response | 17.1 Designate personnel for incident response | IG1 | Defined response for trust exploitation incidents — operator retraining, pattern audit, interface redesign |
| CIS 5 — Account Management | 5.4 Restrict administrator privileges | IG1 | Approval flows independent of agent interface — sensitive approvals cannot be completed via agent chat |
| CIS 8 — Audit Log Management | 8.5 Collect detailed audit logs | IG2 | Agent-influenced operator decisions logged — aggregate over-trust patterns detectable |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 14.1: Provide security awareness training to all
  users of agentic tools — AI limitations, verification
  requirements, how to identify AI advisory vs
  authoritative content, mandatory before access
- CIS 5.4: Approval flows restricted to independent
  systems — sensitive approvals cannot be completed
  through agent chat interface
- CIS 17.1: Define trust exploitation incident response —
  operator retraining, pattern audit, interface review

**Hardening (IG2)**
- CIS 8.5: Log all agent-influenced operator decisions —
  aggregate over-trust patterns detectable through
  audit log analysis
- AI advisory labelling in all interface contexts —
  visual distinction from authoritative system content,
  enforced at rendering layer
- Safety alarm independence — agents prohibited from
  acknowledging or suppressing safety alarms (OT)

**Advanced (IG3)**
- CIS 18.1: Include trust exploitation in penetration
  testing — test operator susceptibility to manipulated
  agent recommendations in your specific deployment
- Operator competency assessments covering AI trust —
  verify operators can identify manipulated recommendations

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: EU AI Act Art. 13/50 · ISO 27001 A.6.3 · AIUC-1 C/F

---

### ASI10 — Rogue Agents

**Severity:** Critical

Compromised agents pursue hidden goals while appearing compliant.
CIS Controls 8 (audit log management) and 13 (network monitoring)
are the primary detection controls — comprehensive logging and
behavioural monitoring are the foundational rogue agent defences.

#### CIS Controls mapping

| Control | Safeguard | IG | How it applies |
|---|---|---|---|
| CIS 8 — Audit Log Management | 8.2 Collect audit logs | IG1 | Comprehensive audit logging of all agent actions — no production deployment without full observability |
| CIS 13 — Network Monitoring and Defence | 13.1 Centralise security event alerting | IG2 | Agent behavioural anomalies centralised and alerted — rogue agent patterns detected through SIEM |
| CIS 17 — Incident Response | 17.2 Establish incident response procedures | IG1 | Rogue agent containment as incident response procedure — kill switch, audit, state validation, forensic |
| CIS 18 — Penetration Testing | 18.1 Establish penetration testing | IG3 | Rogue agent scenarios in penetration testing — persistent hidden goal simulation, detection verification |

#### Mitigations by tier

**Foundational (IG1)**
- CIS 8.2: Comprehensive audit logging of all agent
  actions — no production agentic deployment without
  full observability, non-negotiable IG1 requirement
- CIS 17.2: Rogue agent containment as incident response
  procedure — kill switch activation, recommendation
  audit, process state validation, forensic capture
  documented before deployment
- Scope constraints enforced — rogue agent cannot
  exceed permission envelope regardless of internal goal

**Hardening (IG2)**
- CIS 13.1: Centralise agent behavioural anomaly alerts —
  behavioural baseline deviation events fed into SIEM,
  tiered response automated
- Establish behavioural baseline during commissioning —
  expected action patterns documented, deviation
  triggers tiered alert
- Aggregate recommendation analysis — periodic review
  detects systematic bias before operational harm

**Advanced (IG3)**
- CIS 18.1: Rogue agent scenarios in penetration testing —
  simulate persistent hidden goal pursuit across extended
  sessions, verify detection capability holds, document
  results
- CIS 18.3: Remediate and retest after rogue agent
  drill findings — detection gaps closed before
  next deployment

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Overreach
- Other frameworks: ISO 27001 A.8.16/A.8.15 · AIUC-1 B001/B002/C/E · EU AI Act Art. 14/15

---

## CIS Controls implementation priority by IG

### IG1 — Essential hygiene (start here)

| ASI entry | CIS safeguards | Action |
|---|---|---|
| ASI03, ASI02 | CIS 5.4, CIS 6.1/6.2 | Agent NHIs as privileged accounts — minimum scope, JIT, revocation process |
| ASI01, ASI10 | CIS 8.2 | Audit logging on all agent inputs, outputs, and actions |
| ASI08 | CIS 4.1, CIS 17.1 | Circuit breakers in secure config, cascade incident response defined |
| ASI03 | CIS 3.11 | Agent credentials encrypted at rest |
| ASI09 | CIS 14.1, CIS 17.1 | Security awareness training, trust exploitation incident response |

### IG2 — For organisations with sensitive data (add next)

| ASI entry | CIS safeguards | Action |
|---|---|---|
| ASI01, ASI02 | CIS 16.1 | Secure development standards covering agentic integration |
| ASI02, ASI10 | CIS 8.5 | Detailed audit logs for tool invocations and agent actions |
| ASI04 | CIS 15.1, CIS 16.6 | Service provider management for tool vendors, approved component list |
| ASI07 | CIS 12.4 | A2A channels in network architecture, authentication documented |
| ASI08 | CIS 12.6 | Network controls for cross-cluster cascade prevention |
| ASI10 | CIS 13.1 | Centralised agent anomaly alerting in SIEM |

### IG3 — Enterprise and regulated (complete coverage)

| ASI entry | CIS safeguards | Action |
|---|---|---|
| All | CIS 18.1, CIS 18.3 | Penetration testing programme covering all agentic scenarios |
| ASI01, ASI10 | CIS 18.3 | Remediate and retest after each finding |

---

## References

- [CIS Controls v8.1](https://www.cisecurity.org/controls)
- [CIS Controls implementation guide](https://www.cisecurity.org/controls/implementation-groups)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — ASI01–ASI10 full entries with IG-tiered safeguards | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the GenAI Security Crosswalk: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk
