class ABC:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        h=self.a
        self.a +=1
        return h
obj= ABC()
f= iter(obj)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

'''class A:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=25:
            d=self.a
            self.a +=1
            return d
        else:
            raise StopIteration
myiter=A()
c= iter(myiter)
for d in c:
    print(d)'''
       
