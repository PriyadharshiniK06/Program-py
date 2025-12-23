'''16.Write a program that prints numbers from 1 to N.
Input:
5
Output:
1 2 3 4 5'''
print("Enter the number: ",end=" ")
number=int(input())
for i in range(1,number+1):
    print(i,end=" ")