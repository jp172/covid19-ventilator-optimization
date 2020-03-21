from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .person import Person


@dataclass_json
@dataclass
class Request:
    filed_at: int
    pickup_at : int
    delivery_at : int
    is_handled: bool = False
    hospital_id : str
    person: Person
