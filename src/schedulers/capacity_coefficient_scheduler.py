from .utils import get_feasible_hospitals
from ..objects.proposal import RankedProposal


class CapacityScheduler:
    def assign_request(self, hospitals, request, max_vehicle_range):

        # get feasible hospitals checks for vehicle range and free beds
        feasible_hospitals = get_feasible_hospitals(
            hospitals, request.person.position, max_vehicle_range
        )

        if not feasible_hospitals:
            best_hospital = min(hospitals, key=lambda hosp: hosp.capacity_coefficient)
            return RankedProposal([best_hospital])
        else:
            feasible_hospitals = sorted(feasible_hospitals, key = lambda h : h.capacity_coefficient)[:3]
            return RankedProposal(feasible_hospitals)
