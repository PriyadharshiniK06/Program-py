a=int(input("Enter the units consumed: "))
if(a<=100):
    print(a*1.5)
elif(a<=200):
    print((100*1.5)+((a-100)*2.5))
else:
    print((100*1.5)+((200-100)*2.5)+((a-200)*4))