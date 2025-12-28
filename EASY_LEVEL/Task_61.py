'''61.Write a program that converts a decimal number to binary.
Input:
10
Output:
1010'''
print("Enter the number: ",end="")
number=int(input())
binary=bin(number)
print(binary[2:])