print("Hello world!")

import argparse
from meterly import ConfigReader, InfluxDBConnection, DataPoint, MarkingCounter

def main():
    print("Parse arguments")
    #region Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='python.conf', help='The name of the configuration file.')
    args = parser.parse_args()
    #endregion
    
    print("Setup the configuration file reader")
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

if __name__ == '__main__':
    print('__main__')
    main()