# 
# Author ---------- Shuber Ali Mirza
# hash_harness.py - Test harness for hash map
# Created --------- 28/FEB/2021
# Last Updated ---- 28/FEB/2021
# 

from Hash import *
import pickle, sys, os

print('\n# ------------------------- Hash Harness ------------------------- #')

user = DSAHashTable()

print('''
Type:
PUT\tTo put key and value pair in hash table
R\tTo remove key value pair in table
GET\tTo get a key value pair from table
HAS\tTo check if key is present in the table
S\tTo get current size of hash table
P\tTo print out all hash table key value pairs
PK\tTo manipulate graph using pickle
FILE\tTo read and write to a file
Q\tTo quit test harness
''')

option = None

while option != 'q':
    option = input('\nEnter option: ').lower()
    
    if option == 'put':
        k = input('Enter key: ')
        v = input('Enter value: ')
        user.put(k, v)
        
    elif option == 's':
        print(user.size)
        
    elif option == 'r':
        k = input('Enter key: ')
        user.removeKey(k)
        
    elif option == 'get':
        k = input('Enter key: ')
        print(user.get(k))
            
    elif option == 'has':
        k = input('Enter key: ')
        print(user.hasKey(k))
    
    elif option == 'p':
        user.printHash()
            
    elif option == 'pk':
        print('''
Type:
W\tTo write your current hash table to serialized file
P\tTo print the hash table present in the file
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
                    with open('pickleHash.txt' , 'wb') as sHash:
                        pickle.dump(user , sHash)
                        print('Hash table serialized to pickleHash.txt')
                except:
                    print('ERROR - Problem pickling object')
            elif optionp == 'r':
                try:
                    with open('pickleHash.txt' , 'rb') as sHash:
                        user = pickle.load(sHash)
                except:
                    print('ERROR - File does not exist')
                    
            elif optionp == 'p':
                try:
                    with open('pickleHash.txt' , 'rb') as sHash:
                        read = pickle.load(sHash)
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
                    with open(f, 'r') as h:
                        for line in h:
                            l = line.split(',')
                            user.put(l[0], l[1].strip())
#                         stdout_ = sys.stdout
#                         sys.stdout = open('trash.txt', 'w')
#                         for line in g:
#                             l = line.split(' ')
#                             l1 = l[0]
#                             l2 = l[1].strip()
#                             user.addVertex(l1 , ' ')
#                             user.addVertex(l2, ' ')
#                             user.addEdge(l1, l2)
#                         sys.stdout = sys.__stdout__
#                         os.remove('trash.txt')
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
