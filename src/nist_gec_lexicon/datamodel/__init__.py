from pathlib import Path
from .nist_gec_lexicon import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "nist_gec_lexicon.yaml"
