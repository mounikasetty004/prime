#reverse
'''def rev(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(n//10))
n=1009
print(rev(n))'''

#palindrome
'''def rev(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(n//10))
n=1009
r=rev(n)
print(r)
if(r==n):
    print("palindrome")
else:
    print("not a palindrome")'''
#addition
'''def add(a,b):
    if a==0:
        return b
    if b==0:
        return a
    else:
        if(a>b):
            return 1+add(a,b-1)
        else:
            return 1+add(a-1,b)
a=int(input("a:"))
b=int(input("b:"))
print(add(a,b))'''

###patterns
'''for i in range(0,5):
    for j in range(0,5):
        print("*",end=" ")
    print("\n ")'''

'''n=int(input("enter a no:"))
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print("\n ")

n=int(input("enter a no:"))
v=1
for i in range(n):
    for j in range(n):
        print(v,end=" ")
        v=v+1

    print("\n ")'''

'''n=int(input("enter a no:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("\n ")'''

'''n=int(input("enter a no:"))
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print("\n ")'''

'''n=int(input("enter a no:"))
for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")    
    for j in range(i):
        print("*",end=" ")
    print("\n ")'''

'''n=int(input("enter a no:"))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
             print("*",end=" ")    
        else:
            print(" ",end=" ")
    print()'''

'''n=int(input("enter a no:"))
for i in range(n):
    for space in range(n):
        print(" ",end=" ")    
    for j in range(i):
        print("*",end=" ")
    print("\n ")'''

'''n=int(input("enter a no:"))
for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")    
    for j in range(2*i-1):
        print("*",end=" ")
    print("\n ")'''


#day 11
'''n=int(input("enter a no:")
for i in range(n):
    for space in range(i):
        print(" ",end=" ")
    for j in range(2*n-2*i-1):
        print("*",end=" ")
    print("\n")'''


'''n=int(input("enter a no:"))
for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")    
    for j in range(2*i-1):
        print("*",end=" ")
    print("\n ")
for i in range(n+1):
    for space in range(i):
        print(" ",end=" ")
    for j in range(2*n-2*i-1):
        print("*",end=" ")
    print("\n")'''


'''n=int(input("enter:"))
for i in range(1,2*n):
    if i<=n:
        star=i
    else:
        star=2*n-i
    print(star*"*",end=" ")
    print()'''

'''n=int(input("enter a no:"))
for i in range(n):
    for space in range(n-i):
        print(" ",end=" ")    
    for j in range(i):
        print("*",end=" ")
    print("\n ")
for i in range(n):
    for space in range(i):
        print(" ",end=" ")    
    for j in range(n-i):
        print("*",end=" ")
    print("\n ")'''

'''n=int(input("enter no:"))
for i in range(1,n+1):
    for space in range(n-i):
        print("1",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()'''
'''n=9
for i in range(n):
    for space in range(i):
        print(" ",end=" ")    
    for j in range(n-i):
        print("*",end=" ")
    print("\n ")'''

'''n=int(input("enter:"))
size=2*n-1
for i in range(size):
    for j in range(size):
        v=n-min(i,j,size-1-i,size-1-j)
        print(v,end=" ")
    print()'''

'''n=int(input("enter :"))
v=1
for i in range(n):
    for j in range(i+1):
        print(v,end=" ")
        v=v+1
    print()'''
#traingle(pascals)
n=5
for i in range(n):
    for spaces in range(n-i):
        print("",end=" ")
    c=1
    for j in range(i+1):
        print(c,end=" ")
        c=c*(i-j)//(j+1)
    print()
