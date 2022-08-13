#
# Author --------- Shuber Ali Mirza
# Created -------- 28/JAN/2021
# Last Updated --- 6/FEB/2021
#

import numpy as np
from ../LinkedList/linked_list import *

class SUPER():
    DEFAULT_CAPACITY = 100
    
    def __init__(self):
        self.l = LinkedList()
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
