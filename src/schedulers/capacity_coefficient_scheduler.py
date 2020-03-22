from .utils import get_feasible_hospitals
from ..objects.proposal import RankedProposal


class CapacityScheduler:
    def assign_request(self, hospitals, request, max_vehicle_range):
        sorted_hospitals = sorted(hospitals, key=lambda hosp: hosp.capacity_coefficient)

        feasible_hospitals = get_feasible_hospitals(
            hospitals, request.person.position, max_vehicle_range
        )

        if not feasible_hospitals:
            return RankedProposal([sorted_hospitals[0]])

        return RankedProposal(feasible_hospitals[: min(len(feasible_hospitals), 3)])
