'''51.Write a program that swaps two numbers without using a third variable.
Input:
3 5
Output:
5 3'''
print("Enter the two numbers: ",end="")
a,b=list(map(int,input().split(" ")))
a=a+b
b=a-b
a=a-b
print("a=",a,"b=",b)
