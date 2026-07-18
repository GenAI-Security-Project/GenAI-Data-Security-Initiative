# Prompt Injection & Data Extraction Test Cases

A curated set of adversarial prompts and extraction techniques for red-teaming and regression testing of GenAI data security controls.

**Status:** Accepting contributions — this dataset is maintained with the community.

## Scope

Test cases designed to evaluate whether GenAI systems adequately protect against data extraction through prompt manipulation. Each test case targets a specific DSGAI risk and can be used for red-teaming, automated security testing, or regression testing after control changes.

Categories include:

- **Direct extraction** — Prompts designed to elicit sensitive data from model weights or RAG retrieval (DSGAI01)
- **Cross-context bleed** — Techniques to access data from other users or sessions (DSGAI11)
- **System prompt extraction** — Attempts to retrieve system instructions and configuration (DSGAI15)
- **Tool/plugin data leakage** — Prompts that exploit tool integrations to access unauthorized data (DSGAI06)
- **Natural-language query injection** — Inputs that generate unsafe SQL/GraphQL through LLM-to-database gateways (DSGAI12)
- **Multimodal extraction** — Techniques using images, audio, or documents to bypass text-only controls (DSGAI09)
- **Credential harvesting** — Prompts targeting agent credentials or API keys (DSGAI02)

## Data Format

The canonical JSON contract is
[`data_validation/schemas/promptinj_testcase.schema.json`](../../data_validation/schemas/promptinj_testcase.schema.json).
Contributions may add documented metadata for provenance, integrity, language,
or contrastive controls while retaining the required base fields.

Each test case should include:

- **Test case ID**
- **Category** — From the list above or a new category with justification
- **DSGAI mapping** — Primary DSGAI entry targeted
- **Prompt / input** — The adversarial input (text, structured payload, or multimodal description)
- **Expected behavior (secure)** — What a properly secured system should do
- **Expected behavior (vulnerable)** — What an unprotected system would return
- **Prerequisites** — Required access level, system configuration, or setup
- **Severity if bypassed** — Critical / High / Medium / Low
- **Source** — Research paper, tool, or original contribution
- **Notes** — Any caveats, model-specific behavior, or known limitations

## Current suites

| Contribution | Cases | Format |
|---|---:|---|
| [`tr_altayduel_testcases.json`](tr_altayduel_testcases.json) | 5 | Aggregate Turkish test-case document |
| [`tr_altaysec_turkish_llm_injection/`](tr_altaysec_turkish_llm_injection/) | 300 | Standalone Turkish cases with manifest and source lineage |
| [`tr_turkish_conversation_prompt_injection_pairs/`](tr_turkish_conversation_prompt_injection_pairs/) | 150 | Standalone Turkish attack cases with matched benign controls |

## Important

These test cases are for **defensive testing only**. All prompts should be sourced from published research, existing red-teaming frameworks, or original contributions designed for security validation. Do not submit test cases that rely on undisclosed vulnerabilities in specific vendor products.

## Contributing

Add test cases as individual JSON or YAML files and submit a pull request. See the [main datasets README](../README.md) for general contribution guidelines.
