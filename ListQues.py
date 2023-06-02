"""
Create a list having elements 1,2,3,4,5.
Write function for following opeartions :
1. Swap any 2 elements of which indexes are passed eg 0, 4 --> 5,2,3,4,1
2. Maximum value of that list ---> 5
3. Minimum value of that list --> 2
4. Check if list is sorted in ascending order. --> True
"""

#1. Swap any 2 elements of which indexes are passed eg 0, 4 --> 5,2,3,4,1
#using 3rd variable

def swapDeezNuts(l, pos1, pos2):
    temp=l[pos1]
    l[pos1]=l[pos2]
    l[pos2]=temp
    return l

List = [5,4,3,2,1]
pos1= 1
pos2=5
 
print(swapDeezNuts(List, pos1-1, pos2-1))
