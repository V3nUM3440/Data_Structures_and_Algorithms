#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

# Author ------- Shuber Ali Mirza
# Last Updated - 14/MAR/2021

import sys
import random
import numpy as np

sys.setrecursionlimit(10**6)

def bubbleSort(A):
    for ii in range(len(A)-1, 0, -1):
        for j in range(ii):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                
def insertionSort(A):
    for nn in range(1, len(A)-1):
        ii = nn
        temp = A[ii]
        while ii>0 and A[ii-1] > temp:
            A[ii] = A[ii-1]
            ii -= 1
        A[ii] = temp

def selectionSort(A):
    for nn in range(len(A)-1):
        minIdx = nn
        for jj in range(nn+1, len(A)-1):
            if A[jj] < A[minIdx]:
                minIdx = jj
        temp = A[minIdx]
        A[minIdx] = A[nn]
        A[nn] = temp

# Reference: https://www.youtube.com/watch?v=3aTfQvs-_hA&ab_channel=BrianFaure
def mergeSort(A):
#     mergeSortRecurse(A, 0, len(A) - 1)
    mergeSortRecurse(A)

def mergeSortRecurse(A):
# def mergeSortRecurse(A, l, r):
    if len(A)<=1: return A
    left,right = mergeSortRecurse(A[:int(len(A)/2)]), mergeSortRecurse(A[int(len(A)/2):])
    return merge(left, right)
#     if l < r:
#         m = int((l + r) / 2)
#         mergeSortRecurse(A, l, m)
#         mergeSortRecurse(A, m, r)
#         merge(A, l, m, r)
#     return A

def merge(l, r):
# def merge(A, l, m, r):
    temp = []
    a,b = 0,0
    while a < len(l) and b < len(r):
        if l[a] > r[b]:
            temp.append(l[a])
            a += 1
        else:
            temp.append(r[b])
            b += 1
    if a == len(l):
        temp.extend(r[b:])
    else:
        temp.extend(l[a:])
    return temp
#     temp = np.zeros(r-l+1, dtype=int)
#     ii = l
#     jj = m + 1
#     kk = 0
#     while (ii <= m) and (jj <= r):
#         if A[ii] <= A[jj]:
#             temp[kk] = A[ii]
#             ii += 1
#         else:
#             temp[kk] = A[jj]
#             jj += 1
#         kk += 1
#     i = ii
#     while i != m:
#         temp[kk] = A[i]
#         kk += 1
#         i += 1
#     j = jj
#     while j != r:
#         temp[kk] = A[j]
#         kk += 1
#         j += 1
#     k = l
#     while k != r:
#         A[k] = temp[k - l]
#         k += 1
#     return A

def quickSort(A, pivType):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    if pivType == 'ran':
        quickSortRecurse(A, 0, len(A)-1, 'ran')
    elif pivType == 'left':
        quickSortRecurse(A, 0, len(A)-1, 'left')
    elif pivType == 'med':
        quickSortRecurse(A, 0, len(A)-1, 'med')

def quickSortRecurse(A, leftIdx, rightIdx, pivType):
    if rightIdx > leftIdx:
        if pivType == 'left':
            pivot = leftIdx
            newPivot = doPartitioning(A, leftIdx, rightIdx, pivot)
            quickSortRecurse(A, leftIdx, newPivot-1, 'left')
            quickSortRecurse(A, newPivot+1, rightIdx, 'left')
        elif pivType == 'ran':
            pivot = random.randint(leftIdx, rightIdx)
            newPivot = doPartitioning(A, leftIdx, rightIdx, pivot)
            quickSortRecurse(A, leftIdx, newPivot-1, 'ran')
            quickSortRecurse(A, newPivot+1, rightIdx, 'ran')
        elif pivType == 'med':
            n1 = random.randint(leftIdx, rightIdx)
            n2 = random.randint(leftIdx, rightIdx)
            n3 = random.randint(leftIdx, rightIdx)
            while (n1 == n2) and (n1 == n3) and (n2 == n3):
                n1 = random.randint(leftIdx, rightIdx)
                n2 = random.randint(leftIdx, rightIdx)
                n3 = random.randint(leftIdx, rightIdx)
            if n1 < n2 and n2 < n3:
                pivot = n2
            elif n1 < n2 and n2 > n3:
                pivot = n3
            else:
                pivot = n1
            newPivot = doPartitioning(A, leftIdx, rightIdx, pivot)
            quickSortRecurse(A, leftIdx, newPivot-1, 'med')
            quickSortRecurse(A, newPivot+1, rightIdx, 'med')

def doPartitioning(A, leftIdx, rightIdx, pivot):
    pivotV = A[pivot]
    A[pivot] = A[rightIdx]
    A[rightIdx] = pivotV
    cur = leftIdx
#     for i in range(leftIdx, rightIdx - 1):
#         if A[i] < pivotV:
#             temp = A[i]
#             A[i] = A[cur]
#             A[cur] = temp
#             cur += 1
    ii = leftIdx
    while ii != rightIdx:
        if A[ii] < pivotV:
            temp = A[ii]
            A[ii] = A[cur]
            A[cur] = temp
            cur += 1
        ii += 1
    newPiv = cur
    A[rightIdx] = A[newPiv]
    A[newPiv] = pivotV
    return newPiv
