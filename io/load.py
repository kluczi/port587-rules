"""Load rules from configuration."""

import json
from pathlib import Path


def load_rules(config_path: str) -> dict:
    """Load rules configuration from JSON file."""
    path = Path(config_path)
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)
