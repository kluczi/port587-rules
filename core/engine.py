"""Rules engine for evaluating multiple rules."""

from .rule import Rule, RuleResult
from .context import Context


class EngineResult:
    def __init__(self, results: list[str], passed_rules: list[str], failed_rules: list[str], passed_count: int, failed_count: int, actions:list[str]):
        self.results=results
        self.passed_rules=passed_rules
        self.failed_rules=failed_rules



class Engine:
    """Engine for evaluating rules."""
    
    def __init__(self, rules:list[Rule]):
        self.rules = rules

    def run(self, context: Context) -> EngineResult:
        results=[]
        for rule in self.rules:
            results.append(rule.evaluate(context))

        passed_rules=[result.rule_name for result in results if result.passed]
        failed_rules=[result.rule_name for result in results if not result.passed]
        passed_count=len(passed_rules)
        failed_count=len(failed_rules)
        
        return EngineResult (
            results=results,
            passed_rules=passed_rules,
            failed_rules=failed_rules,
            passed_count=passed_count,
            failed_count=failed_count
        )
