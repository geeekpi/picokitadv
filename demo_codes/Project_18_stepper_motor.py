from machine import Pin
import utime


pins = [
    Pin(15, Pin.OUT), #IN1
    Pin(14, Pin.OUT), #IN2
    Pin(16, Pin.OUT), #IN3
    Pin(17, Pin.OUT)  #IN4
    ]

full_step_sequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
    ]

while True:
    for step in full_step_sequence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep(0.001)