from random import choice
from ..objects.update import Update

UPDATE_CASES = ["normal_to_corona", "corona_leaves_hosp"]


def get_random_update(time, hospital_key):
    case = choice(UPDATE_CASES)
    if case == "normal_to_corona":
        return Update(
            hospital_ident=hospital_key,
            filed_at=time,
            normal_bed_delta=-1,
            corona_bed_delta=1,
            corona_pat_normal_bed_delta=-1,
        )

    elif case == "corona_leaves_hosp":
        return Update(
            hospital_ident=hospital_key,
            filed_at=time,
            normal_bed_delta=0,
            corona_bed_delta=-1,
            corona_pat_normal_bed_delta=0,
        )
