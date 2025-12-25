'''Write a program to print the count of even and odd numbers up to N
Input:
5
Output:
Even: 2 Odd: 3'''
print("Enter the number: ",end="")
number=int(input())
counteven=0
countodd=0
for i in range(1,number+1):
    if(i%2==0):
        counteven+=1
    else:
        countodd+=1
print("Even: ",counteven," Odd: ",countodd)