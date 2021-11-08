from machine import Pin
from utime import sleep
import micropython 


class Rotary:
    ROT_CW = 1
    ROT_CCW = 2
    SW_PRESS = 4
    SW_RELEASE = 8
    
    def __init__(self, dt, clk, sw):
        self.dt_pin = Pin(dt, Pin.IN)
        self.clk_pin = Pin(clk, Pin.IN)
        self.sw_pin = Pin(sw, Pin.IN)
        self.last_status = (self.dt_pin.value() << 1) | self.clk_pin.value()
        self.dt_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
        self.clk_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
        self.sw_pin.irq(handler=self.switch_detect, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
        self.handlers = []
        self.last_button_status = self.sw_pin.value()
        
    def rotary_change(self, pin):
        new_status = (self.dt_pin.value() << 1) | self.clk_pin.value()
        if new_status == self.last_status:
            return
        
        transition = (self.last_status << 2) | new_status
        try:
            if transition == 0b1110:
                micropython.schedule(self.call_handlers, Rotary.ROT_CW)
            elif transition == 0b1101:
                micropython.schedule(self.call_handlers, Rotary.ROT_CCW)
            self.last_status = new_status
        except RuntimeError:
            pass
        
    def switch_detect(self, pin):
        if self.last_button_status == self.sw_pin.value():
            return
        self.last_button_status = self.sw_pin.value()
        if self.sw_pin.value():
            micropython.schedule(self.call_handlers, Rotary.SW_RELEASE)
        else:
            micropython.schedule(self.call_handlers, Rotary.SW_PRESS)
    
    def add_handler(self, handler):
        self.handlers.append(handler)
    
    def call_handlers(self, type):
        for handler in self.handlers:
            handler(type)
