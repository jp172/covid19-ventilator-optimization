from dataclasses import dataclass
from dataclasses_json import dataclass_json

from ..globals import CAPACITY_SCALAR

from .location import Location


@dataclass_json
@dataclass
class Hospital:
    id: str  # identity
    position: Location  # of hospital
    name: str = ""  # name of hospital
    photo: str = ""  # link to hospital image file
    nbr_free_beds: int = 0  #
    nbr_free_corona_beds: int = 0
    nbr_corona_beds: int = 0
    nbr_corona_pat_in_normal_bed: int = 0
    available_ventilators: int = 0  # number of available ventilators
    capacity_coefficient: float = 0
    current_wait_time: int = 0  # current wait time for check in at hospital
    travel_distance: int = 0 # distance (from patients current location) in meters
    travel_time: int = 0  # travel time of patient to hospital

    def calculate_capacity_coefficient(self):
        self.capacity_coefficient = (
            (1 + CAPACITY_SCALAR * self.nbr_corona_pat_in_normal_bed)
        ) / (1 + max(-0.75, self.nbr_free_corona_beds))
