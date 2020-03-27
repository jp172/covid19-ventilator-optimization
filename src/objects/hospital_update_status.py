from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .hospital_status import HospitalStatus

@dataclass_json
@dataclass
class HospitalUpdateStatus:
    status: str
    updated_status: HospitalStatus
