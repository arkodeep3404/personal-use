#max & min element

l=[int(i) for i in input("enter list elements ").split()]
print(l)
k=l[0]
m=l[0]
for i in range(len(l)):
    if l[i]>k:
        k=l[i]
print("max value =",k)

for j in range(len(l)):
    if l[j]<m:
        m=l[j]
print("min value =",m)

