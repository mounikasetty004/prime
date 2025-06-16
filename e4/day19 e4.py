###linked list of circular queue
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularQueue():
    def __init__(self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.front=newnode
            self.rear=newnode
            self.rear.next=self.front#to form like a circle
        #print("enqueue: ",data)
        else:
            self.rear.next=newnode#updating address to the previous.next
            self.rear=newnode##in queue we add elements at the rear
            self.rear.next=self.front##to form like a circle
        print("enqueue: ",data)
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        data=self.front.data
        if self.front==self.rear:##it means there  is only one element. 
            self.front=None #so if we make as none then automatically it is deleted
            self.rear=None
        else:
            self.front=self.front.next#for deleting we just madefront.next as None
            self.rear.next=self.front#to form circle
        print(f"Dequeue:{data}")
    def peek(self):
        return self.front.data
    def display(self):
        if self.is_empty():
            print("queue is empty")
            return None
        else:
            t=self.front
            print("elements are:")
            while True:
                print(t.data,end=" ")
                t=t.next
                if t==self.front:
                    break
a=CircularQueue()
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
        print(a.peek())
    elif(str=="5"):
        print(a.is_empty())
    else:
        print("enter correct option")
        break'''

##trees
###Binary tree
'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert_recursion(self.root,data)
    def insert_recursion(self,current_node,data):#here current_node is self.root
        if current_node.left is None:
            current_node.left=Node(data)
        elif current_node.right is None:
            current_node.right=Node(data)
        else:
            self.insert_recursion(current_node.left,data)
    def inorder(self):
        return self.inorder_traversal_recursion(self.root)

    def inorder_traversal_recursion(self,current_node):
        if current_node is None:
            return[]
        return (self.inorder_traversal_recursion(current_node.left))+[current_node.data]+(self.inorder_traversal_recursion(current_node.right))
    def preorder(self):
        return self.preorder_traversal_recursion(self.root)

    def preorder_traversal_recursion(self,current_node):
        if current_node is None:
            return[]
        return [current_node.data]+(self.preorder_traversal_recursion(current_node.left))+(self.preorder_traversal_recursion(current_node.right))
    def postorder(self):
        return self.postorder_traversal_recursion(self.root)

    def postorder_traversal_recursion(self,current_node):
        if current_node is None:
            return[]
        return (self.postorder_traversal_recursion(current_node.left))+(self.postorder_traversal_recursion(current_node.right))+[current_node.data]
        
a=BinaryTree()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
print("inorder",a.inorder())
print("preorder",a.preorder())
print("postorder",a.postorder())'''

##binary search tree 
'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insertion_recursion(self.root,data)
    def insertion_recursion(self,current_node,data):
        if data<current_node.data:
            if current_node.left is None:
                current_node.left=Node(data)
            else:
                self.insertion_recursion(current_node.left,data)
        else:
            if current_node.right is None:
                current_node.right=Node(data)
            else:
                self.insertion_recursion(current_node.right,data)
    def search(self,data):
        return self.search_recursion(self.root,data)
    def search_recursion(self,current_node,data):
        if current_node.data == data or current_node is None:
            return current_node.data
        if data<current_node.data:
            return self.search_recursion(current_node.left,data)
        else:
            return self.search_recursion(current_node.right,data)
    def inorder(self):
        return self.inorder_traversal_recursion(self.root)

    def inorder_traversal_recursion(self,current_node):
        if current_node is None:
            return[]
        return (self.inorder_traversal_recursion(current_node.left))+[current_node.data]+(self.inorder_traversal_recursion(current_node.right))
    def preorder(self):
        return self.preorder_traversal_recursion(self.root)

    def preorder_traversal_recursion(self,current_node):
        if current_node is None:
            return[]
        return [current_node.data]+(self.preorder_traversal_recursion(current_node.left))+(self.preorder_traversal_recursion(current_node.right))
    def postorder(self):
        return self.postorder_traversal_recursion(self.root)

    def postorder_traversal_recursion(self,current_node):
        if current_node is None:
            return[]
        return (self.postorder_traversal_recursion(current_node.left))+(self.postorder_traversal_recursion(current_node.right))+[current_node.data]
a=BST()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
print("inorder",a.inorder())
print("preorder",a.preorder())
print("postorder",a.postorder())
data=6
found_node=a.search(data)
if found_node:
    print(f"Node with value {data}")
else:
    print("not found")'''
###












    
    

        

























            
