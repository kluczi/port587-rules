"""Rules engine for evaluating multiple rules."""

from .rule import Rule, RuleResult
from .context import Context
from .action import Action
from dataclasses import dataclass


@dataclass
class EngineResult:
    results: list[RuleResult]
    passed_rules: list[str]
    failed_rules: list[str]
    passed_count: int
    failed_count: int
    actions: list[Action]


class Engine:
    """Engine for evaluating rules."""

    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def run(self, context: Context) -> EngineResult:
        actions_to_execute = []
        results = []
        for rule in self.rules:
            result = rule.evaluate(context)
            results.append(result)
            if result.passed:
                actions_to_execute.extend(rule.actions)

        passed_rules = [result.rule_name for result in results if result.passed]
        failed_rules = [result.rule_name for result in results if not result.passed]
        passed_count = len(passed_rules)
        failed_count = len(failed_rules)

        return EngineResult(
            results=results,
            passed_rules=passed_rules,
            failed_rules=failed_rules,
            passed_count=passed_count,
            failed_count=failed_count,
            actions=actions_to_execute,
        )
