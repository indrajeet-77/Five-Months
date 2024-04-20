# Q1. When resistors are connected together in series, the same current
# passes through each resistor in the chain and the total resistance, RT, of
# the circuit must be equal to the sum of all the individual resistors added
# together. That is:
# RT = R1 + R2 + R3 ...
# Create a function that takes an array of values resistance that are
# connected in series, and calculates the total resistance of the circuit in
# ohms. The ohm is the standard unit of electrical resistance in the
# International System of Units ( SI ).

#iteration by value
# def calculate_ohm(my_list:list)->int:
#     total=0
#     for i in my_list:
#         total+=i
#     return total
# x=[10,20,20,33,89,100,200,455]
# print(f"The total resistance of circuit is {calculate_ohm(x)} ohms")
        
#iteration by index
# def cal_ohm(my_list:list):
#     total=0
#     n=len(my_list)
#     for i in range(n):
#         total+=my_list[i]
#     return total
# x=[10,20,30,400,500]
# print(cal_ohm(x))








# Q2. Given a number, return a list containing the two halves of the number.
# If the number is odd, make the rightmost number higher.

#given  by sir
# def number_split(n):
#     evenResult = n // 2
#     if n % 2 == 0:
#         oddResult = n // 2
#     else:
#         oddResult = n // 2 + 1
#     my_list = list()
#     my_list.insert(0, evenResult)
#     my_list.insert(1, oddResult)
#     print(my_list)

# number_split(11)

#my code
# def split(n:int)->list:
#     even=n//2
#     if  n%2==0:
#         odd=n//2
#     else:
#         odd=n//2+1
#     l1=[]
#     l1.insert(0,even)
#     l1.insert(1,odd)
#     print(l1)
# split(11)


# Q3. Lists can be mixed with various types. Your task for this challenge is to
# sum all the number elements in the given list. Create a function that takes
# a list and returns the sum of all numbers in the list.


# def sum_of_nums(my_list:list)->int:
#     sum=0
#     n=len(my_list)
#     for i in range(n):
#         if type(my_list[i])==int:
#              sum+=my_list[i]
#     return sum
# x=[1,2,"13","4"]

# print(sum_of_nums(x))