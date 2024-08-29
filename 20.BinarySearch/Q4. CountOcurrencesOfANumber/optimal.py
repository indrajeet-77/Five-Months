# 6. Binary Search/Medium/1. Number of occurrence/optimal.py

def lowerbound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    lb=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
def upperbound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ub=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub
def countOcurranceOfANumber(nums,target):
    return upperbound(nums,target)-lowerbound(nums,target)
            
            
x=[1,2,3,3,3,4,5,6,6,6,6,6,6,6,7]
t=6
print(f"Ocurrance of {t} is",countOcurranceOfANumber(x,t),"times")

            
            
    