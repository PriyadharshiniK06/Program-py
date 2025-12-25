'''48.Write a program that sorts a list in ascending order.
Input:
3 1 2
Output:
1 2 3'''
print("Enter the elements of the list: ",end="")
lists=list(map(int,input().split(" ")))
sort=sorted(lists)
for i in sort:
    print(i,end=" ")