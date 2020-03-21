from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .position import Position


@dataclass_json
@dataclass
class City:
    name: str
    full_name: str
    ident: int
    position: Position
    population: int
    state: str
