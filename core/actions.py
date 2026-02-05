"""Actions that can be triggered by rules."""

from typing import Callable, Dict, Any


class Action:
    """Base action class."""
    
    def execute(self, context: Dict[str, Any]):
        """Execute the action."""
        raise NotImplementedError


class LogAction(Action):
    """Action that logs a message."""
    
    def __init__(self, message: str):
        self.message = message
    
    def execute(self, context):
        print(f"[LOG] {self.message}")
