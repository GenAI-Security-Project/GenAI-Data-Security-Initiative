# Governance

This document defines how the OWASP GenAI Crosswalk project is
maintained, how decisions are made, and how contributors can grow
into leadership roles.

---

## Maintainers

| Role | Responsibility | Current holder |
|---|---|---|
| Lead maintainer | Final decision authority; release management | [@emmanuelgjr](https://github.com/emmanuelgjr) |
| Framework lead | Owns quality for one or more framework mapping families | See CODEOWNERS |
| Contributor | Submits PRs; no merge authority | Open to all |

To become a framework lead, submit five merged PRs to a framework
family and express interest in `#genai-security` on the OWASP Slack.

---

## PR review SLO

| PR type | First response | Merge target |
|---|---|---|
| Bug fix / broken link | 24 hours | 48 hours |
| Content update (existing file) | 48 hours | 5 business days |
| New mapping file | 72 hours | 10 business days |
| New framework (adds column to matrix) | 1 week | Requires maintainer sign-off |

If a PR has no response within the SLO, the submitter may ping
`@emmanuelgjr` directly on the PR thread.

---

## Decision-making

**Routine decisions** (content updates, bug fixes, new entries within
existing frameworks): single maintainer or framework lead approval
is sufficient.

**Significant decisions** (new frameworks, schema changes, source list
additions, breaking changes to directory structure): require the lead
maintainer to post a 5-business-day comment period on the PR or an
Issue before merging.

**Mapping disputes** — if two contributors propose conflicting mappings
for the same vulnerability and framework:
1. Both proposals must cite a primary source (framework document, CVE, OWASP page).
2. The framework lead for that mapping family makes the call.
3. If no framework lead exists, the lead maintainer decides.
4. The losing proposal's evidence is documented in a `<!-- DISPUTE -->` comment in the file.

---

## Release process

Releases follow [Semantic Versioning](https://semver.org/):

| Change | Version bump |
|---|---|
| New mapping file | Minor (`x.Y.0`) |
| New source list coverage | Minor (`x.Y.0`) |
| Updated mapping content, new CVE ref | Patch (`x.y.Z`) |
| New recipe | Patch (`x.y.Z`) |
| Breaking schema change | Major (`X.0.0`) |
| Org transfer or rename | Major (`X.0.0`) |

Steps to cut a release:
1. Update `CHANGELOG.md` with version entry and date.
2. Update README.md version badge and counts.
3. Commit: `Add [list of files] — vX.Y.Z`.
4. Create a GitHub Release with the same tag; attach `data/schema.json`
   as a release artifact for programmatic consumers.

---

## What the project will NOT do

- Recommend specific commercial vendors or paid tools (TOOLS.md is
  open-source only unless commercial-open-source dual-licensed).
- Map to frameworks that are not publicly accessible without payment
  (exception: ISO standards are referenced by clause number and title,
  allowing verification without full text access).
- Remove mappings without evidence that they are incorrect — old
  mappings are deprecated with `<!-- DEPRECATED: reason -->`, not deleted.

---

## Conflict of interest

Contributors who are employed by, or have a commercial interest in,
a framework body (e.g., an ISO working group member) must disclose
this in the PR. Disclosed COIs are noted in the mapping file's
changelog entry; they do not disqualify the contribution.

---

## Inactive maintainers

A maintainer who has not merged a PR, responded to an Issue, or made
a commit in 6 months is considered inactive. The lead maintainer may
transfer framework-lead ownership to an active contributor after a
public 2-week notice period on the project's GitHub Discussions.

---

## Code of Conduct

This project follows the [Contributor Covenant 2.1](CODE_OF_CONDUCT.md).
Violations should be reported to the OWASP Foundation at
`conduct@owasp.org`.

---

## Questions

Open a GitHub Discussion or reach the lead maintainer via OWASP Slack
`#genai-security`.
