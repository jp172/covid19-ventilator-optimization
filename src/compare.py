from copy import deepcopy

from .schedulers.simple_scheduler import SimpleScheduler
from .schedulers.capacity_coefficient_scheduler import CapacityScheduler
from .simulate import simulate
from .evaluate import simple_evaluation, weighted_evaluation


def compare(instance):
    simple_scheduler = SimpleScheduler()
    capacity_scheduler = CapacityScheduler()

    instance_copy = deepcopy(instance)

    snapshots_simple = simulate(instance_copy, simple_scheduler)
    objective_simple = simple_evaluation(instance_copy)
    snapshots_capacity = simulate(instance, capacity_scheduler)
    objective_capacity = weighted_evaluation(instance)

    return snapshots_simple, objective_simple, snapshots_capacity, objective_capacity
