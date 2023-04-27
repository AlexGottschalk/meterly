import os
import time
import random
import datetime
import influxdb_client
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

bucket =    "power_consumption_raw"
org =       "data_source"
token =     os.environ['DOCKER_INFLUXDB_INIT_ADMIN_TOKEN']
url =       "http://influxdb:" + os.environ['DOCKER_INFLUXDB_PORT']

from threading import Timer

def write_data():
    with InfluxDBClient(url=url, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

        record = influxdb_client.Point("electricity_meter").tag("location", "home").tag("sensor_type", "TCRT5000").field("power_per_turn", 75).field("turns", 1)

        write_api.write(
            bucket=bucket,
            record=record)
        
        print("{}\t{}".format(datetime.datetime.now(), record))


def write_data_cyclic():
    sleeptime_dlt = 20
    sleeptime_min = 5
    sleeptime_max = 90
    sleeptime = random.randint(sleeptime_min, sleeptime_max)
    
    while True:
        write_data()
        
        sleeptime += random.randint(-sleeptime_dlt, sleeptime_dlt)
        sleeptime = max(sleeptime_min, sleeptime)
        sleeptime = min(sleeptime_max, sleeptime)
        
        time.sleep(sleeptime)
        
write_data_cyclic()