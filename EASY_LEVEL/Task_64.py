'''Write a program to finds the transpose of a matrix
Input:
1 2 
3 4
Output:
1 3
2 4'''
print("Enter the number of rows and columns: ",end="")
rows,cols=list(map(int,input().split(" ")))
matrix=[]
print("Enter the elements of the list (row by row): ",end="")
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
transpose=[[matrix[j][i] for j in range(rows)] for i in range(cols)]
for i in range(rows):
    for j in range(cols):
        print(transpose[i][j],end=" ")
    print("")
    
