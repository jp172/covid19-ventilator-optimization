from random import choice
from ..objects.update import Update

from ..globals import UPDATE_CASES


def get_update_for_case(time, hospital, case):
    if case == "normal_to_corona":
        return Update(
            hospital=hospital,
            filed_at=time,
            normal_bed_delta=-1,
            corona_bed_delta=1,
            corona_pat_normal_bed_delta=-1,
        )

    elif case == "corona_leaves_hosp":
        return Update(
            hospital=hospital,
            filed_at=time,
            normal_bed_delta=0,
            corona_bed_delta=-1,
            corona_pat_normal_bed_delta=0,
        )


def get_random_update(time, hospital):
    case = choice(UPDATE_CASES)
    get_update_for_case(time, hospital, case)


def feasible_update_cases(hospital):
    cases = []
    if hospital.nbr_corona_pat_in_normal_bed > 0:
        cases.append("normal_to_corona")
    if hospital.nbr_free_corona_beds < hospital.nbr_corona_beds:
        cases.append("corona_leaves_hosp")
    return cases


def get_random_bed_update(update_roll, hospital, time):
    return Update(
        hospital=hospital,
        filed_at=time,
        normal_bed_delta=0,
        corona_bed_delta=-1,
        corona_pat_normal_bed_delta=0,
    )
