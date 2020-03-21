# Generates a JSON file with @nbr_patients patients where for each of them a request will be filed
import json
import random

from ..objects.person import Person


def generate_patients():
    nbr_patients = 10

    # coordinate ranges
    lat_range = (48, 52)
    lon_range = (8, 12)

    # range where the request file time is taken from
    time_range = (0, 100000)

    data = {}
    data["patients"] = []

    for i in range(nbr_patients):
        p = Person(
            i,
            random.uniform(lat_range[0], lat_range[1]),
            random.uniform(lon_range[0], lon_range[1]),
            random.random(),
            random.random(),
        )
        p.action_times.request_filed = random.uniform(time_range[0], time_range[1])
        data["patients"].append(p.to_dict())

    with open("data/patient_requests/patients.json", "w") as f:
        json.dump(data, f)
