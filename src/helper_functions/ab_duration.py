from coordinates_to_distance import get_distance

def get_duration(a, b, speed):
    if speed == 0:
        return 1e18
    else:
        return get_distance(a, b) * 1.4 / speed