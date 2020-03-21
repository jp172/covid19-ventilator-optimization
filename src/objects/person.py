from dataclasses import dataclass
from dataclasses_json import dataclass_json

from timeOfActions import TimeOfActions
from position import Position


@dataclass_json
@dataclass
class Person:
    ident: str
    position: Position
    corona_likelihood: float
    severity: float
    is_assigned: bool
    is_delivered: bool
    assigned_hospital_id: int = 1
    action_times: TimeOfActions = TimeOfActions()
