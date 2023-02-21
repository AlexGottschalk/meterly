from influxdb_client import InfluxDBClient
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
        self.write_api.write(bucket=self.bucket, record=data)
        print('write_data')
        print(data)