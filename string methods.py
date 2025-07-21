a=str(input("Enter any string:"))
print("the string with start and end: ",a[3:6])
print("the string from the start: ", a[:4])
print("the string with start and till the end: " , a[1::])
print("the string with negative slicing: " , a[-5:-3])
print("the uppercase string is:",a.upper())
b=str(input("Enter any string: "))
print("the lowercase string is:",b.lower())
c="  hello, world"
print("the whitespace before the string is removed:",c.strip())
print("the replaced word:",c.replace("d", "g"))
print("the splited two strings are:",c.split())
d="hi"
e="world"
f=d+e
print("the joined string is:",f)
g=d+"  "+e
print("the string with whitespace:",g)
      
