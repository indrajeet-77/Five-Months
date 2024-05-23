# tc=O(2n)==O(N)
# sc=O(1)
# This is opttimal for only +ve elements

def largestSubarraywithSumK(arr:list,target)->int:
    k=target
    n=len(arr)
    right=0
    left=0
    Sum=0
    Maxlen=0
    while right<n:
        while left<=right and Sum>k:
            Sum-=arr[left]
            left+=1
        if Sum==k:
            Maxlen=max(Maxlen,right-left+1)
        right+=1
        if right<n:    
              Sum+=arr[right]
    return Maxlen
l=[1,1,2,3,1,2,1,1,1,1]
k=4
print(largestSubarraywithSumK(l,k))    