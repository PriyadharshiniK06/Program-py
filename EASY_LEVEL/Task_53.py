'''53.Write a program that finds common elements between two lists.
Input:
1 2 3
2 3 4
Output:
2 3'''
print("Enter the elements of list 1: ",end="")
list1=list(map(int,input().split(" ")))
print("Enter the elements of list 2: ",end="")
list2=list(map(int,input().split(" ")))
for i in list1:
    for j in list2:
        if(i == j):
            print(i,end=" ")