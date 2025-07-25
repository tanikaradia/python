class Employee:
    age=22 #class attribute
    city='Jaipur'

tani=Employee() #obj
tani.name='Tani' #instance attribute
print(tani.name,tani.age)


anshu=Employee()
anshu.age=21 # ins>class atrri preference
#and also this doesnt change the class attri

print(anshu.age,anshu.city)
