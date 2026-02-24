import unittest

from core.context import Context
from core.condition import Condition, ComparisonOperator


class TestCondition(unittest.TestCase):
    def test_greater_than_pass(self):
        context = Context({"reply_rate": 0.05})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.GREATER_THAN, expected=0.03
        )

        result = condition.evaluate(context)

        self.assertTrue(result.passed)
        self.assertIn("Metric 'reply_rate'", result.reason)
        self.assertIn("threshold 0.03", result.reason)

    def test_greater_than_fail(self):
        context = Context({"reply_rate": 0.01})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.GREATER_THAN, expected=0.03
        )

        result = condition.evaluate(context)

        self.assertFalse(result.passed)
        self.assertIn("Metric 'reply_rate' did not", result.reason)
        self.assertIn("threshold 0.03", result.reason)

    def test_equal_pass(self):
        context = Context({"reply_rate": 0.02})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.EQUAL, expected=0.02
        )

        result = condition.evaluate(context)

        self.assertTrue(result.passed)
        self.assertIn("Metric 'reply_rate'", result.reason)
        self.assertIn("threshold 0.02", result.reason)

    def test_equal_fail(self):
        context = Context({"reply_rate": 0.04})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.EQUAL, expected=0.02
        )

        result = condition.evaluate(context)

        self.assertFalse(result.passed)
        self.assertIn("Metric 'reply_rate' did not", result.reason)
        self.assertIn("threshold 0.02", result.reason)

    def test_greater_equal_equal_values(self):
        context = Context({"reply_rate": 0.1})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.GREATER_EQUAL, expected=0.1
        )

        result = condition.evaluate(context)

        self.assertTrue(result.passed)

    def test_greater_equal_greater_values(self):
        context = Context({"reply_rate": 0.4})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.GREATER_EQUAL, expected=0.1
        )

        result = condition.evaluate(context)

        self.assertTrue(result.passed)

    def test_greater_equal_less_fail(self):
        context = Context({"reply_rate": 0.1})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.GREATER_EQUAL, expected=0.4
        )

        result = condition.evaluate(context)

        self.assertFalse(result.passed)

    def test_less_equal_equal_values(self):
        context = Context({"reply_rate": 0.1})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.LESS_EQUAL, expected=0.1
        )

        result = condition.evaluate(context)

        self.assertTrue(result.passed)

    def test_less_equal_less_pass(self):
        context = Context({"reply_rate": 0.05})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.LESS_EQUAL, expected=0.1
        )

        result = condition.evaluate(context)

        self.assertTrue(result.passed)

    def test_less_equal_greater_fail(self):
        context = Context({"reply_rate": 0.15})
        condition = Condition(
            field="reply_rate", op=ComparisonOperator.LESS_EQUAL, expected=0.1
        )

        result = condition.evaluate(context)

        self.assertFalse(result.passed)


if __name__ == "__main__":
    unittest.main()
