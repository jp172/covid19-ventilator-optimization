from ..helper_functions.coordinates_to_distance import get_distance
from ..objects.proposal import RankedProposal
from .utils import get_feasible_hospitals


class SimpleScheduler:
    # disponents schedule patients to bed as long as there are available beds in nearby hospitals
    # they choose the nearest available hospital
    def assign_request(self, hospitals, request, max_vehicle_range):
        sorted_hospitals = sorted(
            hospitals,
            key=lambda hosp: get_distance(hosp.position, request.person.position),
        )

        # get feasible hospitals checks for vehicle range and free beds
        feasible_hospitals = get_feasible_hospitals(
            sorted_hospitals, request.person.position, max_vehicle_range
        )

        if not feasible_hospitals:
            return RankedProposal([sorted_hospitals[0]])

        return RankedProposal(feasible_hospitals[: min(len(feasible_hospitals), 3)])
