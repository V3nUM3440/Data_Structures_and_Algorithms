#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

# Author ------- Shuber Ali Mirza
# Last Updated - 14/JAN/2021

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

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


