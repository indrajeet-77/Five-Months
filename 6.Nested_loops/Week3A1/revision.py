# Q1. Write a function that converts hours into seconds.

# def hTOs(hours:float):
#     return hours*60*60
# print(hTOs(2))




# Q2. Create a function that takes the age in years and returns the age in
# days.

# def convo(years:int)->int:
#     day=365
#     return day*years
# print(convo(65))




# Q3. Create a function that takes a base number and an exponent number
# and returns the calculation.

# def calculate_exponent(base:int,expo:int)->int:
#     return base**expo
# b=int(input("Enter base num: "))
# ex=int(input("Enter expo: "))
# print(calculate_exponent(b,ex))



# 4. Create a function that takes the number of wins, draws and losses and
# calculates the number of points a football team has obtained so far.

# def game(wins,draws,losses):
#     total=0
#     win_points=wins*3
#     total=win_points+draws
#     return total



# Q5. A farmer is asking you to tell him how many legs can be counted among
# all his animals. The farmer breeds three species:
# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs
# The farmer has counted his animals and he gives you a subtotal for each
# species. You have to implement a function that returns the total number of
# legs of all the animals.
# ex:
# animals(2, 3, 5) ➞ 36
# animals(1, 2, 3) ➞ 22
# animals(5, 2, 8) ➞ 50
# Don't forget to return the result.
# The order of animals passed is animals(chickens, cows, pigs).

# def animal(chickens:int,cows:int,pigs:int)->int:
#     total = chickens*2 + cows*4 + pigs*4
#     return total
# chicken=int(input("Enter no. of chickens: "))
# cows=int(input("Enter no. of cows: "))
# pigs=int(input("Enter no. of pigs: "))
# x=animal(chicken,cows,pigs)
# print(x)





# Q6. Write a function that takes two integers (hours, minutes), converts
# them to seconds, and adds them

# def convert(hours,mins):
#     result=hours*60*60 + mins*60
#     return result
# print(convert(1,3))




# Q7. Write a function that returns the string "something" joined with a
# space " " and the given argument a.

# def give_me_something(a:str)->str:
#     result="something "+a
#     return result
# print(give_me_something("is better than nothing."))




# Q8. Create a function that takes two arguments: the original price and the
# discount percentage as integers and returns the final price after the
# discount.

# def dis(price:int,discount:int)->str:
#     final_price= price/100*discount
#     return f"{final_price:.2f} is final price"

# x=dis(1500,50)
# print(x)




# Curzon number is defined to be a positive integer n for which 2n + 1 is evenly divisible by 2 × n + 1.

# def iscurzon(num:int)->bool:
#     exp=num
#     base=2
#     a=(base**exp)+1
#     b=(base*exp)+1
#     if  a%b ==0:
#         print(f"{a} is a multiple of {b}")
#         return True
#     print(f"{a} is not a multiple of {b}")
#     return False
# x=iscurzon(10)
# print(x)




# Q10. Create a function that takes the number of daily average recovered
# cases recovers, daily average new_cases, current active_cases, and returns
# the number of days it will take to reach zero cases.

# def end_corona(recovers,new_cases,active_cases):
#     count=0
#     while active_cases>0:
#         active_cases-=recovers
#         active_cases+=new_cases
#         count+=1
#     return count

# print(end_corona(4000,2000,77000))




# Q11. Create a function that takes damage and speed (attacks per second)
# and returns the amount of damage after a given time.
# ex:
# damage(40, 5, "second") ➞ 200
# damage(100, 1, "minute") ➞ 6000
# damage(2, 100, "hour") ➞ 720000
# Return "invalid" if damage or speed is negative

# def damage(attack,unit,time):
#     if time=="second":
#         return attack*unit
#     elif time=="minute":
#         return attack*unit*60
#     elif time=="hour":
#         return attack*unit*3600
#     return "invalid"
    
# print(damage(2,100,"hour"))




# Q12. Create a function that takes three arguments a, b, c and returns the
# sum of the numbers that are evenly divided by c from the range a, b
# inclusive.
# Return 0 if there is no number between a and b that can be evenly divided
# by c
# evenly_divisible(1, 10, 20) ➞ 0
# # No number between 1 and 10 can be evenly divided by 20.
# evenly_divisible(1, 10, 2) ➞ 30
# # 2 + 4 + 6 + 8 + 10 = 30

# def cal(a:int,b:int,c:int)->int:
#     sum=0
#     for i in range(a,b+1):
#         if i%c==0:
#             sum+=i
#     return sum
    
# print(cal(1,10,3))




# Q13. Create a function that returns the thickness (in meters) of a piece of
# paper after folding it n number of times. The paper starts off with a
# thickness of 0.5mm.
# num_layers(1) ➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)

# def thickness(mm:float)->str:
#     meters=mm/1000
#     return f"{meters:.10f}m" 
# print(thickness(21))





# Q14. Create a function that takes two parameters and, if both parameters
# are strings, add them as if they were integers or if the two parameters are
# integers, concatenate them.
# ex:
# stupid_addition(1, 2) ➞ "12"
# stupid_addition("1", "2") ➞ 3
# stupid_addition("1", 2) ➞ None

# If the two parameters are different data types, return None.
# All parameters will either be strings or integers.


# def stupid_addition(a:str|int,b:str|int):
#     if type(a)==str and b==str:
#         c=int(a)
#         d=int(b)
    
#         return c+d
#     elif a==int and b==int:
#         e=str(a)
#         f=str(b)
#         return e+f
#     else:
#      return None

# print(stupid_addition(1,2))
    