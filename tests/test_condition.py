from core.context import Context
from core.condition import Condition, ComparisonOperator
import pytest


def test_greater_than_pass():
    # GIVEN
    context = Context({"reply_rate": 0.05})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.GREATER_THAN, expected=0.03
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is True


def test_greater_than_fail():
    # GIVEN
    context = Context({"reply_rate": 0.01})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.GREATER_THAN, expected=0.03
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is False


def test_equal_pass():
    # GIVEN
    context = Context({"reply_rate": 0.02})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.EQUAL, expected=0.02
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is True


def test_equal_fail():
    # GIVEN
    context = Context({"reply_rate": 0.04})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.EQUAL, expected=0.02
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is False


def test_greater_equal_equal_values():
    # GIVEN
    context = Context({"reply_rate": 0.1})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.GREATER_EQUAL, expected=0.1
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is True


def test_greater_equal_greater_pass():
    # GIVEN
    context = Context({"reply_rate": 0.4})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.GREATER_EQUAL, expected=0.1
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is True


def test_greater_equal_less_fail():
    # GIVEN
    context = Context({"reply_rate": 0.1})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.GREATER_EQUAL, expected=0.4
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is False


def test_less_equal_equal_values():
    # GIVEN
    context = Context({"reply_rate": 0.1})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.LESS_EQUAL, expected=0.1
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is True


def test_less_equal_less_pass():
    # GIVEN
    context = Context({"reply_rate": 0.05})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.LESS_EQUAL, expected=0.1
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is True


def test_less_equal_greater_fail():
    # GIVEN
    context = Context({"reply_rate": 0.15})
    condition = Condition(
        field="reply_rate", op=ComparisonOperator.LESS_EQUAL, expected=0.1
    )

    # WHEN
    result = condition.evaluate(context)

    # THEN
    assert result.passed is False
