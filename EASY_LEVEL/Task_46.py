'''46.Write a program that counts occurrences of an element in a list.
Input:
1 2 2 3
2
Output:
2'''
print("Enter the elements of the list: ",end="")
lists=list(map(int,input().split(" ")))
print("Enter the element to find the count of duplicates: ",end="")
elements=int(input())
count=0
for i in lists:
    if(i==elements):
        count+=1
print(count)