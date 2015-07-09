__author__ = 'user'
#_*_ coding:utf-8 _*_
#ㅇㅇㅇㅇㅇ

import math

class do:
    nulby=0
    dul=0

    def calcArea(self):
        pass
    def calcPerimeter(self):
        pass
    def printInfo(self):
        print "Area : {0}, Perimeter : {1}".format(self.nulby,self.dul)

class Rectangle(do):
    garo=0
    sero=0

    def __init__(self,ga,se):
        self.garo=ga
        self.sero=se

    def calcArea(self):
        self.nulby=self.garo*self.sero

    def calcPerimeter(self):
        self.dul=2*self.garo+2*self.sero


class Triangle(do):
    bun=0

    def __init__(self,bun):
        self.bun=bun

    def calcArea(self):
       self.nulby= math.sqrt(3)*self.bun*self.bun/4

    def calcPerimeter(self):
        self.dul=3*self.bun


class Circle(do):
    r=0

    def __init__(self,r):
        self.r=r

    def calcArea(self):
        self.nulby=self.r*self.r*3.14

    def calcPerimeter(self):
        self.dul=2*3.14*self.r


rec=Rectangle(2,3)
tri=Triangle(4)
cir=Circle(3)

rec.calcArea()
rec.calcPerimeter()
tri.calcArea()
tri.calcPerimeter()
cir.calcArea()
cir.calcPerimeter()

rec.printInfo()

tri.printInfo()

cir.printInfo()
