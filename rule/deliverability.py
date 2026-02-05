"""Email deliverability rules."""

from ..core.rule import Rule


class DeliverabilityRule(Rule):
    """Rule for checking email deliverability."""
    
    def evaluate(self, context):
        """Check deliverability factors."""
        domain = context.get("domain", "")
        return domain and len(domain) > 0
