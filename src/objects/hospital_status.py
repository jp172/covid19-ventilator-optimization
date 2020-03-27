from .location import Location

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class HospitalStatus:
    ident: str
    name: str
    location: Location
    photo: str
    specialty: list = field(default_factory=list)  # collection of specialty of the hospital.
    available_beds: int = -1  # number of available beds at the hospital now.
    available_ventilators: int = -1  # number of available ventilators at the hospital now.
    current_wait_time: int = -1  # current wait time for check-in at the hospital now (in seconds).
    distance: int = -1  # distance to patient
