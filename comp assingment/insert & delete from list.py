#insert & delete from list

k=[]
l=[int(i) for i in input("enter list elements ").split()]
print(l)
a=int(input("enter number to delete "))
for i in l:
    if i==a:
        continue
    else:
        k.append(i)
print(k)

