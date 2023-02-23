import random
import influxdb_client
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

bucket =    "power_consumption_raw"
org =       "data_source"
token =     "KYw6fFH7RpP1MH6Pq8Dex99AAuuTK8dh5XrqdAE_5Sh80nQBrJb2VIFUlR5nCs1H_34-RW9u7sW_S5QKwQD4RQ=="
url =       "http://influxdb:8086"

from threading import Timer

def write_data():
    print("write_data()")

    with InfluxDBClient(url=url, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

        record = influxdb_client.Point("electricity_meter").tag("location", "home").tag("sensor_type", "TCRT5000").field("power_per_turn", 75).field("turns", random.randint(0, 10))

        write_api.write(
            bucket=bucket,
            record=record)
    
    Timer(10, write_data).start()

write_data()