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

    def generate_vehicles(self):
        for h in hospitals.values():
            vehicles[h.ident] = Vehicle(
                ident = h.ident,
                speed = 50,
                max_range = 50,
                position = h.position,
                depot = h.position
            )
