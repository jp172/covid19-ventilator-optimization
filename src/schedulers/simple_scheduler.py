from ..helper_functions.coordinates_to_distance import get_distance
from ..objects.proposal import RankedProposal
from .utils import get_feasible_hospitals


class SimpleScheduler:
    # dispositions schedule patients to bed as long as there are available beds in nearby hospitals
    # they choose the nearest available hospital
    def assign_request(self, instance, request):

        hospitals = instance.get_hospitals_in_area(request.person.position)

        sorted_hospitals = sorted(
            hospitals,
            key=lambda hosp: get_distance(hosp.position, request.person.position),
        )

        # get feasible hospitals checks for vehicle range and free beds
        feasible_hospitals = get_feasible_hospitals(sorted_hospitals, request.person.position)

        if not feasible_hospitals:
            return RankedProposal([sorted_hospitals[0]])

        return RankedProposal(feasible_hospitals[: min(len(feasible_hospitals), 3)])
