#
# Author --------- Shuber Ali Mirza
# super_class.py - Contains super class for DSAStacks and DSAQueues subclasses
# Created -------- 28/JAN/2021
# Last Updated --- 6/FEB/2021
#

import numpy as np
from linked_list import *

class DSAADS():
    DEFAULT_CAPACITY = 100
    
    def __init__(self):
        self.l = DSALinkedList()
        self.count = 0
        
    def getCount(self):
        return self.count
    
    def isEmpty(self):
        if self.count == 0:
            empty = True
        else:
            empty = False
        return empty
    
    def isFull(self):
        if self.count == self.DEFAULT_CAPACITY:
            full = True
        else:
            full = False
        return full
    
    def printArr(self):
        for i in self.l:
            print(i)