# Agent Data Flow & Tool Exchange Traces

Sanitized traces of agentic AI tool calls, plugin data exchanges, and delegation chains for security research.

**Status:** Accepting contributions — this dataset is being built from scratch with the community.

## Scope

Structured traces capturing how data flows through agentic AI systems — between agents, tools, plugins, APIs, and memory stores. This dataset supports research into DSGAI06 (Tool, Plugin & Agent Data Exchange Risks), DSGAI02 (Agent Identity & Credential Exposure), DSGAI15 (Over-Broad Context Windows & Prompt Over-Sharing), and related agent security patterns.

Categories include:

- **Tool call traces** — Sequences of tool invocations showing what data is sent to and received from external tools (APIs, databases, file systems, code execution environments)
- **Multi-agent delegation chains** — Traces showing how tasks and data are passed between agents, including what context is forwarded, filtered, or accumulated
- **Plugin data exchange logs** — Records of data shared with third-party plugins, including request/response payloads and metadata
- **Credential and permission flows** — How credentials, tokens, and permissions are scoped, delegated, and consumed across agent workflows
- **Context accumulation patterns** — Traces showing how agent context windows grow over multi-step tasks, what data persists across steps, and where over-sharing occurs
- **Memory read/write traces** — How agents interact with short-term and long-term memory stores, including what data is persisted and retrieved

## Data Format

Each trace is one JSON file validating against
[data_validation/schemas/agentdataflow_trace.schema.json](../../data_validation/schemas/agentdataflow_trace.schema.json).

Required fields:

| field | type | meaning |
|---|---|---|
| `trace_id` | string matching `TRACE-NNNN` | the trace's identifier, unique in this dataset |
| `category` | one of `tool_call`, `multi_agent_delegation`, `plugin_data_exchange`, `credential_flow`, `context_accumulation`, `memory_read_write` | which of the categories above the trace illustrates |
| `dsgai_mapping` | array of `DSGAI01` through `DSGAI21`, at least one | the DSGAI entries the trace is evidence for |
| `trace_data` | array of objects, at least one | the ordered sequence of events |
| `type` | `benign` or `adversarial` | whether the trace shows a normal workflow or a security failure |

Optional fields: `agent_framework`, `sensitivity_annotations`, `security_observations`.

### The shape of a step

The schema constrains `trace_data` to an array of objects and does not constrain the objects.
The convention proposed here, and used by the example in this directory, is:

| key | meaning |
|---|---|
| `step` | integer, 1-based, the position in the sequence |
| `actor` | who performed the step: an agent identifier, a tool name, or `user` |
| `action` | what was done, in the vocabulary of the framework that produced the trace |
| `data_out` | what left the actor at this step, sanitized |
| `data_in` | what came back, sanitized |
| `observed_by` | how this step was recorded: `agent_self_report` where the agent's own transcript is the source, or a named external source |

`observed_by` is the field worth arguing about, and the reason it is proposed. Most agent traces are
the agent's own account of what it did. For the benign categories that is fine. For the adversarial
ones it is the crux: a trace that shows an agent over-sharing is evidence only if the record of the
over-sharing did not come from the component that over-shared. Marking the source per step lets a
reader tell a self-reported trace from a captured one without having to ask the contributor.

### Sanitization

Every requirement in the Sanitization Requirements section below applies to `trace_data` in full.
A step's `data_out` and `data_in` carry placeholder values in place of any credential, token, key,
identifier, hostname or personal datum. Where a trace's security point depends on the *shape* of a
secret, use a placeholder of the same shape (`sk-REDACTED-32CHARS`). Never a real one.

### Contributing a trace

Add one JSON file per trace, named for its `trace_id` (`TRACE-0001.json`). Validate it against the
schema before opening the pull request:

```
python -m jsonschema -i datasets/agentdataflow_toolexchange_traces/TRACE-0001.json \
  data_validation/schemas/agentdataflow_trace.schema.json
```

State in the pull-request body which DSGAI entries the trace is evidence for and, for an adversarial
trace, what a defence would have had to observe to catch it.

## Sanitization Requirements

All traces **must** be sanitized before submission:

- No real API keys, tokens, credentials, or secrets — replace with placeholder values (e.g., `sk-REDACTED`, `Bearer EXAMPLE_TOKEN`)
- No real PII, PHI, or proprietary data — use synthetic equivalents
- No internal hostnames, IP addresses, or infrastructure details
- Generalize organization-specific tool names if they could identify the source

Traces from test environments, sandboxes, or CTF exercises are ideal. Production traces must be thoroughly sanitized.

## Contributing

Add traces as individual JSON, JSONL, or YAML files and submit a pull request. See the [main datasets README](../README.md) for general contribution guidelines.
