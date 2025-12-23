'''20.Write a program that prints the multiplication table of a number.
Input:
3
Output:
3 6 9 12 15'''
print("Enter the number:",end=" ")
number=int(input())
for i in range(1,6):
    print(number*i,end=" ")