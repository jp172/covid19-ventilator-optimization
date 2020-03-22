from random import random, choice

from .update_for_case import get_update_for_case, feasible_update_cases

from .update_objects import (
    update_hospital,
    update_objects_after_request,
    create_update_object_for_request,
)
from ..schedulers.vehicle_scheduler import vehicle_scheduler
from ..objects.snapshot import Snapshot
from ..globals import BED_UPDATE_PROB


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
        hospital = choice(list(instance.hospitals.values()))
        cases = feasible_update_cases(hospital)
        if not cases:
            return None
        update = get_update_for_case(time, hospital, choice(cases))
        update_hospital(hospital, update)
        return Snapshot(hospital.ident, update.filed_at, hospital.capacity_coefficient)
    return None
