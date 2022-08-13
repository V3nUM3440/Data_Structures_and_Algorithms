#
# Author -------- Shuber Ali Mirza
# Activity_3.py - Contains solution for activity 3
# Created ------- 20/JAN/2021
# Last Updated -- 21/JAN/2021
#

# Referred from: https://stackoverflow.com/questions/2088201/integer-to-base-x-system-using-recursion-in-python
def converter(a , b):
    base = None
    try:
        add = a%b
        if a<=1:
            base = str(a)
        else:
            base = str(converter(a//b,b)) + str(add)
    except:
        print('ERROR - Enter (Decimal/Interger , Base[integer])')
    return base

# def binary(n):
#     if n > 1:
#         binary(n//2)
#     print(n % 2,end = '')

# binary(10)
# print(converter(10.23423,16))