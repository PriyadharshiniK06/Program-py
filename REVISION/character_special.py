a=input("Enter a value: ")[0]
if(a>="A" and a<="Z"):
    print("Uppercase")
elif(a>="a" and a<="z"):
    print("Lowercase")
elif(a>="0" and a<="9"):
    print("Digit")
else:
    print("Special Character")
