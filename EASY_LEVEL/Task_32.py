'''Write a program to print the numbers in reverse order from N to 1
Input:
5
Output:
5 4 3 2 1'''
print("Enter the number: ",end="")
number=int(input())
for i in range(number,0,-1):
    print(i,end=" ")