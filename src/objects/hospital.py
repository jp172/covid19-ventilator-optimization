class Hospital:
    def __init__(self, id, nbr_free_beds, nbr_free_corona_beds, lat, lon):
        self.id = id
        self.nbr_free_beds = nbr_free_beds
        self.nbr_free_corona_beds = nbr_free_corona_beds
        self.position = (lat, lon)


def read_hospitals(input_file):
    hospitals = {}
    with open(input_file) as f:
        data = json.load(f)
        for key in data:
            lat = data["latitude"]
            lon = data["longitude"]
            hospitals[key] = (key, 0, 0, lat, lon)
