# Q1. Create a function named divs, which will take two parameters n1 and
# n2. Return the count of how many numbers from 1 to n1 are divisible by n2.

# def divs(n1:int,n2:int)->int:
#     i=1
#     count=0
#     while i<=n1:
#         if i%n2==0:
#             count+=1
#         i+=1
#     return count
# n1=int(input("ENter n1:"))
# n2=int(input("ENter n2: "))
# print(divs(n1,n2))



# Q2. From 1 to 2000, print all the LEAP YEARS, using WHILE loop.

# i=1
# while i<=2000:
#     if (i%4==0 and i%100!=0) or (i%400==0):
#         print(i)
#     i+=1



# 3. Create a function named factorial which takes a integer as an input and
# returns the factorial of that number

# def factorial(num:int)->int:
#     result=1
#     i=1
#     while i<=num:
#      result*=i
#      i+=1
#     return result
# num=int(input("Enter the num:"))
# print(factorial(num))



# Q4. Create a function named pattern which takes an integer as an input
# and print the following pattern.
# testcase:
# pattern(4)
# output:: 10 20 30 40


# def pattern(n:int)->int:
#     i=1
#     while i<=n:
#         print(i*10,end=" ")
#         i+=1
# pattern(4)




# Q5. Create a function named pattern which takes an integer as an input
# and print the following pattern.
# testcase
# pattern(4)
# output: 1,2,4,8

# def pattern(n:int)->int:
#     i=1
#     num=1
#     while i<=n:
#         print(num,end=" ")
#         num=num*2
#         i+=1
# pattern(4)



# Q6. Don’t create a function, just print the following pattern
# 1 11 111 1111 11111....n times (Ask n from user)

# n=int(input("Enter value of n: "))
# i=1
# num=1
# while i<=n:
#     print(num,end=" ")
#     num=(num*10)+1
#     i+=1
    



# Q7. Keep asking numbers from user until the user enters 0. Then display
# the average of all numbers.

# total=0
# count=0
# while True:#here we can write 1==1 (for infi) i.e. True
#     n=int(input("Enter a number : "))
#     if n==0:
#         break 
#     total=total + n
#     count+=1
# print(f"the average  of the entered numners is : {total/count}")


# Q8. Write a function named pattern which accepts an integer n as an
# argument. Then print the following pattern

# output: 1,4,9,25


# def pattern(n:int):
#     i=1
#     while i<=n:
#         print(i**2,end=" ")
#         i+=1

# n=int(input("Enter the number: "))
# pattern(n)




# Q9. Ask a number from user. Print if that number is prime or not, use
# functions


# def isprime(n:int)->bool:
#     i=1
#     count=0
#     while i<=n:
#         if n%i==0:
#             count+=1
#         i+=1
#     if count ==2:
#         return True
#     return False
# n=int(input("Enter the number: "))
# print(isprime(n))

#or
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# # Test the function
# num = int(input("Enter a number : "))
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
    
    


# Q10. Ask a number from user n1. From 1 to n1, print how many prime
# numbers are there
n1=int(input("Enter the number: "))

i=1
count=0
while i<=n1:
    if i>=1:
        print("it is not a prime number ")
    elif i==2:
        print("it is a prime number  ")
    elif n1%i==0:
        count+=1
    if count==2:
        print()



   
