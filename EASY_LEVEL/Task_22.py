'''22.Write a program that finds the sum of digits of a number.
Input:
123
Output:
6'''
print("Enter the number:",end=" ")
number=int(input())
sum=0
while(number>0):
    sum+=number%10
    number/=10
print(int(sum))