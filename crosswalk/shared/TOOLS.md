<!--
  OWASP GenAI Crosswalk — Shared Resources
  File        : TOOLS.md — Open-Source Security Tools for GenAI Systems
  Version     : 2026-Q1
  Maintained by: OWASP GenAI Data Security Initiative — https://genai.owasp.org
  License     : CC BY-SA 4.0
-->

# Open-Source Security Tools for GenAI Systems

> **57+ tools** across 13 categories — covering adversarial testing, prompt injection detection, data validation, agent security, observability, guardrails, OT/ICS, and more.

A curated, practitioner-oriented catalogue of open-source and freely available tools for securing LLM applications, agentic AI systems, and GenAI data pipelines. Every tool listed here is referenced in one or more [crosswalk mapping files](../README.md) in this repository.

Each entry includes: what it does, which OWASP entries it addresses, and a direct link. Contributions welcome via PR — see [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## Quick reference

| Category | Tools | Primary risks addressed |
|----------|-------|------------------------|
| [Adversarial Testing & Red Teaming](#adversarial-testing-and-red-teaming) | 12 | LLM01, ASI01, LLM08 |
| [Prompt Injection Detection](#prompt-injection-detection) | 4 | LLM01, LLM07, ASI01 |
| [Output Scanning & Redaction](#output-scanning-and-redaction) | 4 | LLM02, DSGAI01, DSGAI09 |
| [Data Validation & Ingestion](#data-validation-and-ingestion-security) | 6 | LLM04, DSGAI05, DSGAI17 |
| [Vector Store Security](#vector-store-security) | 3 | LLM08, DSGAI04 |
| [Supply Chain & SBOM](#supply-chain-and-sbom) | 4 | LLM05, ASI04, DSGAI06 |
| [Agent Identity & Credentials](#agent-identity-and-credentials) | 4 | ASI02, ASI03, DSGAI02 |
| [Observability & Monitoring](#observability-and-monitoring) | 10 | DSGAI01, ASI07, LLM09 |
| [Rate Limiting & API Security](#rate-limiting-and-api-security) | 2 | LLM10, LLM04 |
| [Guardrails & Policy Enforcement](#guardrails-and-policy-enforcement) | 4 | LLM01, LLM06, ASI01 |
| [OT & ICS Security](#ot-and-ics-security-tools) | 2 | ISA/IEC 62443, SP 800-82 |
| [Evaluation & Benchmarking](#evaluation-and-benchmarking) | 4 | LLM09, DSGAI05 |
| [MCP-Specific Tools](#mcp-specific-tools) | 2 | ASI02, ASI07 |

---

## Adversarial Testing and Red Teaming

Tools for testing LLM and agentic systems against known attack
patterns before production deployment.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| Garak | LLM vulnerability scanner — probes for prompt injection, jailbreaks, data extraction, hallucination, and dozens of other failure modes across 100+ detectors | LLM01, LLM02, LLM09, ASI01 | https://github.com/leondz/garak |
| PyRIT | Microsoft Python Risk Identification Toolkit — adversarial probing framework for LLM applications with orchestrators for multi-turn attack simulation | LLM01, LLM06, ASI01, ASI02 | https://github.com/Azure/PyRIT |
| Promptfoo | LLM testing framework — runs automated test suites against LLM responses, supports red team scenarios and regression testing | LLM01, LLM09, ASI01 | https://github.com/promptfoo/promptfoo |
| Invariant Analyzer | Agentic system security analyser — detects policy violations in agent traces, validates tool call sequences, identifies unsafe action chains | ASI01, ASI02, ASI10 | https://github.com/invariantlabs-ai/invariant |
| Inspect AI | UK AI Safety Institute evaluation framework — structured LLM evals with solvers, scorers, and dataset support for reproducible safety testing | LLM01, LLM09, ASI01 | https://github.com/UKGovernmentBEIS/inspect_ai |
| TextAttack | Adversarial NLP attack library — 16+ attack recipes for text classification, NLI, and sequence-to-sequence models; includes augmentation and training modules | LLM01, LLM08 | https://github.com/QData/TextAttack |
| Counterfit | Microsoft adversarial ML attack framework — automated attacks against AI models including evasion, inversion, and extraction | LLM01, LLM08, ASI01 | https://github.com/Azure/counterfit |
| Foolbox | Python adversarial attack library — gradient-based, decision-based, and score-based attacks for neural networks; most-cited adversarial ML library | LLM08, LLM03 | https://github.com/bethgelab/foolbox |
| Mindgard | AI security testing platform — automated adversarial testing, model vulnerability scanning, and continuous security monitoring for production AI | LLM01, ASI01, LLM08 | https://github.com/Mindgard/cli |
| Agentic Security | Open-source scanner for agentic AI systems — tests for goal hijacking, tool abuse, lateral movement, and cascade failures in multi-agent deployments | ASI01, ASI02, ASI07, ASI08 | https://github.com/msoedov/agentic_security |
| OpenAI Evals | OpenAI evaluation framework — build and run custom eval suites for LLMs with structured datasets, completion functions, and metric reporting | LLM01, LLM09, LLM06 | https://github.com/openai/evals |
| PurpleLlama CyberSecEval | Meta benchmark suite for LLM cybersecurity evaluation — covers insecure code generation, prompt injection, and cyberattack assistance detection | LLM01, LLM05, LLM07 | https://github.com/meta-llama/PurpleLlama |

---

## Prompt Injection Detection

Runtime detection of prompt injection attempts in user inputs and
retrieved content before they reach the model.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| LLM Guard | Production-grade input and output scanning library — detects prompt injection, toxic content, PII leakage, secrets, and insecure output patterns in real time | LLM01, LLM02, LLM07 | https://github.com/protectai/llm-guard |
| Rebuff | Self-hardening prompt injection detector — two-layer defence combining heuristics and a dedicated LLM-based classifier | LLM01, ASI01 | https://github.com/protectai/rebuff |
| Vigil | LLM prompt injection detection library — scans inputs for injection patterns using vector similarity, YARA rules, and canary token detection | LLM01, LLM07 | https://github.com/deadbits/vigil-llm |
| LangKit | WhyLabs LLM monitoring toolkit — includes prompt injection and jailbreak detection, toxicity scoring, and semantic drift detection | LLM01, LLM09 | https://github.com/whylabs/langkit |

---

## Output Scanning and Redaction

Tools for detecting and removing sensitive content from LLM responses
before they reach users or downstream systems.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| Microsoft Presidio | PII detection and anonymisation framework — supports 20+ entity types, multiple languages, extensible with custom recognisers, integrates with RAG pipelines | LLM02, DSGAI01, DSGAI09 | https://github.com/microsoft/presidio |
| spaCy | Industrial-strength NLP — used as the base NER engine for many PII detection pipelines, supports custom entity recognition | LLM02, DSGAI01 | https://github.com/explosion/spaCy |
| detect-secrets | Yelp secrets scanner — detects API keys, tokens, and credentials in text, integrates as a pre-commit hook and CI gate | LLM02, DSGAI02, ASI03 | https://github.com/Yelp/detect-secrets |
| Trufflehog | Secrets scanning for git repos, filesystems, and S3 — useful for scanning agent memory stores and LLM application codebases for leaked credentials | DSGAI02, ASI03 | https://github.com/trufflesecurity/trufflehog |

---

## Data Validation and Ingestion Security

Tools for validating, profiling, and securing data before it enters
RAG pipelines, training datasets, or embedding stores.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| Great Expectations | Data quality and validation framework — define expectations on dataset structure, statistical properties, and content; validate at ingestion with full reporting | LLM04, DSGAI05, DSGAI21 | https://greatexpectations.io |
| Pandera | DataFrame validation library — schema validation, statistical tests, and custom checks for pandas and polars DataFrames in training pipelines | LLM04, DSGAI05 | https://pandera.readthedocs.io |
| CleanLab | Data-centric AI toolbox — detects label errors, outliers, and data quality issues in training datasets, including AI-generated annotation quality assessment | LLM04, DSGAI05 | https://github.com/cleanlab/cleanlab |
| OWASP ZAP | Web application security scanner — DAST for LLM API endpoints, tests for injection vulnerabilities in interfaces consuming LLM output | LLM05, DSGAI12 | https://www.zaproxy.org |
| WhyLogs | Data profiling and drift detection for ML pipelines — statistical profiling, data quality constraints, and monitoring with WhyLabs integration | DSGAI05, DSGAI17, LLM03 | https://github.com/whylabs/whylogs |
| Evidently | ML model and data monitoring — data drift detection, model performance tracking, bias analysis, and automated reporting | DSGAI17, LLM09, DSGAI05 | https://github.com/evidentlyai/evidently |
| Semgrep | Static analysis for code security — rules for detecting insecure LLM output handling patterns in application code | LLM05, DSGAI12 | https://semgrep.dev |

---

## Vector Store Security

Tools for securing, monitoring, and testing the vector databases that
underpin RAG systems and agentic memory.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| Weaviate | Open-source vector database — built-in RBAC, multi-tenancy, authentication, encrypted storage, and audit logging; the most security-mature open-source vector store | LLM08, DSGAI13, ASI06 | https://weaviate.io |
| Qdrant | High-performance vector database — collection-level API key authentication, payload filtering, and access control; patch CVE-2024-3584 before production deployment | LLM08, DSGAI13 | https://qdrant.tech |
| Chroma | Lightweight embedding store — suitable for development; requires additional hardening before production use | LLM08, DSGAI13 | https://www.trychroma.com |
| Pinecone Canopy | Open-source RAG framework — includes context engine, query engine, and chat engine with namespace-based isolation | DSGAI11, DSGAI13 | https://github.com/pinecone-io/canopy |
| ML Privacy Meter | Measures privacy risks of ML models — membership inference attacks, attribute inference, and reconstruction attack simulation | DSGAI18, LLM02 | https://github.com/privacytrustlab/ml_privacy_meter |

---

## Supply Chain and SBOM

Tools for managing the software supply chain of LLM components.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| CycloneDX | Software Bill of Materials standard and toolchain — ML-BOM supports model components, training datasets, and AI-specific metadata; 20+ language plugins | LLM03, DSGAI04, ASI04 | https://cyclonedx.org |
| ModelScan | Scanning tool for ML model files — detects malicious code embedded in serialised model formats before loading | LLM03, DSGAI04, ASI04 | https://github.com/protectai/modelscan |
| OWASP Dependency-Check | Identifies known vulnerable components in project dependencies — integrates with CI/CD pipelines to gate on CVE findings | LLM03, ASI04 | https://owasp.org/www-project-dependency-check/ |
| Syft | SBOM generation tool by Anchore — generates SBOMs in CycloneDX and SPDX formats from container images and filesystems | LLM03, ASI04 | https://github.com/anchore/syft |
| MLflow | ML lifecycle management — experiment tracking, model registry, model serving, and artifact versioning for end-to-end ML pipeline governance | LLM05, DSGAI05, DSGAI06 | https://github.com/mlflow/mlflow |
| Grype | Vulnerability scanner that pairs with Syft — scans SBOMs for known CVEs in LLM dependencies and inference runtime packages | LLM03, ASI04 | https://github.com/anchore/grype |

---

## Agent Identity and Credentials

Tools for managing Non-Human Identities — agent service accounts,
API keys, OAuth tokens, and short-lived credentials.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| HashiCorp Vault | Secrets management platform — dynamic secret generation, short-lived credential issuance, automatic rotation, audit logging | ASI03, DSGAI02 | https://www.vaultproject.io |
| SPIFFE and SPIRE | Workload identity framework — issues cryptographic identity documents to workloads, enabling mutual TLS for A2A communication without long-lived secrets | ASI03, ASI07 | https://spiffe.io |
| Teleport | Identity-aware infrastructure access — zero-trust access for agents, full session recording, short-lived certificates | ASI03, ASI07 | https://goteleport.com |
| cert-manager | Kubernetes certificate manager — automates TLS certificate issuance and rotation for agent-to-agent communication | ASI07 | https://cert-manager.io |

---

## Observability and Monitoring

Tools for tracing, logging, and monitoring LLM and agentic system
behaviour in production.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| Langfuse | Open-source LLM observability platform — traces, spans, scores, and session-level analytics with self-hosting option; supports PII masking before storage | DSGAI14, ASI10 | https://langfuse.com |
| Helicone | LLM observability and gateway — request/response logging, cost tracking, user analytics; open-source self-hosted version available | DSGAI14, LLM10 | https://www.helicone.ai |
| OpenTelemetry | Vendor-neutral observability framework — standard for traces, metrics, and logs across LLM infrastructure | DSGAI14, LLM10, ASI08 | https://opentelemetry.io |
| TruLens | LLM application evaluation and monitoring — RAG triad evaluation, hallucination detection, feedback functions | LLM09, DSGAI21 | https://github.com/truera/trulens |
| Arize Phoenix | Open-source LLM observability — tracing, evaluation, embedding visualization, and retrieval quality analysis for LLM applications | LLM09, ASI06, DSGAI01 | https://github.com/Arize-AI/phoenix |
| AgentOps | Agent observability platform — session replay, cost tracking, error analysis, and compliance monitoring for autonomous AI agents | ASI01, ASI07, ASI08, ASI10 | https://github.com/AgentOps-AI/agentops |
| LangSmith | LangChain tracing and evaluation platform — production monitoring, dataset management, and automated testing for LLM applications (free tier available) | LLM01, LLM06, ASI01 | https://smith.langchain.com |
| Weave | Weights & Biases LLM evaluation and tracing framework — track experiments, evaluate outputs, and monitor production LLM applications | LLM09, LLM01, ASI01 | https://github.com/wandb/weave |
| OpenLLMetry | OpenTelemetry instrumentation for LLMs — vendor-neutral observability with automatic tracing for OpenAI, Anthropic, Cohere, and 20+ providers | DSGAI01, DSGAI14, ASI07 | https://github.com/traceloop/openllmetry |
| Deepchecks | ML testing and monitoring — data integrity checks, model performance monitoring, RAG evaluation, and drift detection | DSGAI05, DSGAI21 | https://deepchecks.com |

---

## Rate Limiting and API Security

Tools for protecting LLM API endpoints against resource exhaustion
and denial-of-service attacks.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| LiteLLM | LLM API gateway and proxy — unified interface for 100+ LLMs with built-in rate limiting, cost tracking, per-user budgets, and request/response logging | LLM10, ASI08 | https://github.com/BerriAI/litellm |
| Kong Gateway | API gateway — rate limiting, authentication, request transformation, and plugin ecosystem | LLM10, DSGAI17 | https://github.com/Kong/kong |
| Traefik | Cloud-native reverse proxy and load balancer — rate limiting, circuit breakers, middleware for LLM API traffic management | LLM10, ASI08 | https://traefik.io |

---

## Guardrails and Policy Enforcement

Tools for enforcing safe behaviour boundaries on LLM and agentic
systems at runtime — independent of model instruction.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| Guardrails AI | Open-source framework for adding guardrails to LLM applications — validators for output structure, content policy, PII detection, SQL injection prevention | LLM06, ASI01, ASI02 | https://github.com/guardrails-ai/guardrails |
| NeMo Guardrails | NVIDIA programmable guardrails toolkit — Colang-based policy language for defining topical, safety, and action guardrails | LLM06, ASI01, ASI02 | https://github.com/NVIDIA/NeMo-Guardrails |
| LlamaIndex | Data framework for LLM applications — RAG pipeline primitives with metadata filtering, access control integration, and context assembly controls | LLM02, DSGAI01, DSGAI15 | https://www.llamaindex.ai |
| LangChain | LLM application framework — includes prompt management, chain composition, and tool integration | LLM06, ASI02 | https://github.com/langchain-ai/langchain |

---

## OT and ICS Security Tools

Tools for monitoring, detecting, and responding to threats in
operational technology environments where AI is being deployed.

| Tool | Description | OT risks addressed | Link |
|---|---|---|---|
| Velociraptor | Digital forensics and incident response platform — endpoint visibility and hunting capability for OT Windows hosts running LLM applications | LLM01, LLM04, ASI10 | https://github.com/Velocidex/velociraptor |
| OpenSearch | Open-source search and analytics — SIEM capability for correlating OT security events, LLM audit logs, and agent behaviour anomalies | LLM10, ASI08, ASI10 | https://opensearch.org |
| Wazuh | Open-source security platform — SIEM, XDR, and compliance management; integrates with OT environments for file integrity monitoring and log analysis | LLM01, ASI10 | https://wazuh.com |
| MITRE Caldera for OT | Adversary emulation framework with ICS/OT plugins — test detection capabilities against MITRE ATT&CK for ICS techniques | LLM01, LLM04, ASI01 | https://github.com/mitre/caldera |
| GNS3 | Network simulation platform — model OT network zones and test LLM deployment architectures before production rollout | All OT entries | https://www.gns3.com |

---

## Evaluation and Benchmarking

Tools for measuring LLM and agentic system quality, safety, and
accuracy before and after deployment.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| RAGAS | RAG evaluation framework — measures faithfulness, answer relevance, context precision, and context recall | LLM09, DSGAI21 | https://github.com/explodinggradients/ragas |
| DeepEval | LLM evaluation framework — 14+ evaluation metrics including hallucination, bias, toxicity, answer relevance, and custom metrics | LLM09, DSGAI21 | https://github.com/confident-ai/deepeval |
| EleutherAI LM Eval Harness | Standardised evaluation framework — runs models against 200+ academic benchmarks; detect unexpected capability changes post fine-tuning | LLM04, DSGAI04 | https://github.com/EleutherAI/lm-evaluation-harness |
| IBM Adversarial Robustness Toolbox | ML adversarial robustness library — poisoning attacks, evasion attacks, membership inference, model extraction, and defences | LLM04, DSGAI04, DSGAI18 | https://github.com/Trusted-AI/adversarial-robustness-toolbox |

---

## MCP-Specific Tools

Tools for developing, testing, and securing Model Context Protocol
server deployments.

| Tool | Description | Risks addressed | Link |
|---|---|---|---|
| MCP Inspector | Official MCP debugging and testing tool — inspect tool schemas, test tool calls, validate descriptor integrity | ASI02, ASI04, DSGAI06 | https://github.com/modelcontextprotocol/inspector |
| MCP Python SDK | Official Python SDK for MCP servers — use as the base for building secure MCP servers with typed schemas and validation | ASI02, ASI04 | https://github.com/modelcontextprotocol/python-sdk |
| MCP TypeScript SDK | Official TypeScript SDK — same as Python SDK for Node.js deployments | ASI02, ASI04 | https://github.com/modelcontextprotocol/typescript-sdk |

---

## Tool selection guidance

### For a new RAG deployment

Start with Weaviate (vector store with RBAC) + Microsoft Presidio
(output redaction) + Great Expectations (ingestion validation) +
Langfuse (observability) + Garak (pre-deployment adversarial testing).

### For an agentic deployment

Start with HashiCorp Vault (credential management) + Guardrails AI
(action policy enforcement) + Invariant Analyzer (agent trace analysis) +
LiteLLM (rate limiting) + Langfuse (observability).

### For OT/ICS environments

Start with Wazuh (SIEM) + Velociraptor (endpoint forensics) +
HashiCorp Vault (agent credentials) + OpenTelemetry (observability) +
Garak (adversarial testing before OT deployment).

### For supply chain assurance

Start with CycloneDX (ML SBOM generation) + ModelScan (model file
scanning) + Grype (CVE scanning) + detect-secrets (credential leakage
in codebases).

---

## Contributing a tool

To add a tool to this file, open a PR with the following information:

- Tool name
- One-sentence description of what it does and why it matters for GenAI security
- Risk IDs addressed (LLMxx, ASIxx, or DSGAIxx)
- URL

Requirements for inclusion: open-source or freely available, actively
maintained (last commit within 12 months), directly relevant to at
least one OWASP source list entry in this repo, not a duplicate.

---

## References

- OWASP LLM Top 10 2025: https://genai.owasp.org/llm-top-10/
- OWASP Agentic Top 10 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP GenAI Data Security Risks 2026: https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/
- OWASP NHI Top 10: https://owasp.org/www-project-non-human-identities-top-10/

---

Maintained by the OWASP GenAI Data Security Initiative.
Part of the OWASP GenAI Crosswalk: https://github.com/GenAI-Security-Project/GenAI-Data-Security-Initiative/tree/main/crosswalk
