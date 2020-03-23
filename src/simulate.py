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


    times = sorted(instance.requests.keys())
    all_requests = { t : [] for t in times}
    for t, r in instance.requests.items():
        all_requests[t].append(r)

    for t in times:
        occured_requests = all_requests[t]

        snaps = handle_requests(
            occured_requests, instance, scheduler, MAX_VEHICLE_RANGE
        )
        snapshots.extend(snaps)

        snap = execute_bed_update(instance, t)
        if snap:
            snapshots.append(snap)



    return snapshots
