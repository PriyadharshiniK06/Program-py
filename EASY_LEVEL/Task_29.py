'''29.Write a program that checks whether a number is an Armstrong number.
Input:
153
Output:
Armstrong'''
print("Enter the number: ",end="")
number=int(input())
original=number
strings=str(number)
lengths=len(strings)
digit=0
while(number>0):
    digit_power=(number%10)**lengths
    digit+=digit_power
    number//=10
if(digit==original):
    print("Armstrong")
else:
    print("Not Armstrong")
    