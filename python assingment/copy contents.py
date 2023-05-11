#copy contents

with open("abc.txt","w") as obj:
    a=input("enter data ")
    obj.write(a)

with open("abc.txt","r") as obj:
    with open("abc2.txt","w") as obj2:
        for i in obj:
            obj2.write(i)
            print("original data from text file is",i)

with open("abc2.txt","r") as obj:
    for i in obj:
        print("copied data from text file is",i)
