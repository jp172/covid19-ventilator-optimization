from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .hospital import Hospital
from .request import Request
from .vehicle import Vehicle

@dataclass_json
@dataclass
class Instance:
    hospitals : dict
    requests : dict
    vehicles : dict
    time_frame : tuple
