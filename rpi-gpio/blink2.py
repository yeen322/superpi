from gpiozero import LED
from time import sleep

led = LED(23)

try:
    while True:
        print("On")
        led.on()
        sleep(10)
        print("Off")
        led.off()
        sleep(10)
except KeyboardInterrupt:
    print("I'm done!")
finally:
    pass # led.off()