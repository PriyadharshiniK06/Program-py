'''Write a program that finds the minimum element in a list
Input:
7 1 4
Output:
1'''
print("Enter the elements in the list: ",end="")
lists=list(map(int,input().split(" ")))
print(min(lists))