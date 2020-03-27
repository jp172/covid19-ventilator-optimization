from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class HospitalUpdate:
    hospital_id: str
    filed_at: int
    normal_beds: int = -1
    corona_beds: int = -1
    corona_pat_in_normal_bed: int = -1
    available_ventilators: int = -1
    current_wait_time: int = -1
