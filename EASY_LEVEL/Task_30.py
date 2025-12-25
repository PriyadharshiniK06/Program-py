'''Write a program to print all the numbers that are divisible by 3 and 5 up to N
Input:
30
Output:
15 30'''
print("Enter the number: ",end="")
number=int(input())
for i in range(1,number+1):
    if(i%3==0 and i%5==0):
        print(i,end=" ")