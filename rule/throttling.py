"""Throttling rules for rate limiting."""

from ..core.rule import Rule


class ThrottlingRule(Rule):
    """Rule for throttling email sends."""
    
    def __init__(self, max_per_hour: int = 10):
        super().__init__("throttling")
        self.max_per_hour = max_per_hour
    
    def evaluate(self, context):
        """Check if throttling limit is respected."""
        sent_count = context.get("sent_count", 0)
        return sent_count < self.max_per_hour
