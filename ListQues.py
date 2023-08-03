"""
Create a list having elements 1,2,3,4,5.
Write function for following opeartions :
1. Swap any 2 elements of which indexes are passed eg 0, 4 --> 5,2,3,4,1
2. Maximum value of that list ---> 5
3. Minimum value of that list --> 2
4. Check if list is sorted in ascending order. --> True
"""


#Make this as a function named sortList() which takes
#list as a parameter
#'ASC' or 'DESC' as parameter to decide sorting order
#It returns same list with sorted values based on ASC or DESC value provided
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

k = [5,4,3,2,1]
pos1 = 1
pos2 = 3

print(swapElement(k, pos1, pos2))

print("Sorted in ASC order:", sortList(k.copy(), 'ASC')) #copy() returns a copy of the specified list
print("Sorted in DESC order:", sortList(k.copy(), 'DESC'))

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

print("Largest element is:", Max(k))
print("Smallest element is:", Min(k))

for i in range(len(k)): 
    for j in range(i +1 , len(k)):  #using a nested loop to iterate each number in the list
        if k[i] > k[j]:
            k[i], k[j] = k[j], k[i] #to sort in ascending order I'm using bubble sort where I'm comparing the current element with the one after it swapping their values if needed
print(k)




