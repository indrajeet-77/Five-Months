def searchinsertionposition(nums,target):
    n=len(nums)
    low =0
    high =n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

x=[1,2,3,5]
t=4
print(searchinsertionposition(x,t))