from ..helper_functions.coordinates_to_distance import get_distance


class SimpleScheduler:
    # todo: on given all the objects, return the most suitable hospital ID
    def assign_request(self, hospitals, request):
        # this takes just the nearest hospital
        return min(
            hospitals.values(), key=lambda h: get_distance(h.position, request.person.position)
        )
