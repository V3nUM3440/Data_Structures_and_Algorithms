# 
# Author ---------- Shuber Ali Mirza
# list_harness.py - Test harness for linked list, and for serialization
# Created --------- 5/FEB/2021
# Last Updated ---- 7/FEB/2021
# 

from linked_list import *
import pickle

print('\n# ------------------------- Linked List Harness ------------------------- #')

print('''
Type:
IE\tTo insert in empty list
IF\tTo insert value first
IL\tTo insert value last
PF\tTo peek first value
PL\tTo peek last value
RF\tTo remove first value
RL\tTo remove last value
P\tTo print the list
PK\tTo manipulate list with pickle
Q\tTo quit test harness
''')

user = DSALinkedList()

option = None

while option != 'q':
    option = input('\nEnter option: ').lower()
    if option == 'ie':
        v = input('Enter value to add: ')
        user.insertEmpty(v)
        
    elif option == 'if':
        v = input('Enter value to add: ')
        user.insertFirst(v)
        
    elif option == 'il':
        v = input('Enter value to add: ')
        user.insertLast(v)
    
    elif option == 'pf':
        print(user.peekFirst())
        
    elif option == 'pl':
        print(user.peekLast())
        
    elif option == 'rf':
        user.removeFirst()
        
    elif option == 'rl':
        user.removeLast()
    
    elif option == 'p':
        for i in user:
            print(i)
            
    elif option == 'pk':
        print('''
Type:
W\tTo write your current list to serialized file
P\tTo print the list present in the file
R\tTo read the serialized file
Q\tTo quit pickling
        ''')
        optionp = None
        
        while optionp != 'q':
            optionp = input('\nEnter an option: ').lower()
            if optionp == 'q':
                break
            elif optionp == 'w':
                try:
                    with open('pickleList.txt' , 'wb') as slist:
                        pickle.dump(user , slist)
                        print('List serialized to pickleList.txt')
                except:
                    print('ERROR - Problem pickling object')
            elif optionp == 'r':
                try:
                    with open('pickleList.txt' , 'rb') as slist:
                        user = pickle.load(slist)
                except:
                    print('ERROR - File does not exist')
                    
            elif optionp == 'p':
                try:
                    with open('pickleList.txt' , 'rb') as slist:
                        read = pickle.load(slist)
                        for i in read:
                            print(i)
                except:
                    print('ERROR - File does not exist')
            else:
                print('ERROR - Unknown option')
        
    elif option == 'q':
        break
        
    else:
        print('ERROR - Unknown option')

