from .utils import get_feasible_hospitals
from ..objects.proposal import RankedProposal


class CapacityScheduler:

    def assign_request(self, instance, request):

        hospitals = instance.get_hospitals_in_area(request.person.position)

        # get feasible hospitals checks for vehicle range and free beds
        feasible_hospitals = get_feasible_hospitals(
            hospitals, request.person.position
        )

        # todo: Take the min really from all hospitals here?
        if not feasible_hospitals:
            best_hospital = min(instance.hospitals.values(), key=lambda h: h.capacity_coefficient)
            return RankedProposal([best_hospital])
        else:
            feasible_hospitals = sorted(feasible_hospitals, key=lambda h: h.capacity_coefficient)[:3]
            return RankedProposal(feasible_hospitals)
