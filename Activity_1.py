#
# Author -------- Shuber Ali Mirza
# Activity_1.py - Contains solution for activity 1
# Created ------- 20/JAN/2021
# Last Updated -- 21/JAN/2021
#

# -------------------- Factorial ---------------------- #
def factorial(n):
    result = None
    try:
        if n < 0:
            raise ValueError(str(n) + ' is not a positive interger')
        else:
            if n == 0:
                result = 1
            else:
                result = n * factorial(n-1)
    except ValueError as e:
        print('Incorrect value: ', e)
    return result

# print('Factorial:\t', factorial(10))
# print('Factorial:\t', factorial(2961))

# -------------------- Fibonacci ---------------------- #
def fibonacci(n):
    fibVal = None
    try:
        if n < 0:
            raise Exception
        elif n == 0:
            fibVal = 0
        elif n == 1:
            fibVal = 1
        else:
            fibVal = fibonacci(n-1) + fibonacci(n-2)
    except Exception:
        print('ERROR - Enter positive integer')
    return fibVal

# print('Fibonacci:\t', fibonacci(10))
# print('Fibonacci:\t', fibonacci(40))