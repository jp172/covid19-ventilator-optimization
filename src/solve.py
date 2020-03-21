# the solver should do the simulation, i.e., go through time steps, call the scheduler
# if a new request comes in, etc. to this end the requests should be sorted in terms of time.
from src.schedulers.vehicle_scheduler import vehicle_scheduler
from src.helper_functions.ab_duration import get_duration


def max_vehicle_range(hospital):
    return max(list(map(lambda x: x.max_range, hospital.vehicles.values())))


def solve(instance, scheduler):

    # do the simulation
    updates_requests = []

    for request in instance.requests.values():
        updates_requests.append([request.ident, request.filed_at, True])
    for bed in instance.bed_updates.values():
        updates_requests.append([bed.ident, bed.filed_at, False])

    updates_requests = sorted(updates_requests, key=lambda r: r[1])

    snapshots = {}
    max_vehicle_range = max(
        list(map(lambda x: x.max_range, instance.vehicles.values()))
    )
    for el in updates_requests:

        cur_time = round(el[1])

        # it is a request, so process request!
        if el[2] is True:
            request = instance.requests[str(el[0])]
            hospital = scheduler.assign_request(
                instance.hospitals, request, max_vehicle_range
            )

            # set person/request properties
            request.is_handled = True
            request.person.assigned_hospital_id = hospital.ident
            request.person.is_assigned = True
            request.hospital_id = hospital.ident

            vehicle = vehicle_scheduler(instance.vehicles, request)
            pickup_at = get_duration(
                vehicle.position, request.person.position, vehicle.speed
            )
            delivery_at = get_duration(
                request.person.position, hospital.position, vehicle.speed
            )
            request.pickup_at = pickup_at
            request.delivery_at = delivery_at


            hospital.nbr_free_beds -= 1
            hospital.nbr_free_corona_beds -= 1

        # it is a bed update. update hospital!
        else:
            bed = instance.bed_updates[el[0]]
            hospital = instance.hospitals[bed.hospital_key]
            hospital.nbr_free_beds = bed.nbr_free_beds
            hospital.nbr_free_corona_beds = bed.nbr_free_corona_beds

        # for visualisation: make a snapshot of the current time.
        # hospitals -> id, nbr freebeds, nbr free corona beds,
        hospital_occ = [
            [hospital.ident, hospital.nbr_free_beds, hospital.nbr_free_corona_beds]
            for hospital in instance.hospitals.values()
        ]
        snapshots[cur_time] = hospital_occ

    instance.snapshots = snapshots
