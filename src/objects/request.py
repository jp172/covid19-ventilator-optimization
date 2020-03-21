from dataclasses import dataclass
from dataclasses_json import dataclass_json

from person import Person


@dataclass_json
@dataclass
class Request:
    filed_at: int
    is_handled: bool
    person: Person
