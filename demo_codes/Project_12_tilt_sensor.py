from machine import Pin
from time import sleep
 
 
led = Pin(0, Pin.OUT)
tilt_sensor = Pin(4, Pin.IN)

while True:
    if tilt_sensor.value() == 1:
        print("It is tilt...")
        led.value(1)
        sleep(0.02)
    else:
        print("It is not tilt...")
        led.value(0)
        sleep(0.02)