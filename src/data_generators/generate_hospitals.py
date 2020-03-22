import random

from ..helper_functions.write_data import write_objects
from ..globals import CAPACITY_SCALAR
from src.objects.hospital import Hospital
from src.objects.position import Position


num_hospitals = 100
max_num_free_beds = 20
lat_range = (48, 52)
lon_range = (8, 12)


def generate_hospitals(write=True):

    # coordinate ranges

    hospitals = {}

    for i in range(num_hospitals):
        num_free_beds = random.randint(0, max_num_free_beds)
        num_free_corona_beds = random.randint(0, num_free_beds)
        num_corona_pat_in_normal_bed = random.randint(
            0, num_free_beds - num_free_corona_beds
        )
        hospital = Hospital(
            ident=i,
            position=Position(
                lat=random.uniform(lat_range[0], lat_range[1]),
                lon=random.uniform(lon_range[0], lon_range[1]),
            ),
            nbr_free_beds=num_free_beds,
            nbr_free_corona_beds=num_free_corona_beds,
            nbr_corona_pat_in_normal_bed=num_corona_pat_in_normal_bed,
            capacity_coefficient=1e9
            if num_free_corona_beds == 0
            else (CAPACITY_SCALAR * num_corona_pat_in_normal_bed)
            / num_free_corona_beds,
        )
        hospitals[i] = hospital

    if write:
        write_objects(hospitals, "data/hospitals/hospitals.json")

    return hospitals
