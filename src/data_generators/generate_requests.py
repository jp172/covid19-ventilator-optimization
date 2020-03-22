import json
import random

from ..helper_functions.write_data import write_dict, write_object_dict
from ..objects.request import Request

num_days = 150
num_initially_infected = 10
exponential_rate = 0.15


def populate_exponentially_requests(patients):
    patients_sorted = sorted(patients.values(), key=lambda patient: patient.corona_likelihood, reverse=True)
    num_patients = len(patients_sorted)

    requests = {}
    infected_per_day = {}

    num_already_infected = 0
    for day in range(num_days):
        num_newly_infected = int(exponential_rate * (1 - 1. * num_already_infected / num_patients) * (num_initially_infected + num_already_infected))
        num_newly_infected = min(num_patients - num_already_infected, num_newly_infected)
        
        infected_per_day[day] = num_newly_infected

        for i in range(num_newly_infected):
            patient_i = num_already_infected + i
            patient = patients_sorted[patient_i]

            request = Request(
                ident=patient_i,
                person=patient,
                filed_at=day+random.uniform(0, 1))

            requests[patient_i] = request

        num_already_infected += num_newly_infected

    return requests, infected_per_day


def generate_requests(patients, write=True):
    requests, infected_per_day = populate_exponentially_requests(patients)

    if write:
        write_object_dict(requests, "data/patient_requests/requests.json")
        write_dict(infected_per_day, "data/patient_requests/infected_per_day.json")

    return requests
