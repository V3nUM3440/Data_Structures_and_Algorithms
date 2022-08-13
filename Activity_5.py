#
# Author -------- Shuber Ali Mirza
# Activity_5.py - Contains solution for activity 5
# Created ------- 21/JAN/2021
# Last Updated -- 21/JAN/2021
#

def moveDisk(src , dest , recur):
    print('(', recur , ') Moving top disk from peg', src, 'to peg' , dest)

def towers(n , src , dest , recur):
    try:
        if n == 1:
            moveDisk(src , dest , int(recur))
        else:
            tmp = 6 - src - dest
            towers(n-1 , src , tmp , int(recur))
            recur += 1
            moveDisk(src , dest , int(recur))
            towers(n-1 , tmp , dest , int(recur))
    except:
        print('ERROR - Enter a positive integer')
        
towers(3, 1 , 3 , 1)