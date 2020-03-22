import json
import random

from ..objects.request import Request

# range where the request file time is taken from
time_range = (0, 100000)


def generate_requests(patients, write=True):
    reqs = {}

    for ident, p in patients.items():
        r = Request(
            ident=ident, person=p, filed_at=random.uniform(time_range[0], time_range[1])
        )
        reqs[ident] = r.to_dict()

    if write:
        with open("data/patient_requests/requests.json", "w") as f:
            json.dump(reqs, f)

    return reqs
