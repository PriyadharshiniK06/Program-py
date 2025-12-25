'''Write a program that check whether a string is a palindrome
Input:
madam
Output:
Palindrome'''
print("Enter the string: ",end="")
string=str(input())
if(string==string[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")