from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from enum import Enum
from .person import Person
from .location import Location


@dataclass_json
@dataclass
class PatientRequest:
    ident: int
    filed_at: int
    person: Person

    current_location: Location
    immediate_medical_needs: list = field(default_factory=list)
    patient_prognosis: list = field(default_factory=list)
    patient_demographics: list = field(default_factory=list)
    preferred_hospitals: list = field(default_factory=list)
    preferred_regions: list = field(default_factory=list)
    preferred_types: list = field(default_factory=list)

    pickup_at: int = -1
    delivery_at: int = -1
    is_handled: bool = False
    hospital_id: int = -1


class Intent(Enum):
    EXPLORATION = 1
    NEEDHELP = 2


class PatientStatus(Enum):
    MILD = 1
    SEVERE = 2
    CRITICAL = 3


class Covid19Status(Enum):
    NONE = 1
    LIKELY = 2
    TESTED = 3
    CONFIRMED = 4
