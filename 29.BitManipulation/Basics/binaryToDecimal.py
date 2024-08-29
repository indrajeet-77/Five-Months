# TC=O(n) ,n==len(s)
# SC=O(1)
def binaryToDecimal(s:str)->int:
    n=len(s)
    total=0
    power=1
    for i in range(n-1,-1,-1):
        if s[i]=='1':
            total+=power
        power=power*2
    return total
x='1010'
print(binaryToDecimal(x))