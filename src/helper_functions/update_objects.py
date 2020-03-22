from ..objects.update import Update


def create_update_object_for_request(request, hospital):
    person = request.person
    if person.severity > 0.8:
        return Update(
            hospital=hospital,
            filed_at=request.filed_at,
            normal_bed_delta=0,
            corona_bed_delta=-1,
            corona_pat_normal_bed_delta=0,
        )
    else:
        return Update(
            hospital=hospital,
            filed_at=request.filed_at,
            normal_bed_delta=-1,
            corona_bed_delta=0,
            corona_pat_normal_bed_delta=1,
        )


def update_objects_after_request(hospital, update):
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
