from .globals import ScoreWeight


def return_score_for_capacity(capacity):
    if capacity > 5:
        return ScoreWeight.HIGH.value
    elif capacity > 2:
        return ScoreWeight.MIDDLE.value
    elif capacity > 1:
        return ScoreWeight.LOW.value
    else:
        return 0


def capacity_coefficients(hospitals):
    return list(map(lambda hosp: hosp.capacity_coefficient, hospitals))


def squared_deviation_from_optimal_capacity(instance):
    coefficients = capacity_coefficients(instance.hospitals.values())

    return sum([(1 - cap) ** 2 for cap in coefficients])
