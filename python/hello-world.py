from time import sleep
from gpiozero import LineSensor

def test():
    sensor = LineSensor(17)
    sensor.when_line = lambda: print('Line detected')
    sensor.when_no_line = lambda: print('No line detected')

while True:
    sleep(1)