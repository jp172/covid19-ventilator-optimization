# object storing all relevant timing information of a person
class TimeOfActions:
    def __init__(self):
        # time the reqeust for the person is filed
        self.request_filed = -1

        # time the person is picked up
        self.picked_up = -1

        # time the person is delivered to some hospital
        self.delivered = -1

    def to_json(self):
        return {"req_filed" : str(req_filed), "picked_up" : str(picked_up), "delivered" : str(delivered)}
