from gpiozero import LineSensor
from signal import pause

sensor = LineSensor(17)
sensor.when_line = lambda: print('Line detected')
sensor.when_no_line = lambda: print('No line detected')

while True:
    pass