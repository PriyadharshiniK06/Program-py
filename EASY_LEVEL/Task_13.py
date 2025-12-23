'''13.Write a program that reads marks and prints “Pass” if marks ≥ 40.
Input:
65
Output:
Pass'''
print("Enter the mark:",end=" ")
mark=int(input())
if(mark>=40):
    print("Pass")
else:
    print("Fail")