from gpiozero import LineSensor
from apscheduler.schedulers.background import BackgroundScheduler

class MarkingCounter:
    def __init__(self, pin, sample_rate=1000, interval=60):
        self.sensor = LineSensor(pin, sample_rate=sample_rate)
        self.sensor.when_line = self.marking_detected
        self.sensor.when_no_line = self.marking_passed

        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.periodic_job, 'interval', seconds=interval)
        self.scheduler.start()

        self.count = 0
        
    def marking_detected(self):
        self.count += 1
        if self.on_marking_detected:
            self.on_marking_detected(self.count)
            
    def marking_passed(self):
        if self.on_marking_passed:
            self.on_marking_passed(self.count)
    
    def periodic_job(self):
        if self.on_periodic_job:
            self.on_periodic_job(self.count)
                
    def set_on_marking_detected(self, fn, reset_count = False):
        def wrapped_fn(count):
            fn(count)
            if reset_count:
                self.count = 0
        self.on_marking_detected = wrapped_fn
        
    def set_on_marking_passed(self, fn, reset_count = False):
        def wrapped_fn(count):
            fn(count)
            if reset_count:
                self.count = 0
        self.on_marking_passed = wrapped_fn
        
    def set_on_periodic_job(self, fn, reset_count = False):
        def wrapped_fn(count):
            fn(count)
            if reset_count:
                self.count = 0
        self.on_periodic_job = wrapped_fn
    
    def get_count(self):
        return self.count