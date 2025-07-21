'''RETURN FUNCTION'''
def fun(x):
    return 6+x
print(fun(8))


'''LAMBDA FUNCTION'''
'''basic'''

a=lambda x : x*4
print(a(5))

'''MULTIPLE ARGUMENTS IN LAMBDA FUNCTION'''
A = lambda x,y,z : x*y*z
print(A(5,6,7))

'''function with lambda function'''
def fun(n):
    return lambda f : f*n
'''x=fun(45)
print(x(4))'''
print(fun(45))

'''function with lambda function with  two or more parameters'''

def fun(n,m):
    return lambda v,y,h:v+y-n+h+m
s=fun(3,4)
print(s(7,8,9))
