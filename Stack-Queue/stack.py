#
# Author ------- Shuber Ali Mirza
# stack.py ----- Contains DSAStack class, uses linked list
# Created ------ 28/JAN/2021
# Last Updated - 6/FEB/2021
#

from super_class import *

class DSAStack(DSAADS):
    def push(self , x):
        try:
            if self.isFull() == True:
                raise Exception
            else:
                self.l.insertLast(x)
                self.count += 1
        except Exception:
            print('ERROR - Stack already full')
            
    def pop(self):
        try:
            topVal = self.top()
            self.l.removeLast()
            self.count -= 1
        except:
            None
        return topVal
        
    def top(self):
        try:
            topVal = None
            if self.isEmpty() == True:
                raise Exception
            else:
                topVal = self.l.peekLast()
        except Exception:
            print('ERROR - Stack is empty')
        return topVal