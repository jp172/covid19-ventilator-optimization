import json
import overpy
import numpy as np
from random import randint, seed
import matplotlib.pyplot as plt


# set fixed random seed
seed(42)

api = overpy.Overpass()
r = api.query(
    """
area["ISO3166-1"="DE"][admin_level=2];
(node["amenity"="hospital"](area);
 way["amenity"="hospital"](area);
 rel["amenity"="hospital"](area);
);
out center;
"""
)
coords = []
coords += [(float(node.lon), float(node.lat)) for node in r.nodes]

hospital_dict = {
    f"{index}": {
        "ident": index,
        "nbr_free_beds": randint(0, 20),
        "nbr_free_corona_beds": randint(0, 10),
        "position": {"lat": data[1], "lon": data[0]},
        "nbr_corona_pat_in_normal_bed": 0,
        "capacity_coefficient" : 0.0,
    }
    for index, data in enumerate(coords)
}

with open("hospitals.json", "w") as json_file:
    json.dump(hospital_dict, json_file)

# Convert coordinates into numpy array
X = np.array(coords)
plt.plot(X[:, 0], X[:, 1], "o")
plt.title("Hospitals in Germany")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.axis("equal")
plt.show()
