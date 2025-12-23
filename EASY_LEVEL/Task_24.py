'''24.Write a program that checks whether a number is a palindrome.
Input:
121
Output:
Palindrome'''
print("Enter the number: ",end="")
number=int(input())
original=number
reverse=0
while(number>0):
    reverse=(reverse*10)+(number%10)
    number//=10
if(reverse==original):
    print("Palindrome")
else:
    print("Not a Palindrome")