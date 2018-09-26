#!/usr/bin/python
import RPi.GPIO as GPIO
import time

pin = 18 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT) 

try:
	GPIO.output(pin, GPIO.HIGH)
	print "Closed"

# End program cleanly with keyboard
except KeyboardInterrupt:
	print "  Quit"

	# Reset GPIO settings
	GPIO.cleanup()

