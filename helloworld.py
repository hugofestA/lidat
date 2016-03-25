import RPi.GPIO as GPIO, time

LED = 2
TEXT = "Hello World!"

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

while True:
   print ' '.join(format(ord(x), 'b') for x in TEXT)
   print "Setting led to on..."
   GPIO.output(LED, GPIO.HIGH)
   time.sleep(1.5)
   print "Setting led to off..."
   GPIO.output(LED, GPIO.LOW)
   time.sleep(1.5)

GPIO.cleanup()