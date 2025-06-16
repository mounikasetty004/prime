###Queue
'''queue=[]
for i in range(5):
    n=int(input())
    queue.append(n)
print(queue)

front_element=queue.pop()
print(front_element)
print(queue)

front_element=queue[0]
print(front_element)

rare_element=queue[-1]
print(rare_element)

is_empty=len(queue)==0
print(is_empty)

size=len(queue)
print(size)

q=[]
a=q.pop(0)
print(a)'''

###using function
'''queue=[]
def enqueue():
    n=int(input("enter to be inserted"))
    queue.append(n)
def dequeue():
    if is_empty():
        print("queue is empty.we can't pop")
    else:
        a=queue.pop(0)
        print("deleted element is",a)
def is_empty():
    return len(queue)==0
def size():
    print(len(queue))
def display():
    if is_empty():
        print("list is empty")
    else:
        print("the queue elements are:")
        for i in queue:
            print(i,end=" ""\n")
        print("front element is",queue[0])
        print("rare element is",queue[-1])
display()
dequeue()
enqueue()
enqueue()
enqueue()
display()
dequeue()
display()
is_empty()
size()
while(1):
    print("enter option \n 1.enqueue \n 2.dequeue \n 3.display \n 4. empty \n 5.size")
    str=input()
    if(str=="1"):
        enqueue()
    elif(str=="2"):
        dequeue()
    elif(str=="3"):
        display()
    elif(str=="4"):
        print(is_empty())
    elif(str=="5"):
        size()
    else:
        print("enter correct option")
        break'''
###fixed size queue
'''max_size=5
queue=[]
def enqueue(queue,max_size,data):
    if is_full():
        print("queue is full")
    else:
        queue.append(data)
        print(f"{data} is inserted")
def is_full():
    return len(queue)>=max_size
def is_empty():
    return len(queue)==0
def dequeue(queue):
    if is_empty():
        print("queue is empty. can't pop")
    else:
        queue.pop(0)
        print(queue[0],"is popped ")
def display():
    if is_empty():
        print("queue is empty.")
    else:
        print("the elements are:")
        for i in queue:
            print(i,end=" ""\n")
while(1):
    print("enter option \n 1.enqueue \n 2.dequeue \n 3.display \n 4. empty \n 5.full")
    str=input()
    if(str=="1"):
        data=int(input("enter the elemrnt to insert"))
        enqueue(queue,max_size,data)
    elif(str=="2"):
        dequeue(queue)
    elif(str=="3"):
        display()
    elif(str=="4"):
        print(is_empty())
    elif(str=="5"):
        print(is_full())
    else:
        print("enter correct option")
        break'''
###Types of queue
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rare=None
    def enqueue(self):
        data=int(input("enter data to be inserted"))
        newnode=Node(data)
        if self.front is None:
            self.front=newnode
            self.rare=newnode
            print("data inserted ",self.front.data)
        else:
            self.rare.next=newnode
            self.rare=newnode
            print("data inserted ",newnode.data)

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            if self.front.next is None:
                print("Popped element",self.front.data)
                self.front=None
               
            else:
                t=self.front
                print("Popped element",self.front.data)
                self.front=t.next
                t=None
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            t=self.front
            print("elements are")
            while t is not None:
                print(t.data,end=" ")
                t=t.next
            print()
            print("front element",self.front.data)
            print("rare element",self.rare.data)
a=Queue()
while(1):
    print("enter option \n 1.enqueue \n 2.dequeue \n 3.display ")
    str=input()
    if(str=="1"):
        a.enqueue()
    elif(str=="2"):
        a.dequeue()
    elif(str=="3"):
        a.display()
    else:
        print("enter correct option")'''

##Queue using two stacks
'''stack1=[]
stack2=[]
def enqueue():
    data=int(input("enter element to be inserted"))
    stack1.append(data)
    print("element inserted",data)
def dequeue():
    if len(stack2)==0:
        while stack1:
            stack2.append(stack1.pop())
        return stack2.pop()
    else:
        return stack2.pop()
def peek():
    if len(stack2)==0:
        while len(stack1)!=0:
            stack2.append(stack1.pop())
        return stack2[-1]
    else:
        return stack2[-1]
def is_empty():
    return len(stack1)==0 and len(stack2)==0
def display():
    if is_empty():
        print("queue is empty")
    else :
        print("queue")
        for i in stack1:
            print(i,end=" ")
        for i in stack2[::-1]:
            print(i,end=" ")
while(1):
    print("enter option \n 1.enqueue \n 2.dequeue \n 3.display\n 4.peek\n 5.empty")
    str=input()
    if(str=="1"):
        enqueue()
    elif(str=="2"):
        dequeue()
    elif(str=="3"):
        display()
    elif(str=="4"):
        print(peek())
    elif(str=="5"):
        print(is_empty())
    else:
        print("enter correct option")
        break'''

###Circular queue
'''class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def is_full(self):
        return (self.rear+1==self.size and self.front==0) or (self.rear+1==self.front)
    def is_empty(self):
        return self.rear==self.front==-1
    def enqueue(self,data):
        if self.is_full():
            print("Queue is overflow")
            return
        if self.is_empty():
            self.front=0
        if self.rear+1==self.size:
            self.rear=0
        else:
            self.rear+=1
        self.queue[self.rear]=data
        print(f"Element enqueued:{data}")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        data=self.queue[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            if self.front+1==self.size:
                self.front=0
            else:
                self.front+=1
            print(f"Dequeue:{data}")
    def peek():
        if is_empty():
            print("queue is empty")
            return None
        return self.queue[self.front]
    def display(self):
        if self.is_empty():
            print("queue is empty")
            return None
        if self.rear>=self.front:
            print("queue :",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
        else:
            print("QUEUE elements are:")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
size=int(input("enter size"))
a=CircularQueue(size)
while(1):
    print("\n enter option \n 1.enqueue \n 2.dequeue \n 3.display\n 4.peek\n 5.empty")
    str=input()
    if(str=="1"):
        data=int(input("enter data to be inserted"))
        a.enqueue(data)
    elif(str=="2"):
        a.dequeue()
    elif(str=="3"):
        a.display()
    elif(str=="4"):
        a.print(peek())
    elif(str=="5"):
        a.print(is_empty())
    else:
        print("enter correct option")
        break '''
def prefix(l):
    if not l:
        return " "
    l.sort()
    print(l)
    first_string=l[0]
    last_string=l[-1]
    common_prefix=" "
    for i in range(min(len(first_string),len(last_string))):
        if first_string[i]==last_string[i]:
             common_prefix+=first_string[i]
        else:
             break
    return common_prefix
                   
    
l=["flower","floy","floo","face","eat"]
print(prefix(l))

        
    












