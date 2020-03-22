from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .position import Position


@dataclass_json
@dataclass
class City:
    ident: str
    name: str
    position: Position
    population: int
    state: str
