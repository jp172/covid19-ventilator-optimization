from ..helper_functions.coordinates_to_distance import get_distance


def get_feasible_hospitals(hospitals, person_position, max_vehicle_range):
    return filter(
            lambda h: (h.nbr_free_beds > 0 or h.nbr_free_corona_beds > 0) and get_distance(h.position, person_position)
            < max_vehicle_range, hospitals)
