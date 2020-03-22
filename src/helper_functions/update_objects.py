from src.helper_functions.ab_duration import get_duration
from ..objects.update import Update


def create_update_object_for_request(request, hospital):
    person = request.person
    if person.corona_likelihood > 0 and person.severity > 0:
        return Update(
            hospital_ident=hospital.ident,
            filed_at=request.filed_at,
            normal_bed_delta=0,
            corona_bed_delta=-1,
            corona_pat_normal_bed_delta=0,
        )
    else:
        return Update(
            hospital_ident=hospital.ident,
            filed_at=request.filed_at,
            normal_bed_delta=-1,
            corona_bed_delta=0,
            corona_pat_normal_bed_delta=0,
        )


def update_objects_after_request(hospital, update, vehicle, request):
    pickup_at = get_duration(vehicle.position, request.person.position, vehicle.speed)
    delivery_at = get_duration(
        request.person.position, hospital.position, vehicle.speed
    )
    request.pickup_at = pickup_at
    request.delivery_at = delivery_at

    hospital.nbr_free_beds += update.normal_bed_delta
    hospital.nbr_free_corona_beds += update.corona_bed_delta
    hospital.nbr_corona_pat_in_normal_bed += update.corona_pat_normal_bed_delta

    hospital.calculate_capacity_coefficient()


def update_hospital(hospital, update):
    hospital.nbr_free_beds += update.normal_bed_delta
    hospital.nbr_free_corona_beds += update.corona_bed_delta
    hospital.nbr_corona_pat_in_normal_bed += update.corona_pat_normal_bed_delta

    hospital.nbr_free_corona_beds = min(hospital.nbr_free_corona_beds, 20)

    hospital.calculate_capacity_coefficient()
