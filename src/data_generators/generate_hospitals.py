import random

from ..helper_functions.read_data import read_objects
from ..helper_functions.write_data import write_objects
from ..globals import CAPACITY_SCALAR
from src.objects.hospital import Hospital
from src.objects.position import Position

max_num_free_beds = 20


def generate_hospitals(write=True):
    hospitals = read_objects("data/hospitals/hospitals-all.json", Hospital)

    for hospital in hospitals.values():
        hospital.nbr_free_beds = random.randint(0, max_num_free_beds + 1)
        hospital.nbr_free_corona_beds = random.randint(0, hospital.nbr_free_beds + 1)
        hospital.nbr_corona_pat_in_normal_bed = random.randint(0, hospital.nbr_free_beds - hospital.nbr_free_corona_beds + 1)
        if hospital.nbr_free_corona_beds == 0:
            hospital.capacity_coefficient = 1e9
        else:
            hospital.capacity_coefficient = (CAPACITY_SCALAR * hospital.nbr_corona_pat_in_normal_bed) / hospital.nbr_free_corona_beds

    if write:
        write_objects(hospitals, "data/hospitals/hospitals.json")

    return hospitals
