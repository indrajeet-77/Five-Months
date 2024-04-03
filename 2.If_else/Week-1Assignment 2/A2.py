#q1
# num1=int(input("Enter the fist number: "))
# num2 = int(input("Enter the second number: "))
# if num1%num2==0:
#     print("Divisible")
# else:
#     print("Not divisible")

#q2
# class_held=int(input("Enter no. of classes held: "))
# class_attended=int(input("Enter no. of classes attended: "))
# attendance = class_attended/class_held*100
# if attendance<75:
#     print(f"You are not allowed to sit in exam ,cause your attendace is below 75% and your percentange of class attended if {attendance}")
# else:
#     print(f"You are allowed to sit for exams as your attendace is {attendance}")

#q3
# num=int(input("Enter number: "))
# if num%2==0 and num%3==0 and num%8!=0:
#     print(f"{num} is divisible by 2 and 3 but not 8.")

#q4
# user_input=int(input("Enter the score: "))
# if user_input<=100 and user_input>=90:
#     grade="A"
# elif user_input<=89 and user_input>=80:
#     grade="B"
# elif user_input<=79 and user_input>=70:
#     grade="C"
# elif user_input<=69 and user_input>=60:
#     grade="D"
# else:
#     grade="F"
# print(f"{grade= }")


#q5
# final_amount:float =float(input("Enter final amount: "))
# discount=0
# discounted_amount:float =final_amount
# if final_amount>=50000:
#     discount=30
# elif 40000<=final_amount and final_amount <=49999:
#     dicount=25
# elif 30000<=final_amount and final_amount<=39999:
#     discount=20
# elif 10000<=final_amount and final_amount<=29999:
#     discount=10
# #calculate discount
# if discount>0:
#         discounted_amount=final_amount - (final_amount * discount / 100)
# print(f"You got {discount}%discount")
# print(f"Your final bill is RS {discounted_amount:.2f}")



#q6
# a=int(input("Enter number: "))
# b=int(input("Enter number: "))
# c=int(input("Enter number: "))
# d=int(input("Enter number: "))
# if a<b and a<c and a<d:
#     print(f"{a} is smallest")
# if b<a and b<c and b<d:
#     print(f"{b} is smallest") 
# if c<a and c<b and c<d:
#     print(f"{c} is smallest")
# else:
#     print(f"{d} is smallest")



#q7
# salary=float(input("Enter the salary: "))
# if salary <10000:
#     increment_percentage= 5
# elif 10000<=salary <20000:
#     increment_percentage=10
# elif 20000<=salary<50000:
#     increment_percentage=15
# else:
#     increment_percentage=20

# increment=(salary*increment_percentage)/100
# updated_salary= salary+increment

# print(f"The original salary was : RS{salary:.2f}")
# print(f"The increment percentage is:{increment_percentage}%")
# print(f"The updated salary is :Rs{updated_salary:.2f}")
   
#q8

# year=int(input("Enter a year: "))
# if(year%4==0 and year %100!=0 ) or (year%400==0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year}is not a leap year") 
