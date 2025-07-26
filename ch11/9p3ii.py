#employee salary increment
class Employee:

    def __init__(self):
        self.salary=0
        self.increby=0

    @property
    def finalsalary(self):
        return f'Final salary after increment is {self.salary + (self.salary * self.increby / 100)}'

    @finalsalary.setter
    def finalsalary(self,data):
        salary,increby=data ##this is called making a tuple, as setter only takes one input

        self.salary=salary
        self.increby=increby

a=Employee()
salary=int(input('Enter total salary: '))
increby=int(input('and increment by percentage: '))
a.finalsalary=(salary,increby)  # Set using tuple
print(a.finalsalary)