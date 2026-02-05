"""Base rule class for cold mailing rules."""

from typing import Any, Dict


class Rule:
    """Base class for all rules."""
    
    def __init__(self, name: str):
        self.name = name
    
    def evaluate(self, context: Dict[str, Any]) -> bool:
        """Evaluate rule against context."""
        raise NotImplementedError
