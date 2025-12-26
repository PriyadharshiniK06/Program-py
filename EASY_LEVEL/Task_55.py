'''55.Write a program that prints the frequency of each character in a string.
Input:
aab
Output:
a:2 b:1'''
print("Enter the string: ",end="")
string=str(input())
result={char:string.count(char) for char in set(string)}
for i,j in result.items():
    print(f"{i}:{j}",end=" ")