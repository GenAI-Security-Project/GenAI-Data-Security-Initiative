# AltaySec Turkish LLM Prompt-Injection Test Cases

This contribution packages 300 Turkish-first defensive test cases for prompt-injection and data-extraction regression testing. Each case is a standalone JSON document that conforms to the repository's `promptinj_testcase.schema.json` contract.

The corpus is an adaptation of the public [AltaySec Turkish LLM Prompt Injection Dataset v0.2](https://huggingface.co/datasets/AltaySec/turkish-llm-injection). It is not a record of observed attacks, model responses, or exploit success rates.

## Layout

- `cases/TC-0001.json` through `cases/TC-0300.json`: one test case per file.
- `manifest.csv`: deterministic source-to-output mapping, language and review metadata, lineage tier, and integrity hashes.

Every case preserves the public source record ID and its original 16-character prompt hash, and adds a full SHA-256 for the adapted prompt.

## Source and attribution

| Field | Value |
|---|---|
| Source dataset | AltaySec Turkish LLM Prompt Injection Dataset v0.2 |
| Source creator | Fevzi Ege Yurtsevenler / AltaySec |
| Source repository | `AltaySec/turkish-llm-injection` |
| Source revision | `08d1fdccf10a831c2f32627c615002e6286f6315` |
| Source file | `data/train.jsonl` |
| Source file SHA-256 | `7655b67c958b4dde1d77026c392f3ffad39d59d39109afb3c48b78a60590ab9f` |
| Source license | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Source copyright | Copyright (c) 2026 Fevzi Ege Yurtsevenler / AltaySec |
| Adapted by | Enes Deniz / AltaySec |
| Adaptation license | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |

The original source material remains licensed under CC BY 4.0. Enes Deniz / AltaySec licenses the new annotations, DSGAI mappings, anonymization changes, and collection arrangement in this contribution under CC BY-SA 4.0. This does not replace the source license or imply endorsement.

## Adaptation contract

The source snapshot was transformed deterministically in source-ID order:

1. Verify the pinned source-file SHA-256 and all 300 source prompt hashes.
2. Preserve the adversarial text's Unicode representation; normalization is used only for duplicate matching.
3. Replace named organizations, products, public or name-shaped people, and identifier-shaped values with typed synthetic placeholders.
4. Replace demonstration network locations with names under the IANA-reserved `.example` namespace.
5. Map the intended protected asset and attack path to the canonical DSGAI taxonomy.
6. Add explicit secure behavior, vulnerable behavior, and sandbox prerequisites.
7. Correct language metadata after content-level review while retaining the original source label in provenance.
8. Re-score `severity` using the target impact rubric while retaining `source_severity`.
9. Recompute the adapted prompt SHA-256 and write one case per file plus a matching manifest row.

Typed placeholders retain the security-testing intent without carrying named entities or realistic identifier values. Examples include `[SENTETIK_KAMU_KURUMU]`, `[SENTETIK_TC_KIMLIK_NO]`, `[SENTETIK_API_ANAHTARI]`, and `[SENTETIK_PLAKA]`.

## Coverage

### Target categories

| Category | Cases | Primary DSGAI mapping |
|---|---:|---|
| System prompt extraction | 106 | DSGAI15 |
| Direct extraction | 82 | DSGAI01 |
| Credential harvesting | 65 | DSGAI02 |
| Other prompt-injection controls | 39 | DSGAI05 |
| Cross-context bleed | 1 | DSGAI11 |
| Tool/plugin leakage | 7 | DSGAI06 |

Some cases add a secondary mapping for the protected data or attack path: sensitive-data leakage (DSGAI01), indirect tool exchange (DSGAI06), multimodal/OCR handling (DSGAI09), synthetic-data pitfalls (DSGAI10), or integrity manipulation (DSGAI21).

### Review and scope signals

| Signal | Cases | Meaning |
|---|---:|---|
| `scope=data_extraction` | 227 | Contains an explicit protected target and an extraction or confirmation action. |
| `scope=prompt_injection_control` | 73 | Retained as a control-oriented injection test; downstream extraction benchmarks should review or exclude it. |
| `source_failure_mode_review=manual_review` | 54 | Source failure mode was broad or control-oriented; mapping received explicit content-level review. |
| `source_lineage=public_generator` | 120 | Corresponds to the source's publicly reproducible v0.1 generator batch. |
| `source_lineage=pinned_snapshot_only` | 180 | Reproducible at artifact, row-ID, and hash level; no generator-level claim is made. |

All 300 records are retained. The scope and review fields prevent generic injection controls or source-label uncertainty from being presented as confirmed extraction evidence.

### Language and severity

- Primary language: 297 Turkish, 3 English.
- Content-level language tags: Turkish 298, English 29, plus one case each containing Arabic, Azerbaijani, Kurmanji (`kmr`), Kyrgyz, and Russian.
- Three encoded system-prompt payloads declare `encoded_payload_language=tr`; `TC-0100` keeps English as its visible primary language and also records the decoded Turkish payload.
- Target impact severity: 40 Critical, 187 High, 73 Medium.
- Source severity is preserved separately in each record and in `manifest.csv`.

Severity is a conservative test-impact label, not a CVSS score. Prompt-injection-only review cases are capped at Medium; cross-context bleed is Critical; protected data or credential extraction is High or Critical; system-prompt and tool-mediated extraction is High.

## Safety and anonymization

- All fixtures and prerequisites require non-production systems and synthetic data only.
- 162 cases received at least one typed replacement in the prompt or retained descriptive metadata.
- Named organizations, products, public or name-shaped people, realistic TCKN/IBAN/phone/plate forms, credential candidates, and internal-ID candidates were removed from the adapted fields.
- `KVKK` is intentionally retained only as the public name of Türkiye's data-protection law/regime; it is not treated as an organization, person, or private identifier.
- No production credentials, real personal records, vendor-specific undisclosed vulnerabilities, or model performance claims are included.
- Web-location fixtures use IANA-reserved `.example` names and require no third-party network target.
- Encoded and mixed-script payloads are intentionally retained where they are the behavior under test.

## Validation evidence

Release QA performed on 2026-07-16:

| Check | Result |
|---|---:|
| Draft-07 JSON Schema validation | 300 / 300 pass |
| Unique test-case IDs | 300 / 300 |
| Unique source IDs and source hashes | 300 / 300 |
| Source row-hash verification | 300 / 300 |
| Adapted SHA-256 verification | 300 / 300 |
| Manifest-to-file integrity | 300 / 300 |
| Canonical DSGAI/category validation | 300 / 300 |
| Non-allowlisted denylisted named entities and direct PII/live-secret patterns | 0 findings |
| Non-reserved network domains in adapted prompts | 0 findings |
| Normalized exact duplicates | 0 |
| Lexical near-duplicate pairs at similarity `>= 0.86` | 0 |

The lexical duplicate check uses Unicode NFKC, case folding, whitespace normalization, and pairwise similarity. Semantic embedding deduplication was not performed and is not claimed.

The repository's current `run_all_checks.py` entry point reports that its validators are not yet implemented. For that reason, schema, integrity, provenance, mapping, anonymization, and duplicate checks were executed independently rather than treating the stub's zero exit status as validation evidence.

## Intended use

Use these cases for sandboxed red-team exercises, prompt-injection detector evaluation, and regression tests for instruction hierarchy, sensitive-data access control, context isolation, and tool/RAG boundaries. Do not run them against production systems or data stores.
