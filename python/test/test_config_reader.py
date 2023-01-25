import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

import unittest
import configparser
from meterly import ConfigReader

class TestConfigReader(unittest.TestCase):
    def setUp(self):
        self.config_file = 'config.ini'
        self.config_parser = configparser.ConfigParser()
        self.config_parser.add_section('SECTION')
        self.config_parser.set('SECTION', 'bool', str(True))
        self.config_parser.set('SECTION', 'float', str(3.14))
        self.config_parser.set('SECTION', 'int', str(42))
        self.config_parser.set('SECTION', 'string', 'test')
        with open(self.config_file, 'w') as configfile:
            self.config_parser.write(configfile)
        self.config_reader = ConfigReader(self.config_file)
        
    def tearDown(self):
        os.remove(self.config_file)

    def test_get(self):
        self.assertEqual(self.config_reader.get('SECTION', 'bool'), 'True')
        self.assertEqual(self.config_reader.get('SECTION', 'float'), '3.14')
        self.assertEqual(self.config_reader.get('SECTION', 'int'), '42')
        self.assertEqual(self.config_reader.get('SECTION', 'string'), 'test')

    def test_get_type(self):
        self.assertEqual(self.config_reader.get('SECTION', 'bool', type=bool), True)
        self.assertEqual(self.config_reader.get('SECTION', 'float', type=float), 3.14)
        self.assertEqual(self.config_reader.get('SECTION', 'int', type=int), 42)
        self.assertEqual(self.config_reader.get('SECTION', 'string', type=str), 'test')

    def test_get_fallback(self):
        self.assertEqual(self.config_reader.get('SECTION', 'fallback', True, bool), True)
    
    def test_raises_system_exit(self):
        with self.assertRaises(SystemExit):
            ConfigReader("file_does_not_exist.ini")

if __name__ == '__main__':
    unittest.main()