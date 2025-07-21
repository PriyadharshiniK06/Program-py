print ( student details)
tamil1=int(input("Enter your mark in first subject:"))
english1=int(input("Enter your mark in second subject:"))
science1=int(input("Enter your mark in third subject:"))
social1=int(input("Enter your mark in fourth subject:"))
maths1=int(input("Enter your mark in fifth subject:"))

maths2=int(input("Enter your mark in maths:"))
english2=int(input("Enter your mark in english:"))
science2=int(input("Enter your mark in science:"))
social2=int(input("Enter your mark in social:"))
tamil2=int(input("Enter your mark in tamil:"))

maths3=int(input("Enter your mark in maths:"))
english3=int(input("Enter your mark in english:"))
science3=int(input("Enter your mark in science:"))
social3=int(input("Enter your mark in social:"))
tamil3=int(input("Enter your mark in tamil:"))

              
a=tamil1+english1+science1+social1+maths1
print("total of first student is:",a)
b=a/5
print("percentage of first student is:  ",b,"%")
c=tamil2+english2+science2+social2+maths2
print("total of second student is:",c)
d=c/5
print("percentage of second student is:",d,"%")

e=tamil3+english3+science3+social3+maths3
print("total of third student  is:",e)
f=e/5
print("percentage of third student is:",f,"%")


if a>c:
    if a>e:
        print("first student has got the first mark")
    
if b>a:
    if b>e:
        print("second student has got the first mark")
        
if e>a: 
    if e>c:
        print("third student has got the first mark")



























    
    
