from machine import Pin
from time import sleep


light_sensor = Pin(0, Pin.IN)

while True:
    if light_sensor.value() == 1:
        print("light detected.")
        sleep(0.2)
    else:
        print("NO Light detected.")
        sleep(0.2)