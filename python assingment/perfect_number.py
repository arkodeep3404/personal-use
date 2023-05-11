#perfect_number

def factor(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    return l
n=int(input("enter number "))
#print(factors(n))
k=0
for i in factor(n):
    k=k+i
if k==n:
    print("yes")
else:
    print("no")

