'''63.Write a program that finds the sum of diagonal elements of a square matrix.
Input:
1 2
3 4
Output:
5'''
print("Enter the number of rows: ")
rows=int(input())
matrix=[]
print("Enter the elements of the list(row by row): ")
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
n=len(matrix)
principal=sum(matrix[i][i] for i in range(n))
secondary=sum(matrix[i][n-1-i] for i in range(n))
if(rows>2):
    diagonal=principal+secondary
else:
    diagonal=principal
print(diagonal)
