#
# Author -------- Shuber Ali Mirza
# Activity_2.py - Contains solution for activity 2
# Created ------- 20/JAN/2021
# Last Updated -- 20/JAN/2021
#

# Referred from: https://stackoverflow.com/questions/59147282/how-to-find-greatest-common-divisor-using-recursive-function-in-python
def gcd(x , y):
    denominator = None
    try:
        if y == 0:
            denominator = x
        else:
            denominator = gcd(y, x % y)
    except:
        print('ERROR - Enter integers')
    return denominator
    
# print(gcd(10013512,20027048))