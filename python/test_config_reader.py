import configparser
import unittest
from config_reader import ConfigReader

class TestConfigReader(unittest.TestCase):
    def setUp(self):
        self.config_file = 'config.ini'
        self.config = configparser.ConfigParser()
        self.config.add_section('DATABASE')
        self.config.set('DATABASE', 'user', 'test_user')
        self.config.set('DATABASE', 'password', 'test_password')
        self.config.set('DATABASE', 'host', 'test_host')
        self.config.set('DATABASE', 'database', 'test_database')

        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

        self.config_reader = ConfigReader(self.config_file)

    def test_get(self):
        self.assertEqual(self.config_reader.get('DATABASE', 'user'), 'test_user')
        self.assertEqual(self.config_reader.get('DATABASE', 'password'), 'test_password')
        self.assertEqual(self.config_reader.get('DATABASE', 'host'), 'test_host')
        self.assertEqual(self.config_reader.get('DATABASE', 'database'), 'test_database')

    def test_get_fallback(self):
        fallback_value = 'fallback_value'
        self.assertEqual(self.config_reader.get('DATABASE', 'non_existing_option', fallback_value), fallback_value)

    def test_get_no_section(self):
        fallback_value = 'fallback_value'
        self.assertEqual(self.config_reader.get('NON_EXISTING_SECTION', 'non_existing_option', fallback_value), fallback_value)

if __name__ == '__main__':
    unittest.main()   
