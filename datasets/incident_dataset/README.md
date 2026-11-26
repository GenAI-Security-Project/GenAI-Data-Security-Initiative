# GenAI Data Security Incident Database

A structured catalog of real-world data security incidents in GenAI deployments, mapped to the DSGAI risk taxonomy.

**Status:** 17 public incidents; accepting contributions. **Browse:** [INDEX.md](INDEX.md) lists every incident.

## Scope

Documented incidents where GenAI systems experienced data security failures in production or staging environments. This includes data leakage events, cross-tenant bleed, RAG exfiltration, agent credential exposure, training data extraction, vector store compromise, telemetry over-collection, and any other incident aligned with the DSGAI risk taxonomy (DSGAI01–DSGAI21).

This dataset is modeled on existing incident databases (e.g., AIAAIC, AI Incident Database) but focused specifically on **data security failure modes** in GenAI systems. Incidents that are also in the [crosswalk incident list](https://genai-security-project.github.io/crosswalk/#/incidents) carry its ID in `crosswalk_id`.

## Two kinds of entry: public and anonymized

Every entry sets `disclosure` to one of two values. The schema enforces the difference.

| | `"disclosure": "public"` | `"disclosure": "anonymized"` |
| --- | --- | --- |
| **What it is** | An incident already disclosed in public: a vendor or researcher advisory, a regulator notice or filing, a peer-reviewed or preprint paper, or reputable news reporting | A self-report or any incident that is not public, e.g. one from your own organization |
| **Organization names** | Allowed, for the organization(s) affected by or responsible for the incident, exactly as the cited sources name them, listed in `affected_organizations` | Not allowed anywhere in the entry (`affected_organizations` is rejected) |
| **Sources** | `source_urls` is **required**: at least one public, citable URL | Optional; `source` can say "Anonymized self-report" |
| **People's names** | Not allowed. Credit researchers by citing their published work in `source_urls` | Not allowed |
| **CI name scan** | Flags person names only | Flags person and organization names |

### Rules for public entries

1. **Stay within the sources.** Describe only what the cited sources state. Don't add allegations, speculation about cause, or blame the sources don't make. If sources disagree, say so.
2. **Primary sources first.** Prefer the affected vendor's advisory or post-mortem, the regulator's notice, or the researchers' own paper over secondary coverage.
3. **The organization is the subject, never the sponsor.** An organization may be named only as the affected party or the party responsible for the failure. No other organization names (e.g. a security vendor that "detected" the incident) unless a source makes them part of the incident itself. Links to a contributor's own company, product, blog or tool are not accepted, and a write-up by the contributor or their employer cannot be the only source.
4. **Public is public.** Only incidents disclosed by the organization, a regulator, the researchers, or reputable press. Leaks, rumors, social-media posts and unconfirmed reports go in as `anonymized`, or not at all.
5. **Your own words.** Write the summary and impact yourself; don't paste text from sources or from other incident databases.

Self-reported incidents from your own organization are welcome and encouraged — submit them as `anonymized`, which makes them safe to share.

### Rules for anonymized entries

- No organization names, employee names, or customer names
- No IP addresses, internal hostnames, or system identifiers
- No proprietary model names unless publicly known
- Generalize details that could identify a specific organization (e.g., "a financial services company" not "Bank X")

## Data format

Each entry is one JSON file in `entries/`, named after its `incident_id` (e.g. `entries/INC-0001.json`), that validates against [`schema.json`](schema.json) in this folder. Start the file with `"$schema": "../schema.json"`.

Required fields: `incident_id`, `title`, `disclosure`, `date`, `summary`, `dsgai_mapping`, `attack_vector`, `data_types_affected`, `impact` — plus `source_urls` for public entries.

| Field | Notes |
| --- | --- |
| `incident_id` | `INC-` plus four digits, assigned on merge; matches the file name |
| `title` | One-line headline (may name the organization only in public entries) |
| `disclosure` | `public` or `anonymized` (see above) |
| `date` | When the incident occurred or was first disclosed (ISO 8601). If only the month or year is known, use its first day and set `precision` to `month` or `year` |
| `summary` | What happened |
| `dsgai_mapping` | DSGAI entries (DSGAI01–DSGAI21), primary first |
| `attack_vector` | How the data security failure occurred |
| `data_types_affected` | `pii`, `phi`, `credentials`, `ip`, `model_weights`, `embeddings`, `system_prompts`, `financial`, `other` |
| `impact` | Scope of data exposed, regulatory consequences, operational disruption |
| `root_cause`, `detection_method`, `mitigations_applied` | Optional, where known |
| `source` | Free-text description of the source |
| `source_urls` | Public sources (required for public entries) |
| `affected_organizations` | Public entries only |
| `industry` | Sector, if known |
| `crosswalk_id` | Matching crosswalk incident ID, e.g. `INC-006` |
| `contributor` | Optional: your `name` and, optionally, one `orcid`. No affiliation or links |

Example (public):

```json
{
  "$schema": "../schema.json",
  "incident_id": "INC-0001",
  "title": "Example Vendor chatbot shows users other users' conversation titles",
  "disclosure": "public",
  "date": "2023-03-01",
  "precision": "month",
  "summary": "A caching bug in Example Vendor's hosted chatbot showed some users the titles of other users' conversations and, for a small share of subscribers, partial payment details.",
  "dsgai_mapping": ["DSGAI11", "DSGAI01"],
  "attack_vector": "Software defect in a shared cache returned another session's data",
  "data_types_affected": ["pii", "financial"],
  "impact": "Conversation titles exposed across users; payment details of a small share of subscribers visible to others for several hours",
  "source": "Vendor post-mortem",
  "source_urls": ["https://vendor.example/blog/march-incident"],
  "affected_organizations": ["Example Vendor Inc."]
}
```

## Validating and listing

```bash
cd datasets/incident_dataset
python validate.py       # schema, disclosure rule, DSGAI IDs, IDs match file names
python build_index.py    # regenerate INDEX.md; commit it with your entry
```

CI runs both, and fails if `INDEX.md` is out of date.

## Contributing

Add each incident as its own JSON file in `entries/`, regenerate `INDEX.md`, and submit a pull request. See the [main datasets README](../README.md) for general contribution guidelines.
