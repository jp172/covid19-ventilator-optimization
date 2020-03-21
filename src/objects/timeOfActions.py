from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
# object storing all relevant timing information of a person
class TimeOfActions:
    request_filed: int
    picked_up: int
    deliverd: int
