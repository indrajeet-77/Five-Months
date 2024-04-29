# class Student:
#     def __init__(self):
#         self.id=int(input("Enter ID: "))
#         self.name=input("Enter name: ")
#         self.gender=input("Enter gender: ")
    
#     def display(self):
#         self.id=print(f"{self.id}")
#         self.name=print(f"{self.name}")
#         self.gender=print(f"{self.gender}")

# s1=Student()
# s1.display()

#without using __init__ method
# class Employee:
#     # attributes
#     Company="Infosys Technologies India Private Limited"
#     print(Company)
    
#     #methods
#     def set_data(self):
#             self.Name=input("Enter name:")
#             self.Salary=int(input("Enter Salary: "))
#             self.Shift=input("Enter Day / Night: ")
#     def display(self):
#         print(f"Name: {self.Name}")
#         print(f"Salary: {self.Salary}")
#         print(f"Shift: {self.Shift}")
        
# e1=Employee()
# e1.set_data()
# e1.display()



# #Using __init__ method

# class Employee1:
#     def __init__(self):
#         Company="Infosys Technologies India Private Limited"
#         print(Company)
#         self.Name=input("Enter name:")
#         self.Salary=int(input("Enter Salary: "))
#         self.Shift=input("Enter Day / Night: ")
    
#     def display1(self):
#          print(f"Name: {self.Name}")
#          print(f"Salary: {self.Salary}")
#          print(f"Shift: {self.Shift}")
         
# e2=Employee1()
# e2.display1()


#without using self(very basic level)

# class Student:
#     #attributes
#     Name="Yet to be "
#     Salary=0
#     Shift="Yet to be"

# #st1 object created  here  
# st1=Student()
# st2=Student()

# #name,salary and shift values are assigned here
# st1.Name="Indrajeet"
# st1.Salary=40000
# st1.Shift="Night"

# #printing the s1 object and its attributes
# print(st1.Name)
# print(st1.Salary)
# print(st1.Shift)

# print("----------")
# print(st2.Name)
# print(st2.Salary)
# print(st2.Shift)
        
        





























"""    








"""
# class Student1:
#     # Attributes/Class Variables
#     def __init__(self):
#         self.id = int(input("Enter ID = "))
#         self.name = input("Enter name = ")
#         self.gender = input("Enter gender = ")
#         self.age = int(input("Enter age = "))
#         # self.school_name = "XYZ School"
#     def display(self):
#         print(f"ID = {self.id}")
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         print(f"Gender = {self.gender}")
#     def displayName(self):
#         print(f"Your name is {self.name}")

# s1 = Student1()
# print("----------")
# s1.display()