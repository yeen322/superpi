import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BUTTON = 24
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(BUTTON) == True:
            print("You pressed the button")
        sleep(0.1)
except KeyboardInterrupt:
    print("I'm done!")
finally:
    GPIO.cleanup()
