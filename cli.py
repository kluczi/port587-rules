"""CLI entry point for rules engine."""

import sys
from core.engine import Engine


def main():
    """Main CLI function."""
    engine = Engine()
    print("Cold mailing rules engine")
    print(f"Loaded {len(engine.rules)} rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
