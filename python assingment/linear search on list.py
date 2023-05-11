#linear search on list

k=0
l=[int(i) for i in input("enter list elements ").split()]
print(l)
a=int(input("enter number to search for "))
for i in l:
    k=k+1
    if i==a:
        print("the number is present at index = ",k-1)
