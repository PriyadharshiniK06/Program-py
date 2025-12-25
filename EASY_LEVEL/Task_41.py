'''Write a program that reads a list of numbers and prints the sum
Input: 
1 2 3 4
Output:
10'''
print("Enter the list of numbers: ",end="")
lists=list(map(int,input().split(" ")))
sum=0
for i in lists:
    sum+=i
print(sum)