'''58.Write a program that finds the GCD of two numbers.
Input:
12 18
Output:
6'''
import math
print("Enter the two numbers: ",end="")
a,b=list(map(int,input().split(" ")))
print(math.gcd(a,b))