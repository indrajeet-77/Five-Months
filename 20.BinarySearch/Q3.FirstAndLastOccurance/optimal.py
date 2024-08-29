# tc=O(2 log N)==O(log N)
# # sc=O(1)
def first(nums,target):
    first_time=-1
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            first_time=mid
            high=mid-1
        else:
            low=mid+1
    return first_time
def last(nums,target):
    n=len(nums)
    low=0
    high=n-1
    last_time=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            last_time=mid
            high=mid-1
        else:
            low=mid+1
    return last_time

def firstandlastoccurance(nums,target):
    f=first(nums,target)
    l=last(nums,target)
    return f,l-1


x=[1,2,3,3,3,4,5,6,6,6,7]
t=6
print(firstandlastoccurance(x,t))
