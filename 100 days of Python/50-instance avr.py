class employee:
    companyName = "Apple"
    noofemployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_ammount= 3
        employee.noofemployees +=1
    def detail(self):
        print(f"The name of the employee is {self.name} and the raise ammount in {self.noofemployees} sized company {self.companyName} is {self.raise_ammount}")

e1=employee("Harry")     
e1.raise_ammount=5 
e1.companyName="Apple Pakistan"
e1.detail()
e2=employee("Fawad")
e2.raise_ammount=6
e2.detail()
e3=employee("Sameer")   
e3.companyName="Apple International"     
e3.raise_ammount=6
e3.detail()