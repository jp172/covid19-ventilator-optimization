# Generates a JSON file with @nbr_patients patients where for each of them a request will be filed
import csv
import json
import random

from ..objects.city import City
from ..objects.person import Person
from ..objects.position import Position

nbr_patients = 20000


def parse_cities():
    cities = {}
    with open('data/data_gatherer/full_population_data.csv', newline='') as csvfile:
        city_reader = csv.reader(csvfile)
        for row in city_reader:
            city = City(
                    ident=row[0], 
                    name=row[1], 
                    position=Position(row[3], row[4]), 
                    population=row[5], 
                    state=row[6])
            cities[city.ident] = city
    return cities


def generate_patients(write=True):
    cities = parse_cities()
    for city in cities.values():
        print(city.ident, city.name, city.position.lat, city.position.lon, city.population, city.state)

    # coordinate ranges
    lat_range = (48, 52)
    lon_range = (8, 12)

    data = {}

    for i in range(nbr_patients):
        p = Person(
            ident=i,
            position=Position(
                random.uniform(lat_range[0], lat_range[1]),
                random.uniform(lon_range[0], lon_range[1]),
            ),
            corona_likelihood=random.random(),
            severity=random.random(),
        )

        data[p.ident] = p.to_dict()
    if write:
        with open("data/patient_requests/patients.json", "w") as f:
            json.dump(data, f)
    return data
