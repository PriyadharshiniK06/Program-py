'''EXPERIMENT 2A
#EXCHANGE THE VALUE OF TWO VARIABLES
a=45
b=78
print("The a value before exchange of value: ", a)
print("the b value before swapping of value: ",b)

a,b=b,a

print("The a value after swapping is: ",a)
print("The b value after swapping is: ",b)'''


'''EXPERIMENT 2B'''
#CIRCULATE THE VALUE OF N VARIABLES
'''n=int(input("Enter the range: "))
list=[]
for a in range(0,n,1):
    b=int(input("Enter integer: "))
    list.append(b)
print("Circulating the elements: ",list)
for a in range(0,n,1):
    b=list.pop(0)
    list.append(b)
    print(list)'''

'''EXPERIMENT 2C'''
#CALCULATE THE DISTANCE BETWEEN THE TWO POINTS
'''import math'''
'''a1=int(input("Enter the integer: "))
a2=int(input("Enter the integer: "))
b1=int(input("enter the integer : "))
b2=int(input("Enter the integer: "))
da=a1-a2
db=b1-b2
d=da**2+db**2
result=math.sqrt(d)
print("Distance between two points: ",result)'''

#EXPERIMENT 3A
#NUMBER SERIES
'''n=int(input("Enter the range of number series: "))
i=1
s=0
while i<=n:
    s=s*2+1
    print(s,sep='')
    i+=1'''
    

#EXPERIMENT 3B
#NUMBER PATTERNS
'''rows=int(input("Enter the number of rows: "))
for a in range (1,rows+1):
    for b in range (1,a+1):
        print(a,end='')
    print('\n')'''

#EXPERIMENT 3C
#PYRAMID

def pyramid(n):
  for i in range (0,n):
    for j in range(0,n-i-1):
      print(end=" ")
    for j in range (0,2*i+1):
      print("*",end="")
    print()
n=int(input("Enter the number: "))
pyramid(n) 




def pyramid(N):
    for i in range(0,N):
        for j in range(0,N-i-1):
            print(end=" ")
        for j in range(0,2*i+1):
            print("*",end=" ")
            print()
            
N=int(input("enter the range:"))
pyramid(N)
    


'''EXPERIMENT 4A'''

#CREATE A  LIST  AND CHANGE THE ITEMS IN A LIST AND PRINT THE LIST


#CREATE TWO TUPLES AND CHANGE THE FIRST ELEMENT OF THE TUPLE AND COMBINE THE TWO TUPLES AND PRINT THE COMBINED TUPLE



'''EXPERIMENT 4B'''

#CREATE A LIST AND CREATE A NEW EMPTY LIST AND USING FOR OPERATION COMBINE THE WORDS THAT START WITH PARTICULAR LETTER AND APPEND IT TO THE NEW EMPTY LIST AND PRINT THE LIST.
#CREATE  A TUPLE AND PRINT THE TUPLE AND PRINT THE ELEMENTS OF THE TUPLE SEPERATELY AND PARTICULARLY USING THEIR INDEX NUMBER

'''EXPERIMENT 4C'''

Te



