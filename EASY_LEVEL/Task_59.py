'''59.Write a program that finds the LCM of two numbers.
Input:
4 6
Output:
12'''
import math
print("Enter the two number: ",end="")
a,b=list(map(int,input().split(" ")))
print(math.lcm(a,b))