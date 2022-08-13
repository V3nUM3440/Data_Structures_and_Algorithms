#
# Author ------- Shuber Ali Mirza
# Created ------ 28/JAN/2021
# Last Updated - 28/JAN/2021
#

from super_class import *

class Stack(SUPER):
    def push(self , x):
        try:
            if self.isFull() == True:
                raise Exception
            else:
                self.l.append(x)
                self.count += 1
        except Exception:
            print('ERROR - Stack already full')
            
    def pop(self):
        try:
            topVal = self.top()
            del self.l[self.count - 1]
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
                topVal = self.l[self.count - 1]
        except Exception:
            print('ERROR - Stack is empty')
        return topVal
