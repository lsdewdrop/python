__author__ = 'user'

reg={}
o=open("register.txt")
while True:
    hhh=o.readline()
    if hhh=="":
        break
    name,number=hhh.split()
    reg[name]=int(number)


def add():
    print "input name  : "
    name=raw_input()

    print "input number : "
    number=input()

    if(name in reg):
        reg[name]=reg[name]+number
    else:
        reg[name]=number
    o=open("register.txt",'w+')
    for i in reg.keys():
        o.write(i)
        o.write(" ")
        o.write(str(reg[i]))
        o.write("\n")


def delete():
    print "input name  : "
    name=raw_input()

    print "input number : "
    number=input()

    if(name in reg):
        if(reg[name]==number):
            del reg[name]
        elif(reg[name]>number):
            reg[name]=reg[name]-number
        else:
            print "so many number"
    else:
        print "There is not name"
    o=open("register.txt",'w+')
    for i in reg.keys():
        o.write(i)
        o.write(" ")
        o.write(str(reg[i]))
        o.write("\n")

def look():
    print reg


while True:
    o=open("register.txt")
    print "choose   1. add  2. delete  3. look  4. ESC"
    n=input()

    if(n==1):
        add()

    elif(n==2):
        delete()

    elif(n==3):
        look()

    elif(n==4):
        o.close()
        break
