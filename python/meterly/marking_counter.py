from gpiozero import LineSensor

class MarkingCounter:
    def __init__(self, pin, sample_rate=1000, interval=60):
        self.sensor = LineSensor(pin, sample_rate=sample_rate)
        self.sensor.when_line = self.marking_detected
        self.sensor.when_no_line = self.marking_passed
        
        self.on_marking_detected = None
        self.on_marking_passed = None

        self.count = 0
        
    def marking_detected(self):
        self.count += 1
        if callable(self.on_marking_detected):
            self.on_marking_detected(self.count)
            
    def marking_passed(self):
        if callable(self.on_marking_passed):
            self.on_marking_passed(self.count)
                
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
    
    def get_count(self):
        return self.count