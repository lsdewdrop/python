__author__ = 'user'
def listveiw():
    print "input name."
    name=raw_input()
    if name !="kjh" and name !="gsw" and name !="ldk" and name !="smh":
        print "There is not this user."
        return

    o=open("user.txt")
    user=[]
    while True:
        bb=o.readline()
        if bb=="":
            break
        user.append(list(bb.split()))
    p=open("subject.txt")
    moklok={}
    while True:
        aa=p.readline()
        if aa=="":
            break
        na, co=aa.split()
        moklok[co]=na

    for i in range(0,4):
            if user[i][0]==name:
                for k in range(1,len(user[i])):
                    print moklok[user[i][k]]
