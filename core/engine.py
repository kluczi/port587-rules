"""Rules engine for evaluating multiple rules."""

from typing import List
from .rule import Rule
from .context import Context


class Engine:
    """Engine for evaluating rules."""
    
    def __init__(self):
        self.rules: List[Rule] = []
    
    def add_rule(self, rule: Rule):
        """Add a rule to the engine."""
        self.rules.append(rule)
