class Person:
    def __init__(self, id, lat, lon, corona_likelihood, severity):
        self.id = str(id)
        self.position = (lat, lon)
        self.corona_likelihood = corona_likelihood
        self.severity = severity

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
    def to_json(self):
        return {"id" : self.id, "latitude" : str(self.position[0]), "longitude" : str(self.position[1]),
            "corona_likelihood" : str(self.corona_likelihood), "severity" : str(self.severity)}
