"""
Create a list having elements 1,2,3,4,5.
Write function for following opeartions :
1. Swap any 2 elements of which indexes are passed eg 0, 4 --> 5,2,3,4,1
2. Maximum value of that list ---> 5
3. Minimum value of that list --> 2
4. Check if list is sorted in ascending order. --> True
"""

# Creating a list having Elements 1,2,3,4,5
myList = [1,2,3,7,33,5]
# Swapping 2 indexes of which indexes are passed
index1, index2 = 0, 4
print(f"List before swapping at {index1},{index2} indexes is ", myList)
swapElement(myList, index1, index2)
print(f"List after swapping at {index1},{index2} indexes is ", myList)
# Print maximum value of list
print(Max(myList))
# Print minimum value of list
print(Min(myList))
# Sorting the list in ascending order
print("Original list order is ", myList)
print("List after sorting in ASC order is ", myList)
sortList(myList, "ASC")
# Sorting the list in descending order
sortList(myList, "DESC")
print("List after sorting in DESC order is ", myList)

def sortList(lst, order): #bubble sorting
    if order == 'ASC': 
        for i in range(len(lst)): #lst refers to the list to be sorted
            for j in range(i + 1, len(lst)): 
                if lst[i] > lst[j]:
                    lst = swapElement(lst, i, j)
    elif order == 'DESC': #f the previous condition was not true, then this condition will be in work
        for i in range(len(lst)): 
            for j in range(i + 1, len(lst)): 
                if lst[i] < lst[j]:
                    lst = swapElement(lst, i, j)
    else:
        print("error")

def swapElement(l, pos1, pos2):
    temp = l[pos1]
    l[pos1] = l[pos2]
    l[pos2] = temp
    return l

def Max(k):
    if not k:  
        print("List is empty")
    max = k[0]
    for ele in k:
        if ele > max:
            max = ele
    return max

def Min(k):
    if not k:  
        print("List is empty")
    min = k[0]
    for ele in k:
        if ele < min:
            min = ele
    return min
