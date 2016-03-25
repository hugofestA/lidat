#!/usr/bin/env python
import RPi.GPIO as GPIO
import smbus
import time
import os
# 2014-08-26 PCF8591-x.py
# Connect Pi 3V3 - VCC, Ground - Ground, SDA - SDA, SCL - SCL.
# ./PCF8591-x.py
bus = smbus.SMBus(1)
CURR = 1
aout = 0
dout = 18
bright = 0
ifcounter = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(dout, GPIO.OUT)
GPIO.output(dout, GPIO.LOW)
while True:
   start = time.time()
   aout = aout + 1
   v = bus.read_byte(0x48)
   if CURR % 2 != 0:
      print(v)
      if v <= 200:
         GPIO.output(dout, GPIO.HIGH)
      else:
         GPIO.output(dout, GPIO.LOW)
   else:
      print CURR
      print CURR % 2
   print "----"
   CURR = CURR + 1
   end = time.time()
   elapsed = end - start
   time.sleep(0.01 - elapsed)
GPIO.cleanup()
# =
