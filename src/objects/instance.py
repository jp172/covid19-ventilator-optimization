from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from .hospital import Hospital
from .request import Request
from .vehicle import Vehicle
from .bedsupdate import BedsUpdate

@dataclass_json
@dataclass
class Instance:
    hospitals : dict = field(default_factory=dict)
    requests : dict = field(default_factory=dict)
    vehicles : dict = field(default_factory=dict)
    bed_updates : dict = field(default_factory=dict)

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

    def generate_bed_updates(self):

        time_frame = [min(r.filed_at for r in requests.values()), max(r.filed_at for r in requests.values())]

        cnt = 0
        for h in hospitals.values():

            # 10 updates over the time frame
            for i in range(10):
                time = round(time_frame[0] + i/10 * time_frame[1] - time_frame[0])

                b = BedsUpdate(
                    ident = cnt,
                    hospital_id = h.ident,
                    filed_at = time,
                    nbr_beds = 100 - 10 * i,
                    nbr_corona_beds = 50 - 5 * i
                )
                bed_updates[cnt] = b

                cnt += 1
