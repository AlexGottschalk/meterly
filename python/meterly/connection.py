import random
from influxdb_client import InfluxDBClient, Point
from influxdb_client .client.write_api import SYNCHRONOUS

class InfluxDBConnection:
    def __init__(self, url, token, org, bucket='my_bucket'):
        self.url = url
        self.token = token
        self.org = org
        self.bucket = bucket
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_data(self, data):
        record = Point("electricity_meter").tag("location", "home").tag("sensor_type", "TCRT5000").field("power_per_turn", 75).field("turns", random.randint(0, 10))
        self.write_api.write(bucket=self.bucket, record=record)