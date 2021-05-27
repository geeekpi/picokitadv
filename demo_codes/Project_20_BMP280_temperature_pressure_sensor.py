from machine import Pin, I2C
from utime import sleep
from bmp280 import *


i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
print(i2c.scan())
bmp = BMP280(i2c)

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

print("temperature: ", bmp.temperature)
print("Pressure: ", bmp.pressure)

# True while measuring
# bmp.is_measuring
# True while copying data to registers
# bmp.is_updating