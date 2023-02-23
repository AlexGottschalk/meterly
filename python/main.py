import argparse
import datetime
from signal import pause
from meterly import ConfigReader, InfluxDBConnection, DataPoint, MarkingCounter

def main():
    #region Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='python.conf', help='The name of the configuration file.')
    args = parser.parse_args()
    #endregion

    #region Setup the configuration file reader
    config = ConfigReader(args.config)
    #endregion

    #region Setup the database connection
    url = config.get('influxdb', 'url', 'http://influxdb:8086')
    token = config.get('influxdb', 'token', 'my_token')
    org = config.get('influxdb', 'org', 'my_org')
    bucket = config.get('influxdb', 'bucket', 'my_bucket')    
    connection = InfluxDBConnection(url, token, org, bucket)
    
    print("{}\tInfluxDBConnection(url=\"{}\" org=\"{}\" bucket=\"{}\")".format(datetime.datetime.now(), url, org, bucket))
    #endregion

    #region Setup the data (to be written to the database)
    measurement = config.get('data_point', 'measurement', 'my_measurement')
    location = config.get('data_point', 'location', 'my_location')
    sensor_type = config.get('data_point', 'sensor_type', 'my_sensor_type')
    power_per_turn = config.get('data_point', 'power_per_turn', 75, int)
    data_point = DataPoint(measurement, location, sensor_type, power_per_turn)
    #endregion
    
    #region Setup the readout of the analog electricity meter
    pin = config.get('marking_counter', 'pin', 17, int)
    sample_rate = config.get('marking_counter', 'sample_rate', 1000, int)
    interval = config.get('marking_counter', 'interval', 60, int)
    counter = MarkingCounter(pin, sample_rate, interval)
    
    print("{}\tRaspberryPI(pin=\"{}\" sample_rate=\"{}\" interval=\"{}\")".format(datetime.datetime.now(), pin, sample_rate, interval))
    #endregion
    
    #region Record function
    def marking_detected(count):
        point = data_point.set_turns(count).get_point()
        connection.write_data(point)
        print("{}\t{}".format(datetime.datetime.now(), point))
    #endregion
    
    #region Record the number of revolutions    
    counter.set_on_marking_detected(marking_detected, True)
    #endregion

if __name__ == '__main__':
    main()
    print("{}\tSetup successfully completed: Waiting for sensor signal".format(datetime.datetime.now()))
    pause()