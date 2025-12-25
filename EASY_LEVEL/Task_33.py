'''Write a program to check whether a year is a leap year
Input:
2024
Output:
Leap Year'''
print("Enter the year: ",end="")
year=int(input())
if(year%4==0):
    print("Leap Year")
else:
    print("Not Leap Year")