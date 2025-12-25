'''Write a program to print the largest of three numbers
Input: 
4 9 2
Output: 
9'''
print("Enter the three number: ",end="")
a,b,c=list(map(int,input().split()))
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)