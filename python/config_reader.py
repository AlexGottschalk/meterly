import configparser
import os.path

class ConfigReader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()

        if not os.path.exists(self.config_file):
            print(f"Error: Configuration file '{config_file}' not found.")
            raise SystemExit

        if not os.access(self.config_file, os.R_OK):
            print(f"Error: Configuration file '{config_file}' not readable.")
            raise SystemExit

        try:
            self.config.read(self.config_file)
        except configparser.Error as e:
            print(f"Error reading configuration file '{config_file}':", e)
            raise SystemExit

    def get(self, section, key, fallback=None, type=str):
        try:
            if type == int:
                return self.config.getint(section, key)
            elif type == float:
                return self.config.getfloat(section, key)
            elif type == bool:
                return self.config.getboolean(section, key)
            else:
                return self.config.get(section, key)
        except (configparser.NoOptionError, configparser.NoSectionError, ValueError):
            return fallback