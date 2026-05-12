<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : MAESTRO — Multi-Agent Environment, Security, Threat, Risk, and Outcome
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × MAESTRO

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
(Multi-Agent Environment, Security, Threat, Risk, and Outcome) —
the Cloud Security Alliance's threat modeling framework designed
specifically for the unique challenges of agentic AI systems.

**Created by:** Ken Huang, CEO & Chief AI Officer, DistributedApps.ai;
Co-Chair of AI Safety Working Groups, Cloud Security Alliance.

**Official repository:** https://github.com/CloudSecurityAlliance/MAESTRO

---

## Why MAESTRO for agentic AI threat modeling

Every other framework in this crosswalk maps an agentic risk to a
control, a compliance article, or a testing procedure. MAESTRO does
something different — it maps each risk to the **architectural layer
where it originates**. This distinction matters for three reasons:

**Root cause precision.** A goal hijack (ASI01) originates at L1
Foundation Models — the layer where the model interprets instructions.
A supply chain compromise (ASI04) originates at L3 Agent Frameworks
or L4 Deployment & Infrastructure. Knowing the originating layer
tells you which team owns the risk and where the countermeasure must
be deployed. No other framework in this repo provides that answer.

**Threat modeling before control selection.** MAESTRO is a threat
modeling methodology, not a control framework. Its role in a security
programme is upstream of ISO 27001, CIS Controls, or ASVS — you use
MAESTRO to enumerate threats by layer, then use those other frameworks
to select controls. This file is the "what are the threats and where
do they live architecturally" answer that precedes every other file
in this folder.

**OWASP ecosystem alignment.** MAESTRO is cited by the OWASP GenAI
Security Project's Multi-Agentic System Threat Modeling Guide v1.0
as the framework for threat modeling complex AI systems. Ken Huang is
a core contributor to the OWASP LLM Top 10. This framework is already
inside the OWASP GenAI ecosystem.

---

## MAESTRO seven-layer architecture

MAESTRO decomposes every agentic AI system into seven functional
layers, each with its own threat surface, trust boundaries, and
control responsibilities:

| Layer | ID | Description | Threat theme |
|---|---|---|---|
| Foundation Models | L1 | Base LLMs providing core reasoning and generation | Model-level manipulation, extraction, misalignment |
| Data Operations | L2 | Ingestion pipelines, storage, RAG, embeddings, vector stores | Data poisoning, PII exfiltration, retrieval compromise |
| Agent Frameworks | L3 | Orchestration platforms, tool registries, MCP, plugin ecosystems | Tool misuse, orchestration injection, supply chain |
| Deployment & Infrastructure | L4 | Servers, containers, networks, CI/CD, runtime environments | Infrastructure compromise, code execution, sandbox escape |
| Evaluation & Observability | L5 | Monitoring, logging, telemetry, behavioural baselines, drift detection | Blind spots, rogue behaviour detection failure, evasion |
| Security & Compliance | L6 | Identity, access control, audit, governance, credential management | Privilege abuse, credential exposure, policy failure |
| Agent Ecosystem | L7 | Multi-agent interaction, A2A communication, cascade dynamics | Lateral movement, cascading failures, trust exploitation |

Each layer has distinct trust boundaries. Threats originating at one
layer propagate upward through dependent layers — a L1 model
vulnerability enables L3 tool misuse; a L2 data poisoning attack
corrupts L5 observability because the monitoring system uses the same
poisoned RAG corpus. MAESTRO's layered model makes these propagation
paths explicit.

---

## How MAESTRO fits in the security programme

```
MAESTRO (threat enumeration by layer)
    ↓
Agentic_AITG.md (test cases per threat)
    ↓
Agentic_AIVSS.md (severity scoring per threat)
    ↓
ISO 27001 / CIS Controls / ASVS (control selection)
    ↓
Agentic_ISO42001.md (governance and impact assessment)
```

Use MAESTRO first. The threats it surfaces feed directly into the
test cases in `Agentic_AITG.md`, the scores in `Agentic_AIVSS.md`,
and the control selections in every other framework file in this folder.

---

## Layer-to-ASI entry mapping

Before the detailed entries, this matrix shows which ASI entries
originate at which MAESTRO layer — use this to scope threat modeling
sessions by architectural component:

| MAESTRO Layer | Primary ASI entries | Secondary ASI entries |
|---|---|---|
| L1 Foundation Models | ASI01 Goal Hijack, ASI09 Trust Exploitation | ASI10 Rogue Agents |
| L2 Data Operations | ASI06 Memory & Context Poisoning | ASI01, ASI04 |
| L3 Agent Frameworks | ASI02 Tool Misuse, ASI04 Supply Chain | ASI05, ASI07 |
| L4 Deployment & Infrastructure | ASI05 Unexpected Code Execution | ASI04, ASI08 |
| L5 Evaluation & Observability | ASI10 Rogue Agents | ASI06, ASI08 |
| L6 Security & Compliance | ASI03 Identity & Privilege Abuse | ASI02, ASI07 |
| L7 Agent Ecosystem | ASI07 Insecure Inter-Agent Comms, ASI08 Cascading Failures | ASI09, ASI10 |

---

## Quick-reference summary

| ID | Name | Severity | Primary MAESTRO Layers | Originating Layer | Tier |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Critical | L1, L2, L3 | L1 | Foundational–Advanced |
| ASI02 | Tool Misuse & Exploitation | Critical | L3, L6, L4 | L3 | Foundational–Advanced |
| ASI03 | Identity & Privilege Abuse | Critical | L6, L7, L4 | L6 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain | High | L3, L4, L2 | L3/L4 | Foundational–Hardening |
| ASI05 | Unexpected Code Execution | Critical | L4, L3, L5 | L4 | Hardening–Advanced |
| ASI06 | Memory & Context Poisoning | High | L2, L1, L5 | L2 | Hardening–Advanced |
| ASI07 | Insecure Inter-Agent Comms | High | L7, L6, L5 | L7 | Hardening–Advanced |
| ASI08 | Cascading Agent Failures | High | L7, L4, L5 | L7 | Foundational–Advanced |
| ASI09 | Human-Agent Trust Exploitation | Medium | L1, L7, L6 | L1 | Foundational–Hardening |
| ASI10 | Rogue Agents | Critical | L5, L1, L6 | L5/L1 | Hardening–Advanced |

---

## Audience tags

- **Security architect** — layer-to-ASI mapping for agentic system design threat modeling
- **Red team / threat modeler** — layer-by-layer threat enumeration before control selection
- **DevSecOps engineer** — L4/L5 entries for CI/CD and observability integration
- **AppSec engineer** — L3 agent framework and L6 identity entries
- **CISO** — layer propagation analysis for agentic risk programme scoping
- **OT security engineer** — ASI01, ASI02, ASI08 OT amplifier notes

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical
**Originating layer:** L1 — Foundation Models
**Propagation path:** L1 (injection interpreted) → L2 (injected via RAG/data) → L3 (executed through framework)

Goal hijack begins at L1 because the foundation model is the component
that interprets instructions — it is where the attacker's injected
directive is accepted as legitimate. The attacker's goal is to exploit
the model's instruction-following capability, which is an L1 property.
The injection vector may arrive through L2 (a poisoned RAG document)
or L3 (a crafted tool return value), but the acceptance happens at L1.

#### MAESTRO layer analysis

**L1 — Foundation Models (primary)**

The core vulnerability is the model's inability to structurally
distinguish instructions from data. The model processes a crafted
input — whether direct in the user prompt or indirect in retrieved
content — and generates a response that deviates from the authorised
goal. This is an inherent property of current transformer architectures:
the instruction and the data share the same token space with no
cryptographic or structural separator.

Threat actors: Nation-state adversaries with indirect injection
capability, insiders with RAG corpus write access, supply chain
attackers who control tool return values.

Mitigations at L1:
- Goal-state verification at the model orchestration layer —
  the agent's stated goal at session start is compared against
  its inferred goal at each action step
- Structural prompt architecture separating trusted instructions
  from untrusted content through context window organisation
- Constitutional AI constraints as L1 guardrails — hard limits
  on goal-changing instructions regardless of source

**L2 — Data Operations (indirect injection vector)**

RAG-retrieved documents, processed email content, and uploaded files
are the most prevalent indirect injection channels because they enter
the context window through the data pipeline before the model processes
them. An adversary who can influence the content indexed in the RAG
corpus can inject instructions that the model receives as retrieved
knowledge rather than user input.

Mitigations at L2:
- Source provenance tracking — each retrieved passage carries
  its trust level into the context window, preventing
  adversary-controlled content from being treated as trusted
- Content integrity verification on RAG ingestion — injection
  patterns detected before content enters the index
- Read-only data flow from corpus to context — no tool can
  modify the RAG corpus through the same pathway that reads it

**L3 — Agent Frameworks (execution channel)**

The framework orchestrates the sequence of tool calls and model
invocations. If the model's goal has been redirected, the framework
executes the hijacked goal through its tool dispatch mechanism.
A framework without goal-state verification cannot detect that the
actions it is executing diverge from the session's authorised scope.

Mitigations at L3:
- Framework-level goal-state verification as a middleware layer
  between model output and tool dispatch
- Action scope allowlisting at the framework level — the
  framework enforces what actions are permissible regardless
  of model instruction
- Kill switch accessible from the framework control plane —
  operator can halt all tool dispatch without model involvement

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| Direct prompt injection via user input | L1 | High | Critical | P1 |
| Indirect injection via RAG document | L2 → L1 | High | Critical | P1 |
| Indirect injection via tool return value | L3 → L1 | Medium | Critical | P1 |
| Multi-turn cumulative injection | L1 | Medium | High | P2 |
| Goal-verification bypass via injection | L1 → L3 | Low | Critical | P2 |

#### Cross-references
- LLM Top 10: LLM01 Prompt Injection, LLM06 Excessive Agency
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways, DSGAI15 Over-Broad Context Windows
- Other frameworks: MITRE ATLAS AML.T0051 · ISO 27001 A.8.28 · AIUC-1 B001/B005

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical
**Originating layer:** L3 — Agent Frameworks
**Propagation path:** L3 (tool dispatch) → L6 (credential used) → L4 (action executes in infrastructure)

Tool misuse originates at L3 because tool access, permission manifests,
and dispatch logic live in the agent framework layer. The agent
framework is the component that decides which tools are available,
what parameters are acceptable, and whether a requested tool invocation
is within authorised scope.

#### MAESTRO layer analysis

**L3 — Agent Frameworks (primary)**

The framework's tool registry is the permission boundary for tool
access. If this boundary is misconfigured — overly broad permissions,
no parameter validation, no irreversibility classification — any
injection reaching the model can be converted into harmful tool
invocations through the framework's own dispatch mechanism.

MCP (Model Context Protocol) introduces a specific L3 vulnerability:
tool descriptors loaded from external sources may contain hidden
instructions that redirect framework behaviour. The descriptor is
processed at L3 before the model evaluates the tool.

Mitigations at L3:
- Per-tool permission manifests enforced at the framework dispatch
  layer — each tool's permitted operations enumerated, all
  others rejected at dispatch regardless of model instruction
- MCP descriptor integrity verification — cryptographic hash of
  each descriptor checked against approved baseline before loading
- Irreversibility classification at L3 — framework marks each
  tool as reversible or irreversible, routes irreversible calls
  to a human confirmation gate before dispatch

**L6 — Security & Compliance (credential scope)**

Tool invocations execute under agent credentials. If those credentials
are over-privileged, a tool misuse attack that bypasses L3 controls
can access systems beyond the tool's intended scope. L6 controls
limit the blast radius of L3 failures.

Mitigations at L6:
- Least-privilege credentials per tool — each tool integration
  uses a scoped credential granting only the minimum required
  access, not a shared high-privilege service account
- Tool-scoped OAuth tokens — each tool receives a token with
  the minimum permission set for its defined function

**L4 — Deployment & Infrastructure (execution environment)**

Tool invocations that execute code, modify files, or call external
APIs cross into L4. Infrastructure-level controls at L4 provide a
final containment layer if L3 tool dispatch controls are bypassed.

Mitigations at L4:
- Network egress filtering — tools that should not make external
  calls are blocked at the network layer
- Execution environment isolation — tools run in sandboxed
  contexts with limited host access

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| Out-of-scope tool invocation via injection | L3 | High | Critical | P1 |
| Destructive parameter injection | L3 → L4 | Medium | Critical | P1 |
| MCP descriptor poisoning | L3 | Medium | High | P1 |
| Irreversible action without confirmation | L3 | High | High | P1 |
| Tool chain exploitation (combined harm) | L3 → L6 → L4 | Low | Critical | P2 |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling, LLM06 Excessive Agency
- DSGAI 2026: DSGAI06 Tool, Plugin & Agent Data Exchange
- Other frameworks: ISO 27001 A.8.2 · CIS Controls CIS 5 · AIUC-1 B006/B007

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical
**Originating layer:** L6 — Security & Compliance
**Propagation path:** L6 (credential exposed) → L7 (lateral movement across agents) → L4 (access to infrastructure)

Identity and privilege abuse is fundamentally an L6 failure — the
credential lifecycle management, scope controls, and audit logging
that govern non-human identities (NHIs) all live in the Security &
Compliance layer. When these controls fail, stolen agent credentials
provide authenticated access that bypasses every other layer's controls.

#### MAESTRO layer analysis

**L6 — Security & Compliance (primary)**

Agent credentials — API keys, OAuth tokens, service account secrets,
JWT tokens — are L6 assets. Their issuance, scope, rotation, storage,
and revocation are all L6 responsibilities. The most common failure
mode is not theft of credentials but over-privilege: credentials are
issued with broader scope than the agent requires, meaning any
compromise yields disproportionate access.

MAESTRO identifies three specific L6 failure patterns for agentic
NHIs: long-lived credentials that persist beyond session scope,
cleartext credential storage in agent memory or observability logs,
and shared credentials across multiple agent instances that make
attribution impossible.

Mitigations at L6:
- Short-lived JIT credentials scoped to session duration —
  credential expires at session end, no standing access
- Unique NHI per agent deployment — shared credentials
  eliminated, all agent actions attributable to a specific
  identity in audit log
- Credential scanning on all L6 output paths — credentials
  never appear in model outputs, observability traces, or
  tool call payloads

**L7 — Agent Ecosystem (lateral movement)**

Once a credential is compromised at L6, the attacker's next step
is lateral movement through the agent ecosystem at L7. In multi-agent
deployments, a compromised orchestrator credential can be used to
direct sub-agents, access shared memory stores, or invoke tools
across the entire cluster's scope.

Mitigations at L7:
- Inter-agent trust boundaries — even authenticated agents
  cannot invoke actions outside their defined role in the
  multi-agent hierarchy
- Credential scope bounded to specific agent cluster — a
  compromised credential in one cluster cannot traverse
  to another cluster's resources

**L4 — Deployment & Infrastructure (infrastructure access)**

Stolen agent credentials may grant access to L4 infrastructure —
database connections, container registries, CI/CD pipelines, or
cloud provider APIs. L4 controls provide a final access boundary
after L6 credential controls have failed.

Mitigations at L4:
- Network-level enforcement of credential scope —
  infrastructure access controlled at network layer
  independent of credential validity

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| Credential leakage via model output | L6 → L1 | High | Critical | P1 |
| Credential leakage via observability logs | L6 → L5 | High | Critical | P1 |
| Long-lived credential enabling lateral movement | L6 → L7 | Medium | Critical | P1 |
| Shared credential making attribution impossible | L6 | High | High | P2 |
| Cross-cluster lateral movement via stolen credential | L7 → L6 | Low | Critical | P2 |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 · ISO 27001 A.8.2/A.5.16 · NIST CSF 2.0 PR.AA-01

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High
**Originating layer:** L3 and L4 (dual origin)
**Propagation path:** L3/L4 (compromise) → L1 (behaviour alteration) → L5 (evasion of detection)

Agentic supply chain compromises originate at L3 (agent frameworks,
tool registries, MCP servers) and L4 (deployment infrastructure,
model weight delivery, container images). The defining characteristic
of supply chain attacks is that the compromise happens before the
system is running — the adversary modifies what gets deployed, not
what is running.

#### MAESTRO layer analysis

**L3 — Agent Frameworks (tool and framework supply chain)**

The agent framework layer includes all external dependencies that
the orchestration system loads at runtime: tool libraries, MCP server
packages, plugin registries, and the framework itself. MAESTRO
specifically highlights the MCP ecosystem as a high-risk L3 supply
chain surface because MCP servers are loaded dynamically at runtime
from registries that may not have adequate integrity controls.

The first documented malicious MCP package (npm, 2025) demonstrated
that tool descriptor poisoning at L3 is an active, not theoretical,
attack class.

Mitigations at L3:
- Cryptographic signature verification for all L3 components —
  tool packages, MCP servers, framework dependencies verified
  before loading
- Approved component list enforced at L3 — only components from
  the approved list may be loaded, unapproved packages rejected
  regardless of availability
- Descriptor integrity verification — each MCP tool descriptor
  hash-checked against approved baseline before the framework
  registers the tool

**L4 — Deployment & Infrastructure (model and image supply chain)**

Model weights, container images, and CI/CD pipeline components
are L4 supply chain assets. A compromised model weight file carries
embedded backdoor functionality into every deployment that uses it.
A poisoned container image provides an attacker foothold at the
infrastructure layer from the first deployment.

CVE-2024-34359 (llama_cpp_python) — RCE via malicious model file —
is a documented L4 supply chain attack against agentic AI infrastructure.

Mitigations at L4:
- ML SBOM as L4 asset inventory — every model weight, adapter,
  and library inventoried with source, version, and hash
- Build pipeline integrity — CI/CD pipeline itself subject to
  supply chain integrity controls, not just what it builds
- Isolated evaluation environment — each new component evaluated
  in an isolated L4 environment before production promotion

**L1 — Foundation Models (backdoor manifestation)**

A successfully delivered supply chain backdoor manifests at L1 —
the compromised model weights alter foundation model behaviour in
response to specific trigger inputs. This is an L1 symptom of an
L3/L4 origin attack.

Mitigations at L1:
- Post-training backdoor detection as mandatory deployment gate —
  testing for trigger-activated behaviour before any L1 model
  enters production

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| Malicious MCP server package | L3 | Medium | High | P1 |
| Backdoored model weights | L4 → L1 | Low | Critical | P1 |
| Compromised container image | L4 | Low | Critical | P1 |
| Hidden instructions in tool descriptor | L3 | Medium | High | P1 |
| CI/CD pipeline compromise | L4 | Low | Critical | P2 |

#### Cross-references
- LLM Top 10: LLM03 Supply Chain Vulnerabilities
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning
- Other frameworks: NIST CSF 2.0 GV.SC-01 · ISO 27001 A.5.19/A.5.21 · CWE-494

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical
**Originating layer:** L4 — Deployment & Infrastructure
**Propagation path:** L1 (code generation) → L3 (dispatch) → L4 (execution in infrastructure)

Code execution risks originate at L4 because the infrastructure layer
is where generated code actually runs. The generation happens at L1
and the dispatch at L3, but the blast radius of a successful attack
is determined entirely by what the L4 execution environment permits.

#### MAESTRO layer analysis

**L4 — Deployment & Infrastructure (primary)**

The execution environment — sandbox, container, virtual machine, or
bare metal — determines what a successfully injected piece of code
can do. An inadequately isolated L4 execution environment converts
any code generation capability into a potential RCE vulnerability.

MAESTRO's L4 threat model for code execution specifically addresses:
the sandbox escape path (attacker achieves host access from within
the execution environment), the network access path (generated code
makes external connections from inside the sandbox), and the
filesystem path (generated code reads or writes outside the scratch
directory).

Mitigations at L4:
- Hardware-level sandboxing — kernel-level isolation (gVisor,
  Firecracker) prevents sandbox escape regardless of what code
  the L1 model generates
- Network isolation of execution environment — no outbound
  connections from code execution sandbox to production networks
- Filesystem confinement — scratch directory only, all other
  paths blocked at L4

**L3 — Agent Frameworks (dispatch control)**

Before code reaches L4 for execution, the L3 framework dispatches
the execution request. L3 can apply static analysis and allowlist
enforcement before any code leaves the orchestration layer.

Mitigations at L3:
- Static analysis at L3 dispatch — generated code scanned for
  dangerous operations before dispatch to L4 execution
- Operation allowlist at L3 — only operations in the approved
  list may be dispatched for execution
- No-code-execution policy as default L3 configuration —
  code execution capability not included in framework
  unless explicitly required and approved

**L1 — Foundation Models (generation)**

The model generates the code that eventually reaches L4. L1 controls
cannot reliably prevent the generation of dangerous code — a
sufficiently motivated adversary can craft prompts that produce
obfuscated dangerous code that passes model-level safety filters.
L1 is the weakest layer for this risk; L3 and L4 controls are primary.

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| RCE via crafted prompt → code generation | L1 → L4 | Medium | Critical | P1 |
| Network exfiltration from sandbox | L4 | Medium | Critical | P1 |
| Filesystem traversal from sandbox | L4 | Medium | High | P1 |
| Static analysis bypass via obfuscation | L3 | Low | Critical | P2 |
| Sandbox escape to host | L4 | Low | Critical | P1 |

#### Cross-references
- LLM Top 10: LLM05 Insecure Output Handling
- DSGAI 2026: DSGAI12 Unsafe NL Data Gateways
- Other frameworks: AIUC-1 B005/B006 · CWE-94 · ISA/IEC 62443 SR 3.3 (OT)

---

### ASI06 — Memory & Context Poisoning

**Severity:** High
**Originating layer:** L2 — Data Operations
**Propagation path:** L2 (memory poisoned) → L1 (model uses poisoned context) → L5 (monitoring misses it)

Memory poisoning originates at L2 because agent memory — vector
stores, long-term memory databases, session context stores — is a
data operations asset. The memory store is where the attack is
staged; the model at L1 is where its effect is realised.

#### MAESTRO layer analysis

**L2 — Data Operations (primary)**

MAESTRO designates data operations as the layer responsible for all
data that shapes agent behaviour — not just training data, but
operational memory that the agent reads at inference time. Agent
memory stores are high-value L2 targets because poisoning them
produces systematic, persistent incorrect behaviour across all
future interactions, without requiring repeated injection.

MAESTRO specifically highlights three L2 memory attack paths: direct
write to the memory store (requires credential compromise at L6),
indirect write through conversation (attacker crafts conversational
content that the agent's memory system records as a factual entry),
and indirect write through tool return values (tool responses
containing crafted content are stored as memory entries).

Mitigations at L2:
- Access controls on all memory write paths — only the agent
  and designated administrators can write, no unauthenticated
  writes in any environment
- Memory TTL enforcement — entries expire and require
  re-validation, preventing indefinite persistence of
  poisoned content
- Content provenance tagging — each memory entry tagged with
  its source and trust level, preventing adversary-controlled
  content from being stored as authoritative memory

**L1 — Foundation Models (poisoned context consumption)**

When the model retrieves from a poisoned memory store, the poisoned
entry enters the context window as retrieved knowledge — indistinguishable
to the model from legitimate memory. The L1 model has no mechanism
to detect that retrieved content is adversarially crafted unless
source provenance information accompanies the retrieval.

Mitigations at L1:
- Source provenance carried through retrieval into context —
  model receives not just the memory content but its source
  trust level, allowing reasoning about reliability

**L5 — Evaluation & Observability (detection failure)**

The most dangerous aspect of memory poisoning is that it evades L5
monitoring — the agent's outputs remain superficially plausible,
making detection through output analysis alone difficult. L5 must
monitor not just outputs but the memory content that influences them.

Mitigations at L5:
- Memory integrity monitoring as L5 observability control —
  anomalous content changes in memory stores detected as
  security events, not just data quality events
- Systematic recommendation analysis — L5 monitoring tracks
  whether the agent's recommendations have shifted in ways
  consistent with poisoning

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| Indirect memory injection via conversation | L2 | High | High | P1 |
| Direct memory store write (credential compromise) | L2 ← L6 | Medium | Critical | P1 |
| Memory poisoning via tool return value | L2 ← L3 | Medium | High | P1 |
| Cross-session persistence of poisoned entries | L2 | Medium | High | P1 |
| Monitoring evasion through plausible-but-wrong output | L5 | High | High | P2 |

#### Cross-references
- LLM Top 10: LLM04 Data and Model Poisoning, LLM08 Vector and Embedding Weaknesses
- DSGAI 2026: DSGAI04 Data, Model & Artifact Poisoning, DSGAI13 Vector Store Platform Security
- Other frameworks: NIST AI RMF MS-2.5 · AIUC-1 A/B002 · ISA/IEC 62443 SR 3.7 (OT)

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High
**Originating layer:** L7 — Agent Ecosystem
**Propagation path:** L7 (A2A channel compromised) → L6 (authentication bypassed) → L3 (commands injected into target agent's framework)

Inter-agent communication risks originate at L7 because the
multi-agent communication topology, trust relationships, and
coordination protocols are properties of the agent ecosystem layer.
The A2A channel is a L7 construct; the authentication failure that
enables exploitation is an L6 failure; the commands that get injected
into the target agent reach it through its L3 framework.

#### MAESTRO layer analysis

**L7 — Agent Ecosystem (primary)**

MAESTRO's L7 threat model specifically addresses the security
properties that emerge only when multiple agents communicate. The
key insight is that the trust relationships between agents are often
implicit — agent A trusts messages from agent B because they share
the same orchestration context, not because B has cryptographically
authenticated itself to A. This implicit trust is the root cause of
agent-in-the-middle attacks.

MAESTRO also highlights the replay attack surface at L7: A2A messages
are often stateless, making it straightforward to capture and replay
a valid authenticated message to produce the same action without
the sending agent's knowledge.

Mitigations at L7:
- Explicit trust model for all A2A communication — no implicit
  trust based on shared infrastructure context, each message
  must carry verifiable sender identity
- Nonce-based replay protection — each A2A message includes a
  unique nonce, replays rejected at the receiving agent
- Schema validation at L7 — the ecosystem layer enforces
  message structure, rejecting malformed or unexpected payloads
  before they reach the receiving agent's framework

**L6 — Security & Compliance (authentication enforcement)**

The authentication of A2A messages is an L6 responsibility. Mutual
TLS with short-lived certificates, binding agent identity to
cryptographic proof, is the L6 control that makes L7 explicit trust
possible.

Mitigations at L6:
- Mutual TLS on all A2A channels — both sender and receiver
  authenticated, messages encrypted in transit
- Short-lived A2A certificates — bound to session, automatically
  revoked at session end

**L3 — Agent Frameworks (command injection point)**

A successfully injected A2A message reaches the receiving agent
through its L3 framework. If the framework does not validate that
the received message is within the authorised command scope for the
claimed sender, the injected message will be executed.

Mitigations at L3:
- Command scope validation at L3 — receiving framework checks
  that the message content is within the sending agent's
  authorised command scope for this interaction

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| Unauthenticated A2A message injection | L7 | Medium | High | P1 |
| Agent identity spoofing | L7 → L6 | Medium | Critical | P1 |
| Replay attack on A2A channel | L7 | Medium | High | P1 |
| Command injection via crafted A2A message | L7 → L3 | Low | Critical | P2 |
| A2A message in cleartext | L7 | High | High | P1 |

#### Cross-references
- DSGAI 2026: DSGAI02 Agent Identity & Credential Exposure
- Other frameworks: OWASP NHI Top 10 NHI-4/NHI-7 · ISO 27001 A.8.20/A.8.24 · AIUC-1 B007/B008

---

### ASI08 — Cascading Agent Failures

**Severity:** High
**Originating layer:** L7 — Agent Ecosystem
**Propagation path:** L7 (cascade propagates) → L4 (infrastructure overloaded) → L5 (monitoring overwhelmed before detection)

Cascading failures originate at L7 because cascade propagation is
an emergent property of multi-agent topology — it requires the agent
ecosystem to be present for the failure pattern to manifest. A single
agent failing is an L4 event; a cascade is an L7 event.

#### MAESTRO layer analysis

**L7 — Agent Ecosystem (primary)**

MAESTRO's L7 cascade model identifies two distinct propagation
mechanisms: **synchronous cascade**, where a failed agent's error
response is consumed by the next agent in the pipeline as valid
input, causing that agent to produce incorrect downstream actions;
and **resource cascade**, where a failed agent's retry behaviour
consumes resources that other agents in the same cluster depend on,
causing secondary failures through resource starvation.

In OT environments, L7 cascade propagation has a physical consequence
category that does not exist in IT deployments: a cascade reaching
the agent-process interface can produce incorrect process control
guidance before the cascade is detected. This elevates OT cascade
severity to Critical.

Mitigations at L7:
- Circuit breakers at every L7 agent-to-agent boundary —
  cascade propagation halted at the boundary, not allowed
  to reach the next agent in the topology
- Blast radius limits by design — agent cluster topology
  designed so that any single failure can affect at most
  a defined maximum number of downstream agents
- Operator kill switch accessible from outside the L7
  topology — operator can halt the entire cluster without
  needing to access individual agent instances

**L4 — Deployment & Infrastructure (resource exhaustion)**

Resource cascade at L7 manifests as resource exhaustion at L4 —
CPU, memory, API rate limits, or database connection pools consumed
by failing agents' retry behaviour. L4 controls limit how much
resource any agent instance can consume.

Mitigations at L4:
- Per-agent resource limits enforced at L4 — no agent instance
  can consume more than its allocated resource quota regardless
  of retry behaviour
- Rate limiting on all agent API calls — runaway retry behaviour
  bounded at the infrastructure layer

**L5 — Evaluation & Observability (detection)**

Cascade events produce large volumes of correlated anomalies across
multiple agents simultaneously — a pattern that overwhelms L5
monitoring systems that are designed for single-instance anomaly
detection. MAESTRO flags this as a specific L5 design requirement:
cascade monitoring must be correlation-based, not instance-based.

Mitigations at L5:
- Correlated anomaly detection — L5 monitoring designed to
  detect patterns across multiple agents simultaneously, not
  just individual agent anomalies
- Cascade-specific alert thresholds — alert when correlated
  failure rate across the cluster exceeds defined threshold,
  before blast radius reaches critical systems

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| Synchronous cascade via error propagation | L7 | Medium | High | P1 |
| Resource cascade via retry amplification | L7 → L4 | Medium | High | P1 |
| Cascade detection failure due to alert volume | L5 | High | High | P1 |
| Cross-cluster cascade propagation | L7 | Low | Critical | P1 |
| OT cascade reaching process control interface | L7 → L4 | Low | Critical | P1 |

#### Cross-references
- LLM Top 10: LLM10 Unbounded Consumption
- DSGAI 2026: DSGAI17 Data Availability & Resilience Failures
- Other frameworks: AIUC-1 D · ISA/IEC 62443 SR 7.6/7.7 (OT) · NIST SP 800-82 Rev 3

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium
**Originating layer:** L1 — Foundation Models
**Propagation path:** L1 (plausible output generation) → L7 (sustained interaction builds trust) → external (human makes harmful decision)

Trust exploitation originates at L1 because the plausibility of
agent outputs — the property that makes them convincing enough to
mislead human decision-makers — is a capability of the foundation
model. A model that produces outputs indistinguishable from
authoritative information is the prerequisite for this attack class.

#### MAESTRO layer analysis

**L1 — Foundation Models (primary)**

The foundation model's fluency, confidence calibration, and persuasive
writing capability are L1 properties that enable trust exploitation.
An adversary does not need to compromise any other layer to exploit
this risk — they can craft inputs that cause the model to produce
maximally convincing incorrect recommendations through the normal
inference API.

MAESTRO distinguishes between passive trust exploitation (the model
generates plausible misinformation in response to adversarial queries)
and active trust exploitation (a compromised or misaligned model
systematically builds trust with a specific operator over multiple
sessions before attempting to influence a high-stakes decision).

Mitigations at L1:
- AI disclosure enforcement — the model identifies itself as
  AI in all interface contexts, enforced at the rendering layer
  so that injected content cannot override the disclosure
- Advisory labelling as a rendering-layer control, not a
  model output control — the distinction between AI advisory
  and authoritative content is enforced outside L1

**L7 — Agent Ecosystem (sustained interaction)**

In multi-session deployments, trust accumulates at L7 through
repeated interactions. The agent ecosystem layer maintains session
history and interaction patterns — the substrate on which long-term
trust exploitation is built.

Mitigations at L7:
- Aggregate trust pattern monitoring at L7 — the ecosystem
  layer tracks whether operators are systematically accepting
  agent recommendations without independent verification,
  a pattern indicative of over-trust

**L6 — Security & Compliance (approval flow independence)**

High-stakes approvals must be routed through L6 identity and access
controls that are independent of the L1 model's output. An approval
that can be completed through the agent's conversational interface
is an approval that a compromised or exploited model can influence.

Mitigations at L6:
- Approval flows independent of agent interface — sensitive
  state changes require confirmation through an L6 access
  control system, not through the agent conversation

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| Plausible misinformation in high-stakes domain | L1 | High | Medium | P2 |
| Sustained multi-session trust building | L1 → L7 | Low | High | P2 |
| Approval manipulation via persuasive output | L1 → L6 | Medium | High | P1 |
| Safety alarm suppression via AI recommendation | L1 | Low | Critical | P1 (OT) |
| Identity concealment — AI claims to be human | L1 | Low | High | P2 |

#### Cross-references
- LLM Top 10: LLM09 Misinformation
- DSGAI 2026: DSGAI21 Disinformation via Data Poisoning
- Other frameworks: EU AI Act Art. 13/50 · ISO 27001 A.6.3 · AIUC-1 C/F

---

### ASI10 — Rogue Agents

**Severity:** Critical
**Originating layer:** L5 and L1 (dual origin)
**Propagation path:** L1 (hidden goal) + L5 (detection failure) → L6 (credential scope exploited) → L7 (systematic harm)

Rogue agents have a dual origin in MAESTRO's model. The hidden goal
— whether introduced through supply chain compromise, memory poisoning,
or adversarial fine-tuning — originates at L1. But a rogue agent
only succeeds because L5 Evaluation & Observability fails to detect
the deviation between the agent's stated and actual behaviour. Both
layers must fail for a rogue agent to operate at scale.

#### MAESTRO layer analysis

**L5 — Evaluation & Observability (detection failure)**

MAESTRO designates L5 as the primary defence against rogue agents
because the defining characteristic of a rogue agent is that it
pursues a hidden goal while appearing compliant — making L5
monitoring the only layer that can detect the discrepancy.

L5 must maintain a behavioural baseline established during
commissioning and detect deviation from that baseline across three
dimensions: action frequency (does the agent take more or fewer
actions than baseline?), action scope (does the agent access systems
or data outside its baseline scope?), and recommendation bias (do
the agent's recommendations systematically favour a particular
outcome across many interactions?).

The last dimension — recommendation bias — is the hardest to detect
because individual recommendations may be defensible; only the
aggregate pattern reveals the hidden goal.

Mitigations at L5:
- Behavioural baseline established at commissioning — expected
  action patterns documented before production deployment,
  baseline serves as the comparison point for all subsequent
  monitoring
- Tiered deviation response — minor deviations logged and
  flagged, major deviations trigger automatic suspension,
  the threshold documented before deployment
- Aggregate recommendation analysis — periodic review of
  recommendation patterns across many sessions detects
  systematic bias that individual-session monitoring cannot see
- Anomaly-to-suspension latency SLA — time from deviation
  detection to agent suspension defined and measured, ensures
  monitoring system performance meets risk requirements

**L1 — Foundation Models (hidden goal)**

The rogue behaviour — whether a persistent hidden goal, a triggered
backdoor, or a systematic bias — is an L1 property. The model's
weights encode the behaviour that L5 must detect. This means rogue
agent defences at L1 focus on provenance and integrity, not runtime
behaviour detection.

Mitigations at L1:
- Model provenance documentation — the training data, fine-tuning
  pipeline, and weight provenance chain documented before
  deployment, enabling investigation if rogue behaviour is detected
- Post-training behaviour audits — periodic audits of model
  recommendation patterns across production sessions to detect
  emerging systematic biases

**L6 — Security & Compliance (scope constraints)**

Even if L5 detection fails and L1 provenance is compromised, L6
scope constraints limit what a rogue agent can do with the access
it has. A rogue agent operating at minimum privilege causes less
damage before detection than one operating at elevated privilege.

Mitigations at L6:
- Scope constraints enforced at L6 infrastructure layer —
  rogue agent cannot exceed its permission envelope regardless
  of internal goal state
- Regular privilege reviews — rogue agent cannot accumulate
  permissions over time if access rights are reviewed periodically

#### MAESTRO threat model output

| Threat | Originating layer | Likelihood | Impact | Priority |
|---|---|---|---|---|
| Supply-chain-introduced hidden goal | L1 ← L4 | Low | Critical | P1 |
| Memory-poisoning-induced goal drift | L1 ← L2 | Medium | Critical | P1 |
| Systematic recommendation bias detection failure | L5 | High | High | P1 |
| Rogue agent operating at elevated privilege | L6 | Medium | Critical | P1 |
| Rogue agent coordinating across agent ecosystem | L7 | Low | Critical | P2 |

#### Cross-references
- LLM Top 10: LLM06 Excessive Agency
- DSGAI 2026: DSGAI16 Endpoint & Browser Assistant Overreach
- Other frameworks: AIUC-1 B001/B002/C/E · EU AI Act Art. 14/15 · ISA/IEC 62443 SR 3.7 (OT)

---

## MAESTRO threat modeling session guide

Use this guide to run a MAESTRO-based threat modeling session for
a new agentic AI deployment before selecting controls.

### Step 1 — Map your system to the seven layers

For each MAESTRO layer, document:
- What components in your deployment live at this layer?
- What trust boundaries exist at this layer?
- What are the data flows in and out of this layer?

### Step 2 — Enumerate threats per layer

For each layer, work through the threat table in the relevant ASI
entry above. Ask: is this threat applicable to our specific deployment?
If yes, what is the likelihood given our architecture?

### Step 3 — Identify propagation paths

For each threat you have identified, trace the propagation path
upward through the layers. A threat at L2 that can reach L1 and evade
L5 detection is categorically more dangerous than a threat contained
to a single layer.

### Step 4 — Prioritise by layer + propagation

| Priority | Criteria |
|---|---|
| P1 Critical | Originates at L1 or L2 AND propagates to 2+ additional layers |
| P1 High | Single-layer containment with Critical impact |
| P2 High | Originates at L3–L4 with defined containment at L5/L6 |
| P3 Medium | Contained to single layer with defined mitigation |

### Step 5 — Select controls from companion files

Map each P1 threat to controls from:
- `Agentic_AITG.md` — test cases to verify the control works
- `Agentic_AIVSS.md` — severity score for the risk register
- `Agentic_ISO27001.md` / `Agentic_CISControls.md` — specific control selection
- `Agentic_ISO42001.md` — impact assessment for each P1 threat

### Step 6 — Iterate as scope expands

MAESTRO is explicitly designed for iteration. When a new tool, model,
or capability is added to the deployment, re-run Steps 1–4 for the
affected layers only. Do not re-run the full threat model — scope
the session to the layers touched by the change.

---

## MAESTRO × OWASP integration summary

MAESTRO is already referenced by the OWASP GenAI Security Project.
The integration across OWASP artefacts is:

| OWASP artefact | MAESTRO integration point |
|---|---|
| LLM Top 10 | L1 Foundation Model threats map to LLM01, LLM04, LLM09 |
| Agentic Top 10 | Full mapping — this file |
| DSGAI 2026 | L2 Data Operations threats map to DSGAI — see `DSGAI_MAESTRO.md` |
| AI Testing Guide | MAESTRO threat enumeration → AITG test case selection |
| AIVSS | MAESTRO layer + propagation depth informs AIVSS scoring dimensions |
| Multi-Agentic Threat Modeling Guide | MAESTRO is the referenced framework |

---

## References

- [MAESTRO Framework — CSA](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
- [MAESTRO GitHub Repository](https://github.com/CloudSecurityAlliance/MAESTRO)
- [MAESTRO for Real-World Agentic AI Threats](https://cloudsecurityalliance.org/blog/2026/02/11/applying-maestro-to-real-world-agentic-ai-threat-models-from-framework-to-ci-cd-pipeline)
- [MAESTRO Applied to OpenAI Responses API](https://cloudsecurityalliance.org/blog/2025/03/24/threat-modeling-openai-s-responses-api-with-the-maestro-framework)
- [MAESTRO Applied to Google A2A Protocol](https://cloudsecurityalliance.org/blog/2025/04/30/threat-modeling-google-s-a2a-protocol-with-the-maestro-framework)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [DSGAI 2026 × MAESTRO](../dsgai-2026/DSGAI_MAESTRO.md)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — ASI01–ASI10 full MAESTRO layer analysis with threat model outputs and session guide | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.  
Created by Emmanuel Guilherme Junior.  
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
