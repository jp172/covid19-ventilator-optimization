from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PatientResponse:
    status: bool
    candidates: list = field(default_factory=list)
