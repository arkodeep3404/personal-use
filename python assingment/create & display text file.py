#create & display text file

with open("abc.txt","w") as obj:
    a=input("enter data ")
    obj.write(a)

with open("abc.txt","r") as obj:
    for i in obj:
        print("data from text file is",i)
