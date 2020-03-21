import json, random

from src.objects.hospital import Hospital
from src.objects.position import Position


def generate_hospitals(write = True):
    nbr_hospitals = 10

    # coordinate ranges
    lat_range = (48, 52)
    lon_range = (8, 12)

    ret = {}

    for i in range(nbr_hospitals):
        nbr_free_beds = random.randint(0, 20)
        r = Hospital(
            ident = i,
            nbr_free_beds = nbr_free_beds,
            nbr_free_corona_beds = random.randint(0, nbr_free_beds),
            position = Position(lat = random.uniform(lat_range[0], lat_range[1]),
                                lon = random.uniform(lon_range[0], lon_range[1]))
        )
        ret[i] = r.to_dict()

    if write:
        with open("data/hospitals/hospitals-autogen.json", "w") as f:
            json.dump(ret, f)
