def maximumsubarraysum(arr:list):
    n=len(arr)
    maxsum=float('-inf')
    for i in range(0,n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            maxsum=max(sum,maxsum)
    return maxsum
x=[-2,1,-3,4,-1,2,1,-5,4]
print(maximumsubarraysum(x))
        
        