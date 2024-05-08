# You are given two integers 'n', and 'm'.
# Calculate 'gcd(n,m)', without using library functions.

def calcGCD(n:int,m:int)->int:
    if n>m:
        mn=n
    else:
        mn=m
    for i in range(1,mn+1):
        if(n%i==0) and (m%i==0):
            hcf=i
    return hcf

print(calcGCD(10,20))
        
        