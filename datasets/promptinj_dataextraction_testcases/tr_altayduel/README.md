# Turkish Prompt-Injection and Data-Extraction Test Cases (AltayDuel)

Five Turkish-language test cases, `TC-0451` to `TC-0455`. They exercise morphological and cross-lingual bypass surfaces that English-only test sets miss: verbatim-repeat leaks, spoofed system tags, translate-then-execute smuggling, Cyrillic homoglyphs, and cross-session probes. Each case carries an English gloss of its prompt (`prompt_en_gloss`).

Contributed by Fevzi Ege Yurtsevenler in #8. Original contribution designed for defensive security validation; no undisclosed vendor vulnerabilities are referenced.

## Source and attribution

| Field | Value |
|---|---|
| Source | AltayDuel, Turkish agent-vs-agent prompt-injection arena (AltaySec / AltayDuel) |
| Identifier | https://huggingface.co/datasets/AltaySec/altayduel-transcripts |
| License | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

## Changes from the original contribution

The cases were first contributed as one aggregate file, `tr_altayduel_testcases.json`, with its own field names. They were split into one file per case so each validates against [`promptinj_testcase.schema.json`](../../../data_validation/schemas/promptinj_testcase.schema.json):

- `id` (`TR-ALTAYDUEL-001` to `-005`) became `testcase_id` `TC-0451` to `TC-0455`; the original ID is kept in `source_id`.
- `category` moved to the schema's values: `system_prompt_extraction`, `direct_extraction`, `cross_context_bleed`.
- `dsgai_mapping` became a one-item list.
- `expected_behavior_secure`, `expected_behavior_vulnerable` and `severity_if_bypassed` were renamed `expected_secure`, `expected_vulnerable` and `severity`.

Prompts, glosses, expected behaviors, prerequisites, severities, sources and notes are unchanged.
