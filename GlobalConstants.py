#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-09-04"
__doc__     = "Useful global constants used across all Standing Strong Desks code"
"""


class GlobalConstant:

    # Desk model name CONTSTANTS
    MAGIC_DESK_V0 = 0
    
    # GPIO pin CONSTANTS
    # https://randomnerdtutorials.com/esp32-pinout-reference-gpios
    # Available Pins are from the following ranges (inclusive): 0-19, 21-23, 25-27, 32-39. 
    # Pins 1 and 3 are REPL UART TX and RX respectively
    # Pins 6, 7, 8, 11, 16, and 17 are used for connecting the embedded flash, and are not recommended for other uses
    # Pins 34-39 are input only, and also do not have internal pull-up resistors
    # The pull value of some pins can be set to Pin.PULL_HOLD to reduce power consumption during deepsleep.
    
    UP_BUTTON_PIN = 34          # Input only pin
    DOWN_BUTTON_PIN = 35        # Input only pin
    HOLD_BUTTON_PIN = 36        # Input only pin
    ERROR_LED_PIN = 2           # Also connected to an onboard LED
    LEFT_MAGIC_TOUCH_PIN = 32   # Connect to Internal touch sensor 
    RIGH_MAGIC_TOUCH_PIN = 33   # Connect to internal touch sensor
    LASER_PIN = 27              # Input & Output to send and recieve pusle                   
    L298P_ENABLE_PIN = 
    L298P_DIRECTION_PIN = 
    
    # LASER CONSTANTS    
    TIME_HIGH_PULSE = 1
    TIME_LOW_PULSE = 0
    LASER_TIMEOUT = 0.001 # 1 ms = ?? meters in light Time Of Flight

    # Aluminium color CONTSTANTS 
    PRODUCT_RED = 0xB00D23
    APPLE_WHITE = 0XFEFEFE
    SPACE_GREY = 0x110022
    
    # Code run mode CONSTANTS
    PRODUCTION = 0
    TESTING = 1
    DEVELOPMENT = 2
    
    # Moving hardware CONTSTANTS
    LEFT_LINEAR_ACUTATOR = 0        # Acutator to left of user whil facing deck from normal front
    RIGHT_LINEAR_ACUTATOR = 1       # Acutator to right of user whil facing deck from normal front
    DEFAULT_MAX_TRAVEL = 45         # Units are in centimeters
    MIN_TIMESTEP = 0.001            # Units are seconds
    
    # User Interface CONSTANTS
    UI_TERMINAL_DELAY = 0.1         # Units are seconds
    MAX_UI_DEALY = 2.0              # Units are seconds
    FUNCTION_DELAY = 0.005          # Units are seconds
    TOUCH_SENSOR_DELAY = 1.2        # Units are seconds
    HIGH = 1
    LOW = 0
    NULL = -1
        
    # CPU CONSTANTS
    MAX_CPU_FREQ = 80000000         # 80 MHz
    USB_2_FREQ = 48000000           # 48 MHz for 10 bits at 480 MHz
    AVERAGE_CPU_FREQ = 12000000     # 24 MHz
    MIN_CPU_FREQ = 6000000          # 6 MHz   TODO Deep Sleep for use on batteru power MIGHT need to be slower
