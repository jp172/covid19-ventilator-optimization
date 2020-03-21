from helper_functions.coordinates_to_distance import *

class SimpleScheduler:
    # todo: on given all the objects, return the most suitable hospital ID
    def assign_request_to_hospital(self, hospitals, vehicles, drivers, request):
        best_hospital =  min(hospitals.values(), key = lambda h : get_distance(h.position, r.position))
