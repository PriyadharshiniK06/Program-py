'''18.Write a program that prints the sum of numbers from 1 to N.
Input:
5
Output:
15'''
print("Enter the number:",end=" ")
number=int(input())
sum=0
for i in range(1,number+1):
    sum+=i
print(sum)