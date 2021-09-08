#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__status__  = "Development"
__date__    = "Late Updated: 2021-09-08"
__doc__     = "Pin definition and control on a "
"""


class L298:

A_IN_1 = GC.L298_FORWARD_DIRECTION_PIN
A_IN_2 = GC.L298_BACKWARD_DIRECTION_PIN
A_ENABLE = GC.L298_ENABLE_PIN
A_IN_1 = GC.L298_FORWARD_DIRECTION_PIN
A_IN_2 = GC.L298_BACKWARD_DIRECTION_PIN
B_ENABLE = GC.L298_ENABLE_PIN 

def __init__(self):
    self.A_IN_1 = GC.PRODUCT_LIST[0] 
    self.A_IN_2 = GC.PRODUCT_LIST[1] 
    self.A_ENABLE = GC.PRODUCT_LIST[2] 
    self.B_IN_1 = GC.PRODUCT_LIST[3] 
    self.B_IN_2 = GC.PRODUCT_LIST[4] 
    self.B_ENABLE = GC.PRODUCT_LIST[5] 


def openOutlet(outletList, outletNumber=GC.NULL):
    if(outletNumber != GC.NULL):
       outletList[outletNumber]
    else:
        numOfOutlets = len(outlerList)
        for i in range(0, numOfOutlets

def liftDesk(move):
    if(move == True):
    

def lowerDesk(move):
    if(move == True):
    
