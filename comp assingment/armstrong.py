#armstrong_number

a=int(input("enter number "))
x=len(str(a))
f=0
for i in str(a):
    f=(int(i)**x)+f
if f==a:
    print("Yes")
else:
    print("No")

