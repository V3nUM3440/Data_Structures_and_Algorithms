# 
# Author ----------- Shuber Ali Mirza
# graph_harness.py - Test harness for graphs
# Created ---------- 21/FEB/2021
# Last Updated ----- 22/FEB/2021
# 

from graphs import *
import pickle, sys, os

print('\n# ------------------------- Graphs Harness ------------------------- #')

print('''
Type:
D\tFor directed
U\tFor undirected
''')

direct = None
user = None

while direct == None:
    direct = input('Enter option: ').lower()
    if direct == 'd':    
        user = Graph(True)
    elif direct == 'u':
        user = Graph(False)
    else:
        direct = None
        print('ERROR - Unknown option')

print('''
Type:
AV\tTo add vertex
AE\tTo add edge
HV\tTo check is graph has vertex
VC\tTo get vertex count
EC\tTo get edge count
GV\tTo get a vertex
GA\tTo get adjacency list
IA\tTo check if vertices are adjacent
DL\tTo display as list
DM\tTo display as Matrix
BFS\tTo perform breadth first search
PK\tTo manipulate graph using pickle
FILE\tTo read and write to a file
Q\tTo quit test harness
''')

option = None

while option != 'q':
    option = input('\nEnter option: ').lower()
    if option == 'av':
        l = input('Enter label: ')
        v = input('Enter value: ')
        user.addVertex(l, v)
        
    elif option == 'ae':
        try:
            l1 = input('Enter label 1: ')
            l2 = input('Enter label 2: ')
            if user.hasVertex(l1) == False:
                raise Exception
            elif user.hasVertex(l2) == False:
                raise Exception
            else:
                user.addEdge(l1, l2)
        except Exception:
            print('ERROR - label doesn\'t exist')
        
    elif option == 'hv':
        l = input('Enter label: ')
        print(user.hasVertex(l))
            
    elif option == 'vc':
        print(user.vertexCount())
    
    elif option == 'ec':
        print(user.edgeCount())
        
    elif option == 'gv':
        l = input('Enter label: ')
        print(user.getVertex(l))
        
    elif option == 'ga':
        l = input('Enter label: ')
        user.getAdjacent(l)
    
    elif option == 'ia':
        try:
            l1 = input('Enter label 1: ')
            l2 = input('Enter label 2: ')
            if user.hasVertex(l1) == False:
                raise Exception
            elif user.hasVertex(l2) == False:
                raise Exception
            else:
                print(user.isAdjacent(l1, l2))
        except Exception:
            print('ERROR - label doesn\'t exist')
        
    elif option == 'dl':
        user.displayList()
    
    elif option == 'dm':
        user.displayMatrix()
        
    elif option == 'bfs':
        user.breadthFirst()
            
    elif option == 'pk':
        print('''
Type:
W\tTo write your current graph to serialized file
P\tTo print the graph present in the file in as adjacency list
R\tTo read the serialized file
Q\tTo quit pickling
        ''')
        optionp = None
        
        while optionp != 'q':
            optionp = input('\nEnter an option (pickle menu): ').lower()
            if optionp == 'q':
                break
            elif optionp == 'w':
                try:
                    with open('pickleGraph.txt' , 'wb') as sgraph:
                        pickle.dump(user , sgraph)
                        print('Graph serialized to pickleGraph.txt')
                except:
                    print('ERROR - Problem pickling object')
            elif optionp == 'r':
                try:
                    with open('pickleGraph.txt' , 'rb') as sgraph:
                        user = pickle.load(sgraph)
                except:
                    print('ERROR - File does not exist')
                    
            elif optionp == 'p':
                try:
                    with open('pickleGraph.txt' , 'rb') as sgraph:
                        read = pickle.load(sgraph)
                        read.displayList()
                except:
                    print('ERROR - File does not exist')
            else:
                print('ERROR - Unknown option')
    
    elif option == 'file':
        print('''
Type:
W\tTo write a file
P\tTo print content of a file
R\tTo read a file
Q\tTo quit csv menu
        ''')
        
        optionc = None
        
        while optionc != 'q':
            optionc = input('\nEnter an option (file menu): ').lower()
            
            if optionc == 'q':
                break
            elif optionc == 'r':
                try:
                    f = input('Enter file name (with extension): ')
                    with open(f, 'r') as g:
                        stdout_ = sys.stdout
                        sys.stdout = open('trash.txt', 'w')
                        for line in g:
                            l = line.split(' ')
                            l1 = l[0]
                            l2 = l[1].strip()
                            user.addVertex(l1 , ' ')
                            user.addVertex(l2, ' ')
                            user.addEdge(l1, l2)
                        sys.stdout = sys.__stdout__
                        os.remove('trash.txt')
                except:
                    print('ERROR - File does not exist')
                
            elif optionc == 'w':
                f = input('Enter file name (with extension): ')
                stdout_ = sys.stdout
                sys.stdout = open(f, 'w')
                for i in user.vertices:
                    for link in i.links:
                        if link != None:
                            print(i.label, link.getValue())
                sys.stdout = sys.__stdout__
                    
            elif optionc == 'p':
                f = input('Enter file name (with extension): ')
                try:
                    with open(f , 'r') as cf:
                        for line in cf:
                            print(line)
                except:
                    print('ERROR - File does not exist')
                
            else:
                print('ERROR - Unknown option')
        
    
    elif option == 'q':
        break
        
    else:
        print('ERROR - Unknown option')
