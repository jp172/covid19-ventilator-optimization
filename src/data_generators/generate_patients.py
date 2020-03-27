import csv
import json
import numpy as np
import random

from ..globals import (
    NUMBER_PATIENTS,
    LAT_DELTA,
    LON_DELTA
)
from ..helper_functions.write_data import write_objects
from ..objects.city import City
from ..objects.person import Person
from ..objects.location import Location


def parse_cities():
    cities = {}

    with open('data/data_gatherer/full_population_data.csv', newline='') as csvfile:
        city_reader = csv.reader(csvfile)
        for row in city_reader:
            city = City(
                    ident=row[0],
                    name=row[1],
                    position=Location(float(row[3]), float(row[4])),
                    population=int(row[5]),
                    population_density=0,
                    state=row[6])
            cities[city.ident] = city

    total_density = 0
    with open('data/data_gatherer/full_population_density_data.csv', newline='') as csvfile:
        city_reader = csv.reader(csvfile)
        for row in city_reader:
            city_name = ''.join(c.lower() for c in row[0] if not c.isspace())
            for city in cities.values():
                if city_name == city.name:
                    city.population_density += int(row[4])
            total_density += int(row[4])

    min_density = 1e9
    for city in cities.values():
        if city.population_density:
            min_density = min(min_density, city.population_density)

    for city in cities.values():
        if not city.population_density:
            city.population_density = min_density

    return cities


def sample_patients(cities):
    patient_cities = random.choices(
            population=list(cities.values()),
            weights=[city.population * city.population_density for city in cities.values()],
            k=NUMBER_PATIENTS)

    patients = {}

    for i, patient_city in enumerate(patient_cities):
        patient = Person(
            ident=i,
            position=Location(
                patient_city.position.lat + random.uniform(-LON_DELTA, LAT_DELTA),
                patient_city.position.lon + random.uniform(-LON_DELTA, LAT_DELTA)
            ),
            corona_likelihood=random.random(),
            severity=random.random()
        )
        patients[patient.ident] = patient

    return patients


def generate_patients(write=True):
    cities = parse_cities()

    patients = sample_patients(cities)

    if write:
        write_objects(patients, "data/patient_requests/patients.json")

    return patients
