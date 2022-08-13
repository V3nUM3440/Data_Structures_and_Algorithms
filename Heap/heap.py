#
# Author ------- Shuber Ali Mirza
# heap.py ------ Contains classes for creating a heap
# Created ------ 6/MAR/2021
# Last Updated - 6/MAR/2021
#

import numpy as np

class HeapEntry():
    def __init__(self, inPriority, inValue):
        self.priority = inPriority
        self.value = inValue
        
    def __str__(self):
        return 'Priority: '+ str(self.priority) + '\tValue: ' + str(self.value)

class Heap(HeapEntry):
    def __init__(self, maxSize=10):
        self.maxSize = maxSize
        self.count = 0
        self.heap = np.zeros(self.maxSize, dtype=object)
        
    def _trickleUp(self, cur):
        parent = int((cur - 1) / 2)
        if cur > 0:
            if self.heap[cur].priority > self.heap[parent].priority:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[cur]
                self.heap[cur] = temp
                self._trickleUp(parent)
                
    def _trickleDown(self, cur, num):
        lChild = (cur * 2) + 1
        rChild = lChild + 1
        if lChild < num:
            large = lChild
            if rChild < num:
                if self.heap[lChild].priority < self.heap[rChild].priority:
                    large = rChild
            if self.heap[large].priority > self.heap[cur].priority:
                temp = self.heap[large]
                self.heap[large] = self.heap[cur]
                self.heap[cur] = temp
                self._trickleDown(large, num)
                
    def add(self, priority, value):
        new = HeapEntry(priority, value)
        self.heap[self.count] = new
        self._trickleUp(self.count)
        self.count += 1
        
    def remove(self):
        temp = self.heap[self.count-1]
        self.heap[self.count-1] = 0
        self.heap[0] = temp
        self._trickleDown(0, self.count-1)
        self.count -= 1
        
    def _heapify(self):
        ii = self.count - 1
        while ii != -1:
            self._trickleDown(ii, self.count - 1)
            ii -= 1
    
    def heapSort(self):
        self._heapify()
        ii = self.count - 1
        while ii != 0:
            temp = self.heap[0]
            self.heap[0] = self.heap[ii]
            self.heap[ii] = temp
            self._trickleDown(0, ii)
            ii -= 1

    def printit(self):
        for i in self.heap:
            if i != 0:
                print(i)
