# Q1. Make a function named reverse which accepts an integer n from the
# user. Reverse the number passed as a parameter and return the reverse
# number. Do not use STRINGS.


# def rev(n:int):
#     result=0
#     while n>0:
#         ld =n%10
#         result=( result*10)+ld
#         n=n//10
#     return result




# Q2. Make a function named checkPalindrome which accepts an integer n
# from the user. Return True or False if the number is palindrome or not

# def rev(n:int):
#     result=0
#     while n>0:
#         ld =n%10
#         result=( result*10)+ld
#         n=n//10
#     return result

# def check_palindrome(a:int):
#     if rev(a)==a:
#         return True
#     return False

# print(check_palindrome(1991))
        



# Q3. Make a function named printWords which accepts an integer n from
# the user. Print the number as words

# def rev(n:int):
#     result=0
#     while n>0:
#         ld =n%10
#         result=( result*10)+ld
#         n=n//10
#     return result

# def printWords(n:int):
#     reversed_num=rev(n)
#     while reversed_num>0:
#         ld=reversed_num%10
#         if ld==0:
#             print("Zero",end=" ")
#         elif ld==1:
#             print("One",end=" ")
#         elif ld==2:
#             print("Two",end=" ")
#         elif ld==3:
#             print("Three",end=" ")
#         elif ld==4:
#             print("Four",end=" ")
#         elif ld==5:
#             print("Five",end=" ")
#         elif ld==6:
#             print("Six",end=" ")
#         elif ld==7:
#             print("Seven",end=" ")
#         elif ld==8:
#             print("Eight",end=" ")
#         elif ld==9:
#             print("Nine,",end=" ")
#         reversed_num=reversed_num//10

# printWords(992299)




# Q4. Make a function named checkArmstrong which accepts an integer n
# from the user. Return True or False if that number is an armstrong number

# def amst(n:int):
#     res=0
#     while n>0:
#         ld=n%10
#         res=res+ld**3
#         n=n//10
#     return res
# def checkamstrong(n:int):
#     if amst(n)==n:
#         return True
#     return False

# print(checkamstrong(407))




# Q5. Make a function named sumOfFirstAndLastDigit which accepts an
# integer n from the user. Calculate the sum of first and last digit of a
# number and return it

def Sum_of_first_and_last(n:int)
    sum=0
    while n>0:
        ld =n%10