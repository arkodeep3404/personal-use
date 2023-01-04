#krishnamurty_number

def fact(k):
    x=1
    for i in range(1,k+1):
        x=x*i
    return(x)  

a=int(input("enter number "))
f=0
for j in str(a):
    f=fact(int(j))+f
if f==a:
    print("yes")
else:
    print("no")
    
    
     