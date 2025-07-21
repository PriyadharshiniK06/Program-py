a = int(input("Enter any number:"))
b= int(input("Enter any number:"))
c= int(input("Enter any number:"))
d= int(input("Enter any number:"))
e= int(input("Enter any number:"))


if(a>b):
    print("a is greater than b")
    if(a>c):
        print("a is greater than c")
    elif(a>d):
        print("a is greater than d")
    elif(a>e):
        print("a is greater than e")
if(b>a):
    print("b is greater than a")
    if(b>c):
        print("b is greater than c")
    elif(b>d):
        print("b is greater than d")
    elif(b>e):
        print("b is greater than e")
if(c>a):
    print("c is greater than b")
    if(c>b):
        print("c is greater than a")
    elif(c>d):
        print("c is greater than d")
    elif(c>e):
        print("c is greater than e")
if(d>a):
    print("d is greater than a")
    if(d>b):
        print("d is greater than b")
    elif(d>c):
        print("d is greater than c")
    elif(d>e):
        print("d is greater than e")
else :
    print("e is greater")
