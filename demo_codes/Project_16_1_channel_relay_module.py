from machine import Pin
from time import sleep

# GP4 - IN 
relay_pin = Pin(4, Pin.OUT)

while True:
    print("turn on relay!")
    relay_pin.value(1)
    sleep(5)
    print("turn off relay!")
    relay_pin.value(0)
    sleep(5)