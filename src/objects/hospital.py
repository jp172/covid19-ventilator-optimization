from dataclasses import dataclass
from dataclasses_json import dataclass_json

from ..globals import CAPACITY_SCALAR

from .position import Position


@dataclass_json
@dataclass
class Hospital:
    ident: str
    position: Position
    nbr_free_beds: int
    nbr_free_corona_beds: int
    nbr_corona_beds: int
    nbr_corona_pat_in_normal_bed: int
    capacity_coefficient: float

    def calculate_capacity_coefficient(self):
        self.capacity_coefficient = (
            (1 + CAPACITY_SCALAR * self.nbr_corona_pat_in_normal_bed)
        ) / (1 + max(-0.75, self.nbr_free_corona_beds))
