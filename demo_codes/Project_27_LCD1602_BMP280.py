from machine import Pin, I2C, ADC
import utime as time
from bmp280 import *
from machine_i2c_lcd import I2cLcd

# LCD1602 I2C
lcd_bus = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
addr = lcd_bus.scan()[0]
lcd = I2cLcd(lcd_bus, addr, 2, 16)
lcd.putstr("WELCOME TO PICO\n")
time.sleep(1)
lcd.clear()
# BMP280 I2C 
bmp_bus = I2C(1, scl=Pin(15), sda=Pin(14), freq=200000)
 
bmp = BMP280(bmp_bus)

bmp.use_case(BMP280_CASE_WEATHER)
bmp.oversample(BMP280_OS_HIGH)

bmp.temp_os = BMP280_TEMP_OS_8
bmp.press_os = BMP280_PRES_OS_4

bmp.standby = BMP280_STANDBY_250
bmp.iir = BMP280_IIR_FILTER_2

bmp.spi3w = BMP280_SPI3W_ON
# or 
bmp.force_measure()

bmp.power_mode = BMP280_POWER_NORMAL
# or 
bmp.normal_measure()

bmp.power_mode = BMP280_POWER_SLEEP
# or 
bmp.sleep()


while True:
    temp = bmp.temperature
    press = bmp.pressure
    lcd.putstr("TEMP:{}\n".format(temp))
    lcd.putstr("Pascal:{}".format(press))
    time.sleep(2)
    lcd.clear()
