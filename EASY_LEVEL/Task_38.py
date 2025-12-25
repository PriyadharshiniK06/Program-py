'''Write a program that counts vowels in a string
Input:
apple
Output:
2'''
print("Enter the string: ",end="")
string=str(input())
count=0
for i in string:
    if i in 'aeiou':
        count+=1
print(count)