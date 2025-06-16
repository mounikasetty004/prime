#test answers
'''n=5
c=0
for i in range(1,n+1):
   
    for spaces in range(2*(n-i)):
        print(" ",end="")
    
    for j in range(2*i-1):
        
        if j<i:
            c=c+1   
        else:
            c=c-1
        print(c,end=" ")
    print()'''

'''n=int(input("enter a number"))
c=0
v=0
if n>=0 and n<=((2**31)-1):
    for i in range(n):
        for j in range(n):
            c=(i**2)+(j**2)
            if c==n:
                v=v+1
if v==0:
    print("false")
else:
    print("true")'''

#numbers as alphabet code
'''n=int(input("enter a number"))
m=[]
n=n-1
while n>=0:
    rem=n%26
    m.append(chr(rem+ord("A")))
    n=n//26-1
m.reverse()
for i in m:
    print(i,end=" ")'''

##roman numbers
'''l1=[1000,900,500,400,100,50,40,10,9,5,4,1]
r1=["M","CM","D","CD","C","L","XL","X","IX","V","IV","I"]
r=" "
n=int(input("enter no:"))
i=0
while n>0:
    rem=n//l1[i]
    r=r+r1[i]*rem
    n=n%l1[i]
    i=i+1
print(r)'''

'''l=[]
for i in range(3):
    l1=[]
    for j in range(3):
        a= int(input(""))
        l1.append(a)
    l.append(l1)
for i in range(3):
    for j in range(3):
        print(l[i][j],end=" ")
    print()
for i in range(3):
    for j in range(i,3):
        l[i][j],l[j][i]=l[j][i],l[i][j]
    print()
for i in l:
    print(*i)
for i in l:
    i.reverse()
    print(*i)'''
l=[]
for i in range(3):
    a=input().split()
    l.append(a)
for i in l:
    print(*i)






















        
