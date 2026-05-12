<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic AI 2026 (ASI01–ASI10)
  Framework   : NIST SP 800-218A Secure Software Development Practices for Generative AI and Dual-Use Foundation Models
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative – https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 – NIST SP 800-218A

Mapping the [OWASP Top 10 for Agentic AI 2026](https://genai.owasp.org/agentic-ai/)
to [NIST SP 800-218A: Secure Software Development Practices for Generative AI and Dual-Use Foundation Models](https://doi.org/10.6028/NIST.SP.800-218A.ipd)
(Initial Public Draft, March 2024).

NIST SP 800-218A extends the Secure Software Development Framework (SSDF)
with AI-specific practices covering the full lifecycle of generative AI and
foundation model development — from defining training data requirements and
designing secure ML pipelines, through adversarial testing and supply chain
verification, to vulnerability response and root cause analysis. For agentic
AI deployments — where autonomous agents invoke tools, persist memory across
sessions, and orchestrate multi-agent workflows — SP 800-218A provides
critical guidance on securing the expanded attack surface introduced by tool
usage, delegated authority, chained automation, and shared context stores.
Organisations following SSDF for their conventional software estate can
extend that programme to their agentic AI systems using this mapping. US
federal agencies are directed to align with SP 800-218A under OMB memoranda
referencing the SSDF.

---

## SP 800-218A practice groups

| Group | ID | Purpose |
|---|---|---|
| Produce Well-Secured Software | PW | Security requirements, design, reuse, secure coding, review, and testing across the AI development lifecycle |
| Protect the Software | PS | Protecting model weights, training data, pipeline code, and build artefacts from unauthorised access and tampering |
| Respond to Vulnerabilities | RV | Identifying, assessing, remediating, and analysing AI-specific vulnerabilities including emergent behaviours |

---

## Quick-reference summary

| ID | Name | Severity | SP 800-218A Practices | Scope |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijacking | Critical | PW.2.1-PS, PW.7.2-PS, PW.8.2-PS, RV.1.1-PS | Both |
| ASI02 | Misconfigured Access Controls | High | PW.1.1-PS, PW.2.1-PS, PS.1.1-PS, PW.7.2-PS | Build |
| ASI03 | Privilege Escalation | Critical | PW.1.1-PS, PW.5.1-PS, PS.1.1-PS, RV.1.1-PS | Both |
| ASI04 | Supply Chain Compromise | High | PW.4.1-PS, PS.2.1-PS, PS.3.1-PS, RV.1.1-PS | Both |
| ASI05 | Uncontrolled Code Execution | Critical | PW.2.1-PS, PW.5.1-PS, PW.8.2-PS, PS.1.1-PS | Both |
| ASI06 | Memory Poisoning & Context Confusion | High | PS.1.1-PS, PS.3.1-PS, PW.7.2-PS, RV.3.1-PS | Both |
| ASI07 | Lateral Tool Chaining | High | PW.1.1-PS, PW.2.1-PS, PW.7.2-PS, RV.1.1-PS | Build |
| ASI08 | Cascading Automation & Failure | High | PW.2.1-PS, PW.8.2-PS, RV.2.1-PS, PW.1.1-PS | Both |
| ASI09 | Emerging Agentic Patterns | Medium | PW.7.2-PS, PW.8.2-PS, RV.1.1-PS, RV.3.1-PS | Both |
| ASI10 | AI Agent Dependency Failures | Medium | PW.4.1-PS, PS.2.1-PS, RV.1.1-PS, RV.2.1-PS | Both |

---

## Audience tags

`developer` `security-engineer` `ml-engineer` `compliance-officer` `ciso` `red-teamer`

- **Developer / ML engineer** – PW practices per vulnerability entry; secure coding and testing
- **Security engineer** – PS and RV practices; pipeline protection and vulnerability response
- **Red teamer** – PW.8.2-PS adversarial testing entries for every vulnerability
- **Compliance officer** – full file; SSDF alignment and SP 800-218A traceability
- **CISO** – PW.1 and PW.2 entries; AI security requirements and design governance

---

## Detailed mappings

---

### ASI01 – Agent Goal Hijacking

**Severity:** Critical

Adversaries manipulate agent goals through direct or indirect prompt
injection, context manipulation, or tool output poisoning, causing the agent
to pursue attacker-chosen objectives instead of its intended task.
SP 800-218A addresses this through threat modelling of adversarial inputs
targeting agent goal structures in the design phase (PW.2), output and
behaviour review for goal deviation (PW.7), adversarial red-team testing of
goal manipulation vectors (PW.8), and vulnerability identification
procedures for goal hijacking incidents in production (RV.1).

**Real-world references:**
- EchoLeak (2025) – indirect prompt injection turned Microsoft 365 Copilot
  into a silent exfiltration engine via email content, demonstrating agent
  goal redirection through injected instructions
- MCP tool descriptor injection (2025) – malicious tool descriptions in
  Model Context Protocol servers redirected agent behaviour to attacker
  objectives

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PW.2.1-PS – Design software to meet security requirements | Threat model the agent pipeline for adversarial goal manipulation vectors including direct injection, indirect injection via tool outputs, and context poisoning | Ensures goal integrity is a design-phase requirement for all agentic systems |
| PW.7.2-PS – Review the software for security vulnerabilities | Review agent behaviour for goal deviation — verify that the agent maintains intended objectives under adversarial input conditions | Catches goal manipulation vulnerabilities before production deployment |
| PW.8.2-PS – Test for security vulnerabilities | Conduct adversarial red-team testing against goal hijacking vectors including injection through every data source, tool output, and context channel | Validates goal integrity controls under realistic attack conditions |
| RV.1.1-PS – Identify and confirm vulnerabilities | Establish procedures to identify goal hijacking incidents in production including goal deviation monitoring, triage, and confirmation workflows | Enables rapid detection and response to goal manipulation in live systems |

#### Mitigations

**Foundational**
- PW.2.1-PS: During design, explicitly threat model all channels through
  which an adversary can influence agent goals — user inputs, tool outputs,
  retrieved documents, MCP server responses, shared memory stores — and
  design structural separations between goal context and data context
- Establish a policy that all agent inputs from untrusted sources are treated
  as potentially adversarial; enforce separation of instruction and data
  planes in architecture review gates
- PW.7.2-PS: Include goal deviation scenarios in pre-release agent behaviour
  reviews; assign a reviewer responsible for validating goal integrity under
  adversarial edge cases

**Hardening**
- PW.8.2-PS: Implement a structured red-team testing programme covering
  goal hijacking through direct injection, indirect injection via tool
  outputs and RAG sources, context manipulation, and multi-turn goal
  drift — gate production releases on red-team sign-off
- RV.1.1-PS: Deploy runtime monitoring for goal deviation indicators —
  define escalation and triage procedures for detected goal manipulation
  events; monitor tool invocation patterns for anomalous sequences
- Apply goal anchoring — periodically re-inject the original objective
  during multi-step agent execution to resist gradual goal drift

**Advanced**
- PW.8.2-PS: Extend adversarial testing to cover your specific tool
  descriptors, MCP server schemas, memory stores, and every data source
  that feeds agent context during multi-step execution
- RV.1.1-PS: Integrate goal deviation detection signals into your SIEM;
  automate session termination on high-confidence goal hijacking indicators
- PW.2.1-PS: Document goal integrity threat model outputs as a living SDLC
  artefact; refresh on every new tool integration, memory store addition,
  or agent orchestration change

#### Tools

| Tool | Type | Link |
|---|---|---|
| LAAF (LLM Agent Assessment Framework) | Open-source | https://github.com/OWASP/LAAF |
| Garak | Open-source | https://github.com/leondz/garak |
| PyRIT | Open-source | https://github.com/Azure/PyRIT |
| NIST SP 800-218A | Reference | https://doi.org/10.6028/NIST.SP.800-218A.ipd |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: MITRE ATLAS AML.T0051 – SSDF PW.2 – NIST CSF 2.0 PR.AC-5

---

### ASI02 – Misconfigured Access Controls

**Severity:** High

Agents deployed with overly permissive access to tools, data sources, APIs,
or infrastructure resources can be manipulated to access or modify resources
beyond their intended scope. Misconfigured RBAC, missing tool-level
permission boundaries, and absent tenant isolation expose organisations to
data leakage, unauthorised actions, and lateral movement. SP 800-218A
addresses this through explicit security requirements for capability
constraints (PW.1), threat modelling of access paths (PW.2), protection of
agent configuration artefacts (PS.1), and review of access control
enforcement (PW.7).

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PW.1.1-PS – Define security requirements | Define explicit security requirements specifying the maximum permitted tool access, API scope, data source access, and resource boundaries for each agent deployment | Establishes access control as a mandatory deployment requirement |
| PW.2.1-PS – Design software to meet security requirements | Threat model all agent access paths to tools, data stores, and APIs; design least-privilege tool manifests and enforce tenant isolation by design | Ensures access boundaries are designed before implementation |
| PS.1.1-PS – Protect all code from unauthorised access | Protect agent configuration files, tool manifests, permission policies, and orchestration definitions from unauthorised modification | Prevents tampering with access control configuration |
| PW.7.2-PS – Review the software for security vulnerabilities | Review agent access control enforcement — verify that tool permission manifests, RBAC policies, and tenant isolation boundaries are correctly implemented and cannot be bypassed | Validates access controls before production deployment |

#### Mitigations

**Foundational**
- PW.1.1-PS: Document explicit security requirements for each agent
  deployment defining maximum permitted tool access, API scope, and data
  source boundaries — treat as mandatory deployment requirements reviewed
  before go-live
- PW.2.1-PS: Design a tool permission manifest for every agent — principle
  of least privilege applied to each tool; no tool should have broader
  access than the narrowest capability needed for its specific function
- PS.1.1-PS: Classify agent configuration files and tool manifests as
  sensitive security artefacts; apply version control, access control, and
  change logging

**Hardening**
- PW.7.2-PS: Include access control bypass scenarios in pre-release reviews
  — verify that agents cannot exceed their permission manifest through
  prompt manipulation, tool chaining, or context injection
- Implement runtime enforcement of tool permission manifests independent of
  the model — the enforcement layer must not be bypassable through model
  manipulation
- Log all tool invocations with full parameter capture and requesting agent
  identity; feed into runtime anomaly detection for access pattern violations

**Advanced**
- PW.2.1-PS: Implement formal access control verification — automatically
  validate that deployed agent configurations match approved permission
  manifests in CI/CD before production promotion
- PS.1.1-PS: Implement drift detection on agent access control
  configurations — alert on any deviation from approved baselines
- PW.1.1-PS: Include agent access scope changes in security design reviews;
  any expansion of tool access requires explicit security sign-off and
  threat model update

#### Tools

| Tool | Type | Link |
|---|---|---|
| LAAF (LLM Agent Assessment Framework) | Open-source | https://github.com/OWASP/LAAF |
| Open Policy Agent (OPA) | Open-source | https://www.openpolicyagent.org |
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency, LLM07 System Prompt Leakage
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange, DSGAI08 Non-Compliance & Regulatory Violations
- Other frameworks: AIUC-1 B006 – NIST CSF 2.0 PR.AC-1 – CWE-285

---

### ASI03 – Privilege Escalation

**Severity:** Critical

Agents escalate their own privileges by exploiting weak identity boundaries,
inheriting user credentials through tool integrations, or leveraging
multi-agent delegation to acquire permissions exceeding their intended
authorisation level. In agentic architectures, privilege escalation is
particularly dangerous because agents may chain tool calls that individually
appear authorised but collectively achieve unauthorised access. SP 800-218A
addresses this through security requirements for privilege boundaries (PW.1),
secure coding for credential handling (PW.5), protection of identity and
credential stores (PS.1), and vulnerability monitoring for escalation
incidents (RV.1).

**Real-world references:**
- OAuth token inheritance in agent frameworks (2025) – agents inherited
  user OAuth tokens and used them to access resources beyond agent scope
- Multi-agent delegation exploit (2025) – sub-agents accumulated privileges
  from multiple delegating agents, exceeding any single agent's authorisation

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PW.1.1-PS – Define security requirements | Define explicit privilege boundaries for each agent identity — maximum permitted privilege level, credential scope, and escalation constraints | Establishes privilege boundaries as mandatory requirements |
| PW.5.1-PS – Secure coding practices | Implement secure credential handling — agents must not inherit user credentials, store tokens in context, or pass credentials between agents without explicit authorisation | Prevents credential leakage through agent code paths |
| PS.1.1-PS – Protect all code from unauthorised access | Protect credential stores, identity configurations, and privilege mapping files from unauthorised access and modification | Prevents tampering with privilege boundaries |
| RV.1.1-PS – Identify and confirm vulnerabilities | Establish monitoring and triage procedures for privilege escalation incidents — detect agents operating beyond their assigned privilege level | Enables rapid detection of privilege escalation in production |

#### Mitigations

**Foundational**
- PW.1.1-PS: Define explicit privilege boundaries for every agent identity
  — each agent must have its own credential scope, and privilege levels
  must be documented as mandatory deployment requirements
- PW.5.1-PS: Enforce that agents never inherit user credentials directly;
  implement credential brokering through a dedicated identity service that
  issues scoped, time-limited tokens for each agent operation
- PS.1.1-PS: Protect all credential stores and identity configuration with
  strict access controls; encrypt at rest and in transit; audit all access

**Hardening**
- PW.1.1-PS: Implement privilege attenuation in multi-agent delegation —
  sub-agents must receive equal or lesser privileges than the delegating
  agent; enforce in the orchestration layer, not relying on model judgment
- RV.1.1-PS: Deploy runtime monitoring for privilege escalation indicators
  — agents accessing resources or invoking tools beyond their defined
  privilege level; alert and terminate on detection
- PW.5.1-PS: Conduct code review focused on credential handling in agent
  tool integrations — verify that tokens are scoped, rotated, and never
  persisted in agent memory or context

**Advanced**
- Implement formal privilege verification at every tool invocation — the
  tool execution layer must independently verify that the requesting agent
  has sufficient privilege for the specific operation
- RV.1.1-PS: Integrate privilege escalation detection into your SIEM;
  correlate across agent identity, tool invocations, and resource access
  patterns for multi-step escalation detection
- PW.1.1-PS: Conduct regular privilege audit reviews — verify that deployed
  agent privilege levels match approved baselines; flag and remediate drift

#### Tools

| Tool | Type | Link |
|---|---|---|
| LAAF (LLM Agent Assessment Framework) | Open-source | https://github.com/OWASP/LAAF |
| HashiCorp Vault | Open-source | https://www.vaultproject.io |
| Open Policy Agent (OPA) | Open-source | https://www.openpolicyagent.org |
| Falco | Open-source | https://falco.org |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency, LLM01 Prompt Injection
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange, DSGAI08 Non-Compliance & Regulatory Violations
- Other frameworks: MITRE ATLAS AML.T0015 – CWE-269 – NIST CSF 2.0 PR.AC-4

---

### ASI04 – Supply Chain Compromise

**Severity:** High

Agentic AI systems depend on third-party tools, plugins, MCP servers, model
weights, agent frameworks, and orchestration libraries — any of which can be
compromised to inject backdoors, exfiltrate data, or redirect agent
behaviour. The agentic supply chain extends beyond traditional model and
dataset dependencies to include tool descriptors, agent templates, and
runtime-loaded plugins that execute with agent privileges. SP 800-218A
addresses this through vetting of third-party components (PW.4), integrity
verification of all artefacts (PS.2), secure model and artefact registries
(PS.3), and supply chain vulnerability monitoring (RV.1).

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PW.4.1-PS – Reuse existing well-secured software | Vet all third-party agent components — tools, plugins, MCP servers, model weights, orchestration libraries — for provenance, integrity, and security posture before use | Prevents introduction of compromised components into agent pipelines |
| PS.2.1-PS – Verify software integrity | Verify integrity of all agent artefacts and third-party components using cryptographic signatures and checksums before deployment | Detects tampering in agent supply chain artefacts |
| PS.3.1-PS – Archive and protect software releases | Maintain a secure, versioned registry of all agent components with provenance records; enable auditability and rollback | Ensures traceability and recovery capability for supply chain incidents |
| RV.1.1-PS – Identify and confirm vulnerabilities | Monitor for newly disclosed vulnerabilities in third-party agent components; establish a triage process for AI-specific supply chain disclosures | Enables rapid response to supply chain compromises |

#### Mitigations

**Foundational**
- PW.4.1-PS: Establish an approved sources policy for all agent components
  — tools, plugins, MCP servers, model weights, and libraries must come
  from vetted sources; require security review sign-off before any new
  component enters a production agent pipeline
- Maintain a complete agent SBOM for every production deployment — model,
  tools, plugins, MCP servers, orchestration libraries, and their
  transitive dependencies
- PS.2.1-PS: Verify cryptographic signatures or checksums for all agent
  artefacts before deployment — do not deploy unsigned or unverified
  components

**Hardening**
- PS.3.1-PS: Implement a versioned, access-controlled agent component
  registry; all promoted components must have documented provenance and
  integrity attestation
- RV.1.1-PS: Subscribe to security advisories for all agent framework
  providers, tool vendors, and MCP server maintainers; define triage SLAs
  for supply chain disclosures
- PW.4.1-PS: Scan all third-party libraries in the agent stack using SCA
  tools; extend existing dependency scanning to cover agent-specific
  dependencies including tool descriptors and plugin manifests

**Advanced**
- PW.4.1-PS: Conduct security assessment of MCP servers and tool providers
  before integration — review their access patterns, data handling, and
  update mechanisms for potential supply chain attack vectors
- PS.2.1-PS: Implement automated supply chain integrity verification in
  CI/CD — block deployment on any component whose signature cannot be
  verified or whose provenance cannot be traced
- Extend agent SBOM to cover runtime-loaded components — MCP servers,
  dynamically discovered tools, and plugins fetched at inference time

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |
| Sigstore | Open-source | https://www.sigstore.dev |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI06 Tool, Plugin & Agent Data Exchange
- Other frameworks: SSDF PW.4 – MITRE ATLAS AML.T0056 – CycloneDX ML SBOM

---

### ASI05 – Uncontrolled Code Execution

**Severity:** Critical

Agents with code execution capabilities — code interpreters, shell access,
or dynamic tool generation — can be manipulated to execute arbitrary code
on host systems, escape sandboxes, or modify their own runtime environment.
This is uniquely dangerous in agentic systems where agents may generate and
execute code as part of their normal task completion workflow. SP 800-218A
addresses this through threat modelling of code execution paths (PW.2),
secure coding for execution sandboxing (PW.5), adversarial testing of
sandbox escapes (PW.8), and protection of execution environments (PS.1).

**Real-world references:**
- Code interpreter sandbox escapes (2024-2025) – multiple demonstrations
  of agents escaping sandboxed code execution environments to access host
  file systems and network resources
- Self-modifying agent code (2025) – agents generated code that altered
  their own tool definitions and execution constraints

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PW.2.1-PS – Design software to meet security requirements | Threat model all code execution paths in agent workflows; design sandboxing, resource limits, and execution constraints as explicit security requirements | Ensures code execution boundaries are designed before implementation |
| PW.5.1-PS – Secure coding practices | Implement secure coding for agent code execution — sandbox isolation, input validation for code generation, output filtering, and prevention of self-modification | Prevents code execution vulnerabilities in agent implementation |
| PW.8.2-PS – Test for security vulnerabilities | Conduct adversarial testing targeting code execution — sandbox escapes, resource limit bypasses, self-modification, and host system access through generated code | Validates execution boundary controls under attack conditions |
| PS.1.1-PS – Protect all code from unauthorised access | Protect agent execution environments, sandbox configurations, and runtime constraints from unauthorised modification | Prevents weakening of execution boundaries through configuration tampering |

#### Mitigations

**Foundational**
- PW.2.1-PS: Threat model all code execution capabilities in agent
  workflows — identify every path through which an agent can generate,
  execute, or influence code execution; design mandatory sandboxing for
  each path
- PW.5.1-PS: Enforce strict sandbox isolation for all agent code execution
  — no network access, no host filesystem access, resource limits on CPU,
  memory, and execution time; enforce at the infrastructure level, not
  relying on model compliance
- PS.1.1-PS: Protect sandbox configurations and execution environment
  settings as security artefacts; prevent agents from modifying their own
  execution constraints

**Hardening**
- PW.8.2-PS: Include sandbox escape scenarios in adversarial testing —
  test code generation that attempts to access host resources, modify
  sandbox configuration, or establish network connections
- PW.5.1-PS: Implement allowlisting for code execution — define permitted
  language subsets, library imports, and system calls; block all others by
  default
- Deploy code analysis on agent-generated code before execution — static
  analysis for dangerous patterns, blocked imports, and known escape
  techniques

**Advanced**
- PW.8.2-PS: Conduct formal sandbox escape red team exercises against your
  specific execution environment; document residual risk and required
  compensating controls
- PW.2.1-PS: Implement defence in depth for code execution — multiple
  independent containment layers (container, seccomp, network policy) so
  that no single bypass grants host access
- PS.1.1-PS: Implement runtime integrity monitoring of sandbox
  configurations — alert on any modification to execution constraints
  during agent operation

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| gVisor | Open-source | https://gvisor.dev |
| Firecracker | Open-source | https://firecracker-microvm.github.io |
| Semgrep | Open-source | https://semgrep.dev |

#### Cross-references
- LLM Top 10: LLM02 Insecure Output Handling, LLM01 Prompt Injection
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange, DSGAI05 Data Integrity & Validation Failures
- Other frameworks: CWE-94 – MITRE ATLAS AML.T0015 – NIST CSF 2.0 PR.DS-5

---

### ASI06 – Memory Poisoning & Context Confusion

**Severity:** High

Adversaries corrupt agent memory stores — persistent memory, conversation
history, shared context between agents, or RAG retrieval sources — to
influence future agent behaviour across sessions. In multi-agent systems,
poisoned shared memory can propagate malicious influence across multiple
agents. Context confusion occurs when agents conflate data from different
trust domains within their context window. SP 800-218A addresses this
through protection of memory and context stores (PS.1), versioned memory
snapshots for rollback (PS.3), behaviour review for memory-influenced
anomalies (PW.7), and root cause analysis for poisoning incidents (RV.3).

**Real-world references:**
- Persistent memory poisoning (2025) – adversarial inputs stored in agent
  long-term memory influenced all future sessions for the affected user
- Multi-agent context propagation (2025) – poisoned context from one agent
  propagated through shared memory to corrupt decision-making across an
  entire agent swarm

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PS.1.1-PS – Protect all code from unauthorised access | Protect agent memory stores, context databases, and shared state repositories from unauthorised read, write, and modification; enforce access controls per agent identity | Prevents direct tampering with agent memory and context |
| PS.3.1-PS – Archive and protect software releases | Maintain versioned, integrity-verified snapshots of agent memory and context stores; enable rollback to pre-poisoning states | Ensures recovery capability for memory poisoning incidents |
| PW.7.2-PS – Review the software for security vulnerabilities | Review agent behaviour for memory-influenced anomalies — verify that persistent memory and shared context do not introduce unintended behaviour changes across sessions | Catches memory poisoning effects before they propagate |
| RV.3.1-PS – Analyse root causes | When memory poisoning is detected, conduct forensic analysis to identify the poisoned records, their ingestion source, propagation path, and blast radius across agents | Enables thorough incident response for memory poisoning events |

#### Mitigations

**Foundational**
- PS.1.1-PS: Implement access controls on all agent memory stores — enforce
  per-agent identity isolation; only the owning agent can write to its
  memory, all access logged with full audit trail
- PS.3.1-PS: Implement memory versioning — maintain integrity-verified
  snapshots of agent memory at regular intervals; enable rollback to
  pre-poisoning checkpoints on detection
- PW.7.2-PS: Include memory influence scenarios in pre-release behaviour
  reviews — verify that poisoned memory entries cannot redirect agent
  behaviour outside acceptable bounds

**Hardening**
- PS.1.1-PS: Enforce trust domain separation in agent context — data from
  different trust levels (user input, tool output, system instructions,
  retrieved documents) must be tagged and processed with appropriate trust
  boundaries
- RV.3.1-PS: Establish a memory poisoning forensics playbook — procedures
  for isolating poisoned records, tracing to ingestion source, determining
  propagation to other agents, and measuring influence on agent behaviour
- Implement memory content validation — apply anomaly detection to new
  memory entries before persistence; flag entries inconsistent with
  expected content patterns

**Advanced**
- Apply memory decay and expiration policies — bound the influence of any
  single memory entry over time; implement automatic pruning of aged
  memory that has not been validated
- PW.7.2-PS: Implement continuous memory integrity monitoring — alert on
  statistical distribution changes in memory stores that may indicate
  ongoing poisoning campaigns
- RV.3.1-PS: Build automated memory forensic capability — on detection of
  anomalous agent behaviour, automatically capture memory state, identify
  suspect entries, and correlate with ingestion events

#### Tools

| Tool | Type | Link |
|---|---|---|
| LAAF (LLM Agent Assessment Framework) | Open-source | https://github.com/OWASP/LAAF |
| Garak | Open-source | https://github.com/leondz/garak |
| Weaviate (with RBAC) | Open-source | https://weaviate.io |
| Great Expectations | Open-source | https://greatexpectations.io |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM08 Vector and Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: MITRE ATLAS AML.T0032 – NIST CSF 2.0 PR.DS-8 – ISO 42001 6.1.2

---

### ASI07 – Lateral Tool Chaining

**Severity:** High

Agents chain multiple tool invocations in sequences that individually appear
authorised but collectively achieve unauthorised outcomes — accessing data
across trust boundaries, combining partial capabilities into full exploits,
or using one tool's output to unlock another tool's restricted functionality.
In multi-agent systems, lateral chaining can span agents, with each agent
contributing a legitimate step in an unauthorised workflow. SP 800-218A
addresses this through security requirements for action scope constraints
(PW.1), threat modelling of tool interaction paths (PW.2), behaviour review
for chain-based scope violations (PW.7), and vulnerability monitoring for
chaining incidents (RV.1).

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PW.1.1-PS – Define security requirements | Define explicit security requirements constraining permitted tool invocation sequences and cross-tool data flows for each agent deployment | Establishes chaining constraints as mandatory requirements |
| PW.2.1-PS – Design software to meet security requirements | Threat model tool interaction graphs — identify composite action sequences that could achieve unauthorised outcomes; design controls for chain-level authorisation | Ensures chaining risks are addressed at design time |
| PW.7.2-PS – Review the software for security vulnerabilities | Review agent behaviour for chain-based scope violations — verify that multi-step tool sequences cannot achieve outcomes exceeding individual tool permissions | Catches chaining vulnerabilities before production |
| RV.1.1-PS – Identify and confirm vulnerabilities | Establish monitoring for anomalous tool invocation sequences; define triage procedures for suspected lateral chaining incidents | Enables detection of chaining attacks in production |

#### Mitigations

**Foundational**
- PW.1.1-PS: Define permitted tool invocation sequences as part of agent
  security requirements — document allowed tool chains and explicitly
  prohibit chains that cross trust boundaries or combine capabilities
  into sensitive operations
- PW.2.1-PS: Threat model tool interaction graphs — enumerate composite
  action paths that could achieve sensitive outcomes through individually
  innocuous tool calls; design chain-level authorisation checks
- PW.7.2-PS: Include multi-step chaining scenarios in pre-release reviews
  — verify that no tool sequence can achieve outcomes exceeding individual
  tool permissions

**Hardening**
- Implement chain-aware authorisation — evaluate the cumulative effect of
  tool sequences, not just individual tool calls; enforce at the
  orchestration layer
- RV.1.1-PS: Deploy tool invocation sequence monitoring — detect anomalous
  chain patterns, unusual tool combinations, and sequences that match known
  lateral chaining attack patterns
- Log complete tool chain execution traces with data flow between tools;
  feed into security analytics for chaining pattern detection

**Advanced**
- PW.2.1-PS: Formally specify permitted action graphs — only pre-approved
  tool sequences can execute in production; block any tool chain not in
  the approved set
- Implement cross-agent chain detection in multi-agent deployments — monitor
  for distributed chaining where individual agents each execute one step of
  a combined attack
- RV.1.1-PS: Build automated chain analysis capability — on detection of
  anomalous tool sequences, automatically reconstruct the full chain,
  identify data flows, and assess the composite outcome

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LangSmith | Commercial | https://smith.langchain.com |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency, LLM01 Prompt Injection
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange
- Other frameworks: MITRE ATLAS AML.T0015 – CWE-285 – AIUC-1 B006

---

### ASI08 – Cascading Automation & Failure

**Severity:** High

Autonomous agent workflows amplify errors, hallucinations, or malicious
inputs through cascading automation — a single faulty output from one agent
or tool propagates through downstream agents, triggers additional automated
actions, and escalates into system-wide failures or runaway cost. Without
circuit breakers and human checkpoints, agentic systems can execute hundreds
of automated steps before any human becomes aware of a failure. SP 800-218A
addresses this through resource and availability constraints in design
(PW.2), adversarial testing of cascade failure paths (PW.8), remediation
procedures for automation runaway incidents (RV.2), and security
requirements for automation boundaries (PW.1).

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PW.2.1-PS – Design software to meet security requirements | Design circuit breakers, step limits, cost budgets, and human approval gates as explicit security requirements for all agentic automation workflows | Ensures cascade prevention is a design-phase requirement |
| PW.8.2-PS – Test for security vulnerabilities | Conduct adversarial testing of cascade failure paths — test error propagation, hallucination amplification, and runaway automation scenarios | Validates cascade prevention controls under attack conditions |
| RV.2.1-PS – Assess, prioritise, and remediate vulnerabilities | Define remediation procedures for cascade failure incidents including automatic circuit breaker activation, workflow suspension, cost cap enforcement, and rollback | Enables rapid response to cascading automation failures |
| PW.1.1-PS – Define security requirements | Define explicit requirements for maximum automation depth, step limits, cost budgets, and mandatory human checkpoints for each agent workflow | Establishes automation boundaries as mandatory requirements |

#### Mitigations

**Foundational**
- PW.2.1-PS: Design mandatory circuit breakers for all agentic automation
  workflows — define maximum step counts, execution time limits, cost
  budgets, and error thresholds that trigger automatic workflow suspension
- PW.1.1-PS: Define explicit requirements for human-in-the-loop checkpoints
  — identify decision points in agent workflows where human review is
  mandatory before proceeding; enforce in architecture, not relying on
  model judgment
- Implement per-workflow and per-session cost budgets with automatic
  suspension on breach — alerting alone is insufficient for autonomous
  systems

**Hardening**
- PW.8.2-PS: Include cascade failure scenarios in adversarial testing —
  test error propagation chains, hallucination amplification through
  multi-agent workflows, and cost runaway under adversarial input
  conditions
- RV.2.1-PS: Define and test automated response to cascade indicators —
  workflow suspension, agent isolation, cost circuit breaker activation,
  and stakeholder notification; exercise procedures quarterly
- Implement output validation between agent steps — each agent in a chain
  validates the output of the preceding agent before proceeding; reject
  and escalate on validation failure

**Advanced**
- PW.8.2-PS: Conduct chaos engineering exercises against agentic workflows
  — inject failures, hallucinations, and adversarial tool outputs at
  random points to validate cascade prevention controls
- Implement adaptive circuit breakers with anomaly detection — thresholds
  adjust dynamically based on workflow context and historical patterns
- RV.2.1-PS: Document RTO and RPO for agentic automation services; include
  cascade failure scenarios in your AI incident response plan with specific
  recovery procedures

#### Tools

| Tool | Type | Link |
|---|---|---|
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| LangSmith | Commercial | https://smith.langchain.com |
| Kong Gateway | Open-source | https://github.com/Kong/kong |

#### Cross-references
- LLM Top 10: LLM04 Model DoS, LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: CWE-400 – ISA/IEC 62443 SR 7.1 – NIST SP 800-82 Rev 3

---

### ASI09 – Emerging Agentic Patterns

**Severity:** Medium

Novel agentic AI patterns — self-evolving agents, autonomous tool discovery,
dynamic agent spawning, cross-organisational agent federations, and agents
that modify their own prompts or tool definitions — introduce security risks
that existing frameworks do not fully address. These patterns emerge as
agentic capabilities evolve and can create unpredictable security
implications. SP 800-218A addresses this through behaviour review for
emergent capabilities (PW.7), adversarial testing of novel patterns (PW.8),
vulnerability identification for emergent behaviours (RV.1), and root cause
analysis for incidents involving novel agent capabilities (RV.3).

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PW.7.2-PS – Review the software for security vulnerabilities | Review agent behaviour for emergent capabilities — verify that self-modification, dynamic tool discovery, and autonomous agent spawning do not create unintended security exposures | Catches emergent pattern risks before production |
| PW.8.2-PS – Test for security vulnerabilities | Conduct adversarial testing targeting emerging agentic patterns — self-evolution, prompt self-modification, autonomous tool acquisition, and dynamic agent creation | Validates controls against novel attack surfaces |
| RV.1.1-PS – Identify and confirm vulnerabilities | Establish monitoring for emergent agent behaviours — detect agents acquiring new capabilities, modifying their own definitions, or spawning sub-agents outside approved patterns | Enables detection of emerging risks in production |
| RV.3.1-PS – Analyse root causes | When incidents involve novel agentic patterns, conduct root cause analysis focused on understanding the emergent capability and its security implications | Builds organisational knowledge of emerging agentic risks |

#### Mitigations

**Foundational**
- PW.7.2-PS: Include emergent capability review in pre-release agent
  behaviour assessments — verify that agents cannot self-modify, discover
  new tools, or spawn sub-agents outside explicitly approved patterns
- RV.1.1-PS: Establish baseline agent capability profiles — monitor for
  deviations indicating emergent capabilities or behaviour patterns not
  present in the approved agent definition
- Define a policy requiring security review before deploying any novel
  agentic pattern — self-evolution, autonomous tool discovery, dynamic
  spawning, or cross-organisational federation

**Hardening**
- PW.8.2-PS: Include emerging pattern scenarios in adversarial testing —
  attempt self-modification through prompt manipulation, tool discovery
  through output exploitation, and sub-agent spawning through tool chaining
- RV.3.1-PS: Document all incidents involving unexpected agent behaviour
  with detailed root cause analysis — build an organisational knowledge
  base of emergent pattern risks
- Implement capability constraints at the infrastructure level — agents
  cannot acquire new tool access, modify their own configurations, or
  create new agent instances without explicit platform-level authorisation

**Advanced**
- PW.8.2-PS: Establish a dedicated research and red-team capability
  focused on emerging agentic patterns — proactively identify security
  implications of novel agent architectures before production deployment
- PW.7.2-PS: Implement continuous agent capability monitoring — detect and
  alert on agents exhibiting capabilities beyond their defined profile,
  including emergent tool usage patterns and unexpected inter-agent
  communication
- RV.1.1-PS: Contribute findings from emergent pattern incidents to
  community knowledge bases — collaborate with OWASP and MITRE ATLAS to
  catalogue new agentic attack patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| LangSmith | Commercial | https://smith.langchain.com |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| MITRE ATLAS | Reference | https://atlas.mitre.org |

#### Cross-references
- LLM Top 10: LLM09 Misinformation, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange
- Other frameworks: EU AI Act Art. 13 – MITRE ATLAS – ENISA AI Threat Landscape

---

### ASI10 – AI Agent Dependency Failures

**Severity:** Medium

Agentic systems depend on external services — LLM APIs, tool endpoints, MCP
servers, identity providers, vector databases, and orchestration platforms —
whose unavailability, degradation, or behavioural changes cause agent
failures, incorrect outputs, or security control bypasses. Unlike traditional
software dependencies, agent dependencies may fail in semantically subtle
ways — an LLM API returning degraded output quality or a tool endpoint
returning plausible but incorrect data — that propagate silently through
agent workflows. SP 800-218A addresses this through dependency vetting
(PW.4), dependency integrity verification (PS.2), vulnerability monitoring
for dependency issues (RV.1), and remediation procedures for dependency
failure incidents (RV.2).

#### SP 800-218A mapping

| SP 800-218A Practice | Sub-task | Relevance |
|---|---|---|
| PW.4.1-PS – Reuse existing well-secured software | Vet all external agent dependencies — LLM APIs, tool endpoints, MCP servers, orchestration platforms — for reliability, security posture, and failure mode characteristics before adoption | Prevents adoption of unreliable dependencies |
| PS.2.1-PS – Verify software integrity | Verify that external dependency responses are consistent with expected behaviour — detect API version changes, model swaps, or degraded output quality that could affect agent correctness | Detects dependency degradation and tampering |
| RV.1.1-PS – Identify and confirm vulnerabilities | Monitor all agent dependencies for availability, behavioural consistency, and security posture changes; establish triage procedures for dependency degradation events | Enables rapid detection of dependency failures |
| RV.2.1-PS – Assess, prioritise, and remediate vulnerabilities | Define remediation procedures for dependency failures — graceful degradation, fallback providers, workflow suspension, and stakeholder notification | Ensures operational continuity during dependency outages |

#### Mitigations

**Foundational**
- PW.4.1-PS: Vet all external agent dependencies before adoption — evaluate
  SLA commitments, security posture, failure mode characteristics, and
  historical reliability; maintain an approved dependency registry
- RV.1.1-PS: Implement health monitoring for all agent dependencies —
  availability, latency, and behavioural consistency checks; alert on
  degradation before it impacts agent workflows
- RV.2.1-PS: Define graceful degradation procedures for each critical
  dependency — what the agent does when an LLM API, tool endpoint, or
  identity provider becomes unavailable

**Hardening**
- PS.2.1-PS: Implement dependency output validation — verify that responses
  from external services are consistent with expected schemas, quality
  levels, and behavioural patterns; detect silent degradation
- PW.4.1-PS: Maintain fallback providers for critical dependencies —
  alternative LLM APIs, backup tool endpoints, and redundant identity
  services; test failover procedures quarterly
- RV.2.1-PS: Define and test automated dependency failure response — agent
  workflow suspension, fallback activation, cost protection, and
  stakeholder notification; exercise procedures regularly

**Advanced**
- PS.2.1-PS: Implement continuous dependency behavioural monitoring — detect
  subtle changes in LLM API response patterns, model swaps by providers,
  and tool endpoint behavioural drift that could affect agent correctness
- Build dependency risk profiles for each critical external service —
  document single points of failure, blast radius of outage, and required
  recovery procedures
- RV.1.1-PS: Integrate dependency monitoring into your SIEM; correlate
  dependency health signals with agent behaviour anomalies for early
  detection of dependency-induced failures

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| Grafana | Open-source | https://grafana.com |
| PagerDuty | Commercial | https://www.pagerduty.com |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities, LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures, DSGAI06 Tool, Plugin & Agent Data Exchange
- Other frameworks: CWE-400 – SSDF PW.4 – NIST CSF 2.0 ID.SC

---

## Implementation priority

| Phase | PW – Produce | PS – Protect | RV – Respond |
|---|---|---|---|
| 1 – Now | PW.2.1-PS threat models for ASI01/05/08; PW.1.1-PS requirements for ASI02/03/07 | PS.1.1-PS access controls on agent memory, credentials, and configuration (ASI02/03/06) | RV.1.1-PS monitoring for ASI01/03; triage procedures |
| 2 – This sprint | PW.5.1-PS secure coding for ASI03/05; PW.4.1-PS dependency vetting for ASI04/10 | PS.2.1-PS integrity verification in CI/CD for ASI04/10; PS.3.1-PS agent component registry for ASI04/06 | RV.2.1-PS remediation procedures for ASI08/10 |
| 3 – This quarter | PW.7.2-PS behaviour reviews for all 10 entries; PW.8.2-PS adversarial tests for ASI01/05/08 | PS.3.1-PS versioned registry with rollback for all agent artefacts | RV.3.1-PS root cause playbooks for ASI06/09 |
| 4 – Ongoing | PW.8.2-PS continuous red-team programme; threat model refresh on new tool integrations | Supply chain integrity monitoring; agent SBOM refresh | Production monitoring; incident response exercises |

---

## References

- [NIST SP 800-218A (Initial Public Draft, March 2024)](https://doi.org/10.6028/NIST.SP.800-218A.ipd)
- [NIST SSDF (SP 800-218)](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [OWASP Top 10 for Agentic AI 2026](https://genai.owasp.org/agentic-ai/)
- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [MITRE ATLAS](https://atlas.mitre.org)
- [CycloneDX ML SBOM](https://cyclonedx.org/capabilities/mlbom/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-28 | 2026-Q1 | Initial mapping – ASI01–ASI10 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) –
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
