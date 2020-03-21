# the solver should do the simulation, i.e., go through time steps, call the scheduler
# if a new request comes in, etc. to this end the requests should be sorted in terms of time.
from src.schedulers.vehicle_scheduler import vehicle_scheduler
from .helper_functions.update_objects import (
    update_hospital,
    update_objects_after_request,
    create_update_object_for_request,
)
from .objects.event import Event


def create_events(instance):
    events = []

    for request in instance.requests.values():
        events.append(Event(request, True))

    for update in instance.updates.values():
        events.append(Event(update, False))
    events = sorted(events, key=lambda r: r.filed_at)
    return events


def solve(instance, scheduler):
    snapshots = {}

    max_vehicle_range = max(
        list(map(lambda x: x.max_range, instance.vehicles.values()))
    )

    for event in create_events(instance):

        cur_time = round(event.filed_at)

        # it is a request, so process request!
        if event.request:
            request = instance.requests[str(event.request.ident)]
            ranked_hospital_proposal = scheduler.assign_request(
                instance.hospitals, request, max_vehicle_range
            )
            hospital = ranked_hospital_proposal.proposal_dict[1]
            update = create_update_object_for_request(request, hospital)
            vehicle = vehicle_scheduler(instance.vehicles, request)

            update_objects_after_request(hospital, update, vehicle, request)

        # event is a bed update. update hospital!
        elif event.update:
            hospital = instance.hospitals[event.update.hospital_ident]
            update_hospital(hospital, event.update)

        # for visualisation: make a snapshot of the current time.
        # hospitals -> id, nbr freebeds, nbr free corona beds,
        hospital_occ = [
            [key, hospital.nbr_free_beds, hospital.nbr_free_corona_beds]
            for key, hospital in instance.hospitals.items()
        ]
        snapshots[cur_time] = hospital_occ

    instance.snapshots = snapshots
