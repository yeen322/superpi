# led-strip1.py
from time import sleep
import board

import neopixel

pixel_pin = board.D10
num_pixels = 4

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

pixels.fill((0, 255, 255))
pixels.show()
sleep(2)

pixels[0] = (255, 0, 0)
pixels[1] = (255, 255, 0)
pixels[2] = (60,179,113)
pixels[3] = (70,130,180)

pixels.show()
sleep(2)
