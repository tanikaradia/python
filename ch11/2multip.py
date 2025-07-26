class Employee:
    company='MS'
    name='Tani'

    def show(self):
        print(f'name is {self.name} in the company {self.company}')

class Coder:
    lang='Python'
    def printlang(self):
        print(f'this coder knows {self.lang} language')

class Programmer(Employee,Coder):
    company='Microsoft'
    def showlang(self):
        print(f'name is {self.name} in the company {self.company} who knows {self.lang} language')

s=Programmer()
s.show()
s.printlang()
s.showlang()

b=Employee()
b.show()