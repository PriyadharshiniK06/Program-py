from  operators import addition
a=int(input("Enter the integer: "))
b=int(input("Enter the integer: "))
c=input("enter any operation: ")
if c=='+':
    print(addition(a,b))
elif c=='-':
    print(subtraction(a,b))
elif c=='*':
    print(multiplication(a,b))
elif c=='/':
    print(division(a,b))
else:
    print("The operator is invalid")
