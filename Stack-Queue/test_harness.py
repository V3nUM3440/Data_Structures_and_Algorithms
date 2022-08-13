#
# Author ------- Shuber Ali Mirza
# test_harness.py - Contains test harness for every program
# Created ------ 3/JAN/2021
# Last Updated - 3/JAN/2021
#

from stack import *
from queue import *
from infix_postfix import *

harness = None

while harness != 'quit':
    print('''
    Type:
    stack\tFor stack harness
    queue\tFor queue harness
    ip\t\tFor infix/postfix harness
    quit\tTo exit harness
    ''')

    harness = input('Enter harness name: ').lower()

    if harness == 'stack':
        print('\n# ---------------------------- Stack Harness ---------------------------- #')
        print('''
        Type:
        push\tTo push something to the stack
        pop\tTo pop the top off the stack
        top\tTo show the current top value
        print\tTo print current stack
        count\tTo show the number of items currently in stack
        empty\tTo check if stack is empty
        full\tTo check if stack is full
        quit\tTo quit stack test
        ''')

        s1 = DSAStack()

        option = None

        while option != 'quit':
            option = input('\nEnter option: ').lower()
            if option == 'push':
                value = input('Add to stack: ')
                s1.push(value)

            elif option == 'pop':
                print('Poped: ', s1.pop())

            elif option == 'top':
                print(s1.top())

            elif option == 'count':
                print(s1.getCount())

            elif option == 'full':
                print(s1.isFull())

            elif option == 'empty':
                print(s1.isEmpty())

            elif option == 'print':
                s1.printArr()

            elif option == 'quit':
                break

            else:
                print('ERROR - Unknown option')
                
    elif harness == 'queue':
        print('\n# ---------------------------- Queue Harness ---------------------------- #')
        print('''
        Type:
        s\tTo use shuffling queue
        c\tTo use circular queue
        ''')
        
        option1 = None
        while option1 != 's' and option1 != 'c':
            option1 = input('Enter queue type: ').lower()
            
        if option1 == 's':
            q1 = DSAShufflingQueue()
        else:
            q1 = DSACircularQueue()
        
        print('''
        Type:
        enqueue\tTo enter something to the queue
        dequeue\tTo pop the top off the queue
        peek\tTo show the current queued value
        print\tTo print current queue
        count\tTo show the number of items currently in queue
        empty\tTo check if queue is empty
        full\tTo check if queue is full
        quit\tTo quit queue test
        ''')
        
        option = None

        while option != 'quit':
            option = input('\nEnter option: ').lower()
            if option == 'enqueue':
                value = input('Add to stack: ')
                q1.enqueue(value)

            elif option == 'dequeue':
                print('Dequeued: ', q1.dequeue())

            elif option == 'peek':
                print(q1.peek())

            elif option == 'count':
                print(q1.getCount())

            elif option == 'full':
                print(q1.isFull())

            elif option == 'empty':
                print(q1.isEmpty())

            elif option == 'print':
                q1.printArr()

            elif option == 'quit':
                break

            else:
                print('ERROR - Unknown option')
                
    elif harness == 'ip':
        print('\n# ---------------------------- Infix/postfix Harness ---------------------------- #')
        print('''
        Type:
        convert\tTo convert infix expression to postfix
        quit\tTo quit queue test
        ''')
        
        option = None
        obj = EQNSolver()
        
        while option != 'quit':
            option = input('\nEnter option: ').lower()
            if option == 'convert':
                exp = input('Enter expression to convert: ')
                obj.infixToPostfix(exp)
            elif option == 'quit':
                break
            else:
                print('ERROR - Unknown option')
                
    elif harness == 'quit':
        break
        
    else:
        print('ERROR - Unknown option')