class Driver:
    def __init__(self, lat, lon, shift_start, shift_end):
        self.position = (lat, lon)
        self.shift_start = shift_start
        self.shift_end = shift_end
