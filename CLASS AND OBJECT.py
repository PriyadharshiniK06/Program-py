class a:
    f=67
print(a)

class A:
    x=56

a= A()
print(a.x)

class B:
    def __init__(self,b,c):
        self.b=b
        self.c=c
d=B(45,34)
print(d.b)
print(d.c)

class C:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):

        return f"{(self.a) , (self.b) }"
g=C(67 , 98)
print(g)



