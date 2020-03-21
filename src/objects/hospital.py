import json

from .position import Position


class Hospital:
    ident: int
    nbr_free_beds: int
    nbr_free_corona_beds: int
    position: Position


def read_hospitals(input_file):
    hospitals = {}
    with open(input_file) as f:
        data = json.load(f)
        for key in data:
            lat = data["latitude"]
            lon = data["longitude"]
            hospitals[key] = (key, 0, 0, lat, lon)
    return hospitals
