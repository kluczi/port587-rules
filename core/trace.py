"""Tracing for rule evaluation."""

from typing import List, Dict, Any


class Trace:
    """Trace of rule evaluations."""
    
    def __init__(self):
        self.events: List[Dict[str, Any]] = []
    
    def add_event(self, rule_name: str, result: bool):
        """Add an evaluation event."""
        self.events.append({
            "rule": rule_name,
            "result": result
        })
