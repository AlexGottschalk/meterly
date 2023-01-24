import argparse
from config_reader import ConfigReader

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='python.conf', help='The name of the configuration file.')
    args = parser.parse_args()

    cfg = ConfigReader(args.config)
    print(cfg.get('influxdb', 'bucket', ''))

if __name__ == '__main__':
    main()