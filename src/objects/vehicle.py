from dataclasses import dataclass
from dataclasses_json import dataclass_json

from typing import List

from .position import Position


@dataclass_json
@dataclass
class Vehicle:
    max_range: int
    position: Position
    depot_position: Position
    locations: List[Position] = []
