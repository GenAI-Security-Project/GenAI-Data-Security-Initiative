# Pre-Registration: GenAI Security Crosswalk Classifier

**Pre-registered:** 2026-04-09
**Authors:** Emmanuel Guilherme Junior
**Status:** Pre-registered (no eval code has been executed)

---

## 1. Research Question

Can a retrieval-augmented classifier automatically map OWASP GenAI vulnerability
descriptions to the correct framework controls, with sufficient precision and
recall to be useful as a human-review assistant?

## 2. Hypotheses

**H1 (Retrieval baseline):** A BGE bi-encoder + FAISS retrieval pipeline will
achieve P@10 ≥ 0.30 and R@10 ≥ 0.50 on the holdout set, meaning at least half
of the correct controls appear in the top-10 candidates.

**H2 (Reranker lift):** Adding a cross-encoder reranker on top of bi-encoder
retrieval will improve MAP by ≥ 10 percentage points over bi-encoder alone.

**H3 (LLM pseudo-labeler):** An LLM-as-SME bulk labeler using few-shot examples
from hand-curated mappings will achieve agreement ≥ 0.70 (Cohen's κ) with
human labels on the holdout set.

**H4 (Contamination):** Model performance on the contamination-clean framework
(CoSAI — never seen in any training or few-shot examples) will be no more than
15 percentage points below performance on contaminated frameworks (those used
in few-shot prompts), measured by MAP.

## 3. Data

### 3.1 Source data
- **OWASP entries:** 41 vulnerability entries (LLM01–10, ASI01–10, DSGAI01–21)
  from `data/entries/*.json`
- **Framework controls:** 505 controls across 14 frameworks from
  `data/frameworks/*.json`
- **Hand-curated mappings:** 1,097 control backlinks from `data/backlinks.json`,
  each linking a framework control_id to one or more OWASP entries with tier,
  scope, and notes

### 3.2 Holdout split

**Stratified split by source list × severity:**

| Split | Purpose | Size | Selection |
|---|---|---|---|
| **Calibration** | Few-shot examples, threshold tuning | 150 mappings | Stratified random, SHA-pinned |
| **Test** | Final evaluation, reported metrics | 400 mappings | Remainder after calibration |
| **Contamination-clean** | Generalization probe | All CoSAI mappings | Entire framework held out |

**Split pinning:** The split will be determined by SHA-256 hash of
`entry_id + "::" + framework + "::" + control_id`, sorted, then partitioned.
The split seed and hash will be committed to `classifier/splits/split_meta.json`
before any evaluation runs.

**Leakage CI:** A CI check will verify that no calibration example appears in
the test set, and that no CoSAI control appears in any few-shot prompt or
calibration set.

### 3.3 Framework contamination design

- **Contaminated frameworks:** All frameworks used in few-shot prompts for the
  LLM pseudo-labeler (expected: NIST AI RMF, MITRE ATLAS, EU AI Act, ISO 27001)
- **Clean framework:** CoSAI — held out entirely from all training, few-shot,
  and calibration data
- **Comparison:** MAP on contaminated frameworks vs. MAP on CoSAI, with 95%
  bootstrap CIs

## 4. Models

### 4.1 Bi-encoder (retrieval)
- **Model:** `BAAI/bge-small-en-v1.5` (33M params, 384-dim embeddings)
- **Index:** FAISS IndexFlatIP (inner product, since BGE embeddings are normalized)
- **Query construction:** Concatenation of `entry_id + ": " + entry_name + ". " + mapping_notes`
- **Candidate set:** Top-k controls from FAISS search (k = 10, 20, 50)

### 4.2 Cross-encoder (reranker)
- **Model:** `cross-encoder/ms-marco-MiniLM-L-6-v2` (22M params)
- **Input:** (query, control_text) pairs from bi-encoder top-50
- **Output:** Re-scored top-k (k = 10)

### 4.3 LLM pseudo-labeler
- **Model:** Claude Sonnet (via Anthropic API)
- **Prompt:** System prompt with task description + 5 few-shot examples from
  calibration set + candidate control text → binary relevance judgment +
  confidence score
- **Batch size:** All test set mappings in a single run (no iterative refinement)

## 5. Metrics

All metrics are computed on the **test split only** (never on calibration).

| Metric | Formula | Why |
|---|---|---|
| **P@k** | Precision at k (fraction of top-k that are correct) | Measures noise in suggestions |
| **R@k** | Recall at k (fraction of correct controls found in top-k) | Critical — missing a control is worse than suggesting a wrong one |
| **MAP** | Mean Average Precision across all queries | Single-number summary for ranking quality |
| **R-Precision** | Precision at R (where R = number of relevant controls for that query) | Calibrated to the actual multi-label count per entry |
| **Cohen's κ** | Inter-rater agreement between LLM labels and human labels | For H3 — LLM pseudo-labeler quality |

**Why not just MRR:** The mapping is multi-label (each OWASP entry maps to
multiple controls). MRR only measures the rank of the first correct result,
which is insufficient. MAP and R@k capture multi-label performance.

**Confidence intervals:** 95% bootstrap CIs (10,000 resamples) on all metrics.

## 6. Thresholds for success

| Criterion | Threshold | Action if not met |
|---|---|---|
| R@10 ≥ 0.50 | At least half of correct controls in top-10 | Pipeline not useful as human assistant; do not deploy |
| MAP ≥ 0.25 | Minimum ranking quality | Investigate retrieval failures before proceeding |
| κ ≥ 0.70 | LLM labels substantially agree with human labels | LLM labeler not reliable; use only retrieval |
| Contamination gap ≤ 15pp | Generalization to unseen frameworks | Flag as limitation; do not claim generalization |

## 7. Analysis plan

1. **Baseline:** Report bi-encoder retrieval metrics (P@k, R@k, MAP, R-Precision)
   at k = 1, 3, 5, 10, 20
2. **Reranker:** Report same metrics after cross-encoder reranking
3. **LLM labeler:** Report κ, precision, recall, F1 against human labels
4. **Contamination:** Report MAP on contaminated vs. clean frameworks with CIs
5. **Error analysis:** Manually inspect 20 worst-ranked queries to identify
   failure modes (semantic gap, framework jargon, multi-hop reasoning)
6. **Ablations:** Query construction variants (with/without notes, with/without
   severity)

## 8. Reproducibility

- All code in `classifier/` directory
- `make eval` reproduces all metrics from frozen splits
- Split metadata committed before first eval run
- Model versions pinned in `classifier/requirements.txt`
- Random seeds fixed: split seed = 42, bootstrap seed = 42

## 9. Timeline

| Phase | Deliverable |
|---|---|
| 3a | Scaffolding, FAISS index, classify CLI |
| 3b | Reranker, LLM pseudo-labeler, eval harness |
| 3c | Contamination probe, eval report |

## 10. Limitations (known in advance)

- BGE-small is a general-purpose encoder, not fine-tuned for security/compliance text
- Framework control descriptions vary in granularity (NIST AI RMF subcategories
  vs. EU AI Act full articles)
- Hand-curated mappings may contain errors that propagate to evaluation
- CoSAI is a newer, smaller framework — contamination comparison may be
  underpowered
- The classifier assists human reviewers; it does not replace expert judgment

---

*Pre-registered before any evaluation code was executed. This document was
committed to git with the date above as the authoritative timestamp.*
