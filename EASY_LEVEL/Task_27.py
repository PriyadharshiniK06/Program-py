'''27.Write a program that calculates factorial of a number.
Input:
5
Output:
120'''
print("Enter the number: ",end="")
number=int(input())
fact=1
for i in range(1,number+1):
    fact*=i
print(fact)