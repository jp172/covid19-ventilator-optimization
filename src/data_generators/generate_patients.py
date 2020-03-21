# Generates a JSON file with @nbr_patients patients where for each of them a request will be filed
import json
import random

from ..objects.person import Person
from ..objects.position import Position


def generate_patients(write=True):
    nbr_patients = 2000

    # coordinate ranges
    lat_range = (48, 52)
    lon_range = (8, 12)

    data = {}

    for i in range(nbr_patients):
        p = Person(
            ident=i,
            position=Position(
                random.uniform(lat_range[0], lat_range[1]),
                random.uniform(lon_range[0], lon_range[1]),
            ),
            corona_likelihood=random.random(),
            severity=random.random(),
        )

        data[p.ident] = p.to_dict()
    if write:
        with open("data/patient_requests/patients.json", "w") as f:
            json.dump(data, f)
    return data
