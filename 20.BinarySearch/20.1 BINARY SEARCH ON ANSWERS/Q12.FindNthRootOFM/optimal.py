def findNthsqrtOfM(n,m):
    low=1
    high=m
    while low<=high:
        mid=(low+high)//2
        if mid**n==m:
            return mid
        if mid**n>m:
            high=mid-1
        else:
            low=mid+1
    return -1
squareRootOF=125
Nth=3
print(findNthsqrtOfM(Nth,squareRootOF))
    