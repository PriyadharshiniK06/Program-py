'''LOCAL VARIABLE
def fun():
    x=56
    print(x)
fun()'''

'''LOCAL VARIABLE WITH FUNCTION INSIDE FUNCTION'''
'''def fun():
    x=4
    def inner():
        print(x)
    inner()
fun()'''  '''can be accessed in outer function only'''    
'''GLOBAL VARIABLE'''
''' 1. x=45
def fun():
    print(x)
fun()  '''
'''2. x=234
def fun():
    print(x)
fun()
print(x)'''
'''def fun():
    global x
    x=456
    print(x)
fun()
print(x)'''
'''NON LOCAL VARIABLE'''
def fun():
    x="tesla"
    def func():
        nonlocal x
        x="their"
    func()
    return x
    '''func()'''
print(fun())

