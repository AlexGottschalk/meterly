from time import sleep
from threading import Thread
from gpiozero import LineSensor

def event_loop():
    sensor = LineSensor(17)
    sensor.when_line = lambda: print('Line detected')
    sensor.when_no_line = lambda: print('No line detected')

def endless_loop():
    while True:
        sleep(1)

event_thread = Thread(target=event_loop)
event_thread.start()

endless_thread = Thread(target=endless_loop)
endless_thread.start()

event_thread.join()
endless_thread.join()