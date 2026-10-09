Community-contributed datasets supporting research, benchmarking, and practical security testing for GenAI data security. Each subfolder contains a specific dataset aligned with the [DSGAI risk taxonomy](../README.md#key-deliverables).

| Folder | Dataset | Status |
|---|---|---|
| `vulnerability_dataset` | Real-world vulnerabilities affecting LLM applications | Active |
| `exploit_dataset` | Documented exploits and attack techniques targeting LLMs | Active |
| `riskassessment_dataset` | Mapped risk assessments for various LLM deployments | Active |
| `incident_dataset` | Anonymized GenAI data security incidents (DSGAI01–DSGAI21) | Accepting contributions |
| `promptinj_dataextraction_testcases` | Adversarial prompts and extraction techniques for red-teaming | Accepting contributions |
| `rag_dataset` | RAG poisoning and retrieval integrity test sets | Accepting contributions |
| `crossframework_mapping_dataset` | Machine-readable DSGAI-to-framework control mappings | Superseded by the [GenAI Crosswalk](https://github.com/GenAI-Security-Project/crosswalk) |
| `agentdataflow_toolexchange_traces` | Sanitized agentic AI tool call and delegation chain traces | Accepting contributions |

## How to Contribute

1. Fork this repository
2. Add your data to the appropriate dataset folder following the formatting guidelines in that folder's README
3. Submit a pull request with a description of your contribution

For questions or to discuss contributions, join `#team-genai-data-security-initiative` on the [OWASP Slack workspace](https://owasp.slack.com).
