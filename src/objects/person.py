class Person:
    def __init__(self, id, lat, lon, corona_likelihood, severity):
        self.id = str(id)
        self.position = (lat, lon)
        self.corona_likelihood = corona_likelihood
        self.severity

    def to_json(self):
        return { self.id : {"latitude" : str(self.lat), "longitude" : str(self.lon),
            "corona_likelihood" : str(self.corona_likelihood), "severity" : str(self.severity)}}
