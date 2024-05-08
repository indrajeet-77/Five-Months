#Sum of all divisors optimal
# TC=
# SC=O(1)
def sumdivs(n:int)->int:
    sum=0
    for i in range(1,n+1):
        sum=sum+i*(n//i)
    return sum

x=5
print(sumdivs(x))