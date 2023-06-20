"""
Create a list having elements 1,2,3,4,5.
Write function for following opeartions :
1. Swap any 2 elements of which indexes are passed eg 0, 4 --> 5,2,3,4,1
2. Maximum value of that list ---> 5
3. Minimum value of that list --> 2
4. Check if list is sorted in ascending order. --> True
"""

#did some changes from scratch as there were some indention error
#sorting algo is not implementing correctly I'll do it tomorrow

def swapElement(l, pos1, pos2):
    temp = l[pos1]
    l[pos1] = l[pos2]
    l[pos2] = temp
    return l

k = [5,4,3,2,1]
pos1 = 1
pos2 = 3

print(swapElement(k, pos1, pos2))

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
    for j in range(i +1 , len(k)):

        if k[i] > k[j]:
            k[i], k[j] = k[j], k[i]

print(k)




