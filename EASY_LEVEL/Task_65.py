'''Write program to checks whether a list is sorted
Input:
1 2 3 4
Output:
Sorted'''
print("Enter the elements of the list: ",end="")
lists=list(map(int,input().split()))
if(lists==sorted(lists)):
    print("Sorted")
else:
    print("Not Sorted")