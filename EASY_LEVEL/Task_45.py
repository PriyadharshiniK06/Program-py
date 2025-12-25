'''Write a program that checks whether an element exists in a list
Input:
List: 1 2 3
Element: 2
Output:
Found'''
print("Enter the Input: ")
print("List: ",end="")
lists=list(map(int,input().split(" ")))
print("Element: ",end="")
element=int(input())
for i in lists:
    if(element==i):
        print("Found")
