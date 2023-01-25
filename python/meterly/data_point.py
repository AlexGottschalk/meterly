from influxdb_client import Point

class DataPoint:
    def __init__(self, measurement, location, sensor_type, power_per_turn):
        self.measurement = measurement
        self.location = location
        self.sensor_type = sensor_type
        self.power_per_turn = power_per_turn
        self.point = Point(measurement).tag("location", location).tag("sensor_type", sensor_type).field("power_per_turn", power_per_turn)

    def set_turns(self, turns):
        self.point.field("turns", turns)
        
    def get_point(self):
        return self.point