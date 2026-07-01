from pathlib import Path

# Directories
PROJECT_ROOT = Path(__file__).parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

RAW_FILE = RAW_DIR / "moviesTMBD.csv"

# Target column
TARGET = "vote_count"

# Split ratios
TRAIN_SIZE = 0.7
VALID_SIZE = 0.15
TEST_SIZE = 0.15

RANDOM_STATE = 42