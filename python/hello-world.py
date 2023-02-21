import time
import multiprocessing
from signal import pause
from gpiozero import LineSensor

def test():
    sensor = LineSensor(17)
    sensor.when_line = lambda: print('Line detected')
    sensor.when_no_line = lambda: print('No line detected')

t1 = multiprocessing.Process(target=test)
t1.start()

print("LineSensor")
#time.sleep(10)
#print("Slept")