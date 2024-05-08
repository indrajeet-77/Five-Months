# #Optimal
# Problem statement
# Given an integer 'N', your task is to write a program that returns all the divisors of ‘N’ in ascending order.
# For example:
# 'N' = 5.
# The divisors of 5 are 1, 5.
# # tc=O(N)
# # sc=O(1)

def printDivisors(n: int) ->list[int]:
    # l1=[]
    return [ i for i in range(1,n//2+1) if n%i==0 if n//i!=i]
n=20
print(printDivisors(n))