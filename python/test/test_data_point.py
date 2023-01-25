import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

import unittest
from influxdb_client import Point
from meterly import DataPoint

class TestDataPoint(unittest.TestCase):
    def setUp(self):
        self.datapoint = DataPoint("test_measurement", "test_location", "test_sensor_type", 42)
        
    def test_init(self):
        self.assertEqual(self.datapoint.measurement, "test_measurement")
        self.assertEqual(self.datapoint.location, "test_location")
        self.assertEqual(self.datapoint.sensor_type, "test_sensor_type")
        self.assertEqual(self.datapoint.power_per_turn, 42)

    def test_set_turns(self):
        self.datapoint.set_turns(13)
        self.assertEqual(self.datapoint.point._fields, {"power_per_turn": 42, "turns": 13})

    def test_get_point(self):
        self.datapoint.set_turns(13)
        self.assertIsInstance(self.datapoint.get_point(), Point)        
        self.assertTrue("test_measurement" in str(self.datapoint.get_point()))
        self.assertTrue("location=test_location" in str(self.datapoint.get_point()))
        self.assertTrue("sensor_type=test_sensor_type" in str(self.datapoint.get_point()))
        self.assertTrue("power_per_turn=42" in str(self.datapoint.get_point()))
        self.assertTrue("turns=13" in str(self.datapoint.get_point()))

if __name__ == '__main__':
    unittest.main()