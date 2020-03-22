from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .hospital import Hospital


@dataclass_json
@dataclass
class Update:
    hospital: Hospital
    filed_at: int
    normal_bed_delta: int
    corona_bed_delta: int
    corona_pat_normal_bed_delta: int
