from rotary import Rotary
import utime as time
from machine import Pin, I2C 
from ssd1306 import SSD1306_I2C
import framebuf

WIDTH = 128
HEIGHT = 64

buffer = bytearray(b'\x00\x00\x00\x00\x01\xf0\x0f\x00\x06\x860\xb0\x04\x01@\x10\x04\x01\x000\x02\x10\x89 \x02\x05\xd2 \x01\x03\xe0@\x01\x87\xe0\x80\x10~?\x00\x00\x88\x11\x80\x01\x18\x08@\x02><@\x02a\xc3@C\xc1\x81\xe0\x05\x80\x90\x91\x08\x80\x80\x98\x08\x81\xc0\x88\t\x83\xe1\x98)\xe4\x1f\x98\x07\xf8\x0e0\x068\x0c \x02\x18\x080\x02\x88\x08 \x03\x0e0A\x01\x8f\xf8\x80\x00|\x1f\x00\x008\x0c\x00\x00\x0c0\x02\x00\x03\xe0\x00\x00\x00\x80\x00\x01\x00\x00\x04')

fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

i2c = I2C(1, scl=Pin(15), sda=Pin(14),freq=200000)

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# clear screen
oled.fill(0)
oled.blit(fb, 64, 32)
oled.show()
time.sleep(1)
oled.fill(0)
rotary = Rotary(0, 1, 2)

val = 0

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val += 10
        oled.blit(fb, val, 32)
        oled.show()
        time.sleep(0.2)
        oled.fill(0)
        print(val)
    elif change == Rotary.ROT_CCW:
        val -= 10
        oled.blit(fb, val, 32)
        oled.show()
        time.sleep(0.2)
        oled.fill(0)
        print(val)
    elif change == Rotary.SW_PRESS:
        val += 20
        oled.blit(fb, 64, val)
        oled.show()
        time.sleep(0.2)
        oled.fill(0)
    elif change == Rotary.SW_RELEASE:
        val -= 20
        oled.blit(fb, 64, val)
        oled.show()
        time.sleep(0.2)
        oled.fill(0)
        
rotary.add_handler(rotary_changed)


while True:
    time.sleep(0.1)