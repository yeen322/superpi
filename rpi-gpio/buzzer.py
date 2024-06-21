from gpiozero import PWMOutputDevice
from time import sleep

pwm_device = PWMOutputDevice(pin=12, frequency=100, initial_value= 0.5)

tones = [261, 294, 329, 349, 392, 440, 493, 523]
music = [4, 4, 5, 4, 4, 2, 4, 4, 2, 2, 1]
term = [0.5, 0.5,0.5,0.5,0.5,0.5, 1, 0.5,0.5,0.5,0.5,1]

try:
	for i in range(len(music)):
		pwm_device.frequency = tones[music[i]]
		pwm_device.value = 0.5 # 50% duty cycle
		sleep(term[i])
		pwm_device.value=0
finally:
	pwm_device.close()