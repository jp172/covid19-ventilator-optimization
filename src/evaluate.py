from .globals import ScoreWeight, TARGET_SCORE


def return_score_for_capacity(capacity):
    if capacity > 1.75:
        return ScoreWeight.HIGH.value
    elif capacity > 1.5:
        return ScoreWeight.MIDDLE.value
    elif capacity > 1:
        return ScoreWeight.LOW.value
    else:
        return 0


def weighted_evaluation(instance):
    capacity_coefficients = list(
        map(lambda hosp: hosp.capacity_coefficient, instance.hospitals.values())
    )
    score = sum([return_score_for_capacity(cap) for cap in capacity_coefficients])

    if score < TARGET_SCORE:
        print(f"The world is saved. (score: {score})")
    else:
        print(f"The world is doomed.(score: {score})")

    return score


def simple_evaluation(instance):
    capacity_coefficients = list(
        map(lambda hosp: hosp.capacity_coefficient, instance.hospitals.values())
    )
    score = sum([1 for cap in capacity_coefficients if cap > 1])

    if score < TARGET_SCORE // 2:
        print(f"The world is saved. (score: {score})")
    else:
        print(f"The world is doomed.(score: {score})")

    return score


def quadratic_evaluation(instance):
    pass
