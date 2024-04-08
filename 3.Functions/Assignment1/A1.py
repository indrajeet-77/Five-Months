#q1 Write a Python function to find the Maximum and minimum of three
# numbers. Use 3 parameters. Make 2 different functions named as maxi and
# mini.

# def maxi(a,b,c):
#     if a>b and a>c:
#         print(f"{ a} is maximum")
#     elif b>a and b>c:
#         print(f"{b} is maximum")
#     elif c>a and c>b:
#         print(f"{c} is maximum")
# maxi(1,2,3)

# def mini(a,b,c):
#     if a<b and a<c:
#         print(f"{ a} is minimum")
#     elif b<a and b<c:
#         print(f"{b} is minimum")
#     elif c<a and c<b:
#         print(f"{c} is minimum")

# mini(11,22,33)



#q2
# Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but
# using function. Try calling function with different years as a parameter and
# check the output

# def check_year(year:int)->str:
#      if(year%4==0 and year %100!=0 ) or (year%400==0):
#       return  f"{year} it is a leap year"
#      return f"{year} is not a leap year"
# print(check_year(2003))



#q3 Attempt the same bill calculator question (Week 1 - Assignment 2-Q5)
#but using function. Try calling function with different bill amount as a
#parameter and check the output.

# def create_bill(final_amount :float)->str:
#     discount=0
#     discounted_amount=final_amount
#     if final_amount>50000:
#         discount=30
#     elif final_amount>=40000 and final_amount<=49999:
#         discount=25
#     elif final_amount>=30000 and final_amount<=39999:
#         discount=20
#     elif final_amount>=10000 and final_amount<=29999:
#         discount=10
#     elif final_amount<=1 and final_amount<=9999:
#         print("No dicount")
#     if discount>0:
#      discounted_amount=final_amount-(final_amount*discount/100)
#     return f"You got {discount} %  and your final bill is RS. {discounted_amount:.2f}"

# x=float(input("Enter final amount: "))
# print(create_bill(x))



#Q4. Attempt Week 1 - Assignment 2 (Q6) and Week 1 - Assignment 2 (Q7)
#using function.

# def smallest(a:int,b:int,c:int,d:int)->int:
#     if a<b and a<c and a<d:
#         return a
#     elif b<c and b<a and b<d:
#         return b
#     elif c<a and c<b and c<d:
#         return c
#     return d
# x=smallest(22,33,44,1)
# print(x)



#Q5. Write a function named personal_greet that takes a name as a
# parameter and prints a greeting message with that name. For example,
# personal_greet("Alice") should print "Hello, Alice!".

# def personal_greet(name:str)->str:
#     return f"Hello, {name}!"
# name=input("enter name: ")
# print(personal_greet(name))



# Q6. Write a function named is_even that takes a number as a parameter
# and prints "Even" if the number is even and "Odd" if the number is odd.

# def is_even(num:int)->str:
#     if num%2==0:
#         return f"{num} is Even"
#     return f"{num} is Odd"
# num=int(input("Enter a number: "))
# print(is_even(num))



# Q7. Write a function named celsius_to_fahrenheit that converts Celsius to
# Fahrenheit and prints the result. (Formula: (Celsius * 9/5) + 32 = Fahrenheit)

# def celsius_to_fahrenheit(cel:float)->str:
#     f= (cel * 9/5)+32
#     return f" {cel} degree celcius converted into fahrenheit is {f}"
# cel=float(input("Enter temprature in celcius: "))
# print(celsius_to_fahrenheit(cel))



#Q8. Create a function named simple_calculator that takes three
# parameters: two numbers and an operation (addition or subtraction
# represented by '+' or '-'), and prints the result of the operation.

# def simple_calculator(num1:int,num2:int,operation:str)->str:
#     if operation== "+":
#      return f"Addition is {num1+num2}"
#     return f"Substraction is {num1-num2}"
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2: "))
# operation=input("Enter addition or substraction symbol: ")
# print(simple_calculator(num1,num2,operation))
    


# def check_number(num:int)->str:
#     if num==0:
#         return "Zero"
#     elif num<0:
#         return "Negative"
#     return "Positive"
# num=int(input("Enter number: "))
# print(check_number(num))



# Q10. Write a function named is_odd_even that determines if a number is
# odd or even without using the modulo operator (%). Hint: Use division or
# subtraction.

# def is_odd(num:int):
#     if (num //2)*2==num:
#         print("Even")
#     else:
#         print("Odd")

# #test cases
# is_odd(2)
# is_odd(3)



# Q11. Write a function named calculate_interest that takes the principal,
# rate of interest, and time as parameters and prints the simple interest
# calculated.

# def calculate_interest(p,r,t):
#     simple_interest=(p*r*t)/100
#     return f"Simple interest is {simple_interest}"
# print(calculate_interest(100,4,2))