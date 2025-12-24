'''26.Write a program that prints all prime numbers up to N.
Input:
10
Output:
2 3 5 7'''
import math
print("Enter the number: ",end="")
number=int(input())
for i in range(2,number+1):
    prime=True
    for j in range(2,int((math.sqrt(i)))+1):
        if(i%j==0):
            prime=False
    if(prime==True):
        print(i,end=" ")