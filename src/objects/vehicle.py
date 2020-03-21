class Vehicle:
    def __init__(self, max_range, is_corona_vehicle, lat, lon):

        # maximum range the vehicle can actually drive away from its depot
        self.max_range = max_range

        self.is_corona_vehicle = is_corona_vehicle

        self.position = (lat, lon)
        self.depot_position = (lat, lon)

        # list of locations where the vehicle was driven to
        # a vehicle should always go  depot -> pickup -> delivery -> depot
        self.locations = []
