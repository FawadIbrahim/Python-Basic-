class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(f"The name of the Employee: {self.id}, is: {self.name}")
class programmer(person):  
    def newfunc(self):
        print("This is a new function in the programmer class")         

e=person("Fawad","2021")
e.display()
e2=person("Sameer","2022")
e2.display()
e3=programmer("Kiran","2020")
e3.display()
e3.newfunc()