"""Base rule class for cold mailing rules."""

from enum import Enum
from .context import Context
from .condition import Condition
from .action import Action
from dataclasses import dataclass


class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"


@dataclass
class RuleResult:
    passed: bool
    rule_name: str
    reasons: list[str]


class Rule:
    """Base class for all rules."""

    def __init__(
        self,
        name: str,
        conditions: list[Condition],
        actions: list[Action],
        op: LogicalOperator = LogicalOperator.AND,
    ):
        self.name = name
        self.conditions = conditions
        self.op = op
        self.actions = actions

    def evaluate(self, context: Context) -> RuleResult:
        if not self.conditions:
            return RuleResult(False, self.name, ["Rule has no conditions."])

        condition_results = []
        for condition in self.conditions:
            res = condition.evaluate(context)
            condition_results.append(res)

        reasons = [r.reason for r in condition_results]

        if self.op == LogicalOperator.AND:
            passed = all(r.passed for r in condition_results)
        elif self.op == LogicalOperator.OR:
            passed = any(r.passed for r in condition_results)
        else:
            passed = False
            reasons.append(f"Unsupported logical operator: {self.op}")

        return RuleResult(passed=passed, rule_name=self.name, reasons=reasons)
