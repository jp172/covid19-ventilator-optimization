from random import choice
from ..objects.update import Update

from ..globals import UPDATE_CASES


def get_random_update(time, hospital):
    case = choice(UPDATE_CASES)
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


def feasible_bed_updates_for_hospital(hospital):
    pass


def get_random_bed_update(update_roll, hospital, time):
    return Update(
        hospital=hospital,
        filed_at=time,
        normal_bed_delta=0,
        corona_bed_delta=-1,
        corona_pat_normal_bed_delta=0,
    )
