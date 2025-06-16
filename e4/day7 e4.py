'''str=input("str: ")
l=[]
c=0
for i in str:
     if i not in l:
        print(i,str.count(i))
        l.append(i)
     if i in l:
        continue'''
'''
str=input("str: ")
temp=str.upper()
l=[]
c=0
for i in temp:
     if i not in l:
        print(i,temp.count(i))
        l.append(i)
     if i in l:
        continue'''
'''str=input("str: ")
n=int(input("num: "))

for i in range(0,len(str)):
        if not (i==n):
            break
        if (i!=n):
            print(str[i],end="")
else:
    print("no should be positive and lss than length ",len(str))
'''
'''str=input("str: ")
n=int(input("num: "))
if(n>=0 and n<=len(str)):
  #print(str.replace(str[n],""))
else:
    print("no should be positive and lss than length ",len(str))
            
l=input("enter: ").split()
print(l)

s=input("enter")
l=s.split()
print(l)

s=input("enter")
l=s.split()
print(l)

for i in range(0,len(l)):
    l[i]=int(l[i])
print(l)

n=int(input("n:"))
for i in range(n):
    a=int(input("enter: "))
    l.append(a)
print(l)'''

'''l1=[i for i in range(1,11)]
print(l1)

l1=[int(input()) for i in range(1,11)]
print(l1)'''
'''

l1=[i for i in range(10) if i==5]
print(l1)'''

'''l=["even" if int(i)%2==0 else "odd" for i in input("enter: ") ]
print(l)


l1=map(i,int(input("enter")))
print(l1)

l1=list(map(int,input("enter").split(" ")))
print(l1)'''

'''l1=[23,32,1,3243,32]
l2=[34,323,4,457,6]
print(l1*2+l2*2)
l1.append([7,8])
print(l1)
l1.extend([1,[2,[3]]])
print(l1)
l1.insert(1,"kittu")
print(l1)
l1.remove(23)
print(l1)
l1=['apple','v','g','i','o']
l1.sort(key=None,reverse=True)
print(l1)
l1.reverse()
print(l1)'''

'''l1=[int(i) for i in input().split(",")]
l2=[int(i) for i in input().split(",")]
l3=[]
if(len(l1)==len(l2)):
    for i in range(len(l1)):
        r=abs(l1[i]-l2[i])
        l3.append(r)
    print(l3)
else:
    print("lists are of different lenghts")'''


'''def wish():
    print("hello")
wish()

def w():
    return "hi"
print(w())

def cute():
    print("cute")
cute()'''

'''def hello():
    """hi all"""
    print("gm")
    print("gn")
def hi():
    return("kittu","c")
print(hello.__doc__)
print(hi())
hello()
print(hi())'''

#arguments and parameters
#with arguments and with parameters
''''def add(a,b):
    print(a+b)
a,b=10,20
add(a,b)'''
#keyword arguments
'''def sub(c,d):
    print(c-d)
a=int(input("enter"))
b=int(input("enter"))
sub(d=a,c=b)
sub(c=b,d=a)
sub(c=a,d=b)'''
#default arguments
'''def fun1(c="kittu",d=1):
    print(c,d)
fun1("lekha",2)
fun1()
fun1(d=25)'''#keyword argument

#sum of natural numbers
'''def sum(n,s):
    for i in range(1,n):
        s=s+i
    print(s)
n=int(input("enter a number"))
s=0
sum(n,s)'''

#factorial numbers
'''def fact(a,facto):
    for i in range(1,a):
        facto=facto*i
    return facto
a=int(input("enter a num"))
facto=1
print(fact(a,facto))'''

#anonymous functions
s=lambda a,b,c:a+b+c
a,b,c=1,2,3
print(s(a,b,c))
print(s(10,20,30))






















































































































































































        
    
   
