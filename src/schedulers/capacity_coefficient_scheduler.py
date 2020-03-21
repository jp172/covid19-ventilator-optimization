from .utils import get_feasible_hospitals


class CapacityScheduler:
    def assign_request(self, hospitals, request, max_vehicle_range):
        feasible_hospitals = get_feasible_hospitals(
            hospitals, request.person.position, max_vehicle_range
        )

        min_coeff = 1e3
        best_hospital = None

        for hospital in feasible_hospitals:
            if hospital.capacity_coefficient < min_coeff:
                best_hospital = hospital

        return best_hospital
