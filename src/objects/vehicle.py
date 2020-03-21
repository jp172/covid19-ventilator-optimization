class Vehicle:
    def __init__(self, max_range, is_corona_vehicle, lat, lon):
        self.max_range = max_range
        self.is_corona_vehicle = is_corona_vehicle
        self.position = (lat, lon)
