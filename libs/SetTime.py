from machine import I2C, Pin
from urtc import DS1307
import utime

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
rtc = DS1307(i2c)

year = int(input("Year: "))
month = int(input("Month:(Jan->1, Dec->12): "))
date = int(input("date: "))
day = int(input("day: (1-->monday, 2-->Tuesday...0-->Sunday): "))
hour = int(input("hour (24 Hour Format: "))
minute = int(input("minute: "))
second = int(input("Second: "))

now = (year, month, date, day, hour, minute, second, 0)
rtc.datetime(now)

while True:
    (year, month, date, day, hour, minute, second, p1) = rtc.datetime()
    utime.sleep(1)
    print(rtc.datetime())
