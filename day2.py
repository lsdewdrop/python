__author__ = 'user'
import random

a=input()

for i in range(a,a+1):
    for j in range(1,10):
        print str(i)+"*"+str(j)+"="+str(i*j)

num=[0,0,0]

check=[]
for i in range(0,10):
    check.append(0)

num[0]=random.randrange(0,10)
check[num[0]-1]=1

num[1]=random.randrange(0,10)
while check[num[1]-1] == 1:
    num[1]=random.randrange(0,10)
check[num[1]-1]=1

num[2]=random.randrange(0,10)
while check[num[2]-1] == 1:
    num[2]=random.randrange(0,10)


while 2:
    strike=0
    ball=0

    inp=[0,0,0]
    inp[0]=input()
    inp[1]=input()
    inp[2]=input()


    for i in range(0,3):
        for j in range(0,3):
            if num[i]==inp[j]:
                if i==j:
                    strike+=1
                else:
                    ball+=1

    print "strike : " + str(strike) + "   ball : " + str(ball)
    if strike==3:
        print "clear"
        break




