import math 
def totalhours(piles,hourlyrate):
    total=0
    for i in range(len(piles)):
        total+=math.ceil(piles[i]/hourlyrate)
    return total
def cocoEatingBananas(piles,h):
    for i in range(1,max(piles)+1):
        th=totalhours(piles,i)
        if th<=h:
            return i
x=[3,6,7,11]
h = 8
print(cocoEatingBananas(x,h))


  