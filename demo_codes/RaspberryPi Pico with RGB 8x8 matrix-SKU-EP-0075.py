from machine import Pin, SPI
from time import sleep

RED = 0
BLUE = 1
GREEN = 2

# SPI(0, baudrate=992063, polarity=0, phase=0, bits=8, sck=6, mosi=7, miso=4)  SCK-> GP6, MOSI-> GP7, MISO-GP4(Not connect)
bus = SPI(0)
print(bus)
CE = Pin(5, Pin.OUT)
data = bytearray([0,0,0,0])
#heart = [0x00, 0x66, 0xff,0xff,0xff, 0x7e, 0x3c, 0x18]
heart = [0xC3, 0x42, 0x3C, 0x42, 0xA5, 0x5A, 0x7E, 0x81]
heart2 = [0xC3, 0x42, 0x3C, 0x42, 0x99, 0x42, 0x66, 0x99]
CE.value(0)
while True:
    
    for j in range(0, 8):
        data[0] = ~heart[j] #red 
        data[1] = 0xff      # blue
        data[2] = 0xff      # green
        data[3] = 0x01 << j # COM, GND
        
        CE.value(0)
        bus.write(bytearray(data))
        #bus.write_readinto(bytearray(data), bytearray(4))
        CE.value(1)
        sleep(0.001)
    for j in range(0, 8):
        data[0] = 0xff
        data[1] = ~heart2[j]
        data[2] = 0xff
        data[3] = 0x01 << j
        CE.value(0)
        bus.write(bytearray(data))
        CE.value(1)
        sleep(0.001)
        
