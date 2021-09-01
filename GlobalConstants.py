#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-09-01"
__doc__     = "Useful global constants used across all Standing Strong Desks code"
"""


class GlobalConstant:

    # Desk model name CONTSTANTS
    MAGIC_DESK_V0 = 0

    # Aluminium color CONTSTANTS 
    PRODUCT_RED = 0xB00D23
    APPLE_WHITE = 0XFEFEFE
    SPACE_GREY = 0x110022
    
    # Moving hardware CONTSTANTS
    LEFT_LINEAR_ACUTATOR = 0        # Acutator to left of user whil facing deck from normal front
    RIGHT_LINEAR_ACUTATOR = 0       # Acutator to right of user whil facing deck from normal front
    DEFAULT_MAX_TRAVEL = 69         # Units are in millimeters
    MIN_TIMESTEP = 0.001            # Units are seconds
    
    # User Interface CONSTANTS
    UI_TERMINAL_DELAY = 0.1         # Units are seconds
    MAX_UI_DEALY = 2.0              # Units are seconds
    FUNCTION_DELAY = 0.005          # Units are seconds
