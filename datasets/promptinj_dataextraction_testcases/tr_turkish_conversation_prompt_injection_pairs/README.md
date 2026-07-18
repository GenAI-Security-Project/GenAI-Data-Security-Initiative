# Turkish Contrastive Prompt-Injection Test Cases

This contribution adds 149 Turkish-first defensive test cases for
prompt-injection, data-extraction, and agent-boundary regression testing. Every
adversarial input is retained with a vocabulary- and context-matched benign
control. The pairing lets an evaluator test both sides of the boundary:

- reject or contain the attack input; and
- avoid blocking the paired request merely because it contains similar
  security-adjacent language.

The package contains test definitions, not model outputs, exploit-success
claims, production logs, or a certification benchmark.

## Layout

- `cases/TC-0301.json` through `cases/TC-0450.json`: 149 schema-conformant test
  cases, with the documented source-quality exclusion `TC-0440` omitted.
- `manifest.csv`: deterministic source-to-output mapping and integrity hashes.
- `build_cases.py`: reproducible transformation from the pinned source release.
- `contrastive_testcase.schema.json`: strict contract for the additional
  contrastive, provenance, language, and integrity metadata.
- `validate.py`: base and extension schema, provenance, manifest, safety, and
  duplicate checks.

Each case keeps the attack as the repository-standard `prompt` field and the
matched safe request under `contrastive_control`. Consumers that only support
the base schema can ignore the additional control metadata. Pair-aware
evaluators can report attack containment and benign-control handling together.

## Source and attribution

| Field | Value |
|---|---|
| Source dataset | Turkish Conversation Prompt-Injection Dataset |
| Source repository | [`3nesdeniz/turkish-conversation-prompt-injection`](https://github.com/3nesdeniz/turkish-conversation-prompt-injection) |
| Published distribution | [Hugging Face](https://huggingface.co/datasets/3nesdeniz/turkish-conversation-prompt-injection) |
| Release | v1.0.2 |
| Attribution | Enes Deniz, Copyright © 2026 |
| Affiliation | AltaySec |
| DOI | [`10.5281/zenodo.21379389`](https://doi.org/10.5281/zenodo.21379389) |
| Source revision | `9a2163b051237e3c15f842a3ef517cd029b1ccd4` |
| Source license | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

The source attack and benign-control text remain under CC BY 4.0. The new
DSGAI mappings, test expectations, sandbox prerequisites, metadata, scripts,
and collection arrangement are contributed under this repository's CC BY-SA
4.0 license. The transformation preserves source text exactly and identifies
all changes in each record's provenance metadata.

Pinned source-file hashes:

| File | SHA-256 |
|---|---|
| `data/train.jsonl` | `16b007c20581c1be16dac53d96d501a6451c92aa8f3ea9f2e976d543ff3e59fd` |
| `data/validation.jsonl` | `3bd3533f078041bd308fbc5066ac7df1a3161e7a5a1881d4701c78ed7950c80f` |
| `data/test.jsonl` | `b21520130e80a3c28786f32a69b6d2f40740c5899ad6500a6a603931eb1327b4` |

## Adaptation contract

The build performs the following deterministic steps in source-pair order:

1. Verify the source checkout's `v1.0.2` tag and `HEAD` against the pinned
   repository commit, then verify all three source-file hashes.
2. Require exactly one attack and one benign-boundary row for each of the 150
   pair IDs, with both rows in the same source split.
3. Exclude source pair `pair_0140` because its reversed payload does not decode
   to a coherent instruction; do not silently repair licensed source text.
4. Preserve all contributed source texts character-for-character as decoded Unicode
   strings.
5. Apply content-reviewed repository categories and DSGAI mappings.
6. Add explicit secure and vulnerable behavior, synthetic-only sandbox
   prerequisites, scenario-impact severity, and scope metadata.
7. Write one JSON case per included pair and a manifest containing source and output
   SHA-256 values.

Category assignment is explicit rather than keyword-only. This prevents, for
example, an instruction to *ignore* a system message from being mislabeled as
an attempt to *extract* that message.

## Coverage

Nine source attack families contribute 15 cases; obfuscation and code-switching
contributes 14 after the documented malformed-payload exclusion:

| Attack family | Cases |
|---|---:|
| Direct instruction override | 15 |
| System prompt extraction | 15 |
| Roleplay jailbreak | 15 |
| Authority-claim bypass | 15 |
| Sensitive-data exfiltration | 15 |
| Tool-action abuse | 15 |
| Indirect content injection | 15 |
| RAG-context poisoning | 15 |
| Memory-context poisoning | 15 |
| Obfuscation and code-switching | 14 |

Repository categories after content review:

| Category | Cases |
|---|---:|
| Direct extraction | 35 |
| Tool/plugin leakage | 3 |
| System prompt extraction | 22 |
| Credential harvesting | 21 |
| Cross-context bleed | 3 |
| Multimodal extraction | 1 |
| Other prompt-injection controls | 64 |

- 85 cases have `scope=data_extraction`.
- 64 cases have `scope=prompt_injection_control` and should not be represented
  as confirmed extraction attempts.
- Source split lineage is preserved: 100 train, 20 validation, and 29 test
  pairs. The contribution is a security regression suite; these source split
  labels are provenance, not a new train/test recommendation.
- Primary attack-language review yields 147 `tr` and 2 `en` cases; both
  English-primary attacks retain Turkish matched controls and explicit
  `languages=["en", "tr"]` metadata.

Primary and secondary mappings cover DSGAI01, DSGAI02, DSGAI04, DSGAI05,
DSGAI06, DSGAI09, DSGAI11, DSGAI13, DSGAI15, and DSGAI17. Mappings describe the
tested failure mode and do not claim an observed vulnerability in a named
model or product.

## Safety and data handling

- All prompts, controls, protected records, credentials, tools, and systems are
  synthetic or mocked.
- Source rows contain no production conversations, customer data, or scraped
  personal information.
- Test prerequisites prohibit production systems and third-party targets.
- No real-looking e-mail address, IPv4 address, Turkish IBAN, telephone number,
  TCKN-like value, live-secret pattern, or named vendor appears in the paired
  prompt text.
- Critical and High labels describe hypothetical sandbox impact if a control
  is bypassed; they are not CVSS scores or measured model outcomes.

## Validation evidence

Release QA performed on 2026-07-18:

| Check | Result |
|---|---:|
| Canonical and extension Draft-07 JSON Schema validation | 149 / 149 pass |
| Unique source-aligned test-case IDs (one documented gap) | 149 / 149 |
| Test-case ID collisions with existing repository data | 0 |
| Source attack/control pair integrity | 149 / 149 |
| Pinned source file and row-text verification | 149 / 149 |
| Manifest-to-file and SHA-256 integrity | 149 / 149 |
| Canonical DSGAI mapping validation | 149 / 149 |
| Normalized exact attack/control collisions | 0 |
| Normalized exact attack or control overlap with existing repository prompts | 0 |
| Sensitive-data, live-secret, and named-vendor pattern findings | 0 |
| Maximum internal attack similarity | `0.600` |
| Maximum internal control similarity | `0.658` |
| Maximum unpaired attack/control similarity | `0.538` |
| Maximum paired attack/control similarity (reported, not failed) | `0.980` |
| Maximum attack similarity to an existing repository prompt | `0.619` |
| Maximum control similarity to an existing repository prompt | `0.481` |

Lexical near-duplicate validation uses Unicode NFKC normalization, case
folding, punctuation and whitespace normalization, and a `0.92` failure
threshold. The intentionally matched pair is reported but excluded from this
failure rule; unrelated attack/control combinations are not. This is a
deterministic lexical check, not a semantic-embedding claim.

The repository's current `data_validation/run_all_checks.py` entry point still
reports that its validators are not wired together. This contribution therefore
uses its own executable validator instead of presenting the stub's zero exit
status as validation evidence.

## Rebuild and validate

Use a checkout of the source dataset at tag `v1.0.2`:

```bash
python3 build_cases.py --source /path/to/turkish-conversation-prompt-injection
python3 validate.py --source /path/to/turkish-conversation-prompt-injection
```

`validate.py` requires `jsonschema`, which is already declared in
`data_validation/requirements.txt`. Omitting `--source` runs all contribution
checks except byte-for-byte comparison with the external source checkout.

## Intended use and limitations

Use the cases in isolated red-team exercises, detector regression suites, RAG
and agent trust-boundary tests, and false-positive analysis. A strong result
requires both safe handling of the attack and appropriate handling of its
benign control.

The corpus is synthetic, Turkish-first, and intentionally balanced by attack
family. It does not estimate real-world prevalence, establish production
security, measure multilingual generalization, or replace authorization and
tool-level enforcement.
