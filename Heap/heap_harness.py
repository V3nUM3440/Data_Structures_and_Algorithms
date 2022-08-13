# 
# Author ---------- Shuber Ali Mirza
# heap_harness.py - Test harness for heap
# Created --------- 6/MAR/2021
# Last Updated ---- 6/MAR/2021
# 

from heap import *
import pickle, sys

print('\n# ------------------------- Heap Harness ------------------------- #')

size = int(input('Enter heap size (10 by default): '))
user = DSAHeap(size)

print('''
Type:
A\tTo add to heap
R\tTo remove to heap
S\tTo sort the heap
C\tTo get count of items in heap
P\tTo print the current heap
PK\tTo manipulate graph using pickle
FILE\tTo read and write to a file
Q\tTo quit test harness
''')

option = None

while option != 'q':
    option = input('\nEnter option: ').lower()
    
    if option == 'a':
        p = int(input('Enter priority(integer): '))
        v = input('Enter value: ')
        user.add(p, v)
        
    elif option == 'r':
        user.remove()
        
    elif option == 's':
        user.heapSort()
        
    elif option == 'c':
        print(user.count)
    
    elif option == 'p':
        user.printit()
            
    elif option == 'pk':
        print('''
Type:
W\tTo write your current heap to serialized file
P\tTo print the heap present in the file
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
                    with open('pickleHeap.txt' , 'wb') as sHeap:
                        pickle.dump(user , sHeap)
                        print('Heap serialized to pickleHeap.txt')
                except:
                    print('ERROR - Problem pickling object')
            elif optionp == 'r':
                try:
                    with open('pickleHeap.txt' , 'rb') as sHeap:
                        user = pickle.load(sHeap)
                except:
                    print('ERROR - File does not exist')
                    
            elif optionp == 'p':
                try:
                    with open('pickleHeap.txt' , 'rb') as sHeap:
                        read = pickle.load(sHeap)
                        read.printit()
                except:
                    print('ERROR - File does not exist')
            else:
                print('ERROR - Unknown option')
    
    elif option == 'file':
        print('''
Type:
P\tTo print content of a file
R\tTo read a file
Q\tTo quit file menu
        ''')
        
        optionc = None
        
        while optionc != 'q':
            optionc = input('\nEnter an option (file menu): ').lower()
            
            if optionc == 'q':
                break
            elif optionc == 'r':
                try:
                    f = input('Enter file name (with extension): ')
                    with open(f, 'r') as h:
                        for line in h:
                            l = line.split(',')
                            user.add(int(l[0]), l[1].strip())
                except:
                    print('ERROR - File does not exist')
                    
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
