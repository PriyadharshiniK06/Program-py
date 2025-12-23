'''25.Write a program that checks whether a number is prime.
Input:
7
Output:
Prime'''
import math
print("Enter the number: ",end="")
number=int(input())
prime=True
for i in range(2,int(math.sqrt(number))+1):
    if(number%i==0):
        prime=False
if(prime==True):
    print("Prime")
else:
    print("Not Prime")