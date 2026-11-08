import json
from pathlib import Path

import yaml


def parse(filepath):
    extension = Path(filepath).suffix.lower()
    if extension == '.json':
        with open(filepath) as file:
            return json.load(file)
    if extension in ('.yml', '.yaml'):
        with open(filepath) as file:
            return yaml.safe_load(file)
    raise ValueError(f'Unsupported file format: {filepath}')
