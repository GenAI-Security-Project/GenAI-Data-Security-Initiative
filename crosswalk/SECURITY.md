# Security Policy

## Scope of this policy

This policy covers security vulnerabilities in the content and tooling
of the **OWASP GenAI Crosswalk** repository — specifically:

- Factually incorrect security guidance that could mislead practitioners
  into deploying insecure controls
- Inaccurate framework control mappings that misrepresent compliance
  obligations (e.g., incorrect EU AI Act article citations, wrong
  ISO 27001 Annex A references)
- Malicious content introduced via pull request or contribution
- Security issues in any tooling, scripts, or CI/CD workflows
  contained in this repository

**This repository is documentation, not deployable code.** If you have
found a vulnerability in an OWASP project, product, or tool referenced
in this repository, please report it directly to that project.

---

## Supported versions

| Branch / Tag | Supported |
|---|---|
| `main` (latest) | ? Yes |
| Tagged releases | ? Yes — current release only |
| Older tags | ? No — update to latest |

---

## Reporting a vulnerability

**Please do not report security issues via public GitHub issues.**

For issues that could mislead practitioners or introduce harmful content
into the open-source security community, we ask for responsible disclosure:

### Option 1 — GitHub private security advisory (preferred)

Use GitHub's built-in private vulnerability reporting:

1. Go to the **Security** tab of this repository
2. Click **Report a vulnerability**
3. Complete the advisory form with as much detail as possible

This creates a private thread visible only to maintainers.

### Option 2 — Direct contact

Email the OWASP GenAI Data Security Initiative maintainers at:

**[genai-security@owasp.org](mailto:genai-security@owasp.org)**

Include in your report:

- Which file(s) are affected
- A description of the issue and why it constitutes a security or
  accuracy concern
- The correct information or mapping where known
- Your name / handle if you would like to be credited

---

## What we consider a security issue in this repo

| Issue type | Examples |
|---|---|
| **Incorrect control mapping** | Mapping LLM01 to an ISO 27001 control that does not apply, or omitting a critical required control |
| **Misleading compliance guidance** | Incorrectly stating that implementing Control X satisfies EU AI Act Article Y when it does not |
| **Fabricated references** | Citations to non-existent CVEs, framework versions, or OWASP entries |
| **Harmful content injection** | Malicious code, backdoors, or adversarial content introduced via PR |
| **Misinformation at scale** | Guidance that would cause organisations to believe they are compliant when they are not |

---

## What we do NOT consider a security issue

- Disagreements with editorial choices, risk ratings, or control priorities
- Missing framework mappings (use a regular GitHub issue)
- Typos, grammar, or formatting issues (use a PR)
- Requests to add frameworks or source lists (use a GitHub issue with
  the `enhancement` label)

---

## Response commitments

| Stage | Target |
|---|---|
| Initial acknowledgement | Within 5 business days |
| Assessment and triage | Within 10 business days |
| Fix or public advisory | Within 30 days for confirmed issues |
| Credit acknowledgement | In the CHANGELOG.md release notes |

We will keep reporters informed of progress. If a fix requires
significant rework of a mapping file, we will publish a correction
notice in the CHANGELOG.md before the fixed version is tagged.

---

## Credit

Reporters of confirmed vulnerabilities will be credited in the
CHANGELOG.md release notes under a **Security acknowledgements** section,
unless they request to remain anonymous.

We do not offer monetary rewards (bug bounties) for this repository.

---

## OWASP vulnerability disclosure policy

This project follows the OWASP vulnerability disclosure policy:
https://owasp.org/www-policy/operational/bug-bounty

---

*Part of the [OWASP GenAI Crosswalk](https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk) —
maintained by the [OWASP GenAI Data Security Initiative](https://genai.owasp.org)*
