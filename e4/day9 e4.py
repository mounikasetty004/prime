#oops
#example with constructor
#by usig return in method
'''class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def output(self):
        return self.name,self.id,self.salary
x=Employee("kittu",45,100000)
print(x.output())


y=Employee("lekha",21,200000)
print("details: ",y.output())

a=input("name:")
b=int(input("id:"))
c=int(input("salary:"))
z=Employee(a,b,c)
print(z.output())'''
#whithout constructor
#by usind method for input
#by using print in method
'''class Employee:
    def details(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def output(self):
        print("name:",self.name)
        print("id: ",self.id)
        print("salary: ",self.salary)
x=Employee()
x.details("kittu",45,100000)
x.output()

y=Employee()
y.details("lekha",21,200000)
y.output()

z=Employee()
a=input("name:")
b=int(input("id:"))
c=int(input("salary:"))
z.details(a,b,c)
z.output()'''

#class method is skipped or passed
'''class Employee:
    pass
x=Employee()
x.a=20
print(x.a)
y=Employee()
y.b=20
print(y.b)'''

#inheritance
#1.single inheritance
'''class Parent:
    def fun1(self):
        print("hi")
    def fun2(self):
        print("hello")
class child(Parent):
    def fun3(self):
        print("gm")
v=child()#creation of object
v.fun3()
v.fun2()
v.fun1()'''

#2.multiple inheritance
'''class ParentA:
    def fun1(self):
        print("hi")
    def fun2(self):
        print("hello")
class ParentB:
    def fun3(self):
        print("hiii")
    def fun4(self):
        print("hell")

class child(ParentA,ParentB):
    def fun5(self):
        print("gm")
v=child()#creation of object
v.fun3()
v.fun2()
v.fun1()
v.fun4()
v.fun5()'''

#3.multilevel inheritance
'''class ParentA:
    def fun1(self):
        print("hi")
    def fun2(self):
        print("hello")
class ParentB(ParentA):
    def fun3(self):
        print("hiii")
    def fun4(self):
        print("hell")

class child(ParentB):
    def fun5(self):
        print("gm")
v=child()#creation of object
v.fun1()
v.fun2()
v.fun3()
v.fun4()
v.fun5()'''

#4.Hierarchial inheritance
'''class ParentA:
    def fun1(self):
        print("hi")
    def fun2(self):
        print("hello")
class childA(ParentA):
    def fun3(self):
        print("hiii")
    def fun4(self):
        print("hell")

class childB(ParentA):
    def fun5(self):
        print("gm")
v=childA()
y=childB()#creation of object
v.fun1()
v.fun2()
v.fun3()
v.fun4()
v.fun5()'''

class shape:
    def area(self):
        print("every shape have area")
class circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("area:",3.14*self.r*self.r)
class square(shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        print("area: ",4*self.s)
x=[shape(),circle(3),square(4)]
for i in x:
    i.area()
    






























