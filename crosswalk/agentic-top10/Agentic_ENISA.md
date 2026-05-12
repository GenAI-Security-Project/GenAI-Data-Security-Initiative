<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : ENISA Multilayer Framework for Good Cybersecurity Practices for AI
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 — ENISA Multilayer Framework

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to the [ENISA Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai) —
published by the European Union Agency for Cybersecurity (ENISA) to
support the cybersecurity requirements of the EU AI Act and NIS2 Directive.

---

## Why ENISA for agentic AI security

ENISA's Multilayer Framework is the primary European technical
reference for AI cybersecurity. For agentic deployments, ENISA is
particularly critical because:

**EU AI Act autonomy obligations:** Agentic AI systems frequently
qualify as high-risk AI systems under EU AI Act Annex III — or as
General Purpose AI (GPAI) with systemic risk. Article 14 human
oversight requirements and Article 15 robustness requirements apply
directly to autonomous agent behaviour. ENISA's L2 AI-specific
controls provide the technical implementation guidance for these
Articles.

**NIS2 Directive scope:** Essential entities deploying agentic AI
in operational technology, healthcare, finance, or critical
infrastructure must apply ENISA's L1 baseline controls to the
AI infrastructure and extend to L2 AI-specific controls for the
agentic attack surface. NIS2 Article 23 significant incident
reporting applies when agentic failures cause service disruption.

**Agentic threat surface:** ENISA L2 (AI-specific security) is
the layer that addresses the unique agentic threat surface —
agent goal hijack, tool misuse, credential exposure, inter-agent
communication, and cascading failures all require L2 controls
that go beyond L1 general ICT baseline.

**August 2026 EU AI Act deadline:** For European organisations
deploying agentic AI in high-risk categories, the August 2026
compliance deadline for Article 14 (human oversight) and Article 15
(technical robustness) requirements makes this mapping time-critical.

---

## ENISA framework structure

| Layer | Focus | Agentic security relevance |
|---|---|---|
| L1 — General ICT | Network security, access control, patch management, incident response, supply chain | Agentic infrastructure security — the platform on which agents run |
| L2 — AI-specific | Training data governance, model integrity, adversarial robustness, AI supply chain, AI monitoring | Agentic-specific attack surface — goal hijack, tool misuse, credential abuse, inter-agent comms |
| L3 — Sector-specific | Critical infrastructure, healthcare, finance AI security | Sector-specific agentic deployments in NIS2 essential entity or EU AI Act Annex III high-risk scope |

**Key ENISA security domains for agentic AI:**

| Domain | Abbreviation | Agentic scope |
|---|---|---|
| AI System Integrity | ASI | Agent goal consistency, adversarial robustness, tool permission enforcement |
| Data and Model Security | DMS | Agent memory, context stores, inter-agent data, credential storage |
| Supply Chain Security | SCS | Agent frameworks, tool registries, MCP servers, plugin ecosystems |
| Monitoring and Detection | MON | Agent action monitoring, anomaly detection, cascading failure detection |
| Incident Response | IRS | Agent incident handling, rollback, NIS2 Article 23 reporting |
| Governance and Risk | GOV | Agent governance policy, accountability, human oversight design |

---

## Quick-reference summary

| ID | Name | Severity | Primary ENISA Domains | Layer | Tier |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | ASI, MON, GOV | L1–L2 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | ASI, SCS, MON | L1–L2 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | DMS, GOV, MON | L1–L2 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | SCS, DMS, GOV | L1–L2 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | ASI, MON, L1 | L1–L2 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | DMS, ASI, MON | L2 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | ASI, GOV, MON | L2–L3 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | MON, IRS, GOV | L1–L3 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | GOV, ASI, MON | L2–L3 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | MON, ASI, IRS | L2–L3 | Hardening–Advanced |

---

## Audience tags

- **EU organisation subject to NIS2** — full file, ENISA framework alignment for agentic AI programme
- **EU AI Act compliance lead** — L2 AI-specific controls, Article 14 (human oversight) and Article 15 (robustness) evidence
- **CISO (European enterprise)** — GOV domain entries, agentic risk management alignment
- **Security architect** — ASI, SCS domain entries for agentic system design
- **Security engineer** — ASI, DMS, MON technical control entries
- **Incident responder** — IRS domain entries, NIS2 Article 23 agentic incident assessment
- **OT / critical infrastructure operator** — L3 sector-specific entries, ASI01/ASI02/ASI08 OT amplifiers

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

An attacker redirects agent objectives through direct or indirect
instruction injection. ENISA L2 ASI (AI System Integrity) is the
primary domain — adversarial robustness and goal-consistency
verification are explicit L2 AI-specific controls. For NIS2
essential entities, a successful goal hijack that causes operational
disruption is a candidate significant incident under Article 23.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| AI System Integrity (ASI) | L2 | Adversarial input testing | Agent applications tested against goal hijack before deployment — direct and indirect injection across all input channels validated as part of AI system integrity verification |
| Monitoring and Detection (MON) | L1–L2 | AI-specific monitoring | Runtime monitoring for goal-hijack indicators across all agent input channels — AI-specific anomaly detection for instruction-override patterns |
| Governance and Risk (GOV) | L2 | AI risk management | Goal hijack documented in AI risk register — risk owner, treatment controls, review cadence |
| General ICT — Secure Development | L1 | Secure coding practices | Input validation and context separation as secure development requirements for all agent integrations |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Secure Development: Implement input validation
  as a secure development requirement — all agent
  integrations reviewed for injection resistance before
  deployment
- GOV: Document goal hijack in AI risk register —
  risk owner, treatment controls, review cadence

**Hardening (L2)**
- ASI: Include adversarial goal-hijack testing in
  AI system integrity verification — direct, indirect,
  and multi-turn injection tested before each production
  release across all input channels
- MON: Deploy AI-specific runtime monitoring covering
  goal-hijack indicators — ENISA L2 monitoring practice
  extended to agent goal-state deviation detection

**Advanced (L2–L3)**
- ASI: Implement goal-state verification at the
  framework layer — compare agent's inferred goal
  at each action step against session's authorised intent
- L3 (NIS2 essential entities): Include agent goal
  hijack in significant incident assessment — determine
  whether successful hijack constitutes a reportable
  incident under NIS2 Article 23

#### EU AI Act alignment

Article 14 (human oversight) requires that high-risk AI systems
allow human intervention to override autonomous operation — ENISA
ASI goal-state verification is the technical implementation of
Article 14 for goal hijack scenarios.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| Rebuff | Open-source | https://github.com/protectai/rebuff |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISO 27001 A.8.28 — NIST CSF 2.0 PR.PS-04 — EU AI Act Art. 14/15

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

Agents misuse legitimate tools — calling them with destructive
parameters or in unexpected sequences. ENISA ASI addresses this
through AI system integrity controls on agent tool permission
scope; SCS covers third-party tool and plugin supply chain security.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| AI System Integrity (ASI) | L2 | Agent access control and tool permission | Tool permissions defined per agent role — scope enforced at the framework layer; irreversibility controls prevent unrecoverable actions |
| Supply Chain Security (SCS) | L1–L2 | Tool and plugin supply chain | All tool integrations assessed as supply chain components — integrity verification, vendor security review before integration |
| Monitoring and Detection (MON) | L1–L2 | Tool call monitoring | All agent tool invocations logged — data volumes, destination, and parameter patterns monitored for anomalies |
| General ICT — Access Control | L1 | Least-privilege access | Agent tool credentials issued with least-privilege — no unnecessary tool permissions granted |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Access Control: Issue least-privilege tool
  credentials — only tools necessary for the defined
  agent role granted; unused tools not accessible
- SCS: Maintain tool and plugin SBOM as ICT
  supply chain inventory — every integration
  component inventoried with version, source, hash

**Hardening (L2)**
- ASI: Enforce tool permission scope at framework
  layer — agent cannot invoke tools outside its
  defined role regardless of model instruction
- ASI: Implement irreversibility gates — human
  confirmation required before agent executes
  irreversible tool calls as ENISA ASI control
- MON: Log all tool invocations with parameter
  context — alert on destructive parameter patterns
  or access to out-of-scope destinations

**Advanced (L2)**
- ASI: Red team tool integration points — test
  whether poisoned tool responses can manipulate
  agent behaviour or extract sensitive data
- SCS: Verify tool descriptor integrity before
  each load — cryptographic signature check as
  ENISA supply chain practice

#### EU AI Act alignment

Article 15 technical robustness requirements for high-risk AI
systems include tool permission control — ENISA ASI tool
permission enforcement is the technical implementation of
Article 15 for tool misuse scenarios.

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP Dependency-Check | Open-source | https://github.com/jeremylong/DependencyCheck |
| Semgrep | Open-source | https://github.com/returntocorp/semgrep |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange
- Other frameworks: OWASP ASVS V11 — ISA/IEC 62443 SR 2.2 — EU AI Act Art. 15

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

Agents inherit and cache credentials that attackers exploit for
lateral movement. ENISA DMS (Data and Model Security) covers
credential storage as an AI data asset; GOV addresses agent
identity policy; MON covers credential usage audit trails.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Credential storage security | Agent credentials treated as sensitive AI data assets — stored in secrets manager, never in agent memory or model context |
| Governance and Risk (GOV) | L2 | Agent identity policy | Agent credential lifecycle policy documented in AI governance framework — scope, lifetime, rotation, revocation |
| Monitoring and Detection (MON) | L1–L2 | Credential usage monitoring | All agent credential operations logged — anomaly detection for scope expansion or after-session access |
| General ICT — Access Control | L1 | Identity and access management | Short-lived tokens for all agent interactions — credential TTL enforced at the IAM layer |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Access Control: Issue short-lived tokens for
  all agent interactions — credentials expire at session
  end, no persistent credential caching in agent memory
- L1 Secrets Management: Store all agent secrets in
  a secrets manager — never in environment variables,
  agent memory, or model context

**Hardening (L2)**
- DMS: Classify agent credentials as sensitive AI
  data assets — access controls, encryption, and audit
  logging documented as DMS evidence
- GOV: Document agent credential policy in AI
  governance framework — lifetime, scope, rotation
  interval, revocation procedure
- MON: Log all agent credential operations — anomaly
  detection for scope expansion or after-session access

**Advanced (L2)**
- DMS: Red team agent credential extraction paths —
  test whether credentials appear in outputs, logs,
  memory stores, or tool payloads
- Implement per-task ephemeral credentials — each
  agent task receives a fresh, scoped credential
  that cannot be reused after task completion

#### EU AI Act alignment

Article 15 identity and access control requirements for high-risk
AI systems — ENISA DMS and GOV credential management practices
provide the technical implementation framework.

#### Tools

| Tool | Type | Link |
|---|---|---|
| HashiCorp Vault | Open-source | https://github.com/hashicorp/vault |
| AWS Secrets Manager | Commercial | https://aws.amazon.com/secrets-manager/ |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 — NIST AI RMF GV-1.6 — EU AI Act Art. 15

---

### ASI04 — Agentic Supply Chain

**Severity:** High

Agentic applications depend on third-party frameworks, tool
registries, MCP servers, and model weights. ENISA SCS (Supply
Chain Security) provides the primary domain — agentic supply
chain components require the same security assessment practices
as general ICT supply chain components, extended with L2
AI-specific requirements for model and plugin integrity.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Supply Chain Security (SCS) | L1–L2 | AI supply chain management | Agentic component vendors assessed — agent frameworks, tool registries, MCP servers, model providers all subject to SCS practices |
| Data and Model Security (DMS) | L2 | Model and plugin integrity | Model weight and tool descriptor integrity verification — cryptographic signatures, hash-based baseline |
| Governance and Risk (GOV) | L2 | Third-party AI risk | Vendor risk management extended to AI component suppliers — contractual security obligations documented |
| General ICT — Supply Chain | L1 | ICT supply chain security | Agentic SBOM as software asset inventory — all components inventoried, CVEs monitored |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Supply Chain: Maintain agentic SBOM — every
  component (frameworks, tools, model adapters)
  inventoried with version, source, hash
- L1 Patch Management: Include agentic component
  CVEs in vulnerability management — ML libraries
  and agent framework dependencies scanned on schedule

**Hardening (L2)**
- SCS: Apply ENISA AI supply chain security practices
  to all agentic component vendors — security assessment,
  vulnerability disclosure SLA, provenance documentation
- DMS: Verify model weight and tool descriptor
  integrity before deployment — cryptographic signatures
  as ENISA model integrity practice

**Advanced (L2)**
- SCS: Red team supply chain compromise scenarios —
  test whether tampered components are detected before
  deployment as ENISA supply chain security practice
- GOV: Periodic agentic supply chain audits — verify
  vendors continue to meet security requirements

#### Tools

| Tool | Type | Link |
|---|---|---|
| OWASP Dependency-Check | Open-source | https://github.com/jeremylong/DependencyCheck |
| Syft | Open-source | https://github.com/anchore/syft |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange
- Other frameworks: ISO 27001 A.5.22 — NIST AI RMF MP-5.1 — EU AI Act Art. 9

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

Agents generate and execute code beyond intended scope — enabling
arbitrary command execution, sandbox escape, or destructive
filesystem operations. ENISA L1 General ICT secure development
controls combined with L2 ASI adversarial testing address this
as both an infrastructure hardening and AI system integrity issue.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| AI System Integrity (ASI) | L2 | Code execution scope enforcement | Agent-generated code validated and sandboxed before execution — AI system integrity verification includes code generation scope testing |
| Monitoring and Detection (MON) | L1–L2 | Code execution monitoring | All agent-initiated code execution logged — process spawning, filesystem access, and network calls from agent sandboxes monitored |
| General ICT — Secure Development | L1 | Secure coding and sandboxing | Code execution sandbox as a secure development requirement — agent-generated code never executed in host context |
| General ICT — Network | L1 | Network segmentation | Agent code execution sandboxes network-isolated — no outbound connections to non-approved destinations |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- L1 Secure Development: Implement code execution
  sandbox as a mandatory secure development requirement —
  agent-generated code executed only in isolated
  container with no host filesystem access
- ASI: Include code generation scope testing in AI
  system integrity verification — test whether crafted
  inputs cause execution of out-of-scope commands
- MON: Log all agent code execution with full
  command and environment context — alert on
  syscall patterns indicating sandbox escape attempts

**Advanced (L2)**
- ASI: Red team code execution sandbox — test
  for known container escape techniques as part
  of AI system security testing under ENISA L2
- L1 Network: Isolate code execution environments
  at network layer — no outbound connections except
  to explicitly approved endpoints

#### EU AI Act alignment

Article 15 requires technical robustness for high-risk AI systems —
code execution sandboxing is a direct Article 15 requirement
for agentic systems capable of executing generated code.

#### Tools

| Tool | Type | Link |
|---|---|---|
| gVisor | Open-source | https://github.com/google/gvisor |
| Firecracker | Open-source | https://github.com/firecracker-microvm/firecracker |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: ISA/IEC 62443 SR 3.3 — CWE-78 — EU AI Act Art. 15

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

Attackers corrupt agent memory stores, context windows, or
conversation history to manipulate future agent behaviour.
ENISA DMS (Data and Model Security) covers agent memory as
an AI data asset requiring L2 integrity controls; ASI covers
adversarial robustness testing of agent memory systems.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Data and Model Security (DMS) | L2 | Agent memory security | Agent memory stores classified and protected as sensitive AI data assets — integrity verification, access controls, immutable audit log |
| AI System Integrity (ASI) | L2 | Memory integrity testing | AI system integrity verification includes memory poisoning testing — adversarial inputs designed to corrupt persistent agent state |
| Monitoring and Detection (MON) | L2 | Memory anomaly detection | Agent memory stores monitored for unexpected modifications — drift detection on persistent context |
| General ICT — Data Protection | L1 | Memory store access control | Agent memory stores access-controlled — only the owning agent process has write access |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- DMS: Classify agent memory stores as sensitive AI
  data assets — access controls, encryption, and
  integrity verification documented as DMS evidence
- ASI: Include memory poisoning testing in AI system
  integrity verification — test whether adversarial
  content injected into memory stores affects future
  agent behaviour
- MON: Monitor agent memory stores for unexpected
  modifications — integrity baseline established,
  deviations trigger investigation

**Advanced (L2)**
- DMS: Implement memory store audit log — immutable
  record of all memory read and write operations
  for forensic investigation of poisoning events
- ASI: Red team memory persistence paths — test
  whether injection in one session can corrupt
  behaviour in a subsequent session

#### Tools

| Tool | Type | Link |
|---|---|---|
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| Azure AI Content Safety | Commercial | https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: ENISA DMS L2 — NIST AI RMF MS-3.3 — EU AI Act Art. 10

---

### ASI07 — Insecure Inter-Agent Comms

**Severity:** High

Agents communicate without mutual authentication or message
integrity verification — enabling spoofing, injection, and
lateral movement through the agent ecosystem. ENISA ASI
addresses inter-agent communication security as an L2 AI-specific
concern; GOV establishes the trust model and communication policy.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| AI System Integrity (ASI) | L2 | Inter-agent communication integrity | All inter-agent messages authenticated and integrity-verified — mutual authentication as AI system integrity requirement |
| Governance and Risk (GOV) | L2 | Agent trust policy | Agent-to-agent communication policy documented — which agents may communicate with which, under what conditions, with what data |
| Monitoring and Detection (MON) | L2 | Inter-agent communication monitoring | All agent-to-agent messages logged — anomaly detection for unexpected communication patterns |
| General ICT — Network | L1 | Network access control | Inter-agent communication restricted to approved channels — network segmentation enforces the agent communication policy |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- ASI: Implement mutual authentication for all
  inter-agent communication — certificates or tokens
  as ENISA AI system integrity requirement
- ASI: Enforce message integrity verification —
  agents validate the integrity and provenance of
  messages received from other agents before acting
- GOV: Define and enforce inter-agent communication
  policy — documented in AI governance framework
  with approved communication paths and data scope

**Advanced (L2–L3)**
- MON: Log all inter-agent communication with
  full message context — anomaly detection for
  unexpected agents, unexpected data volumes,
  or requests outside the communication policy
- L3 (NIS2 essential entities): Apply NIS2 network
  security requirements to inter-agent communication
  channels in critical infrastructure deployments

#### EU AI Act alignment

Article 14 human oversight requirements extend to multi-agent
systems — ENISA GOV inter-agent communication policy provides
the governance framework for maintaining human oversight visibility
over agent-to-agent interactions.

#### Tools

| Tool | Type | Link |
|---|---|---|
| SPIFFE/SPIRE | Open-source | https://github.com/spiffe/spire |
| mTLS (cert-manager) | Open-source | https://cert-manager.io |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: ISA/IEC 62443 SR 2.10 — NIST AI RMF GV-1.6 — EU AI Act Art. 14

---

### ASI08 — Cascading Agent Failures

**Severity:** High

Agent failures propagate through multi-agent systems causing
large-scale service disruption. ENISA L1 General ICT business
continuity controls provide the baseline; L2 AI-specific
monitoring and IRS (Incident Response) extend these to cover
AI-specific failure propagation patterns.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Monitoring and Detection (MON) | L1–L2 | Cascading failure detection | Early warning detection of failure propagation across agent ecosystem — AI-specific anomaly detection for cascade signatures |
| Incident Response (IRS) | L1–L2 | AI incident response | AI incident response plan covers cascading agent failures — circuit breaker activation, agent isolation, service recovery procedures |
| Governance and Risk (GOV) | L2 | Resilience risk management | Cascade failure risk documented in AI risk register — blast radius analysis, circuit breaker design, residual risk |
| General ICT — Business Continuity | L1 | Business continuity | Multi-agent deployment covered by BCM — recovery time and recovery point objectives defined per agent tier |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Business Continuity: Include multi-agent
  deployments in BCM — RTO/RPO defined for each
  agent tier, recovery procedures documented
- IRS: Include cascading failure scenarios in
  AI incident response plan — circuit breaker
  activation, agent isolation, and service recovery
  procedures documented with RACI

**Hardening (L2)**
- MON: Deploy cascade failure early warning
  detection — AI-specific monitoring for propagation
  signatures before full service impact
- GOV: Document cascade failure risk in AI risk
  register — blast radius analysis, dependency
  mapping, circuit breaker design documented

**Advanced (L2–L3)**
- IRS: Test cascade failure response annually —
  tabletop exercise and simulation of multi-agent
  failure scenarios documented as IRS evidence
- L3 (NIS2 essential entities): Apply NIS2
  resilience requirements to multi-agent deployments —
  include in NIS2 Article 23 significant incident
  threshold assessment

#### EU AI Act alignment

Article 15 requires robustness for high-risk AI systems — cascade
failure prevention and recovery controls are a direct Article 15
compliance requirement for multi-agent deployments.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Prometheus | Open-source | https://prometheus.io |
| Netflix Hystrix | Open-source | https://github.com/Netflix/Hystrix |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: ISO 27001 A.8.14 — ISA/IEC 62443 SR 7.1 — EU AI Act Art. 15

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

Agents exploit human trust through deceptive outputs — impersonating
authorised sources, manufacturing false urgency, or presenting
AI-generated content as human-authored. ENISA GOV (Governance and
Risk) addresses this through AI transparency and accountability
requirements; ASI covers adversarial behaviour testing.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Governance and Risk (GOV) | L2 | AI transparency and accountability | Users informed when interacting with AI agents — disclosure requirements, impersonation prohibitions, accountability for agent outputs |
| AI System Integrity (ASI) | L2 | Deceptive behaviour testing | AI system integrity testing includes deceptive output scenarios — social engineering, false urgency, impersonation tested before deployment |
| Monitoring and Detection (MON) | L2 | Deceptive behaviour monitoring | Agent outputs monitored for deceptive content patterns — AI-specific detection for impersonation and social engineering indicators |
| General ICT — Governance | L1 | Policy and procedures | Acceptable use policy covers agent interaction design — deceptive design patterns prohibited |

#### Mitigations for ENISA alignment

**Foundational (L1)**
- L1 Governance: Publish acceptable use policy
  prohibiting deceptive agent interaction design —
  AI identity disclosure, impersonation prohibition,
  false urgency prohibition documented
- GOV: Implement AI disclosure requirements —
  users informed when interacting with an AI agent
  at the start of each session

**Hardening (L2)**
- ASI: Include deceptive behaviour testing in AI
  system integrity verification — social engineering
  simulation, impersonation scenarios tested
- GOV: Document accountability for agent outputs —
  named responsible person for each deployed agent
  system, output audit trail maintained

**Advanced (L2–L3)**
- MON: Deploy deceptive content detection on
  agent outputs — alert on impersonation patterns,
  false urgency indicators, or synthetic media
- L3 (NIS2 essential entities, EU AI Act Art. III):
  Apply sector-specific deceptive AI prohibitions —
  healthcare and financial services have additional
  requirements for AI identity disclosure

#### EU AI Act alignment

Article 52 transparency obligations require disclosure when AI
generates content that could mislead users — ENISA GOV transparency
practices are the technical implementation of Article 52 for
agentic interaction design.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Azure AI Content Safety | Commercial | https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety |
| Garak | Open-source | https://github.com/leondz/garak |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation via Data Poisoning
- Other frameworks: ISO 27001 A.5.31 — NIST AI RMF GV-1.6 — EU AI Act Art. 52

---

### ASI10 — Rogue Agents

**Severity:** Critical

Agents operate outside authorised scope — executing tasks
not sanctioned by operators, communicating with unapproved
systems, or persisting across session boundaries. ENISA MON
(Monitoring and Detection) is the primary detection domain;
IRS (Incident Response) covers containment; GOV establishes
the behavioural boundaries that define rogue behaviour.

#### ENISA framework mapping

| Domain | Layer | Practice | How it applies |
|---|---|---|---|
| Monitoring and Detection (MON) | L2 | Rogue agent detection | Continuous monitoring for agents operating outside authorised scope — AI-specific behavioural baselines enable deviation detection |
| Incident Response (IRS) | L2 | Agent containment and rollback | AI incident response plan covers rogue agent scenarios — automated isolation, manual rollback, forensic investigation procedures |
| Governance and Risk (GOV) | L2 | Authorised behaviour scope definition | Authorised behaviour envelope documented per agent role — enables definition of what constitutes rogue behaviour |
| AI System Integrity (ASI) | L2 | Behavioural boundary enforcement | AI system integrity controls enforce authorised behaviour boundaries — runtime enforcement, not just policy statements |

#### Mitigations for ENISA alignment

**Hardening (L2)**
- GOV: Document authorised behaviour envelope
  per agent role — specific permitted actions,
  permitted communication endpoints, permitted
  data access; rogue behaviour defined by exclusion
- MON: Establish behavioural baseline per agent —
  ENISA L2 monitoring practice extended to agent
  behaviour; deviations from baseline trigger
  investigation
- ASI: Implement authorised behaviour enforcement —
  agent actions validated against authorised scope
  at runtime, not just at design time

**Advanced (L2–L3)**
- IRS: Include rogue agent scenarios in AI incident
  response plan — automated isolation triggers,
  rollback procedures, forensic evidence preservation
- MON: Deploy persistent session monitoring —
  detect agents that attempt to maintain state
  across authorised session boundaries
- L3 (NIS2 essential entities): Include rogue
  agent events in NIS2 Article 23 significant
  incident assessment — autonomous agent operating
  outside authorised scope in critical infrastructure
  is a candidate significant incident

#### EU AI Act alignment

Article 14 requires that high-risk AI systems allow human
intervention at all times — rogue agent detection and isolation
are the technical implementation of the Article 14 intervention
capability requirement.

#### Tools

| Tool | Type | Link |
|---|---|---|
| Prometheus | Open-source | https://prometheus.io |
| Falco | Open-source | https://falco.org |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI03 Shadow AI & Unsanctioned Data Flows
- Other frameworks: ISO 27001 A.8.16 — NIST AI RMF MG-2.2 — EU AI Act Art. 14

---

## EU AI Act alignment summary

| Article | Requirement | Relevant ASI entries | ENISA domain |
|---|---|---|---|
| Art. 9 | Risk management system | ASI01–ASI10 (all) | GOV |
| Art. 14 | Human oversight for high-risk AI | ASI01, ASI02, ASI06, ASI09, ASI10 | GOV, ASI |
| Art. 15 | Technical robustness and cybersecurity | ASI01, ASI02, ASI05, ASI07, ASI08 | ASI, MON, IRS |
| Art. 17 | Quality management system | ASI04, ASI08 | SCS, IRS |
| Art. 52 | Transparency obligations | ASI09 | GOV |
| Art. 72 | Post-market monitoring | ASI08, ASI10 | MON, IRS |

---

## Implementation priority

| Priority | ASI IDs | Rationale | ENISA Layer |
|---|---|---|---|
| P1 — Critical, deploy first | ASI01, ASI02, ASI03 | Critical severity — goal hijack, tool misuse, credential abuse | L1–L2 |
| P2 — High, deploy within 90 days | ASI05, ASI04, ASI06 | Code execution, supply chain, memory poisoning | L1–L2 |
| P3 — High, deploy within 180 days | ASI07, ASI08, ASI10 | Inter-agent comms, cascade failures, rogue agents | L2–L3 |
| P4 — Medium, deploy within 1 year | ASI09 | Human-agent trust exploitation | L2–L3 |

---

## References

- [ENISA Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [EU AI Act — Official text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [NIS2 Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555)
- [LLM_ENISA.md](../llm-top10/LLM_ENISA.md) — ENISA × LLM Top 10
- [DSGAI_ENISA.md](../dsgai-2026/DSGAI_ENISA.md) — ENISA × DSGAI 2026

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-27 | Initial release — full ASI01–ASI10 mapping to ENISA Multilayer Framework |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the OWASP GenAI Data Security Initiative.
Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
