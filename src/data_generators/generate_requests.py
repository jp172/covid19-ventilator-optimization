import json
import random

from ..helper_functions.write_data import write_object_dict
from ..objects.request import Request

time_range = (0, 100000)


def generate_requests(patients, write=True):
    requests = {}

    for ident, p in patients.items():
        request = Request(
            ident=ident, person=p, filed_at=random.uniform(time_range[0], time_range[1])
        )
        requests[ident] = request

    if write:
        write_object_dict(requests, "data/patient_requests/requests.json")

    return requests
