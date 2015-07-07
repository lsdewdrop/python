__author__ = 'user'
name1=raw_input()
sco1=input()
name2=raw_input()
sco2=input()
name3=raw_input()
sco3=input()
print name1+" : "+str(sco1)
print name2+" : "+str(sco2)
print name3+" : "+str(sco3)
sum=sco1+sco2+sco3
ave=(sum/3.0)
print "score : "+str(sum)
print "average : "+str("%0.4f"%ave)
