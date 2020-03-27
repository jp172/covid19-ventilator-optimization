from ..helper_functions.read_data import read_objects
from ..objects.patient_request import PatientRequest
from ..objects.instance import Instance
from ..schedulers.capacity_coefficient_scheduler import CapacityScheduler


def process_request(self, request_as_json):
    r = read_objects(request_as_json, PatientRequest)
    instance = read_hospitals_from_db(r)
    scheduler = CapacityScheduler()

    # todo: build correct response object
    return scheduler.assign_request(instance, r)


def read_hospitals_from_db(request):
    # todo add DB connection
    instance = Instance()
    # todo read in hospitals
    return instance

