# the solver should do the simulation, i.e., go through time steps, call the scheduler
# if a new request comes in, etc. to this end the requests should be sorted in terms of time.
from .globals import TIMESTEP, MAX_VEHICLE_RANGE
from .helper_functions.simulate_helpers import (
    get_occured_requests,
    execute_bed_update,
    handle_requests,
)


def simulate(instance, scheduler):
    snapshots = []

    requests = list(instance.requests.values())
    time = 0
    finished = False

    while not finished:
        occured_requests = get_occured_requests(requests, time)

        if len(occured_requests) == len(requests):
            finished = True
        crop_index = len(occured_requests)
        requests = requests[crop_index:]

        snaps = handle_requests(
            occured_requests, instance, scheduler, MAX_VEHICLE_RANGE
        )
        snapshots.extend(snaps)

        snap = execute_bed_update(instance, time)
        if snap:
            snapshots.append(snap)

        time += TIMESTEP

    return snapshots
