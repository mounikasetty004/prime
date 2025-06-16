#tuples
'''list1=input("enter:").split(",")
t=tuple(list1)
print(t)'''

#direct input
'''t1=(1,"kittu",80.7,80,1)
print(t1)
print(type(t1))
print(t1[1][4])'''#indexing
#problems
'''list1=[10,20,30,40,50,50,10,20,30,40]
t=tuple(list1)
print(t)

data=input("data: ").split(",")
print("list:",data)
t=tuple(data)
print("tuple:",t)

data=input("data: ").split(",")
print("list: ",data)
t=tuple(data)
print("tuple: ",t)
i=int(input("enter index: "))
if(i<len(t) and i>=-len(t)):
    print(t[i])
else:
    print("invalid index")'''
#dictionary
'''d={}
print(type(d))
d1={1:10,2:20,3:30}
print(d1)
d2={"a":100,"b":200,"c":300}
print(d2)
d2={"a":100,500:200,"c":300}
print(d2)
d2={"a":100,"b":100,"b":300}
print(d2)
print(d1.keys())
print(d1.values())
print(sorted(d1.items()))
for i,j in sorted(d1.items()):
    #print(i,j)
    #print(j,i)
    print(i,"->",j)
d1[1]="lekha"
print(d1)

print(d1.get(2))
d1.pop(3)
print(d1)'''
#using zip
'''k=input("keys: ").split(" ")
v=input("values: ").split(" ")
d=dict(zip(k,v))
print(d)
print(sorted(d.items()))
for i,j in sorted(d.items()):
    print(i,j)'''
#recursions
#palindrome
def rev(n):#4554
    if n<10:
        return 1
    else:
        rem=n%10
        rev=rev(n)*10+rem
        return rev(n//10)
n=int(input("enter "))
print(rev(n))
    







































