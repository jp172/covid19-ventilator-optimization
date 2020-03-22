from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .position import Position


@dataclass_json
@dataclass
class Hospital:
    ident: str
    position: Position
    num_free_beds: int
    num_free_corona_beds: int
    num_corona_pat_in_normal_bed: int
    capacity_coefficient: float
