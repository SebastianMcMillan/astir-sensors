import time
from grove.grove_led import GroveLed
from grove.grove_light_sensor_v1_2 import GroveLightSensor

ledPin = 5
led2Pin = 16
led3Pin = 18
sensorPin = 0


sensor = GroveLightSensor(sensorPin)
led = GroveLed(ledPin)
led2 = GroveLed(led2Pin)
led3 = GroveLed(led3Pin)

led.off()
led2.off()
led3.off()
time.sleep(.1)
led.on()
led2.on()
led3.on()
time.sleep(.1)
led.off()
led2.off()
led3.off()
time.sleep(.1)
led.on()
led2.on()
led3.on()
time.sleep(.1)
led.off()
led2.off()
led3.off()

while True:
	if sensor.light < 300:
		led.on()
		led2.on()
		led3.on()
	else:
		led.off()
		led2.off()
		led3.off()
	time.sleep(1)
