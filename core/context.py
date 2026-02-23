"""Context for rule evaluation."""

from typing import Any, Dict


class Context:
    """Context passed to rules during evaluation."""

    def __init__(self, data: Dict[str, Any] = None):
        self.data = data or {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get value from context."""
        return self.data.get(key, default)
