# tc=O(log N)
# sc=O(1)
def findminimum(nums):
    n=len(nums)
    low=0
    high=n-1
    minimum=float('inf')
    while low<=high:
        mid=(low+high)//2
        if nums[low]<=nums[mid]:
            minimum=min(minimum,nums[low])
            low=mid+1
        else:
            minimum=min(minimum,nums[mid])
            high=mid-1
    return minimum
x=[7,8,9,1,2,3,7]
print(findminimum(x))