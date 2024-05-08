# Sum of first N natural numbers without Loop

def sumOfNums(n:int):
    if n==0:
       return 0
    return n+sumOfNums(n-1)
x=10
print(sumOfNums(x))