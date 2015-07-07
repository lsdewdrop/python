__author__ = 'user'
def sinchung():
    print "input name."
    name=raw_input()
    if name !="kjh" and name !="gsw" and name !="ldk" and name !="smh":
        print "There is not this user."
        return
    print "input code"
    code=raw_input()
    if code !="0001" and code !="0002" and code !="0003" and code !="0004" and code !="0005" and code !="0006":
        print "there is not this code."
        return

    o=open("user.txt")
    user=[]
    while True:
        bb=o.readline()
        if bb=="":
            break
        user.append(list(bb.split()))
    o=open("user.txt", "w+")

    for i in range(0,4):

        if user[i][0]==name:
            user[i].append(code)
        for k in range(0,len(user[i])):
            o.write(user[i][k])
            o.write(" ")
        o.write("\n")
    print "sinchung sucess"
