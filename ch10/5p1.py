class Programmer:
    company='Deloitee'

    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

madhav=Programmer('Madhav',90000,302015)
print(madhav.name,madhav.company,madhav.pin,madhav.salary)

gopal=Programmer('Gopal',100000,302006)
print(gopal.name,gopal.company,gopal.pin,gopal.salary)