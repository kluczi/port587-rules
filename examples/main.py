import json
from pathlib import Path

from core.context import Context
from core.condition import Condition, ComparisonOperator
from core.rule import Rule, LogicalOperator
from core.action import Action, ActionType
from core.engine import Engine


def load_campaign_data(path: str) -> Context:
    with open(path, "r") as f:
        data = json.load(f)
    return Context(data)


def build_rules():
    rule_high_bounce = Rule(
        name="High Bounce Rule",
        conditions=[Condition("bounce_rate", ComparisonOperator.GREATER_THAN, 0.03)],
        actions=[
            Action(
                action_type=ActionType.PAUSE_CAMPAIGN,
                payload={"reason": "High bounce rate detected"},
                source_rule="High Bounce Rule",
            )
        ],
    )

    rule_good_reply = Rule(
        name="Good Reply Rule",
        conditions=[Condition("reply_rate", ComparisonOperator.GREATER_EQUAL, 0.02)],
        actions=[
            Action(
                action_type=ActionType.INCREASE_VOLUME,
                payload={"delta": 500},
                source_rule="Good Reply Rule",
            )
        ],
    )

    rule_low_reply_high_volume = Rule(
        name="Low Reply High Volume Rule",
        conditions=[
            Condition("reply_rate", ComparisonOperator.LESS_THAN, 0.01),
            Condition("sent_today", ComparisonOperator.GREATER_THAN, 1000),
        ],
        op=LogicalOperator.AND,
        actions=[
            Action(
                action_type=ActionType.REDUCE_VOLUME,
                payload={"delta": -300},
                source_rule="Low Reply High Volume Rule",
            )
        ],
    )

    return [rule_high_bounce, rule_good_reply, rule_low_reply_high_volume]


def main():
    sample_path = Path(__file__).with_name("sample.json")
    context = load_campaign_data(str(sample_path))

    rules = build_rules()
    engine = Engine(rules)

    result = engine.run(context)

    print("RULE RESULTS")
    for r in result.results:
        print(f"\nRule: {r.rule_name}")
        print(f"Passed: {r.passed}")
        for reason in r.reasons:
            print(f" - {reason}")

    print("\nSUMMARY")
    print("Passed rules:", result.passed_rules)
    print("Failed rules:", result.failed_rules)
    print("Passed count:", result.passed_count)
    print("Failed count:", result.failed_count)

    print("\nACTIONS")
    for action in result.actions:
        print(action.to_dict())


if __name__ == "__main__":
    main()
