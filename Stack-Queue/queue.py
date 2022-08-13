#
# Author ------- Shuber Ali Mirza
# Created ------ 28/JAN/2021
# Last Updated - 29/JAN/2021
#

from super_class import *

class Queue(SUPER):
    def enqueue(self , v):
        try:
            if self.isFull() == True:
                raise Exception
            else:
                self.l.append(v)
                self.count += 1
        except Exception:
            print('ERROR - Queue is already full')
               
    def dequeue(self):
        try:
            frontVal = self.peek()
            del self.l[0]
            self.count -= 1
        except:
            None
        return frontVal
            
    def peek(self):
        try:
            frontVal = None
            if self.isEmpty() == True:
                raise Exception
            else:
                frontVal = self.l[0]
        except Exception:
            print('ERROR - Queue is empty')
        return frontVal
