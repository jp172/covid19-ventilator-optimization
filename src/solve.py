# the solver should do the simulation, i.e., go through time steps, call the scheduler
# if a new request comes in, etc. to this end the requests should be sorted in terms of time.
from scheduler.vehicle_scheduler import *
from helper_functions.ab_duration import get_duration

def solve(instance, simulator):


    # do the simulation
    reqs = list(instance.requests.values())
    reqs = sort(reqs, key = lambda r : r.filed_at)

    for r in reqs:
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

    
