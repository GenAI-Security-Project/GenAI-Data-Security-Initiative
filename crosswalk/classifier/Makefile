.PHONY: install index splits eval eval-biencoder eval-reranker contamination classify export clean

PYTHON ?= python

install:
	pip install -r requirements.txt

index:
	$(PYTHON) -m classifier.index_builder

splits:
	$(PYTHON) -m classifier.split_maker

# Full evaluation pipeline — reproduces all metrics from frozen splits
eval: index splits eval-biencoder eval-reranker contamination
	@echo ""
	@echo "========================================"
	@echo "  All evaluations complete."
	@echo "  Reports: classifier/splits/eval_report_*.json"
	@echo "  Contamination: classifier/splits/contamination_probe_*.json"
	@echo "========================================"

eval-biencoder:
	$(PYTHON) -m classifier.eval_harness --verbose

eval-reranker:
	$(PYTHON) -m classifier.eval_harness --rerank --verbose

contamination:
	$(PYTHON) -m classifier.contamination_probe
	$(PYTHON) -m classifier.contamination_probe --rerank

classify:
	$(PYTHON) -m classifier.classify $(ARGS)

export:
	$(PYTHON) -m classifier.export_predictions --rerank --top-k 15

clean:
	rm -rf index/ splits/*.json __pycache__ *.pyc
