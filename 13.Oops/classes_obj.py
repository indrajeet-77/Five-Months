# # in python every thing is object

class Student:
    # Attributes/Class Variables
    id = 0
    name = ""
    gender = ""
    age = 0

s1 = Student()
s2 = Student()
s1.id = 65
s1.name = "Anirudh Khurana"
s1.age = 56
s1.gender = "Male"
print(s1.id)
print(s1.name)
print(s1.gender)
print(s1.age)
print("--------")
print(s2.id)
print(s2.name)
print(s2.gender)
print(s2.age)



#sir
# in python every thing is object

# class Student:
#     # Attributes/Class Variables
#     id = 0
#     name = ""
#     gender = ""
#     age = 0
#     # Methods
#     def display(self):
#         print(f"ID = {self.id}")
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         print(f"Gender = {self.gender}")
#     def displayName(self):
#         print(f"Your name is {self.name}")

# s1 = Student()
# s2 = Student()
# s1.id = 65
# s1.name = "Anirudh Khurana"
# s1.age = 56
# s1.gender = "Male"
# s1.display()
# print("--------")
# s2.display()





# in python every thing is object

# class Student:
#     # Attributes/Class Variables
#     id = 0
#     name = ""
#     gender = ""
#     age = 0
#     # Methods
#     def setDetails(self):
#         self.id = int(input("Enter ID = "))
#         self.name = input("Enter name = ")
#         self.gender = input("Enter gender = ")
#         self.age = int(input("Enter age = "))
#     def display(self):
#         print(f"ID = {self.id}")
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         print(f"Gender = {self.gender}")
#     def displayName(self):
#         print(f"Your name is {self.name}")

# s1 = Student()
# s1.setDetails()
# s1.display()



# #sir3
# # in python every thing is object

# class Student:
#     # Attributes/Class Variables
#     # Methods
#     def setDetails(self):
#         self.id = int(input("Enter ID = "))
#         self.name = input("Enter name = ")
#         self.gender = input("Enter gender = ")
#         self.age = int(input("Enter age = "))
#     def display(self):
#         print(f"ID = {self.id}")
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         print(f"Gender = {self.gender}")
#     def displayName(self):
#         print(f"Your name is {self.name}")

# s1 = Student()
# s2 = Student()
# s1.setDetails()
# s1.display()
# s2.display()



#sir 4
# # in python every thing is object

# class Student:
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

# s1 = Student()
# print("----------")
# s1.display()


#sir 5
# in python every thing is object

# class Student:
#     # Attributes/Class Variables
#     def setDetails(self):
#         self.id = int(input("Enter ID = "))
#         self.name = input("Enter name = ")
#         self.gender = input("Enter gender = ")
#         self.age = int(input("Enter age = "))
#     def setDetails2(self, id, name, gender="Male", age=0) -> None:
#         self.id = id
#         self.name = name
#         self.gender = gender
#         self.age = age
#     def displayName(self):
#         print(f"Your name is {self.name}")
#     def display(self):
#         print(f"ID = {self.id}")
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         print(f"Gender = {self.gender}")

# s1 = Student()
# s1.setDetails2(4, "Anirudh")
# s1.display()



#sir6
# in python every thing is object

# class Student:
#     # Attributes/Class Variables
#     def __init__(self, id: int, name: str, gender="Female", age=0) -> None:
#         self.id = id
#         self.name = name
#         self.gender = gender
#         self.age = age
#     def setDetails(self):
#         self.id = int(input("Enter ID = "))
#         self.name = input("Enter name = ")
#         self.gender = input("Enter gender = ")
#         self.age = int(input("Enter age = "))
#     def displayName(self):
#         print(f"Your name is {self.name}")
#     def display(self):
#         print(f"ID = {self.id}")
#         print(f"Name = {self.name}")
#         print(f"Age = {self.age}")
#         print(f"Gender = {self.gender}")

# s1 = Student(33, "Anirydh", "Male", 99)
# s1.display()