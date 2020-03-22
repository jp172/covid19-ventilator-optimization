from .globals import ScoreWeight


def return_score_for_capacity(capacity):
    if capacity > 10:
        return ScoreWeight.WEIGHT_OVER_10.value
    elif capacity > 5:
        return ScoreWeight.WEIGHT_OVER_5.value
    elif capacity > 1:
        return ScoreWeight.WEIGHT_OVER_1.value
    else:
        return 0


def evaluate(instance):
    capacity_coefficients = list(
        map(lambda hosp: hosp.capacity_coefficient, instance.hospitals.values())
    )

    return sum([return_score_for_capacity(cap) for cap in capacity_coefficients])
