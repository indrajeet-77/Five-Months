# Q1. Create a function that takes three numbers as parameters and returns
# the largest among them. Also if no arguments are passed, make sure the
# parameters take default value as None and return answer as -1

# def largest(a=0,b=0,c=0):
#     if a!= None and b!=None and c!=None
#      if a>b and a>c:
#          return a
#      elif b>a and b>c:
#         return b
#      else:
#         return c
    
#     else:
#      return -1 
# print(largest(1,2,3))
    
# With Annotations
# int | None --- It means it can be an int or None
# def largest_part2(
#     num1: int | None = None, num2: int | None = None, num3: int | None = None
# ) -> int:
#     if num1 != None and num2 != None and num3 != None:
#         if num1 > num2 and num1 > num3:
#             return num1
#         elif num2 > num1 and num2 > num3:
#             return num2
#         else:
#             return num3
#     else:
#         return -1


# print(largest_part2(3, 4, 1))  # Output 4
# print(largest_part2())  # Output -1

    


#   Q2. Implement a function that takes two parameters, base and exponent,
# and returns the result of raising the base to the power of the exponent.

# def expo(base,power)->float:
#     return base**power
# base=2
# power=3
# result=expo(2,3)
# print(f"{base} raise to the power of {power} is {result}")  



# Q3. Ask 3 numbers from user. Make a function which returns the middle of
# those 3 numbers. Then make a function to check if that middle number is
# divisible by both 3 and 4. Make 2 functions for reusability.


# def mid(num1:int,num2:int,num3:int)->int:
#     if(num1<=num2<=num3) or (num3<= num2 <=num1):
#         return num2
#     elif (num2<=num1<=num3) or (num3<=num1<=num2):
#         return num1
#     else:
#         return num3
    
# def isDivisibleBy3and4(number:int)->bool:
#     return number%3==0 and number%4==0

# num1:int=int(input("ENter the first number: "))
# num2:int=int(input("ENter the second number: "))
# num3:int=int(input("ENter the third number: "))

# middle_number=mid(num1,num2,num3)
# print(f"The middle num is {middle_number}")


# if isDivisibleBy3and4(middle_number):
#     print(f"{middle_number} is divisible  by both 3 and 4")
# else:
#     print(f"{middle_number}is not divisible by both 3 and 4")



# Q4. Write a Python program that takes four numbers from the user.
# Implement a function to find the average of the first three numbers. Then,
# create another function to check if the average is greater than or equal to
# the fourth number. Make sure to use these two functions to determine and 

def average(a:int,b:int,c:int,d:int)->float:
    return (a+b+c)/3

def is_greater(avg,d)->str:
    if avg>c:
        return f"{avg} is grater than forth number"
    return f"{avg} is smaller than forth number"

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter forth number: "))

avg=average(a,b,c,d)
print(avg)

yes=is_greater(avg,d)
print(yes)