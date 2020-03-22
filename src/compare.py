from copy import deepcopy

from .schedulers.simple_scheduler import SimpleScheduler
from .schedulers.capacity_coefficient_scheduler import CapacityScheduler
from .simulate import simulate
from .evaluate import evaluate


def compare(instance):
    simple_scheduler = SimpleScheduler()
    capacity_scheduler = CapacityScheduler()

    instance_copy = deepcopy(instance)

    snapshots_simple = simulate(instance_copy, simple_scheduler)
    objective_simple = evaluate(instance_copy)
    snapshots_capacity = simulate(instance, capacity_scheduler)
    objective_capacity = evaluate(instance)

    return snapshots_simple, objective_simple, snapshots_capacity, objective_capacity
