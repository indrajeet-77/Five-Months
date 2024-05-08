import math
def countdig(x:int)->int:
    return int(math.log10(x))+1
x=1914
print(countdig(x))