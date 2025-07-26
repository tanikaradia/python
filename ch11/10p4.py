# REAL AND IMAGINARY NUMBERS add
class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,num):
        return Complex(self.r+num.r, self.i+num.i)
    
    def __str__(self):
        return f'{self.r} + {self.i}i'
    
a=Complex(1,4)
b=Complex(2,4)
print(a+b)