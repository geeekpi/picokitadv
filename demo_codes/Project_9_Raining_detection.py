from machine import Pin, ADC
from time import sleep


water_sensor_DO = Pin(0, Pin.IN)
water_sensor_ADC = ADC(0) # GPI26

while True:
    if water_sensor_DO.value() == 0:
        print("It is raining: {}".format(water_sensor_ADC.read_u16()))
        sleep(0.5)
    else:
        print("It is not raining...")
        sleep(0.5)