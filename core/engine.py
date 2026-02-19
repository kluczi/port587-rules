"""Rules engine for evaluating multiple rules."""

from typing import List
from .rule import Rule, RuleResult
from .context import Context


class EngineResult:
    def __init__(self, results: list[RuleResult], passed_rules: list[Rules], failed_rules: list[rules]):
        self.results=results
        self.passed_rules=passed_rules
        self.failed_rules=failed_rules



class Engine:
    """Engine for evaluating rules."""
    
    def __init__(self, rules:list[Rule]):
        self.rules = rules

    def run(self, rule: Rule):
        """Add a rule to the engine."""
        self.rules.append(rule)
