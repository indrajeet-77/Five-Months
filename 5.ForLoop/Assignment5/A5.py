# Q1. 2 22 222 2222 22222 ... upto n. (Ask n from user)

# n=int(input("Enter number: "))
# x=2
# for i in range (2,n+1):
#     x=(x*10)+2
#     print(x,end=" ")

    


# Q2. Write a program to display the n terms of a harmonic series and their
# sum.
# 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms

# n=int(input("Enter the number: "))
# x=0
# for i in range(1,n+1):
#     x= x+(1/i)
# print(x,end=" ")

# #or
# i: int = 1
# total: float = 0
# while i <= n:
#         total = total + (1 / i)
#         i += 1
# print(total)



# Q3. Ask x and n from user and then calculate the following answer.
# example 2
# pattern(x=6,n=4)

# 10.05...

# def pattern(x,n):
#     a=1
#     y=1
#     total=0
#     for i in range (a,n+1):
#         total=total+(x/y)
#         y+=2
    
#     return total
# print(pattern(x=6,n=4))




# Q4. Ask x and n from user and then calculate the following answer.

# def cal(x:int,n:int):
#     total=0
#     exp=1
#     flag=True
#     for i in range (1,n+1):
#         if flag==True:
#             total=total+(x**exp)
#             exp=exp+2
#             flag=False
#         else:
#             total=total-(x**exp)
#             exp=exp+2
#             flag=False
#     print(total)
# cal(9,11)

# or

# def patterSum(x: int, n: int) -> float:
#     total: float = 0
#     y: int = 1
#     for i in range(1, n+1):
#         if i % 2 != 0:
#             total = total + (x**y)
#         else:
#             total = total - (x**y)
#         y += 2
#     return total

# print(patterSum(6, 4))
# print(patterSum(9, 11))



# Q5. Create a function addDigits() that takes an integer as an argument.
# Calculate the sum of digits of that number.

# def addDigits(num:int):
#     result=0
#     i=num
#     while i>0:
        
#         result=result+(i%10)#i%10 gives the last digit
#         i=i//10#i//10 give the floor value
#     return result

# print(addDigits(123))
    


    
    
     
