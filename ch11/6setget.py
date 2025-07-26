class Employee:

    @property       ##GETTER
    def name(self):        #fir isme
        return f'{self.fname} {self.lname}'
    
    @name.setter    ##SETTER
    def name(self,val):    # pehle isme
        self.fname = val.split(" ")[0] #at first index,, split by space
        self.lname = val.split(" ")[1] #at sec index

        #in case>2 words
        # parts = val.split(" ", 1)
        # self.fname = parts[0]
        # self.lname = parts[1] if len(parts) > 1 else '' #iska matlab agar 2 se jyada words h to doosre me save ho jayega


e=Employee()
e.name='Tani karadia'
print(e.fname,e.lname)