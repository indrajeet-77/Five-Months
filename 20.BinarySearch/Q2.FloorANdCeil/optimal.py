# x=[1,2,3,4,4,4,4,5,5,6,7]
def floorceil(nums,target):
    floor=-1
    ceil=-1
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return [target,target]
        elif nums[mid]>target:
            ceil=mid
            high=mid-1
        else:# nums[mid]<target:
            floor=mid
            low=mid+1
    return [floor,ceil]
x=[1,2,3,4,5,7,8]
t=6
print(floorceil(x,t))