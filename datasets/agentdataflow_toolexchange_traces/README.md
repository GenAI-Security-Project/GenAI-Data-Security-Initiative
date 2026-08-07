# Agent Data Flow & Tool Exchange Traces

Sanitized traces of agentic AI tool calls, plugin data exchanges, and delegation chains for security research.

**Status:** Accepting contributions — this dataset is being built from scratch with the community.

## Scope

Structured traces capturing how data flows through agentic AI systems — between agents, tools, plugins, APIs, and memory stores. This dataset supports research into DSGAI06 (Tool, Plugin & Agent Data Exchange Risks), DSGAI02 (Agent Identity & Credential Exposure), DSGAI15 (Over-Broad Context Windows & Prompt Over-Sharing), and related agent security patterns.

Categories include:

- **Tool call traces** (`tool_call`) — Sequences of tool invocations showing what data is sent to and received from external tools (APIs, databases, file systems, code execution environments)
- **Multi-agent delegation chains** (`multi_agent_delegation`) — Traces showing how tasks and data are passed between agents, including what context is forwarded, filtered, or accumulated
- **Plugin data exchange logs** (`plugin_data_exchange`) — Records of data shared with third-party plugins, including request/response payloads and metadata
- **Credential and permission flows** (`credential_flow`) — How credentials, tokens, and permissions are scoped, delegated, and consumed across agent workflows
- **Context accumulation patterns** (`context_accumulation`) — Traces showing how agent context windows grow over multi-step tasks, what data persists across steps, and where over-sharing occurs
- **Memory read/write traces** (`memory_read_write`) — How agents interact with short-term and long-term memory stores, including what data is persisted and retrieved

## Files

| File | Purpose |
|---|---|
| `schema.json` | JSON Schema (draft 2020-12) every entry validates against |
| `example.json` | Worked example. Read it with the schema before writing an entry |
| `entries/` | One trace per file, named `<trace_id>.json` |
| `validate.py` | `python validate.py` - schema, provenance, span graph, and secret-scan checks |
| `build_index.py` | `python build_index.py` - regenerates `index.csv` |
| `index.csv` | Flat index of all entries, for filtering and citation |

## Data Format

One trace per file in `entries/`, named after its `trace_id` (`DSGAI-TRACE-<slug>.json`). The authoritative definition is `schema.json`; the summary below is orientation.

Every entry carries:

- **`trace_id`, `title`, `description`** - what flows, and what makes it security-relevant
- **`category`** - one of the six above
- **`disposition`** - `benign`, `adversarial`, or `unintentional_failure`
- **`dsgai_mapping`** - DSGAI entries this trace illustrates, primary risk first
- **`provenance`** - where the trace came from, and what backs it (see below)
- **`sanitization`** - a hard attestation plus the techniques applied
- **`spans`** - the trace itself: an ordered sequence of events
- **`security_observations`** - what the trace demonstrates, one falsifiable claim per item

Optional: `agent` (framework, protocol, topology, autonomy), `owasp_llm_top10_mapping`, `mitre_atlas_mapping`, `mitigations`, `contributor`, `tags`, `notes`.

### Spans

A span is one event. The shape is OpenTelemetry-compatible without requiring an OTel pipeline to produce it, so a trace can be exported from a real system or written by hand and still validate the same way.

```json
{
  "span_id": "s7",
  "parent_span_id": "s6",
  "t_offset_ms": 176400910,
  "actor": "tool",
  "actor_id": "tool://server-b/lookup_record",
  "operation": "tool.result",
  "summary": "Tool returns the full record, three fields wider than the schema the agent bound to.",
  "payload": { "contact_email": "<synthetic:email>", "internal_notes": "<shape:string,len=1840>" },
  "data_classes": ["tool_output", "pii"],
  "sensitivity": "high",
  "finding": {
    "dsgai_id": "DSGAI01",
    "note": "Entitlement was enforced once, against a schema that has since changed.",
    "severity": "High"
  }
}
```

Two conventions carry most of the weight:

**Payloads are shapes, not content.** String values in `payload` should be typed placeholders - `<synthetic:email>`, `<redacted:bearer-token>`, `<shape:string,len=1840>`. Literal content belongs in a trace only where the literal *is* the published artifact, such as a prompt-injection string from a paper. This is not only a privacy rule: it is what makes traces from real systems shareable at all, because the finding almost always lives in the shape.

**Findings hang off spans.** Attaching a risk to the span where it materializes lets a reader see exactly where a flow stops being safe, instead of inferring it from prose. `validate.py` requires every span-level `finding.dsgai_id` to appear in the trace's top-level `dsgai_mapping`.

Prefer `t_offset_ms` over wall-clock timestamps. Relative offsets carry the ordering that matters without inventing precision or disclosing when a system was running. Use `timestamp` only where the absolute date is part of the finding.

### Provenance tiers

Most people who hold real agent traces cannot publish them, because production telemetry contains everything that must not be published. A dataset that accepts only production telemetry stays empty; a dataset that accepts anything fills with plausible fiction. The `provenance.tier` field is how this dataset takes both contributions without confusing them:

| Tier | Meaning |
|---|---|
| `observed_production` | Sanitized telemetry from a real deployed system |
| `observed_lab` | Sandbox, test environment, CTF, or red-team exercise |
| `derived_from_public_observation` | The mechanism is rendered as a trace, and its precondition is a documented public fact carried in `evidence` |
| `hypothetical` | Illustrative only, no empirical backing |

Every tier except `hypothetical` requires at least one `provenance.evidence` item, enforced by `validate.py`. Each evidence item states what it supports, narrowly - a DOI, advisory, CVE, or vendor changelog establishing that the trace's precondition happens in the world. Statistics computed over this dataset should be reported per tier, never pooled across them.

Choose the tier honestly. `derived_from_public_observation` is not a lesser contribution; it is the tier that lets a measured phenomenon be studied as a data flow without anyone publishing their logs.

### MITRE ATLAS mappings

`mitre_atlas_mapping` is release-pinned by construction: an entry records the ATLAS release it was verified against and the name each identifier carried in that release. ATLAS identifiers and their names have both moved between releases, so an unpinned pair silently rots. Omit the property rather than guess.

## Sanitization Requirements

All traces **must** be sanitized before submission:

- No real API keys, tokens, credentials, or secrets — replace with placeholder values (e.g. `<redacted:bearer-token>`)
- No real PII, PHI, or proprietary data — use synthetic equivalents
- No internal hostnames, IP addresses, or infrastructure details
- Generalize organization-specific tool names if they could identify the source

Traces from test environments, sandboxes, or CTF exercises are ideal. Production traces must be thoroughly sanitized.

Two things back this up rather than leaving it to good intentions. `sanitization.attestation` must be a literal `true`, so an entry cannot merge with the box quietly unticked. And `validate.py` scans every string in the entry, independently of that attestation: payloads, summaries, notes, evidence locators. Placeholders are exempt; real-looking values fail the run. The scan is deliberately wider than the payloads, because prose written while looking at a real trace is where a real hostname actually gets typed.

Naming a third party as the subject of a security failure is a disclosure act, not a dataset contribution. Generalize the counterparty unless you have gone through disclosure and are prepared to say so in `notes`.

## Contributing

1. Copy `example.json` and edit it, or export spans from your own system into the same shape
2. Save as `entries/<trace_id>.json`
3. Run `python validate.py` - it must print OK
4. Run `python build_index.py` to refresh `index.csv`
5. Open a pull request describing what the trace demonstrates and which DSGAI entries it maps to

See the [main datasets README](../README.md) for general contribution guidelines, and `#team-genai-data-security-initiative` on the [OWASP Slack workspace](https://owasp.slack.com) for anything that needs a conversation first.
