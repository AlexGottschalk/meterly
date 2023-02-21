import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
    while True:
        if GPIO.input(17) == 1:
            print("I saw the sign!")
        else: 
            print("Waiting")
        time.sleep(1)
except KeyboardInterrupt:
    print("Bye Bye")
    GPIO.cleanup()