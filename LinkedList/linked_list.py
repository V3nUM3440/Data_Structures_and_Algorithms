# 
# Author ------- Shuber Ali Mirza
# Created ------ 4/FEB/2021
# Last Updated - 6/FEB/2021
# 

# Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

class ListNode():
    def __init__(self , value):
        self.value = value
        self.next = None
        self.prev = None
        
    def getValue(self):
        return self.value
        
    def setValue(self , inValue):
        self.value = inValue
        
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setNext(self , newNext):
        self.next = newNext
    
    def setPrev(self , newPrev):
        self.prev = newPrev


class LinkedList(ListNode):
    
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        
    def isEmpty(self):
        empty = None
        if self.head.value == None or self.head == None:
            empty = True
        else:
            empty = False
        return empty
    
    def insertEmpty(self , inValue):
        if self.isEmpty() == True:
            self.head.setValue(inValue)
            self.tail = self.head
            print('Node inserted in empty list')
        else:
            print('ERROR - List not empty')
    
    def insertFirst(self , inValue):
        if self.isEmpty() == True:
            self.insertEmpty(inValue)
        else:
            new = ListNode(inValue)
            new.setNext(self.head)
            self.head.setPrev(new)
            self.head = new
            print('Node inserted at start')
            
    def insertLast(self , inValue):
        if self.isEmpty() == True:
            self.insertEmpty(inValue)
        else:
            new = ListNode(inValue)
            new.setPrev(self.tail)
            self.tail.setNext(new)
            self.tail = new
            print('Node inserted at end')
            
    def peekFirst(self):
        if self.head == None:
            result = None
        else:
            if self.head.getNext() == None:
                self.tail = self.head
                result = self.head.getValue()
            elif self.isEmpty() == True:
                result = None
            else:
                result = self.head.getValue()
            return result
    
    def peekLast(self):
        if self.tail == None:
            result = None
        else:
            if self.head.getNext() == None:
                self.tail = self.head
                result = self.tail.getValue()
            elif self.isEmpty() == True:
                result = None
            else:
                result = self.tail.getValue()
            return result
    
    def removeFirst(self):
        if self.head == None:
            print('ERROR - List is empty')
        elif self.isEmpty() == True:
            v = None
            print('ERROR - List is empty')
        elif self.head.getNext() == None:
            v = self.head.getValue()
            self.head.setValue(None)
            self.tail = self.head
            print('Removed' , v , 'from start of list')
        else:
            v = self.head.getValue()
            self.head = self.head.getNext()
            self.head.setPrev(None)
            print('Removed' , v , 'from start of list')
        return v
            
    def removeLast(self):
        if self.head == None:
            print('ERROR - List is empty')
        elif self.isEmpty() == True:
            v = None
            print('ERROR - List is empty')
        elif self.head.getNext() == None:
            v = self.head.getValue()
            self.head.setValue(None)
            self.tail = self.head
            print('Removed' , v , 'from end of list')
        else:
            v = self.tail.getValue()
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
            print('Removed' , v , 'from end of list')
        return v
    
    def __iter__(self):
        self._cur = self.head
        self._val = self._cur.getValue()
        return self
    
    def __next__(self):
        curval = None
        if self._cur == None:
            raise StopIteration
        else:
            curval = self._cur.getValue()
            self._cur = self._cur.getNext()
        return curval
