#
# Author ------- Shuber Ali Mirza
# Created ------ 29/JAN/2021
# Last Updated - 31/JAN/2021
#

# Reference 1: https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
# Reference 2: https://www.goeduhub.com/2680/python-program-to-implement-postfix-from-infix-expressions

from stack import *

class EQNSolver(DSAStack):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    def isOperand(self, ch):
        result = None
        if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.':
            result = True
        else:
            result = False
        return result

    def notGreater(self, i):
        result = None
        try: 
            a = self.precedence[i] 
            b = self.precedence[self.top()] 
            if a <= b:
                result = True
            else:
                result = False
        except KeyError: 
            result = False
        return result
        
    def infixToPostfix(self, exp):
        self.output = []
        for i in exp: # If the character is an operand, add it to output
            if self.isOperand(i):
                self.output.append(i)

            elif i == '(': # If the character is an '(', push it to stack
                self.push(i)

            elif i == ')': # If the scanned character is an ')', pop and output from the stack until and '(' is found 
                while (self.isEmpty() == False) and (self.top() != '('):
                    a = self.pop() 
                    self.output.append(a) 
                if (self.isEmpty() == False) and (self.top() != '('): 
                    return -1
                else: 
                    self.pop()

            else: # An operator is encountered
                self.output[-1] += ' '
                while (self.isEmpty() == False) and (self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(' '+i)

        while self.isEmpty() == False: # pop all the operator from the stack 
            self.output.append(self.pop())
        
        joint = ''.join(self.output)
        print(joint)
