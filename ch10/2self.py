# self is how a method knows which object it's working on.

class Employee:
    age=22 #class attribute
    city='Jaipur'

    def getInfo(self):
        print(f'age is {self.age}, city is {self.city}')

tani=Employee()
tani.name='Tani' #instance attribute
tani.city='Bangalore'

tani.getInfo()
#gets converted into
# Employee.getInfo(tani)
#which gives TypeError --as its giving 1 arg,, but takes 0
#that's why use self Alwayss