'''Write a print to print the sum of even numbers up to N
Input: 
10
Output:
30'''
print("Enter the number: ",end="")
number=int(input())
sum=0
for i in range(number+1):
    if(i%2==0):
        sum+=i
print(sum)