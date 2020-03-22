from .utils import get_feasible_hospitals
from ..objects.proposal import RankedProposal


class CapacityScheduler:
    def assign_request(self, hospitals, request, max_vehicle_range):
        hospitals = sorted(hospitals, key=lambda hosp: hosp.capacity_coefficient)

        feasible_hospitals = get_feasible_hospitals(
            hospitals, request.person.position, max_vehicle_range
        )

        # only if we have beds left
        feasible_hospitals = list(filter(lambda h : h.nbr_free_beds >= 0 or h.nbr_free_corona_beds >= 0, feasible_hospitals))

        if not feasible_hospitals:
            return RankedProposal([hospitals[0]])

        return RankedProposal(feasible_hospitals[: min(len(feasible_hospitals), 3)])
