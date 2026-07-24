a=int(input("Enter an integer: "))
b=int(input("Enter an integer: "))
c=input("Enter an operator: ")
if(c=="+"):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    if(b!=0):
       print(a/b)
    else:
        print("Cannot Divide by zero")
else:
    print("Invalid Operator")