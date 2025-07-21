print('INSERT YOUR CARD')
print('The options you can do: ')
print('I. WITHDRAWAL')
print('II. DEPOSIT')
print('III. BALANCE ENQUIRY')
a=str(input('What  you are likely to do(print as it is shown): '))
h=89000
if a== 'WITHDRAWAL' :
    print('A. SAVINGS')
    print('B. CURRENT')
    b=str(input('The choice you are preferred in(print as it is showns): '))
    if b=='SAVINGS' :
        c=int(input("Enter your pin: "))
        d=int(input("the amount you are likely to take : "))
        print('THE REMAINING AMOUNT IN YOUR ACCOUNT :  ',h-d)     
    elif b=='CURRENT AMOUNT':
         c=int(input("Enter your pin: "))
         d=int(input("the amount you are likely to take : "))
            
elif a== 'DEPOSIT':

    b=int(input("Enter your pin: "))
    e=int(input("the amount you are likely to give : "))
    print('THE AMOUNT IN YOUR ACCOUNT IS :',h+e)
elif a == 'BALANCE ENQUIRY' :
     J=int(input('Enter your pin: '))
     print('THE AMOUNT IN YOUR ACCOUNT IS: ',h)
    
    
         
        
        
