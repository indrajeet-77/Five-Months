# we use kadan's algo here
def maxsumUsingKadansalgo(arr:list):
    n=len(arr)
    maxi=0
    Sum=0
    for i in range(0,n):
        Sum+=arr[i]
        maxi=max(maxi,Sum)
        if Sum<0:
            Sum=0
        return maxi
x=[-1,5,6,-6,9,10,2]
print(maxsumUsingKadansalgo(x))
        