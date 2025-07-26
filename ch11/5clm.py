class Employee:
    a=1

    @classmethod  #this just always shows class attri (X obj)
    def show(cls):
        print(f'the class attri of a is {cls.a}')

e=Employee()
e.a=44
e.show()