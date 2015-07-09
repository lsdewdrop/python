__author__ = 'user'
import math
class do:
    nulby=0

    def calcArea(self):
        pass



class TwoDim(do):
    perimeter=0

    def calcPerimeter(self):
        pass

    def printInfo(self):
        print "Area : {0}, Perimeter : {1}".format(self.nulby,self.perimeter)


class ThreeDim(do):
    volume=0

    def calcVolume(self):
        pass

    def printInfo(self):
        print "Area : {0}, Volume : {1}".format(self.nulby,self.volume)


class Rectangle(TwoDim):
    garo=0
    sero=0

    def __init__(self,ga,se):
        self.garo=ga
        self.sero=se

    def calcArea(self):
        self.nulby=self.garo*self.sero

    def calcPerimeter(self):
        self.perimeter=2*self.garo+2*self.sero


class Triangle(TwoDim):
    bun=0

    def __init__(self,bun):
        self.bun=bun

    def calcArea(self):
       self.nulby= math.sqrt(3)*self.bun*self.bun/4

    def calcPerimeter(self):
        self.perimeter=3*self.bun


class Circle(TwoDim):
    r=0

    def __init__(self,r):
        self.r=r

    def calcArea(self):
        self.nulby=self.r*self.r*3.14

    def calcPerimeter(self):
        self.perimeter=2*3.14*self.r


class Cube(ThreeDim):
    a=0

    def __init__(self,a):
        self.a=a

    def calcArea(self):
        self.nulby=6*self.a*self.a

    def calcVolume(self):
        self.volume=self.a*self.a*self.a


class Sphere(ThreeDim):
    r=0

    def __init__(self,r):
        self.r=r

    def calcArea(self):
        self.nulby=4*3.14*self.r

    def calcVolume(self):
        self.volume=4*3.14*self.r*self.r*self.r/4


rec=Rectangle(2,3)
tri=Triangle(4)
cir=Circle(3)
cub=Cube(5)
sph=Sphere(60)

rec.calcArea()
rec.calcPerimeter()
tri.calcArea()
tri.calcPerimeter()
cir.calcArea()
cir.calcPerimeter()
cub.calcArea()
cub.calcVolume()
sph.calcArea()
sph.calcVolume()

rec.printInfo()

tri.printInfo()

cir.printInfo()
cub.printInfo()
sph.printInfo()
