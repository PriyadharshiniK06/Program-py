'''52.Write a program that checks whether all elements in a list are unique.
Input:
1 2 3
Output:
Unique'''
print("Enter the elements of the list: ",end="")
lists=list(map(int,input().split(" ")))
sets=set(lists)
if (len(lists))==(len(sets)):
    print("Unique")
else:
    print("Not Unique")