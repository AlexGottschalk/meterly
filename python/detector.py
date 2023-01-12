from apscheduler.schedulers.background import BackgroundScheduler
from gpiozero import LineSensor
from signal import pause

# The GPIO pin which the sensor is connected to.
PIN = 17
# The number of values to read from the device per second.
SAMPLE_RATE = 1000
MEASURE_INTERVAL_SEC = 5

class ElectricityMeter:
    def __init__(self, pin, sample_rate, measure_interval_sec):
        self.disk_rotation_count = 0
        
        self.sensor = LineSensor(pin, sample_rate=sample_rate)
        self.sensor.when_line = self.marking_detected
        self.sensor.when_no_line = self.marking_passed
        
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.capture_measurement, 'interval', seconds=measure_interval_sec)

    def capture_measurement(self):
        print("capture ", self.disk_rotation_count)
        self.disk_rotation_count = 0

    def marking_detected(self):
        self.disk_rotation_count += 1

    def marking_passed(self):
        pass
    
    def start(self):
        self.scheduler.start()
        return self
        
em = ElectricityMeter(PIN, SAMPLE_RATE, MEASURE_INTERVAL_SEC).start()

pause()