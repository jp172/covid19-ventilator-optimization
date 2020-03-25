from random import randint
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from math import floor, ceil

from ..helper_functions.update_for_case import get_random_update
from ..helper_functions.hospital_precomputation import get_area_pts
from ..globals import MAX_VEHICLE_RANGE, NBR_SEGMENTS

@dataclass_json
@dataclass
class Instance:
    hospitals: dict = field(default_factory=dict)
    requests: dict = field(default_factory=dict)
    updates: dict = field(default_factory=dict)
    hospitals_in_area: dict = field(default_factory=dict)

    # hospital precomputation
    x_pts: list = field(default_factory=list)
    x_spread_over_nbr: float = 1.0
    y_pts: list = field(default_factory=list)
    y_spread_over_nbr: float = 1.0

    def generate_updates(self):

        time_frame = [
            min(r.filed_at for r in self.requests.values()),
            max(r.filed_at for r in self.requests.values()),
        ]

        for key in self.hospitals:
            # 10 updates over the time frame
            for ind in range(10):
                time = randint(int(time_frame[0]), int(time_frame[1]))
                update = get_random_update(time, self.hospitals[key])

                self.updates[f"{key}#{ind}"] = update

    def get_x_index_from_lon(self, x):
        return floor((x - self.x_pts[0]) / self.x_spread_over_nbr)

    def get_y_index_from_lat(self, y):
        return floor((y - self.y_pts[0]) / self.y_spread_over_nbr)

    def get_hospitals_in_area(self, position):
        x_index = max(0, min(len(self.x_pts) - 1, self.get_x_index_from_lon(position.lon)))
        y_index = max(0, min(len(self.y_pts) - 1, self.get_y_index_from_lat(position.lat)))
        return self.hospitals_in_area[x_index, y_index]

    def precompute_hospitals_in_area(self):

        self.x_pts = get_area_pts([h.position.lon for h in self.hospitals.values()])
        self.y_pts = get_area_pts([h.position.lat for h in self.hospitals.values()])
        self.x_spread_over_nbr = (self.x_pts[-1] - self.x_pts[0]) / len(self.x_pts)
        self.y_spread_over_nbr = (self.y_pts[-1] - self.y_pts[0]) / len(self.y_pts)

        self.hospitals_in_area = {(x, y): [] for x in range(len(self.x_pts)) for y in range(len(self.y_pts))}

        for h in self.hospitals.values():

            x_index = self.get_x_index_from_lon(h.position.lon)
            y_index = self.get_y_index_from_lat(h.position.lat)

            x_box_range = (self.x_pts[-1] - self.x_pts[0]) / NBR_SEGMENTS
            # todo: does not work for antarctica, lol
            veh_degree_range = MAX_VEHICLE_RANGE / 20
            delta_x = ceil(veh_degree_range / x_box_range)

            delta_y = ceil((MAX_VEHICLE_RANGE / 110) / ((self.x_pts[-1] - self.x_pts[0]) / NBR_SEGMENTS))

            for x in range(max(0, x_index - delta_x), min(len(self.x_pts), x_index + delta_x + 1)):
                for y in range(max(0, y_index - delta_y), min(len(self.y_pts), y_index + delta_y + 1)):
                    self.hospitals_in_area[x, y].append(h)
