import pytest
from core.context import Context
from core.condition import Condition, ComparisonOperator
from core.rule import Rule
from core.engine import Engine
from core.action import Action, ActionType


def test_engine_executes_actions_for_passed_rules():
    context = Context({"reply_rate": 0.5})
    action = Action(ActionType.PAUSE_CAMPAIGN, {"id": 1}, "test_rule")
    cond = Condition("reply_rate", ComparisonOperator.GREATER_THAN, 0.4)
    rule = Rule("test_rule", [cond], [action])
    engine = Engine([rule])

    result = engine.run(context)

    assert result.passed_count == 1
    assert "test_rule" in result.passed_rules
    assert len(result.actions) == 1
    assert result.actions[0].action_type == ActionType.PAUSE_CAMPAIGN


def test_engine_multiple_rules_mixed_results():
    context = Context({"val": 10})
    rule1 = Rule("pass_rule", [Condition("val", ComparisonOperator.EQUAL, 10)], [])
    rule2 = Rule("fail_rule", [Condition("val", ComparisonOperator.EQUAL, 20)], [])
    engine = Engine([rule1, rule2])

    result = engine.run(context)

    assert result.passed_count == 1
    assert result.failed_count == 1
    assert "pass_rule" in result.passed_rules
    assert "fail_rule" in result.failed_rules


def test_engine_empty_rules():
    engine = Engine([])
    result = engine.run(Context({}))

    assert result.passed_count == 0
    assert result.actions == []
