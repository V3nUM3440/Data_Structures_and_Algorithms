#
# Author ------- Shuber Ali Mirza
# graphs.py ---- Contains class for graphs
# Created ------ 18/FEB/2021
# Last Updated - 22/FEB/2021
#

from ../LinkedList/linked_list import *
from ../Stack-Queue/queue import *
import numpy as np

class EmptyError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


class GraphVertex(ListNode):
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.links = LinkedList()
        self.visited = None
            
    def addLink(self, vertex):
        self.links.insertLast(ListNode(vertex.label))
        self.links.peekLast().setNext(vertex)
    
    def getLinks(self):
#         print('\nLinks of: ', self.label)
        for i in self.links:
            if i == None:
                print('No links')
            else:
                print(i.getValue())
    
    def __str__(self):
        return ('Label: ' + str(self.label) + ' Value: ' + str(self.value))


class Graph(GraphVertex):
    
    def __init__(self, directed):
        self.vertices = LinkedList()
        self.directed = directed
    
    def isEmpty(self):
        empty = False
        for i in self.vertices:
            if i == None:
                empty = True
        return empty
        
    def addVertex(self, label, value):
        try:
            for i in self.vertices:
                if i != None:
                    if i.label == label:
                        raise Exception
            self.vertices.insertLast(GraphVertex(label, value))
        except Exception:
            print('ERROR - Label already exists')
        
    def addEdge(self, label1, label2):
        try:
            if label1 == label2:
                raise ValueError
            elif self.isEmpty():
                raise EmptyError('')
            elif self.isAdjacent(label1, label2):
                raise Exception
            else:
                for i in self.vertices:
                    if i.label == label1:
                        for j in self.vertices:
                            if j.label == label2:
                                if self.directed == False:
                                    i.addLink(j)
                                    j.addLink(i)
                                else:
                                    i.addLink(j)
        except ValueError:
            print('ERROR - Edge cannot be added to same vertex')
        except EmptyError:
            print('ERROR - Graph empty')
        except Exception:
            print('ERROR - Edge already exists')
        
    
    def hasVertex(self, label):
        present = False
        try:
            if self.isEmpty():
                raise EmptyError('')
            else:
                for i in self.vertices:
                    if i.label == label:
                        present = True
        except EmptyError:
            print('ERROR - Graph empty')
        return present
    
    def vertexCount(self):
        count = 0
        try:
            if self.isEmpty():
                raise EmptyError('')
            else:
                for i in self.vertices:
                    count += 1
        except EmptyError:
            print('ERROR - Graph empty')
        return count
    
    def edgeCount(self):
        count = 0
        try:
            if self.isEmpty():
                raise EmptyError('')
            else:
                for i in self.vertices:
                    for link in i.links:
                        if link != None:
                            count += 1
                if self.directed == False:
                    count = count / 2
        except EmptyError:
            print('ERROR - Graph Empty')
        return int(count)
    
    def getVertex(self, label):
        v = None
        if self.hasVertex(label) == True:
            for vertex in self.vertices:
                if vertex.label == label:
                    v = vertex
        return v
    
    def getAdjacent(self, label):
        try:
            if self.isEmpty():
                raise EmptyError('')
            else:
                for vertex in self.vertices:
                    if vertex.label == label:
                        vertex.getLinks()
        except EmptyError:
            print('ERROR - Graph empty')
                
    def isAdjacent(self, label1, label2):
        linked = False
        try:
            if self.isEmpty():
                raise EmptyError('')
            else:
                for i in self.vertices:
                    if i.label == label1:
                        for j in self.vertices:
                            if j.label == label2:
                                for linki in i.links:
                                    for linkj in j.links:
                                        if linki != None and linki.getValue() == label2:
                                            linked = True
                                        elif linkj != None and linkj.getValue() == label1:
                                            linked = True
        except EmptyError:
            print('ERROR - Graph empty')
        return linked

    def displayList(self):
        try:
            if self.isEmpty():
                raise EmptyError('')
            else:
                for i in self.vertices:
                    string = i.label + '|'
                    for link in i.links:
                        if link != None:
                            string += ' ' + link.getValue()
                    print(string)
        except EmptyError:
            print('ERROR - Graph Empty')

    def displayMatrix(self):
        try:
            if self.isEmpty():
                raise EmptyError('')
            else:
                count = int(self.vertexCount())
                m = np.zeros((count+1, count+1), dtype=np.str)
                i = 1
                l = 1
                for e in range(count+1):
                    for el in range(count+1):
                        m[e][el] = 0
                for j in self.vertices:
                    m[0][i] = j.label
                    i += 1
                for k in self.vertices:
                    m[l][0] = k.label
                    l += 1

                for r in range(count+1):
                    for c in range(count+1):
                        if self.isAdjacent(m[r][0], m[0][c]):
                            for link in self.getVertex(m[r][0]).links:
                                if link != None and link.getValue() == m[0][c]:
                                    m[r][c] = '1'
                m[0][0] = ' '
                print(m)
        except EmptyError:
            print('ERROR - Graph empty')
            
    def breadthFirst(self):
        try:
            if self.isEmpty():
                raise EmptyError('')
            q = Queue()
            BFS = ''
            for i in self.vertices:
                BFS += i.label
                q.enqueue(i.label)
                for link in i.links:
                    if link != None:
                        q.enqueue(link.getValue())
                q.dequeue()
            print(BFS)
            
        except EmptyError:
            print('ERROR - Graph empty')
