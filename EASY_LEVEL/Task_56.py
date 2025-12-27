'''56.Write a program that replaces spaces in a string with hyphens.
Input:
hello world
Output:
hello-world'''
print("Enter the sentence: ",end="")
strings=input()
strings1=strings.replace(" ","-")
print(strings1)