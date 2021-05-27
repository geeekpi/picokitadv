from machine import Pin, PWM
import utime


# GP14 -> Trigger, GP15 -> Echo
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)

buzzer = PWM(Pin(16))
buzzer.freq(1000)
# define a function
def measure_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

 
while True:
    dist = measure_distance()
    print(round(dist))
    if dist <= 10:
        buzzer.duty_u16(2100)
        utime.sleep(0.01)
    else:
        buzzer.duty_u16(0)
        utime.sleep(0.01)

    