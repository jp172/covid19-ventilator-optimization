from ..helper_functions.read_data import read_objects
from ..objects.instance import Instance
from ..objects.hospital import Hospital
from ..objects.request import Request


def build_instance(args):
    project_instance = Instance()
    project_instance.hospitals = read_objects(
        "data/hospitals/hospitals.json", Hospital
    )

    project_instance.requests = read_objects(
        "data/patient_requests/requests.json", Request
    )

    print("precomputing hospitals for areas")
    project_instance.precompute_hospitals_in_area()

    return project_instance
