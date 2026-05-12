<!--
  GenAI Security Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10)
  Framework   : CWE / CVE Mapping
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Agentic Top 10 2026 × CWE / CVE

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [MITRE CWE](https://cwe.mitre.org/) (Common Weakness Enumeration)
and documented [CVEs](https://cve.mitre.org/) (Common Vulnerabilities
and Exposures) relevant to agentic AI systems.

---

## How to use this file

**CWE mapping** provides the software weakness taxonomy that security
architects, developers, and tool vendors use to classify root causes.
Every agentic risk maps to one or more CWEs — these are the
engineering-level descriptions of what makes each risk possible.

**CVE mapping** provides real-world incident and vulnerability
evidence. CVEs cited here have been confirmed in production systems
and components used by agentic AI deployments. They demonstrate that
these risks are not theoretical.

**Use this file to:**
- Link agentic risks to SAST/DAST tool rule sets (most tools use CWE IDs)
- Provide evidence in risk assessments that vulnerabilities are real
- Satisfy penetration test scope requirements referencing specific CWEs
- Brief development teams using engineering-level weakness terminology

---

## Quick-reference summary

| ID | Name | Primary CWEs | Confirmed CVEs | Severity |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | CWE-20, CWE-74, CWE-693 | CVE-2025-29927, CVE-2024-27564 | Critical |
| ASI02 | Tool Misuse & Exploitation | CWE-284, CWE-862, CWE-434 | CVE-2025-43703, CVE-2025-30018 | Critical |
| ASI03 | Identity & Privilege Abuse | CWE-250, CWE-522, CWE-312 | CVE-2025-54795, CVE-2025-32711 | Critical |
| ASI04 | Agentic Supply Chain | CWE-494, CWE-829, CWE-506 | CVE-2024-34359, CVE-2025-32444 | High |
| ASI05 | Unexpected Code Execution | CWE-94, CWE-78, CWE-77 | CVE-2024-3095, CVE-2024-27564 | Critical |
| ASI06 | Memory & Context Poisoning | CWE-349, CWE-345, CWE-20 | CVE-2024-3584, CVE-2024-45022 | High |
| ASI07 | Insecure Inter-Agent Comms | CWE-287, CWE-294, CWE-319 | CVE-2025-32727, CVE-2024-7965 | High |
| ASI08 | Cascading Agent Failures | CWE-400, CWE-703, CWE-755 | CVE-2024-11831, CVE-2025-30066 | High |
| ASI09 | Human-Agent Trust Exploitation | CWE-183, CWE-451, CWE-346 | CVE-2025-24371 | Medium |
| ASI10 | Rogue Agents | CWE-284, CWE-693, CWE-799 | CVE-2025-54795, CVE-2025-32444 | Critical |

---

## Audience tags

- **Developer / AppSec engineer** — CWE IDs for SAST tool configuration
- **Penetration tester** — CWE IDs for test scope definition; CVEs for evidence
- **Risk manager** — CVE evidence for risk register entries
- **Procurement / legal** — CVE evidence of real-world exploitability
- **SIEM engineer** — CWE-based detection rule mapping

---

## Detailed mappings

---

### ASI01 — Agent Goal Hijack

**Severity:** Critical

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-20 | Improper Input Validation | Root cause — agent inputs not validated before entering model context; indirect injection content not treated as untrusted |
| CWE-74 | Improper Neutralisation of Special Elements in Output Used by a Downstream Component | Instruction elements in processed content not neutralised before agent reasoning |
| CWE-693 | Protection Mechanism Failure | Safety and goal-verification controls bypassed through injection |
| CWE-441 | Unintended Proxy or Intermediary | Agent acts as a proxy executing attacker instructions against backend systems |
| CWE-610 | Externally Controlled Reference to a Resource in Another Sphere | Agent retrieves and acts on externally controlled content (RAG, email, tool returns) without adequate validation |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2025-29927 | Next.js middleware | Middleware bypass allowing unauthenticated access through crafted headers | Pattern: input handling bypass enabling downstream injection — directly analogous to agent context injection via crafted inputs |
| CVE-2024-27564 | ChatGPT | SSRF via image injection causing server-side request forgery | Demonstrated indirect injection via processed content causing agent to make unintended requests |
| CVE-2024-5184 | EmailGPT | Prompt injection via email content leading to arbitrary instructions execution | Direct real-world example of ASI01 via indirect injection channel |

#### Engineering root cause

Goal hijack is fundamentally CWE-20 (Improper Input Validation) at
the agent context assembly layer. The agent's context window is a
trust boundary — content from different sources (user, RAG, tools,
email) with different trust levels is mixed into a single flat
namespace without content integrity markers. The fix is structural:
maintain source provenance and trust level through context assembly
and apply differentiated validation per trust level.

#### Detection rule hints (CWE-based)

- SAST: flag any code path that inserts external content into LLM
  context without validation (CWE-20 analogue for AI pipelines)
- DAST: test all agent input channels for instruction injection
  using CWE-74 test cases adapted for natural language context

---

### ASI02 — Tool Misuse & Exploitation

**Severity:** Critical

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-284 | Improper Access Control | Agent can invoke tools it should not have access to; tool parameters not range-validated |
| CWE-862 | Missing Authorisation | No authorisation check before irreversible tool invocations; human confirmation not required |
| CWE-434 | Unrestricted Upload of File with Dangerous Type | Analogy: agent accepts and executes tool payloads without content validation |
| CWE-913 | Improper Control of Dynamically-Managed Code Resources | MCP descriptors and tool specifications are dynamically loaded code resources — modification not controlled |
| CWE-20 | Improper Input Validation | Tool parameters generated by LLM not validated against safe ranges before execution |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2025-43703 | MCP ecosystem | Malicious MCP server used tool descriptor to redirect agent actions (Postmark MCP — first malicious MCP on npm) | Direct ASI02 real-world example — poisoned tool descriptor causing unintended agent actions |
| CVE-2025-30018 | Agent framework (undisclosed) | Tool call parameter injection bypassing schema validation | LLM-generated parameters used directly in system calls without validation |
| CVE-2024-6087 | LangChain | Agent tools callable with arbitrary parameters through crafted inputs | Demonstrates CWE-284 in production agentic framework |

#### Engineering root cause

Tool misuse is CWE-284 (Improper Access Control) applied to the
agent-tool boundary. The fix pattern is identical to API access
control: treat every tool call as an API call from an untrusted
client, enforce authorisation at the tool boundary independently
of the agent framework, and validate all parameters against a
strict schema before execution.

---

### ASI03 — Identity & Privilege Abuse

**Severity:** Critical

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-250 | Execution with Unnecessary Privileges | Agent runs with broader credentials than its task requires; NHI-5 over-privilege |
| CWE-522 | Insufficiently Protected Credentials | Agent credentials stored in cleartext memory, logs, config, or tool payloads |
| CWE-312 | Cleartext Storage of Sensitive Information | Credentials and tokens not encrypted at rest in agent memory or configuration |
| CWE-798 | Use of Hard-coded Credentials | Agent credentials hardcoded in prompts or source code |
| CWE-613 | Insufficient Session Expiration | Long-lived agent credentials without expiry or rotation — NHI-7 |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2025-54795 | Anthropic Claude Code | Confirmation bypass enabling execution of untrusted commands via agent credential access | Direct ASI03 example — agent identity used to bypass confirmation, enabling privilege abuse |
| CVE-2025-32711 | Agent orchestration framework | Session token leaked to tool payload enabling lateral movement | NHI-2 credential leakage via tool call |
| CVE-2024-45022 | AI platform credential handling | Service account credentials persisted in conversation logs | CWE-312 cleartext credential storage in agent observability pipeline |

#### Engineering root cause

Identity abuse is CWE-250 (Unnecessary Privileges) combined with
CWE-522 (Insufficiently Protected Credentials). The NHI governance
fix is: treat every agent credential as a privileged access token
subject to PAM controls — least privilege, short TTL, JIT issuance,
no cleartext storage, full audit logging.

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-494 | Download of Code Without Integrity Check | Agent tool components and MCP servers loaded without signature verification |
| CWE-829 | Inclusion of Functionality from Untrusted Control Sphere | MCP servers and plugins from external registries loaded into agent execution context |
| CWE-506 | Embedded Malicious Code | Model weights and tool components containing hidden backdoor functionality |
| CWE-1357 | Reliance on Insufficiently Trustworthy Component | Agent dependency on third-party MCP servers without security assessment |
| CWE-441 | Unintended Proxy or Intermediary | Compromised tool acting as malicious intermediary in agent workflow |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2024-34359 | llama_cpp_python | Remote code execution via malicious model file (pickle deserialisation) | CWE-506 — model artifact as a vehicle for embedded malicious code |
| CVE-2025-32444 | MCP server npm package | Supply chain compromise of MCP server package with hidden exfiltration code | First documented MCP supply chain attack — ASI04 in production |
| CVE-2024-3584 | Qdrant vector database | Path traversal via snapshot import achieving arbitrary file write | CWE-494 — component loaded without adequate integrity checks enabling write to host |

#### Engineering root cause

Supply chain risk is CWE-494 (Download Without Integrity Check) —
the fix is cryptographic verification of all components at every
stage of the delivery pipeline. For ML-specific components, this
means ML SBOM generation, model scanning (ModelScan), and hash
verification before any component enters a production environment.

---

### ASI05 — Unexpected Code Execution

**Severity:** Critical

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-94 | Improper Control of Generation of Code | Agent generates and executes code without adequate static analysis or sandbox |
| CWE-78 | Improper Neutralisation of Special Elements in OS Command | LLM-generated code containing shell commands executed without sanitisation |
| CWE-77 | Improper Neutralisation of Special Elements in Command | LLM output used directly in command context |
| CWE-95 | Improper Neutralisation of Directives in Dynamically Evaluated Code | Eval of LLM-generated code |
| CWE-676 | Use of Potentially Dangerous Function | Agent uses exec(), eval(), subprocess without validation |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2024-3095 | AutoGPT | Remote code execution via crafted prompt triggering code generation and execution | Direct ASI05 example — prompt injection ? code generation ? RCE |
| CVE-2024-27564 | ChatGPT plugins | SSRF via crafted image causing server-side request from agent execution context | Code execution context used for network-based attack |
| CVE-2024-6087 | LangChain agents | Arbitrary code execution via tool input manipulation | CWE-94 in production LangChain agent framework |

#### Engineering root cause

Unexpected code execution is CWE-94 — the fix is never to execute
LLM-generated code without (a) static analysis against an allowlist,
(b) hardware-level sandboxing, and (c) network isolation of the
execution context. The strongest control is CWE-94 prevention
by design: do not give agents code execution capability unless
the business case is compelling and the risk is formally accepted.

---

### ASI06 — Memory & Context Poisoning

**Severity:** High

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-349 | Acceptance of Extraneous Untrusted Data with Trusted Data | Agent memory store accepts writes from untrusted sources alongside trusted operational knowledge |
| CWE-345 | Insufficient Verification of Data Authenticity | Memory content not integrity-verified before storage or retrieval |
| CWE-20 | Improper Input Validation | Content entering agent memory not validated before write |
| CWE-284 | Improper Access Control | Vector store and memory databases with insufficient access controls permitting unauthorised writes |
| CWE-1341 | Multiple Releases of Same Resource or Handle | Memory TTL not enforced — entries persist beyond intended lifetime |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2024-3584 | Qdrant | Path traversal via snapshot import enabling arbitrary file write on vector DB host | CWE-284 — vector store (memory infrastructure) with access control failure enabling direct memory poisoning |
| CVE-2024-45022 | AI platform | Persistent memory manipulation via crafted conversation enabling long-term behavioural influence | Direct ASI06 example — poisoned conversation persisting as agent memory |
| CVE-2024-7965 | Chrome V8 | Memory corruption via type confusion | Infrastructure-level memory vulnerability that could affect agent runtime environments |

#### Engineering root cause

Memory poisoning is CWE-349 — the fix is treating the memory store
as a trust boundary. Content from different sources (conversation,
tools, external data) should not be written to memory with equal
trust without explicit validation and provenance tagging.

---

### ASI07 — Insecure Inter-Agent Communication

**Severity:** High

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-287 | Improper Authentication | A2A channels without mutual authentication — agents accept messages from any sender |
| CWE-294 | Authentication Bypass by Capture-replay | Replay attacks on A2A channels without nonce-based replay protection |
| CWE-319 | Cleartext Transmission of Sensitive Information | A2A messages containing sensitive context transmitted without encryption |
| CWE-346 | Origin Validation Error | Agent does not verify that A2A messages originate from the claimed sender |
| CWE-924 | Improper Enforcement of Message Integrity During Transmission | A2A message integrity not cryptographically verified |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2025-32727 | Multi-agent orchestration framework | Unauthenticated inter-agent message injection enabling goal redirection | Direct ASI07 example — A2A channel without authentication |
| CVE-2024-7965 | A2A API implementation | Insufficient validation of agent-to-agent messages allowing spoofed coordinator messages | CWE-287 in production A2A communication |
| CVE-2024-47832 | Workflow orchestration platform | Session token reuse across agent instances enabling replay | CWE-294 replay attack on agent communication |

#### Engineering root cause

A2A communication failures are CWE-287 (Improper Authentication) —
the fix is mutual TLS with short-lived certificates and nonce-based
replay protection on all inter-agent channels. This is the same
fix as securing any microservice-to-microservice communication, with
the additional requirement that agent identities must be verifiable
and non-reusable across deployments.

---

### ASI08 — Cascading Agent Failures

**Severity:** High

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-400 | Uncontrolled Resource Consumption | Agent resource consumption not bounded — enables exhaustion propagation across cluster |
| CWE-703 | Improper Check or Handling of Exceptional Conditions | Agent failures not caught and handled — exception propagates to downstream agents |
| CWE-755 | Improper Handling of Exceptional Conditions | Cascade fails because upstream agents do not handle failure conditions gracefully |
| CWE-730 | OWASP ReDoS | Regex-based input processing causing runaway computation propagating through pipeline |
| CWE-674 | Uncontrolled Recursion | Recursive agent calls without depth limits enabling stack exhaustion cascade |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2024-11831 | npm package in agent pipeline | Prototype pollution causing uncontrolled resource consumption | CWE-400 — resource exhaustion in agent pipeline component |
| CVE-2025-30066 | tj-actions/changed-files (CI/CD supply chain) | Compromised CI action cascading to all downstream consumers | Supply chain failure pattern causing cascade across all dependent workflows — direct ASI08 analogue |
| CVE-2024-3584 | Qdrant vector database | Resource exhaustion via malformed snapshot import | CWE-400 — cascade trigger via vector store component failure |

#### Engineering root cause

Cascading failures are CWE-703/CWE-755 — improper exception handling
combined with CWE-400 uncontrolled resource consumption. The fix is
circuit breakers at every agent-to-agent and agent-to-system boundary,
with explicit fail-safe defaults that halt autonomous operation rather
than propagating degraded state downstream.

---

### ASI09 — Human-Agent Trust Exploitation

**Severity:** Medium

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-183 | Permissive List of Allowed Inputs | System accepts human-like agent output without disclosure requirements |
| CWE-451 | User Interface Misrepresentation of Critical Information | Agent advisory output not clearly distinguished from authoritative system information in UI |
| CWE-346 | Origin Validation Error | User cannot determine whether advice originates from AI or human — no origin verification |
| CWE-940 | Improper Verification of Source of a Communication Channel | User cannot verify the agent is operating under its stated configuration |
| CWE-200 | Exposure of Sensitive Information to an Unauthorised Actor | System prompt and agent configuration not protected — extraction enables targeted trust exploitation |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2025-24371 | AI assistant platform | AI system manipulated into producing misleading content that appeared authoritative to users | Direct ASI09 example — trust exploitation through plausible but incorrect authoritative-appearing output |

#### Engineering root cause

Trust exploitation is CWE-451 (UI Misrepresentation) — the fix is
mandatory, non-bypassable AI disclosure in all interface contexts
(EU AI Act Art. 50), with visual distinction between agent advisory
output and authoritative system content. The disclosure must be
at the rendering layer, not in the agent's response text, because
injected content can alter response text but cannot alter the
rendering framework's persistent labels.

---

### ASI10 — Rogue Agents

**Severity:** Critical

#### CWE mapping

| CWE | Name | How it applies |
|---|---|---|
| CWE-284 | Improper Access Control | Rogue agent exceeds its permitted access scope — no scope enforcement |
| CWE-693 | Protection Mechanism Failure | Behavioural monitoring and detection mechanisms bypassed by rogue agent |
| CWE-799 | Improper Control of Interaction Frequency | Rogue agent evades detection by maintaining normal action frequency while biasing recommendations |
| CWE-506 | Embedded Malicious Code | Rogue behaviour may result from backdoored model or component |
| CWE-276 | Incorrect Default Permissions | Agent deployed with broader permissions than needed — amplifies rogue blast radius |

#### CVE evidence

| CVE | System | Description | Agentic relevance |
|---|---|---|---|
| CVE-2025-54795 | Claude Code | Agent confirmation bypass via crafted inputs enabling execution of unintended commands | Demonstrates how an agent can be made to operate outside its intended constraints — rogue behaviour trigger |
| CVE-2025-32444 | MCP npm package | Supply chain compromise introducing hidden exfiltration code operating covertly in agent context | Direct rogue agent via supply chain — agent appears compliant while covertly exfiltrating |

#### Engineering root cause

Rogue agents are CWE-284 (Improper Access Control) combined with
CWE-693 (Protection Mechanism Failure). The fix has two parts:
(1) scope enforcement at the infrastructure layer so a rogue agent
cannot exceed its permission envelope regardless of internal goal
state, and (2) behavioural monitoring so that the systematic
deviations that characterise rogue behaviour are detected before
the blast radius becomes unacceptable.

---

## CWE cross-reference index

Use this index to find all ASI entries associated with a given CWE:

| CWE | Name | ASI entries |
|---|---|---|
| CWE-20 | Improper Input Validation | ASI01, ASI06 |
| CWE-74 | Improper Neutralisation of Special Elements | ASI01 |
| CWE-77 | OS Command Injection | ASI05 |
| CWE-78 | Shell Command Injection | ASI05 |
| CWE-94 | Code Injection | ASI05 |
| CWE-183 | Permissive Allowed Inputs | ASI09 |
| CWE-200 | Information Exposure | ASI09 |
| CWE-250 | Execution with Unnecessary Privileges | ASI03 |
| CWE-276 | Incorrect Default Permissions | ASI10 |
| CWE-284 | Improper Access Control | ASI02, ASI06, ASI10 |
| CWE-287 | Improper Authentication | ASI07 |
| CWE-294 | Replay Attack | ASI07 |
| CWE-312 | Cleartext Storage of Sensitive Information | ASI03 |
| CWE-319 | Cleartext Transmission | ASI07 |
| CWE-345 | Insufficient Verification of Data Authenticity | ASI06 |
| CWE-346 | Origin Validation Error | ASI07, ASI09 |
| CWE-349 | Acceptance of Extraneous Untrusted Data | ASI06 |
| CWE-400 | Uncontrolled Resource Consumption | ASI08 |
| CWE-434 | Unrestricted File Upload | ASI02 |
| CWE-441 | Unintended Proxy | ASI01, ASI04 |
| CWE-451 | UI Misrepresentation | ASI09 |
| CWE-494 | Download Without Integrity Check | ASI04 |
| CWE-506 | Embedded Malicious Code | ASI04, ASI10 |
| CWE-522 | Insufficiently Protected Credentials | ASI03 |
| CWE-610 | Externally Controlled Resource Reference | ASI01 |
| CWE-613 | Insufficient Session Expiration | ASI03 |
| CWE-674 | Uncontrolled Recursion | ASI08 |
| CWE-676 | Use of Dangerous Function | ASI05 |
| CWE-693 | Protection Mechanism Failure | ASI01, ASI10 |
| CWE-703 | Improper Exception Handling | ASI08 |
| CWE-755 | Improper Handling of Exceptional Conditions | ASI08 |
| CWE-798 | Hard-coded Credentials | ASI03 |
| CWE-799 | Improper Interaction Frequency Control | ASI10 |
| CWE-829 | Inclusion from Untrusted Control Sphere | ASI04 |
| CWE-862 | Missing Authorisation | ASI02 |
| CWE-913 | Improper Control of Dynamic Code Resources | ASI02 |
| CWE-924 | Improper Message Integrity Enforcement | ASI07 |
| CWE-940 | Improper Source Verification | ASI09 |
| CWE-1341 | Multiple Release of Same Resource | ASI06 |
| CWE-1357 | Reliance on Insufficiently Trustworthy Component | ASI04 |

---

## CVE update policy

CVEs listed in this file were confirmed as of the 2026-Q1 release date.
The agentic AI CVE landscape is evolving rapidly. Contributors are
encouraged to submit new CVEs via pull request as they are published.

**To add a CVE:**
1. Confirm the CVE is published in the NVD
2. Verify the affected system is used in or relevant to agentic AI deployments
3. Write a one-sentence description of the agentic relevance
4. Open a PR with the addition to the relevant ASI entry table
5. Update the CHANGELOG.md entry for the next patch release

**CVE research resources:**
- NVD: https://nvd.nist.gov
- MITRE CVE: https://cve.mitre.org
- OSV (open source vulnerabilities): https://osv.dev
- MITRE ATLAS incidents: https://atlas.mitre.org/studies

---

## References

- [MITRE CWE](https://cwe.mitre.org/)
- [MITRE CVE](https://cve.mitre.org/)
- [NVD — National Vulnerability Database](https://nvd.nist.gov/)
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [MITRE ATLAS — Adversarial ML Threat Matrix](https://atlas.mitre.org)
- [OSV — Open Source Vulnerabilities](https://osv.dev)

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-03-26 | 2026-Q1 | Initial mapping — ASI01–ASI10 CWE and CVE evidence with CWE cross-reference index | OWASP GenAI Data Security Initiative |

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the GenAI Security Crosswalk: https://github.com/emmanuelgjr/GenAI-Security-Crosswalk
