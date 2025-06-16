'''import math
n=int(input("enter a number:"))
s=0
temp=n
while n>0:
    rem=n%10
    fact=math.factorial(rem)
    s=s+fact
    n=n//10
    
if(s==temp):
    print("strong number")
else:
    print("not a strong number")'''


n=int(input("enter a number:"))
s=0
temp=n
l=len(str(n))
while n>0:
    rem=n%10
    arm= pow(rem,l)
    s=s+arm
    n=n//10
    
if(s==temp):
    print("armstrong")
else:
    print("not")

