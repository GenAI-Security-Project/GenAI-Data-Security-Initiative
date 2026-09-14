<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic AI Applications 2026 (ASI01-ASI10)
  Framework   : OWASP AISVS 1.0
  Version     : 2026-Q3
  Maintained by: OWASP GenAI Data Security Initiative - https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# OWASP Top 10 for Agentic AI Applications 2026 × OWASP AISVS 1.0

Mapping the [OWASP Top 10 for Agentic AI Applications 2026](https://genai.owasp.org/resource/agentic-ai-top-10/) to the [OWASP Artificial Intelligence Security Verification Standard 1.0](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/), a technical verification standard of 191 testable requirements across 12 chapters, used by engineers and auditors to verify that a specific AI system implements a control rather than merely documents it.

---

## Why AISVS for this source list

Most frameworks already in this crosswalk answer the question of what an organisation should govern. AISVS answers a different question: given a running AI system, what does an assessor check, and what does a pass look like. Every requirement is written to be independently verifiable and starts with the words Verify that.

That makes this mapping the bridge between a risk in this source list and a concrete test an engineer can run. Where ISO 42001 or NIST AI RMF establish that a control must exist, AISVS states the condition that demonstrates it does. The two are complements, not substitutes, and reading them together turns a control objective into an audit step.

AISVS also assigns each requirement a level from 1 to 3 reflecting implementation difficulty and how situational the control is. That maps cleanly onto the tier model used throughout this crosswalk, so the tier column below carries real information about sequencing rather than a subjective judgement.

---

## AISVS structure

| Chapter | Description | Requirements |
|---|---|---|
| [C1 Training Data Integrity & Traceability](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md) | This chapter addresses protecting the integrity and traceability of training data as it is sourced, handled, and maintained. | 13 |
| [C2 Input Validation](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C02-Input-Validation.md) | This chapter addresses validation of all inputs as a first-line defense against prompt injection, one of the most damaging attacks on AI systems. | 12 |
| [C3 Model Lifecycle Management & Change Control](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md) | This chapter addresses control of model changes so that unauthorized or unsafe modifications cannot reach production. | 15 |
| [C4 Infrastructure, Configuration & Deployment Security](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C04-Infrastructure.md) | This chapter addresses hardening AI-specific infrastructure components against model theft, data leakage, and cross-tenant contamination. | 14 |
| [C5 Access Control & Identity for AI Components & Users](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C05-Access-Control-and-Identity.md) | This chapter addresses access control challenges that AI systems introduce beyond traditional application security. | 11 |
| [C6 Supply Chain Security for Models](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C06-Supply-Chain.md) | This chapter addresses defending against AI supply chain attacks that exploit third-party models, frameworks, or datasets to embed backdoors, bias, or exploitable code. | 7 |
| [C7 Model Behavior, Output Control & Safety Assurance](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C07-Model-Behavior.md) | This chapter addresses constraining, validating, and monitoring model outputs so that unsafe, malformed, or high-risk responses cannot reach users or downstream systems. | 13 |
| [C8 Memory, Embeddings & Vector Database Security](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md) | This chapter addresses securing the embeddings and vector stores that act as semi-persistent and persistent "memory" for AI systems through Retrieval-Augmented Generation (RAG). | 11 |
| [C9 Orchestration & Agentic Security](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md) | This chapter addresses ensuring autonomous and multi-agent systems execute only authorized, intended, and bounded actions. | 34 |
| [C10 Model Context Protocol (MCP) Security](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C10-MCP-Security.md) | This chapter addresses secure discovery, authentication, authorization, transport, and use of MCP-based tool and resource integrations. | 23 |
| [C11 Adversarial Robustness](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C11-Adversarial-Robustness.md) | This chapter addresses keeping AI systems reliable and abuse-resistant when facing evasion, inference, extraction, or poisoning attacks. | 17 |
| [C12 Monitoring, Logging & Anomaly Detection](https://github.com/OWASP/AISVS/tree/main/1.0/en/0x10-C12-Monitoring-and-Logging.md) | This chapter addresses real-time and forensic visibility into what the model and other AI components see, do, and return, so that AI-specific threats can be detected and triaged. | 21 |

Levels map to crosswalk tiers as Level 1 Foundational, Level 2 Hardening, Level 3 Advanced. Where an entry maps to requirements at several levels, the tier column below reports the level most of its requirements sit at.

---

## Quick-reference summary

| ID | Name | Severity | Primary AISVS Controls | Tier | Scope |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | C2.1, C10.4, C8.2, C9.3, C9.2, C12.2 | Hardening | Both |
| ASI02 | Tool Misuse and Exploitation | Critical | C9.5, C9.3, C10.2 | Hardening | Both |
| ASI03 | Identity and Privilege Abuse | Critical | C9.4, C9.5, C5.1, C5.2, C10.2 | Advanced | Both |
| ASI04 | Agentic Supply Chain | High | C10.1, C6.1, C6.2, C9.3, C10.4 | Hardening | Both |
| ASI05 | Unexpected Code Execution | Critical | C9.3, C4.1, C7.1, C9.1, C3.4 | Foundational | Both |
| ASI06 | Memory and Context Poisoning | High | C8.2, C8.1, C12.5, C8.3, C9.4 | Hardening | Both |
| ASI07 | Insecure Inter-Agent Communications | High | C10.3, C9.4, C10.4, C9.5 | Hardening | Both |
| ASI08 | Cascading Agent Failures | Critical | C9.1, C9.6, C9.2, C9.3, C12.3 | Advanced | Both |
| ASI09 | Human-Agent Trust Exploitation | High | C9.2, C9.6, C7.4, C7.2, C12.4 | Hardening | Both |
| ASI10 | Rogue Agents | Critical | C12.1, C12.2, C9.4, C9.6, C9.2, C12.4, C12.5 | Hardening | Both |

---

## Target audience

| Role | Sections to prioritise |
|---|---|
| Security engineer | C2 Input Validation, C9 Orchestration and Agentic Security, C10 MCP Security |
| Developer | C7 Model Behavior and Output Control, C8 Memory and Embeddings, C5 Access Control |
| ML engineer | C1 Training Data, C3 Model Lifecycle, C11 Adversarial Robustness |
| Auditor | The whole standard. Every requirement is written as a verifiable test |
| Compliance and GRC | C1 Training Data, C6 Supply Chain, C12 Monitoring and Logging |
| Red teamer | C2 Input Validation, C11 Adversarial Robustness, C9 Orchestration |

---

## Detailed mappings

---

### ASI01 - Agent Goal Hijack

AISVS addresses goal hijack at both the injection point and the persistence point. C2.1 screens the steering input, C10.4.2 screens tool responses, and C8.2.3 stops unvalidated agent and tool output being written into trusted memory where a hijack would survive the session.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that all inputs that could steer model behavior are treated as untrusted and screened by a prompt injection detection ruleset or classifier,... | [2.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 1. All inputs able to steer model behavior treated as untrusted and screened by an injection classifier, the primary hijack vector |
| Verify that the system enforces an instruction hierarchy in which system and developer messages override user instructions and other untrusted inpu... | [2.1.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 2. Instruction hierarchy keeps the operator goal authoritative over injected instructions |
| Verify that MCP tools/list and tools/call responses are screened for indirect prompt injection before being injected into the model context. | [10.4.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c104-schema-message-and-input-validation) | Level 1. MCP tool responses screened for indirect injection before entering model context, the tool-output hijack path |
| Verify that agent outputs and tool outputs are not automatically written to trusted agent memory without explicit source validation. | [8.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 2. Agent and tool outputs not written to trusted agent memory without explicit source validation, blocking hijack persistence |
| Verify that components processing untrusted data are isolated from tool-calling capabilities, ensuring that compromised data processing cannot trig... | [9.3.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. Components processing untrusted data isolated from tool-calling capability so a hijacked reasoning step cannot act |
| Verify that any self-modification capability (e.g., prompt rewriting, tool-list changes, parameter updates) is restricted by enforceable boundaries. | [9.2.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 2. Self-modification capability such as prompt rewriting, tool-list changes and parameter updates restricted by enforceable boundaries |
| Verify that agentic systems include an AI-augmented review of planned high-risk actions before execution that adds to, and does not replace, the de... | [9.2.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 2. AI-augmented review of planned high-risk actions, added to and not replacing the deterministic policy gate |
| Verify that the system detects and alerts on known jailbreak patterns, prompt injection attempts, and adversarial inputs. | [12.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c122-detection-and-alerting) | Level 1. Detection and alerting on jailbreak patterns, injection attempts and adversarial inputs |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 2.1.3: Verify that all inputs that could steer model behavior are treated as untrusted and screened by a prompt injection detection ruleset or classifier, with flag...
- 10.4.2: Verify that MCP tools/list and tools/call responses are screened for indirect prompt injection before being injected into the model context.
- 12.2.1: Verify that the system detects and alerts on known jailbreak patterns, prompt injection attempts, and adversarial inputs.

**Tier 2 - Short-term (first 30 days):**
- 2.1.6: Verify that the system enforces an instruction hierarchy in which system and developer messages override user instructions and other untrusted inputs, even a...
- 8.2.3: Verify that agent outputs and tool outputs are not automatically written to trusted agent memory without explicit source validation.
- 9.3.5: Verify that components processing untrusted data are isolated from tool-calling capabilities, ensuring that compromised data processing cannot trigger unauth...
- 9.2.5: Verify that any self-modification capability (e.g., prompt rewriting, tool-list changes, parameter updates) is restricted by enforceable boundaries.
- 9.2.6: Verify that agentic systems include an AI-augmented review of planned high-risk actions before execution that adds to, and does not replace, the deterministi...

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: LLM01, LLM06
- Agentic: N/A
- DSGAI: DSGAI01, DSGAI15, DSGAI12, DSGAI02
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### ASI02 - Tool Misuse and Exploitation

AISVS constrains tools declaratively and enforces the declaration. C9.3 requires tool manifests declaring privileges, resource limits and output validation, and requires the runtime to enforce them; C9.5.1 adds parameter-value level authorization so a legitimate tool cannot be called destructively.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that agent actions are authorized against fine-grained policies enforced by the runtime that restrict which tools an agent may invoke, and w... | [9.5.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. Fine-grained runtime policy over which tools may be invoked and which parameter values may be supplied, the direct control for destructive-parameter misuse |
| Verify that each tool/plugin executes in a least-privilege sandbox or is otherwise isolated from model operations. | [9.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Each tool or plugin executes in a least-privilege sandbox or is isolated from model operations |
| Verify that tool outputs are validated against schemas. | [9.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Tool outputs validated against schemas |
| Verify that tool manifests declare required privileges, resource limits, and output validation requirements. | [9.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. Tool manifests declare required privileges, resource limits and output validation requirements |
| Verify that the runtime enforces the privileges, resource limits, and output-validation requirements declared in tool manifests. | [9.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. Runtime enforces the privileges, resource limits and output validation declared in tool manifests |
| Verify that external resources named in model output are verified against an approved allow-list or registry before the agent installs or invokes t... | [9.3.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. External resources named in model output verified against an approved allow-list or registry before install or invocation |
| Verify that MCP servers enforce access control on every tool invocation, validating that the user's access token authorizes both the requested tool... | [10.2.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c102-authentication--authorization) | Level 2. MCP servers enforce access control on every tool invocation, validating both the tool and the specific argument values |
| Verify that policy violations trigger automated tool containment. | [9.3.8](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 3. Policy violations trigger automated tool containment |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 9.3.1: Verify that each tool/plugin executes in a least-privilege sandbox or is otherwise isolated from model operations.
- 9.3.2: Verify that tool outputs are validated against schemas.

**Tier 2 - Short-term (first 30 days):**
- 9.5.1: Verify that agent actions are authorized against fine-grained policies enforced by the runtime that restrict which tools an agent may invoke, and which param...
- 9.3.3: Verify that tool manifests declare required privileges, resource limits, and output validation requirements.
- 9.3.4: Verify that the runtime enforces the privileges, resource limits, and output-validation requirements declared in tool manifests.
- 9.3.7: Verify that external resources named in model output are verified against an approved allow-list or registry before the agent installs or invokes them.
- 10.2.5: Verify that MCP servers enforce access control on every tool invocation, validating that the user's access token authorizes both the requested tool and the s...

**Tier 3 - Strategic:**
- 9.3.8: Verify that policy violations trigger automated tool containment.

#### Cross-references

- LLM Top 10: LLM05, LLM06, LLM07
- Agentic: N/A
- DSGAI: DSGAI06, DSGAI12, DSGAI07, DSGAI08
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### ASI03 - Identity and Privilege Abuse

AISVS makes the agent a first-class principal rather than a credential holder. C9.4.1 requires a unique cryptographic identity per agent instance, C9.5.2 requires a scope-limited user context token enforced at every downstream call, and C10.2 adds OAuth 2.1 token validation on the MCP path.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that each agent instance has a unique cryptographic identity and authenticates as a first-class principal to downstream systems. | [9.4.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c94-agent-and-orchestrator-identity) | Level 2. Each agent instance has a unique cryptographic identity and authenticates as a first-class principal to downstream systems, removing inherited-credential ambiguity |
| Verify that when an agent acts on a user's behalf, the runtime propagates an integrity-protected, scope-limited token that carries the user's autho... | [9.5.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. Integrity-protected scope-limited token carries the user authorization context and is enforced at every downstream call |
| Verify that secrets and credentials required by an agent at runtime are not exposed within the model's observable context, including the context wi... | [9.5.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. Secrets and credentials required at runtime kept out of the model observable context |
| Verify that AI agents in federated or multi-system deployments authenticate using short-lived, minimal-scoped, cryptographically signed tokens. | [5.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c51-authentication) | Level 3. Agents in federated or multi-system deployments authenticate with short-lived, minimal-scoped, cryptographically signed tokens |
| Verify that high-risk AI operations (model deployment, weight export, training data access, production configuration changes) require step-up authe... | [5.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c51-authentication) | Level 3. Step-up authentication for high-risk AI operations including model deployment, weight export, training data access and production configuration change |
| Verify that agent identity credentials rotate on a defined schedule. | [9.4.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c94-agent-and-orchestrator-identity) | Level 3. Agent identity credentials rotate on a defined schedule |
| Verify that privileged access to model weights, training pipelines, and production AI configuration is granted just in time, with a defined maximum... | [5.2.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 3. Just-in-time privileged access to weights, training pipelines and production AI configuration with maximum session duration and automatic expiry |
| Verify that MCP servers validate the presented access token's issuer, audience, expiration, and scope claims in accordance with OAuth 2.1. | [10.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c102-authentication--authorization) | Level 1. MCP servers validate the presented token issuer, audience, expiration and scope claims per OAuth 2.1, the check that stops a valid credential being replayed beyond its intended scope |
| Verify that MCP servers validate access tokens for each request and do not rely on transport security alone. | [10.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c102-authentication--authorization) | Level 1. MCP servers validate access tokens on each request rather than relying on transport security alone |
| Verify that the policy decision point for agent authorization is isolated from the agent's execution environment. | [5.2.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Policy decision point for agent authorization isolated from the agent execution environment, so a compromised agent cannot rewrite its own privilege boundary |
| Verify that long-running agent sessions re-evaluate current backend authorization policy on every privileged action. | [9.5.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 3. Long-running agent sessions re-evaluate current backend authorization policy on every privileged action, closing the stale-grant window |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 10.2.2: Verify that MCP servers validate the presented access token's issuer, audience, expiration, and scope claims in accordance with OAuth 2.1.
- 10.2.1: Verify that MCP servers validate access tokens for each request and do not rely on transport security alone.

**Tier 2 - Short-term (first 30 days):**
- 9.4.1: Verify that each agent instance has a unique cryptographic identity and authenticates as a first-class principal to downstream systems.
- 9.5.2: Verify that when an agent acts on a user's behalf, the runtime propagates an integrity-protected, scope-limited token that carries the user's authorization c...
- 9.5.4: Verify that secrets and credentials required by an agent at runtime are not exposed within the model's observable context, including the context window, syst...
- 5.2.5: Verify that the policy decision point for agent authorization is isolated from the agent's execution environment.

**Tier 3 - Strategic:**
- 5.1.2: Verify that AI agents in federated or multi-system deployments authenticate using short-lived, minimal-scoped, cryptographically signed tokens.
- 5.1.1: Verify that high-risk AI operations (model deployment, weight export, training data access, production configuration changes) require step-up authentication.
- 9.4.3: Verify that agent identity credentials rotate on a defined schedule.
- 5.2.6: Verify that privileged access to model weights, training pipelines, and production AI configuration is granted just in time, with a defined maximum session d...
- 9.5.6: Verify that long-running agent sessions re-evaluate current backend authorization policy on every privileged action.

#### Cross-references

- LLM Top 10: LLM06, LLM01
- Agentic: N/A
- DSGAI: DSGAI02, DSGAI10, DSGAI11, DSGAI06, DSGAI08
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### ASI04 - Agentic Supply Chain

AISVS covers the runtime-fetched supply chain that static inventory misses. C10.1 requires trusted sources and allow-listed MCP servers, C9.3.7 requires allow-list verification of resources named in model output, and C10.4.8 requires re-approval when a tool definition changes.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that MCP components are obtained only from trusted sources and cryptographically verified. | [10.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c101-component-integrity) | Level 1. MCP components obtained only from trusted sources and cryptographically verified |
| Verify that only allow-listed MCP servers are permitted. | [10.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c101-component-integrity) | Level 2. Only allow-listed MCP servers permitted |
| Verify that model weights, datasets, and fine-tuning adapters are downloaded only from approved sources. | [6.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c61-model-artifact-integrity) | Level 1. Model weights, datasets and adapters downloaded only from approved sources |
| Verify that every model artifact publishes a version-controlled, machine-readable AI BOM listing datasets, weights, licenses, and data-origin state... | [6.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c62-ai-bom--supply-chain-monitoring) | Level 1. Version-controlled machine-readable AI BOM per model artifact, giving the static inventory this risk says is usually missing |
| Verify that external resources named in model output are verified against an approved allow-list or registry before the agent installs or invokes t... | [9.3.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. External resources named in model output verified against an approved allow-list or registry before the agent installs or invokes them, covering runtime-fetched components |
| Verify that locally launched MCP servers run in a least-privilege sandbox with restricted file system, network, and system access. | [10.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c101-component-integrity) | Level 2. Locally launched MCP servers run in a least-privilege sandbox with restricted file system, network and system access |
| Verify that every third-party model artifact can be integrity-verified. | [6.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c61-model-artifact-integrity) | Level 2. Every third-party model artifact is integrity-verifiable |
| Verify that MCP clients maintain a snapshot of tool definitions and that any change to a tool definition triggers re-approval before the modified t... | [10.4.8](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c104-schema-message-and-input-validation) | Level 3. Tool definition snapshot maintained and any change triggers re-approval before the modified tool can be invoked, the rug-pull control |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 10.1.1: Verify that MCP components are obtained only from trusted sources and cryptographically verified.
- 6.1.2: Verify that model weights, datasets, and fine-tuning adapters are downloaded only from approved sources.
- 6.2.1: Verify that every model artifact publishes a version-controlled, machine-readable AI BOM listing datasets, weights, licenses, and data-origin statements.

**Tier 2 - Short-term (first 30 days):**
- 10.1.2: Verify that only allow-listed MCP servers are permitted.
- 9.3.7: Verify that external resources named in model output are verified against an approved allow-list or registry before the agent installs or invokes them.
- 10.1.3: Verify that locally launched MCP servers run in a least-privilege sandbox with restricted file system, network, and system access.
- 6.1.3: Verify that every third-party model artifact can be integrity-verified.

**Tier 3 - Strategic:**
- 10.4.8: Verify that MCP clients maintain a snapshot of tool definitions and that any change to a tool definition triggers re-approval before the modified tool can be...

#### Cross-references

- LLM Top 10: LLM03, LLM08, LLM05
- Agentic: N/A
- DSGAI: DSGAI04, DSGAI06, DSGAI19
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### ASI05 - Unexpected Code Execution

AISVS treats generated code as untrusted output requiring a sandbox. C9.3.1 and C4.1.1 require isolated execution, C4.1.2 blocks code execution during artifact deserialization, and C9.1.1 caps the blast radius of anything that does execute.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that each tool/plugin executes in a least-privilege sandbox or is otherwise isolated from model operations. | [9.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Each tool or plugin executes in a least-privilege sandbox or is isolated from model operations |
| Verify that AI models execute in isolated sandboxes. | [4.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C04-Infrastructure.md#c41-ai-workload-sandboxing--validation) | Level 1. AI models execute in isolated sandboxes |
| Verify that model artifact loading enforces an explicit allow-list of serialization formats that do not permit arbitrary code execution during dese... | [4.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C04-Infrastructure.md#c41-ai-workload-sandboxing--validation) | Level 1. Model artifact loading restricted to serialization formats that cannot execute code during deserialization |
| Verify that tool outputs are validated against schemas. | [9.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Tool outputs validated against schemas before consumption |
| Verify that the application validates all model outputs against a defined schema and rejects any output that does not match. | [7.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c71-output-format-enforcement) | Level 1. Model output validated against a defined schema and rejected when it does not match, applied to generated code before it reaches an interpreter |
| Verify that per-tool quotas and timeouts (e.g., CPU, memory, disk, egress, and execution time) are enforced. | [9.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c91-execution-budgets-loop-control-and-circuit-breakers) | Level 1. Per-tool quotas and timeouts for CPU, memory, disk, egress and execution time bound the blast radius of executed code |
| Verify that AI-specific runtime components are not shared across environment boundaries (e.g., development, staging, production). | [3.4.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c34-secure-development-practices) | Level 1. AI-specific runtime components not shared across development, staging and production boundaries, so code executed in a lower environment cannot reach production |
| Verify that there is architectural separation between processing of untrusted tool outputs and agent operations. | [9.3.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. Architectural separation between processing of untrusted tool outputs and agent operations |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 9.3.1: Verify that each tool/plugin executes in a least-privilege sandbox or is otherwise isolated from model operations.
- 4.1.1: Verify that AI models execute in isolated sandboxes.
- 4.1.2: Verify that model artifact loading enforces an explicit allow-list of serialization formats that do not permit arbitrary code execution during deserialization.
- 9.3.2: Verify that tool outputs are validated against schemas.
- 7.1.1: Verify that the application validates all model outputs against a defined schema and rejects any output that does not match.
- 9.1.1: Verify that per-tool quotas and timeouts (e.g., CPU, memory, disk, egress, and execution time) are enforced.
- 3.4.1: Verify that AI-specific runtime components are not shared across environment boundaries (e.g., development, staging, production).

**Tier 2 - Short-term (first 30 days):**
- 9.3.6: Verify that there is architectural separation between processing of untrusted tool outputs and agent operations.

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: LLM05, LLM07, LLM03, LLM02, LLM01, LLM06
- Agentic: N/A
- DSGAI: DSGAI12, DSGAI13, DSGAI06, DSGAI05, DSGAI08
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### ASI06 - Memory and Context Poisoning

AISVS addresses memory poisoning as a write-path access control problem. C8.2.3 requires explicit source validation before agent or tool output enters trusted memory, C12.5.4 tags every ingested document with source and writer identity, and C8.3 provides quarantine and reset as recovery.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that agent outputs and tool outputs are not automatically written to trusted agent memory without explicit source validation. | [8.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 2. Agent and tool outputs not automatically written to trusted agent memory without explicit source validation, the direct control |
| Verify that document metadata tags are immutable after the initial write. | [8.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c81-access-controls-on-memory--rag-indices) | Level 2. Document metadata tags immutable after initial write |
| Verify that every ingested document is tagged at write time with source, writer identity, and timestamp. | [12.5.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c125-training-data--model-lifecycle-audit) | Level 2. Every ingested document tagged at write time with source, writer identity and timestamp, making poisoned entries attributable |
| Verify that content crafted to manipulate retrieval results is detected and rejected or quarantined before vectorization. | [8.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 3. Content crafted to manipulate retrieval results detected and rejected or quarantined before vectorization |
| Verify that new content written to memory is checked for contradictions with what is already stored and that conflicts trigger alerts. | [8.2.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 3. New content written to memory checked for contradictions with what is already stored, with conflicts alerting |
| Verify that memory can be reset. | [8.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c83-memory-expiry--revocation) | Level 2. Memory can be reset, giving a recovery path once poisoning is confirmed |
| Verify that quarantined content is retained but excluded from all retrieval results. | [8.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c83-memory-expiry--revocation) | Level 3. Quarantined content retained but excluded from all retrieval results, preserving evidence without re-exposure |
| Verify that agent state persisted between invocations is integrity-protected. | [9.4.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c94-agent-and-orchestrator-identity) | Level 3. Agent state persisted between invocations is integrity-protected |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- No AISVS Level 1 requirement maps to this entry

**Tier 2 - Short-term (first 30 days):**
- 8.2.3: Verify that agent outputs and tool outputs are not automatically written to trusted agent memory without explicit source validation.
- 8.1.2: Verify that document metadata tags are immutable after the initial write.
- 12.5.4: Verify that every ingested document is tagged at write time with source, writer identity, and timestamp.
- 8.3.2: Verify that memory can be reset.

**Tier 3 - Strategic:**
- 8.2.4: Verify that content crafted to manipulate retrieval results is detected and rejected or quarantined before vectorization.
- 8.2.5: Verify that new content written to memory is checked for contradictions with what is already stored and that conflicts trigger alerts.
- 8.3.3: Verify that quarantined content is retained but excluded from all retrieval results.
- 9.4.4: Verify that agent state persisted between invocations is integrity-protected.

#### Cross-references

- LLM Top 10: LLM04, LLM08, LLM02, LLM03
- Agentic: N/A
- DSGAI: DSGAI04, DSGAI13, DSGAI06, DSGAI08
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### ASI07 - Insecure Inter-Agent Communications

AISVS covers inter-agent communication mainly through the MCP transport chapter. C10.3 requires authenticated encrypted transport, independent Origin and Host validation, and minimum protocol version enforcement, while C9.4 supplies the cryptographic agent identity that makes spoofing detectable.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that authenticated, encrypted streamable HTTP is used for MCP transport for remote services. | [10.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c103-secure-transport) | Level 1. Authenticated, encrypted streamable HTTP required for remote MCP transport |
| Verify that each agent instance has a unique cryptographic identity and authenticates as a first-class principal to downstream systems. | [9.4.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c94-agent-and-orchestrator-identity) | Level 2. Each agent instance has a unique cryptographic identity and authenticates as a first-class principal, the anti-spoofing base control |
| Verify that agent-initiated actions are cryptographically bound to each step of the execution chain for non-repudiation. | [9.4.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c94-agent-and-orchestrator-identity) | Level 2. Agent-initiated actions cryptographically bound to each step of the execution chain for non-repudiation |
| Verify that MCP servers validate both the Origin header and the Host header independently on all HTTP-based transports to prevent DNS rebinding att... | [10.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c103-secure-transport) | Level 2. Origin and Host headers validated independently on all HTTP-based transports to prevent DNS rebinding |
| Verify that MCP clients enforce a minimum acceptable protocol version and reject initialize responses that propose a version below that minimum. | [10.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c103-secure-transport) | Level 2. Clients enforce a minimum acceptable protocol version and reject initialize responses below it, blocking downgrade |
| Verify that MCP servers sign tool responses with a unique nonce and timestamp so MCP clients can detect replay attempts. | [10.4.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c104-schema-message-and-input-validation) | Level 2. Tool responses signed with a unique nonce and timestamp so clients can detect replay |
| Verify that inter-agent task delegation is restricted by an explicit authorization policy. | [9.5.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. Inter-agent task delegation restricted by an explicit authorization policy |
| Verify that access tokens between the MCP client and server are sender-constrained using mTLS or DPoP. | [10.3.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c103-secure-transport) | Level 3. Access tokens between client and server sender-constrained using mTLS or DPoP, defeating agent-in-the-middle token replay |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 10.3.1: Verify that authenticated, encrypted streamable HTTP is used for MCP transport for remote services.

**Tier 2 - Short-term (first 30 days):**
- 9.4.1: Verify that each agent instance has a unique cryptographic identity and authenticates as a first-class principal to downstream systems.
- 9.4.2: Verify that agent-initiated actions are cryptographically bound to each step of the execution chain for non-repudiation.
- 10.3.3: Verify that MCP servers validate both the Origin header and the Host header independently on all HTTP-based transports to prevent DNS rebinding attacks.
- 10.3.4: Verify that MCP clients enforce a minimum acceptable protocol version and reject initialize responses that propose a version below that minimum.
- 10.4.6: Verify that MCP servers sign tool responses with a unique nonce and timestamp so MCP clients can detect replay attempts.
- 9.5.5: Verify that inter-agent task delegation is restricted by an explicit authorization policy.

**Tier 3 - Strategic:**
- 10.3.5: Verify that access tokens between the MCP client and server are sender-constrained using mTLS or DPoP.

#### Cross-references

- LLM Top 10: LLM03, LLM06, LLM01
- Agentic: N/A
- DSGAI: DSGAI02, DSGAI16, DSGAI17, DSGAI06
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### ASI08 - Cascading Agent Failures

AISVS treats cascade as a containment problem. C9.1.3 requires a swarm-level kill-switch able to halt all active agent instances, C9.6.3 requires the kill-switch channel to be out-of-band from the agent runtime, and C9.2.10 requires chain-wide approval gates to take the highest-impact classification present.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that a swarm-level kill-switch exists that can halt all active agent instances. | [9.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c91-execution-budgets-loop-control-and-circuit-breakers) | Level 2. Swarm-level kill-switch able to halt all active agent instances, the direct containment control for a propagating failure |
| Verify that per-execution budgets (e.g., max recursion depth, token use, and monetary spend) are configured and enforced by the runtime. | [9.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c91-execution-budgets-loop-control-and-circuit-breakers) | Level 1. Per-execution budgets including max recursion depth bound runaway amplification |
| Verify that per-tool quotas and timeouts (e.g., CPU, memory, disk, egress, and execution time) are enforced. | [9.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c91-execution-budgets-loop-control-and-circuit-breakers) | Level 1. Per-tool quotas and timeouts contain a single failing component |
| Verify that a manual kill-switch mechanism exists to immediately halt AI model inference and outputs. | [9.6.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c96-shutdown-and-graceful-degradation) | Level 1. Manual kill-switch to immediately halt model inference and outputs |
| Verify that kill-switch commands are implemented through an out-of-band channel that is isolated from the agent runtime. | [9.6.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c96-shutdown-and-graceful-degradation) | Level 3. Kill-switch commands implemented through an out-of-band channel isolated from the agent runtime, so containment survives runtime compromise |
| Verify that approval gates for multi-step or multi-agent action chains enforce the highest-impact reversibility classification present anywhere in ... | [9.2.10](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 3. Approval gates for multi-step or multi-agent chains enforce the highest-impact reversibility classification present anywhere in the chain |
| Verify that policy violations trigger automated tool containment. | [9.3.8](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 3. Policy violations trigger automated tool containment |
| Verify that unexplained behavioral shifts are distinguished from gradual, expected operational drift. | [12.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c123-model-data-and-performance-drift-detection) | Level 3. Unexplained behavioral shifts distinguished from gradual expected operational drift, detecting cascade onset |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 9.1.2: Verify that per-execution budgets (e.g., max recursion depth, token use, and monetary spend) are configured and enforced by the runtime.
- 9.1.1: Verify that per-tool quotas and timeouts (e.g., CPU, memory, disk, egress, and execution time) are enforced.
- 9.6.1: Verify that a manual kill-switch mechanism exists to immediately halt AI model inference and outputs.

**Tier 2 - Short-term (first 30 days):**
- 9.1.3: Verify that a swarm-level kill-switch exists that can halt all active agent instances.

**Tier 3 - Strategic:**
- 9.6.3: Verify that kill-switch commands are implemented through an out-of-band channel that is isolated from the agent runtime.
- 9.2.10: Verify that approval gates for multi-step or multi-agent action chains enforce the highest-impact reversibility classification present anywhere in the chain.
- 9.3.8: Verify that policy violations trigger automated tool containment.
- 12.3.4: Verify that unexplained behavioral shifts are distinguished from gradual, expected operational drift.

#### Cross-references

- LLM Top 10: LLM10, LLM01, LLM04
- Agentic: N/A
- DSGAI: DSGAI17, DSGAI05
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### ASI09 - Human-Agent Trust Exploitation

AISVS makes the human approval gate resistant to a persuasive agent. C9.2.2 requires canonicalized complete action parameters shown without truncation, C9.2.8 cryptographically binds the approval to those exact parameters, and C9.6.2 blocks rather than proceeds when approval times out.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that approval requests display canonicalized and complete action parameters, such as diffs, commands, recipients, amounts, resources, and sc... | [9.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 2. Approval requests display canonicalized and complete action parameters including diffs, commands, recipients, amounts, resources and scopes, without truncation or unsafe transformation, so the approver sees what they are actually approving |
| Verify that when a human-approval gate is not satisfied within the defined approval time, the system blocks the pending action. | [9.6.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c96-shutdown-and-graceful-degradation) | Level 2. Pending action blocked when a human-approval gate is not satisfied within the defined approval time, removing approval-fatigue pressure |
| Verify that the AI-augmented review mechanism is protected against manipulation by adversarial inputs, and cannot be overridden or bypassed through... | [9.2.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 2. AI-augmented review mechanism protected against adversarial manipulation and cannot be overridden through prompt injection |
| Verify that responses generated using retrieval-augmented generation (RAG) include attribution to the source documents. | [7.4.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c74-source-attribution--citation-integrity) | Level 1. RAG responses carry source attribution so a persuasive answer can be checked against its source |
| Verify that the system assesses the reliability of generated answers using a confidence estimation method. | [7.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c72-hallucination-detection--mitigation) | Level 2. Reliability of generated answers assessed with a confidence estimation method, surfacing uncertainty against fluency |
| Verify that audit logs capture security-critical proactive actions, including approver identity, timestamp, action parameters, and decision outcomes. | [12.4.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c124-proactive-security-behavior-monitoring) | Level 2. Audit logs capture approver identity, timestamp, action parameters and decision outcomes |
| Verify that approvals are cryptographically bound to action parameters, requester identity, execution context, and a unique single-use nonce. | [9.2.8](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 3. Approvals cryptographically bound to action parameters, requester identity, execution context and a single-use nonce, so a displayed approval cannot be swapped for a different action |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 7.4.1: Verify that responses generated using retrieval-augmented generation (RAG) include attribution to the source documents.

**Tier 2 - Short-term (first 30 days):**
- 9.2.2: Verify that approval requests display canonicalized and complete action parameters, such as diffs, commands, recipients, amounts, resources, and scopes, with...
- 9.6.2: Verify that when a human-approval gate is not satisfied within the defined approval time, the system blocks the pending action.
- 9.2.7: Verify that the AI-augmented review mechanism is protected against manipulation by adversarial inputs, and cannot be overridden or bypassed through prompt in...
- 7.2.1: Verify that the system assesses the reliability of generated answers using a confidence estimation method.
- 12.4.2: Verify that audit logs capture security-critical proactive actions, including approver identity, timestamp, action parameters, and decision outcomes.

**Tier 3 - Strategic:**
- 9.2.8: Verify that approvals are cryptographically bound to action parameters, requester identity, execution context, and a unique single-use nonce.

#### Cross-references

- LLM Top 10: LLM09, LLM06
- Agentic: N/A
- DSGAI: DSGAI21, DSGAI04, DSGAI06, DSGAI18
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### ASI10 - Rogue Agents

AISVS detects rogue behaviour through telemetry and immutability. C12.1 and C12.2 require AI-specific logging and behavioural anomaly detection, C12.5.3 requires immutable model change records, and C9.2.5 stops an agent widening its own boundary through self-modification.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that AI interactions are logged with session context and AI-specific telemetry. | [12.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c121-request--response-logging) | Level 1. AI interactions logged with session context and AI-specific telemetry, the foundational visibility control |
| Verify that behavioral anomaly detection identifies unusual conversation patterns, excessive retry attempts, or probing behaviors. | [12.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c122-detection-and-alerting) | Level 2. Behavioral anomaly detection identifies unusual conversation patterns, excessive retry attempts and probing behaviors |
| Verify that agent-initiated actions are cryptographically bound to each step of the execution chain for non-repudiation. | [9.4.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c94-agent-and-orchestrator-identity) | Level 2. Agent-initiated actions cryptographically bound to each step of the execution chain for non-repudiation |
| Verify that a manual kill-switch mechanism exists to immediately halt AI model inference and outputs. | [9.6.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c96-shutdown-and-graceful-degradation) | Level 1. Manual kill-switch to immediately halt inference and outputs |
| Verify that any self-modification capability (e.g., prompt rewriting, tool-list changes, parameter updates) is restricted by enforceable boundaries. | [9.2.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 2. Self-modification capability restricted by enforceable boundaries, blocking a compromised agent from widening its own scope |
| Verify that autonomous action triggers include proactive behavior-pattern analysis, security evaluation, and threat-landscape assessment. | [12.4.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c124-proactive-security-behavior-monitoring) | Level 2. Autonomous action triggers include proactive behavior-pattern analysis, security evaluation and threat-landscape assessment |
| Verify that kill-switch activations and override commands are logged. | [12.4.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c124-proactive-security-behavior-monitoring) | Level 2. Kill-switch activations and override commands logged |
| Verify that LLM API traffic is monitored for covert-channel indicators and communication signatures to identify malware and command-and-control (C2... | [12.2.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c122-detection-and-alerting) | Level 3. LLM API traffic monitored for covert-channel indicators and C2 communication signatures |
| Verify that all model changes generate immutable audit records. | [12.5.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c125-training-data--model-lifecycle-audit) | Level 2. All model changes generate immutable audit records, so a silent substitution behind a compliant-looking agent is detectable |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 12.1.1: Verify that AI interactions are logged with session context and AI-specific telemetry.
- 9.6.1: Verify that a manual kill-switch mechanism exists to immediately halt AI model inference and outputs.

**Tier 2 - Short-term (first 30 days):**
- 12.2.2: Verify that behavioral anomaly detection identifies unusual conversation patterns, excessive retry attempts, or probing behaviors.
- 9.4.2: Verify that agent-initiated actions are cryptographically bound to each step of the execution chain for non-repudiation.
- 9.2.5: Verify that any self-modification capability (e.g., prompt rewriting, tool-list changes, parameter updates) is restricted by enforceable boundaries.
- 12.4.1: Verify that autonomous action triggers include proactive behavior-pattern analysis, security evaluation, and threat-landscape assessment.
- 12.4.3: Verify that kill-switch activations and override commands are logged.
- 12.5.3: Verify that all model changes generate immutable audit records.

**Tier 3 - Strategic:**
- 12.2.6: Verify that LLM API traffic is monitored for covert-channel indicators and communication signatures to identify malware and command-and-control (C2) activity.

#### Cross-references

- LLM Top 10: LLM06, LLM10, LLM05
- Agentic: ASI01, ASI02, ASI03, ASI05, ASI04, ASI06, ASI07, ASI08, ASI09
- DSGAI: DSGAI16, DSGAI03, DSGAI19, DSGAI02, DSGAI17, DSGAI06
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

## Implementation priority table

| Priority | AISVS components | Entries addressed |
|---|---|---|
| P1 - Pre-production gate | All Level 1 requirements | ASI01, ASI02, ASI03, ASI04, ASI05, ASI07, ASI08, ASI09, ASI10 |
| P2 - First 30 days | All Level 2 requirements | ASI01, ASI02, ASI03, ASI04, ASI05, ASI06, ASI07, ASI08, ASI09, ASI10 |
| P3 - Programme maturity | All Level 3 requirements | ASI02, ASI03, ASI04, ASI06, ASI07, ASI08, ASI09, ASI10 |

---

## References

- [OWASP AISVS project page](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/)
- [OWASP AISVS 1.0 frozen text](https://github.com/OWASP/AISVS/tree/main/1.0/en)
- [OWASP Top 10 for Agentic AI Applications 2026 - OWASP](https://genai.owasp.org/resource/agentic-ai-top-10/)
- [shared/TEMPLATE.md](../shared/TEMPLATE.md)

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-28 | Initial release - full mapping of ASI01-ASI10 to OWASP AISVS 1.0 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) - maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
