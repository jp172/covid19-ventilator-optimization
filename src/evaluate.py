def capacity_coefficients(hospitals):
    return list(map(lambda hosp: hosp.capacity_coefficient, hospitals))


def squared_deviation_from_optimal_capacity(instance):
    coefficients = capacity_coefficients(instance.hospitals.values())

    return sum([(1 - cap) ** 2 for cap in coefficients])
