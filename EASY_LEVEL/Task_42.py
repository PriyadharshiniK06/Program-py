'''Write a program that finds the maximum element in a list
Input:
5 9 2
Output:
9'''
print("Enter the elements in the list: ",end="")
lists=list(map(int,input().split(" ")))
print(max(lists))