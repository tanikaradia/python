#2D and 3D vectors

class TwoDv:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print (f'2d vector => {self.i}i+{self.j}j')
    
class ThreeDv:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def show(self):
        print (f'3d vector => {self.i}i+{self.j}j+{self.k}k')
    
a=TwoDv(2,5) #passing val to class
b=ThreeDv(3,4,5)

a.show()
b.show()