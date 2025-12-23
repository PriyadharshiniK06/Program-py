'''23.Write a program that reverses a number.
Input:
456
Output:
654'''
print("Enter the number: ",end="")
number=int(input())
reverse=0
while(number>0):
    reverse=(reverse*10)+(number%10)
    number//=10
print(reverse)
