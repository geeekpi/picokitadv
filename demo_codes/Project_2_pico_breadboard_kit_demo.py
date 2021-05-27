from machine import Pin
from time import sleep

# initial pin 
btn1 = Pin(0, Pin.IN, Pin.PULL_UP)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
btn1_status = 0

while True:
    btn1_status = btn1.value()
    if btn1.value() == 1:
        led1.value(1)
        led2.value(0)
    else:
        led1.value(0)
        led2.value(1)
    sleep(0.02)

 