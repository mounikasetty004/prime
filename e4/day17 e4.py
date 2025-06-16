#####Stack
##basic methods of list
'''l=[]
l.append(10)
print(l)
for i in range(5):
    a=int(input())
    l.append(a)
print(l)
l.remove(6)
print(l)
b=l.pop()
print(l)
print(b)
del l[0]
print(l)
is_empty=len(l)==0
print(is_empty)
print(len(l))'''

#with OOPS  Concept:

'''class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if self.is_empty():
            print("list is empty")
        return self.items.pop()
    def delete(self,data):
        del self.items[data]
    def remove(self,data):
        self.items.remove(data)
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        print(len(self.items))
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("\nstack elements are:")
            for data in self.items:
                print(data,end=" ")
a=Stack()
print("enter elements: ")
for i in range(6):
    b=int(input())
    a.push(b)
a.is_empty()
a.size()
a.display()
a.pop()
a.display()
a.delete(3)
a.display()
a.remove(1)
a.display()

c=Stack()
while(1):
    print("\nenter the option \n1. push \n2.pop\n3.del\n4.remove\n")
    str=input()
    if str=="1":
        print("Push")
        n=int(input("enter value"))
        c.push(n)
        c.display()
    elif str=="2":
        print("pop")
        c.pop()
        c.display()
    elif str=="3":
        key=int(input("enter key to remove"))
        print("delete")
        c.delete(key)
        c.display()
    elif str=="4":
        print("remove")
        c.remove(12)
        c.display()
    else:
        print("enter correct option")
        break'''

##linked lists
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self):
        data=int(input("enter the value to be inserted"))
        newnode=Node(data)
        if self.top==None:
            self.top=newnode
            self.top.next=None
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.top is None:
            print("stack is empty")
        elif self.top.next is  None:#single node
            print("Popped element is",self.top.data)
            self.top=None
        else:#more nodes
            temp=self.top
            print("popped element is",self.top.data)
            self.top=temp.next
            temp=None
    def display(self):
        if self.top is None:
            print("stack is empty")
        else:
            print("the elements are:")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("Top of the stack is:",self.top.data)
a=Stack()
a.push()
a.push()
a.push()
a.push()
a.display()
a.pop()
a.display()'''

###fixed size stack
'''class fixedsizestack():
    def __init__(self,maxsize):
        self.stack=[0]*maxsize
        self.top=-1 #empty
        self.maxsize=maxsize

    def isfull(self):
        return self.top==self.maxsize-1
    def isempty(self):
        return self.top == -1
    def push(self):
        data=int(input("enter element to be inserted"))
        if self.isfull():
            print("stack is full")
        else:
            self.top=self.top+1
            self.stack[self.top]=data
            print(f"pushed {data}into the stack")
    def pop(self):
        if self.isempty():
            print("stack is empty ,we can not pop")
        else:
            data=self.stack[self.top]
            self.top= self.top-1
            print(data,"is popped from stack")
            return data
    def peek(self):
        if self.isempty():
            print("stack is empty ,we can not pop")
            return None
        else:
            print("Top element",self.stack[self.top])
            return self.stack[self.top]
    def display(self):
         if self.isempty(): 
            print("stack is empty ")
            return None
         else:
             print("stack elements: ",self.stack[:self.top+1])
a=fixedsizestack(5)
a.push()
a.push()
a.push()
a.push()
a.push()
a.display()
a.pop()
a.display()'''

###two stack with fixed
class TwoStackFixedSize:
    def __init__(self,n):
        self.size=n
        self.array=[None]*n
        self.mid=(n+1)//2
    def pop2(self):
        if self.pop(56):
           
    

                



