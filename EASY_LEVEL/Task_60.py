'''60.Write a program that counts uppercase letters in a string.
Input:
HeLLo
Output:
3'''
print("Enter the string: ",end="")
strings=str(input())
count=0
for i in strings:
    if(i == i.upper()):
        count+=1
print(count)