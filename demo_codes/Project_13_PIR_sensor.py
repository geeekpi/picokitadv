from machine import Pin
import utime
from time import sleep

# Connect GP16 to PIR sensor's OUT pin), please use 3.3V connect to VCC on PIR sensor.
pir = Pin(16, Pin.IN, Pin.PULL_UP)


while True:
    print(pir.value())
    sleep(0.1)
    
    
