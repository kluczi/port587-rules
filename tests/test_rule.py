import pytest
from core.context import Context
from core.condition import Condition, ComparisonOperator
from core.rule import Rule, LogicalOperator
from core.action import Action, ActionType


def test_rule_and_operator_pass():
    context = Context({"reply_rate": 0.5, "open_rate": 0.8})
    cond1 = Condition("reply_rate", ComparisonOperator.GREATER_THAN, 0.4)
    cond2 = Condition("open_rate", ComparisonOperator.GREATER_THAN, 0.7)
    rule = Rule("test_rule", [cond1, cond2], [], LogicalOperator.AND)

    result = rule.evaluate(context)

    assert result.passed is True
    assert result.rule_name == "test_rule"


def test_rule_and_operator_fail():
    context = Context({"reply_rate": 0.3, "open_rate": 0.8})
    cond1 = Condition("reply_rate", ComparisonOperator.GREATER_THAN, 0.4)
    cond2 = Condition("open_rate", ComparisonOperator.GREATER_THAN, 0.7)
    rule = Rule("test_rule", [cond1, cond2], [], LogicalOperator.AND)

    result = rule.evaluate(context)

    assert result.passed is False


def test_rule_or_operator_pass():
    context = Context({"reply_rate": 0.5, "open_rate": 0.1})
    cond1 = Condition("reply_rate", ComparisonOperator.GREATER_THAN, 0.4)
    cond2 = Condition("open_rate", ComparisonOperator.GREATER_THAN, 0.7)
    rule = Rule("test_rule", [cond1, cond2], [], LogicalOperator.OR)

    result = rule.evaluate(context)

    assert result.passed is True


def test_rule_no_conditions():
    rule = Rule("empty_rule", [], [])
    result = rule.evaluate(Context({}))

    assert result.passed is False
    assert "Rule has no conditions." in result.reasons
