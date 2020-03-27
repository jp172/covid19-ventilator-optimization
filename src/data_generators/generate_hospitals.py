import random

from ..globals import (
    NUMBER_FREE_BEDS,
    NUMBER_CORONA_BEDS,
    NUMBER_FREE_CORONA_BEDS,
    NUMBER_CORONA_PAT_IN_NORMAL_BED
)
from ..helper_functions.read_data import read_objects
from ..helper_functions.write_data import write_objects
from ..globals import CAPACITY_SCALAR
from src.objects.hospital import Hospital
from src.objects.location import Location


def generate_hospitals(write=True):
    hospitals = read_objects("data/hospitals/hospitals-all.json", Hospital)

    for hospital in hospitals.values():
        hospital.nbr_free_beds = NUMBER_FREE_BEDS
        hospital.nbr_free_corona_beds = NUMBER_FREE_CORONA_BEDS
        hospital.nbr_corona_pat_in_normal_bed = NUMBER_CORONA_PAT_IN_NORMAL_BED
        hospital.nbr_corona_beds = NUMBER_CORONA_BEDS

    if write:
        write_objects(hospitals, "data/hospitals/hospitals.json")

    return hospitals
