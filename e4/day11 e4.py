#removing of spaces between words
'''s=input("enter:")
o=s.strip()
print(o)
s1=""
#c=0
for i in s:
    if i!=" ":
        s1=s1+i
    else:
        #c=c+1
        c=s.count(" ")
print(s1)
print("count:",c)'''

#reverse the sentence of words 
'''s=input("enter: ")
print(s)
l=s.split()
l1=l[::-1]
for i in l1:
    print(i,end=" ")'''

#capital of every word of starting letter
'''str=input("enter: ")
#print(str.title())
l=str.split()
for i in l:
    #print(i.capitalize(),end=" ")
    i[0]=chr(ord(i[0])-32)'''
#anagram
a=input("enter")
b=input("enter another:")
c=0
if(len(a)==len(b)):
    print("not anagram")
    

else:
   for i in a:
        for j in b:
            if(i==j):
                c=c+1
    if(c!=0):
    print("not anagram")

















    


