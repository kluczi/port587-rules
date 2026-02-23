"""Actions that can be triggered by rules."""

from typing import Any
from enum import Enum


class ActionType(Enum):
    PAUSE_CAMPAIGN = ("pause_campaign",)
    REDUCE_VOLUME = ("reduce_volume",)
    INCREASE_VOLUME = ("increase_volume",)
    HARD_STOP = "hard_stop"


class Action:
    def __init__(
        self, action_type: ActionType, payload: dict[str, Any], source_rule: str
    ):
        self.action_type = action_type
        self.payload = payload
        self.source_rule = source_rule

    def to_dict(self) -> dict:
        return {
            "action_type": self.action_type.name,
            "payload": self.payload,
            "source_rule": self.source_rule,
        }
