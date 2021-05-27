from machine import Pin, I2C, 
from ssd1306 import SSD1306_I2C
from time import sleep
import mpu6050
import math
import time


WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height
imu_data = {}


i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=400000)
imui2c = I2C(1, scl=Pin(15), sda=Pin(14))

imu = mpu6050.accel(imui2c)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                   

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
    oled.fill(0)
    # oled.text("X:{}".format(imu_data['GyX']), 0, 0)
    # oled.text("Y:{}".format(imu_data['GyY']), 64, 0)
    # oled.text("Z:{}".format(imu_data['GyZ']), 0, 10)
    # oled.line(0,20, 128, 20,1)
    accx =  (imu_data['AcX'] ) / 131.0
    accy =  (imu_data['AcY'] ) / 131.0
    accz =  (imu_data['AcZ'] ) / 131.0
    
    # print(x, y, z)
    accAnglex = (math.atan(accy /math.sqrt(pow(accx, 2) + pow(accz, 2))) * 180 / math.pi) - 0.58
    accAngleY = (math.atan(-1 * accx / math.sqrt(pow(accy, 2) + pow(accz, 2))) * 180 / math.pi) + 1.58
     
    
    cTime = time.time()
    pTime = cTime
    eTime = (cTime - pTime) / 1000
    
    gyx = imu_data['GyX']   + 0.56
    gyy = imu_data['GyY']   - 2
    gyz = imu_data['GyZ']   + 0.79
    """
    gyx = imu_data['GyX'] / 131.0 + 0.56
    gyy = imu_data['GyY'] / 131.0 - 2
    gyz = imu_data['GyZ'] / 131.0 + 0.79
    """
    gAnglex = gAnglex + gyx * eTime
    gAngleY = gAngley + gyy * eTime
    

    roll = 0.96 * gAnglex + 0.04 * accx
    pitch = 0.96 * gAngley + 0.04 * accy
    
    # print(roll, pitch)
    
    if pitch >=0:
        x = int(64 + pitch * 10)
    else:
        x = int(64 + pitch * 10)
        
    if roll >=0:
        y = int(32 + roll * 10)
    else:
        y = int(32 + roll * 10)
        
    oled.text("Pico Kit", x, y ,1)
    
    """
    oled.text("AcX: {}".format(imu_data['AcX']), 0, 30)
    oled.text("AcY: {}".format(imu_data['AcY']), 15, 30)
    oled.text("AcZ: {})".format(imu_data['AcZ']), 30, 30)
    """
    oled.show()
    sleep(0.001)
    
