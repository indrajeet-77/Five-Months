# You are given an integer 'n'. Return 'true' if 'n' is an Armstrong number, and 'false' otherwise.
# An Armstrong number is a number (with 'k' digits) such that the sum of its digits raised to 'kth' power is equal to the number itself. 
# For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.

def isams(n:int)->bool:
    org_n=n
    n1=str(n)
    k=len(n1)
    sum=0
    while n>0:
        lst=n%10
        sum+=lst**k
        n=n//10
    if org_n==sum:
        return True
    else:
        return False
print(isams(371))