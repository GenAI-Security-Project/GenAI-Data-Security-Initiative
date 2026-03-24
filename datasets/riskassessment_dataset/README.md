# Risk Assessment Dataset

Mapped risk assessments for various LLM and GenAI deployment scenarios.

## Scope

Structured risk assessments documenting how specific GenAI architectures and deployment patterns expose organizations to data security risks. Assessments map real-world deployment configurations to the DSGAI risk taxonomy and applicable framework controls.

## Data Format

<!-- TODO: Define schema once initial data is contributed -->

Contributions should include where possible:

- **Deployment scenario** — Description of the GenAI architecture being assessed (e.g., customer-facing RAG chatbot, internal code assistant, multi-agent workflow)
- **Components assessed** — LLM provider, vector store, plugins/tools, agent framework, observability stack
- **DSGAI risks identified** — Which DSGAI entries (DSGAI01–DSGAI21) apply to this deployment
- **Risk rating** — Per-risk severity (Critical / High / Medium / Low)
- **Existing controls** — What mitigations are in place
- **Control gaps** — What mitigations are missing
- **Framework alignment** — Which framework controls (NIST CSF, NIST AI RMF, ISO 42001, etc.) are satisfied or missing
- **Industry / sector** — If applicable and non-identifying

## Contributing

Assessments should be anonymized — remove organization names, proprietary system names, and any information that could identify a specific deployment. Add entries as individual JSON, CSV, or Markdown files and submit a pull request. See the [main datasets README](../README.md) for general contribution guidelines.
