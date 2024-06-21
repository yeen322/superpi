from time import sleep

from gpiozero import Button

button = Button(24, pull_up=False, bounce_time = 0.1)

def button_pressed():
	print("Button Pressed!")

button.when_pressed = button_pressed

try:
	i = 0
	while True:
		sleep(1)
		i = i+1
		print(i)

except KeyboardInterrupt:
	print("I'm done!")