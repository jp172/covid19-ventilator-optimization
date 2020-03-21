from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Snapshot:
    hospital_ident: str
    filed_at: int
    capacity_coefficient: float
