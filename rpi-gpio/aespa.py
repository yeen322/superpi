from gpiozero import PWMOutputDevice
from time import sleep

pwm_device = PWMOutputDevice(pin=12, frequency=100, initial_value= 0.5)

tones = [523,587,659,698,784,880,988,1047,1175,1319,1397,1480,0]
music = [4,9, 6, 4,12,12,4, 6, 9, 6,4,2,6,6,6, 6,6,7,7,7,7,7,6,12,4,4,4,4,4,4,7,7,7,5,7,6,9,9,9,9,9,9,9,11,11,11,8,11,9,12,9,9,9,9,9,9,9,8,8,8,8,8,8,11,9,12,2,2,4,2,2,4,4,2,4,12,2,2,4,2,2,4,4,2,4]
term = [1,0.5, 0.5, 0.5,1.5,0.5, 0.25, 0.25, 0.5, 0.5,0.25, 0.25,0.25,0.25,0.5,0.25,0.25, 0.5,0.25,0.25,0.5,0.25,0.25,0.25,0.25, 0.25,0.25,0.5,0.25,0.25, 0.5,0.25,0.25,0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.5,0.25,0.25,0.5,0.25,0.25,0.5,0.25,0.25,0.25, 0.25,0.25,0.25, 0.25,0.25,0.25,0.125,0.125,0.25,0.25,0.25,0.25,0.5,0.25,0.25,0.25, 0.125,0.125,0.25,0.125,0.125,0.25,0.25,0.375,0.125,0.25, 0.125,0.125,0.25,0.125,0.125,0.25,0.25,0.375,0.125]
try:
	for i in range(len(music)):
		pwm_device.frequency = tones[music[i]]
		pwm_device.value = 0.5 # 50% duty cycle
		sleep(term[i])
		
		pwm_device.value=0
finally:
	pwm_device.close()