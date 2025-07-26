class Number:
    def __init__(self,n):
        self.n=n
    
    def __add__(self,num):
        # return self.n + num.n
        return Number(self.n+num.n)  #for c to be obj

    def __str__(self):
        return f'sum is {self.n}'
    
a=Number(5)
b=Number(2)

# print(a+b) #+ ->looks for the __add__ method
#a.__add__(b)
#obj1.__add__(obj2)

#or
c=a+b #c = Number(7) becomes obj
print(c)