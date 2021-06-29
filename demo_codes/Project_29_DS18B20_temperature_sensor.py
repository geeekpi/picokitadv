import machine
import onewire
import ds18x20
import time

ds_pin = machine.Pin(16) # GP16 - OUT
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print("Found a ds18x20 device")

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(ds_sensor.read_temp(rom))
    time.sleep(2)
    