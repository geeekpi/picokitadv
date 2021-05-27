from machine import Pin, ADC
from time import sleep
 
 
led = Pin(0, Pin.OUT)
# GP26 -> ADC0
sound_sensor = ADC(0)

def sound_map(read_value, in_min, in_max, out_min, out_max):
    return (read_value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

count = 0 
while True:
    sound_level = round(sound_map(sound_sensor.read_u16(), 0, 65535, 0, 255))
    if sound_level:
        print("Sound Level: ", sound_level)
        if sound_level > 100:
            print("Detect Noise!", count)
            led.value(1)
            count +=1
        else:
            led.value(0)
        sleep(0.3)
    