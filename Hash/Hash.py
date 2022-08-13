#
# Author ------- Shuber Ali Mirza
# Hash.py ------ Contains classes for hash table
# Created ------ 27/FEB/2021
# Last Updated - 28/FEB/2021
#

import numpy as np
from math import *
from linked_list import *


class DSAHashEntry():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return 'Key: ' + self.key + '  Value: ' + str(self.value)

class DSAHashTable(DSAHashEntry):
    def __init__(self, size=11):
        self.size = size
        self.count = 0
        self.table = np.zeros(self.size, dtype=object)
        for i in range(self.size):
            self.table[i] = DSALinkedList()
    
    def _hashFunc(self, key):
        keyASCII = 0
        for i in key:
            keyASCII += ord(i)
        index = keyASCII % self.size
        return index
    
    def resize(self):
        length = self.size
        self.size = self._findPrime(self.size*2)
        length = self.size - length
        new = np.zeros(length, dtype=object)
        for i in range(length):
            new[i] = DSALinkedList()
        self.table = np.append(self.table, new)
        
        for index in self.table:
            for item in index:
                if item != None:
                    self._putAfterResize(item.key, item.value)
                    index.removeMid(item)
                    self.count -= 1
        
    def _findPrime(self, startVal):
        primeVal = 0
        if startVal % 2 == 0:
            primeVal = startVal - 1
        else:
            primeVal = startVal
            
        isPrime = False
        while isPrime == False:
            primeVal += 2
            i = 3
            isPrime = True
            rootVal = sqrt(primeVal)
            while  (i <= rootVal) and (isPrime == True):
                if primeVal % i == 0:
                    isPrime = False
                else:
                    i += 2
        return primeVal
    
    def _putAfterResize(self, key, val):
        new = DSAHashEntry(key, val)
        index = self._hashFunc(key)
        while (self.count / self.size > 0.7):
            self.resize()
        self.table[index].insertLast(new)
        self.count += 1
    
    def put(self, key, val):
        if self.hasKey(key) == False:
            new = DSAHashEntry(key, val)
            index = self._hashFunc(key)
            while (self.count / self.size > 0.7):
                self.resize()
            self.table[index].insertLast(new)
            self.count += 1
        else:
            print(key, 'present')
        
    def get(self, key):
        val = None
        try:
            index = self._hashFunc(key)
            for i in self.table[index]:
                if i != None and i.key == key:
                    val = i
        except:
            val = None
        return val
    
    def hasKey(self, key):
        try:
            has = False
            index = self._hashFunc(key)
            for i in self.table[index]:
                if i.key == key:
                    has = True
        except:
            has = False
        return has
    
    def removeKey(self, key):
        try:
            if self.hasKey(key) == False:
                raise Exception
            index = self._hashFunc(key)
            for i in self.table[index]:
                if i != None and i.key == key:
                    self.table[index].removeMid(i)
            self.count -= 1
        except Exception:
            print('ERROR -', key, 'not present')
        
    def printHash(self):
        for i in self.table:
            if i != None:
                for item in i:
                    if item != None:
                        print('Index:', self._hashFunc(item.key), item)
