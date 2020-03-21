from .schedulers.simple_scheduler import SimpleScheduler
from .schedulers.capacity_coefficient_scheduler import CapacityScheduler
from .simulate import simulate


def compare(instance):
    simple_scheduler = SimpleScheduler()
    capacity_scheduler = CapacityScheduler()

    return simulate(instance, simple_scheduler), simulate(instance, capacity_scheduler)
