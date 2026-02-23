from dataclasses import dataclass
from typing import Any
from enum import Enum
import operator
from .context import Context


class ComparisonOperator(Enum):
    GREATER_THAN = ">"
    LESS_THAN = "<"
    EQUAL = "=="
    GREATER_EQUAL = ">="
    LESS_EQUAL = "<="


OPERATOR_FUNCTIONS = {
    ComparisonOperator.GREATER_THAN: operator.gt,
    ComparisonOperator.LESS_THAN: operator.lt,
    ComparisonOperator.EQUAL: operator.eq,
    ComparisonOperator.GREATER_EQUAL: operator.ge,
    ComparisonOperator.LESS_EQUAL: operator.le,
}

OPERATOR_PHRASES = {
    ComparisonOperator.GREATER_THAN: "exceeded",
    ComparisonOperator.LESS_THAN: "fell below",
    ComparisonOperator.EQUAL: "matched",
    ComparisonOperator.GREATER_EQUAL: "met or exceeded",
    ComparisonOperator.LESS_EQUAL: "met or fell below",
}


@dataclass
class ConditionResult:
    passed: bool
    reason: str


class Condition:
    def __init__(self, field: str, op: ComparisonOperator, expected: Any):
        self.field = field
        self.op = op
        self.expected = expected

    def evaluate(self, context: Context) -> ConditionResult:
        actual = context.get(self.field)

        if actual is None:
            return ConditionResult(
                passed=False,
                reason=f"Missing metric '{self.field}' in campaign context",
            )

        compare = OPERATOR_FUNCTIONS.get(self.op)

        if compare is None:
            return ConditionResult(
                passed=False, reason=f"Unsupported operator '{self.op}'"
            )

        try:
            passed = compare(actual, self.expected)
        except TypeError:
            return ConditionResult(
                passed=False,
                reason=(
                    f"Cannot compare metric '{self.field}' (value={actual})"
                    f" with expected={self.expected}"
                ),
            )

        phrase = OPERATOR_PHRASES.get(self.op, "compared against")

        if passed:
            reason = f"Metric '{self.field}' {phrase} threshold {self.expected} (actual={actual})"
        else:
            reason = f"Metric '{self.field}' did not {phrase} threshold {self.expected} (actual={actual})"

        return ConditionResult(passed=passed, reason=reason)
