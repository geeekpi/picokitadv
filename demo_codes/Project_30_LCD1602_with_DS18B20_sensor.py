from machine import Pin, I2C
import onewire
import ds18x20
import time
from machine_i2c_lcd import I2cLcd

# GP0 - SDA, GP1 - SCL
i2c_bus = I2C(0, scl=Pin(1), sda=Pin(0), freq=2000000)

# get address of i2c deivce
addr = i2c_bus.scan()[0]

# create object i2clcd
lcd = I2cLcd(i2c_bus, addr, 2, 16) # 2 line, 16 characters

# draw greetings
lcd.putstr("Hello RPi Pico!\n")

ds_pin = Pin(16) # GP16 - DS18B20's OUT Pin

# create ds_sensor object via onewire protocol
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print("Found a ds18x20 device")

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        #print(ds_sensor.read_temp(rom))
        lcd.putstr("DS18B20 Detect\n")
        lcd.putstr("Temp: {:.2f}\n".format(ds_sensor.read_temp(rom)))
        time.sleep(3)
        lcd.clear()  # clear screen.
    




