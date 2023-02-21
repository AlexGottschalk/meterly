from gpiozero import LineSensor
from threading import Thread

def event_loop():
    sensor = LineSensor(17)
    sensor.when_line = lambda: print('Line detected')
    sensor.when_no_line = lambda: print('No line detected')
    while True:
        pass

event_thread = Thread(target=event_loop)
event_thread.start()

# Hier können Sie den Hauptthread fortsetzen und andere Aufgaben ausführen

event_thread.join()