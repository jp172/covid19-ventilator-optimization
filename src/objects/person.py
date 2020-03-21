from timeOfActions import TimeOfActions

class Person:
    def __init__(self, id, lat, lon, corona_likelihood, severity):
        self.id = str(id)
        # position of person
        self.position = (lat, lon)

        # likelihood of person being infected with corona (float in (0,1))
        self.corona_likelihood = corona_likelihood
        # severity of persons symptoms (float in (0, 1) - 0 is healthy, 1 is dead)
        self.severity = severity

        # is person already assigned to a vehicle
        self.assigned = False

        # is person delivered to a hospital
        self.delivered = False

        # hospital id
        self.assigned_hospital_id = -1

        # object storing all relevant times of actions that happened to the person
        self.time = TimeOfActions()

    def to_json(self):
        return {"id" : self.id, "latitude" : str(self.position[0]), "longitude" : str(self.position[1]),
            "corona_likelihood" : str(self.corona_likelihood), "severity" : str(self.severity), "assigned" : str(self.assigned),
            "hospital_id" : self.assigned_hospital_id, "action_times" : self.time_of_actions.to_json()}
