from helper_functions.coordinates_to_distance import get_distance


class SimpleScheduler:
    # todo: on given all the objects, return the most suitable hospital ID
    def assign_request_to_hospital(self, hospitals, vehicles, drivers, request):
        # this takes just the nearest hospital
        best_hospital = min(
            hospitals.values(), key=lambda h: get_distance(h.position, request.position)
        )
        return best_hospital.id
