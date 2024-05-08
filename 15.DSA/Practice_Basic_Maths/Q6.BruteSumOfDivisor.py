#Brute_Force :- Sum of all divisors

# You are given an integer "n".
# Function sumOfDivisors(n) is defined as the sum of all divisors of 'n.
# Find the sum of sumOfDivisors(i) for all 'i' from 1 to 'n.
# Example:
# Input: 'n = 5
# Output: 21

def sumdivs(n:int)->int:
 sum=0
 for num in range(1,n+1):
    for i in range(1,int(num**0.5)+1):
         if num%i==0:
             sum+=i
             if num//i!=i:
                sum+=num//i
 return sum

x=5
print(sumdivs(x))



























import math
def sunOfDivisors(x:int)->int:
    sum=0
    for num in range (1,x+1):
        for i in  range(1,int(math.sqrt(num))+1):
            if num%i==0:
                sum+=i
                if num//i !=i:
                    sum+=num//i
    return sum
x=5
print(sunOfDivisors(x))
                    

