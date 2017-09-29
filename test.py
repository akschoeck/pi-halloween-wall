import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18, True)
time.sleep(1)
GPIO.output(18, False)
time.sleep(1)

print('Enter a Letter')
letter = sys.stdin.readline()
if 's' in letter:
	GPIO.output(18, True)
	time.sleep(1)
	GPIO.output(18, False)