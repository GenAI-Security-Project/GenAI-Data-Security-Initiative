# Security Policy

The **OWASP GenAI Data Security Initiative** publishes security research,
guidance, datasets, and tooling for the GenAI/LLM ecosystem. As a security
project, we hold our own artifacts to the standards we ask others to meet —
this policy describes how to report vulnerabilities or material defects in
anything we publish.

## Scope

This policy applies to content in this repository:

- **Code** — Python validators, the `dsgai_scanner_tool`, the JavaScript
  crosswalk explorer, HTML resources, and CI/build scripts.
- **Datasets** — `dsgai-bench`, validation datasets, and community-contributed
  data hosted here.
- **Frameworks & documentation** — risk taxonomies, best-practices guides, and
  the framework crosswalk content, where errors could materially mislead a
  reader in a way that weakens their security posture.

### In scope

- Code execution, injection, deserialization, path traversal, SSRF, XSS in
  tools we ship
- **Prompt injection, jailbreaks, or unsafe LLM-output handling in
  `dsgai_scanner_tool`** or any other AI-enabled component we ship
- **Dataset poisoning, contamination, or adversarial-example susceptibility**
  in `dsgai-bench` or validation datasets
- Sensitive data accidentally committed (keys, tokens, PII, proprietary
  third-party content)
- Datasets containing live secrets, PII, copyrighted material, or content
  that could enable harm at scale
- Supply-chain issues (typosquatted/compromised dependencies, malicious build
  steps, tampered releases)
- Authoritative errors in published guidance that would lead a reasonable
  implementer to a less-secure outcome
- Unverifiable or modified release artifacts

### Out of scope

- Misuse of our published frameworks or taxonomies by third parties
- Vulnerabilities in upstream dependencies — please report those upstream;
  we will pin/patch once an advisory exists
- Issues in third-party frameworks the crosswalk maps to (NIST AI RMF,
  ISO/IEC 42001, MITRE ATLAS, etc.) — those belong with their maintainers
- Theoretical risks already documented in our published taxonomy
- Social-engineering, physical, or denial-of-service testing against
  contributors or infrastructure
- Findings produced solely by automated scanners without demonstrated impact

## Reporting a Vulnerability

**Do not open a public GitHub issue for security reports.**

Use one of the following private channels:

1. **Preferred — GitHub Private Vulnerability Reporting:**
   <https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/security/advisories/new>
2. **Email:** `emmanuelgjr@owasp.org`
   Subject: `[SECURITY] GenAI Data Security Initiative — <short summary>`

For escalation involving OWASP infrastructure (not this repository's content),
contact the OWASP Foundation directly: <https://owasp.org/contact/>.

Please include, where possible:

- Affected file(s), commit SHA, dataset record(s), or release artifact
- Description of the issue and realistic impact
- Reproduction steps or a minimal proof-of-concept
- Suggested remediation, if you have one
- Whether you wish to be credited, and the name/handle to use

If you need to send sensitive material, request our PGP key in your initial
email (fingerprint published once generated) and we will respond before you
transmit details. Reports are accepted in **English**.

## Our Commitments

| Stage                          | Target                       |
|--------------------------------|------------------------------|
| Initial acknowledgement        | within 3 business days       |
| Triage and severity assessment | within 10 business days      |
| Status updates during triage   | at least every 14 days       |
| Fix or mitigation plan         | within 90 days of validation |

We use **CVSS v3.1** for severity scoring and will request a CVE for
qualifying issues in shipped code or releases. AI-specific findings are
additionally classified using the **OWASP Top 10 for LLM Applications** and,
where applicable, the categories in our own *GenAI Data Security Risks and
Mitigations 2026*.

## Coordinated Disclosure

We follow a **coordinated disclosure** model:

- We will agree a public-disclosure date with you, default 90 days from
  validated triage, or sooner if a fix ships earlier.
- We will not disclose your identity without consent.
- We will credit reporters in the published advisory and in
  [`SECURITY-THANKS.md`](./SECURITY-THANKS.md), unless you request anonymity.
- If a vulnerability is being actively exploited in the wild, we may publish
  guidance ahead of the agreed date and will notify you first.

## Safe Harbor

We consider security research conducted in good faith under this policy to be:

- Authorized under applicable anti-hacking and anti-circumvention laws, and
- Exempt from restrictions in our terms of use that would interfere with
  good-faith security research.

You are expected to comply with all applicable laws, avoid privacy violations,
data destruction, and service disruption, and to use only the access necessary
to demonstrate the issue. If in doubt about whether a planned activity is
covered, contact us before testing.

## Supported Versions

We maintain security fixes for the **current published edition** of each
artifact and the `main` branch. Prior editions receive fixes only for
**critical** issues, for 12 months after a successor edition ships.

| Artifact                                         | Currently supported  |
|--------------------------------------------------|----------------------|
| GenAI Data Security Risks and Mitigations        | 2026 v1.0            |
| LLM and GenAI Data Security Best Practices       | 2025 v1.0            |
| `dsgai-bench`                                    | latest tag on `main` |
| `dsgai_scanner_tool`                             | latest tag on `main` |
| Crosswalk Explorer                               | `main`               |

## Dependencies & Supply Chain

- Direct dependencies are pinned (`requirements.txt`, `package-lock.json`).
- We monitor advisories via GitHub Dependabot and act on `high`/`critical`
  alerts within the SLA above.
- Releases are produced from signed, tagged commits on `main`. Verify
  integrity using the SHA-256 hashes (and, once available, signatures)
  published with each release.

## Acknowledgements

We thank the researchers who help keep this project — and the wider GenAI
security community — safer. Credited reporters are listed in
[`SECURITY-THANKS.md`](./SECURITY-THANKS.md).

---

*This policy is published under [CC BY-SA 4.0](./LICENSE) and is itself open
to community review — open a PR to suggest improvements.*
