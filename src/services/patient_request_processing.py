from ..helper_functions.read_data import read_objects
from ..objects.patient_request import PatientRequest
from ..helper_functions.database_operations import read_hospitals_from_db
from ..schedulers.capacity_coefficient_scheduler import CapacityScheduler


def process_patient_request(self, request_as_json):
    r = read_objects(request_as_json, PatientRequest)
    instance = read_hospitals_from_db(r)
    scheduler = CapacityScheduler()

    # todo: build correct response object
    return scheduler.assign_request(instance, r)




