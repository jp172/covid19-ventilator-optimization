# the solver should do the simulation, i.e., go through time steps, call the scheduler
# if a new request comes in, etc. to this end the requests should be sorted in terms of time.
from src.schedulers.vehicle_scheduler import *
from src.helper_functions.ab_duration import get_duration

def solve(instance, simulator):


    # do the simulation
    updates_requests = []
    for r in instance.requests:
        updates_requests.append([r.ident, r.filed_at, True])
    for b in instance.bed_updates.values():
        updates_requests.append([b.ident, b.filed_at, False])

    reqs = sorted(reqs, key = lambda r : r[1])

    for el in updates_and_requests:
        if el[2] == True:
            r = instance.requests[el[0]]
            hospital = simulator.assign_request(instance.hospitals, r)

            # set person/request properties
            r.is_handled = True
            r.person.assigned_hospital_id = hospital.ident
            r.person.is_assigned = True

            vehicle = vehicle_scheduler(instance.vehicles, r)
            pickup_at = get_duration(vehicle.position, r.person.position, vehicle.speed)
            delivery_at = get_duration(r.person.position, hospital.position, vehicle.speed)
            r.pickup_at = pickup_at
            r.delivery_at = delivery_at

        # it is a bed update. update hospital!
        else:
            b = instance.bed_updates[el[0]]
            h = instance.hospitals[b.hospital_id]
            h.nbr_free_beds = b.nbr_free_beds
            h.nbr_free_corona_beds = b.nbr_free_corona_beds
