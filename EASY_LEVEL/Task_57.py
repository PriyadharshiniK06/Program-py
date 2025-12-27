'''57.Write a program that checks whether two strings are anagrams.
Input:
listen silent
Output:
Anagram'''
print("Enter the two strings: ",end="")
string1,string2=list(map(str,input().split(" ")))
if(sorted(string1.lower()) ==sorted(string2.lower())):
    print("Anagram")
else:
    print("Not Anagram")