"""Actions that can be triggered by rules."""

from typing import Callable, Dict, Any
from enum import Enum

class ActionType(Enum):
    PAUSE_CAMPAIGN,
    REDUCE_VOLUME,
    INCREASE_VOLUME,
    HARD_STOP


class Action:    
    def __init__(self, type: ActionType, payload: dict[str, Any], source_rule: str):
        self.type=type
        self.payload=payload
        self.source_rule=source_rule
    def to_dict(self, ):
        
    
