"""Lead quality scoring rules."""

from ..core.rule import Rule


class LeadQualityRule(Rule):
    """Rule for evaluating lead quality."""
    
    def evaluate(self, context):
        """Check lead quality score."""
        score = context.get("quality_score", 0)
        return score >= 50
