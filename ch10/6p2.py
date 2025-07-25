class Calc:
    def __init__(self,n):
        self.n=n

    def cube(self):
        print(f'cube is: {self.n*self.n*self.n}')

    def sqroot(self):
        print(f'square root is: {self.n**1/2}')

n=int(input('enter a no: '))
a=Calc(n)
a.cube()
a.sqroot()