<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic AI 2026 (ASI01–ASI10)
  Framework   : FedRAMP AI Overlay (NIST SP 800-53 Rev 5 AI-specific extensions)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative – https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 – FedRAMP AI Overlay

Mapping the [OWASP Top 10 for Agentic AI 2026](https://genai.owasp.org/agentic-ai/)
to the [FedRAMP AI Overlay](https://www.fedramp.gov/) extending
[NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
with AI-specific control enhancements.

FedRAMP (Federal Risk and Authorization Management Program) is the US
government's standardised approach to security authorisation for cloud
services. The AI overlay extends FedRAMP baseline controls with
AI-specific requirements. For agentic AI deployments — where autonomous
agents invoke tools, persist memory across sessions, and orchestrate
multi-agent workflows — the FedRAMP AI overlay provides critical guidance
on securing the expanded attack surface introduced by tool usage, delegated
authority, chained automation, and shared context stores within the federal
authorisation boundary. Organisations deploying agentic AI in FedRAMP
environments must address non-human identity management, agent privilege
controls, cascading automation risk, and supply chain integrity for agent
components.

---

## FedRAMP AI control families

| Family | ID | Purpose |
|---|---|---|
| Access Control | AC | AI agent account management, model access enforcement, agent least privilege |
| Audit and Accountability | AU | AI agent action logging, behaviour monitoring, tool invocation audit trails |
| Security Assessment | CA | AI-specific assessments, agent behaviour drift monitoring, AI red-teaming |
| Configuration Management | CM | Agent configuration versioning, tool manifest controls, capability restrictions |
| Identification and Authentication | IA | Non-human identity for AI agents, agent identifier management |
| Incident Response | IR | AI agent incident handling, cascading failure response |
| Program Management | PM | AI agent risk management strategy, autonomy threat framing |
| Risk Assessment | RA | Agent-specific risk assessment, adversarial agent testing |
| System and Services Acquisition | SA | Agent SDLC, safety by design, third-party agent services |
| System and Communications Protection | SC | Agent API boundaries, inter-agent encryption, memory store protection |
| System and Information Integrity | SI | Adversarial input protection, agent behaviour monitoring, tool output validation |
| Supply Chain Risk Management | SR | Agent supply chain plan, tool and plugin provenance controls |

---

## Quick-reference summary

| ID | Name | Severity | FedRAMP AI Controls | Scope |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijacking | Critical | SI-3, SI-10, CA-8, AU-2 | Both |
| ASI02 | Misconfigured Access Controls | High | AC-3, AC-6, CM-7, AU-2 | Build |
| ASI03 | Privilege Escalation | Critical | AC-6, IA-2, AC-3, IR-4 | Both |
| ASI04 | Supply Chain Compromise | High | SR-2, SR-3, SA-9, SA-3 | Both |
| ASI05 | Uncontrolled Code Execution | Critical | CM-7, SC-7, SI-3, CA-8 | Both |
| ASI06 | Memory Poisoning & Context Confusion | High | SC-28, SI-3, AU-2, RA-5 | Both |
| ASI07 | Lateral Tool Chaining | High | AC-6, CM-7, AC-3, AU-2 | Build |
| ASI08 | Cascading Automation & Failure | High | SC-7, SI-4, IR-4, PM-9 | Both |
| ASI09 | Emerging Agentic Patterns | Medium | CA-7, RA-5, SI-4, AU-6 | Both |
| ASI10 | AI Agent Dependency Failures | Medium | SR-2, SA-9, SI-4, IR-4 | Both |

---

## Audience tags

`developer` `security-engineer` `ml-engineer` `compliance-officer` `ciso` `fedramp-assessor`

- **Developer / ML engineer** – SI and CM controls per entry; secure agent development and configuration
- **Security engineer** – AC, SC, and AU controls; agent access control, boundary protection, and audit
- **FedRAMP assessor** – full file; control traceability and evidence mapping for agentic AI
- **Compliance officer** – full file; FedRAMP AI overlay alignment for autonomous systems
- **CISO** – PM and RA entries; agent risk strategy and governance

---

## Detailed mappings

---

### ASI01 – Agent Goal Hijacking

**Severity:** Critical

Adversaries manipulate agent goals through direct or indirect prompt
injection, context manipulation, or tool output poisoning, causing the
agent to pursue attacker-defined objectives while appearing to function
normally. FedRAMP AI overlay addresses this through malicious code
protection extended to adversarial agent inputs (SI-3), input validation
for agent prompts and context (SI-10), penetration testing covering agent
hijacking (CA-8), and logging of all agent actions (AU-2).

**Real-world references:**
- EchoLeak (2025) – indirect prompt injection hijacked Microsoft 365
  Copilot agent goals via email content
- Academic research demonstrating agent goal manipulation through
  poisoned tool outputs in multi-step workflows

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Malicious Code Protection — adversarial agent inputs | SI-3 | SI | Extend malicious code protection to detect and block adversarial inputs targeting agent goal manipulation including injection through tool outputs and context stores |
| Information Input Validation — agent context validation | SI-10 | SI | Validate all inputs to agent systems including user prompts, tool outputs, memory retrievals, and inter-agent messages; enforce structural separation of instructions and data |
| Penetration Testing — agent hijacking testing | CA-8 | CA | Include agent goal hijacking in penetration testing scope; cover injection through all input channels — user prompts, tool outputs, memory stores, and inter-agent communication |
| Event Logging — agent action audit trail | AU-2 | AU | Log all agent actions, goal interpretations, tool invocations, and decision points with sufficient detail to detect goal hijacking in post-incident analysis |

#### Mitigations

**Foundational**
- SI-10: Implement input validation on all channels feeding agent
  context — user prompts, tool outputs, memory retrievals, inter-agent
  messages; enforce structural separation between instructions and data
- SI-3: Extend malicious input detection to cover adversarial patterns
  targeting agent goal manipulation; deploy as a pre-processing layer
- AU-2: Log all agent actions with goal context, tool invocations, and
  decision rationale; retain per FedRAMP requirements

**Hardening**
- CA-8: Include agent goal hijacking in penetration testing; cover all
  input channels including tool output poisoning and memory injection
- SI-3: Deploy real-time goal consistency monitoring; alert when agent
  behaviour deviates from defined objectives
- Apply privilege separation; bound the impact of goal hijacking by
  restricting available tools and actions

**Advanced**
- CA-8: Conduct structured red-team exercises targeting goal hijacking
  through multi-step tool chains and inter-agent communication
- SI-10: Implement formal goal verification at each agent decision
  point; cross-check planned actions against defined objectives
- AU-2: Integrate agent action logs into FedRAMP continuous monitoring;
  automate detection of goal drift patterns

#### Tools

| Tool | Type | Link |
|---|---|---|
| Garak | Open-source | https://github.com/leondz/garak |
| PyRIT | Open-source | https://github.com/Azure/PyRIT |
| LLM Guard | Open-source | https://github.com/protectai/llm-guard |
| LangSmith | Commercial | https://smith.langchain.com |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection
- DSGAI 2026: DSGAI01 Sensitive Data Leakage, DSGAI12 Unsafe NL Data Gateways
- Other frameworks: MITRE ATLAS AML.T0051 – SP 800-218A PW.2.1-PS – NIST CSF 2.0 PR.AC-5

---

### ASI02 – Misconfigured Access Controls

**Severity:** High

Agent systems deployed with overly permissive access to tools, data stores,
APIs, or other agents enable unintended actions and data exposure. FedRAMP
AI overlay addresses this through access enforcement on agent resources
(AC-3), least privilege for agent permissions (AC-6), least functionality
restricting agent capabilities (CM-7), and audit logging of access
decisions (AU-2).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Access Enforcement — agent resource access | AC-3 | AC | Enforce role-based access control on all agent resources — tools, data stores, APIs, and inter-agent communication channels; deny by default |
| Least Privilege — agent permissions | AC-6 | AC | Enforce least privilege for all agent permissions; restrict tool access, data store access, and API scope to minimum necessary per agent role |
| Least Functionality — agent capability restrictions | CM-7 | CM | Restrict agents to minimum necessary capabilities; disable unused tools, APIs, and action types; enforce capability restrictions in agent configuration |
| Event Logging — access decision logging | AU-2 | AU | Log all agent access decisions — permitted and denied — with sufficient detail for access control review and incident investigation |

#### Mitigations

**Foundational**
- AC-6: Define explicit least privilege policies for each agent; document
  maximum permitted tool access, data store access, and API scope
- AC-3: Implement role-based access control on all agent resources;
  deny access by default; require explicit grants
- CM-7: Disable all agent capabilities not explicitly required; maintain
  a capability manifest per agent deployment

**Hardening**
- AU-2: Log all access decisions with full context; review access
  patterns for over-privileging indicators
- AC-3: Implement just-in-time access for agent tool invocations;
  grant access only for the duration of the specific task
- CM-7: Review agent capability manifests at each FedRAMP annual
  assessment; remove unused permissions

**Advanced**
- AC-6: Implement dynamic privilege adjustment based on agent context
  and risk level; escalate to human approval for high-risk operations
- AC-3: Deploy policy-as-code for agent access control; automate
  enforcement and audit of access policies
- AU-2: Integrate access decision logs into FedRAMP continuous
  monitoring; automate detection of access control drift

#### Tools

| Tool | Type | Link |
|---|---|---|
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| HashiCorp Vault | Commercial | https://www.vaultproject.io |
| AWS IAM / Azure RBAC | Commercial | https://aws.amazon.com/iam/ |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Data Lineage Fragmentation
- Other frameworks: SP 800-218A PW.1.1-PS – NIST CSF 2.0 PR.AC-4 – CIS Controls 6

---

### ASI03 – Privilege Escalation

**Severity:** Critical

Agents exploit misconfigured permissions, tool chaining, or inter-agent
trust to escalate privileges beyond intended scope — accessing sensitive
data, invoking restricted tools, or taking administrative actions. FedRAMP
AI overlay addresses this through least privilege enforcement (AC-6),
non-human identity authentication for agents (IA-2), access enforcement
at tool boundaries (AC-3), and incident handling for escalation events (IR-4).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Least Privilege — escalation prevention | AC-6 | AC | Enforce least privilege with explicit privilege ceilings per agent; prevent accumulation of permissions through tool chaining or inter-agent delegation |
| Identification and Authentication — agent NHI | IA-2 | IA | Assign unique non-human identities to each AI agent; authenticate agent identity at each tool invocation and inter-agent communication boundary |
| Access Enforcement — tool boundary enforcement | AC-3 | AC | Enforce access control at every tool invocation boundary; validate agent identity and authorisation for each requested action regardless of calling context |
| Incident Handling — escalation incident response | IR-4 | IR | Define incident handling procedures for agent privilege escalation events; include automated containment, privilege revocation, and forensic investigation |

#### Mitigations

**Foundational**
- AC-6: Define explicit privilege ceilings per agent; prevent privilege
  accumulation through chained operations or delegated authority
- IA-2: Assign unique non-human identities to each agent; authenticate
  at every tool invocation and inter-agent boundary
- AC-3: Enforce access control at each tool boundary independently;
  never inherit permissions from calling agent context

**Hardening**
- IR-4: Define automated containment procedures for detected privilege
  escalation; include privilege revocation and session termination
- AC-6: Implement privilege decay; agent permissions expire after
  defined duration and must be re-authorised
- IA-2: Implement mutual authentication between agents in multi-agent
  workflows; verify identity at each delegation point

**Advanced**
- AC-3: Deploy formal access control verification; prove that no
  sequence of tool invocations can exceed the defined privilege ceiling
- IR-4: Conduct tabletop exercises for agent privilege escalation
  scenarios; test containment and response procedures
- IA-2: Implement attestation-based agent identity with hardware-backed
  credentials where feasible

#### Tools

| Tool | Type | Link |
|---|---|---|
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| SPIFFE/SPIRE | Open-source | https://spiffe.io |
| HashiCorp Vault | Commercial | https://www.vaultproject.io |
| CyberArk | Commercial | https://www.cyberark.com |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI08 Data Leakage & Exposure
- Other frameworks: SP 800-218A PW.1.1-PS – MITRE ATLAS AML.T0015 – CWE-269

---

### ASI04 – Supply Chain Compromise

**Severity:** High

Agentic AI systems depend on third-party tools, plugins, MCP servers,
model weights, and agent frameworks — any of which can be compromised.
FedRAMP AI overlay addresses this through supply chain planning (SR-2),
supply chain controls and provenance verification (SR-3), external
services controls for third-party agent components (SA-9), and secure
development lifecycle for agent systems (SA-3).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Supply Chain Risk Management Plan — agent components | SR-2 | SR | Include all agent components — tools, plugins, MCP servers, model weights, and agent frameworks — in the supply chain risk management plan |
| Supply Chain Controls — agent component provenance | SR-3 | SR | Verify integrity and provenance of all agent supply chain components using cryptographic signatures, checksums, and attestation before deployment |
| External Information System Services — third-party agent services | SA-9 | SA | Require third-party agent tool and plugin providers to meet FedRAMP requirements; establish SLAs for security, availability, and incident notification |
| System Development Life Cycle — agent SDLC | SA-3 | SA | Integrate agent-specific security activities into the SDLC — tool integration review, privilege analysis, and adversarial testing at each lifecycle phase |

#### Mitigations

**Foundational**
- SR-2: Establish an approved sources policy for agent components;
  tools, plugins, MCP servers, and frameworks must come from vetted
  sources with documented provenance
- SR-3: Verify cryptographic signatures for all agent components before
  deployment; maintain an agent component SBOM
- SA-9: Require FedRAMP authorisation or equivalent for third-party
  agent service providers

**Hardening**
- SA-3: Integrate agent security review into the SDLC; gate deployments
  on security sign-off for all new tool integrations
- SR-3: Implement automated supply chain integrity verification in
  CI/CD; block deployment on verification failure
- SA-9: Include AI-specific security requirements in third-party
  agent service agreements

**Advanced**
- SR-2: Conduct backdoor detection on agent tools and plugins from
  third-party providers; test for malicious behaviour in sandbox
- SA-9: Include agent provider security posture in FedRAMP continuous
  monitoring; reassess on significant change
- Extend agent SBOM to cover runtime dynamic components — MCP servers
  and tools fetched at execution time

#### Tools

| Tool | Type | Link |
|---|---|---|
| CycloneDX | Open-source | https://cyclonedx.org |
| ModelScan | Open-source | https://github.com/protectai/modelscan |
| Sigstore | Open-source | https://www.sigstore.dev |
| OWASP Dependency-Check | Open-source | https://owasp.org/www-project-dependency-check/ |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI19 Third-Party Data Risk
- Other frameworks: MITRE ATLAS AML.T0056 – SP 800-218A PW.4.1-PS – CycloneDX ML SBOM

---

### ASI05 – Uncontrolled Code Execution

**Severity:** Critical

Agents with code execution capabilities run attacker-influenced code —
through prompt injection, tool output manipulation, or supply chain
compromise — leading to system compromise, data exfiltration, or lateral
movement. FedRAMP AI overlay addresses this through least functionality
restricting code execution (CM-7), boundary protection for execution
sandboxes (SC-7), malicious code protection for agent-generated code
(SI-3), and penetration testing of execution boundaries (CA-8).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Least Functionality — code execution restrictions | CM-7 | CM | Restrict agent code execution to minimum necessary scope; enforce sandbox boundaries, disable unnecessary language features, and limit filesystem and network access |
| Boundary Protection — execution sandbox | SC-7 | SC | Enforce strict boundary protection on agent code execution environments; isolate from production systems, restrict network access, and enforce resource limits |
| Malicious Code Protection — agent-generated code | SI-3 | SI | Scan agent-generated code for malicious patterns before execution; detect and block code that attempts filesystem access, network communication, or privilege escalation |
| Penetration Testing — execution boundary testing | CA-8 | CA | Include agent code execution sandbox escape in penetration testing scope; test boundary integrity under adversarial conditions |

#### Mitigations

**Foundational**
- CM-7: Restrict agent code execution to sandboxed environments with
  minimum necessary capabilities; disable filesystem access, network
  communication, and system calls not explicitly required
- SC-7: Deploy agents with code execution in isolated environments;
  enforce network segmentation and resource limits
- SI-3: Implement pre-execution scanning of agent-generated code;
  block execution of code matching malicious patterns

**Hardening**
- CA-8: Include sandbox escape testing in penetration testing; verify
  that agents cannot break out of execution boundaries
- CM-7: Implement allowlisting for permitted code operations; deny
  by default; log all execution attempts
- SC-7: Deploy multi-layer sandbox isolation; enforce at container,
  process, and language runtime levels

**Advanced**
- CA-8: Conduct structured red-team exercises targeting code execution
  through multi-step agent manipulation; test full attack chain
- SI-3: Deploy runtime code analysis during agent execution; detect
  and terminate suspicious operations in real time
- SC-7: Implement formal verification of sandbox boundary integrity;
  prove that no code path can escape the execution environment

#### Tools

| Tool | Type | Link |
|---|---|---|
| gVisor | Open-source | https://gvisor.dev |
| Firecracker | Open-source | https://firecracker-microvm.github.io |
| Semgrep | Open-source | https://semgrep.dev |
| E2B | Open-source | https://e2b.dev |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI08 Data Leakage & Exposure
- Other frameworks: CWE-94 – SP 800-218A PW.5.1-PS – MITRE ATLAS AML.T0015

---

### ASI06 – Memory Poisoning & Context Confusion

**Severity:** High

Adversaries manipulate agent memory stores, context windows, or shared
state to influence future agent decisions. FedRAMP AI overlay addresses
this through protection of information at rest for memory stores (SC-28),
malicious code protection extended to adversarial memory manipulation
(SI-3), audit logging of memory operations (AU-2), and vulnerability
scanning covering memory infrastructure (RA-5).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Protection of Information at Rest — memory store protection | SC-28 | SC | Encrypt agent memory stores and context databases at rest; enforce access controls and integrity verification on all memory read and write operations |
| Malicious Code Protection — adversarial memory detection | SI-3 | SI | Extend malicious content detection to agent memory stores; detect poisoned memories, manipulated context, and adversarial state modifications |
| Event Logging — memory operation audit | AU-2 | AU | Log all agent memory operations — reads, writes, deletions — with sufficient detail to detect poisoning and support forensic investigation |
| Vulnerability Scanning — memory infrastructure | RA-5 | RA | Include agent memory stores, context databases, and shared state infrastructure in vulnerability scanning and security assessment |

#### Mitigations

**Foundational**
- SC-28: Encrypt all agent memory stores at rest; implement access
  controls restricting read/write to authorised agent instances
- AU-2: Log all memory operations with agent identity, operation type,
  and content metadata; retain per FedRAMP requirements
- SI-3: Validate all content before writing to agent memory; reject
  content failing integrity checks

**Hardening**
- SI-3: Deploy anomaly detection on memory writes; flag content
  inconsistent with expected patterns or agent context
- RA-5: Include memory store security in vulnerability assessments;
  test for injection, access control bypass, and cross-agent leakage
- SC-28: Implement memory integrity verification; detect and alert
  on unauthorised modifications to stored context

**Advanced**
- Implement memory provenance tracking; record the source and
  chain of custody for all stored context
- SI-3: Deploy continuous memory store monitoring; detect gradual
  poisoning campaigns across multiple sessions
- SC-28: Include memory store security in FedRAMP annual assessments;
  document memory architecture in SSP

#### Tools

| Tool | Type | Link |
|---|---|---|
| Weaviate | Open-source | https://weaviate.io |
| LangSmith | Commercial | https://smith.langchain.com |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| HashiCorp Vault | Commercial | https://www.vaultproject.io |

#### Cross-references
- LLM Top 10: LLM03 Training Data Poisoning, LLM08 Vector and Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning
- Other frameworks: MITRE ATLAS AML.T0018 – SP 800-218A PS.1.1-PS – CWE-1395

---

### ASI07 – Lateral Tool Chaining

**Severity:** High

Agents exploit tool chaining to combine individually safe operations into
harmful sequences — exfiltrating data, modifying systems, or escalating
privileges through multi-step workflows. FedRAMP AI overlay addresses
this through least privilege on tool access (AC-6), least functionality
restricting tool combinations (CM-7), access enforcement at each tool
boundary (AC-3), and comprehensive tool invocation logging (AU-2).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Least Privilege — tool chain restrictions | AC-6 | AC | Enforce least privilege across tool chains; prevent agents from combining tool invocations that individually are safe but together achieve harmful outcomes |
| Least Functionality — tool combination restrictions | CM-7 | CM | Restrict permitted tool combinations; define allowed tool chains in configuration and deny undefined sequences |
| Access Enforcement — per-tool boundary enforcement | AC-3 | AC | Enforce access control at each tool invocation independently; re-evaluate authorisation at every step in a tool chain regardless of prior approvals |
| Event Logging — tool chain audit trail | AU-2 | AU | Log complete tool chain sequences with full context; enable detection and forensic analysis of harmful tool combination patterns |

#### Mitigations

**Foundational**
- AC-6: Define permitted tool chains per agent role; restrict tool
  combinations to pre-approved sequences
- AC-3: Enforce access control independently at each tool boundary;
  never inherit authorisation from previous tool invocations
- AU-2: Log complete tool chain sequences; include input, output,
  and context at each step

**Hardening**
- CM-7: Implement tool chain allowlisting; deny tool combinations not
  explicitly approved; alert on attempts to invoke undefined sequences
- AC-6: Implement transaction-level authorisation for multi-step
  operations; require explicit approval for tool chains that cross
  security boundaries
- AU-2: Deploy automated detection of anomalous tool chain patterns;
  alert on novel tool combinations

**Advanced**
- AC-3: Deploy formal tool chain analysis; verify that no permitted
  tool combination can achieve outcomes beyond the defined privilege
  ceiling
- CM-7: Implement runtime tool chain policy enforcement; evaluate
  each tool invocation in context of the full chain
- AC-6: Include tool chain security in FedRAMP penetration testing;
  test for harmful combinations specific to your deployment

#### Tools

| Tool | Type | Link |
|---|---|---|
| Open Policy Agent | Open-source | https://www.openpolicyagent.org |
| Guardrails AI | Open-source | https://github.com/guardrails-ai/guardrails |
| LangSmith | Commercial | https://smith.langchain.com |
| NeMo Guardrails | Open-source | https://github.com/NVIDIA/NeMo-Guardrails |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Data Lineage Fragmentation
- Other frameworks: SP 800-218A PW.1.1-PS – MITRE ATLAS AML.T0015 – CWE-269

---

### ASI08 – Cascading Automation & Failure

**Severity:** High

Failures or attacks in one agent propagate through interconnected multi-agent
systems causing cascading disruptions, amplified damage, or system-wide
compromise. FedRAMP AI overlay addresses this through boundary protection
between agents (SC-7), system monitoring for cascade indicators (SI-4),
incident handling for cascading failures (IR-4), and risk management
strategy covering automation risk (PM-9).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Boundary Protection — inter-agent boundaries | SC-7 | SC | Enforce boundary protection between agents in multi-agent systems; prevent uncontrolled propagation of failures or attacks across agent boundaries |
| System Monitoring — cascade detection | SI-4 | SI | Monitor multi-agent systems for cascade indicators — error propagation, resource exhaustion spreading, and anomalous inter-agent communication patterns |
| Incident Handling — cascading failure response | IR-4 | IR | Define incident handling procedures for cascading agent failures; include automated circuit breakers, agent isolation, and multi-agent system shutdown procedures |
| Risk Management Strategy — automation risk | PM-9 | PM | Include cascading automation risk in the organisational risk management strategy; define acceptable multi-agent coupling thresholds and circuit breaker requirements |

#### Mitigations

**Foundational**
- SC-7: Enforce boundaries between agents; prevent direct state sharing
  without validation; implement circuit breakers at agent boundaries
- SI-4: Monitor inter-agent communication for anomalous patterns;
  alert on error propagation and resource exhaustion spreading
- IR-4: Define automated circuit breaker procedures; isolate failing
  agents before cascading failure spreads

**Hardening**
- PM-9: Define maximum acceptable blast radius for agent failures;
  design multi-agent architectures with failure containment
- SC-7: Implement rate limiting on inter-agent communication; prevent
  amplification loops
- IR-4: Conduct tabletop exercises for cascading agent failure
  scenarios; test circuit breaker effectiveness

**Advanced**
- SI-4: Deploy cascade prediction models; identify early indicators
  of cascading failure and trigger preventive isolation
- SC-7: Implement formal failure domain analysis for multi-agent
  systems; prove that failure in any single agent cannot cascade
  beyond defined boundaries
- PM-9: Include cascading automation risk in FedRAMP risk assessment;
  document multi-agent architecture in SSP

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Istio | Open-source | https://istio.io |
| LangSmith | Commercial | https://smith.langchain.com |
| PagerDuty | Commercial | https://www.pagerduty.com |

#### Cross-references
- LLM Top 10: LLM04 Model DoS, LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: SP 800-218A PW.2.1-PS – NIST CSF 2.0 RS.RP-1 – ISA/IEC 62443 SR 7.1

---

### ASI09 – Emerging Agentic Patterns

**Severity:** Medium

Novel agentic architectures — multi-agent orchestration, tool-use planning,
self-reflection loops, and autonomous goal decomposition — introduce
security risks not yet fully characterised. FedRAMP AI overlay addresses
this through continuous monitoring for novel behaviour patterns (CA-7),
vulnerability scanning covering emerging attack surfaces (RA-5), system
monitoring for unexpected agent behaviour (SI-4), and audit review of
agent decisions (AU-6).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Continuous Monitoring — novel pattern detection | CA-7 | CA | Include monitoring for novel agentic behaviour patterns in FedRAMP continuous monitoring; track for unexpected capabilities, emergent behaviours, and architectural drift |
| Vulnerability Scanning — emerging attack surfaces | RA-5 | RA | Include emerging agentic attack surfaces in vulnerability scanning; assess novel architectures for security implications before production deployment |
| System Monitoring — unexpected behaviour detection | SI-4 | SI | Monitor agent systems for unexpected behaviour — novel tool use patterns, unanticipated goal decomposition, and emergent inter-agent coordination |
| Audit Review — agent decision review | AU-6 | AU | Conduct regular audit review of agent decision logs; identify patterns indicative of unexpected capabilities or emergent behaviours requiring security assessment |

#### Mitigations

**Foundational**
- CA-7: Include agentic AI behaviour monitoring in continuous
  monitoring programme; track for capability drift and unexpected
  behaviour patterns
- RA-5: Assess novel agentic architectures for security implications
  before production; document findings in risk assessment
- SI-4: Monitor for unexpected agent behaviours; establish baseline
  behaviour profiles and alert on deviations

**Hardening**
- AU-6: Conduct regular review of agent decision logs; identify
  patterns requiring security assessment; escalate through risk
  governance channels
- CA-7: Establish automated detection for emergent agent capabilities;
  alert when agents exhibit behaviours not in their defined scope
- RA-5: Include emerging agentic attack patterns in vulnerability
  scanning; update scanning rules as new attack techniques are published

**Advanced**
- Participate in AI security research communities; stay current on
  emerging agentic attack techniques and defences
- CA-7: Include emerging agentic pattern risk in FedRAMP annual
  assessment; document novel architectures and their security posture
- SI-4: Deploy advanced behaviour analysis for agentic systems;
  detect subtle capability emergence over time

#### Tools

| Tool | Type | Link |
|---|---|---|
| LangSmith | Commercial | https://smith.langchain.com |
| OpenTelemetry | Open-source | https://opentelemetry.io |
| Garak | Open-source | https://github.com/leondz/garak |
| PyRIT | Open-source | https://github.com/Azure/PyRIT |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI18 Governance Gaps
- Other frameworks: NIST AI RMF MAP 1.5 – SP 800-218A PW.7.2-PS – ISO 42001 A.6.2.6

---

### ASI10 – AI Agent Dependency Failures

**Severity:** Medium

Agents depend on external services — model APIs, tool endpoints, data
sources, and inter-agent communication — whose failure or degradation
causes agent malfunction, incorrect outputs, or service disruption.
FedRAMP AI overlay addresses this through supply chain planning for agent
dependencies (SR-2), external service controls (SA-9), system monitoring
for dependency health (SI-4), and incident handling for dependency
failures (IR-4).

#### FedRAMP AI mapping

| Control | ID | Family | Description |
|---|---|---|---|
| Supply Chain Risk Management Plan — agent dependencies | SR-2 | SR | Include all agent external dependencies — model APIs, tool endpoints, data sources — in supply chain risk management with availability and integrity requirements |
| External Information System Services — agent service dependencies | SA-9 | SA | Require SLAs from agent dependency providers covering availability, performance, security, and incident notification; establish fallback procedures |
| System Monitoring — dependency health monitoring | SI-4 | SI | Monitor agent dependency health in real time — API availability, response latency, error rates; alert on degradation and trigger fallback procedures |
| Incident Handling — dependency failure response | IR-4 | IR | Define incident handling procedures for agent dependency failures; include automated fallback activation, graceful degradation, and service restoration |

#### Mitigations

**Foundational**
- SR-2: Document all agent external dependencies in the supply chain
  plan; assess availability and single-point-of-failure risk
- SA-9: Establish SLAs with dependency providers covering availability,
  performance, and incident notification
- SI-4: Monitor dependency health; alert on availability and
  performance degradation

**Hardening**
- IR-4: Define and test automated fallback procedures for dependency
  failures; include graceful degradation and safe-state transitions
- SA-9: Identify critical agent dependencies; require redundant
  providers for critical services
- SI-4: Include dependency failure scenarios in monitoring; test
  detection and alerting capabilities

**Advanced**
- SR-2: Conduct dependency failure impact analysis; quantify the
  blast radius of each dependency failure on agent system functionality
- IR-4: Include dependency failure in FedRAMP contingency testing;
  verify fallback procedures under realistic conditions
- SA-9: Include dependency provider security posture in FedRAMP
  continuous monitoring

#### Tools

| Tool | Type | Link |
|---|---|---|
| OpenTelemetry | Open-source | https://opentelemetry.io |
| LiteLLM | Open-source | https://github.com/BerriAI/litellm |
| PagerDuty | Commercial | https://www.pagerduty.com |
| Istio | Open-source | https://istio.io |

#### Cross-references
- LLM Top 10: LLM05 Supply Chain Vulnerabilities, LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI19 Third-Party Data Risk
- Other frameworks: SP 800-218A PW.4.1-PS – NIST CSF 2.0 ID.SC-2 – CWE-754

---

## Implementation priority

| Phase | AC / AU / IA | SC / SI / CM | CA / RA / SA / SR / IR / PM |
|---|---|---|---|
| 1 – Now | AC-6 least privilege for ASI02/03/07; IA-2 agent NHI for ASI03; AU-2 action logging for ASI01/02/06 | SI-10 input validation for ASI01; CM-7 capability restrictions for ASI02/05/07 | SR-2 agent supply chain plan for ASI04; IR-4 incident handling for ASI03/08 |
| 2 – This sprint | AC-3 per-tool enforcement for ASI03/07; AU-2 tool chain logging for ASI07 | SI-3 adversarial detection for ASI01/05/06; SC-7 boundaries for ASI05/08; SC-28 memory protection for ASI06 | CA-8 pen testing for ASI01/05; SA-9 third-party controls for ASI04/10 |
| 3 – This quarter | AU-6 agent decision review for ASI09; AC-6 dynamic privilege for ASI03 | SI-4 cascade and behaviour monitoring for ASI08/09/10; CM-7 tool chain policy for ASI07 | CA-7 continuous monitoring for ASI09; PM-9 risk strategy for ASI08; RA-5 scanning for ASI06/09 |
| 4 – Ongoing | Access control reviews; audit log analysis; identity lifecycle management | Continuous monitoring; detection tuning; sandbox integrity verification | Annual FedRAMP assessment; red-team programme; supply chain reassessment |

---

## References

- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [FedRAMP](https://www.fedramp.gov/)
- [OWASP Top 10 for Agentic AI 2026](https://genai.owasp.org/agentic-ai/)
- [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [MITRE ATLAS](https://atlas.mitre.org)
- [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-28 | 2026-Q1 | Initial mapping – ASI01–ASI10 full entries | OWASP GenAI Data Security Initiative |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) –
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
