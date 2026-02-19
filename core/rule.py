"""Base rule class for cold mailing rules."""

from enum import Enum
from .context import Context
from .condition import Condition, ConditionResult

class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"

class RuleResult:
    def __init__(self, passed: bool, rule_name: str, reasons: list[str]):
        self.passed = passed
        self.rule_name=rule_name
        self.reasons=reasons

class Rule:
    """Base class for all rules."""
    
    def __init__(self, name: str, conditions: list[Condition], op: LogicalOperator = LogicalOperator.AND):
        self.name = name
        self.conditions = conditions
        self.op = op
    def evaluate(self, context: Context) -> RuleResult:
        if not self.conditions: 
            return RuleResult(False, self.name, ["Rule has no conditions."])   

        condition_results=[]
        for condition in self.conditions:
            res=condition.evaluate(context)
            condition_results.append(res)
        
        reasons = [r.reason for r in condition_results]

        if self.op == LogicalOperator.AND:
            passed = all(r.passed for r in condition_results)
        elif self.op == LogicalOperator.OR:
            passed = any(r.passed for r in condition_results)
        else:
            passed = False
            reasons.append(f"Unsupported logical operator: {self.op}")


        return RuleResult (
            passed=passed,
            rule_name=self.name,
            reasons=reasons
        )
         

