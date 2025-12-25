'''50.Write a program that merges two lists.
Input:
1 2
3 4
Output:
1 2 3 4'''
print("Enter the elements of list 1: ",end="")
list1=list(map(int,input().split(" ")))
print("Enter the elements of list 2: ",end="")
list2=list(map(int,input().split(" ")))
list3=[]
for j in list1:
    list3.append(j)
for i in list2:
    list3.append(i)
for k in list3:
    print(k,end=" ")
