from machine import Pin, ADC
from time import sleep
 
 
led = Pin(0, Pin.OUT)
# GP26 -> ADC0
sound_sensor = ADC(0)


while True:
    if sound_sensor.read_u16() > 65500:
        print("No Sound Detected!")
        led.value(0)
        sleep(2)
    elif sound_sensor.read_u16() < 9000:
        print("Sound Detected!")
        sleep(0.5)
        led.value(1)    
    