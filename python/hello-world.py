import time
import signal
from gpiozero import LineSensor


sensor = LineSensor(17)
sensor.when_line = lambda: print('Line detected')
sensor.when_no_line = lambda: print('No line detected')

# t1 = multiprocessing.Process(target=test_function)
# t2 = multiprocessing.Process(target=test_function)
# t1.start()
# t2.start()

signal.sigwait(sensor.when_line)

print("LineSensor")
#time.sleep(10)
#print("Slept")