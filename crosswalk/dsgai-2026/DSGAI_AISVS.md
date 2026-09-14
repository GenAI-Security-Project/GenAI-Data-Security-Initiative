<!--
  OWASP GenAI Crosswalk
  Source list : OWASP GenAI Data Security Risks 2026 (DSGAI01-DSGAI21)
  Framework   : OWASP AISVS 1.0
  Version     : 2026-Q3
  Maintained by: OWASP GenAI Data Security Initiative - https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# OWASP GenAI Data Security Risks 2026 × OWASP AISVS 1.0

Mapping the [OWASP GenAI Data Security Risks 2026](https://genai.owasp.org/resource/genai-data-security-risks/) to the [OWASP Artificial Intelligence Security Verification Standard 1.0](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/), a technical verification standard of 191 testable requirements across 12 chapters, used by engineers and auditors to verify that a specific AI system implements a control rather than merely documents it.

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
| DSGAI01 | Sensitive Data Leakage | Critical | C5.2, C8.2, C11.2, C1.1, C7.3 | Hardening | Both |
| DSGAI02 | Agent Identity and Credential Exposure | Critical | C9.5, C10.2, C9.4, C5.1, C9.2 | Hardening | Both |
| DSGAI03 | Shadow AI and Unsanctioned Data Flows | High | C6.1, C10.1, C3.1, C1.1, C12.1, C3.2 | Hardening | Both |
| DSGAI04 | Data Model and Artifact Poisoning | Critical | C1.3, C1.1, C3.1, C6.1, C8.2, C3.5, C11.4 | Hardening | Both |
| DSGAI05 | Data Integrity and Validation Failures | High | C1.1, C7.1, C9.3, C10.4, C1.3, C6.2, C12.3, C3.5 | Hardening | Both |
| DSGAI06 | Tool Plugin and Agent Data Exchange | High | C9.3, C10.4, C10.2 | Hardening | Both |
| DSGAI07 | Data Governance and Lifecycle | High | C1.1, C12.5, C3.1, C8.3, C5.2 | Hardening | Both |
| DSGAI08 | Non-Compliance and Regulatory Violations | High | C1.1, C12.5, C1.2, C11.2, C1.3 | Hardening | Both |
| DSGAI09 | Multimodal Cross-Channel Leakage | High | C2.2, C7.3, C8.2, C5.2 | Hardening | Both |
| DSGAI10 | Synthetic Data and Anonymization Pitfalls | Medium | C11.2, C1.2, C8.2 | Hardening | Both |
| DSGAI11 | Cross-Context Conversation Bleed | High | C5.3, C8.1, C3.3, C10.2, C8.3 | Hardening | Both |
| DSGAI12 | Unsafe Natural Language Data Gateways | Critical | C9.5, C5.2, C2.1, C9.3, C9.2 | Hardening | Both |
| DSGAI13 | Vector Store Platform Security | High | C5.2, C8.1, C8.2, C8.3 | Hardening | Both |
| DSGAI14 | Excessive Telemetry and Monitoring Leakage | High | C12.1, C9.5, C5.2, C1.2 | Hardening | Both |
| DSGAI15 | Over-Broad Context Windows | High | C5.2, C2.1, C8.1 | Hardening | Both |
| DSGAI16 | Endpoint and Browser Overreach | High | C10.1, C10.4, C9.3, C4.3, C9.2, C7.3 | Hardening | Both |
| DSGAI17 | Data Availability and Resilience Failures | High | C3.3, C1.1, C3.5, C12.5, C8.3 | Hardening | Both |
| DSGAI18 | Inference and Data Reconstruction | High | C11.2, C11.3, C1.1 | Hardening | Both |
| DSGAI19 | Human-in-Loop and Labeler Overexposure | Medium | C1.2, C1.3, C12.5 | Hardening | Both |
| DSGAI20 | Model Exfiltration and IP Replication | High | C11.3, C11.2, C4.1, C4.3, C5.2 | Advanced | Both |
| DSGAI21 | Disinformation via Data Poisoning | High | C1.3, C1.1, C8.2, C7.4, C12.3 | Hardening | Both |

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

### DSGAI01 - Sensitive Data Leakage

AISVS enforces authorization at the retrieval boundary rather than the response. C5.2.2 requires the end-user context at each retrieval and assembly stage, C5.2.4 filters post-inference, and C5.2.7 propagates classification labels into embeddings, caches and outputs so the aggregation effect stays governed.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive. | [5.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Post-inference filtering prevents responses including data the requester is not authorized to receive |
| Verify that retrieval pipelines (e.g., RAG queries, embedding lookups) enforce the end-user's authorization context at each retrieval and assembly ... | [5.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Retrieval pipelines enforce the end-user authorization context at each retrieval and assembly stage, the direct control for RAG over-retrieval |
| Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped. | [8.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 1. Sensitive fields detected before embedding and masked, tokenized or dropped |
| Verify that model-inferred sensitive attributes are not directly returned in outputs. | [11.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 1. Model-inferred sensitive attributes not returned directly in outputs |
| Verify that training data includes only features, attributes, and fields required for the model's stated purpose. | [1.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 1. Training data limited to features required for the stated purpose, bounding memorisation exposure at source |
| Verify that output filters detect and block responses that disclose system prompt content or backend data. | [7.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c73-output-safety) | Level 2. Output filters block responses disclosing system prompt content or backend data |
| Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs). | [5.2.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 3. Classification labels propagate to embeddings, prompt caches and outputs, addressing the aggregation effect this risk names |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 8.2.1: Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped.
- 11.2.1: Verify that model-inferred sensitive attributes are not directly returned in outputs.
- 1.1.1: Verify that training data includes only features, attributes, and fields required for the model's stated purpose.

**Tier 2 - Short-term (first 30 days):**
- 5.2.4: Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive.
- 5.2.2: Verify that retrieval pipelines (e.g., RAG queries, embedding lookups) enforce the end-user's authorization context at each retrieval and assembly stage, rat...
- 7.3.2: Verify that output filters detect and block responses that disclose system prompt content or backend data.

**Tier 3 - Strategic:**
- 5.2.7: Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs).

#### Cross-references

- LLM Top 10: LLM02, LLM01, LLM03, LLM07
- Agentic: ASI03, ASI06, ASI01, ASI02
- DSGAI: N/A
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI02 - Agent Identity and Credential Exposure

AISVS keeps credentials out of the model's reach entirely. C9.5.4 excludes secrets from the context window, system prompts and tool call parameters, C10.2.3 stops MCP resource servers persisting tokens, and C10.2.7 blocks the token pass-through that propagates one compromise across services.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that secrets and credentials required by an agent at runtime are not exposed within the model's observable context, including the context wi... | [9.5.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. Secrets and credentials required at runtime not exposed within the model observable context including context window, system prompts and tool call parameters, the direct control |
| Verify that MCP servers acting as OAuth 2.1 resource servers do not store or persist access tokens or user credentials. | [10.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c102-authentication--authorization) | Level 1. MCP servers acting as OAuth 2.1 resource servers do not store or persist access tokens or user credentials |
| Verify that each agent instance has a unique cryptographic identity and authenticates as a first-class principal to downstream systems. | [9.4.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c94-agent-and-orchestrator-identity) | Level 2. Each agent instance has a unique cryptographic identity and authenticates as a first-class principal, so a shared credential is not the identity |
| Verify that MCP servers do not pass through access tokens received from clients to downstream APIs. | [10.2.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c102-authentication--authorization) | Level 2. MCP servers do not pass through client access tokens to downstream APIs, blocking the confused-deputy propagation this risk describes |
| Verify that AI agents in federated or multi-system deployments authenticate using short-lived, minimal-scoped, cryptographically signed tokens. | [5.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c51-authentication) | Level 3. Short-lived, minimal-scoped, cryptographically signed tokens for agents in federated deployments, bounding the value of a leaked credential |
| Verify that agent identity credentials rotate on a defined schedule. | [9.4.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c94-agent-and-orchestrator-identity) | Level 3. Agent identity credentials rotate on a defined schedule |
| Verify that cryptographic key material or credentials used to issue approvals are isolated from the agent runtime. | [9.2.9](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 3. Key material or credentials used to issue approvals isolated from the agent runtime |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 10.2.3: Verify that MCP servers acting as OAuth 2.1 resource servers do not store or persist access tokens or user credentials.

**Tier 2 - Short-term (first 30 days):**
- 9.5.4: Verify that secrets and credentials required by an agent at runtime are not exposed within the model's observable context, including the context window, syst...
- 9.4.1: Verify that each agent instance has a unique cryptographic identity and authenticates as a first-class principal to downstream systems.
- 10.2.7: Verify that MCP servers do not pass through access tokens received from clients to downstream APIs.

**Tier 3 - Strategic:**
- 5.1.2: Verify that AI agents in federated or multi-system deployments authenticate using short-lived, minimal-scoped, cryptographically signed tokens.
- 9.4.3: Verify that agent identity credentials rotate on a defined schedule.
- 9.2.9: Verify that cryptographic key material or credentials used to issue approvals are isolated from the agent runtime.

#### Cross-references

- LLM Top 10: LLM06, LLM04, LLM03, LLM05, LLM09
- Agentic: ASI03, ASI07, ASI04, ASI09
- DSGAI: DSGAI01
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI03 - Shadow AI and Unsanctioned Data Flows

AISVS gives shadow AI a technical rather than policy answer. C10.1.2 allow-lists MCP servers, C6.1.2 restricts model and dataset sources to approved ones, and C12.1.3 requires a structured inference log carrying the provider name so unsanctioned egress is visible.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that model weights, datasets, and fine-tuning adapters are downloaded only from approved sources. | [6.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c61-model-artifact-integrity) | Level 1. Model weights, datasets and fine-tuning adapters downloaded only from approved sources |
| Verify that only allow-listed MCP servers are permitted. | [10.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c101-component-integrity) | Level 2. Only allow-listed MCP servers permitted, the technical gate on unsanctioned tool and data channels |
| Verify that a model registry maintains an inventory of all deployed model artifacts and their origin. | [3.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c31-model-authorization--integrity) | Level 1. Model registry maintains an inventory of all deployed model artifacts and their origin |
| Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, int... | [1.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Current inventory of every training-data source with origin, responsible party, license, collection method and use constraints |
| Verify that log entries for AI inference events follow a structured, interoperable schema that includes at least the model identifier, token usage ... | [12.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c121-request--response-logging) | Level 2. Structured inference log schema including model identifier, token usage, provider name and operation type, giving per-provider visibility of where data is going |
| Verify that provider model, version, or routing changes trigger security re-evaluation before continued use. | [3.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c32-model-validation--testing) | Level 3. Provider model, version or routing changes trigger security re-evaluation before continued use |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 6.1.2: Verify that model weights, datasets, and fine-tuning adapters are downloaded only from approved sources.
- 3.1.1: Verify that a model registry maintains an inventory of all deployed model artifacts and their origin.

**Tier 2 - Short-term (first 30 days):**
- 10.1.2: Verify that only allow-listed MCP servers are permitted.
- 1.1.2: Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, intended use ...
- 12.1.3: Verify that log entries for AI inference events follow a structured, interoperable schema that includes at least the model identifier, token usage (input and...

**Tier 3 - Strategic:**
- 3.2.3: Verify that provider model, version, or routing changes trigger security re-evaluation before continued use.

#### Cross-references

- LLM Top 10: LLM03, LLM02, LLM05, LLM06
- Agentic: ASI04, ASI10
- DSGAI: DSGAI07, DSGAI08
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI04 - Data Model and Artifact Poisoning

AISVS covers poisoning across training data, artifacts and the RAG store. C1.3 requires pipeline poisoning detection, C3.1.3 verifies signatures at deployment admission and on load, and C11.4.3 protects the safety feedback loop itself from adversarial manipulation.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that training and fine-tuning pipelines implement poisoning detection techniques to identify potential data poisoning or unintentional corru... | [1.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 2. Training and fine-tuning pipelines implement poisoning detection |
| Verify that integrity monitoring is applied to guard against unauthorized modifications or corruption of training data. | [1.1.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Integrity monitoring guards training data against unauthorized modification or corruption |
| Verify that model cryptographic signatures are verified at deployment admission and on load. | [3.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c31-model-authorization--integrity) | Level 2. Model cryptographic signatures verified at deployment admission and on load, blocking a poisoned artifact from reaching production |
| Verify that every third-party model artifact can be integrity-verified. | [6.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c61-model-artifact-integrity) | Level 2. Every third-party model artifact is integrity-verifiable |
| Verify that content crafted to manipulate retrieval results is detected and rejected or quarantined before vectorization. | [8.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 3. Content crafted to manipulate retrieval results detected and rejected or quarantined before vectorization, covering RAG-store poisoning |
| Verify that defenses against clean-label poisoning attacks are implemented. | [1.3.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 3. Clean-label poisoning defenses |
| Verify that RLHF training stages include automated detection of reward hacking or reward model over-optimization. | [3.5.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c35-pipeline-fine-tuning) | Level 3. RLHF training stages include automated detection of reward hacking or reward model over-optimization |
| Verify that the safety violation feedback pipeline includes poisoning detection and human review gates to prevent adversarial manipulation of the i... | [11.4.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c114-model-runtime-anomaly-detection) | Level 3. Safety violation feedback pipeline includes poisoning detection and human review gates, protecting the improvement loop itself |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- No AISVS Level 1 requirement maps to this entry

**Tier 2 - Short-term (first 30 days):**
- 1.3.1: Verify that training and fine-tuning pipelines implement poisoning detection techniques to identify potential data poisoning or unintentional corruption in t...
- 1.1.4: Verify that integrity monitoring is applied to guard against unauthorized modifications or corruption of training data.
- 3.1.3: Verify that model cryptographic signatures are verified at deployment admission and on load.
- 6.1.3: Verify that every third-party model artifact can be integrity-verified.

**Tier 3 - Strategic:**
- 8.2.4: Verify that content crafted to manipulate retrieval results is detected and rejected or quarantined before vectorization.
- 1.3.5: Verify that defenses against clean-label poisoning attacks are implemented.
- 3.5.2: Verify that RLHF training stages include automated detection of reward hacking or reward model over-optimization.
- 11.4.3: Verify that the safety violation feedback pipeline includes poisoning detection and human review gates to prevent adversarial manipulation of the improvement...

#### Cross-references

- LLM Top 10: LLM03, LLM04, LLM08, LLM05
- Agentic: ASI06, ASI04
- DSGAI: N/A
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI05 - Data Integrity and Validation Failures

AISVS requires schema validation at each system boundary. C7.1.1 validates model output, C9.3.2 validates tool output, C10.4.3 and C10.4.4 validate MCP parameters and messages, and C6.2.3 turns missing component metadata into a build failure rather than a silent gap.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that data integrity is provided when training data is stored and transferred. | [1.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Data integrity provided when training data is stored and transferred |
| Verify that the application validates all model outputs against a defined schema and rejects any output that does not match. | [7.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c71-output-format-enforcement) | Level 1. All model outputs validated against a defined schema and rejected when they do not match |
| Verify that tool outputs are validated against schemas. | [9.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Tool outputs validated against schemas |
| Verify that all MCP servers enforce strict schema validation. | [10.4.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c104-schema-message-and-input-validation) | Level 2. All MCP servers enforce strict schema validation |
| Verify that MCP servers reject unrecognized or oversized parameters in function calls. | [10.4.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c104-schema-message-and-input-validation) | Level 1. MCP servers reject unrecognized or oversized parameters in function calls |
| Verify that automatically generated labels are subject to confidence thresholds and consistency checks to detect misleading or low-confidence labels. | [1.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 2. Automatically generated labels subject to confidence thresholds and consistency checks |
| Verify that AI BOM completeness checks fail the build if any component metadata is missing. | [6.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C06-Supply-Chain.md#c62-ai-bom--supply-chain-monitoring) | Level 2. AI BOM completeness checks fail the build if any component metadata is missing, turning silent pipeline gaps into build failures |
| Verify that data drift detection monitors input distribution changes that may impact model performance, using statistically validated methods match... | [12.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c123-model-data-and-performance-drift-detection) | Level 1. Data drift detection monitors input distribution changes using statistically validated methods matched to the data type, catching silent pipeline corruption |
| Verify that in multi-stage fine-tuning pipelines, each stage's output is integrity-verified before it is consumed by the next stage. | [3.5.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c35-pipeline-fine-tuning) | Level 3. Each fine-tuning stage output integrity-verified before the next stage consumes it |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 7.1.1: Verify that the application validates all model outputs against a defined schema and rejects any output that does not match.
- 9.3.2: Verify that tool outputs are validated against schemas.
- 10.4.3: Verify that MCP servers reject unrecognized or oversized parameters in function calls.
- 12.3.1: Verify that data drift detection monitors input distribution changes that may impact model performance, using statistically validated methods matched to the ...

**Tier 2 - Short-term (first 30 days):**
- 1.1.3: Verify that data integrity is provided when training data is stored and transferred.
- 10.4.4: Verify that all MCP servers enforce strict schema validation.
- 1.3.2: Verify that automatically generated labels are subject to confidence thresholds and consistency checks to detect misleading or low-confidence labels.
- 6.2.3: Verify that AI BOM completeness checks fail the build if any component metadata is missing.

**Tier 3 - Strategic:**
- 3.5.3: Verify that in multi-stage fine-tuning pipelines, each stage's output is integrity-verified before it is consumed by the next stage.

#### Cross-references

- LLM Top 10: LLM05, LLM04, LLM01, LLM03
- Agentic: ASI02, ASI08, ASI04, ASI06
- DSGAI: DSGAI13, DSGAI04
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI06 - Tool Plugin and Agent Data Exchange

AISVS treats the tool boundary as a trust boundary with a declared contract. C9.3.3 and C9.3.4 require manifests to declare privileges and output validation and the runtime to enforce them, and C10.4.1 validates MCP responses against declared schemas before they enter the model context.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that tool outputs are validated against schemas. | [9.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Tool outputs validated against schemas |
| Verify that tool manifests declare required privileges, resource limits, and output validation requirements. | [9.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. Tool manifests declare required privileges, resource limits and output validation requirements |
| Verify that the runtime enforces the privileges, resource limits, and output-validation requirements declared in tool manifests. | [9.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. Runtime enforces the privileges, resource limits and output validation declared in manifests |
| Verify that MCP tools/list and tools/call responses are validated against their declared schemas before being injected into the model context. | [10.4.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c104-schema-message-and-input-validation) | Level 1. MCP tools/list and tools/call responses validated against declared schemas before injection into model context |
| Verify that MCP servers reject unrecognized or oversized parameters in function calls. | [10.4.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c104-schema-message-and-input-validation) | Level 1. MCP servers reject unrecognized or oversized parameters in function calls |
| Verify that MCP tools/list returns only tools permitted by resource owners' authorized scopes. | [10.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c102-authentication--authorization) | Level 2. MCP tools/list returns only tools permitted by the resource owner authorized scopes |
| Verify that there is architectural separation between processing of untrusted tool outputs and agent operations. | [9.3.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 2. Architectural separation between processing of untrusted tool outputs and agent operations |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 9.3.2: Verify that tool outputs are validated against schemas.
- 10.4.1: Verify that MCP tools/list and tools/call responses are validated against their declared schemas before being injected into the model context.
- 10.4.3: Verify that MCP servers reject unrecognized or oversized parameters in function calls.

**Tier 2 - Short-term (first 30 days):**
- 9.3.3: Verify that tool manifests declare required privileges, resource limits, and output validation requirements.
- 9.3.4: Verify that the runtime enforces the privileges, resource limits, and output-validation requirements declared in tool manifests.
- 10.2.4: Verify that MCP tools/list returns only tools permitted by resource owners' authorized scopes.
- 9.3.6: Verify that there is architectural separation between processing of untrusted tool outputs and agent operations.

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: LLM06, LLM03, LLM05, LLM02
- Agentic: ASI02, ASI04, ASI07, ASI06
- DSGAI: N/A
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI07 - Data Governance and Lifecycle

AISVS supplies the technical substrate governance depends on. C1.1.2 inventories every training-data source with license and use constraints, C12.5.1 records dataset lineage across transformations and merges, and C8.3 gives expiry and reset on the retrieval layer so deletion obligations reach the RAG store.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, int... | [1.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Current inventory of every training-data source with origin, responsible party, license, collection method, intended use constraints and processing history |
| Verify that dataset lineage records each dataset and its components, including all transformations, augmentations, and merges. | [12.5.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c125-training-data--model-lifecycle-audit) | Level 1. Dataset lineage records each dataset and its components including all transformations, augmentations and merges |
| Verify that every ingested document is tagged at write time with source, writer identity, and timestamp. | [12.5.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c125-training-data--model-lifecycle-audit) | Level 2. Every ingested document tagged at write time with source, writer identity and timestamp |
| Verify that a model registry maintains an inventory of all deployed model artifacts and their origin. | [3.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c31-model-authorization--integrity) | Level 1. Model registry maintains an inventory of all deployed model artifacts and their origin |
| Verify that expired vectors are excluded from retrieval results. | [8.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c83-memory-expiry--revocation) | Level 2. Expired vectors excluded from retrieval results, the retention control on the RAG layer |
| Verify that memory can be reset. | [8.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c83-memory-expiry--revocation) | Level 2. Memory can be reset, supporting deletion obligations against agent memory |
| Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs). | [5.2.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 3. Data classification labels propagate to downstream resources including embeddings, prompt caches and model outputs |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 12.5.1: Verify that dataset lineage records each dataset and its components, including all transformations, augmentations, and merges.
- 3.1.1: Verify that a model registry maintains an inventory of all deployed model artifacts and their origin.

**Tier 2 - Short-term (first 30 days):**
- 1.1.2: Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, intended use ...
- 12.5.4: Verify that every ingested document is tagged at write time with source, writer identity, and timestamp.
- 8.3.1: Verify that expired vectors are excluded from retrieval results.
- 8.3.2: Verify that memory can be reset.

**Tier 3 - Strategic:**
- 5.2.7: Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs).

#### Cross-references

- LLM Top 10: LLM02, LLM06, LLM03, LLM08
- Agentic: ASI03, ASI02, ASI06
- DSGAI: DSGAI08, DSGAI01
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI08 - Non-Compliance and Regulatory Violations

AISVS is a technical standard and deliberately excludes governance, so it meets this risk only where a regulatory obligation has a concrete technical control. C1.1.1 is data minimisation expressed as a verifiable requirement, and C12.5.1 lineage is the evidence base for deletion and data-subject requests.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that training data includes only features, attributes, and fields required for the model's stated purpose. | [1.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 1. Training data includes only features required for the model stated purpose, the technical expression of data minimisation and purpose limitation |
| Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, int... | [1.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Source inventory records license and intended use constraints per training-data source, evidencing lawful basis and use limitation |
| Verify that dataset lineage records each dataset and its components, including all transformations, augmentations, and merges. | [12.5.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c125-training-data--model-lifecycle-audit) | Level 1. Dataset lineage across transformations, augmentations and merges, the evidence base for deletion and data-subject obligations |
| Verify that sensitive information in labels is redacted, anonymized, or encrypted before being used in any labeling artifact. | [1.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c12-data-labeling-and-annotation-security) | Level 2. Sensitive information in labels redacted, anonymized or encrypted before use in any labeling artifact |
| Verify that training on sensitive datasets employs differentially-private optimization. | [11.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 2. Differentially-private optimization when training on sensitive datasets |
| Verify that models used in security-relevant decisions are evaluated for bias patterns. | [1.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 2. Models used in security-relevant decisions evaluated for bias patterns |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 1.1.1: Verify that training data includes only features, attributes, and fields required for the model's stated purpose.
- 12.5.1: Verify that dataset lineage records each dataset and its components, including all transformations, augmentations, and merges.

**Tier 2 - Short-term (first 30 days):**
- 1.1.2: Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, intended use ...
- 1.2.3: Verify that sensitive information in labels is redacted, anonymized, or encrypted before being used in any labeling artifact.
- 11.2.4: Verify that training on sensitive datasets employs differentially-private optimization.
- 1.3.3: Verify that models used in security-relevant decisions are evaluated for bias patterns.

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: LLM02, LLM08, LLM07, LLM01
- Agentic: ASI06, ASI01, ASI02, ASI03
- DSGAI: DSGAI07
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI09 - Multimodal Cross-Channel Leakage

AISVS extends input screening beyond text. C2.2.3 requires non-text inputs to be checked for adversarial perturbations, steganographic payloads and hidden embedded content, and C2.2.4 covers attacks coordinated across several modalities at once.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that non-text inputs (image/video/audio) are checked for adversarial perturbations, steganographic payloads, hidden or embedded content, or ... | [2.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c22-content--policy-screening) | Level 2. Non-text inputs including image, video and audio checked for adversarial perturbations, steganographic payloads, hidden or embedded content and known attack patterns, the direct control for the modality gap this risk names |
| Verify that coordinated attacks spanning multiple input types (e.g., steganographic payloads in images combined with prompt injection in text) are ... | [2.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c22-content--policy-screening) | Level 3. Coordinated attacks spanning multiple input types detected and blocked |
| Verify that model outputs are checked for hidden, encoded, or misleading content created through homoglyphs, formatting, metadata, or structured fi... | [7.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c73-output-safety) | Level 3. Outputs checked for hidden, encoded or misleading content created through homoglyphs, formatting, metadata or structured fields |
| Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped. | [8.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 1. Sensitive fields detected before embedding and masked, tokenized or dropped, applied to extracted multimodal content |
| Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive. | [5.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Post-inference filtering prevents responses including data the requester is not authorized to receive |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 8.2.1: Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped.

**Tier 2 - Short-term (first 30 days):**
- 2.2.3: Verify that non-text inputs (image/video/audio) are checked for adversarial perturbations, steganographic payloads, hidden or embedded content, or known atta...
- 5.2.4: Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive.

**Tier 3 - Strategic:**
- 2.2.4: Verify that coordinated attacks spanning multiple input types (e.g., steganographic payloads in images combined with prompt injection in text) are detected a...
- 7.3.4: Verify that model outputs are checked for hidden, encoded, or misleading content created through homoglyphs, formatting, metadata, or structured fields.

#### Cross-references

- LLM Top 10: LLM02, LLM04, LLM08, LLM03, LLM05
- Agentic: ASI03, ASI04
- DSGAI: DSGAI01, DSGAI14
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI10 - Synthetic Data and Anonymization Pitfalls

AISVS tests anonymisation empirically rather than accepting it as done. C11.2.5 requires membership-inference simulations to demonstrate attack accuracy no better than random guessing, and C11.2.4 requires differentially-private optimization where a formal guarantee is needed.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that membership-inference attack simulations demonstrate that attack accuracy does not exceed random guessing on evaluated data. | [11.2.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 3. Membership-inference attack simulations demonstrate attack accuracy does not exceed random guessing, the direct re-identification test |
| Verify that training on sensitive datasets employs differentially-private optimization. | [11.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 2. Training on sensitive datasets employs differentially-private optimization, the formal guarantee ad hoc anonymisation lacks |
| Verify that model outputs are calibrated to reduce overconfident predictions. | [11.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 2. Model outputs calibrated to reduce overconfident predictions, lowering the signal linkage attacks exploit |
| Verify that sensitive information in labels is redacted, anonymized, or encrypted before being used in any labeling artifact. | [1.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c12-data-labeling-and-annotation-security) | Level 2. Sensitive information in labels redacted, anonymized or encrypted before use in any labeling artifact |
| Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped. | [8.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 1. Sensitive fields detected before embedding and masked, tokenized or dropped |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 8.2.1: Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped.

**Tier 2 - Short-term (first 30 days):**
- 11.2.4: Verify that training on sensitive datasets employs differentially-private optimization.
- 11.2.3: Verify that model outputs are calibrated to reduce overconfident predictions.
- 1.2.3: Verify that sensitive information in labels is redacted, anonymized, or encrypted before being used in any labeling artifact.

**Tier 3 - Strategic:**
- 11.2.5: Verify that membership-inference attack simulations demonstrate that attack accuracy does not exceed random guessing on evaluated data.

#### Cross-references

- LLM Top 10: LLM02, LLM01, LLM08, LLM09, LLM03
- Agentic: ASI03, ASI06, ASI09
- DSGAI: DSGAI08, DSGAI18
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI11 - Cross-Context Conversation Bleed

AISVS addresses context bleed as a tenancy and session lifecycle problem. C5.3.1 stops one tenant's operations influencing or observing another's on shared serving infrastructure, C8.1.1 enforces per-tenant namespace uniqueness, and C10.2.6 removes session artifacts at termination.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that shared model serving infrastructure prevents one tenant's fine-tuning, inference, or embedding operations from influencing or observing... | [5.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c53-multi-tenant-isolation) | Level 2. Shared model serving infrastructure prevents one tenant fine-tuning, inference or embedding operations from influencing or observing another tenant, the direct control |
| Verify that vector identifiers and namespaces enforce uniqueness per tenant and prevent cross-tenant collisions. | [8.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c81-access-controls-on-memory--rag-indices) | Level 1. Vector identifiers and namespaces enforce per-tenant uniqueness and prevent cross-tenant collisions |
| Verify that model versions running in parallel use isolated runtime state so that AI-specific shared resources are not shared across deployments. | [3.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c33-controlled-deployment--rollback) | Level 2. Model versions running in parallel use isolated runtime state so AI-specific shared resources are not shared across deployments |
| Verify that MCP servers ensure all session artifacts are removed when a session terminates. | [10.2.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c102-authentication--authorization) | Level 2. MCP servers ensure all session artifacts are removed when a session terminates |
| Verify that memory can be reset. | [8.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c83-memory-expiry--revocation) | Level 2. Memory can be reset, so residual context from a prior session can be cleared rather than carried into the next |
| Verify that one tenant cannot influence or observe another tenant's operations through shared compute resources. Satisfying this requirement typica... | [5.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c53-multi-tenant-isolation) | Level 3. Hardware partitioning, confidential computing or dedicated per-tenant compute so one tenant cannot influence or observe another through shared compute |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 8.1.1: Verify that vector identifiers and namespaces enforce uniqueness per tenant and prevent cross-tenant collisions.

**Tier 2 - Short-term (first 30 days):**
- 5.3.1: Verify that shared model serving infrastructure prevents one tenant's fine-tuning, inference, or embedding operations from influencing or observing another t...
- 3.3.3: Verify that model versions running in parallel use isolated runtime state so that AI-specific shared resources are not shared across deployments.
- 10.2.6: Verify that MCP servers ensure all session artifacts are removed when a session terminates.
- 8.3.2: Verify that memory can be reset.

**Tier 3 - Strategic:**
- 5.3.2: Verify that one tenant cannot influence or observe another tenant's operations through shared compute resources. Satisfying this requirement typically requir...

#### Cross-references

- LLM Top 10: LLM02, LLM07, LLM03, LLM08
- Agentic: ASI06, ASI03
- DSGAI: DSGAI13
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI12 - Unsafe Natural Language Data Gateways

AISVS answers the NL-to-query bypass directly. C9.5.3 requires every access control decision to be made by application logic or a policy engine and never by the model, and C5.2.2 keeps the end-user authorization context enforced through the retrieval path rather than a service account.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that all access control decisions are enforced by application logic or a policy engine, never by the AI model itself. | [9.5.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. All access control decisions enforced by application logic or a policy engine, never by the AI model itself, the direct answer to NL-to-query authorization bypass |
| Verify that retrieval pipelines (e.g., RAG queries, embedding lookups) enforce the end-user's authorization context at each retrieval and assembly ... | [5.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Retrieval pipelines enforce the end-user authorization context at each retrieval and assembly stage rather than the service account permissions |
| Verify that agent actions are authorized against fine-grained policies enforced by the runtime that restrict which tools an agent may invoke, and w... | [9.5.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. Fine-grained runtime policy over which tools an agent may invoke and which parameter values it may supply, constraining generated queries |
| Verify that all inputs that could steer model behavior are treated as untrusted and screened by a prompt injection detection ruleset or classifier,... | [2.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 1. All inputs able to steer model behavior screened by an injection ruleset or classifier |
| Verify that tool outputs are validated against schemas. | [9.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Tool outputs validated against schemas |
| Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive. | [5.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Post-inference filtering prevents responses including data the requester is not authorized to receive |
| Verify that each high-impact action has a trusted reversibility classification, such as read-only, reversible, externally reversible, or irreversible. | [9.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 2. High-impact actions carry a trusted reversibility classification, distinguishing read queries from data-store mutations |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 2.1.3: Verify that all inputs that could steer model behavior are treated as untrusted and screened by a prompt injection detection ruleset or classifier, with flag...
- 9.3.2: Verify that tool outputs are validated against schemas.

**Tier 2 - Short-term (first 30 days):**
- 9.5.3: Verify that all access control decisions are enforced by application logic or a policy engine, never by the AI model itself.
- 5.2.2: Verify that retrieval pipelines (e.g., RAG queries, embedding lookups) enforce the end-user's authorization context at each retrieval and assembly stage, rat...
- 9.5.1: Verify that agent actions are authorized against fine-grained policies enforced by the runtime that restrict which tools an agent may invoke, and which param...
- 5.2.4: Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive.
- 9.2.3: Verify that each high-impact action has a trusted reversibility classification, such as read-only, reversible, externally reversible, or irreversible.

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: LLM05, LLM01, LLM02, LLM03, LLM09
- Agentic: ASI02, ASI05, ASI01, ASI04, ASI09
- DSGAI: DSGAI14
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI13 - Vector Store Platform Security

AISVS covers the vector store as a first-class AI resource. C5.2.1 requires default-deny access control on vector collections and embedding indices, and C8.1 plus C8.2 add namespace isolation, metadata immutability, scope-constrained retrieval and adversarial vector quarantine.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that every AI resource (datasets, endpoints, vector collections, embedding indices, compute instances) enforces access controls with explici... | [5.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Every AI resource including vector collections and embedding indices enforces access controls with explicit allow-lists and default-deny policies, the direct platform control |
| Verify that vector identifiers and namespaces enforce uniqueness per tenant and prevent cross-tenant collisions. | [8.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c81-access-controls-on-memory--rag-indices) | Level 1. Vector identifiers and namespaces enforce per-tenant uniqueness and prevent cross-tenant collisions |
| Verify that retrieval operations enforce scope constraints. | [8.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c81-access-controls-on-memory--rag-indices) | Level 2. Retrieval operations enforce scope constraints |
| Verify that document metadata tags are immutable after the initial write. | [8.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c81-access-controls-on-memory--rag-indices) | Level 2. Document metadata tags immutable after initial write |
| Verify that vectors that fall outside normal clustering patterns are flagged and quarantined before entering production indices. | [8.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 2. Vectors outside normal clustering patterns flagged and quarantined before entering production indices, the adversarial-vector injection control |
| Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped. | [8.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 1. Sensitive fields detected before embedding and masked, tokenized or dropped, limiting what embedding inversion can recover |
| Verify that expired vectors are excluded from retrieval results. | [8.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c83-memory-expiry--revocation) | Level 2. Expired vectors excluded from retrieval results |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 8.1.1: Verify that vector identifiers and namespaces enforce uniqueness per tenant and prevent cross-tenant collisions.
- 8.2.1: Verify that sensitive fields are detected before embedding and are masked, tokenized, or dropped.

**Tier 2 - Short-term (first 30 days):**
- 5.2.1: Verify that every AI resource (datasets, endpoints, vector collections, embedding indices, compute instances) enforces access controls with explicit allow-li...
- 8.1.3: Verify that retrieval operations enforce scope constraints.
- 8.1.2: Verify that document metadata tags are immutable after the initial write.
- 8.2.2: Verify that vectors that fall outside normal clustering patterns are flagged and quarantined before entering production indices.
- 8.3.1: Verify that expired vectors are excluded from retrieval results.

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: LLM08, LLM07, LLM06, LLM03
- Agentic: ASI06, ASI05, ASI01, ASI02
- DSGAI: N/A
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI14 - Excessive Telemetry and Monitoring Leakage

AISVS bounds what telemetry carries rather than only requiring more of it. C12.1.3 fixes a structured schema for inference logs, C12.1.2 and C12.1.4 scope safety-decision and RAG retrieval logging to defined purposes, and C9.5.4 keeps credentials out of the tool parameters that reach logs.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that log entries for AI inference events follow a structured, interoperable schema that includes at least the model identifier, token usage ... | [12.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c121-request--response-logging) | Level 2. Log entries for inference events follow a structured, interoperable schema with a defined field set (model identifier, token usage, provider, operation type), bounding what telemetry carries |
| Verify that secrets and credentials required by an agent at runtime are not exposed within the model's observable context, including the context wi... | [9.5.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c95-agent-authorization-delegation-and-continuous-enforcement) | Level 2. Secrets and credentials not exposed within the model observable context including tool call parameters, which are a primary source of credentials reaching logs |
| Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs). | [5.2.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 3. Data classification labels propagate to downstream resources, so sensitive content retains its handling requirement when it reaches telemetry |
| Verify that sensitive information in labels is redacted, anonymized, or encrypted before being used in any labeling artifact. | [1.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c12-data-labeling-and-annotation-security) | Level 2. Sensitive information redacted, anonymized or encrypted before being used in any labeling artifact |
| Verify that RAG pipeline retrieval events are logged, including the query, documents retrieved, and knowledge source. | [12.1.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c121-request--response-logging) | Level 2. RAG retrieval events logged with query, documents retrieved and knowledge source, which is exactly the high-value content this risk says logging infrastructure accumulates |
| Verify that safety filtering and policy decisions are logged with sufficient detail to support audit, debugging, and forensic analysis of content m... | [12.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c121-request--response-logging) | Level 2. Safety filtering and policy decisions logged with sufficient detail for audit, debugging and forensics, scoping moderation telemetry to a defined purpose |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- No AISVS Level 1 requirement maps to this entry

**Tier 2 - Short-term (first 30 days):**
- 12.1.3: Verify that log entries for AI inference events follow a structured, interoperable schema that includes at least the model identifier, token usage (input and...
- 9.5.4: Verify that secrets and credentials required by an agent at runtime are not exposed within the model's observable context, including the context window, syst...
- 1.2.3: Verify that sensitive information in labels is redacted, anonymized, or encrypted before being used in any labeling artifact.
- 12.1.4: Verify that RAG pipeline retrieval events are logged, including the query, documents retrieved, and knowledge source.
- 12.1.2: Verify that safety filtering and policy decisions are logged with sufficient detail to support audit, debugging, and forensic analysis of content moderation ...

**Tier 3 - Strategic:**
- 5.2.7: Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs).

#### Cross-references

- LLM Top 10: LLM02, LLM03, LLM06
- Agentic: ASI09, ASI02
- DSGAI: DSGAI01, DSGAI07, DSGAI12
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI15 - Over-Broad Context Windows

AISVS keeps authorization attached to content as the context is assembled. C5.2.2 requires enforcement at each retrieval and assembly stage rather than once at the start, C2.1.6 maintains instruction hierarchy inside a mixed-trust context, and C2.1.4 rejects oversized input rather than truncating it.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that retrieval pipelines (e.g., RAG queries, embedding lookups) enforce the end-user's authorization context at each retrieval and assembly ... | [5.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Retrieval pipelines enforce the end-user authorization context at each retrieval AND assembly stage, the direct control for a context assembled from multiple sources |
| Verify that input length controls prevent content from exceeding the context window. The controls must reject inputs that exceed token limits rathe... | [2.1.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 1. Input length controls reject inputs exceeding token limits rather than truncating them |
| Verify that retrieval operations enforce scope constraints. | [8.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c81-access-controls-on-memory--rag-indices) | Level 2. Retrieval operations enforce scope constraints |
| Verify that the system enforces an instruction hierarchy in which system and developer messages override user instructions and other untrusted inpu... | [2.1.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C02-Input-Validation.md#c21-prompt-injection-defenses) | Level 2. Instruction hierarchy maintains trust separation inside a context holding mixed-trust content |
| Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive. | [5.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 2. Post-inference filtering prevents responses including data the requester is not authorized to receive |
| Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs). | [5.2.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 3. Classification labels propagate to prompt caches and model outputs |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 2.1.4: Verify that input length controls prevent content from exceeding the context window. The controls must reject inputs that exceed token limits rather than tru...

**Tier 2 - Short-term (first 30 days):**
- 5.2.2: Verify that retrieval pipelines (e.g., RAG queries, embedding lookups) enforce the end-user's authorization context at each retrieval and assembly stage, rat...
- 8.1.3: Verify that retrieval operations enforce scope constraints.
- 2.1.6: Verify that the system enforces an instruction hierarchy in which system and developer messages override user instructions and other untrusted inputs, even a...
- 5.2.4: Verify that post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive.

**Tier 3 - Strategic:**
- 5.2.7: Verify that data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs).

#### Cross-references

- LLM Top 10: LLM07, LLM02, LLM08, LLM06
- Agentic: ASI01, ASI06, ASI02
- DSGAI: DSGAI03
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI16 - Endpoint and Browser Overreach

AISVS covers endpoint assistants through the local MCP and sandboxing requirements. C10.1.3 requires locally launched servers to run least-privilege with restricted file system and network access, C10.4.7 requires explicit install consent, and C7.3.3 blocks the outbound request path.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that locally launched MCP servers run in a least-privilege sandbox with restricted file system, network, and system access. | [10.1.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c101-component-integrity) | Level 2. Locally launched MCP servers run in a least-privilege sandbox with restricted file system, network and system access, the direct control for local assistant overreach |
| Verify that MCP clients present users with explicit consent dialogue and cancellation options upon installation of a local MCP server. | [10.4.7](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C10-MCP-Security.md#c104-schema-message-and-input-validation) | Level 2. MCP clients present users with explicit consent dialogue and cancellation options upon installation of a local MCP server |
| Verify that each tool/plugin executes in a least-privilege sandbox or is otherwise isolated from model operations. | [9.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c93-component-isolation-and-tool-authorization) | Level 1. Each tool or plugin executes in a least-privilege sandbox or is isolated from model operations |
| Verify that inference runtimes enforce process, memory, and file access isolation. | [4.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C04-Infrastructure.md#c43-edge--distributed-ai-security) | Level 3. Inference runtimes enforce process, memory and file access isolation |
| Verify that the agent runtime blocks execution of privileged, high-impact, or irreversible actions until explicit human approval is received and ve... | [9.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C09-Orchestration-and-Agentic-Action.md#c92-high-impact-action-approval-and-irreversibility-controls) | Level 1. Agent runtime blocks privileged, high-impact or irreversible actions until explicit human approval is received and verified |
| Verify that model-generated output is prevented from triggering outbound requests. | [7.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c73-output-safety) | Level 2. Model-generated output prevented from triggering outbound requests, the exfiltration-to-provider path |
| Verify that edge AI devices authenticate to central infrastructure using strong authentication mechanisms. | [4.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C04-Infrastructure.md#c43-edge--distributed-ai-security) | Level 1. Edge AI devices authenticate to central infrastructure using strong authentication mechanisms |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 9.3.1: Verify that each tool/plugin executes in a least-privilege sandbox or is otherwise isolated from model operations.
- 9.2.1: Verify that the agent runtime blocks execution of privileged, high-impact, or irreversible actions until explicit human approval is received and verified.
- 4.3.1: Verify that edge AI devices authenticate to central infrastructure using strong authentication mechanisms.

**Tier 2 - Short-term (first 30 days):**
- 10.1.3: Verify that locally launched MCP servers run in a least-privilege sandbox with restricted file system, network, and system access.
- 10.4.7: Verify that MCP clients present users with explicit consent dialogue and cancellation options upon installation of a local MCP server.
- 7.3.3: Verify that model-generated output is prevented from triggering outbound requests.

**Tier 3 - Strategic:**
- 4.3.3: Verify that inference runtimes enforce process, memory, and file access isolation.

#### Cross-references

- LLM Top 10: LLM06, LLM03, LLM08, LLM01, LLM02
- Agentic: ASI10, ASI02, ASI03, ASI07, ASI09
- DSGAI: DSGAI03, DSGAI17
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI17 - Data Availability and Resilience Failures

AISVS covers resilience through lifecycle controls rather than a backup chapter. C3.3.1 and C3.3.2 require automated rollback triggers and complete model state restoration, C3.5.4 registers fine-tuning checkpoints as discrete recovery points, and C12.5.1 lineage enables reconstruction.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that production deployments implement rollout mechanisms with automated rollback triggers. | [3.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c33-controlled-deployment--rollback) | Level 2. Production deployments implement rollout mechanisms with automated rollback triggers |
| Verify that rollback capabilities restore the complete model state. | [3.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c33-controlled-deployment--rollback) | Level 2. Rollback capabilities restore the complete model state |
| Verify that integrity monitoring is applied to guard against unauthorized modifications or corruption of training data. | [1.1.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Integrity monitoring guards training data against unauthorized modification or corruption, detecting the corruption event that recovery must answer |
| Verify that fine-tuning checkpoints are registered as distinct artifacts. | [3.5.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C03-Model-Lifecycle-Management.md#c35-pipeline-fine-tuning) | Level 3. Fine-tuning checkpoints registered as distinct artifacts, giving discrete recovery points |
| Verify that dataset lineage records each dataset and its components, including all transformations, augmentations, and merges. | [12.5.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c125-training-data--model-lifecycle-audit) | Level 1. Dataset lineage records each dataset and its components including transformations, augmentations and merges, enabling reconstruction |
| Verify that memory can be reset. | [8.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c83-memory-expiry--revocation) | Level 2. Memory can be reset, giving a defined recovery action for a corrupted agent memory or RAG store |
| Verify that all model changes generate immutable audit records. | [12.5.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c125-training-data--model-lifecycle-audit) | Level 2. All model changes generate immutable audit records, establishing the known-good state to recover to |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 12.5.1: Verify that dataset lineage records each dataset and its components, including all transformations, augmentations, and merges.

**Tier 2 - Short-term (first 30 days):**
- 3.3.1: Verify that production deployments implement rollout mechanisms with automated rollback triggers.
- 3.3.2: Verify that rollback capabilities restore the complete model state.
- 1.1.4: Verify that integrity monitoring is applied to guard against unauthorized modifications or corruption of training data.
- 8.3.2: Verify that memory can be reset.
- 12.5.3: Verify that all model changes generate immutable audit records.

**Tier 3 - Strategic:**
- 3.5.4: Verify that fine-tuning checkpoints are registered as distinct artifacts.

#### Cross-references

- LLM Top 10: LLM10, LLM03, LLM04, LLM09
- Agentic: ASI08, ASI07, ASI09
- DSGAI: N/A
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI18 - Inference and Data Reconstruction

AISVS gives reconstruction defense its own section. C11.2 requires differentially-private training, calibrated outputs, threat-model-sized rate limits and empirical membership-inference testing, and C1.1.1 bounds what could be reconstructed by limiting what was trained on.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that membership-inference attack simulations demonstrate that attack accuracy does not exceed random guessing on evaluated data. | [11.2.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 3. Membership-inference attack simulations demonstrate attack accuracy does not exceed random guessing on evaluated data |
| Verify that training on sensitive datasets employs differentially-private optimization. | [11.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 2. Training on sensitive datasets employs differentially-private optimization |
| Verify that inference endpoints enforce per-principal and global rate limits sized to the extraction threat model, and not solely as a generic API ... | [11.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 1. Inference endpoints enforce per-principal and global rate limits sized to the extraction threat model rather than as a generic API throttle |
| Verify that model-inferred sensitive attributes are not directly returned in outputs. | [11.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 1. Model-inferred sensitive attributes not returned directly in outputs |
| Verify that model outputs are calibrated to reduce overconfident predictions. | [11.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 2. Model outputs calibrated to reduce overconfident predictions, lowering the confidence signal reconstruction attacks exploit |
| Verify that raw model outputs are not directly exposed beyond the application backend, and that externally visible responses are calibrated to the ... | [11.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c113-model-extraction-defense) | Level 2. Raw model outputs not exposed beyond the application backend, with externally visible responses calibrated to the extraction risk level |
| Verify that training data includes only features, attributes, and fields required for the model's stated purpose. | [1.1.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 1. Training data includes only features required for the stated purpose, bounding what can be reconstructed |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 11.2.2: Verify that inference endpoints enforce per-principal and global rate limits sized to the extraction threat model, and not solely as a generic API throttle.
- 11.2.1: Verify that model-inferred sensitive attributes are not directly returned in outputs.
- 1.1.1: Verify that training data includes only features, attributes, and fields required for the model's stated purpose.

**Tier 2 - Short-term (first 30 days):**
- 11.2.4: Verify that training on sensitive datasets employs differentially-private optimization.
- 11.2.3: Verify that model outputs are calibrated to reduce overconfident predictions.
- 11.3.2: Verify that raw model outputs are not directly exposed beyond the application backend, and that externally visible responses are calibrated to the extraction...

**Tier 3 - Strategic:**
- 11.2.5: Verify that membership-inference attack simulations demonstrate that attack accuracy does not exceed random guessing on evaluated data.

#### Cross-references

- LLM Top 10: LLM02, LLM08, LLM06, LLM05, LLM09
- Agentic: ASI04, ASI09
- DSGAI: DSGAI10, DSGAI15
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI19 - Human-in-Loop and Labeler Overexposure

AISVS addresses annotator exposure in the labeling section. C1.2.3 requires sensitive information in labels to be redacted, anonymized or encrypted before use in any labeling artifact, and C1.2.1 restricts who can create, modify or approve annotations.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that sensitive information in labels is redacted, anonymized, or encrypted before being used in any labeling artifact. | [1.2.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c12-data-labeling-and-annotation-security) | Level 2. Sensitive information in labels redacted, anonymized or encrypted before being used in any labeling artifact, the direct control for annotator exposure |
| Verify that labeling platforms enforce access controls that restrict who can create, modify, or approve annotations. | [1.2.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c12-data-labeling-and-annotation-security) | Level 1. Labeling platforms enforce access controls restricting who can create, modify or approve annotations |
| Verify that disallowed content is detected and removed before training. | [1.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 2. Disallowed content detected and removed before training, reducing harmful content reaching human reviewers |
| Verify that cryptographic integrity is applied to labeling artifacts. | [1.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c12-data-labeling-and-annotation-security) | Level 2. Cryptographic integrity applied to labeling artifacts |
| Verify that all labeling activities are recorded in logs. | [12.5.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c125-training-data--model-lifecycle-audit) | Level 1. All labeling activities recorded in logs |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 1.2.1: Verify that labeling platforms enforce access controls that restrict who can create, modify, or approve annotations.
- 12.5.2: Verify that all labeling activities are recorded in logs.

**Tier 2 - Short-term (first 30 days):**
- 1.2.3: Verify that sensitive information in labels is redacted, anonymized, or encrypted before being used in any labeling artifact.
- 1.3.4: Verify that disallowed content is detected and removed before training.
- 1.2.2: Verify that cryptographic integrity is applied to labeling artifacts.

**Tier 3 - Strategic:**
- No AISVS Level 3 requirement maps to this entry

#### Cross-references

- LLM Top 10: LLM02, LLM05, LLM03
- Agentic: ASI10, ASI04
- DSGAI: DSGAI07, DSGAI08
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI20 - Model Exfiltration and IP Replication

AISVS treats extraction as a detect-and-respond problem as well as a prevention one. C11.3 requires query-pattern analysis feeding an extraction detector, response measures on detection, and watermarking or fingerprinting so unauthorized copies remain identifiable.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that query-pattern analysis feeds an extraction-attempt detector. | [11.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c113-model-extraction-defense) | Level 1. Query-pattern analysis feeds an extraction-attempt detector |
| Verify that inference endpoints enforce per-principal and global rate limits sized to the extraction threat model, and not solely as a generic API ... | [11.2.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c112-membership-inference-and-model-inversion-mitigation) | Level 1. Inference endpoints enforce per-principal and global rate limits sized to the extraction threat model |
| Verify that raw model outputs are not directly exposed beyond the application backend, and that externally visible responses are calibrated to the ... | [11.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c113-model-extraction-defense) | Level 2. Raw model outputs not exposed beyond the application backend, with externally visible responses calibrated to the extraction risk level |
| Verify that detection of suspected extraction triggers response measures. | [11.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c113-model-extraction-defense) | Level 3. Detection of suspected extraction triggers response measures |
| Verify that model watermarking or fingerprinting techniques are applied so that unauthorized copies can be identified. | [11.3.3](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C11-Adversarial-Robustness.md#c113-model-extraction-defense) | Level 3. Model watermarking or fingerprinting so unauthorized copies can be identified |
| Verify that confidential inference services protect model weights during runtime through isolated execution environments. | [4.1.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C04-Infrastructure.md#c41-ai-workload-sandboxing--validation) | Level 3. Confidential inference services protect model weights during runtime through isolated execution environments |
| Verify that model weights and sensitive parameters stored locally are encrypted using hardware-backed key stores or secure enclaves. | [4.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C04-Infrastructure.md#c43-edge--distributed-ai-security) | Level 3. Model weights and sensitive parameters stored locally encrypted using hardware-backed key stores or secure enclaves |
| Verify that privileged access to model weights, training pipelines, and production AI configuration is granted just in time, with a defined maximum... | [5.2.6](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C05-Access-Control-and-Identity.md#c52-ai-resource-authorization--classification) | Level 3. Just-in-time privileged access to model weights with maximum session duration and automatic expiry |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 11.3.1: Verify that query-pattern analysis feeds an extraction-attempt detector.
- 11.2.2: Verify that inference endpoints enforce per-principal and global rate limits sized to the extraction threat model, and not solely as a generic API throttle.

**Tier 2 - Short-term (first 30 days):**
- 11.3.2: Verify that raw model outputs are not directly exposed beyond the application backend, and that externally visible responses are calibrated to the extraction...

**Tier 3 - Strategic:**
- 11.3.4: Verify that detection of suspected extraction triggers response measures.
- 11.3.3: Verify that model watermarking or fingerprinting techniques are applied so that unauthorized copies can be identified.
- 4.1.4: Verify that confidential inference services protect model weights during runtime through isolated execution environments.
- 4.3.4: Verify that model weights and sensitive parameters stored locally are encrypted using hardware-backed key stores or secure enclaves.
- 5.2.6: Verify that privileged access to model weights, training pipelines, and production AI configuration is granted just in time, with a defined maximum session d...

#### Cross-references

- LLM Top 10: LLM02, LLM04, LLM07, LLM05
- Agentic: ASI04
- DSGAI: DSGAI18, DSGAI04
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

### DSGAI21 - Disinformation via Data Poisoning

AISVS covers disinformation injection through the same controls as poisoning, plus provenance. C1.3 detects poisoned and disallowed training content, C8.2.4 covers the RAG corpus path, and C7.4 attribution lets a reader trace a claim back to its source document.

#### AISVS mapping

| AISVS requirement | Control | How it applies |
|---|---|---|
| Verify that training and fine-tuning pipelines implement poisoning detection techniques to identify potential data poisoning or unintentional corru... | [1.3.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 2. Training and fine-tuning pipelines implement poisoning detection |
| Verify that disallowed content is detected and removed before training. | [1.3.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 2. Disallowed content detected and removed before training |
| Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, int... | [1.1.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c11-training-data-origin--data-security) | Level 2. Current inventory of every training-data source with origin, responsible party and collection method, enabling attribution of an injected corpus |
| Verify that content crafted to manipulate retrieval results is detected and rejected or quarantined before vectorization. | [8.2.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C08-Memory-Embeddings-and-Vector-Database.md#c82-embedding-sanitization--validation) | Level 3. Content crafted to manipulate retrieval results detected and rejected or quarantined before vectorization, the RAG-corpus disinformation path |
| Verify that defenses against clean-label poisoning attacks are implemented. | [1.3.5](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C01-Training-Data-Integrity-and-Traceability.md#c13-training-data-quality-and-security-assurance) | Level 3. Clean-label poisoning defenses, which is the form targeted disinformation injection usually takes |
| Verify that responses generated using retrieval-augmented generation (RAG) include attribution to the source documents. | [7.4.1](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c74-source-attribution--citation-integrity) | Level 1. RAG responses include attribution to the source documents, letting a reader check a poisoned claim against its source |
| Verify that hallucination detection monitors identify and flag model outputs that contain factually incorrect, inconsistent, or fabricated informat... | [12.3.2](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C12-Monitoring-and-Logging.md#c123-model-data-and-performance-drift-detection) | Level 2. Hallucination detection monitors identify and flag factually incorrect, inconsistent or fabricated output |
| Verify that generated media is watermarked to prove it was AI-generated. | [7.4.4](https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-C07-Model-Behavior.md#c74-source-attribution--citation-integrity) | Level 3. Generated media watermarked to prove it was AI-generated |

#### Three-tier mitigations

**Tier 1 - Immediate (pre-production gate):**
- 7.4.1: Verify that responses generated using retrieval-augmented generation (RAG) include attribution to the source documents.

**Tier 2 - Short-term (first 30 days):**
- 1.3.1: Verify that training and fine-tuning pipelines implement poisoning detection techniques to identify potential data poisoning or unintentional corruption in t...
- 1.3.4: Verify that disallowed content is detected and removed before training.
- 1.1.2: Verify that an up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, intended use ...
- 12.3.2: Verify that hallucination detection monitors identify and flag model outputs that contain factually incorrect, inconsistent, or fabricated information.

**Tier 3 - Strategic:**
- 8.2.4: Verify that content crafted to manipulate retrieval results is detected and rejected or quarantined before vectorization.
- 1.3.5: Verify that defenses against clean-label poisoning attacks are implemented.
- 7.4.4: Verify that generated media is watermarked to prove it was AI-generated.

#### Cross-references

- LLM Top 10: LLM04, LLM09, LLM06, LLM07, LLM02
- Agentic: ASI06, ASI09, ASI02
- DSGAI: DSGAI01, DSGAI03, DSGAI07, DSGAI08, DSGAI02, DSGAI06, DSGAI12, DSGAI13, DSGAI04, DSGAI05, DSGAI11, DSGAI18, DSGAI17, DSGAI14, DSGAI15, DSGAI09, DSGAI16, DSGAI10, DSGAI19, DSGAI20
- See also: the AISVS chapters listed above at https://github.com/OWASP/AISVS/tree/main/1.0/en

---

## Implementation priority table

| Priority | AISVS components | Entries addressed |
|---|---|---|
| P1 - Pre-production gate | All Level 1 requirements | DSGAI01, DSGAI02, DSGAI03, DSGAI05, DSGAI06, DSGAI07, DSGAI08, DSGAI09, DSGAI10, DSGAI11, DSGAI12, DSGAI13, DSGAI15, DSGAI16, DSGAI17, DSGAI18, DSGAI19, DSGAI20, DSGAI21 |
| P2 - First 30 days | All Level 2 requirements | DSGAI01, DSGAI02, DSGAI03, DSGAI04, DSGAI05, DSGAI06, DSGAI07, DSGAI08, DSGAI09, DSGAI10, DSGAI11, DSGAI12, DSGAI13, DSGAI14, DSGAI15, DSGAI16, DSGAI17, DSGAI18, DSGAI19, DSGAI20, DSGAI21 |
| P3 - Programme maturity | All Level 3 requirements | DSGAI01, DSGAI02, DSGAI03, DSGAI04, DSGAI05, DSGAI07, DSGAI09, DSGAI10, DSGAI11, DSGAI14, DSGAI15, DSGAI16, DSGAI17, DSGAI18, DSGAI20, DSGAI21 |

---

## References

- [OWASP AISVS project page](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/)
- [OWASP AISVS 1.0 frozen text](https://github.com/OWASP/AISVS/tree/main/1.0/en)
- [OWASP GenAI Data Security Risks 2026 - OWASP](https://genai.owasp.org/resource/genai-data-security-risks/)
- [shared/TEMPLATE.md](../shared/TEMPLATE.md)

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-28 | Initial release - full mapping of DSGAI01-DSGAI21 to OWASP AISVS 1.0 |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) - maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
*License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
