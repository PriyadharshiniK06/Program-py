'''47.Write a program that reverses a list.
Input:
1 2 3
Output:
3 2 1'''
print("Enter the elements of the list: ",end="")
lists=list(map(int,input().split(" ")))
reverse=[]
for i in lists[::-1]:
    reverse.append(i)
for j in reverse:
    print(j,end=" ")