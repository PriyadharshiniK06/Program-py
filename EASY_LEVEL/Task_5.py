'''5.Write a program that reads length and breadth of a rectangle and prints its area.
Input:
5 4
Output:
20'''
print("Enter the length and breadth of a rectangle: ",end=" ")
length,breadth=list(map(int,input().split()))
print("Area : ",length*breadth)