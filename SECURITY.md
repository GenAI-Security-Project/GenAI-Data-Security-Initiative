# Security Policy

The **OWASP GenAI Data Security Initiative** publishes security research, guidance, datasets, and tooling for the GenAI/LLM ecosystem. As a security project, the organization holds its artifacts to high standards and describes here how to report vulnerabilities or material defects.

## Scope

This policy applies to content in the repository:

- **Code** — Python validators, the `dsgai_scanner_tool`, JavaScript crosswalk explorer, HTML resources, and CI/build scripts
- **Datasets** — `dsgai-bench`, validation datasets, and community-contributed data
- **Frameworks & documentation** — risk taxonomies, best-practices guides, and framework crosswalk content where errors could materially mislead readers

### In Scope

- Code execution, injection, deserialization, path traversal, SSRF, XSS vulnerabilities
- Prompt injection, jailbreaks, or unsafe LLM-output handling
- Dataset poisoning, contamination, or adversarial-example susceptibility
- Sensitive data accidentally committed (keys, tokens, PII)
- Datasets containing live secrets, PII, or copyrighted material
- Supply-chain issues (compromised dependencies, malicious build steps)
- Authoritative errors in published guidance leading to weaker security

### Out of Scope

- Misuse of published frameworks by third parties
- Upstream dependency vulnerabilities (report these to the upstream vendor)
- Issues in third-party frameworks the crosswalk maps to
- Theoretical risks already documented in the taxonomy
- Social-engineering, physical, or denial-of-service testing
- Findings from automated scanners without demonstrated impact

## Reporting a Vulnerability

**Do not open public GitHub issues, pull requests, or Discussions for security reports.**

Use a private channel:

1. **GitHub Private Vulnerability Reporting** *(preferred for sensitive content — encrypted in transit and at rest):*
<https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/security/advisories/new>
2. **Email:** `emmanuelgjr@owasp.org` with subject `[SECURITY] GenAI Data Security Initiative — <summary>`

We will acknowledge receipt within **3 business days**.

### Include where possible

- Affected file(s), commit SHA, dataset record(s), or release version
- Issue description and realistic impact
- Reproduction steps or minimal proof-of-concept
- Suggested severity (CVSS v4.0 or v3.1 vector if available)
- Suggested remediation
- Attribution preferences (public credit, alias, or anonymous)

### Do not include in reports

- Real PII, real credentials, or proprietary data from third parties
- Screenshots or logs that disclose third-party systems without their consent
- Live exploitation against systems you do not own

If a reproduction requires sensitive data, describe its shape and we will coordinate a safe reproduction environment.

### Encrypted email

For follow-up communications that require encryption, request our PGP key in your initial message and we will reply with a current fingerprint over a separate channel. **Do not include sensitive material in the first email** — use GitHub Private Vulnerability Reporting for that, or wait for the key exchange to complete. Verify any fingerprint we provide via at least one independent channel before encrypting sensitive material.

## Our Commitments

| Stage                              | Target                                                                 |
|------------------------------------|------------------------------------------------------------------------|
| Initial acknowledgement            | within 3 business days                                                 |
| Triage and severity assessment     | within 10 business days                                                |
| Status updates during triage       | at least every 14 days                                                 |
| Fix or mitigation — **Critical**   | within 30 days of validation                                           |
| Fix or mitigation — **High**       | within 60 days of validation                                           |
| Fix or mitigation — **Medium/Low** | within 90 days of validation                                           |
| Coordinated public disclosure      | at fix release, or 90 days from triage, whichever is sooner (extendable by mutual agreement) |

The organization scores code findings using **CVSS v4.0** (falling back to v3.1 where v4.0 vectors are not yet supported by downstream consumers). AI/ML-specific findings are additionally classified against the **OWASP Top 10 for LLM Applications**, the **OWASP GenAI Data Security Risks and Mitigations** taxonomy, and **MITRE ATLAS**.

## Coordinated Disclosure

The project follows a coordinated disclosure model aligned with **ISO/IEC 29147** and **CERT/CC** guidance:

- Public-disclosure date is agreed with reporters (default 90 days from triage).
- Reporter identity is kept confidential by default; public credit is given only with the reporter's explicit consent.
- Credit, when given, appears in the published advisory and in [`SECURITY-THANKS.md`](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/blob/main/SECURITY-THANKS.md).
- Early guidance is published if active exploitation occurs in the wild.
- CVEs are requested through **GitHub** as CNA for qualifying issues in code and tooling; for issues affecting third-party components, we coordinate with the upstream CNA.

## Safe Harbor

If you make a good-faith effort to comply with this policy when researching or reporting an issue, the project will:

- Consider your research authorized under this policy.
- Work with you to understand and resolve the issue promptly.
- Not initiate or support legal action against you for accidental, good-faith violations of this policy, including under anti-circumvention or unauthorized-access statutes.

To remain within safe harbor, you must:

- Avoid privacy violations, destruction of data, and disruption of services.
- Interact only with accounts and data you own or have explicit permission to access.
- Exfiltrate only the minimum data necessary to demonstrate the issue, and delete it after the report is resolved.
- Provide reasonable time for remediation before any public disclosure.

This safe harbor applies only to this project. It does not waive obligations you may have to third parties (employers, customers, regulators) or authorize action against systems we merely reference.

## Supported Versions

Security fixes are maintained for the current published edition and the `main` branch. Prior editions receive critical fixes for **12 months** after successors ship.

| Artifact                                          | Currently Supported  |
|---------------------------------------------------|----------------------|
| GenAI Data Security Risks and Mitigations         | 2026 v1.0            |
| LLM and GenAI Data Security Best Practices        | 2025 v1.0            |
| `dsgai-bench`                                     | latest tag on `main` |
| `dsgai_scanner_tool`                              | latest tag on `main` |
| Crosswalk Explorer                                | `main`               |

## Dependencies & Supply Chain

- Direct dependencies are pinned (`requirements.txt`, `package-lock.json`).
- **Dependabot** version and security updates are enabled (`.github/dependabot.yml`).
- All pull requests are scanned by `actions/dependency-review-action`, which blocks known-vulnerable or disallowed-license additions.
- Third-party GitHub Actions are pinned to commit SHAs (not tags).
- **Secret scanning** and **push protection** are enabled on the repository.
- **CodeQL** runs on `main` and on pull requests.
- Releases include SHA-256 checksums; signed releases use Sigstore / `gh attestation` where the artifact format supports it.
- Anyone observing a release artifact whose checksum or signature does not verify should treat it as a potential incident and report under "Reporting a Vulnerability" above.

## Acknowledgements

The project credits researchers in [`SECURITY-THANKS.md`](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/blob/main/SECURITY-THANKS.md).

---

_Policy version: 1.1 — Last reviewed: 2026-05-18._
_Material changes are announced in repository release notes._
