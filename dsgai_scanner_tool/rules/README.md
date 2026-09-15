# DSGAI scanner rules

`dsgai-rules.yaml` is the **source of truth** for every detection pattern. It is
validated by `rules.schema.json` and compiled to `dsgai-rules.json` (which the
deterministic CLI loads with the standard library only — no PyYAML at runtime).

- **Edit** `dsgai-rules.yaml`, then rebuild the JSON:
  `python build/build_rules_json.py`
- **Never edit** `dsgai-rules.json` by hand — it is generated. CI checks it is
  in sync (`python build/build_rules_json.py --check`).

## Rule schema

```yaml
- id: P02.1                      # P<control>.<n>, unique
  control: DSGAI02               # DSGAI01 .. DSGAI21
  name: hardcoded-openai-api-key # kebab-case slug
  classification: value_bearing  # structural | value_bearing
  signal: fail                   # fail | warn | pass_signal | count | info
  confidence: high               # high | medium | low
  pcre: '(?i)(OPENAI_API_KEY|...)\s*[:=]\s*["'']?sk-[A-Za-z0-9_\-]{20,}'
  multiline: false               # optional: allow matches to inspect across lines
  file_globs: ['*.py', '*.env*'] # which files the rule runs against
  exclude_globs: []              # paths excluded from this rule
  framework: dsgai-2026-v1.0     # framework version binding
  description: 'Hardcoded OpenAI API key assignment'
```

### Field reference

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | `P<NN>.<n>`, matches the control number |
| `control` | yes | `DSGAI01`–`DSGAI21` |
| `name` | yes | kebab-case identifier |
| `classification` | yes | `structural` (match may be shown) or `value_bearing` (match content is a secret/PII — never shown; located in `--replace ''` mode) |
| `signal` | yes | how a hit is weighted: `fail`, `warn`, `pass_signal`, `count`, `info` |
| `confidence` | yes | `high` / `medium` / `low` — feeds SARIF `level` and report rendering |
| `pcre` | yes | PCRE2 pattern; must compile under `rg --pcre2` (checked in CI, not by the schema) |
| `multiline` | no | run ripgrep with `--multiline`, allowing a PCRE such as `(?s)…` to inspect across line boundaries |
| `file_globs` | yes | globs the rule scans |
| `exclude_globs` | no | globs excluded from the rule (e.g. migrations/tests) |
| `framework` | yes | `dsgai-YYYY-vX.Y` binding |
| `description` | yes | human-readable summary |
| `remediation` | no | fix guidance |
| `references` | no | CVE IDs / links |
| `subtract` | no | rule IDs whose match on the same line cancels this hit (e.g. `torch.load(` minus `weights_only=True`) |
| `requires_nearby` | no | compound proximity logic: `{rule\|rules\|pattern, lines\|scope, absent}` — `pattern` is a raw corroborating regex (e.g. P12.1 requires an LLM call within 30 lines) |
| `gated_on` | no | only evaluated when the stack is detected: `multimodal`, `synthetic_data`, `labeling` |
| `notes` | no | control-level prose that isn't yet fully formalized |

## Classification: STRUCTURAL vs VALUE-BEARING

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md#structural-vs-value-bearing). In
short: if a rule can match a line whose *content is* a secret or PII, it is
`value_bearing` and runs in location-only mode so the value never leaves
ripgrep. All rules under DSGAI02/13/14/15 are value-bearing.

## Provenance

The initial ruleset was extracted verbatim from `dsgai_scanner_tool.md` Step 2 by
`build/generate_rules.py` (a one-time bootstrap, kept for audit). Pattern *fixes*
land as reviewable diffs against this baseline starting in PR-11.
