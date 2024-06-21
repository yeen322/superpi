import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
TRIG = 13
ECHO = 19
  
print("start")
 
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try :
    while True :
        GPIO.output(TRIG, False)
        time.sleep(0.5)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
 
        while GPIO.input(ECHO) == 0 :
            pulse_start = time.time()
 
        while GPIO.input(ECHO) == 1 :
            pulse_end = time.time()
 
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)
 
        print("Distance : ", distance, "cm")
except :
    GPIO.cleanup()
