from ..helper_functions.coordinates_to_distance import get_distance


def get_feasible_hospitals(hospitals, person_position, max_vehicle_range):
    return list(
        filter(
            lambda hosp: get_distance(hosp.position, person_position)
            < max_vehicle_range,
            hospitals.values(),
        )
    )


class SimpleScheduler:
    # disponents schedule patients to bed as long as there are available beds in nearby hospitals
    # they choose the nearest available hospital
    def assign_request(self, hospitals, request, max_vehicle_range):
        feasible_hospitals = get_feasible_hospitals(
            hospitals, request.person.position, max_vehicle_range
        )
        print(feasible_hospitals)

        min_dist = 1e12
        nearest_hospital = None

        for hospital in feasible_hospitals:
            if get_distance(hospital.position, request.person.position) < min_dist:
                nearest_hospital = hospital

        return nearest_hospital
