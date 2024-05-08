# def checkArmstrong(n):
#     or_n = n
#     num_digits = len(str(n))
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit ** num_digits
#         n //= 10
#     return sum == or_n

def printNtimes(n: int):
    if n<1:
        return
    print("Coding Ninjas")
    printNtimes(n-1)
    
x=4
printNtimes(x)



    