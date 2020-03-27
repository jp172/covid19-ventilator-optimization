from ..objects.report import Report
from ..helper_functions.read_data import read_objects


def process_report(self, report_as_json):
    r = read_objects(report_as_json, Report)
    self.update_database(r)


def update_database(self, request):
    # todo add database connection here and insert new data of request
    print("todo")
