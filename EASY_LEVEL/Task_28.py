'''28.Write a program that prints Fibonacci series up to N terms.
Input:
5
Output:
0 1 1 2 3'''
print("Enter the number of fibonacci numbers : ",end="")
number=int(input())
a=0
b=1
for i in range(number):
    print(a,end=" ")
    c=a
    a=b
    b=c+b


    