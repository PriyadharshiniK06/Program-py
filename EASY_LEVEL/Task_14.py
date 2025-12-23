'''14.Write a program that reads two numbers and prints their difference.
Input:
10 4
Output:
6'''
print("Enter the two number:",end=" ")
a,b=list(map(int,input().split()))
print(a-b)