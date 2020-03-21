from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .person import Person


@dataclass_json
@dataclass
class Request:
    ident: int
    filed_at: int
    person: Person
    pickup_at: int = -1
    delivery_at: int = -1
    is_handled: bool = False
    hospital_id: int = -1
