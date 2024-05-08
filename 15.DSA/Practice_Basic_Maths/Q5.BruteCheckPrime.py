# Brute
#  Check prime
# A prime number is a positive integer that is divisible by exactly 2 integers, 1 and the number itself.
# You are given a number 'n'.
# Find out whether 'n' is prime or not.
# Example :
# Input: 'n' = 5
# Output: YES
# tc= O(n/2)
# sc=o(1)

def isprime(n:int)->bool:
    for i in range(2, int(n//2)+1):
        if n%i==0:
            return False
    return True

x=7
print(isprime(x))