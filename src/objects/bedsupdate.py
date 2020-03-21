from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class BedsUpdate:
    ident : int
    hospital_key : str
    filed_at: int
    nbr_free_beds : int = 0
    nbr_free_corona_beds : int = 0
