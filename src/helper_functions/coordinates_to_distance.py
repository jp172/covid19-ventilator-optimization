from math import sin, asin, cos, sqrt, radians

# distance in kilometers between two positions
# position is given as spherical coordinates (lat, lon)


def get_distance(a, b):
    (lat1, lon1) = a
    (lat2, lon2) = b
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371.0 * asin(sqrt(a))
