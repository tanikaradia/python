class Employee:
    age=22
    city='Jaipur'

    def __init__(self,age):
        self.age=age
        print('object is created')

    def getInfo(self):
        print(f'age is {self.age}, city is {self.city}')

    @staticmethod
    def greet():
        print('hi')

tani=Employee(25)
print(tani.age,tani.city)


# 🧠 Without __init__?
# You'd have to set attributes manually:
# class Student:
#     pass
# s1 = Student()
# s1.name = "Tani"
# s1.age = 21

# class Emp:
#     age=50
#     city='Kota'

#     def __init__(self,age,city):
#         self.age=age
#         self.city=city
#         print('2nd object is created')

# jiggu=Emp(25) #wrongg as 2 argument must passed
# print(jiggu.age,jiggu.city)

##def greet(name):  parameter   empty box
##greet("Tani")     argument    values give to it
