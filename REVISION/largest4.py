a=int(input("Enter an integer: "))
b=int(input("Enter an integer: "))
c=int(input("Enter an integer: "))
d=int(input("Enter an integer: "))
if(a>=b and a>=c and a>=d):
    print(a)
elif(b>=a and b>=c and b>=d):
    print(b)
elif(c>=a and c>=b and c>=d):
    print(c)
else:
    print(d)