from machine import Pin, I2C, ADC
from machine_i2c_lcd import I2cLcd
import utime as time
import mpu6050
import math
import time
# LCD1602 I2C
lcd_bus = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
addr = lcd_bus.scan()[0]
lcd = I2cLcd(lcd_bus, addr, 2, 16)
lcd.putstr("WELCOME TO PICO\n")
time.sleep(1)
lcd.clear()
# MPU6050 I2C 
mpu6050_bus = I2C(1, scl=Pin(15), sda=Pin(14))
imu_data = {}
imu = mpu6050.accel(mpu6050_bus)
datax = 0
datay = 0
dataz = 0
gAnglex = 0
gAngley = 0
yaw = 0
pitch = 0
roll = 0


while True:
    imu_data = imu.get_values()
   
    accx =  (imu_data['AcX'] ) / 131.0
    accy =  (imu_data['AcY'] ) / 131.0
    accz =  (imu_data['AcZ'] ) / 131.0
     
    gyx = imu_data['GyX'] / 131.0 + 0.56
    gyy = imu_data['GyY'] / 131.0 - 2
    gyz = imu_data['GyZ'] / 131.0 + 0.79
    
    lcd.putstr("X:{:.2f} Y:{:.2f}\n".format(gyx, gyy))
    lcd.putstr("Z:{:.2f}".format(gyz))
    time.sleep(2)
    lcd.clear()
