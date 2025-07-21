def fun():
    print("hello")
fun()



'''f- string method :-'''
def fun(name,age):
    print(f"my name is {name}, my age is {age}")
    #print(name,age)
fun("rose",25)


#function with 2 arguments:-
def fun(name,age):
    print(name,age)
fun("girija",35)


#it takes the number with its index number:
def fun(*name):
    print("the name of the second student out of 5 students is: ",name[2])
fun("rose","sunflower","jasmine","lotus","lilly")

"""function with keyword arguments:-"""
def fun(a1,a2,a3):
    print("my variable a3 is",a3)
fun(a3="free",a1="fell",a2="hi")

"""arbitrary keyword arguments:-"""
def function(**a):
    print(f"my name is "+a["fname"],"my age is"+ a["age"])
function(fname="hi",age="rose")



"""default parameter value in a function"""

def fun(a="one"):
    print("the function carries: ",a)
fun("two")
fun()




    

    
