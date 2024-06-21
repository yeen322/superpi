from time import sleep

import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D4)

try:
	while True:
		try:
			temperature = dht_device.temperature
			humidity = dht_device.humidity
			print(temperature, humidity) 
		except RuntimeError:
			sleep(1.0)

		sleep (2.0)

except KeyboardInterrupt:
	print("I'm done!")
finally:
	dht_device.exit()