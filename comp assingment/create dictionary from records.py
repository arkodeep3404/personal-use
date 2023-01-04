#create dictionary from records

l=[]
with open("abc.txt","w") as obj:
    while True:
        a=input("enter data ")
        l.append(a+"\n")
        ch=input("exit to exit, any other key to continue ")
        if ch=="exit":
            break
    obj.writelines(l)

with open("abc.txt","r") as obj:
    l=obj.readlines()
    z=set(l)
    print(z)
