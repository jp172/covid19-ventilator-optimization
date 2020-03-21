import json, random
from src.objects.person import Person

nbr_patients = 10
lat_range = (48, 52)
lon_range = (8, 12)

patients = {}

for i in range(nbr_patients):
    patients[i] = Person(i, random.uniform(lat_range), random.uniform(lon_range), random.random(), random.random())

with open('patients.json', 'w') as f:
    f.write(json.loads(patients))
