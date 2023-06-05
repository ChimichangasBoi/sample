"""
Create a list having elements 1,2,3,4,5.
Write function for following opeartions :
1. Swap any 2 elements of which indexes are passed eg 0, 4 --> 5,2,3,4,1
2. Maximum value of that list ---> 5
3. Minimum value of that list --> 2
4. Check if list is sorted in ascending order. --> True
"""

def swapElement(l, pos1, pos2):
    temp=l[pos1]
    l[pos1]=l[pos2]
    l[pos2]=temp
    return l

k = [5,4,3,2,1]
pos1= 1
pos2=3

k.sort


print(swapElement(k, pos1, pos2))

#max element
def Max(k):
 
    max = k[0] #assuming any element to be max then later get compared with other values for battle of death

    for x in k:
        if x > max:
            max = x
 
    
    return max
 
print("Largest element is:", Max(k))

#min element
def Min(k):
 
    min = k[0]

    for x in k:
        if x < min:
            min = x
 
    
    return min
 
print("smallest element is:", Min(k))


print(bool(k.sort))





