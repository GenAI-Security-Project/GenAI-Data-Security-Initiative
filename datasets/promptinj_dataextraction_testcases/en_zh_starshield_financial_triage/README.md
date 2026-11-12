# English & Mandarin Financial-Triage Indirect Prompt-Injection Test Cases (`StarShield-Bench`)

Twelve defensive test cases (`TC-0456` to `TC-0467`) covering **English (`en`)** and **Simplified Chinese (`zh-Hans`)** indirect prompt-injection, tool/plugin data leakage, cross-session bleed, NL-to-SQL predicate broadening, multimodal PNG metadata/watermark overrides, credential harvesting, and obfuscated system-prompt extraction inside untrusted payment-dispute and B2B invoice-portal workflows.

All Simplified Chinese (`zh-Hans`) cases include an English translation in `prompt_en_gloss`. Every identifier in the prompts uses official ISO-13616 / ISO-7812 textbook test vectors (`GB82WEST12345698765432`, `NO9386011117947`, `00-00-00` / `00000000`, `6200000000000005`), RFC 2606 `.example` domains, and bracketed credential placeholders (`<API_KEY>`, `[BEARER_TOKEN]`). Zero real incident data or personal information is included.

Contributed by Ziqi Xiao (`@Ziqi`). Original synthetic contribution designed for defensive security validation; no undisclosed vendor vulnerabilities are referenced.

## Source and attribution

| Field | Value |
|---|---|
| Source | StarShield Forensics & `StarShield-Bench` (`Ziqi Xiao`) |
| Identifier | https://github.com/Ziqi/starshield-forensics (Concept DOI: [`10.5281/zenodo.24145804`](https://doi.org/10.5281/zenodo.24145804)) |
| License | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (`CC-BY-4.0`) |

## Coverage summary (`TC-0456` – `TC-0467`)

| IDs | Category | DSGAI | Languages | Attack Surface Modeled |
|---|---|---|---|---|
| `TC-0456`–`TC-0457` | `direct_extraction` | `DSGAI01` | `en`, `zh-Hans` | HTML-comment & bilingual authority overrides in chat exports suppressing IOCs and exfiltrating RAG compliance thresholds |
| `TC-0458`–`TC-0459` | `tool_plugin_leakage` | `DSGAI06` | `en`, `zh-Hans` | Invoice/portal notes hijacking connected ERP & wire-transfer lookup plugins |
| `TC-0460`–`TC-0461` | `cross_context_bleed` | `DSGAI11` | `en`, `zh-Hans` | Spoofed QA batch macros probing shared analyst session buffers for prior claimants' data |
| `TC-0462`–`TC-0463` | `nl_query_injection` | `DSGAI12` | `en`, `zh-Hans` | Remittance memo smuggling coercing LLM-to-SQL reconciliation assistants to drop tenant filters |
| `TC-0464`–`TC-0465` | `multimodal_extraction` | `DSGAI09` | `en`, `zh-Hans` | PNG `iTXt` chunk & low-opacity watermark instructions hijacking VLM receipt triage |
| `TC-0466` | `credential_harvesting` | `DSGAI02` | `en` | Webhook troubleshooting pretext soliciting agent `<API_KEY>` / `[BEARER_TOKEN]` headers |
| `TC-0467` | `system_prompt_extraction` | `DSGAI15` | `zh-Hans` | Bilingual JSON transcoding + underscore delimiter obfuscation bypassing output filters |
