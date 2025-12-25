'''49.Write a program that finds the second largest number in a list.
Input:
5 8 3
Output:
5'''
print("Enter the elements of the list: ",end="")
lists=list(map(int,input().split(" ")))
maximum=max(lists)
for i in lists:
    for j in lists:
       if(i>j and i!=maximum):
           second=i
print(second)
