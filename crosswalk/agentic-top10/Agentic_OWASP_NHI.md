<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10)
  Framework   : OWASP Non-Human Identities (NHI) Top 10
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × OWASP NHI Top 10

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to the [OWASP Non-Human Identities (NHI) Top 10](https://owasp.org/www-project-non-human-identities-top-10/)
— the framework for securing machine identities including service
accounts, API keys, OAuth tokens, certificates, and agent identities.

---

## Why NHI is the identity layer for agentic AI

The average enterprise already operates an 82:1 machine-to-human
identity ratio. Every agentic AI deployment multiplies that ratio —
each agent requires credentials to access tools, APIs, databases,
and other agents. These are Non-Human Identities in the NHI Top 10
sense: machine-issued, machine-used, rarely rotated, frequently
over-privileged, and almost never monitored with the same rigour as
human identities.

The overlap between the Agentic Top 10 and the NHI Top 10 is not
incidental — it is structural. Three of the ten agentic risks (ASI01,
ASI02, ASI03) have NHI abuse as their primary attack execution path.
ASI04 introduces new NHI risks at every runtime component load. ASI07
and ASI10 depend on NHI infrastructure for detection and response.

This mapping is the most operationally actionable file in the Agentic
section for security engineers and identity teams — it translates
agentic risks into the NHI controls that practitioners already manage.

---

## OWASP NHI Top 10 reference

| NHI Entry | Name | Description |
|---|---|---|
| NHI-1 | Improper Offboarding | NHIs not revoked when systems decommission or relationships end |
| NHI-2 | Secret Leakage | Credentials exposed in source code, logs, config, or memory |
| NHI-3 | Vulnerable Third-Party NHI | Third-party tokens and identities with excessive permissions |
| NHI-4 | Insecure Authentication | Weak or missing authentication for machine-to-machine communication |
| NHI-5 | Over-Privileged NHI | NHIs with more permissions than required — lateral movement risk |
| NHI-6 | Insecure Credential Storage | Credentials stored insecurely — plaintext, weak encryption |
| NHI-7 | Long-Lived Credentials | Credentials without rotation, expiry, or revocation capability |
| NHI-8 | Environment Isolation Failure | Credentials shared across environments — prod creds in dev |
| NHI-9 | NHI Reuse | Same credentials or token used across multiple services or agents |
| NHI-10 | Human Use of NHI | Humans using machine credentials — no attribution, no MFA |

---

## Quick-reference summary

| ASI ID | Name | Severity | Primary NHI Entries | Tier |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | NHI-5, NHI-7, NHI-9 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | NHI-5, NHI-3, NHI-9 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | NHI-1 through NHI-10 (all) | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | NHI-3, NHI-6, NHI-2 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | NHI-5, NHI-8, NHI-9 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | NHI-2, NHI-6, NHI-7 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | NHI-4, NHI-7, NHI-9 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | NHI-5, NHI-9, NHI-7 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | NHI-10, NHI-5 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | NHI-1, NHI-5, NHI-7 | Hardening–Advanced |

---

## Audience tags

- **Identity and access management (IAM) team** — full file, primary NHI reference for agentic AI
- **Security engineer** — NHI-2/NHI-5/NHI-7 entries most actionable
- **Platform engineer** — NHI-4/NHI-8/NHI-9 entries for infrastructure design
- **Auditor** — NHI-1/NHI-10 offboarding and human use entries
- **CISO** — full file, NHI as the identity governance layer for agentic AI
- **OT engineer** — ASI03, ASI07 entries with ISA 62443 crosswalk for OT context

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects agent goals — but execution requires credentials.
Goal hijack is most effective when agents hold NHI-5 (over-privileged)
credentials, because a hijacked agent with over-privileged access can
cause significantly more damage than a correctly-scoped agent. NHI-7
(long-lived credentials) amplifies this — a hijacked agent can use
stolen long-lived tokens for extended periods before revocation.

#### NHI mapping

| NHI Entry | How it amplifies goal hijack | Control |
|---|---|---|
| NHI-5 Over-Privileged NHI | Hijacked agent with excess privilege causes larger blast radius | Scope all agent credentials to minimum required — least privilege enforced |
| NHI-7 Long-Lived Credentials | Long-lived tokens allow hijack to persist beyond session | Short-lived credentials — tokens expire at task completion, no long-lived agent tokens |
| NHI-9 NHI Reuse | Shared credentials allow hijacked agent to impersonate other agents | Unique identity per agent — no shared service accounts across agent deployments |

#### Mitigations

**Foundational**
- NHI-5: Scope all agent credentials to minimum required
  permissions — a hijacked agent with least privilege has
  a dramatically smaller blast radius than one with broad access
- NHI-9: Issue unique identity per agent deployment —
  no shared credentials across agent instances or roles
- Verify goal-state before any privileged operation —
  credential use requires confirmed intent

**Hardening**
- NHI-7: Implement short-lived credential issuance —
  tokens expire at task completion, require re-issuance
  for each new task, no long-lived tokens in agent memory
- Credential anomaly detection — goal hijack often manifests
  as unusual credential use patterns before tool invocation
- NHI-5: Quarterly privilege review — any permission not
  actively used is removed from agent credential scope

**Advanced**
- Cryptographically bound agent credentials — token valid
  only when agent goal state matches the signed specification
- NHI-7: Automated revocation on goal deviation detection —
  token invalidated immediately on anomaly signal
- Continuous NHI monitoring across all agent sessions —
  unusual access patterns correlated with goal state analysis

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| Entro Security | Commercial | https://entro.security |
| Teleport | Open-source/Commercial | https://goteleport.com |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: AIUC-1 A/B006 · EU AI Act Art. 14 · NIST AI RMF GV-1.6

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents misuse legitimate tools — but tool access is mediated by NHI
credentials. NHI-5 (over-privileged) is the root amplifier: an agent
that misuses a tool can only do so within the scope of its credentials.
NHI-3 (vulnerable third-party NHI) is the supply chain amplifier —
a compromised MCP server's identity token can access every resource
the agent's credential scope permits.

#### NHI mapping

| NHI Entry | How it amplifies tool misuse | Control |
|---|---|---|
| NHI-5 Over-Privileged NHI | Agent with excess privilege can call tools in destructive ways even within normal use | Per-tool permission manifests — each tool scoped to minimum required operations |
| NHI-3 Vulnerable Third-Party NHI | Compromised third-party tool identity gets full scope of agent credential | Validate all third-party tool identities — reject tokens from unregistered issuers |
| NHI-9 NHI Reuse | Single shared credential allows tool misuse to affect multiple services | Unique credential per tool integration — tool-scoped tokens, not agent-wide tokens |

#### Mitigations

**Foundational**
- NHI-5: Implement per-tool permission scope — agent does
  not hold a single broad credential but tool-specific
  scoped tokens for each integration
- NHI-3: Validate all third-party tool and MCP server
  identities before agent connection — reject tokens from
  unregistered or unverified issuers
- Human confirmation for all irreversible tool invocations —
  credential use for high-impact operations gated on
  human approval, not agent decision

**Hardening**
- NHI-9: Issue unique, tool-scoped credentials per tool
  integration — compromise of one tool's credential does
  not affect access to other tools
- Log all tool credential operations — issuance, use,
  expiry — anomalous patterns detected before misuse
  causes damage
- NHI-3: Maintain approved tool identity registry —
  agent cannot connect to any tool not in the registry

**Advanced**
- Automated tool credential revocation on anomaly detection —
  single compromised tool token revoked without affecting
  other tool access
- NHI-5: Continuous privilege monitoring — alert when tool
  invocation scope approaches limits, reduce automatically
- Conduct tool credential abuse red team exercises —
  attempt lateral movement using tool-scoped tokens

#### Tools

| Tool | Type | Link |
|---|---|---|
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| HashiCorp Vault | Open-source | https://www.vaultproject.io |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool Plugin & Agent Data Exchange
- Other frameworks: AIUC-1 B006/B007 · EU AI Act Art. 15 · ISA/IEC 62443 SR 2.2 (OT)

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

ASI03 is the direct intersection of the Agentic Top 10 and the NHI
Top 10 — every NHI risk entry maps to some aspect of agent identity
and privilege abuse. This entry is the most comprehensive NHI mapping
in the repo. If your organisation has a mature NHI programme, applying
it to agent identities addresses ASI03 almost entirely.

#### NHI mapping — full coverage

| NHI Entry | How it maps to ASI03 | Control |
|---|---|---|
| NHI-1 Improper Offboarding | Agent credentials not revoked on decommission — dormant tokens exploitable | Formal agent offboarding — all credentials revoked, tokens invalidated, access removed |
| NHI-2 Secret Leakage | Agent credentials exposed in memory, logs, tool payloads | No credentials in agent context, logs, or tool payloads — secret manager only |
| NHI-3 Vulnerable Third-Party NHI | Third-party tool credentials with excessive permissions inherited by agent | Validate all third-party NHIs — revoke over-privileged third-party tokens |
| NHI-4 Insecure Authentication | Weak agent-to-system authentication — credential reuse or weak secrets | Strong authentication for all agent-to-system connections — mTLS, short-lived tokens |
| NHI-5 Over-Privileged NHI | Agent holds more permissions than required — lateral movement amplifier | Least privilege per agent role — scope enforced, reviewed quarterly |
| NHI-6 Insecure Credential Storage | Agent credentials stored in cleartext — config files, environment variables | Secret manager for all agent credentials — no cleartext storage anywhere |
| NHI-7 Long-Lived Credentials | Agent tokens without expiry — compromise persists indefinitely | Short-lived credentials — task-scoped tokens with automatic expiry |
| NHI-8 Environment Isolation Failure | Production agent credentials accessible in dev/test environments | Strict environment isolation — separate credentials per environment, no cross-environment reuse |
| NHI-9 NHI Reuse | Shared agent credential across multiple instances or deployments | Unique identity per agent deployment — no credential sharing |
| NHI-10 Human Use of NHI | Humans using agent service accounts — no attribution, no MFA | Agent credentials machine-only — human use detected and blocked |

#### Mitigations by tier

**Foundational**
- NHI-5: Enforce least privilege on all agent credentials —
  minimum required permissions, reviewed quarterly
- NHI-6: Store all agent credentials in secret manager —
  no cleartext in config files, source code, or environment
  variables
- NHI-9: Issue unique identity per agent deployment — no
  shared service accounts across agent instances or roles

**Hardening**
- NHI-7: Implement task-scoped short-lived credentials —
  tokens expire at task completion, require re-issuance
- NHI-2: Scan all agent memory stores, logs, and tool
  payloads for exposed credentials — automated detection
- NHI-8: Enforce strict environment isolation — separate
  credential sets per environment, production credentials
  never accessible from development

**Advanced**
- NHI-1: Formal agent offboarding programme — decommission
  checklist covering all credential revocation, token
  invalidation, and access removal
- NHI-10: Detect and block human use of agent credentials —
  machine identity use from human sessions triggers alert
- NHI-4: Implement PKI-backed agent identities — certificate-
  based authentication for all agent-to-system connections

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| Teleport | Open-source/Commercial | https://goteleport.com |
| Entro Security | Commercial | https://entro.security |
| SPIFFE / SPIRE | Open-source | https://spiffe.io |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: AIUC-1 A/B007/B008 · EU AI Act Art. 15 · ISA/IEC 62443 SR 1.2 (OT)

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High

Compromised MCP servers and tools introduce new NHI risks at runtime —
a malicious MCP server's identity token can access everything the
agent's credential scope permits. NHI-3 (vulnerable third-party NHI)
is the primary supply chain NHI risk.

#### NHI mapping

| NHI Entry | How it maps to ASI04 | Control |
|---|---|---|
| NHI-3 Vulnerable Third-Party NHI | Compromised MCP server holds or can request excessive permissions | Validate all third-party NHIs at connection — revoke tokens from unverified sources |
| NHI-6 Insecure Credential Storage | Malicious components extract credentials from agent memory or config | Credential isolation — components cannot access other components' credentials |
| NHI-2 Secret Leakage | Supply chain compromise introduces credential exfiltration code | Scan all agent components for credential access patterns before deployment |

#### Mitigations

**Foundational**
- NHI-3: Validate all third-party tool and MCP server
  identities before agent connection — approved registry,
  token issuer verification, permission scope audit
- NHI-2: Scan all agent supply chain components for
  credential access patterns — any component attempting
  to read credentials outside its scope is a rejection trigger

**Hardening**
- NHI-6: Isolate credentials from supply chain components —
  components receive only the minimum token required for
  their specific function, not the agent's full credential
- NHI-3: Maintain dynamic approved tool identity registry —
  agent cannot connect to any tool not in the registry,
  even if dynamically discovered at runtime

**Advanced**
- Automated NHI audit after each supply chain update —
  verify that new components have not altered credential
  scope or access patterns
- NHI-3: Continuous third-party NHI monitoring — alert on
  unusual permission requests from supply chain components

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data Model & Artifact Poisoning
- Other frameworks: AIUC-1 B001/B003 · EU AI Act Art. 25 · NIST SP 800-218A

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agent code execution capability creates a new NHI risk surface —
executed code runs in the context of the agent's credentials.
NHI-5 (over-privileged) is the primary amplifier: code executing
under an over-privileged agent identity can access far more than
intended.

#### NHI mapping

| NHI Entry | How it maps to ASI05 | Control |
|---|---|---|
| NHI-5 Over-Privileged NHI | Code executes in context of over-privileged agent credential — amplifies RCE impact | Sandbox code execution under a separate, minimal credential — not the agent's primary identity |
| NHI-8 Environment Isolation Failure | Code execution in production context with prod credentials | Strict environment isolation for code execution — dedicated sandboxed identity |
| NHI-9 NHI Reuse | Shared credential means RCE in one agent affects all agents sharing the credential | Unique credential per agent — code execution in one instance cannot leverage other instances' access |

#### Mitigations

**Foundational**
- NHI-5: Run agent code execution under a separate,
  sandboxed identity with minimal permissions — not the
  agent's primary credential
- NHI-8: Strict environment isolation — code execution
  sandbox has no access to production credentials

**Hardening**
- NHI-9: Unique credential per agent deployment — RCE in
  one instance cannot leverage shared credentials to
  access other services
- Monitor code execution identity usage — any access
  outside the defined sandbox scope triggers immediate alert

**Advanced**
- Ephemeral execution identity — unique credential issued
  per code execution task, immediately revoked on completion
- NHI-5: Formal risk acceptance for any code execution
  agent — privilege review required before deployment

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006 · EU AI Act Art. 15

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Agent memory stores are accessed via credentials. If memory store
credentials are compromised through NHI-2 (secret leakage) or
NHI-6 (insecure storage), an attacker can poison memory directly
without going through the agent at all.

#### NHI mapping

| NHI Entry | How it maps to ASI06 | Control |
|---|---|---|
| NHI-2 Secret Leakage | Memory store credentials leaked — attacker writes poisoned content directly | Scan all paths where memory store credentials could leak — logs, config, agent context |
| NHI-6 Insecure Credential Storage | Memory store credentials in cleartext — trivially extracted | Secret manager for all memory store credentials — no cleartext anywhere |
| NHI-7 Long-Lived Credentials | Long-lived memory store credentials enable persistent access for attacker | Short-lived credentials for memory store access — rotate on each agent session |

#### Mitigations

**Foundational**
- NHI-6: Store all memory store credentials in secret
  manager — no cleartext access tokens for vector stores,
  RAG indexes, or agent memory systems
- NHI-2: Scan all agent memory stores for exposed
  credentials — memory poisoning can include credential
  injection for lateral movement

**Hardening**
- NHI-7: Rotate memory store credentials per session —
  long-lived tokens for vector stores are unnecessary
  and expand the window for attacker exploitation
- NHI-2: Implement credential detection on memory write
  operations — alert on any attempt to write credential
  patterns to agent memory

**Advanced**
- Separate memory store identity from agent primary
  identity — memory access uses a distinct, scoped
  NHI that cannot be used for any other operation
- Continuous memory credential audit — access pattern
  anomalies in memory stores correlated with agent
  behaviour analysis

#### Cross-references
- LLM Top 10: LLM04 Data & Model Poisoning
- DSGAI 2026: DSGAI13 Vector Store Platform Security
- Other frameworks: AIUC-1 A/B002 · ISO 27001 A.8.24 · NIST AI RMF GV-1.6

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High

A2A communication security is fundamentally an NHI authentication
problem. NHI-4 (insecure authentication) is the primary failure mode —
agent-to-agent channels without strong mutual authentication enable
spoofing and man-in-the-middle attacks.

#### NHI mapping

| NHI Entry | How it maps to ASI07 | Control |
|---|---|---|
| NHI-4 Insecure Authentication | Weak or missing authentication on A2A channels — agent spoofing enabled | Strong mutual authentication on all A2A channels — mTLS, certificate-based, short-lived |
| NHI-7 Long-Lived Credentials | Long-lived A2A tokens enable persistent replay attacks | Short-lived A2A tokens with nonce-based replay protection |
| NHI-9 NHI Reuse | Shared A2A credentials allow one compromised agent to impersonate others | Unique identity per agent — A2A authentication bound to specific agent identity |

#### Mitigations

**Foundational**
- NHI-4: Implement authentication on all A2A channels —
  no ambient trust between agents, even on internal networks
- NHI-9: Unique agent identity for all A2A communication —
  each agent has its own certificate or token, not shared
  across the cluster

**Hardening**
- NHI-7: Short-lived A2A tokens with replay protection —
  nonces, timestamps, and sequence numbers on all channels
- NHI-4: Mutual TLS for all production A2A channels —
  both parties authenticate before message exchange

**Advanced**
- PKI-backed agent identities — certificate-based A2A
  authentication with hardware-backed keys for highest-risk
  agent clusters
- Continuous A2A credential anomaly detection — unusual
  authentication patterns flagged immediately

#### Tools

| Tool | Type | Link |
|---|---|---|
| SPIFFE / SPIRE | Open-source | https://spiffe.io |
| cert-manager | Open-source | https://cert-manager.io |
| Linkerd | Open-source | https://linkerd.io |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: AIUC-1 B007/B008 · EU AI Act Art. 15 · ISA/IEC 62443 SR 3.1 (OT)

---

### ASI08 — Cascading Agent Failures

**Severity:** High

NHI over-privilege amplifies cascade blast radius. When a failing
or compromised agent in a cluster holds NHI-5 (over-privileged)
credentials or NHI-9 (reused) credentials, its failure can expose
all systems the over-privileged or shared credential provides access
to — across the entire cascade path.

#### NHI mapping

| NHI Entry | How it maps to ASI08 | Control |
|---|---|---|
| NHI-5 Over-Privileged NHI | Cascading agent failure with over-privileged credentials exposes all accessible systems | Least privilege per agent — cascade blast radius limited by credential scope |
| NHI-9 NHI Reuse | Shared credentials mean cascade in one agent affects all agents sharing the credential | Unique identity per agent — cascade cannot leverage shared credentials for lateral movement |
| NHI-7 Long-Lived Credentials | Long-lived credentials exposed during cascade remain valid for attacker use post-incident | Short-lived credentials — cascade event triggers automatic revocation of all affected tokens |

#### Mitigations

**Foundational**
- NHI-5: Least privilege per agent — cascade blast radius
  is bounded by the narrowest credential scope
- NHI-9: Unique identity per agent — cascade failure in
  one agent cannot leverage shared credentials across
  the cluster

**Hardening**
- NHI-7: Automated credential revocation on cascade
  detection — all tokens for suspended agents immediately
  invalidated, not just flagged
- Circuit breaker activation triggers credential suspension —
  failing agents lose credential access before human
  investigation begins

**Advanced**
- NHI-5: Dynamic privilege reduction on anomaly detection —
  agent credential scope automatically reduced before
  cascade propagates
- Post-cascade NHI audit — verify all credentials exposed
  during cascade have been rotated before agent reactivation

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · EU AI Act Art. 14/15 · ISA/IEC 62443 SR 7.6 (OT)

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

NHI-10 (human use of NHI) is directly relevant — humans who use
agent service accounts to impersonate the agent, or agents whose
identities humans cannot distinguish from human identities, enable
trust exploitation. Attribution is the core NHI control here.

#### NHI mapping

| NHI Entry | How it maps to ASI09 | Control |
|---|---|---|
| NHI-10 Human Use of NHI | Humans using agent credentials — or agents using human credentials — destroys attribution | Strict separation: agent credentials machine-only, human credentials human-only |
| NHI-5 Over-Privileged NHI | Over-privileged agent identity makes its recommendations appear more authoritative to users | Least privilege makes agent capabilities visible and bounded — users understand what the agent can actually do |

#### Mitigations

**Foundational**
- NHI-10: Enforce strict separation between agent credentials
  and human credentials — agent service accounts cannot
  be used by humans, human accounts cannot be used by agents
- Implement clear agent identity disclosure — users must
  see a distinct agent identity, not a human-appearing name

**Hardening**
- NHI-5: Make agent privilege scope visible to users —
  users who understand what an agent can access are less
  susceptible to trust exploitation
- NHI-10: Audit and alert on any human access using agent
  credentials — immediate investigation trigger

**Advanced**
- Cryptographic agent identity attestation — users can
  verify the agent's identity and permission scope
  through a trusted mechanism
- NHI-10: Automated detection of agent identity misuse —
  human session using agent token triggers immediate
  credential revocation and alert

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation & Integrity Attacks
- Other frameworks: AIUC-1 C/F · EU AI Act Art. 50 · NIST AI RMF GV-1.7

---

### ASI10 — Rogue Agents

**Severity:** Critical

A rogue agent is an NHI that has escaped its governance boundaries.
NHI-1 (improper offboarding) is the failure mode when rogue behaviour
is detected but credentials are not revoked — the rogue agent
continues to operate with valid credentials. NHI-7 (long-lived
credentials) is the amplifier — a rogue agent with long-lived tokens
can operate indefinitely post-detection.

#### NHI mapping

| NHI Entry | How it maps to ASI10 | Control |
|---|---|---|
| NHI-1 Improper Offboarding | Rogue agent detected but not offboarded — credentials remain valid | Formal agent offboarding triggered immediately on rogue detection — all credentials revoked |
| NHI-5 Over-Privileged NHI | Rogue agent with excess privilege causes larger blast radius before detection | Least privilege — rogue agent with narrow scope causes less damage before containment |
| NHI-7 Long-Lived Credentials | Long-lived tokens allow rogue agent to operate indefinitely after detection | Short-lived credentials — rogue detection triggers token expiry without requiring manual revocation |

#### Mitigations

**Foundational**
- NHI-1: Formal agent offboarding procedure — kill switch
  activation triggers immediate credential revocation, not
  just session termination
- NHI-5: Least privilege per agent — rogue agent with
  narrow scope causes bounded damage before containment
- NHI-7: Short-lived credentials — rogue detection triggers
  token expiry, not indefinite validity

**Hardening**
- Behavioural baseline monitoring correlated with NHI
  usage — rogue behaviour often manifests as unusual
  credential use patterns before visible output deviation
- NHI-1: Automated offboarding on rogue detection — no
  manual step required for credential revocation on
  anomaly detection trigger

**Advanced**
- Continuous NHI monitoring as rogue detection layer —
  anomalous credential usage alerts before behavioural
  deviation becomes visible in outputs
- NHI-7: Real-time credential revocation infrastructure —
  token invalidation within seconds of rogue detection,
  not minutes or hours
- Post-incident NHI audit — full credential usage review
  for the period before rogue detection to assess
  what access was leveraged

#### Tools

| Tool | Type | Link |
|---|---|---|
| Entro Security | Commercial | https://entro.security |
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| Teleport | Open-source/Commercial | https://goteleport.com |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure, DSGAI16 Endpoint & Browser Overreach
- Other frameworks: AIUC-1 B001/B002/C/E · EU AI Act Art. 14 · ISA/IEC 62443 SR 3.7 (OT)

---

## NHI programme maturity for agentic AI

Use this table to assess your NHI programme maturity for agentic
AI deployments against the Agentic Top 10 risk coverage:

| NHI control area | ASI risks it addresses | Maturity indicator |
|---|---|---|
| Agent identity inventory | ASI03, ASI07, ASI10 | All agent NHIs in a centralised identity register |
| Least privilege enforcement | ASI01, ASI02, ASI08 | All agent credentials scope-reviewed quarterly |
| Short-lived credential issuance | ASI01, ASI06, ASI10 | All agent tokens expire at task completion |
| Secret scanning | ASI03, ASI04, ASI06 | Automated scanning of agent memory, logs, and config |
| Third-party NHI validation | ASI02, ASI04 | Approved tool identity registry maintained |
| Environment isolation | ASI05, ASI08 | Strict credential separation per environment |
| Agent offboarding | ASI10 | Formal offboarding procedure triggered on decommission |
| Human use detection | ASI09 | Automated detection of human access via agent credentials |
| Continuous NHI monitoring | ASI01, ASI08, ASI10 | Real-time anomaly detection on all agent credential usage |

---

## Implementation priority

| Phase | ASI / NHI entries | Action | Rationale |
|---|---|---|---|
| 1 — Do now | ASI03 / NHI-5/6/9 | Least privilege, secret manager, unique identities | Fastest impact on largest attack surface |
| 2 — This sprint | ASI01/02/10 / NHI-7 | Short-lived credentials, rotation | Eliminates persistent access after compromise |
| 3 — This quarter | ASI04/07 / NHI-3/4 | Third-party NHI validation, A2A authentication | Supply chain and communication security |
| 4 — Ongoing | ASI08/10 / NHI-1/10 | Offboarding programme, human use detection, continuous monitoring | Detection and response capability hardening |

---

## References

- [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP AIVSS](https://aivss.owasp.org)
- [AIUC-1 Standard](https://www.aiuc-1.com)
- [SPIFFE / SPIRE — workload identity](https://spiffe.io)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-24 | 2026-Q1 | Initial mapping — ASI01–ASI10 full entries with NHI programme maturity table | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
