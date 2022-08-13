#
# Author ------- Shuber Ali Mirza
# queue.py ----- Contains DSAQueues, DSAShufflingQueue and DSACircularQueue classes. Uses linked list
# Created ------ 28/JAN/2021
# Last Updated - 6/FEB/2021
#

from super_class import *

class DSAQueue(DSAADS):
    def enqueue(self , v):
        try:
            if self.isFull() == True:
                raise Exception
            else:
                self.l.insertLast(v)
                self.count += 1
        except Exception:
            print('ERROR - Queue is already full')
               
    def dequeue(self):
        try:
            frontVal = self.peek()
            self.l.removeFirst()
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
                frontVal = self.l.peekFirst()
        except Exception:
            print('ERROR - Queue is empty')
        return frontVal
    
class DSAShufflingQueue(DSAQueue):
    pass

class DSACircularQueue(DSAQueue):
    pass
