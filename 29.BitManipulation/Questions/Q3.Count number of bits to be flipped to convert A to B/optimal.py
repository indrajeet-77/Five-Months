def minBitFlips(start: int, goal: int) -> int:
    count=0
    ans= start^goal
    for i in range(0,32):
            if ans&(1<<i):
                count+=1
    return count

x=10
y=7
print(minBitFlips(x,y))