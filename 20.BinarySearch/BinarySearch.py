def binarysearch(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if  nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high=mid-1
        elif nums[mid]<target:
            low=mid+1
    return -1
arr=[1,2,3,4,5,6,7,8,9,10]
t=9
print(binarysearch(arr,t))