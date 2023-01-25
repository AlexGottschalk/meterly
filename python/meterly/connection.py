from influxdb_client import InfluxDBClient

class InfluxDBConnection:
    def __init__(self, url, token, org, bucket='my_bucket'):
        self.url = url
        self.token = token
        self.org = org
        self.bucket = bucket
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        self.write_api = self.client.write_api()

    def write_data(self, data, sync_=True):
        if sync_:
            self.write_api.write(data, bucket=self.bucket, write_options=self.write_api.SYNCHRONOUS)
        else:
            self.write_api.write(data, bucket=self.bucket)