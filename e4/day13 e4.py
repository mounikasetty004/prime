#zeroes at last
'''l=input("enter the list").split(" ")
l2=[]
l1=[]
for i in range(0,len(l)) :
    l[i]=int(l[i])
    
    if(l[i]==0):
        l1.append(l[i])
    else:
        l2.append(l[i])
print(l2+l1)'''
'''
s=input("enter a string")
s1=" "
s2=" "
for i in range(0,len(s)):
    if(s[i]=="0"):
        s1=s[i]
        
    else:
        s2=s[i]
print(s1+s2)'''

#matrix in python
#direct input
'''l1=[[1,2,3],[4,5,6],[4,6,7],[23,3,4]]
print(l1)
for i in l1:
    print(i)'''


#indirect size
'''n=int(input("size"))
l=[]
for i in range(n):
    v=[]
    for j in range(n):
        v.append(0)
    l.append(v)
print(l)
for i in l:
    print(i)'''
#indirect values
'''n=int(input("size"))
l=[]
for i in range(n):
    v=[]
    for j in range(n):
        a=int(input("enter"))
        v.append(a)
    l.append(v)
print(l)
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()'''
#different sizes of matrix(rows,col)
'''m=int(input("size for row"))
n=int(input("size for col"))
l=[]
for i in range(m):
    v=[]
    for j in range(n):
        a=int(input())
        v.append(a)
    l.append(v)
print(l)
for i in range(m):
    for j in range(n):
        print(l[i][j],end=" ")
    print()'''

#method with map,comprehension
'''r,c=list(map(int,input("enter: ").split(" ")))#map
#r,c=input("enter row,col").split(" ")
l=[[int(input(" ")) for j in range(c)]for i in range(r)]
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print()'''
#printing numbers
'''r,c=list(map(int,input("enter: ").split(" ")))#map
#r,c=input("enter row,col").split(" ")
l=[[int(input("")) for j in range(c)]for i in range(r)]

for i in range(c):
    for j in range(r):
        print(l[j][i],end=" ")
    print()'''

#identity matrix
'''r,c=list(map(int,input("enter: ").split(" ")))#map
#r,c=input("enter row,col").split(" ")
l=[[int(input("")) for j in range(c)]for i in range(r)]

for i in range(r):
    for j in range(c):
        if(i==j):
            l[i][j]=1        
        print(l[i][j],end=" ")
    print()'''
#identity
'''m=int(input("size for row"))
n=int(input("size for col"))
l=[]
for i in range(m):
    v=[]
    for j in range(n):
        
        if(i==j):
            v.append(1)
        v.append(0)
    l.append(v)
print(l)
for i in range(m):
    for j in range(n):
        print(l[i][j],end=" ")
    print()'''
#identity increase
'''m=int(input("size for row"))
n=int(input("size for col"))
l=[]
c=0
for i in range(m):
    v=[]
    for j in range(n):
        if(i==j):
            c=c+1
            v.append(c)
        v.append(0)
    l.append(v)
print(l)
for i in range(m):
    for j in range(n):
        print(l[i][j],end=" ")
    print()'''
#using map()
'''n=4
l=[[1 if i==j else 0 for j in range(n)]for i in range(n)]
print(l)
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()'''

#1 0 1
#0 1 0
#1 0 1
'''n=5
l=[[1 if (i+j)%2==0 else 0 for j in range(n)]for i in range(n)]
print(l)
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()'''
#diagonals 1
'''n=int(input("enter:"))
if(n%2!=0):
    l=[[1 if i==j or j==n-i-1 else 0 for j in range(n)]for i in range(n)]
    
    print(l)
    for i in range(n):
        for j in range(n):
            print(l[i][j],end=" ")
        print()'''
#diamond 1
n=int(input("enter:"))
l=[[1 if j==n-i-3 or j==n-i+1 or j==n+i-3  else 0 for j in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()
#count capitals and smalls in a string
'''s=input("enter a string")
c=0
d=0
for i in s:
    if(i.isupper()):
        c=c+1
    elif(i.islower()):
        d=d+1
    else:
        continue
print(c,d)'''
#extracting company name from mail which is btw @ and .
'''s=input("enter a mail id:")
a=s.index("@")
b=s.index(".")
print(s[a+1:b])'''

#pangarm:all 26 leters in a sentence
'''s=input("enter a sentence")
s1=s.lower()
s2=" "
c=0
for i in s1:
    if i not in s2:
        s2=s2+i
        if(i.isalpha()):
            c=c+1
    else:
        continue
if(c==26):
    print("panagram")
else:
    print("not a pangram")'''
#anagram
'''a=input("enter")
b=input("enter another:")
c=0
d=" "
if(len(a)!=len(b)):
    print("not anagram")
else:
   for i in a:
        for j in b:
            if(i==j and j not in d):
                d=d+i
                print(" anagram")
             
                      
    else:
        print("not anagram")'''
#move hyphens to front
'''s=input("enter:")
s1=" "
s2=" "
for i in s:
    if(i=="-"):
        s1=s1+i
    else:
        s2=s2+i
print(s1+s2)'''
#password character
'''s=input("enter password")
a=s[0]
sp=0
u=0
d=0
if(len(s)>=4) and a.isalpha():
    for i in range(len(s)):
        if(s[i]==" " or s[i]=="/"):
            sp=sp+1
        if(s[i].isupper()):
            u=u+1
        if(s[i].isdigit()):
            d=d+1
    if(sp==0 and d>=1 and u>=1):
        print("proper pass")
    else:
        print("not valid")
    
else:
    print("not a proper pass")'''

'''n=int(input("enter size:"))

#r,c=input("enter row,col").split(" ")
l=[[int(input("")) for j in range(n)]for i in range(n)]

print(l)
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()
m=[[l[j][i] for j in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        print(m[i][j],end=" ")
    print()
k=[[m[i][::-1] for j in range(i)]for i in range(n)]  
for i in range(n):
   for j in range(n):
        print(k[i][j],end=" ")
   print()'''
   
   
        
    



    

        
