#!/usr/bin/python

import RPi.GPIO as GPIO
import time

input = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(input, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# when the Keurig K55 is ready to brew is flashes 
# the brew button LEDs on and off each second 
# so read the LED state for 2 seconds to see
# if it is flashing

first = GPIO.input(input)
time.sleep(.5)
second = GPIO.input(input)
time.sleep(.5)
third = GPIO.input(input)

if((first == second) and (second == third)):
	print('NO')
else:
	print('YES')
GPIO.cleanup()

#print first, second, third
