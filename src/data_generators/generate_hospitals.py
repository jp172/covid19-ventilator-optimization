import json
import random

from src.objects.hospital import Hospital
from src.objects.position import Position

CAPACITY_SCALAR = 0.25


def generate_hospitals(write=True):

    nbr_hospitals = 100

    # coordinate ranges
    lat_range = (48, 52)
    lon_range = (8, 12)

    ret = {}

    for i in range(nbr_hospitals):
        nbr_free_beds = random.randint(0, 20)
        nbr_free_corona_beds = random.randint(0, nbr_free_beds)
        nbr_corona_pat_in_normal_bed = random.randint(
            0, nbr_free_beds - nbr_free_corona_beds
        )
        r = Hospital(
            ident=i,
            position=Position(
                lat=random.uniform(lat_range[0], lat_range[1]),
                lon=random.uniform(lon_range[0], lon_range[1]),
            ),
            nbr_free_beds=nbr_free_beds,
            nbr_free_corona_beds=nbr_free_corona_beds,
            nbr_corona_pat_in_normal_bed=nbr_corona_pat_in_normal_bed,
            capacity_coefficient=1e9
            if nbr_free_corona_beds == 0
            else (CAPACITY_SCALAR * nbr_corona_pat_in_normal_bed)
            / nbr_free_corona_beds,
        )
        ret[i] = r.to_dict()

    if write:
        with open("data/hospitals/hospitals.json", "w") as f:
            json.dump(ret, f)
