from .utils import get_feasible_hospitals
from ..objects.proposal import RankedProposal


class CapacityScheduler:
    def assign_request(self, hospitals, request, max_vehicle_range):
        feasible_hospitals = get_feasible_hospitals(
            hospitals, request.person.position, max_vehicle_range
        )

        sorted_hospitals = sorted(
            feasible_hospitals, key=lambda hosp: hosp.capacity_coefficient
        )

        return RankedProposal(sorted_hospitals[:3])
