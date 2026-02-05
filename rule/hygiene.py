"""Email hygiene rules."""

from ..core.rule import Rule


class HygieneRule(Rule):
    """Rule for email hygiene checks."""
    
    def evaluate(self, context):
        """Check email hygiene."""
        email = context.get("email", "")
        return "@" in email and "." in email.split("@")[1]
