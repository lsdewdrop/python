__author__ = 'user'

class Fraction():
    numerator=0
    denominator=0

    def __init__(self, num, den):
        self.numerator=num
        self.denominator=den


    def __add__(self, other):
        if(self.denominator>other.denominator):
            small=other.denominator
            big=self.denominator
        else:
            big=other.denominator
            small=self.denominator

        if(small==0):
            pass
        else:
            while(small!=0):
                temp=big
                tempp=small
                big=small
                small=temp/tempp
            GCD=big
            LCD=self.denominator*other.denominator/GCD

        print str(self.numerator*(LCD/self.denominator)+other.numerator*(LCD/self.denominator))+"/"+str(LCD)


    def __sub__(self, other):
        if(self.denominator>other.denominator):
            small=other.denominator
            big=self.denominator
        else:
            big=other.denominator
            small=self.denominator

        if(small==0):
            pass
        else:
            while(small!=0):
                temp=big
                tempp=small
                big=small
                small=temp/tempp
            GCD=big
            LCD=self.denominator*other.denominator/GCD

        print str(self.numerator*(LCD/self.denominator)-other.numerator*(LCD/self.denominator))+"/"+str(LCD)


    def __mul__(self, other):
        print str(self.numerator*other.numerator)+"/"+str(self.denominator*self.denominator)

    def __div__(self, other):
        mo=other.numerator
        ja=other.denominator

        print str(self.numerator*ja)+"/"+str(self.denominator*mo)


fac1=Fraction(2,3)
fac2=Fraction(5,3)

fac1+fac2
fac1-fac2
fac1*fac2
fac1/fac2
