from machine import Pin
import time


Green_LED = Pin(0, Pin.OUT)
Red_LED = Pin(1, Pin.OUT)


while True:
    Green_LED.toggle()
    time.sleep(1)
    Red_LED.toggle()
    time.sleep(1)


