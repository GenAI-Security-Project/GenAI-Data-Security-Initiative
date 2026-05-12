<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic AI 2026 (ASI01–ASI10)
  Framework   : DORA – Digital Operational Resilience Act (EU Regulation 2022/2554)
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative – https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 – DORA

Mapping the [OWASP Top 10 for Agentic AI 2026](https://genai.owasp.org/agentic-ai/)
to the [Digital Operational Resilience Act (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
(EU Regulation 2022/2554, effective 17 January 2025).

DORA establishes a binding regulatory framework for digital operational
resilience across the EU financial sector. For financial entities deploying
agentic AI systems — where autonomous agents invoke tools, persist memory,
and orchestrate multi-agent workflows — DORA requires that agent-specific
risks are integrated into ICT risk management, incident reporting,
resilience testing, and third-party oversight. Agentic AI introduces
unique challenges: agents can autonomously chain operations, escalate
privileges through tool composition, persist poisoned state across sessions,
and cascade failures through interconnected multi-agent systems. This
mapping enables financial institutions to trace each OWASP Agentic Top 10
risk to specific DORA articles and implement controls satisfying regulatory
obligations for autonomous AI systems.

---

## DORA article groups

| Group | Articles | Purpose |
|---|---|---|
| ICT Risk Management | Art. 5–7 | Governance framework, risk management strategy, policies for ICT including agentic AI systems |
| Identification | Art. 8 | Identification and classification of ICT assets including agents, tools, and memory stores |
| Protection and Prevention | Art. 9 | Security controls for agent systems including access control, sandbox enforcement, and integrity |
| Detection | Art. 10 | Anomaly detection, monitoring, and alerting for agent behaviour and inter-agent communication |
| Response and Recovery | Art. 11 | Incident response, business continuity, and recovery for agent system disruptions |
| Backup Policies | Art. 12 | Backup and restoration of agent systems including memory stores and configuration |
| Learning and Evolving | Art. 13 | Post-incident analysis and continuous improvement for agent security incidents |
| ICT Incident Management | Art. 17–23 | Incident classification, reporting, and communication for agent-related incidents |
| Resilience Testing | Art. 24–27 | Penetration testing, red-teaming, and resilience testing for agentic AI systems |
| Third-Party Risk | Art. 28–44 | Oversight of third-party providers including agent tool vendors and model providers |
| Information Sharing | Art. 45 | Threat intelligence sharing for agentic AI threats |

---

## Quick-reference summary

| ID | Name | Severity | DORA Articles | Scope |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijacking | Critical | Art. 9, Art. 24–27, Art. 10 | Both |
| ASI02 | Misconfigured Access Controls | High | Art. 9, Art. 5–7, Art. 10 | Build |
| ASI03 | Privilege Escalation | Critical | Art. 9, Art. 17–23, Art. 24–27 | Both |
| ASI04 | Supply Chain Compromise | High | Art. 28–44, Art. 8, Art. 5–7 | Both |
| ASI05 | Uncontrolled Code Execution | Critical | Art. 9, Art. 24–27, Art. 17–23 | Both |
| ASI06 | Memory Poisoning & Context Confusion | High | Art. 9, Art. 10, Art. 8 | Both |
| ASI07 | Lateral Tool Chaining | High | Art. 9, Art. 5–7, Art. 24–27 | Build |
| ASI08 | Cascading Automation & Failure | High | Art. 11, Art. 10, Art. 12 | Both |
| ASI09 | Emerging Agentic Patterns | Medium | Art. 5–7, Art. 10, Art. 13 | Both |
| ASI10 | AI Agent Dependency Failures | Medium | Art. 28–44, Art. 11, Art. 12 | Both |

---

## Audience tags

`developer` `security-engineer` `ml-engineer` `compliance-officer` `ciso` `risk-manager`

- **Developer / ML engineer** – Art. 9 and Art. 24–27 entries; protection controls and resilience testing for agents
- **Security engineer** – Art. 9, Art. 10, Art. 17–23 entries; detection, protection, and incident management
- **Risk manager** – Art. 5–7 and Art. 28–44 entries; governance, strategy, and third-party risk for agentic systems
- **Compliance officer** – full file; DORA regulatory traceability for autonomous AI
- **CISO** – Art. 5–7 entries; ICT risk governance and agentic AI strategy

---

## Detailed mappings

---

### ASI01 – Agent Goal Hijacking

**Severity:** Critical

Adversaries manipulate agent goals through direct or indirect prompt
injection, context manipulation, or tool output poisoning, causing the
agent to pursue attacker-defined objectives while appearing to function
normally. DORA requires financial entities to implement protection controls
against adversarial agent manipulation (Art. 9), conduct resilience testing
including agent hijacking scenarios (Art. 24–27), and deploy detection for
goal manipulation indicators (Art. 10).

**Real-world references:**
- EchoLeak (2025) – indirect prompt injection hijacked Microsoft 365
  Copilot agent goals via email content
- Academic research demonstrating agent goal manipulation through
  poisoned tool outputs in multi-step workflows

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — adversarial agent controls | Art. 9 | Protection | Implement security controls to detect and block adversarial inputs targeting agent goal manipulation including injection through tool outputs and context stores |
| Resilience Testing — agent hijacking scenarios | Art. 24–27 | Testing | Include agent goal hijacking in threat-led penetration testing; cover injection through user prompts, tool outputs, memory stores, and inter-agent messages |
| Detection — goal manipulation monitoring | Art. 10 | Detection | Deploy detection mechanisms for agent goal manipulation; monitor for behavioural deviations, unexpected tool invocations, and goal drift indicators |
| Information Sharing — agent attack intelligence | Art. 45 | Sharing | Share agent goal hijacking threat intelligence with sector peers through DORA information sharing arrangements |

#### Mitigations

**Foundational**
- Art. 9: Implement input validation on all channels feeding agent
  context; enforce structural separation between instructions and data
  in agent prompts, tool outputs, and memory retrievals
- Art. 10: Deploy detection for agent goal manipulation; monitor for
  behavioural deviations from defined objectives
- Establish policy that all inputs to financial AI agents are treated
  as potentially adversarial; document in ICT risk framework

**Hardening**
- Art. 24–27: Include agent hijacking in threat-led penetration testing;
  cover all input channels including multi-step tool output poisoning
- Art. 9: Apply privilege separation to bound hijacking impact; restrict
  available tools and actions per agent role
- Art. 10: Deploy real-time goal consistency verification; alert when
  agent behaviour deviates from defined objectives

**Advanced**
- Art. 24–27: Conduct structured red-team exercises targeting goal
  hijacking through multi-agent communication and shared context
- Art. 13: Document hijacking incidents and update protections based
  on post-incident analysis; share lessons across the organisation
- Art. 45: Participate in sector information sharing for agent attack
  patterns and indicators of compromise

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
- Other frameworks: MITRE ATLAS AML.T0051 – FedRAMP SI-10 – SP 800-218A PW.2.1-PS

---

### ASI02 – Misconfigured Access Controls

**Severity:** High

Agent systems deployed with overly permissive access to tools, data stores,
APIs, or other agents enable unintended actions and data exposure. DORA
requires financial entities to implement protection controls for agent
access (Art. 9), maintain governance covering agent permissions (Art. 5–7),
and deploy detection for unauthorised access patterns (Art. 10).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — agent access controls | Art. 9 | Protection | Implement security controls enforcing least privilege on agent tool access, data store access, and API permissions within financial systems |
| ICT Risk Management — agent permission governance | Art. 5–7 | Governance | Include agent access control policies in ICT risk management framework; define acceptable permission scopes per agent role and financial function |
| Detection — unauthorised access detection | Art. 10 | Detection | Monitor agent access patterns for unauthorised tool invocations, data access beyond scope, and permission violations; alert on detection |
| Resilience Testing — access control testing | Art. 24–27 | Testing | Include agent access control bypass in resilience testing; verify that agents cannot exceed defined permission boundaries under adversarial conditions |

#### Mitigations

**Foundational**
- Art. 9: Implement least privilege for all agent tool access; maintain
  a capability manifest per agent deployment; deny access by default
- Art. 5–7: Define agent access control policies in the ICT risk
  management framework; specify maximum permissions per agent role
- Art. 10: Log all agent access decisions; monitor for over-privileging
  indicators and scope violations

**Hardening**
- Art. 24–27: Test agent access controls under adversarial conditions;
  verify permission boundaries hold against manipulation
- Art. 9: Implement just-in-time access for agent tool invocations;
  grant access only for task duration
- Art. 5–7: Include agent access control reviews in management
  reporting; escalate over-privileging findings

**Advanced**
- Deploy policy-as-code for agent access control; automate enforcement
  and audit of access policies
- Art. 9: Implement dynamic privilege adjustment based on agent context
  and risk level
- Art. 10: Integrate access monitoring into continuous resilience
  assessment; detect access control drift over time

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
- Other frameworks: FedRAMP AC-3 – SP 800-218A PW.1.1-PS – CIS Controls 6

---

### ASI03 – Privilege Escalation

**Severity:** Critical

Agents exploit misconfigured permissions, tool chaining, or inter-agent
trust to escalate privileges beyond intended scope. DORA requires financial
entities to implement protection controls preventing escalation (Art. 9),
classify escalation events as ICT incidents (Art. 17–23), and include
escalation scenarios in resilience testing (Art. 24–27).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — escalation prevention controls | Art. 9 | Protection | Implement security controls preventing agent privilege escalation through tool chaining, inter-agent delegation, or permission accumulation |
| ICT Incident Management — escalation incident reporting | Art. 17–23 | Incidents | Classify agent privilege escalation as an ICT-related incident; assess impact on financial systems and report per DORA incident classification criteria |
| Resilience Testing — escalation scenario testing | Art. 24–27 | Testing | Include agent privilege escalation scenarios in threat-led penetration testing; test for escalation through tool chaining and inter-agent trust |
| Detection — escalation detection | Art. 10 | Detection | Deploy detection mechanisms for agent privilege escalation; monitor for permission boundary violations and unexpected privilege accumulation |

#### Mitigations

**Foundational**
- Art. 9: Define explicit privilege ceilings per agent; prevent
  privilege accumulation through chained operations; enforce at each
  tool invocation boundary
- Art. 17–23: Define incident classification criteria for agent
  privilege escalation events; establish reporting procedures
- Art. 10: Monitor for permission boundary violations; alert on
  unexpected privilege levels

**Hardening**
- Art. 24–27: Include privilege escalation in threat-led penetration
  testing; test for escalation through all available tool chains
- Art. 9: Implement privilege decay; agent permissions expire after
  defined duration and must be re-authorised
- Art. 17–23: Include escalation in incident response playbooks;
  define automated containment procedures

**Advanced**
- Art. 9: Deploy formal privilege verification; prove that no sequence
  of tool invocations can exceed the defined privilege ceiling
- Art. 24–27: Conduct advanced escalation testing in multi-agent
  environments; test inter-agent trust exploitation
- Art. 13: Document escalation incidents; update privilege models based
  on post-incident analysis

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
- Other frameworks: FedRAMP AC-6 – SP 800-218A PW.1.1-PS – MITRE ATLAS AML.T0015

---

### ASI04 – Supply Chain Compromise

**Severity:** High

Agentic AI systems depend on third-party tools, plugins, MCP servers,
model weights, and agent frameworks that can be compromised. DORA requires
financial entities to manage third-party ICT service provider risk for
agent components (Art. 28–44), identify all agent supply chain assets
(Art. 8), and maintain governance covering agent supply chain (Art. 5–7).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Third-Party Risk — agent component vendor oversight | Art. 28–44 | Third-Party | Include agent tool vendors, plugin providers, MCP server maintainers, and model providers in third-party ICT risk oversight with due diligence and contractual controls |
| Identification — agent supply chain assets | Art. 8 | Identification | Identify and classify all agent supply chain components — tools, plugins, MCP servers, model weights, frameworks — in the ICT asset inventory with provenance |
| ICT Risk Management — agent supply chain governance | Art. 5–7 | Governance | Include agent supply chain risk in the ICT risk management framework; define policies for agent component sourcing, vetting, and lifecycle management |
| Resilience Testing — supply chain resilience | Art. 24–27 | Testing | Include agent supply chain disruption in resilience testing; test fallback procedures for third-party tool and service failures |

#### Mitigations

**Foundational**
- Art. 28–44: Include all agent tool and component providers in
  third-party risk assessments; establish contractual provisions for
  security, incident notification, and audit rights
- Art. 8: Maintain a complete agent component SBOM; register all
  tools, plugins, and frameworks in the ICT asset inventory
- Art. 5–7: Define approved sources policy for agent components

**Hardening**
- Art. 28–44: Require contractual commitments covering security
  practices, vulnerability notification, and audit rights from agent
  component providers; identify critical providers per DORA criteria
- Art. 8: Implement automated integrity verification in CI/CD; verify
  cryptographic signatures on all agent components
- Art. 24–27: Include vendor failure scenarios in resilience testing

**Advanced**
- Art. 28–44: Conduct on-site assessments of critical agent tool
  providers; assess security posture and incident management
- Art. 5–7: Include agent supply chain in board-level risk reporting;
  monitor concentration risk across agent tool providers
- Art. 13: Document supply chain incidents; update vetting procedures
  based on lessons learned

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
- Other frameworks: MITRE ATLAS AML.T0056 – FedRAMP SR-2 – EBA Outsourcing Guidelines

---

### ASI05 – Uncontrolled Code Execution

**Severity:** Critical

Agents with code execution capabilities run attacker-influenced code leading
to system compromise, data exfiltration, or lateral movement. DORA requires
financial entities to implement protection controls for code execution
boundaries (Art. 9), conduct resilience testing of execution sandboxes
(Art. 24–27), and classify code execution incidents for reporting
(Art. 17–23).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — code execution controls | Art. 9 | Protection | Implement security controls restricting agent code execution — sandboxing, capability restrictions, network isolation, and resource limits |
| Resilience Testing — sandbox escape testing | Art. 24–27 | Testing | Include agent code execution sandbox escape in threat-led penetration testing; test boundary integrity under adversarial conditions |
| ICT Incident Management — code execution incident reporting | Art. 17–23 | Incidents | Classify uncontrolled code execution events as ICT-related incidents; assess impact on financial systems and report per DORA criteria |
| Detection — execution anomaly detection | Art. 10 | Detection | Monitor agent code execution for anomalous patterns — unexpected system calls, network access, filesystem operations; alert on detection |

#### Mitigations

**Foundational**
- Art. 9: Restrict agent code execution to sandboxed environments with
  minimum necessary capabilities; disable filesystem, network, and
  system call access not explicitly required
- Art. 10: Monitor agent code execution for anomalous behaviour;
  alert on unexpected system calls or network access
- Art. 17–23: Define incident classification criteria for uncontrolled
  code execution events

**Hardening**
- Art. 24–27: Include sandbox escape testing in resilience testing;
  verify execution boundaries under adversarial conditions
- Art. 9: Implement multi-layer sandbox isolation; enforce at container,
  process, and language runtime levels
- Art. 9: Implement pre-execution scanning of agent-generated code;
  block malicious patterns

**Advanced**
- Art. 24–27: Conduct advanced red-team exercises targeting code
  execution through multi-step agent manipulation
- Art. 13: Document code execution incidents; update sandbox controls
  based on post-incident analysis
- Art. 9: Implement formal verification of sandbox boundary integrity

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
- Other frameworks: CWE-94 – FedRAMP CM-7 – SP 800-218A PW.5.1-PS

---

### ASI06 – Memory Poisoning & Context Confusion

**Severity:** High

Adversaries manipulate agent memory stores, context windows, or shared
state to influence future agent decisions. DORA requires financial entities
to implement protection controls for agent memory integrity (Art. 9),
deploy detection for memory manipulation (Art. 10), and identify agent
memory stores as ICT assets (Art. 8).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — memory integrity controls | Art. 9 | Protection | Implement security controls protecting agent memory stores from poisoning, tampering, and unauthorised modification; enforce access controls and integrity verification |
| Detection — memory manipulation detection | Art. 10 | Detection | Deploy detection mechanisms for agent memory manipulation; monitor for anomalous writes, content inconsistencies, and cross-session poisoning patterns |
| Identification — memory store assets | Art. 8 | Identification | Register agent memory stores, context databases, and shared state systems in the ICT asset inventory; classify by data sensitivity |
| Learning and Evolving — memory poisoning post-mortem | Art. 13 | Learning | Conduct post-incident analysis for memory poisoning events; trace poisoned content to source and assess impact on agent decisions |

#### Mitigations

**Foundational**
- Art. 9: Encrypt agent memory stores at rest; implement access controls
  restricting read/write to authorised agent instances; validate all
  content before writing to memory
- Art. 8: Register all agent memory stores in the ICT asset inventory;
  classify by sensitivity of stored financial data
- Art. 10: Monitor memory operations for anomalous patterns; alert on
  unexpected bulk writes or content inconsistencies

**Hardening**
- Art. 9: Implement memory integrity verification; detect and alert on
  unauthorised modifications; deploy anomaly detection on writes
- Art. 10: Deploy cross-session poisoning detection; identify patterns
  of gradual memory manipulation across multiple interactions
- Art. 8: Map memory store dependencies; understand how poisoned memory
  can propagate through multi-agent systems

**Advanced**
- Art. 9: Implement memory provenance tracking; record source and chain
  of custody for all stored context
- Art. 13: Establish memory poisoning forensics playbook; procedures for
  isolating poisoned content and assessing decision impact
- Art. 10: Deploy continuous memory integrity monitoring; alert on
  statistical drift in stored content

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
- Other frameworks: MITRE ATLAS AML.T0018 – FedRAMP SC-28 – SP 800-218A PS.1.1-PS

---

### ASI07 – Lateral Tool Chaining

**Severity:** High

Agents exploit tool chaining to combine individually safe operations into
harmful sequences. DORA requires financial entities to implement protection
controls for tool chain boundaries (Art. 9), maintain governance covering
tool composition risk (Art. 5–7), and include tool chaining in resilience
testing (Art. 24–27).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Protection and Prevention — tool chain controls | Art. 9 | Protection | Implement security controls restricting tool chain composition; enforce per-tool access control and define permitted tool sequences for financial agent systems |
| ICT Risk Management — tool composition governance | Art. 5–7 | Governance | Include tool chaining risk in ICT risk management framework; define policies for permitted tool combinations and escalation requirements for novel tool chains |
| Resilience Testing — tool chain testing | Art. 24–27 | Testing | Include lateral tool chaining in resilience testing; test whether agents can combine permitted tools to achieve unauthorised outcomes |
| Detection — tool chain anomaly detection | Art. 10 | Detection | Monitor agent tool invocation sequences for anomalous patterns; alert on novel tool combinations or sequences that cross security boundaries |

#### Mitigations

**Foundational**
- Art. 9: Define permitted tool chains per agent role; enforce access
  control independently at each tool boundary; deny undefined sequences
- Art. 5–7: Include tool chaining risk in ICT risk management; define
  acceptable tool combinations for financial AI agents
- Art. 10: Log complete tool chain sequences; monitor for novel or
  anomalous tool combinations

**Hardening**
- Art. 24–27: Include tool chain testing in resilience testing; verify
  that no permitted tool combination achieves harmful outcomes
- Art. 9: Implement transaction-level authorisation for multi-step
  operations crossing security boundaries
- Art. 10: Deploy automated detection of anomalous tool chain patterns;
  alert on novel combinations

**Advanced**
- Art. 9: Deploy formal tool chain analysis; verify that no permitted
  combination can exceed defined privilege boundaries
- Art. 24–27: Conduct advanced tool chain testing specific to your
  financial AI deployment; cover all production tool combinations
- Art. 5–7: Include tool chain risk in board-level reporting for
  financial AI systems

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
- Other frameworks: FedRAMP AC-6 – SP 800-218A PW.1.1-PS – CWE-269

---

### ASI08 – Cascading Automation & Failure

**Severity:** High

Failures or attacks in one agent propagate through interconnected multi-agent
systems causing cascading disruptions. DORA requires financial entities to
implement response and recovery procedures for cascading failures (Art. 11),
deploy detection for cascade indicators (Art. 10), and maintain backup and
restoration capabilities for agent systems (Art. 12).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Response and Recovery — cascading failure response | Art. 11 | Recovery | Define response and recovery procedures for cascading agent failures; include automated circuit breakers, agent isolation, and multi-agent system safe-state transitions |
| Detection — cascade indicator monitoring | Art. 10 | Detection | Monitor multi-agent systems for cascade indicators — error propagation, resource exhaustion spreading, and anomalous inter-agent communication patterns |
| Backup Policies — agent system continuity | Art. 12 | Backup | Maintain backup configurations, memory snapshots, and fallback agent deployments; enable restoration of agent systems to known-good state |
| ICT Risk Management — cascading risk governance | Art. 5–7 | Governance | Include cascading automation risk in ICT risk management; define acceptable multi-agent coupling thresholds and circuit breaker requirements |

#### Mitigations

**Foundational**
- Art. 11: Define automated circuit breaker procedures for cascading
  failures; isolate failing agents before failure spreads; establish
  safe-state transitions for multi-agent systems
- Art. 10: Monitor inter-agent communication for error propagation
  and resource exhaustion spreading; alert on cascade indicators
- Art. 12: Maintain backup agent configurations and memory snapshots;
  document restoration procedures

**Hardening**
- Art. 5–7: Define maximum acceptable blast radius for agent failures;
  design architectures with failure containment
- Art. 11: Include cascading failure in business continuity testing;
  verify recovery procedures under realistic conditions
- Art. 10: Deploy cascade prediction; identify early indicators and
  trigger preventive isolation

**Advanced**
- Art. 11: Document AI service RTO and RPO per DORA requirements for
  multi-agent systems; test recovery quarterly
- Art. 12: Include agent system backup in DORA business continuity
  testing; verify restoration under production conditions
- Art. 5–7: Include cascading automation risk in board-level reporting

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
- Other frameworks: FedRAMP SC-7 – SP 800-218A PW.2.1-PS – NIST CSF 2.0 RS.RP-1

---

### ASI09 – Emerging Agentic Patterns

**Severity:** Medium

Novel agentic architectures introduce security risks not yet fully
characterised. DORA requires financial entities to maintain governance
covering novel ICT risks (Art. 5–7), deploy detection for unexpected
agent behaviours (Art. 10), and apply lessons learned to evolving agent
security (Art. 13).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| ICT Risk Management — novel agentic risk governance | Art. 5–7 | Governance | Include emerging agentic pattern risks in ICT risk management framework; assess novel architectures for operational resilience implications before deployment |
| Detection — unexpected behaviour monitoring | Art. 10 | Detection | Monitor agent systems for unexpected behaviour — novel tool use patterns, unanticipated goal decomposition, and emergent inter-agent coordination |
| Learning and Evolving — emerging pattern assessment | Art. 13 | Learning | Apply lessons learned from emerging agentic pattern incidents; update governance and controls as new attack techniques and defence approaches emerge |
| Resilience Testing — novel architecture testing | Art. 24–27 | Testing | Include emerging agentic architecture security in resilience testing; assess novel patterns for resilience implications before production deployment |

#### Mitigations

**Foundational**
- Art. 5–7: Include emerging agentic risks in ICT risk management;
  require security assessment before deploying novel agent architectures
- Art. 10: Monitor for unexpected agent behaviours; establish baseline
  behaviour profiles and alert on deviations
- Art. 13: Track emerging agentic attack techniques; update controls
  as new patterns are identified

**Hardening**
- Art. 24–27: Include novel agent architecture testing in resilience
  testing programme; assess security implications before production
- Art. 10: Deploy automated detection for emergent agent capabilities;
  alert on behaviours outside defined scope
- Art. 5–7: Include emerging agentic risks in management risk reporting

**Advanced**
- Participate in AI security research communities; contribute to and
  learn from sector knowledge on agentic AI security
- Art. 13: Establish continuous learning programme for agentic AI
  security; update governance as the field evolves
- Art. 24–27: Conduct advanced resilience testing for emerging patterns
  specific to financial AI deployments

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
- Other frameworks: NIST AI RMF MAP 1.5 – FedRAMP CA-7 – SP 800-218A PW.7.2-PS

---

### ASI10 – AI Agent Dependency Failures

**Severity:** Medium

Agents depend on external services whose failure or degradation causes
agent malfunction, incorrect outputs, or service disruption. DORA requires
financial entities to manage third-party risk for agent dependencies
(Art. 28–44), implement response and recovery for dependency failures
(Art. 11), and maintain backup policies for service continuity (Art. 12).

#### DORA mapping

| Requirement | Article | Group | Description |
|---|---|---|---|
| Third-Party Risk — agent dependency oversight | Art. 28–44 | Third-Party | Include all agent external dependencies — model APIs, tool endpoints, data sources — in third-party ICT risk management with availability and integrity requirements |
| Response and Recovery — dependency failure response | Art. 11 | Recovery | Define response and recovery procedures for agent dependency failures; include fallback activation, graceful degradation, and service restoration |
| Backup Policies — dependency continuity | Art. 12 | Backup | Maintain backup and fallback mechanisms for critical agent dependencies; enable continued operation during provider outages |
| Detection — dependency health monitoring | Art. 10 | Detection | Monitor agent dependency health in real time — API availability, response latency, error rates; alert on degradation and trigger fallback procedures |

#### Mitigations

**Foundational**
- Art. 28–44: Include all agent dependencies in third-party risk
  assessments per DORA requirements; establish contractual SLAs for
  availability, performance, and incident notification
- Art. 11: Define fallback procedures for dependency failures; include
  graceful degradation and safe-state transitions
- Art. 10: Monitor dependency health; alert on availability and
  performance degradation

**Hardening**
- Art. 28–44: Identify critical agent dependencies per DORA criteria;
  require redundant providers for critical services
- Art. 12: Maintain backup mechanisms for critical dependencies; test
  fallback procedures regularly
- Art. 11: Include dependency failure in business continuity testing

**Advanced**
- Art. 28–44: Conduct on-site assessments of critical agent dependency
  providers; assess resilience posture and recovery capabilities
- Art. 12: Include dependency failover in DORA business continuity
  testing; verify under production conditions
- Art. 11: Document dependency failure RTO/RPO; include in regulatory
  reporting

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
- Other frameworks: FedRAMP SA-9 – SP 800-218A PW.4.1-PS – EBA Outsourcing Guidelines

---

## Implementation priority

| Phase | Governance (Art. 5–7) | Protection & Detection (Art. 9–10) | Testing, Incidents & Third-Party (Art. 11–44) |
|---|---|---|---|
| 1 – Now | Include agentic AI in ICT risk framework (ASI02/07/09); agent access policies (ASI02) | Art. 9 access controls for ASI02/03; input validation for ASI01; code execution restrictions for ASI05 | Art. 28–44 agent vendor assessment for ASI04/10; Art. 17–23 incident criteria for ASI03/05 |
| 2 – This sprint | Agent supply chain governance for ASI04; tool chaining policies for ASI07 | Art. 9 memory protection for ASI06; Art. 10 detection for ASI01/06/08; sandbox enforcement for ASI05 | Art. 24–27 agent hijacking testing for ASI01; escalation testing for ASI03; Art. 11 circuit breakers for ASI08 |
| 3 – This quarter | Board-level agentic AI risk reporting; cascading risk governance for ASI08 | Art. 9 comprehensive agent protection; Art. 10 cascade and behaviour monitoring for all entries | Art. 24–27 full agentic resilience testing; Art. 28–44 critical provider assessments; Art. 12 backup testing |
| 4 – Ongoing | Governance framework refresh; emerging pattern assessment (ASI09) | Continuous monitoring; detection tuning; protection control updates | Annual resilience testing; third-party reassessment; Art. 45 information sharing |

---

## References

- [DORA – EU Regulation 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- [EBA DORA Regulatory Technical Standards](https://www.eba.europa.eu/regulation-and-policy/digital-operational-resilience-act-dora)
- [OWASP Top 10 for Agentic AI 2026](https://genai.owasp.org/agentic-ai/)
- [ECB Guide on Outsourcing and ICT Risk](https://www.bankingsupervision.europa.eu/)
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
