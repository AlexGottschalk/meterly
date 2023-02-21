#!/usr/bin/env python3

# Minimal example of how to break out of signal.pause().
# This waits for a GPIO button to be held (for 1 second), and then exits.
#
# @see https://docs.python.org/3/library/signal.html
#
# robcranfill@gmail.com

from gpiozero import LineSensor
import os
import signal
import sys


# Handler for SIGUSER1
def handleSignal(num, stack):
  print('Got signal! And now we mysteriously will exit....')


def doShutdown():
  print('In Button.when_held handler...')

  # If this worked, all I really want is this. Or return, or whatever. Done.
  #  Why doesn't this work?
#  sys.exit(1)

  # Send a SIGUSER1; this seems to cause signal.pause() to return.
  os.kill(os.getpid(), signal.SIGUSR1)


sensor = LineSensor(17)
sensor.when_line = lambda: print('Line detected')
sensor.when_no_line = lambda: print('No line detected')

# Install a handler for SIGUSER1 .... which seems to entirly fix our problem. Why?!?!
signal.signal(signal.SIGUSR1, handleSignal)

# This waits.
# According to the docs,
#  "Cause the process to sleep until a signal is received; the appropriate handler will then be called."
# so I guess this makes sense.
#
print('Waiting for button hold....')
signal.pause()

