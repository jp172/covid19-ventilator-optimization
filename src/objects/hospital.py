from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .position import Position


@dataclass_json
@dataclass
class Hospital:
    ident: str
    position: Position
    nbr_free_beds: int
    nbr_free_corona_beds: int
    nbr_corona_pat_in_normal_bed: int
    capacity_coefficient: float

    def calculate_capacity_coefficient(self):
        if self.nbr_free_corona_beds > 20:
            print("Attention: negative capacity. The calculation is fukdup.")
        self.capacity_coefficient = 1 - (self.nbr_free_corona_beds / 20)
