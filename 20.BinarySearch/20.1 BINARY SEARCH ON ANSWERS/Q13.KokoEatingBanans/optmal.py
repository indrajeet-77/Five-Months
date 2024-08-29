
# Tc=O(N)+O(log(maxofpiles)*N)
# sc=O(1)
import math
def totalhours(piles,hourlyrate):
    total=0
    for i in range(len(piles)):
        total+=math.ceil(piles[i]/hourlyrate)
    return total
def kokoEatingbananas(piles,h):
    low=1
    high=max(piles)#tc=O(N)
    while low<=high:
        mid=(low+high)//2
        th=totalhours(piles,mid)
        if th<h:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
x=[3,4,7,11]
h=8
print(kokoEatingbananas(x,h))