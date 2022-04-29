ls = [0,1,2,3,4,5,6,7]
def binSearch(key,first,last):
    mid = (first+last)//2
    if first>last:
        return False
    elif key == ls[mid]:
        return True
    elif key < ls[mid]:
        return binSearch(key,first,mid-1)
    else:
        return binSearch(key,mid+1,last)
key = int(input('Enter the number to be searched: '))
print(binSearch(key,0,len(ls)-1))