'''Write a python program to implement binary search with recursion.'''
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)
alist = [0,1,2,3,4,5,6,7]
item = int(input('Enter the number to be searched: '))
print(binarySearch(alist, item))