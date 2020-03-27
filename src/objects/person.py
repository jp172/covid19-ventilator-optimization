from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .location import Location


@dataclass_json
@dataclass
class Person:
    ident: int
    position: Location
    corona_likelihood: float
    severity: float
