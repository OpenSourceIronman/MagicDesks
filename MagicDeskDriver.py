#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "Standing Strong Desks"
__status__  = "Development"
__date__    = "Late Updated: 2021-08-25"
__doc__     = "Entry point to manage all Magic Desk high level tasks"
"""
# Unrestricted access to hardware specific functions for CPU, bluetooth, etc
# https://docs.micropython.org/en/latest/library/machine.html
from machine import Pin

# Interact with software I2C, hardware I2C, and OneWire serial intetfaces
# TODO REMOVE ONE OF THREE
from machine import SoftI2C, I2C, onewire

# Allow interaction with capacitive touch pads
# TODO
from machine import TouchPad

# Interface with Parallax LASER rangefinder SKU #2801
from LaserPING import *

# Small and fast JSON encoder and decoder for RESTful API communication
# https://pypi.org/project/ujson/
import ujson

# Allow interaction with O/S debugging and flash storage
# TODO
import esp
import uos

# Allow interaction with subsystem within ESP-32 module (e.g. Temp sensor)
# TODO
import esp32
from esp32 import NVS  # Non-volatile memory storage

import network
import ubluetooth

# Allow
# TODO
import time

# Access internally developed libraries
try:
    # Generate a timestamped .txt data logging file and custom terminal debugging output
    from Debug import *
    
    # Useful global constants used across all TesMuffler code
    import GlobalConstant as GC
    #TODO
    
except ImportError:
    print("Debug.py, GlobalConstant.py, or TODO.py didn't import correctly")
    print("Please verify that those files are in same directory as the MagicDeskDriver.py")
    #TODO

DEBUG_STATEMENTS_ON = True

# Allow micropython to run on ESP-32
# https://docs.micropython.org/en/latest/esp32/tutorial/intro.html
# https://micropython.org/download/esp32

def unitTest():

    ledPin = machine.Pin(0, machine.Pin.OUT, value=LOW) #GPIO0
    ledPin.on()
    ledPin.off()
    ledPin.value(HIGH)

    gpio_1 = Pin(1, Pin.IN, Pin.PUL_UP)
    print(gpio_1)
    
    time.sleep_us(10)   # 10 microseconds
    time.sleep_ms(5)    # 5 microseconds

    esp32.hall_senor()  # Model M magentic sensor
    esp32.ULP()         # Ultra low power co-processor 

    i2c = I2C(freq=400000)
    i2c.scan()

    i2c.writeto(42, b'123')         # write 3 bytes to slave with 7-bit address 42
    i2c.readfrom(42, 4)             # read 4 bytes from slave with 7-bit address 42

    i2c.readfrom_mem(42, 8, 3)      # read 3 bytes from memory of slave 42,
                                    #   starting at memory-address 8 in the slave
    i2c.writeto_mem(42, 2, b'\x10') # write 1 byte to memory of slave 42
                                    #   starting at address 2 in the slave

def getDistance():

    # https://docs.micropython.org/en/latest/library/machine.html#machine.time_pulse_us
    machine.time_pulse_us(TesMufflerDrice.LASER_PIN, TIME_HIGH_PULSE, LASER_TIMEOUT)

TODO = -1

def restart(time):
    time.sleep(time)
    machine.soft_reset()

def pollUpButton(selectedPin):
    return selectedPin.value

def pollDownButton(selectedPin):
    return selectedPin.value

def pollMagicTouchSensors(sensor1, sensor2):
    if(somethingPluggedIntoOutlet()):
        break
    
    if(sensor1.value or sensor2.value):
        time.sleep(GC.TOUCH_SENSOR_DELAY)
        if(sensor1.value):
            openOutlet()
        elif(sensor2.value)
            openOutlet()
    else:
        time.sleep(GC.MIN_TIMESTAMP)

def main(args=mode):                
    
    # See GlobalConstants.py for GPIO pin number definitions
    activeLowErrorLED = machine.Pin(GC.ERROR_LED_PIN, machine.Pin.OUT, value=HIGH)
    
    upButton = machine.Pin(GC.UP_BUTTON_PIN, Pin.IN, Pin.PUL_UP)
    bottomButton = machine.Pin(GC.DOWN_BUTTON_PIN, Pin.IN, Pin.PUL_UP)
    holdButton = machine.Pin(GC.HOLD_BUTTON_PIN, Pin.IN, Pin.PUL_UP) 
    
    leftMagicTouch = machine.Pin(GC.LEFT_MAGIC_TOUCH_PIN, Pin.???)
    rightMagicTouch = machine.Pin(GC.RIGHT_MAGIC_TOUCH_PIN, Pin.???)
    
    # Infinite loop that is only exitted for main problem requiring a restart
    # The ErrorLED is TURNED on by the off() since it's hardware to ALWAYS be on unless software is TURNING it OFF
    ok = True
    while(ok):
        holdOn = holdButton.value
        if(holdOn == False):
            pollUpButton(upButton)
            pollDownButton(downButton)
        
        pollMagicTouchSenors() #Start this in a new thread to keep up and down button polling faster then GC.TOUCH_SENSOR_DELAY neeed to reduce touch sensor misfires
        
    activeLowErrorLED.off() #TURNS ON LED

if __name__ == "__main__":
    machine.freq(GC.MAX_CPU_FREQ)
    
    uuid = machine.unique_id()
    if(mode==GC.DEVELOPMENT ot mode==GC.TESTING): 
        if(DEBUG_STATEMENTS_ON): 
            print("UUID = ", uuid)
            print("CPU frequency = ", machine.freq())
        unitTest()

    main(GC.DEVELOPMENT)
    