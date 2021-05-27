from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=2000000)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.fill(0)

buffer=bytearray(b'\x00\x00\x00\x00\x01\xf0\x0f\x00\x06\x860\xb0\x04\x01@\x10\x04\x01\x000\x02\x10\x89 \x02\x05\xd2 \x01\x03\xe0@\x01\x87\xe0\x80\x10~?\x00\x00\x88\x11\x80\x01\x18\x08@\x02><@\x02a\xc3@C\xc1\x81\xe0\x05\x80\x90\x91\x08\x80\x80\x98\x08\x81\xc0\x88\t\x83\xe1\x98)\xe4\x1f\x98\x07\xf8\x0e0\x068\x0c \x02\x18\x080\x02\x88\x08 \x03\x0e0A\x01\x8f\xf8\x80\x00|\x1f\x00\x008\x0c\x00\x00\x0c0\x02\x00\x03\xe0\x00\x00\x00\x80\x00\x01\x00\x00\x04')

fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)


xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))

button = Pin(16, Pin.IN, Pin.PULL_UP)
offset = 0
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    
    xStatus = int(WIDTH/2 - 10)
    yStatus = int(HEIGHT/2 - 10)
    buttonStatus = 'not pressed'
    
    if xValue <= 600:
        xStatus -= 30
        if xStatus == 0:
            xStatus = 0
    elif xValue >= 60000:
        xStatus += 30
        if xStatus == WIDTH:
            xStatus = WIDTH
    if yValue <= 600:
        yStatus -= 30
        if yStatus == 0:
            yStatus = 0
    elif yValue >=60000:
        yStatus += 30
        if yStatus == HEIGHT:
            yStatus = HEIGHT
    if buttonValue == 0:
        buttonStatus = 'pressed'
     
    oled.blit(fb, xStatus, yStatus)
    oled.show()
    utime.sleep(0.1)
    oled.fill(0)
    utime.sleep(0.1)