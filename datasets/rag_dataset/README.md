# RAG Poisoning & Retrieval Integrity Dataset

Benign and adversarial document sets for testing vector store integrity controls, retrieval-time redaction, and poisoning detection pipelines.

**Status:** Accepting contributions — this dataset is being built from scratch with the community.

## Scope

Test data designed to evaluate the resilience of Retrieval-Augmented Generation (RAG) systems against data poisoning, unauthorized retrieval, and integrity failures. Aligned primarily with DSGAI04 (Data, Model & Artifact Poisoning), DSGAI05 (Data Integrity & Validation Failures), and DSGAI13 (Vector Store Platform Data Security).

Categories include:

- **Poisoned documents** — Documents containing adversarial content designed to manipulate model behavior when retrieved (e.g., injected instructions, biased content, misleading facts)
- **Integrity test sets** — Baseline "golden" document sets with known-good content for drift and tampering detection
- **Redaction test documents** — Documents containing embedded PII, PHI, credentials, or classified content for testing retrieval-time redaction and filtering controls
- **Cross-tenant retrieval probes** — Query sets designed to test tenant isolation in multi-tenant vector stores (DSGAI11)
- **Embedding inversion test data** — Document-embedding pairs for evaluating reconstruction and inference attack resistance (DSGAI18)

## Data Format

Each entry is one JSON file in [`entries/`](entries/), named after its `document_id` (e.g. `entries/RAG-0002.json`), that validates against [`data_validation/schemas/rag.schema.json`](../../data_validation/schemas/rag.schema.json). Start the file with `"$schema": "../../../data_validation/schemas/rag.schema.json"` and see [`entries/RAG-0001.json`](entries/RAG-0001.json) for a complete example. Check your entry with:

```bash
cd datasets/rag_dataset
python validate.py
```

Contributions should include:

- **Document ID**
- **Category** — From the list above
- **DSGAI mapping** — Primary DSGAI entry targeted
- **Content** — The document text, or a description if synthetic generation is required
- **Adversarial payload** — For poisoned documents, what the injected content is and what it is designed to trigger
- **Expected retrieval behavior (secure)** — What a properly secured RAG system should do
- **Expected retrieval behavior (vulnerable)** — What an unprotected system would return
- **Metadata** — Any metadata fields relevant to the test (e.g., tenant ID, classification label, access control tags)

## Important

All documents in this dataset must be **synthetic or publicly sourced**. Do not submit real PII, PHI, credentials, or proprietary data — use realistic synthetic equivalents. Poisoned documents should be clearly labeled and must not contain content that could cause harm if accidentally ingested into a production system.

## Contributing

Add each document or test case as its own JSON file in `entries/` and submit a pull request. See the [main datasets README](../README.md) for general contribution guidelines.
