from ..helper_functions.coordinates_to_distance import get_distance


class SimpleScheduler:
    # disponents schedule patients to bed as long as there are available beds in nearby hospitals
    def assign_request(self, hospitals, request):
        # this takes just the nearest hospital
        return min(
            hospitals.values(),
            key=lambda h: get_distance(h.position, request.person.position),
        )
