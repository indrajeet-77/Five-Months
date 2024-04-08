# Q1. Create a function named as checkPrime that takes an integer as an
# argument. Print YES if the number passed is a prime number else print NO.

# def checkprime(num:int)->str:
#     factor=0
#     i=1
#     while i<=num:
#         if num%i==0:
#             factor+=1
#         i+=1
#     if factor==2:
#         print("Yes")
#     else:
#         print("No")

# checkprime(2)

#OR

# def isprime(n:int):
#     count=0
#     if n<=1:
#         print("NO")
#     else:
#         for i in range(1,n+1):
#             if n%i==0:
#                 count+=1
#         if count==2:
#             print("yes")
#         else:
#             print("No")
# isprime(100)




# Q2. Print all the prime numbers between 1 to 100.

# def isprime(n:int):
#     count=0
#     if n<=1:
#         return False
#     else:
#         for i in range (1,n+1):
#             if n%i==0:
#                 count+=1
#         if count==2:
#             return True
#         return False

# def one_hun():
#     print("Prime numbers  from 1 to 100 are")
#     for i in range(1,101):
#         if isprime(i):
#             print(i,end=" ")
# one_hun()



# Q3. Create a function named sumNum(), which takes 2 parameters as n1
# and n2. Calculate and return the sum of all the numbers divisible by and 2
# and 7 between n1 to n2. Also if the sum is 0, then return -1.

# def sumNum(n1:int,n2:int):
#     sum=0
#     for i in range(n1,n2+1):
#         if i%2==0 and i%7==0:
#             sum=sum+i
#     if sum==0:
#         return -1
#     else:
#         return sum
# print(sumNum(1,30))




# Q4. Make a function named factorial(), which takes an integer n. Return the
# factorial of that number.

# def factorial(n:int):
#     fac=1
#     for i in range(1,n+1):
#         fac=fac*i
#     return fac
# print(factorial(5))



# Q5. Make a function named sumPattern that takes an integer n as an
# argument from the user. And then calculate the sum of the following
# pattern.

# def factorial1(n:int):
#     fac=1
#     for i in range(1,n+1):
#         fac=fac*i
#     return fac
# def pattern(n:int):

#     total=0
#     for i in range(1,n+1):
#         total=total+(1/factorial1(i))
#     return total
# print(pattern(5))




# Q6. Create a function named sumOfSquares, which takes a single integer
# as a parameter named n. Return the sum of squares from 1 to n.
# def sumOfSquares(n:int):
#     total=0
#     for i in range(1,n+1):
#         total=total+i**2
#     return total
# print(sumOfSquares(5))




# Q7. Create a function named as printPrimeFactors that takes an integer n
# as a argument and print all the prime factors of that number.
# Example if number = 20
# Then the factors of 20 are 1,2,5,10,20.
# So prime factors are 2,5 (this is the output)


def isprime(n:int):
    count=0
    if n<=1:
        return False
    else:
        for i in range (1,n+1):
            if n%i==0:
                count+=1
        if count==2:
            return True
        return False
    
def primefactors(n:int):
    for i in range(1,n+1):
        if n%i==0:
            if isprime(i):
                print(i,end=" ")

primefactors(20)


