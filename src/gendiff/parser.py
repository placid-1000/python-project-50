import json
from pathlib import Path

import yaml


def parse(filepath):
    extension = Path(filepath).suffix.lower()
    with open(filepath) as file:
        if extension in ('.yml', '.yaml'):
            return yaml.safe_load(file)
        return json.load(file)
