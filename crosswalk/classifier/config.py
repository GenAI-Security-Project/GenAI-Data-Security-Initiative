"""Configuration constants for the classifier pipeline."""

from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parent.parent
CLASSIFIER_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
FRAMEWORKS_DIR = DATA_DIR / "frameworks"
ENTRIES_DIR = DATA_DIR / "entries"
BACKLINKS_PATH = DATA_DIR / "backlinks.json"
INDEX_DIR = CLASSIFIER_DIR / "index"
SPLITS_DIR = CLASSIFIER_DIR / "splits"

# Models
BIENCODER_MODEL = "BAAI/bge-small-en-v1.5"
CROSSENCODER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

# Retrieval
DEFAULT_TOP_K = 10
EMBEDDING_DIM = 384

# Splits
SPLIT_SEED = 42
CALIBRATION_SIZE = 150
CONTAMINATION_CLEAN_FRAMEWORK = "CoSAI"

# Eval
BOOTSTRAP_SEED = 42
BOOTSTRAP_N = 10_000
K_VALUES = [1, 3, 5, 10, 20]
