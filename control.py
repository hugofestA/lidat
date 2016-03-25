#!/usr/bin/env python
import RPi.GPIO as GPIO, time

LED = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

while True:
   print "Setting led to on..."
   GPIO.output(LED, GPIO.HIGH)
   time.sleep(1)
   print "Setting led to off..."
   GPIO.output(LED, GPIO.LOW)
   time.sleep(1)

GPIO.cleanup()
