from .globals import ScoreWeight, TARGET_SCORE


def return_score_for_capacity(capacity):
    if capacity > 10:
        return ScoreWeight.WEIGHT_OVER_10.value
    elif capacity > 5:
        return ScoreWeight.WEIGHT_OVER_5.value
    elif capacity > 1:
        return ScoreWeight.WEIGHT_OVER_1.value
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
