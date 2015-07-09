__author__ = 'user'

print "Please input thr file name."
filename=raw_input()

try:
    o=open(filename)
except IOError:
    print "there is error. Please input the line."
    o=open(filename, "w")
    inp=raw_input()
    o.write(inp)
else:
    print "file open sucess. Please input the line."
    o=open(filename, "a+")
    print o.read()
    o.seek(0)
    inp=raw_input()
    o.write(inp)
