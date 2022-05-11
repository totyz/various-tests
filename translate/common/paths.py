import os
from pathlib import Path

ROOT_PATH = (Path(os.path.dirname(__file__)) / '..').resolve()
INPUTS_PATH = ROOT_PATH / 'inputs'
OUTPUTS_PATH = ROOT_PATH / 'outputs'