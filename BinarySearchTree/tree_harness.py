# 
# Author ---------- Shuber Ali Mirza
# tree_harness.py - Test harness for binary search tree
# Created --------- 12/FEB/2021
# Last Updated ---- 14/FEB/2021
# 

from tree import *
import pickle,sys

print('\n# ------------------------- Binary Search Tree Harness ------------------------- #')

print('''
Type:
F\tTo find a node with key
I\tTo insert node in tree
D\tTo delete a node from tree
C\tTo print children of node
MIN\tTo find node with lowest key
MAX\tTo find node with highest key
H\tTo print the current height of tree
B\tTo check how balanced the tree is
PRO\tTo print tree in pre-order
IO\tTo print tree in in-order
PSO\tTo print tree in post order
PK\tTo manipulate tree using pickle
CSV\tTo read and write to a csv file
Q\tTo quit test harness
''')

user = DSABST()

option = None

while option != 'q':
    option = input('\nEnter option: ').lower()
    if option == 'f':
        try:
            k = int(input('Enter key to find: '))
            print(user.find(k))
        except:
            print('ERROR - key not an integer')
        
    elif option == 'i':
        try:
            k = int(input('Enter key for node(integer): '))
            v = input('Enter value for node: ')
            user.insert(k , v)
        except:
            print('ERROR - key not an integer')
        
    elif option == 'd':
        try:
            k = int(input('Enter key of node to delete: '))
            user.delete(k)
        except:
            print('ERROR - key not an integer')
            
    elif option == 'c':
        try:
            k = int(input('Enter key to print children: '))
            p = user.find(k)
            print('Left ->' , p.left , '| Right ->' , p.right)
        except:
            print('ERROR - key not an integer')
    
    elif option == 'min':
        print(user.minIter())
        
    elif option == 'max':
        print(user.maxIter())
        
    elif option == 'h':
        print('Height:' , user.height())
    
    elif option == 'b':
        user.balance()
        
    elif option == 'pro':
        user.pre_order()
    
    elif option == 'io':
        user.in_order()
    
    elif option == 'pso':
        user.post_order()
            
    elif option == 'pk':
        print('''
Type:
W\tTo write your current tree to serialized file
P\tTo print the tree present in the file in in-order format
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
                    with open('pickleTree.txt' , 'wb') as stree:
                        pickle.dump(user , stree)
                        print('Tree serialized to pickleTree.txt')
                except:
                    print('ERROR - Problem pickling object')
            elif optionp == 'r':
                try:
                    with open('pickleTree.txt' , 'rb') as stree:
                        user = pickle.load(stree)
                except:
                    print('ERROR - File does not exist')
                    
            elif optionp == 'p':
                try:
                    with open('pickleTree.txt' , 'rb') as stree:
                        read = pickle.load(stree)
                        read.in_order()
                except:
                    print('ERROR - File does not exist')
            else:
                print('ERROR - Unknown option')
    
    elif option == 'csv':
        print('''
Type:
W\tTo write a .csv file
P\tTo print content of .csv file
R\tTo read a .csv file
Q\tTo quit csv menu
        ''')
        
        optionc = None
        
        while optionc != 'q':
            optionc = input('\nEnter an option (.csv csv menu): ').lower()
            
            if optionc == 'q':
                break
            elif optionc == 'r':
                try:
                    f = input('Enter file name (with extension): ')
                    with open(f , 'r') as cf:
                        for line in cf:
                            kv = line.split(',')
                            user.insert(int(kv[0]) , kv[1].strip())
                except:
                    print('ERROR - File does not exist')
                
            elif optionc == 'w':
                f = input('Enter file name (with extension): ')
                pip = None
                while pip != 'pro' and pip != 'io' and pip != 'pso':
                    pip = input('Type: (PRO)=pre-order ; (IO)=in-order ; (PSO)=post-order: ').lower()
                stdout_ = sys.stdout
                if pip == 'io':
                    sys.stdout = open(f, 'w')
                    user.in_order()
                    sys.stdout = sys.__stdout__
                elif pip == 'pro':
                    sys.stdout = open(f, 'w')
                    user.pre_order()
                    sys.stdout = sys.__stdout__
                elif pip == 'pso':
                    sys.stdout = open(f, 'w')
                    user.post_order()
                    sys.stdout = sys.__stdout__
                kv = []
                with open(f , 'r') as cf:
                    for line in cf:
                        kv.append(line.split(' '))
                with open(f , 'w') as cf:
                    for line in kv:
                        cf.write(str(line[1])+','+str(line[3]))
                        
            elif optionc == 'p':
                f = input('Enter file name (with extension): ')
                try:
                    with open(f , 'r') as cf:
                        for line in cf:
                            kv = line.split(',')
                            print('Key:' , kv[0] , 'Value:' , kv[1].strip())
                except:
                    print('ERROR - File does not exist')
                
            else:
                print('ERROR - Unknown option')
        
    
    elif option == 'q':
        break
        
    else:
        print('ERROR - Unknown option')
