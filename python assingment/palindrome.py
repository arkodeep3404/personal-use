#palindrome

#reverse of number

a=int(input("enter number "))
l=[]
b=[]
c=[]
for i in str(a):
    l.append(i)
    b.append(i)
for k in range(len(l)):
    z=l.pop()
    c.append(z)
if c==b:
    print("yes")
else:
    print("no")

