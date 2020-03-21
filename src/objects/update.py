from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Update:
    hospital_ident: str
    filed_at: int
    normal_bed_delta: int
    corona_bed_delta: int
    corona_pat_normal_bed_delta: int
