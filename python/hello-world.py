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
    
    #region Setup the configuration file reader
    config = ConfigReader(args.config)
    #endregion

if __name__ == '__main__':
    print('__main__')
    main()