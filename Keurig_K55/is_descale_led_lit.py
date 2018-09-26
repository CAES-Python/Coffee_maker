#!/usr/bin/python

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if(GPIO.input(27) ==1):
	print('NO')
else:
	print('YES')
GPIO.cleanup()

