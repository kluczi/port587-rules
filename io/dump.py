"""Dump rules and results to files."""

import json
from pathlib import Path


def dump_results(results: dict, output_path: str):
    """Dump evaluation results to JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
