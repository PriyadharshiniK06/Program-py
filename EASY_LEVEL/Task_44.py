'''Write a program that removes duplicates from a list
Input:
1 2 2 3
Output:
1 2 3'''
print("Enter the elements of the list: ",end="")
lists=list(map(int,input().split(" ")))
duplicate_removal=list(set(lists))
for i in duplicate_removal:
    print(i,end=" ")