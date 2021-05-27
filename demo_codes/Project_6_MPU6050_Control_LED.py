from machine import Pin, I2C
from time import sleep
import mpu6050
import math
import time


upper_led = Pin(2, Pin.OUT)
lower_led = Pin(1, Pin.OUT)
left_led = Pin(0, Pin.OUT)
right_led = Pin(3, Pin.OUT)

imu_data = {}

imui2c = I2C(1, scl=Pin(15), sda=Pin(14))

imu = mpu6050.accel(imui2c)

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
        print("x:" + str(x))
        upper_led.value(1)
        lower_led.value(0)
    else:
        x = int(64 + pitch * 10)
        print("x:" + str(x))
        upper_led.value(0)
        lower_led.value(1)
    if roll >=0:
        y = int(32 + roll * 10)
        print("y:" + str(y))
        left_led.value(1)
        right_led.value(0)
    else:
        y = int(32 + roll * 10)
        print("y:" + str(y))
        left_led.value(0)
        right_led.value(1)
    sleep(0.001)
    

