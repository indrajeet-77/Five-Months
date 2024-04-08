# Q1. Use a while loop to calculate the sum of the first 10 natural numbers

# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i+=1
# print(sum)



# Q2. Ask a positive number from user. Print all the numbers from positive
# number to 1

# num=int(input("Enter positive number: "))
# i=num
# while i>=1:
#     print(i)
#     i-=1



# Q3. Print this pattern using while loop.
# 1 8 15 22 29 36 43 50 57 64 71 78 85 92 99

# num=1
# i=1
# while i<100:
#     print(i,end=" ")
#     i+=7



# Q4. Print all odd numbers less than 15 using a while loop

# i=1
# num=1
# while i<15:
#         if i%2==1:
#                 print(i,end=" ")
#         i+=1



# Q5. Calculate the factorial of a given number using a while loop.
# Example, n = 5
# 5 x 4 x 3 x 2 x 1

# n=int(input("Enter a number: "))
# fact=1
# while n>0:
#     fact*=n
#     n-=1
# print(f"The factoria; of given number is {fact}")



# Q6. Create a function named div_by_3_and_5 which takes 2 integers as a
# arguments (n1,n2), and print all the numbers divisible by 3 and 5 between
# n1 and n2.

# def div_by_3_and_5(n1:int,n2:int)->int:
#     for i in range(n1,n2+1):
#         if i%3==0 and i%5==0:
#             print(i,end="")
# n1=int(input("Enter n1: "))
# n2=int(input("Enter n2: "))
# div_by_3_and_5(n1,n2)



# Q7. Create a function named calSum() which takes 2 integers n1 and n2 as a
# argument. Calculate the sum of all the numbers from n1 and n2 and
# RETURN THAT SUM. Also make sure that n1 is smaller than n2. If it is not,
# then return “n1 should be smaller”.

# def calSum(n1:int,n2:int)->str|int:
#     if n1<n2:
#         total=0
#         i=1
#         while i<=n2:
#             total+=i
#             i+=1
#         return total
#     return "n1 should be smaller than n2"

# n1=int(input("Enter n1: "))
# n2=int(input("Enter n2: "))
# print(calSum(n1,n2))



# Q8. Create a function named multiplicationTable that takes an integer
# num as an argument. Print the multiplication table of that number up to 10
# numbers

# def multiplicationTable(n:int):
#     a=n
#     n=1
#     i=1
#     while i<=10:
#         print(a,"X",a*n) 
#         i+=1
#         n+=1
# x=int(input("Enter the value : "))
# multiplicationTable(x)



# Q9. Create a function named calSum which takes an 2 integer (n1 and n2)
# as an argument. Calculate the sum of all the numbers divisible by 5
# between n1 and n2 and return that sum. (Make sure that n1 is less than n2)

# def calSum(n1:int,n2:int):
#     i=n1
#     total=0
#     while i<=n2:
#         if i%5==0:
#             total+=i
#         i+=1
#     return total
# n1=int(input("Enter n1: "))
# n2=int(input("Enter n2: "))
# print(calSum(n1,n2))



# Q10. Create a function named printPattern that takes one integer (num) as
# an argument. Print from -num to num. Also keep in mind number passed as
# an argument can be negative or positive

def printPattern(num:int):
    if num>0:
        start: int=-num
        end: int=num
    else:
        start: int=num
        end:int=-num
    while start <=end:
     print(start,end=" ")
     start+=1
   
printPattern(5)
