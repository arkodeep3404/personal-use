#reverse of number

a=int(input("enter number "))
l=[]
c=[]
s=""
for i in str(a):
    l.append(i)
for k in range(len(l)):
    z=l.pop()
    c.append(z)
for z in c:
    s=s+str(z)
print("the reverse of number is", int(s))

