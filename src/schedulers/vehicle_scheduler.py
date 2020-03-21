from ..helper_functions.coordinates_to_distance import get_distance


# given the fleet of vehicles, an incoming request, determine the pickup time
def vehicle_scheduler(vehicles, request):
    return min(
        vehicles.values(),
        key=lambda v: get_distance(v.position, request.person.position),
    )
