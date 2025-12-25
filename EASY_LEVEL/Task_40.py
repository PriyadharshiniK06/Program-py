'''Write a program that counts words in a sentence
Input:
I love Python
Output:
3'''
print("Enter the sentence: ",end="")
lists=list(map(str,input().split(" ")))
print(len(lists))