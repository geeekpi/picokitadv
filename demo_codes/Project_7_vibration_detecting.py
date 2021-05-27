from machine import Pin
from time import sleep


vibration_pin = Pin(1, Pin.IN, Pin.PULL_UP)
red_led = Pin(0, Pin.OUT)
blue_led = Pin(2, Pin.OUT)

try:
    while True:
        if vibration_pin.value() == 1:
            red_led.value(1)
            blue_led.value(0)
            sleep(1)
            red_led.value(0)
        elif vibration_pin.value() == 0:
            print(vibration_pin.value())
            red_led.value(0)
            blue_led.value(1)
except KeyboardInterrupt:
    print("BYE")