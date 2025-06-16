                       #data structures
#searching
###using methods
#using membership(in,not in)
'''l=list(map(int,input("enter elements").split(" "))) 
a=int(input("enter a element"))
if(a in l):
    print("true element is in list")
else:
    print("false element is not in list")

print(a in l)'''

#using index()
'''l=[int(i) for i in input("enter numbers").split(" ")]
s=int(input("eneter  element to search:"))
a=l.index(s)
print(a)'''

###without using methods
#linear searching
'''l=input("enter elements:").split(" ")
a=int(input("enetr search element"))
for i in range(0,len(l)):
    l[i]=int(l[i])
print(l)
for i in range(0,len(l)):
    if(l[i]==a):
        print("element is found in",i)
        break
else:
    print("not found")'''

#sorting using methods

#sorted()
'''l=[5,4,3,2,1]
print(l)
l1=sorted(l)
print(l)
print(l1)'''

#.sort()
'''l=[100,433254,565,213,23,98]
print(l)
l.sort()
print(l)'''

#bubble sorting
'''l=[1,53,75,46,867,8345,231,1]
n=len(l)
for i in range(n):
    for j in range(n-i-1):
       if l[j]>l[j+1]:
           l[j],l[j+1]=l[j+1],l[j]
print(l)'''

#binary search
'''l=list(map(int,input("enter elements:").split(" ")))
s=int(input("enter search elemnt"))
n=len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
           l[j],l[j+1]=l[j+1],l[j]
print(l)
le=0
r=len(l)-1
while(le<=r):
    mid=(le+r)//2
    if(s==l[mid]):
        print("element found at:",mid)
        break
    elif(s>l[mid]):
        le=mid+1
    elif(s<l[mid]):
        r=mid-1
    else:
        print("not found")
else:
    print("element not found")'''


###linked list
#SLL
#inserting new node at begining
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.lastnode=None#optional
    def insertatfirst(self,x):
        newnode=Node(x)  #object to create node 
        newnode.next=self.head
        self.head=newnode
    def display(self):
        if self.head is None:
            print("linked list is empty")
            return #is nothing but break
        else:
            t=self.head
            while t is not None:
                print(t.data,end=" ")
                t=t.next
        print()
a=SLL()
a.display()
a.insertatfirst(10)
a.insertatfirst(20)
a.insertatfirst(30)
a.insertatfirst(40)
a.display()

    






















