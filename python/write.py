# https://pypi.org/project/influxdb-client/
# https://github.com/influxdata/influxdb-client-python/tree/master/examples

import random
import influxdb_client
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

bucket =    "mybucket"
org =       "user"
token =     "8Wp7IUmVGvg_DE_G1sVgiNk-OFqWvdQqsOt9CrNwGB5fM7NNeSYRIeoyMxnXo7Or3Xf0GkVg0ulRrmwj7m5RTA=="
url =       "http://localhost:8086"

with InfluxDBClient(url=url, token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

    for n in range(100):
        record = influxdb_client.Point("my_measurement").tag("my_location", "Prague").field("my_temperature", random.uniform(-20, 45))

        write_api.write(
            bucket=bucket,
            record=record)