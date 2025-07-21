

'''with init
class a:
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def person(self):
        print(self.c,self.d)
        
class b(a):
    def __init__(self,c,d):
       
       #super().__init__(c,d)
        #a.__init__(self,c,d)
        
obj= b(12,34)
print(obj.c,obj.d)'''

'''withoutinit'''
class A:
    def student(strill):
        print("student!")
class B(A):
    def school(strill):
        print("bell")
obj=B()
obj.school()
obj.student()
        


        
    
   

