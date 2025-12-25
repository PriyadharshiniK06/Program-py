'''54.Write a program that checks whether a number is a perfect number.
Input:
6
Output:
Perfect'''
print("Enter the number: ",end="")
number=int(input())
perfect=0
for i in range(1,number):
    if (number%i==0):
        perfect+=i
if(perfect==number):
    print("Perfect")
else:
    print("Not Perfect")