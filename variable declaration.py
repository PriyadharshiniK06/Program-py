a=34
if a==34 :
    print("global variable is declared")
else :
    print("global variable is not declared")    
def fun ():
    global c
    c=45        
fun()    
print(a)
print(c)
         
