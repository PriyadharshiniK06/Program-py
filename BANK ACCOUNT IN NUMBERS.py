print('INSERT YOUR CARD')
print('The options you can do: ')
print('1. WITHDRAWAL')
print('2. DEPOSIT')
print('3. BALANCE ENQUIRY')
a=int(input('What  you are likely to do: '))
h=99500
if a== 1 :
    print('A. SAVINGS')
    print('B. CURRENT')
    b=str(input('The choice you are preferred in: '))
    if b=='A' :
        c=int(input("Enter your pin: "))
        d=int(input("the amount you are likely to take : "))
        print('THE REMAINING AMOUNT IN YOUR ACCOUNT :  ',h-d)     
    elif b=='B':
         c=int(input("Enter your pin: "))
         d=int(input("the amount you are likely to take : "))
            
elif a== 2:

    b=int(input("Enter your pin: "))
    e=int(input("the amount you are likely to give : "))
    print('THE AMOUNT IN YOUR ACCOUNT IS :',h+e)
elif a == 3 :
     J=int(input('Enter your pin: '))
     print('THE AMOUNT IN YOUR ACCOUNT IS: ',h)
