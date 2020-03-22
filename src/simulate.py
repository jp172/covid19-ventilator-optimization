# the solver should do the simulation, i.e., go through time steps, call the scheduler
# if a new request comes in, etc. to this end the requests should be sorted in terms of time.
from src.schedulers.vehicle_scheduler import vehicle_scheduler
from .helper_functions.update_objects import (
    update_hospital,
    update_objects_after_request,
    create_update_object_for_request,
)
from random import random, choice

from .helper_functions.update_for_case import get_random_bed_update
from .globals import TIMESTEP, BED_UPDATE_PROB
from .objects.snapshot import Snapshot


def handle_requests(curr_requests, instance, scheduler, max_vehicle_range):
    snaps = []
    for request in curr_requests:
        ranked_hospital_proposal = scheduler.assign_request(
            instance.hospitals.values(), request, max_vehicle_range
        )
        hospital = ranked_hospital_proposal.proposal_dict[1]
        curr_update = create_update_object_for_request(request, hospital)
        vehicle = vehicle_scheduler(instance.vehicles, request)

        update_objects_after_request(hospital, curr_update, vehicle, request)

        snaps.append(
            Snapshot(hospital.ident, request.filed_at, hospital.capacity_coefficient)
        )
    return snaps


def get_occured_requests(requests, time):
    occured_requests = []
    for ind, req in enumerate(requests):
        if req.filed_at <= time:
            occured_requests.append(req)
        if req.filed_at > time:
            break
    return occured_requests


def execute_bed_update(instance, time):
    update_roll = random()
    if update_roll < BED_UPDATE_PROB:
        hospital_key = choice(list(instance.hospitals.keys()))
        hospital = instance.hospitals[hospital_key]

        update = get_random_bed_update(update_roll, hospital_key, time)
        update_hospital(hospital, update)
        return Snapshot(hospital.ident, update.filed_at, hospital.capacity_coefficient)
    return None


def simulate(instance, scheduler):
    snapshots = []

    max_vehicle_range = max(
        list(map(lambda x: x.max_range, instance.vehicles.values()))
    )

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
            occured_requests, instance, scheduler, max_vehicle_range
        )
        snapshots.extend(snaps)

        snap = execute_bed_update(instance, time)
        snapshots.append(snap)

        time += TIMESTEP

    return snapshots
