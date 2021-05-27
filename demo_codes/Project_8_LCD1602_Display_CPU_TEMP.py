from machine import Pin, I2C, ADC
from time import sleep, sleep_ms
from machine_i2c_lcd import I2cLcd
import utime


i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

addr = i2c.scan()[0]
# print(hex(addr[0]))

lcd = I2cLcd(i2c, addr, 2, 16)

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)
 


while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    lcd.putstr("Hello RPi Pico!\n")
    lcd.putstr("CPU Temp:%.2f" % temperature)
    utime.sleep(2)
    sleep(1)
    lcd.clear()
