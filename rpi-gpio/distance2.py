from time import sleep

from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()
sensor = DistanceSensor(echo=19, trigger=13, pin_factory=factory)

try:
	while True:
		print("distance: ", round(sensor.distance *100, 2), "cm")
		sleep(1)
except KeyboardInterrupt:
	print("I'm Done!!")