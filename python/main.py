print("main.py")

import time
import argparse
from signal import pause
from meterly import ConfigReader, InfluxDBConnection, DataPoint, MarkingCounter

def main():
    print("Parse arguments")
    #region Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='python.conf', help='The name of the configuration file.')
    args = parser.parse_args()
    #endregion

    #region Setup the configuration file reader
    config = ConfigReader(args.config)
    #endregion

    print("Setup the database connection")
    #region Setup the database connection
    url = config.get('influxdb', 'url', 'http://localhost:8086')
    token = config.get('influxdb', 'token', 'my_token')
    org = config.get('influxdb', 'org', 'my_org')
    bucket = config.get('influxdb', 'bucket', 'my_bucket')
    connection = InfluxDBConnection(url, token, org, bucket)
    #endregion

    print("Setup the data (to be written to the database)")
    #region Setup the data (to be written to the database)
    measurement = config.get('data_point', 'measurement', 'my_measurement')
    location = config.get('data_point', 'location', 'my_location')
    sensor_type = config.get('data_point', 'sensor_type', 'my_sensor_type')
    power_per_turn = config.get('data_point', 'power_per_turn', 75, int)
    data_point = DataPoint(measurement, location, sensor_type, power_per_turn)
    #endregion
    
    print("Setup the readout of the analog electricity meter")
    #region Setup the readout of the analog electricity meter
    pin = config.get('marking_counter', 'pin', 17, int)
    sample_rate = config.get('marking_counter', 'sample_rate', 1000, int)
    interval = config.get('marking_counter', 'interval', 60, int)
    counter = MarkingCounter(pin, sample_rate, interval)
    #endregion
    
    print("Record the number of revolutions")
    #region Record the number of revolutions
    counter.set_on_marking_detected(
        lambda count :
            (data_point.set_turns(count),
            connection.write_data([data_point.get_point]),
            print("Test"))
        , True)
    #endregion

if __name__ == '__main__':
    main()
    time.sleep(10)