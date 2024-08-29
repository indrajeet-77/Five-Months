def upperboud(nums,target):
    n=len(nums)
    low=0
    high=n-1
    upper_bound=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            upper_bound=mid
            high=mid-1
        elif nums[mid]<target:
            low=mid+1
    return upper_bound
x=[1,2,3,4,5,6,7,7,7,8,9,10]
print(upperboud(x,7))