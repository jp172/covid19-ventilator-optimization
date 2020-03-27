from dataclasses import dataclass
from dataclasses_json import dataclass_json

from ..globals import CAPACITY_SCALAR

from .location import Location


@dataclass_json
@dataclass
class Hospital:
    ident: str  # identity
    name: str  # name of hospital
    position: Location  # of hospital
    photo: str  # link to hospital image file
    nbr_free_beds: int
    nbr_free_corona_beds: int
    nbr_corona_beds: int
    nbr_corona_pat_in_normal_bed: int
    available_ventilators: int # number of available ventilators
    capacity_coefficient: float
    current_wait_time: int  # current wait time for check in at hospital
    travel_distance: int  # distance (from patients current location) in meters
    travel_time: int  # travel time of patient to hospital

    def calculate_capacity_coefficient(self):
        self.capacity_coefficient = (
            (1 + CAPACITY_SCALAR * self.nbr_corona_pat_in_normal_bed)
        ) / (1 + max(-0.75, self.nbr_free_corona_beds))
