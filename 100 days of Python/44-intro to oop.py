# def hello():
#   print("hello")

# hello()
# sales1 = 6000
# profit1 = 2000
# ad1 = 1000
# # rajeev.sales

# sales2 = 6000
# profit2 = 2000
# ad2 = 1000 
# # vikrant.sales

# sales3 = 6000
# profit3 = 2000
# ad3 = 1000
 
# RailwayForm   ---> Class [blueprint]
# harry --> harry ki info wala form --> Object [entity]
# tom --> tom ki info wala form --> Object [entity]
# shubham -- shubham ki info wala form --> Object [entity]
# # shubham.changeName("Shubhi")

# class employee():
#   def data(self):  
#     self.id=int(input("Enter your id:"))
#     self.name=input("Enter your Name:")
#     self.salary=float(input("Enter your Salary:"))
#   def display(self):
#     print("Employee id",self.id)
#     print("Employee Name",self.name)
#     print("Employee Salary",self.salary)
# a=employee()
# a.data()
# a.display()


# class avera:
#     def __init__(self,name,rollno,numbers):
#         self.name=name
#         self.rollno=rollno
#         self.numbers=numbers
#     def aver(self):
#         return sum(self.numbers)/len(self.numbers)
# first_student=avera('Fawad',2021,[70,80,90,100])
# print(first_student)
# print(first_student.aver())



class data:
    Name="Fawad"
    occupation="Python Developer"
    age=20
    def person1(self):
        print(f"My name is {self.Name}. I am a {self.occupation} and I am {self.age} years old")
a=data()        
a.person1()