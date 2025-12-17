'''9.Write a program that reads two numbers and prints the larger one.
Input:
10 7
Output:
10'''
print("Enter the two numbers : ",end=" ")
a,b=list(map(int,input().split()))
if(a>b):
    print(a)
else:
    print(b)