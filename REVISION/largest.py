a=int(input("Enter an integer: "))
b=int(input("Enter an integer: "))
c=int(input("Enter an integer: "))
if(a>=b and a>=c):
    print(a)
elif(b>=a and b>=c):
    print(b)
else:
    print(c)