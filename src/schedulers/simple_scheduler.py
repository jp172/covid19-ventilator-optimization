from ..helper_functions.coordinates_to_distance import get_distance
from ..objects.proposal import RankedProposal
from .utils import get_feasible_hospitals


class SimpleScheduler:
    # disponents schedule patients to bed as long as there are available beds in nearby hospitals
    # they choose the nearest available hospital
    def assign_request(self, hospitals, request, max_vehicle_range):
        feasible_hospitals = get_feasible_hospitals(
            hospitals, request.person.position, max_vehicle_range
        )

        sorted_hospitals = sorted(
            feasible_hospitals,
            key=lambda hosp: get_distance(hosp.position, request.person.position),
        )

        return RankedProposal(sorted_hospitals[:3])
