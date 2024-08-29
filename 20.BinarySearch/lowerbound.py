
def lowerboud(nums,target):
    n=len(nums)
    low=0
    high=n-1
    lower_bound=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lower_bound=mid
            high=mid-1
        elif nums[mid]<target:
            low=mid+1
    return lower_bound
#  0 1 2 3 4 5 6 7 8 9 10 11 
x=[1,2,3,4,5,6,7,7,7,8,9,10]
print(lowerboud(x,10))
            