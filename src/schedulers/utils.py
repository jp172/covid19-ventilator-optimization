from ..helper_functions.coordinates_to_distance import get_distance
from ..globals import MAX_VEHICLE_RANGE


def get_feasible_hospitals(hospitals, person_position):
    return list(filter(
            lambda h: (h.nbr_free_beds > 0 or h.nbr_free_corona_beds > 0) and get_distance(h.position, person_position)
            < MAX_VEHICLE_RANGE, hospitals)
            )
