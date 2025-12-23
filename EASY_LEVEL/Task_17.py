'''17.Write a program that prints all even numbers up to N.
Input:
10
Output:
2 4 6 8 10'''
print("Enter the number:",end=" ")
number=int(input())
for i in range(1,number+1):
    if(i%2==0):
        print(i,end=" ")