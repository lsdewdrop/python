__author__ = 'user'

def all_view(mok):
    o=open("subject.txt")
    while True:
        aa=o.readline()
        if aa=="":
            break
        na, co=aa.split()
        mok[na]=co

    print mok.items()
