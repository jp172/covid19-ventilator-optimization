import json
import random

from .generate_patients import generate_patients
from ..objects.request import Request

# range where the request file time is taken from
time_range = (0, 100000)
nbr_patients = 20000


def generate_requests(write=True):
    patients = generate_patients(nbr_patients, write=False)

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
