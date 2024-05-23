# TC
# SC

def twosum(arr,target):
    n=len(arr)
    hashdict=dict()
    for i in range(0,n):
        rem=target-arr[i]
        if rem in hashdict:
            return [hashdict[rem],i]
        hashdict[arr[i]]=i
x=[1,2,3,4,6]
t=10
print(twosum(x,t))
            
        