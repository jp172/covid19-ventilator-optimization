from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .position import Position


@dataclass_json
@dataclass
class Person:
    ident: int
    position: Position
    corona_likelihood: float
    severity: float
