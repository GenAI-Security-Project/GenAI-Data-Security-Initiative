<!--
  OWASP GenAI Crosswalk
  Source list : OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10)
  Framework   : AVE — Agentic Vulnerability Enumeration
  Version     : 2026-Q1 (pilot — 4 of 80 AVE records, covering 3 of 10 ASI entries)
  Maintained by: aveproject/ave — https://aveproject.org
  License     : This file, CC BY-SA 4.0. Quoted AVE record text is
                Apache-2.0-licensed by aveproject/ave; reproduced here
                with attribution as permitted by that license.
-->

# Agentic Top 10 2026 × AVE

Mapping the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
to [AVE](https://aveproject.org) — the behavioral classification standard
for agentic AI components ([github.com/aveproject/ave](https://github.com/aveproject/ave)).

**What AVE is.** A standard, not a product: 80 published records, each a
stable, immutable ID describing one distinct behavioral class a skill
file, MCP server manifest, system prompt, or agent plugin can exhibit —
scored with OWASP AIVSS v0.8 and mapped to OWASP MCP Top 10, with
`owasp_asi`, `mitre_atlas`, and `nist_ai_rmf` as optional fields added
per-record when a genuinely distinct correspondence is verified. AVE is
implemented by more than one tool; no implementer owns the standard.

**What AVE is not.** Not a controls catalog — a record describes what an
attacker's component *does* (a `behavioral_fingerprint`), not a
defensive requirement to implement or certify against. Not a scoring
framework in its own right — AVE records carry an OWASP AIVSS v0.8 score
each, they don't define a competing scoring methodology.

## Why a manual PR, not the JSON classifier submission

The submission schema's `data/framework-schema.json` shape and its
category enum are built for a controls catalog — a framework with named
controls that get mapped to. AVE's records aren't controls, they're
behavioral definitions. That's the same structural reason MITRE ATLAS —
also a technique taxonomy, not a controls catalog — entered this
crosswalk via a hand-authored file (`Agentic_MITREATLAS.md`) rather than
the automated intake.

**Deliberate scope: 4 of 80.** This pilot maps the four AVE records
whose `owasp_asi` correspondence is the clearest and most unambiguous,
following the same pilot-first approach already used for AVE's OpenCRE
submission. It covers 3 of the 10 ASI entries (ASI02, ASI04, ASI05);
the other 76 records and 7 entries are not represented here and no
claim is made about them. More can follow once this format is
confirmed correct.

---

## Quick-reference summary

| ID | Name | Severity | AVE records | Tier |
|---|---|---|---|---|
| ASI02 | Tool Misuse and Exploitation | Critical | AVE-2026-00068 | Foundational–Advanced |
| ASI04 | Agentic Supply Chain Vulnerabilities | High | AVE-2026-00062, AVE-2026-00074 | Hardening–Advanced |
| ASI05 | Unexpected Code Execution (RCE) | Critical | AVE-2026-00054 | Foundational–Advanced |

Severity and Tier above are the OWASP Agentic Top 10's own published
ratings for each ASI entry (matching the values already used consistently
in `Agentic_MITREATLAS.md` and `Agentic_AIUC1.md` for the same entries),
not an AVE-assigned value. AVE's own per-record severity is a separate,
narrower rating — see the detailed mappings below.

This table omits a "Framework domain/control summary" section: AVE, like
MITRE ATLAS, is a flat taxonomy without a domain grouping layer, so that
section (present in the AIUC-1 mapping, which does have domains A–F)
doesn't apply here. Same reasoning `Agentic_MITREATLAS.md` already used.

---

## Audience tags

- **Red teamer** — full file, behavioral fingerprints describe the exact mechanism to reproduce
- **Detection / scanner engineer** — full file; every AVE record declares `indicators_of_compromise` and scanner-facing evidence fields (`evidence_kind_default`, `detection_stage`) not shown in this crosswalk's control-tier framing
- **Security engineer** — ASI02, ASI04, ASI05
- **Skill / MCP server author** — ASI04 (supply chain hygiene for what you ship)

---

## Detailed mappings

---

### ASI01 — not covered in this pilot

Not an oversight: ASI01 (Agent Goal Hijack) was deliberately left out.
Two AVE records with a single `owasp_asi: ["ASI01"]` tag were considered
during selection — `AVE-2026-00059` and `AVE-2026-00065` — and both were
excluded once re-verified against ASI01's primary-source text, because
their described mechanisms matched ASI04's own named example scenarios
at least as well. See the Methodology note below for the full reasoning.
ASI03, ASI06–ASI10 are likewise not covered — this pilot only maps
entries with a record this batch could verify cleanly.

---

### ASI02 — Tool Misuse and Exploitation

**Severity:** Critical (OWASP's rating for this entry)

Agents misuse legitimate tools they are already authorized to use —
through prompt manipulation, unsafe delegation, or command chaining —
producing an unintended capability without any single call exceeding
its own granted scope.

**Real-world reference:** MOSAIC (arXiv:2607.02857) — Wu, Wang, Zhang,
Nan, Wang — demonstrates this exact composition mechanism achieving a
96.59% attack success rate across 2,525 trials spanning five real-world
CLI coding agents and five backend LLMs, entirely within benign-looking
developer task scenarios.

#### AVE mapping

| AVE Record | ID | Basis for correspondence | Tier | Scope |
|---|---|---|---|---|
| Tool Abuse — CLI Command Composition | [AVE-2026-00068](https://github.com/aveproject/ave/blob/main/records/AVE-2026-00068.json) | Matches ASI02's own scope definition verbatim: "agent operates within authorized privileges but applies a legitimate tool in an unsafe or unintended way." No sandbox breakout or code injection occurs — commands compose through shared OS state (env vars, file descriptors, working directory) into a capability beyond task authorization, which is squarely tool misuse, not ASI05 (Unexpected Code Execution). | Foundational | Both |

#### AVE's own remediation guidance

(Reproduced from the record's `remediation` field, Apache-2.0.)

> Scope each command's access to shared OS state as narrowly as the
> individual task requires, rather than allowing an entire session's
> commands to share an unrestricted environment, working directory, and
> file descriptor space. Where feasible, isolate command executions
> that serve unrelated sub-tasks into separate scopes or sandboxes so
> that one command's artifacts cannot become another's input. Treat
> command-sequence review as a distinct security check from
> single-command review, since the two catch different classes of risk.

#### Cross-references

- OWASP MCP Top 10: MCP05
- Other AVE crosswalks: none yet independently verified for this record
  (`mitre_atlas`/`nist_ai_rmf` are empty on the source record — not
  populated here rather than guessed)

---

### ASI04 — Agentic Supply Chain Vulnerabilities

**Severity:** High (OWASP's rating for this entry)

Agents, tools, and related artifacts supplied by third parties may be
malicious, compromised, or silently substituted after review — often
resolved dynamically at runtime with no static inventory or integrity
check at the point of use.

**Real-world references:**
- AVE-2026-00074: AIR Security's disclosed "SkillJacking" research
  found 925 skills serving ~134,000 agents sitting on this exact class
  of hijackable dependency, including a confirmed takeover — the
  `seedance2-api` skill (11,483 installs) hijacked by re-registering its
  deleted GitHub owner account.
- AVE-2026-00062: no named real-world incident on record; grounded in
  CWE-1357 (Reliance on an Insufficiently Trustworthy Component) rather
  than an incident citation.

#### AVE mapping

| AVE Record | ID | Basis for correspondence | Tier | Scope |
|---|---|---|---|---|
| Supply Chain — Unpinned Dependency Substitution | [AVE-2026-00062](https://github.com/aveproject/ave/blob/main/records/AVE-2026-00062.json) | Matches ASI04's own "Pinning" and "Dependency gatekeeping" mitigation guidelines almost word for word — a mutable reference (tag, range, unpinned name) lets the reviewed and executed artifact silently diverge. | Foundational | Both |
| Supply Chain — Dead Anchor Reclamation (SkillJacking) | [AVE-2026-00074](https://github.com/aveproject/ave/blob/main/records/AVE-2026-00074.json) | Matches ASI04's own "Impersonation and typo squatting" example: a previously-legitimate external anchor (repo, package, domain) is reclaimed by an attacker after its original owner abandons it. The record's own text explicitly distinguishes this from AVE-2026-00062 — pinning would not have prevented this, since the reference was precise and stable when written; the vulnerability is the anchor's identity changing *after* publication, not an unresolved reference. | Hardening | Both |

#### AVE's own remediation guidance

(Reproduced from each record's `remediation` field, Apache-2.0.)

> **AVE-2026-00062:** Pin every dependency to an exact version and,
> where the ecosystem supports it, a content hash. Use a lockfile
> mechanism and commit it. Treat any dependency update as a reviewable
> change to the manifest itself, not something that happens silently
> underneath an unchanged reference.

> **AVE-2026-00074:** Do not treat a specific, well-formed external
> reference as permanently safe once reviewed; periodically re-verify
> that referenced GitHub owners, packages, domains, and cloud
> subdomains still resolve to their original, reviewed owner before
> trusting content fetched or installed from them. Where feasible, pin
> to a content hash or commit SHA rather than a mutable owner/name, and
> treat any pre-install or pre-fetch step that resolves an external
> anchor as a point requiring a fresh trust check, not a one-time
> review at publication time. Registries hosting skills should
> periodically re-scan published skills for anchor decay rather than
> only screening at submission.

#### Cross-references

- OWASP MCP Top 10: MCP04 (both records)
- Other AVE crosswalks: none yet independently verified for either
  record (`mitre_atlas`/`nist_ai_rmf` are empty on both source records)

---

### ASI05 — Unexpected Code Execution (RCE)

**Severity:** Critical (OWASP's rating for this entry)

Agentic systems that generate or execute code become RCE gateways when
a sandbox intended to confine that execution fails to enforce its own
boundary — a distinct failure mode from ASI02, which covers misuse of
tools the agent was never meant to be confined from in the first place.

**Real-world reference:** CERT/CC VU#414811 / CVE-2026-5752 — Jeremy
Brown's coordinated disclosure of a Cohere Terrarium sandbox escape via
JavaScript prototype-chain traversal, CVSS 9.3.

#### AVE mapping

| AVE Record | ID | Basis for correspondence | Tier | Scope |
|---|---|---|---|---|
| Execution Hijack — Code Execution Sandbox Escape | [AVE-2026-00054](https://github.com/aveproject/ave/blob/main/records/AVE-2026-00054.json) | The OWASP primary source's own text for ASI05 uses the phrase "sandbox escape" verbatim for this exact outcome class. The record is explicit that this is about a flaw in the sandbox's *own containment* — exploitable even by code the agent was authorized to run — not how malicious code gets in (that's AVE-2026-00042, a separate record). | Foundational | Both |

#### AVE's own remediation guidance

(Reproduced from the record's `remediation` field, Apache-2.0.)

> Use strong isolation primitives for untrusted code execution — a
> dedicated microVM (e.g. Firecracker) or gVisor-class sandbox with its
> own kernel, not a shared-kernel container or in-process VM context.
> Never expose Node.js `vm.Script`, Python `exec()`/`eval()` run
> in-process, or similar in-language sandboxing as the sole isolation
> boundary for untrusted code — these share the host language runtime's
> prototype/object model and are not designed as a security boundary.
> Run the code-execution process with the minimum host privileges
> necessary, never as root. Monitor sandboxed process behavior for
> filesystem, network, or process-table access outside the declared
> execution boundary. Apply defense-in-depth: scan submitted code for
> known escape-technique signatures before execution as an additional
> signal, not a sole control.

#### Cross-references

- OWASP MCP Top 10: MCP05, MCP07
- Other AVE crosswalks: none yet independently verified for this record
  (`mitre_atlas`/`nist_ai_rmf` are empty on the source record)

---

## Tools

Deliberately omitted. AVE's own hard rules (`CLAUDE.md`) exclude
vendor/tool recommendations from records by design — "vendor-neutral
only, no enforcement-tool config ever belongs here." Naming specific
commercial or open-source tools in this mapping would misrepresent
what AVE itself claims to be. `Agentic_MITREATLAS.md` and
`Agentic_AIUC1.md` both include a Tools table because their source
frameworks make tool recommendations natively; AVE does not.

## Implementation priority

Not included. A 3-of-10-entry pilot doesn't carry enough coverage for
a meaningful phased rollout table — the existing tables in
`Agentic_MITREATLAS.md`/`Agentic_AIUC1.md` sequence across all 10
entries. Deferred to a future full-corpus mapping round rather than
filled in with placeholder ordering.

---

## Methodology note

Each `AVE Record` row above was verified against the OWASP Agentic Top
10 2026 primary-source PDF's own category text (`genai.owasp.org`,
document ID 52117) directly — not by category-name resemblance to the
`attack_class` string, and not by trusting the AVE record's own
existing `owasp_asi` tag at face value. Every one of these 4 records
was independently re-verified even though its tag was also untouched by
AVE's own internal `owasp_asi` corpus audit (aveproject/ave#196).

Two candidate records were excluded during selection specifically
because that re-verification found a real ambiguity the internal audit
had not caught: `AVE-2026-00059` (fragmented cross-description
injection) and `AVE-2026-00065` (A2A agent-card poisoning) both carried
a single `ASI01` tag, but their described mechanisms match ASI04's own
named example scenarios ("Tool-descriptor injection" and
"Agent-in-the-Middle via Agent Cards," respectively) at least as well as
ASI01's. Neither is included here as a result — being explicit about
what didn't make the cut is offered as evidence of how this pilot was
actually verified, not just a list of what passed.

`Tier` values for AVE records reuse the OWASP-entry-level ranges already
established in `Agentic_MITREATLAS.md`/`Agentic_AIUC1.md`, plus a
per-record judgment grounded in that record's own `remediation` text
(e.g. AVE-2026-00074's periodic re-verification requirement reads as
Hardening-tier, not baseline Foundational hygiene, the same distinction
those two files draw elsewhere). `Scope` is `Both` throughout — none of
these four records' mechanisms are addressable by a purchased vendor
capability alone.

---

## References

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [AVE registry](https://aveproject.org) · [AVE schema](https://aveproject.org/schema.html) · [github.com/aveproject/ave](https://github.com/aveproject/ave)
- [AVE-2026-00054](https://github.com/aveproject/ave/blob/main/records/AVE-2026-00054.json) — citing CERT/CC VU#414811, CVE-2026-5752, CWE-693
- [AVE-2026-00062](https://github.com/aveproject/ave/blob/main/records/AVE-2026-00062.json) — citing CWE-1357
- [AVE-2026-00068](https://github.com/aveproject/ave/blob/main/records/AVE-2026-00068.json) — citing MOSAIC, arXiv:2607.02857
- [AVE-2026-00074](https://github.com/aveproject/ave/blob/main/records/AVE-2026-00074.json) — citing AIR Security's SkillJacking disclosure, CWE-829

---

## Changelog

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-08-30 | 2026-Q1-pilot | Initial mapping — 4-record pilot, ASI02/ASI04/ASI05 only | aveproject |

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
