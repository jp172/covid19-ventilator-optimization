from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from typing import List

from .position import Position


@dataclass_json
@dataclass
class Vehicle:
    ident : int
    max_range: int
    position: Position
    depot_position: Position
    speed : int # in km/h
    locations: List[Position] = field(default_factory=list)
