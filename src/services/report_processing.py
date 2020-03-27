from ..objects.hospital_update import HospitalUpdate
from ..helper_functions.read_data import read_objects


def process_report(report_as_json):
    r = read_objects(report_as_json, HospitalUpdate)
    update_database(r)


def update_database(request):
    # todo add database connection here and insert new data of request
    print("todo")


def get_hospital_status(hospital_id):
    h = get_hospital_from_database(hospital_id)
    return h.to_response()


def get_hospital_from_database(id):
    # todo add database connection here.
    return -1