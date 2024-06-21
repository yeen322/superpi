import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 23
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        print("On")
        GPIO.output(LED, GPIO.HIGH)
        sleep(1)
        print("Off")
        GPIO.output(LED, GPIO.LOW)
        sleep(1)
except KeyboardInterrupt:
    print("I'm done!")
finally:
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()
