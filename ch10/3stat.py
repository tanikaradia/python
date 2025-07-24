class Employee:
    age=22
    city='Jaipur'

    def getInfo(self):
        print(f'age is {self.age}, city is {self.city}')

    @staticmethod
    def greet():
        print('hi')

tani=Employee()
tani.name='Tani'
tani.city='Bangalore'

tani.getInfo()

Employee.greet()
tani.greet()