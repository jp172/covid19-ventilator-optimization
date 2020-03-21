from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from .hospital import Hospital
from .request import Request
from .vehicle import Vehicle

@dataclass_json
@dataclass
class Instance:
    hospitals : dict = field(default_factory=dict)
    requests : dict = field(default_factory=dict)
    vehicles : dict = field(default_factory=dict)

    def generate_vehicles(self):
        for h in self.hospitals.values():
            v = Vehicle(
                ident = h.ident,
                speed = 50,
                max_range = 50,
                position = h.position,
                depot_position = h.position
            )
            self.vehicles[v.ident] = v
